from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel

from .contracts import TaskEnvelope
from .discord_bridge import create_approval_request, emit_event, event_from_approval
from .legacy_adapter import build_paperclip_run_request, queue_legacy_task, queue_paperclip_request
from .pm_compiler import compile_pm_spec, load_pm_spec


class DispatchResult(BaseModel):
    envelope_path: str
    legacy_task_path: str
    paperclip_request_path: str
    approval_id: str | None = None
    discord_event_path: str | None = None
    discord_delivery_mode: str | None = None


def _load_selected_envelope(envelope_paths: list[str], task_id: str | None) -> tuple[TaskEnvelope, str]:
    selected_path: str | None = None
    for path in envelope_paths:
        envelope = TaskEnvelope.model_validate_json(Path(path).read_text(encoding="utf-8"))
        if task_id is None or envelope.task_id == task_id or envelope.envelope_id == task_id:
            selected_path = path
            return envelope, selected_path
    raise ValueError(f"No compiled task matched task_id={task_id!r}")


def dispatch_order(
    pm_spec_path: Path,
    repo_root: Path,
    company_id: str,
    task_id: str | None = None,
    discord_bot_token: str | None = None,
    discord_channel_id: str | None = None,
) -> DispatchResult:
    compile_result = compile_pm_spec(load_pm_spec(pm_spec_path), repo_root)
    envelope, envelope_path = _load_selected_envelope(compile_result.envelope_paths, task_id)

    legacy_task_path = queue_legacy_task(envelope, repo_root)
    paperclip_request_path = queue_paperclip_request(
        build_paperclip_run_request(envelope, company_id),
        repo_root,
    )

    result = DispatchResult(
        envelope_path=envelope_path,
        legacy_task_path=str(legacy_task_path),
        paperclip_request_path=str(paperclip_request_path),
    )

    if envelope.approval_required:
        approval = create_approval_request(envelope, repo_root)
        delivery = emit_event(
            event_from_approval(approval),
            repo_root,
            discord_bot_token,
            discord_channel_id,
        )
        result.approval_id = approval.approval_id
        result.discord_event_path = delivery.event_path
        result.discord_delivery_mode = delivery.mode

    return result
