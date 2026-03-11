from __future__ import annotations

from datetime import datetime, timezone

from pathlib import Path

import requests
from pydantic import BaseModel

from .contracts import ApprovalRecord, ApprovalStatus, DiscordEvent, DiscordEventType, TaskEnvelope
from .fs_utils import ensure_dir, to_repo_path, write_json


def event_from_blocked(
    task_id: str,
    title: str,
    blocker_type: str,
    description: str,
    task_envelope_ref: str | None = None,
) -> DiscordEvent:
    """Create a run_blocked Discord event."""
    return DiscordEvent(
        event_id=f"blocked__{task_id}",
        event_type=DiscordEventType.run_blocked,
        title=f"Task Blocked: {title}",
        summary=description,
        task_envelope_ref=task_envelope_ref,
        metadata={
            "blocker_type": blocker_type,
            "blocked_at": datetime.now(timezone.utc).isoformat(),
        },
    )


def event_from_completion(
    task_id: str,
    title: str,
    status: str,
    summary: str,
    duration: str | None = None,
    task_envelope_ref: str | None = None,
) -> DiscordEvent:
    """Create a run_completed Discord event."""
    metadata = {"status": status}
    if duration:
        metadata["duration"] = duration
    return DiscordEvent(
        event_id=f"completed__{task_id}",
        event_type=DiscordEventType.run_completed,
        title=f"Task {status.title()}: {title}",
        summary=summary,
        task_envelope_ref=task_envelope_ref,
        metadata=metadata,
    )


def event_from_budget(
    initiative_id: str,
    current_spend: float,
    budget_cap: float,
    remaining_tasks: int = 0,
    task_envelope_ref: str | None = None,
) -> DiscordEvent:
    """Create a budget_threshold_hit Discord event."""
    utilization = (current_spend / budget_cap * 100) if budget_cap > 0 else 0
    action = "approve_overbudget" if utilization >= 95 else "none"

    return DiscordEvent(
        event_id=f"budget__{initiative_id}",
        event_type=DiscordEventType.budget_threshold_hit,
        title=f"Budget Alert: {initiative_id}",
        summary=f"Current spend: ${current_spend:.2f} / ${budget_cap:.2f} ({utilization:.1f}%)",
        task_envelope_ref=task_envelope_ref,
        metadata={
            "current_spend": str(current_spend),
            "budget_cap": str(budget_cap),
            "utilization": f"{utilization:.1f}%",
            "remaining_tasks": str(remaining_tasks),
            "action_required": action,
        },
    )


class DiscordDeliveryResult(BaseModel):
    delivered: bool
    mode: str
    event_path: str


def create_approval_request(envelope: TaskEnvelope, repo_root: Path) -> ApprovalRecord:
    approval = ApprovalRecord(
        approval_id=f"approval__{envelope.envelope_id}",
        title=f"Approval needed: {envelope.title}",
        summary=envelope.objective,
        task_envelope_ref=to_repo_path(
            repo_root / "ops/tasks/compiled" / f"{envelope.envelope_id}.json",
            repo_root,
        ),
    )
    approval_path = ensure_dir(repo_root / "ops/approvals/pending") / f"{approval.approval_id}.json"
    write_json(approval_path, approval.model_dump(mode="json"))
    return approval


def resolve_approval_request(
    approval_id: str,
    status: ApprovalStatus,
    actor: str,
    notes: str,
    repo_root: Path,
) -> Path:
    pending_path = repo_root / "ops/approvals/pending" / f"{approval_id}.json"
    if not pending_path.exists():
        raise FileNotFoundError(f"Approval request not found: {approval_id}")

    approval = ApprovalRecord.model_validate_json(pending_path.read_text(encoding="utf-8"))
    approval.status = status
    approval.decided_by = actor
    approval.notes = notes

    target_dir = ensure_dir(repo_root / "ops/approvals" / status.value)
    target_path = target_dir / pending_path.name
    write_json(target_path, approval.model_dump(mode="json"))
    pending_path.unlink()
    return target_path


def event_from_approval(approval: ApprovalRecord) -> DiscordEvent:
    return DiscordEvent(
        event_id=approval.approval_id,
        event_type=DiscordEventType.approval_requested,
        title=approval.title,
        summary=approval.summary,
        approval_id=approval.approval_id,
        task_envelope_ref=approval.task_envelope_ref,
    )


def format_discord_message(event: DiscordEvent) -> str:
    lines = [f"**{event.event_type.value.replace('_', ' ').title()}**", f"**{event.title}**", event.summary]
    if event.approval_id:
        lines.append(f"approval_id: `{event.approval_id}`")
    if event.task_envelope_ref:
        lines.append(f"task: `{event.task_envelope_ref}`")
    for key, value in event.metadata.items():
        lines.append(f"{key}: `{value}`")

    # Add action buttons for approval requests
    if event.event_type == DiscordEventType.approval_requested:
        lines.append("\n**Actions:** 👍 Approve | 👎 Reject | ❓ Request Info")

    # Add action for budget alerts at critical threshold
    if event.event_type == DiscordEventType.budget_threshold_hit:
        util = event.metadata.get("utilization", "0%")
        if float(util.rstrip("%")) >= 95:
            lines.append("\n**Actions:** ⚠️ Approve Overbudget | 🛑 Stop Initiative")

    return "\n".join(lines)


def emit_event(
    event: DiscordEvent,
    repo_root: Path,
    bot_token: str | None = None,
    channel_id: str | None = None,
) -> DiscordDeliveryResult:
    outbox_dir = ensure_dir(repo_root / "ops/discord/outbox")
    event_path = write_json(
        outbox_dir / f"{event.event_id}.json",
        event.model_dump(mode="json"),
    )

    if not bot_token or not channel_id:
        return DiscordDeliveryResult(
            delivered=False,
            mode="dry_run",
            event_path=str(event_path),
        )

    response = requests.post(
        f"https://discord.com/api/v10/channels/{channel_id}/messages",
        headers={
            "Authorization": f"Bot {bot_token}",
            "Content-Type": "application/json",
        },
        json={"content": format_discord_message(event)},
        timeout=20,
    )
    response.raise_for_status()
    return DiscordDeliveryResult(
        delivered=True,
        mode="discord_api",
        event_path=str(event_path),
    )
