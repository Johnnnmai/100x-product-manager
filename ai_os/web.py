from __future__ import annotations

import os
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from .config import load_settings
from .contracts import ApprovalStatus
from .discord_bridge import resolve_approval_request
from .ops_state import list_approvals, list_reports, summarize_status
from .order_flow import dispatch_order


class DispatchRequest(BaseModel):
    input_path: str
    task_id: str | None = None
    company_id: str | None = None


class ResolveApprovalRequest(BaseModel):
    approval_id: str
    status: str
    actor: str
    notes: str = ""


def _console_html() -> str:
    return """<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>AI OS Control Console</title>
  <style>
    :root {
      --ink: #15211d;
      --panel: rgba(255, 250, 240, 0.92);
      --line: #d6c8af;
      --accent: #0f766e;
      --accent-2: #b45309;
      --muted: #55615d;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: "Georgia", "Songti SC", serif;
      color: var(--ink);
      background:
        radial-gradient(circle at top left, rgba(180, 83, 9, 0.12), transparent 28%),
        radial-gradient(circle at bottom right, rgba(15, 118, 110, 0.14), transparent 32%),
        linear-gradient(135deg, #f7f3eb 0%, #efe6d6 100%);
      min-height: 100vh;
    }
    .shell {
      max-width: 1240px;
      margin: 0 auto;
      padding: 28px;
    }
    .hero, .layout {
      display: grid;
      gap: 20px;
      margin-bottom: 20px;
    }
    .hero { grid-template-columns: 1.3fr 1fr; }
    .layout { grid-template-columns: 1.1fr 0.9fr; }
    .card {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 22px;
      box-shadow: 0 18px 45px rgba(21, 33, 29, 0.08);
      padding: 22px;
      backdrop-filter: blur(10px);
    }
    h1, h2, h3, button {
      font-family: "Trebuchet MS", "Microsoft YaHei", sans-serif;
      letter-spacing: 0.02em;
    }
    h1 {
      font-size: clamp(32px, 5vw, 58px);
      line-height: 0.95;
      margin: 0 0 12px;
    }
    .hero p, .meta {
      color: var(--muted);
      font-size: 15px;
      line-height: 1.6;
      margin: 0;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 14px;
      margin-top: 18px;
    }
    .metric {
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 16px;
      background: rgba(255, 255, 255, 0.55);
    }
    .label {
      font-size: 12px;
      text-transform: uppercase;
      color: var(--muted);
      letter-spacing: 0.08em;
    }
    .value {
      margin-top: 6px;
      font-size: 30px;
      font-weight: 700;
    }
    .field { margin-bottom: 14px; }
    label {
      display: block;
      font-size: 13px;
      margin-bottom: 8px;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }
    input, textarea {
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 12px 14px;
      font: inherit;
      background: rgba(255, 255, 255, 0.84);
      color: var(--ink);
    }
    textarea { min-height: 92px; resize: vertical; }
    .actions {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }
    button {
      border: 0;
      border-radius: 999px;
      padding: 12px 18px;
      color: white;
      cursor: pointer;
      background: linear-gradient(120deg, var(--accent), #115e59);
      box-shadow: 0 10px 24px rgba(15, 118, 110, 0.25);
      transition: transform 0.18s ease;
    }
    button.secondary {
      background: linear-gradient(120deg, var(--accent-2), #92400e);
      box-shadow: 0 10px 24px rgba(180, 83, 9, 0.24);
    }
    button:hover { transform: translateY(-1px); }
    pre {
      margin: 0;
      padding: 14px;
      border-radius: 18px;
      background: #1b2722;
      color: #f7f7f2;
      overflow: auto;
      font-size: 12px;
      min-height: 180px;
    }
    .list {
      display: grid;
      gap: 10px;
    }
    .item {
      border: 1px solid var(--line);
      border-radius: 16px;
      padding: 14px;
      background: rgba(255, 255, 255, 0.55);
    }
    .item-title {
      font-family: "Trebuchet MS", "Microsoft YaHei", sans-serif;
      font-size: 15px;
      margin-bottom: 6px;
    }
    .pill {
      display: inline-block;
      border-radius: 999px;
      padding: 4px 10px;
      font-size: 11px;
      margin-bottom: 8px;
      color: white;
      background: #334155;
    }
    .pill.pending { background: #b45309; }
    .pill.approved { background: #0f766e; }
    .pill.rejected { background: #b91c1c; }
    .muted-break {
      color: var(--muted);
      font-size: 13px;
      line-height: 1.5;
      word-break: break-all;
    }
    @media (max-width: 980px) {
      .hero, .layout { grid-template-columns: 1fr; }
      .grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    }
  </style>
</head>
<body>
  <div class="shell">
    <section class="hero">
      <div class="card">
        <h1>AI OS Control Console</h1>
        <p>一个页面完成发令、审批和状态查看。Paperclip 继续做控制面，OpenClaw 继续做真实云端执行，本页只把它们连起来。</p>
        <div class="grid" id="metrics"></div>
      </div>
      <div class="card">
        <h2>当前闭环</h2>
        <p>发令后会同时生成 compiled envelope、legacy pending task、Paperclip request。需要审批时，还会把事件发到 Discord 或 dry-run outbox。</p>
      </div>
    </section>

    <section class="layout">
      <div class="card">
        <h2>发号施令</h2>
        <div class="field">
          <label for="inputPath">PM Spec 路径</label>
          <input id="inputPath" value="examples/pm_spec.yaml" />
        </div>
        <div class="field">
          <label for="taskId">Task ID</label>
          <input id="taskId" value="signup-dropoff-audit" />
        </div>
        <div class="field">
          <label for="companyId">Paperclip Company ID</label>
          <input id="companyId" placeholder="留空则使用环境变量" />
        </div>
        <div class="actions">
          <button id="dispatchBtn">下发任务</button>
          <button class="secondary" id="refreshBtn">刷新状态</button>
        </div>
        <h3>结果</h3>
        <pre id="dispatchResult">等待操作...</pre>
      </div>

      <div class="card">
        <h2>审批处理</h2>
        <div class="field">
          <label for="actor">审批人</label>
          <input id="actor" value="owner" />
        </div>
        <div class="field">
          <label for="notes">备注</label>
          <textarea id="notes">approved from web console</textarea>
        </div>
        <div class="actions">
          <button id="approveBtn">批准首个待审批</button>
        </div>
        <h3>最近审批</h3>
        <div class="list" id="approvals"></div>
      </div>
    </section>

    <section class="layout">
      <div class="card">
        <h2>最近报告</h2>
        <div class="list" id="reports"></div>
      </div>
      <div class="card">
        <h2>执行说明</h2>
        <p class="meta">
          如果 `pending_tasks` 增加，说明任务已经进入真实执行队列。<br />
          如果你的云端 OpenClaw 正在轮询这个仓库，它会继续把任务移动到 `running` 和 `done`，并把报告写回 `ops/reports/`。
        </p>
      </div>
    </section>
  </div>
  <script>
    const metrics = document.getElementById("metrics");
    const approvals = document.getElementById("approvals");
    const reports = document.getElementById("reports");
    const dispatchResult = document.getElementById("dispatchResult");

    async function loadStatus() {
      const [statusRes, approvalsRes, reportsRes] = await Promise.all([
        fetch("/api/status"),
        fetch("/api/approvals"),
        fetch("/api/reports")
      ]);
      const status = await statusRes.json();
      const approvalItems = await approvalsRes.json();
      const reportItems = await reportsRes.json();

      metrics.innerHTML = Object.entries(status).map(([key, value]) => `
        <div class="metric">
          <div class="label">${key.replaceAll("_", " ")}</div>
          <div class="value">${value}</div>
        </div>
      `).join("");

      approvals.innerHTML = approvalItems.length ? approvalItems.map((item) => `
        <div class="item">
          <div class="pill ${item.status}">${item.status}</div>
          <div class="item-title">${item.title}</div>
          <div class="muted-break">${item.approval_id}</div>
          <div class="muted-break">${item.summary}</div>
        </div>
      `).join("") : `<div class="item"><div class="muted-break">当前没有审批记录。</div></div>`;

      reports.innerHTML = reportItems.length ? reportItems.map((item) => `
        <div class="item">
          <div class="item-title">${item.name}</div>
          <div class="muted-break">${item.path}</div>
        </div>
      `).join("") : `<div class="item"><div class="muted-break">当前没有执行报告。</div></div>`;
    }

    document.getElementById("dispatchBtn").addEventListener("click", async () => {
      const payload = {
        input_path: document.getElementById("inputPath").value,
        task_id: document.getElementById("taskId").value || null,
        company_id: document.getElementById("companyId").value || null
      };
      const res = await fetch("/api/dispatch", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      dispatchResult.textContent = JSON.stringify(data, null, 2);
      await loadStatus();
    });

    document.getElementById("approveBtn").addEventListener("click", async () => {
      const approvalsRes = await fetch("/api/approvals");
      const approvalItems = await approvalsRes.json();
      const target = approvalItems.find((item) => item.status === "pending");
      if (!target) {
        dispatchResult.textContent = "没有待审批任务。";
        return;
      }
      const payload = {
        approval_id: target.approval_id,
        status: "approved",
        actor: document.getElementById("actor").value || "owner",
        notes: document.getElementById("notes").value || ""
      };
      const res = await fetch("/api/resolve-approval", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      dispatchResult.textContent = JSON.stringify(data, null, 2);
      await loadStatus();
    });

    document.getElementById("refreshBtn").addEventListener("click", loadStatus);
    loadStatus();
  </script>
</body>
</html>"""


