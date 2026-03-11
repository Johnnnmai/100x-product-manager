from __future__ import annotations

import json
import os
import subprocess
import tempfile
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Callable, Literal
from functools import lru_cache

from pydantic import BaseModel, Field

from .agent_fleet import ResolvedAgent, resolve_fleet
from .contracts import ApprovalStatus, ExecutorType, TaskEnvelope
from .discord_bridge import ApprovalRecord
from .fs_utils import ensure_dir, slugify, write_json
from .legacy_adapter import legacy_task_path


# Fleet resolution cache to avoid repeated YAML parsing
_fleet_cache: dict[str, tuple[float, list[ResolvedAgent]]] = {}
_FLEET_CACHE_TTL = 10.0  # Cache fleet for 10 seconds


class AgentExecution(BaseModel):
    exit_code: int
    stdout: str = ""
    stderr: str = ""
    response: dict[str, Any] = Field(default_factory=dict)


class LocalWorkerResult(BaseModel):
    agent_key: str
    status: Literal["no_task", "blocked", "succeeded", "failed"]
    summary: str
    executor_type: str | None = None
    envelope_id: str | None = None
    task_id: str | None = None
    envelope_path: str | None = None
    pending_task_path: str | None = None
    running_task_path: str | None = None
    done_task_path: str | None = None
    report_path: str | None = None
    approval_state: str | None = None
    blockers: list[str] = Field(default_factory=list)


class _QueuedTask(BaseModel):
    envelope: TaskEnvelope
    envelope_path: Path
    pending_task_path: Path
    approval_state: str


Runner = Callable[[ResolvedAgent, str, Path, _QueuedTask, bool], AgentExecution]

_FINAL_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {
            "type": "string",
            "enum": ["succeeded", "failed", "blocked"],
        },
        "summary": {"type": "string"},
        "report_path": {"type": "string"},
        "verification": {"type": "string"},
    },
    "required": ["status", "summary", "report_path"],
    "additionalProperties": True,
}


def _agent_executor_type(agent: ResolvedAgent) -> ExecutorType:
    if agent.adapter_type == "codex_local":
        return ExecutorType.codex
    if agent.adapter_type == "claude_local":
        return ExecutorType.claude_code
    raise ValueError(f"Agent {agent.key} is not a local executable worker")


def _select_agent(repo_root: Path, agent_key: str) -> tuple[ResolvedAgent, ExecutorType]:
    # Use cached fleet resolution
    cache_key = str(repo_root.resolve())
    now = time.time()

    if cache_key in _fleet_cache:
        cached_time, cached_fleet = _fleet_cache[cache_key]
        if now - cached_time < _FLEET_CACHE_TTL:
            fleet = {agent.key: agent for agent in cached_fleet}
        else:
            fleet = {agent.key: agent for agent in resolve_fleet(repo_root)}
            _fleet_cache[cache_key] = (now, list(fleet.values()))
    else:
        fleet = {agent.key: agent for agent in resolve_fleet(repo_root)}
        _fleet_cache[cache_key] = (now, list(fleet.values()))

    if agent_key not in fleet:
        raise ValueError(f"Unknown agent_key={agent_key!r}")
    agent = fleet[agent_key]
    executor_type = _agent_executor_type(agent)
    if not agent.ready:
        raise ValueError(f"Agent {agent_key} is not ready: {', '.join(agent.blockers)}")
    if not agent.command:
        raise ValueError(f"Agent {agent_key} does not define a command")
    if not agent.working_directory:
        raise ValueError(f"Agent {agent_key} does not define a working directory")
    return agent, executor_type


def _approval_state(repo_root: Path, envelope: TaskEnvelope) -> str:
    if not envelope.approval_required:
        return "not_required"

    approval_id = f"approval__{envelope.envelope_id}"
    for status in ApprovalStatus:
        path = repo_root / "ops/approvals" / status.value / f"{approval_id}.json"
        if path.exists():
            record = ApprovalRecord.model_validate_json(path.read_text(encoding="utf-8"))
            return record.status.value
    return "missing"


def _task_matches(envelope: TaskEnvelope, task_id: str | None) -> bool:
    if task_id is None:
        return True
    return task_id in {envelope.task_id, envelope.envelope_id}


