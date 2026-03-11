from __future__ import annotations

from pathlib import Path

from .contracts import ApprovalRecord


TRACKED_DIRS = {
    "compiled_tasks": "ops/tasks/compiled",
    "pending_tasks": "ops/tasks/pending",
    "running_tasks": "ops/tasks/running",
    "done_tasks": "ops/tasks/done",
    "reports": "ops/reports",
    "paperclip_outbox": "ops/paperclip/outbox",
    "discord_outbox": "ops/discord/outbox",
    "approvals_pending": "ops/approvals/pending",
    "approvals_approved": "ops/approvals/approved",
    "approvals_rejected": "ops/approvals/rejected",
    "context_bundles": "ops/context_bundles",
    "evidence_processed": "ops/evidence/processed",
    "strategy_reports": "ops/strategy_lab/reports",
}


def summarize_status(repo_root: Path) -> dict[str, int]:
    summary: dict[str, int] = {}
    for key, relative_path in TRACKED_DIRS.items():
        path = repo_root / relative_path
        if not path.exists():
            summary[key] = 0
            continue
        summary[key] = sum(1 for item in path.iterdir() if item.is_file() and item.name != ".gitkeep")
    return summary


def list_approvals(repo_root: Path, limit: int = 50) -> list[dict[str, str]]:
    records: list[tuple[float, dict[str, str]]] = []
    for status in ("pending", "approved", "rejected"):
        approval_dir = repo_root / "ops/approvals" / status
        if not approval_dir.exists():
            continue
        for path in approval_dir.glob("*.json"):
            record = ApprovalRecord.model_validate_json(path.read_text(encoding="utf-8"))
            records.append(
                (
                    path.stat().st_mtime,
                    {
                        "approval_id": record.approval_id,
                        "status": record.status.value,
                        "title": record.title,
                        "summary": record.summary,
                        "task_envelope_ref": record.task_envelope_ref,
                        "decided_by": record.decided_by or "",
                        "notes": record.notes or "",
                    },
                )
            )
    records.sort(key=lambda item: item[0], reverse=True)
    return [payload for _, payload in records[:limit]]


def list_reports(repo_root: Path, limit: int = 20) -> list[dict[str, str]]:
    reports_dir = repo_root / "ops/reports"
    if not reports_dir.exists():
        return []
    payloads: list[tuple[float, dict[str, str]]] = []
    for path in reports_dir.glob("*"):
        if not path.is_file() or path.name == ".gitkeep":
            continue
        payloads.append(
            (
                path.stat().st_mtime,
                {
                    "name": path.name,
                    "path": str(path),
                },
            )
        )
    payloads.sort(key=lambda item: item[0], reverse=True)
    return [payload for _, payload in payloads[:limit]]