def create_app(repo_root: Path | None = None) -> FastAPI:
    resolved_root = (repo_root or Path(os.getenv("AI_OS_REPO_ROOT", "."))).resolve()
    settings = load_settings(resolved_root)
    web_app = FastAPI(title="AI OS Control Console")

    @web_app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @web_app.get("/api/status")
    def api_status() -> dict[str, int]:
        return summarize_status(resolved_root)

    @web_app.get("/api/approvals")
    def api_approvals() -> list[dict[str, str]]:
        return list_approvals(resolved_root)

    @web_app.get("/api/reports")
    def api_reports() -> list[dict[str, str]]:
        return list_reports(resolved_root)

    @web_app.post("/api/dispatch")
    def api_dispatch(payload: DispatchRequest) -> dict[str, str | None]:
        pm_spec_path = (resolved_root / payload.input_path).resolve()
        if not pm_spec_path.exists():
            raise HTTPException(status_code=404, detail=f"PM spec not found: {payload.input_path}")

        result = dispatch_order(
            pm_spec_path=pm_spec_path,
            repo_root=resolved_root,
            company_id=payload.company_id or settings.paperclip_company_id,
            task_id=payload.task_id,
            discord_bot_token=settings.discord_bot_token,
            discord_channel_id=settings.discord_channel_id,
        )
        return result.model_dump(mode="json")

    @web_app.post("/api/resolve-approval")
    def api_resolve_approval(payload: ResolveApprovalRequest) -> dict[str, str]:
        try:
            path = resolve_approval_request(
                approval_id=payload.approval_id,
                status=ApprovalStatus(payload.status),
                actor=payload.actor,
                notes=payload.notes,
                repo_root=resolved_root,
            )
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc

        return {"path": str(path)}

    @web_app.get("/", response_class=HTMLResponse)
    def console() -> str:
        return _console_html()

    return web_app


app = create_app()