def _discover_next_task(repo_root: Path, executor_type: ExecutorType, task_id: str | None) -> tuple[_QueuedTask | None, list[str]]:
    compiled_dir = repo_root / "ops/tasks/compiled"
    if not compiled_dir.exists():
        return None, []

    candidates: list[tuple[float, _QueuedTask]] = []
    blockers: list[str] = []

    for envelope_path in compiled_dir.glob("*.json"):
        if envelope_path.name == ".gitkeep":
            continue
        payload = json.loads(envelope_path.read_text(encoding="utf-8"))
        if "envelope_id" not in payload:
            continue
        envelope = TaskEnvelope.model_validate(payload)
        if envelope.executor_type != executor_type or not _task_matches(envelope, task_id):
            continue

        pending_task_path = legacy_task_path(envelope, repo_root, "pending")
        if not pending_task_path.exists():
            continue

        approval_state = _approval_state(repo_root, envelope)
        if approval_state not in {"approved", "not_required"}:
            blockers.append(f"{envelope.task_id}:{approval_state}")
            continue

        candidates.append(
            (
                pending_task_path.stat().st_mtime,
                _QueuedTask(
                    envelope=envelope,
                    envelope_path=envelope_path,
                    pending_task_path=pending_task_path,
                    approval_state=approval_state,
                ),
            )
        )

    if not candidates:
        return None, blockers

    candidates.sort(key=lambda item: item[0])
    return candidates[0][1], blockers


def _claim_task(repo_root: Path, queued_task: _QueuedTask) -> Path:
    running_path = legacy_task_path(queued_task.envelope, repo_root, "running")
    ensure_dir(running_path.parent)
    queued_task.pending_task_path.replace(running_path)
    return running_path


def _complete_task(repo_root: Path, envelope: TaskEnvelope, running_task_path: Path) -> Path:
    done_path = legacy_task_path(envelope, repo_root, "done")
    ensure_dir(done_path.parent)
    running_task_path.replace(done_path)
    return done_path


def _expected_report_path(repo_root: Path, envelope: TaskEnvelope, agent_key: str) -> Path:
    report_dir = ensure_dir(repo_root / "ops/reports")
    stamp = datetime.now(UTC).strftime("%Y-%m-%d-%H%M%S")
    slug = slugify(f"{envelope.task_id}-{agent_key}")
    return report_dir / f"{stamp}-{slug}.md"


