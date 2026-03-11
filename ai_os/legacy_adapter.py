from __future__ import annotations

from pathlib import Path

from .contracts import PaperclipRunRequest, TaskEnvelope
from .fs_utils import ensure_dir, slugify, write_json


def legacy_task_name(envelope: TaskEnvelope) -> str:
    return slugify(f"{envelope.initiative_id}-{envelope.epic_id}-{envelope.task_id}")


def legacy_task_filename(envelope: TaskEnvelope) -> str:
    return f"{legacy_task_name(envelope)}.md"


def legacy_task_path(envelope: TaskEnvelope, repo_root: Path, state: str = "pending") -> Path:
    return repo_root / "ops/tasks" / state / legacy_task_filename(envelope)


def envelope_to_markdown(envelope: TaskEnvelope) -> str:
    low = "x" if envelope.priority == "low" else " "
    medium = "x" if envelope.priority == "medium" else " "
    high = "x" if envelope.priority == "high" else " "
    steps = "\n".join(f"{idx}. {step}" for idx, step in enumerate(envelope.steps, start=1))
    expected = "\n".join(f"- {item}" for item in envelope.acceptance_criteria)
    constraints = "\n".join(f"- {item}" for item in envelope.constraints)
    evidence = "\n".join(f"- {ref.path}" for ref in envelope.evidence_refs)

    return f"""# Task: {envelope.title}

## Objective
{envelope.objective}

## Steps
{steps or "1. Review the linked context bundle"}

## Expected Output
{expected or "- Complete the task and write the execution report"}

## Priority
- [{low}] Low
- [{medium}] Medium
- [{high}] High

## Metadata
- goal_id: {envelope.goal_id}
- initiative_id: {envelope.initiative_id}
- epic_id: {envelope.epic_id}
- task_id: {envelope.task_id}
- executor_type: {envelope.executor_type}
- budget_cap: {envelope.budget_cap}
- approval_required: {str(envelope.approval_required).lower()}
- context_bundle_ref: {envelope.context_bundle_ref}
- artifact_output_path: {envelope.artifact_output_path}

## Constraints
{constraints or "- No extra constraints supplied"}

## Evidence Refs
{evidence or "- No evidence refs supplied"}
"""


def queue_legacy_task(envelope: TaskEnvelope, repo_root: Path) -> Path:
    pending_dir = ensure_dir(repo_root / "ops/tasks/pending")
    task_path = pending_dir / legacy_task_filename(envelope)
    task_path.write_text(envelope_to_markdown(envelope), encoding="utf-8")
    return task_path


def build_paperclip_run_request(
    envelope: TaskEnvelope,
    company_id: str,
) -> PaperclipRunRequest:
    return PaperclipRunRequest(
        request_id=envelope.envelope_id,
        company_id=company_id,
        goal_id=envelope.goal_id,
        initiative_id=envelope.initiative_id,
        epic_id=envelope.epic_id,
        task_id=envelope.task_id,
        title=envelope.title,
        summary=envelope.objective,
        executor_type=envelope.executor_type,
        budget_cap=envelope.budget_cap,
        approval_required=envelope.approval_required,
        context_bundle_ref=envelope.context_bundle_ref,
        artifact_output_path=envelope.artifact_output_path,
        metadata={
            "initiative_title": envelope.initiative_title,
            "priority": envelope.priority,
        },
    )


def queue_paperclip_request(
    request: PaperclipRunRequest,
    repo_root: Path,
) -> Path:
    outbox_dir = ensure_dir(repo_root / "ops/paperclip/outbox")
    return write_json(
        outbox_dir / f"{request.request_id}.json",
        request.model_dump(mode="json"),
    )
