from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .engine import LightCubeEngine
from .models import RunMode, RunRequest
from .renderers import decision_pack_markdown
from .utils import ensure_run_dir, save_json, slugify

app = FastAPI(title="LightCube v1")
app.mount("/static", StaticFiles(directory=str(Path(__file__).parent / "static")), name="static")
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))
engine = LightCubeEngine()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/run", response_class=HTMLResponse)
async def run_workflow(
    request: Request,
    project_name: str = Form(...),
    mode: str = Form(...),
    url: str = Form(""),
    idea: str = Form(""),
    context: str = Form(""),
) -> HTMLResponse:
    parsed = RunRequest(
        project_name=project_name,
        mode=RunMode(mode),
        url=url or None,
        idea=idea or None,
        context=context or None,
    )
    pack, paperclip_export = await engine.run(parsed)
    run_dir = ensure_run_dir(parsed.project_name, pack.run_id)
    save_json(run_dir / "decision-pack.json", pack.model_dump())
    save_json(run_dir / "paperclip-tasks.json", paperclip_export)
    save_json(run_dir / "meta.json", {"project": parsed.project_name, "mode": parsed.mode.value, "slug": slugify(parsed.project_name)})
    (run_dir / "decision-pack.md").write_text(decision_pack_markdown(pack), encoding="utf-8")
    return templates.TemplateResponse("result.html", {"request": request, "pack": pack, "run_dir": str(run_dir)})


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/runs/{project_slug}/{run_id}", response_class=HTMLResponse)
async def view_run(request: Request, project_slug: str, run_id: str) -> HTMLResponse:
    run_dir = Path(__file__).resolve().parent.parent / "storage" / "projects" / project_slug / run_id
    if not run_dir.exists():
        return HTMLResponse("Run not found", status_code=404)
    content = (run_dir / "decision-pack.md").read_text(encoding="utf-8")
    return templates.TemplateResponse("stored_run.html", {"request": request, "content": content, "run_dir": str(run_dir)})


@app.get("/latest")
async def latest() -> RedirectResponse:
    root = Path(__file__).resolve().parent.parent / "storage" / "projects"
    runs = sorted(root.glob("*/*"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not runs:
        return RedirectResponse(url="/")
    run = runs[0]
    return RedirectResponse(url=f"/runs/{run.parent.name}/{run.name}")