def _relative_report_path(path: Path, repo_root: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def _workspace_equivalent(repo_root: Path, workspace_root: Path, path: Path) -> Path:
    try:
        relative = path.resolve().relative_to(repo_root.resolve())
    except ValueError:
        return path
    return workspace_root / relative


def _repo_equivalent(repo_root: Path, workspace_root: Path, path: Path) -> Path:
    try:
        relative = path.resolve().relative_to(workspace_root.resolve())
    except ValueError:
        return path
    return repo_root / relative


def _build_worker_prompt(
    agent: ResolvedAgent,
    repo_root: Path,
    queued_task: _QueuedTask,
    running_task_path: Path,
    report_path: Path,
) -> str:
    bootstrap = ""
    if agent.bootstrap_prompt_file:
        bootstrap = Path(agent.bootstrap_prompt_file).read_text(encoding="utf-8").strip()

    workspace_root = Path(agent.working_directory)
    workspace_envelope_path = _workspace_equivalent(repo_root, workspace_root, queued_task.envelope_path)
    workspace_running_task_path = _workspace_equivalent(repo_root, workspace_root, running_task_path)
    context_bundle_path = _workspace_equivalent(
        repo_root,
        workspace_root,
        repo_root / queued_task.envelope.context_bundle_ref,
    )
    artifact_output = queued_task.envelope.artifact_output_path
    approval_state = queued_task.approval_state

    return f"""{bootstrap}

Execute the assigned local worker task in this repository.

Task envelope file: {workspace_envelope_path}
Claimed running task markdown: {workspace_running_task_path}
Context bundle file: {context_bundle_path}
Expected report path: {report_path}
Artifact output path: {artifact_output}
Approval state: {approval_state}

Rules:
- Work only on this task.
- Read the task envelope and context bundle before changing code.
- Implement the task in the current workspace.
- Run verification needed for the acceptance criteria.
- Write a concise execution report to {report_path}.
- The report must include: status, summary, verification, changed files, and follow-up risks.
- If the task cannot be completed, still write the report and explain the blocker.

Return only JSON matching the required schema with:
- status: succeeded | failed | blocked
- summary: one short sentence
- report_path: repo-relative path of the report you wrote
- verification: short verification summary
"""


def _parse_json_payload(text: str) -> dict[str, str]:
    payload = text.strip()
    if not payload:
        return {}
    return json.loads(payload)


def _run_codex_agent(agent: ResolvedAgent, prompt: str, schema_path: Path, response_path: Path) -> AgentExecution:
    command = [
        agent.command,
        "exec",
        "--skip-git-repo-check",
        "--dangerously-bypass-approvals-and-sandbox",
        "--output-schema",
        str(schema_path),
        "-o",
        str(response_path),
    ]
    if agent.model:
        command.extend(["-m", agent.model])
    if agent.enable_search:
        command.append("--search")

    completed = subprocess.run(
        command,
        input=prompt,
        text=True,
        capture_output=True,
        cwd=agent.working_directory,
        timeout=int(os.getenv("AI_OS_LOCAL_WORKER_TIMEOUT_SECONDS", "3600")),
        check=False,
    )

    payload = {}
    if response_path.exists():
        payload = _parse_json_payload(response_path.read_text(encoding="utf-8"))

    return AgentExecution(
        exit_code=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
        response=payload,
    )


def _run_claude_agent(agent: ResolvedAgent, prompt: str) -> AgentExecution:
    command = [
        agent.command,
        "-p",
        "--output-format",
        "json",
        "--json-schema",
        json.dumps(_FINAL_RESPONSE_SCHEMA, ensure_ascii=True),
        "--add-dir",
        agent.working_directory,
        "--no-chrome",
    ]
    if agent.skip_permissions:
        command.append("--dangerously-skip-permissions")
    else:
        command.extend(["--permission-mode", "bypassPermissions"])
    if agent.model and agent.model != "Default":
        command.extend(["--model", agent.model])

    completed = subprocess.run(
        command,
        input=prompt,
        text=True,
        capture_output=True,
        cwd=agent.working_directory,
        timeout=int(os.getenv("AI_OS_LOCAL_WORKER_TIMEOUT_SECONDS", "3600")),
        check=False,
    )

    payload = {}
    if completed.stdout.strip():
        payload = _parse_json_payload(completed.stdout)

    return AgentExecution(
        exit_code=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
        response=payload,
    )


def _default_runner(
    agent: ResolvedAgent,
    prompt: str,
    report_path: Path,
    queued_task: _QueuedTask,
    dry_run: bool,
) -> AgentExecution:
    if dry_run:
        return AgentExecution(
            exit_code=0,
            response={
                "status": "succeeded",
                "summary": "dry-run completed without invoking a local agent",
                "report_path": str(report_path),
                "verification": "dry-run only",
            },
            stdout="dry-run",
            stderr="",
        )

    with tempfile.TemporaryDirectory() as tmpdir:
        temp_dir = Path(tmpdir)
        schema_path = temp_dir / "worker-schema.json"
        response_path = temp_dir / "worker-response.json"
        write_json(schema_path, _FINAL_RESPONSE_SCHEMA)

        if agent.adapter_type == "codex_local":
            return _run_codex_agent(agent, prompt, schema_path, response_path)
        if agent.adapter_type == "claude_local":
            return _run_claude_agent(agent, prompt)
    raise ValueError(f"Unsupported local agent type: {agent.adapter_type}")


def _resolve_report_path(
    repo_root: Path,
    workspace_root: Path,
    requested_report_path: str | None,
    fallback_path: Path,
) -> Path:
    if not requested_report_path:
        return fallback_path
    candidate = Path(requested_report_path)
    if candidate.is_absolute():
        return _repo_equivalent(repo_root, workspace_root, candidate)
    return _repo_equivalent(repo_root, workspace_root, (workspace_root / candidate).resolve())


def _write_fallback_report(
    path: Path,
    agent: ResolvedAgent,
    queued_task: _QueuedTask,
    execution: AgentExecution,
    started_at: float,
    finished_at: float,
    summary: str,
    verification: str,
) -> Path:
    ensure_dir(path.parent)
    duration = round(finished_at - started_at, 2)
    content = f"""# Execution Report: {queued_task.envelope.title}

## Status
- agent: {agent.key}
- adapter_type: {agent.adapter_type}
- status: {execution.response.get("status", "failed")}
- duration_seconds: {duration}

## Summary
{summary}

## Verification
{verification or "No verification summary supplied."}

## Task
- envelope_id: {queued_task.envelope.envelope_id}
- task_id: {queued_task.envelope.task_id}
- objective: {queued_task.envelope.objective}
- context_bundle_ref: {queued_task.envelope.context_bundle_ref}
- artifact_output_path: {queued_task.envelope.artifact_output_path}

## Agent Stdout
```text
{execution.stdout.strip() or "(empty)"}
```

## Agent Stderr
```text
{execution.stderr.strip() or "(empty)"}
```
"""
    path.write_text(content, encoding="utf-8")
    return path


def run_local_worker_once(
    repo_root: Path,
    agent_key: str = "local_builder",
    task_id: str | None = None,
    dry_run: bool = False,
    runner: Runner | None = None,
) -> LocalWorkerResult:
    agent, executor_type = _select_agent(repo_root, agent_key)
    queued_task, blockers = _discover_next_task(repo_root, executor_type, task_id)

    if queued_task is None:
        if blockers:
            return LocalWorkerResult(
                agent_key=agent_key,
                status="blocked",
                summary="No runnable local task is available because queued work is blocked.",
                executor_type=executor_type.value,
                blockers=blockers,
            )
        return LocalWorkerResult(
            agent_key=agent_key,
            status="no_task",
            summary="No matching local task is queued.",
            executor_type=executor_type.value,
        )

    running_task_path = _claim_task(repo_root, queued_task)
    workspace_root = Path(agent.working_directory)
    report_path = _expected_report_path(repo_root, queued_task.envelope, agent_key)
    workspace_report_path = _workspace_equivalent(repo_root, workspace_root, report_path)
    started_at = time.time()
    prompt = _build_worker_prompt(
        agent,
        repo_root,
        queued_task,
        running_task_path,
        workspace_report_path,
    )
    agent_runner = runner or _default_runner

    try:
        execution = agent_runner(agent, prompt, workspace_report_path, queued_task, dry_run)
        requested_report = execution.response.get("report_path")
        resolved_report_path = _resolve_report_path(repo_root, workspace_root, requested_report, report_path)
        verification = execution.response.get("verification", "")
        summary = execution.response.get("summary", "") or "The local worker finished without a summary."
        status = execution.response.get("status", "")
        if status not in {"succeeded", "failed", "blocked"}:
            status = "succeeded" if execution.exit_code == 0 else "failed"
        if not resolved_report_path.exists():
            resolved_report_path = _write_fallback_report(
                resolved_report_path,
                agent,
                queued_task,
                execution,
                started_at,
                time.time(),
                summary,
                verification,
            )
    except Exception as exc:
        execution = AgentExecution(
            exit_code=1,
            stdout="",
            stderr=str(exc),
            response={
                "status": "failed",
                "summary": f"Local worker crashed: {exc}",
                "report_path": _relative_report_path(report_path, repo_root),
                "verification": "worker exception",
            },
        )
        status = "failed"
        summary = execution.response["summary"]
        resolved_report_path = _write_fallback_report(
            report_path,
            agent,
            queued_task,
            execution,
            started_at,
            time.time(),
            summary,
            execution.response["verification"],
        )

    done_task_path = _complete_task(repo_root, queued_task.envelope, running_task_path)
    final_status = status if status in {"blocked", "succeeded"} else "failed"

    return LocalWorkerResult(
        agent_key=agent_key,
        status=final_status,
        summary=summary,
        executor_type=executor_type.value,
        envelope_id=queued_task.envelope.envelope_id,
        task_id=queued_task.envelope.task_id,
        envelope_path=str(queued_task.envelope_path),
        pending_task_path=str(queued_task.pending_task_path),
        running_task_path=str(running_task_path),
        done_task_path=str(done_task_path),
        report_path=str(resolved_report_path),
        approval_state=queued_task.approval_state,
    )
