from __future__ import annotations

import json
import re
import shutil
import subprocess
import time
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Literal

import requests
from pydantic import BaseModel, Field

from .agent_fleet import resolve_fleet
from .fs_utils import ensure_dir
from .paperclip_provision import match_live_agents

DEFAULT_LOCAL_LANES = ("ceo", "pm_compiler", "local_builder", "local_claude_builder")
IDLE_PATTERNS = (
    "no assigned",
    "no assignment",
    "no issues",
    "exit cleanly",
    "don't have an assigned task",
    "do not have an assigned task",
)
RATE_LIMIT_PATTERNS = (
    "rate limit",
    "too many requests",
    "429",
    "quota",
    "try again later",
    "rate limits remaining",
)


class HeartbeatRunResult(BaseModel):
    key: str
    agent_id: str
    agent_name: str
    status: Literal["idle", "running", "succeeded", "rate_limited", "failed", "skipped", "missing"]
    summary: str
    run_id: str | None = None
    backoff_until: str | None = None
    exit_code: int | None = None
    last_invoked_at: str | None = None
    last_completed_at: str | None = None
    consecutive_failures: int = 0
    consecutive_rate_limits: int = 0
    output_excerpt: str | None = None


class SupervisorSnapshot(BaseModel):
    generated_at: str
    company_id: str
    cycle: int
    results: list[HeartbeatRunResult] = Field(default_factory=list)


def _paperclip_api_base() -> str:
    import os

    return (os.getenv("PAPERCLIP_LOCAL_API_URL") or os.getenv("PAPERCLIP_API_URL") or "http://localhost:3100").rstrip("/")


def _company_id() -> str:
    import os

    value = os.getenv("PAPERCLIP_LOCAL_COMPANY_ID") or os.getenv("PAPERCLIP_COMPANY_ID")
    if not value:
        raise ValueError("Missing PAPERCLIP_LOCAL_COMPANY_ID or PAPERCLIP_COMPANY_ID")
    return value


def _heartbeat_state_dir(repo_root: Path) -> Path:
    return ensure_dir(repo_root / "ops/paperclip/heartbeat")


def _heartbeat_state_path(repo_root: Path, key: str) -> Path:
    return _heartbeat_state_dir(repo_root) / f"{key}.json"


def _snapshot_path(repo_root: Path) -> Path:
    return ensure_dir(repo_root / "ops/reports") / "paperclip-swarm-latest.json"


def _load_previous_result(repo_root: Path, key: str) -> HeartbeatRunResult | None:
    path = _heartbeat_state_path(repo_root, key)
    if not path.exists():
        return None
    return HeartbeatRunResult.model_validate_json(path.read_text(encoding="utf-8"))


def _save_result(repo_root: Path, result: HeartbeatRunResult) -> None:
    _heartbeat_state_path(repo_root, result.key).write_text(
        result.model_dump_json(indent=2),
        encoding="utf-8",
    )


def _save_snapshot(repo_root: Path, snapshot: SupervisorSnapshot) -> None:
    _snapshot_path(repo_root).write_text(snapshot.model_dump_json(indent=2), encoding="utf-8")


def _is_rate_limited(text: str) -> bool:
    lowered = text.lower()
    return any(pattern in lowered for pattern in RATE_LIMIT_PATTERNS)


def _is_idle(text: str) -> bool:
    lowered = text.lower()
    return any(pattern in lowered for pattern in IDLE_PATTERNS)


def _parse_run_id(text: str) -> str | None:
    match = re.search(r"Invoked heartbeat run ([a-f0-9-]+)", text)
    return match.group(1) if match else None


def _next_backoff(rate_limit_count: int) -> int:
    schedule = [300, 900, 1800, 3600]
    index = min(max(rate_limit_count - 1, 0), len(schedule) - 1)
    return schedule[index]


def _utcnow() -> datetime:
    return datetime.now(UTC)


def _parse_iso_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def _agent_headers() -> dict[str, str]:
    import os

    api_key = os.getenv("PAPERCLIP_API_KEY")
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    return headers


def _list_live_agents(company_id: str, api_base: str) -> dict[str, dict[str, object]]:
    response = requests.get(
        f"{api_base}/api/companies/{company_id}/agents",
        headers=_agent_headers(),
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    if isinstance(payload, dict):
        if "items" in payload:
            payload = payload["items"]
        elif "value" in payload:
            payload = payload["value"]
    return match_live_agents(payload)


def _run_heartbeat(agent_id: str, api_base: str, timeout_ms: int) -> subprocess.CompletedProcess[str]:
    executable = shutil.which("npx") or shutil.which("npx.cmd") or "npx"
    command = [
        executable,
        "paperclipai",
        "heartbeat",
        "run",
        "-a",
        agent_id,
        "--api-base",
        api_base,
        "--source",
        "automation",
        "--trigger",
        "system",
        "--timeout-ms",
        str(timeout_ms),
        "--json",
    ]
    return subprocess.run(
        command,
        text=True,
        capture_output=True,
        check=False,
        timeout=max(timeout_ms // 1000 + 15, 60),
    )


def _combine_output(stdout: str | None, stderr: str | None) -> str:
    return "\n".join(part for part in (stdout, stderr) if part).strip()


def _is_success_output(text: str) -> bool:
    lowered = text.lower()
    return any(
        pattern in lowered
        for pattern in (
            "completed with status succeeded",
            "\"status\":\"succeeded\"",
            "\"status\": \"succeeded\"",
            "heartbeat completed successfully",
        )
    )


def _select_lane_keys(repo_root: Path, agent_keys: list[str] | None) -> list[str]:
    if agent_keys:
        return agent_keys
    resolved = {agent.key: agent for agent in resolve_fleet(repo_root)}
    return [key for key in DEFAULT_LOCAL_LANES if key in resolved]


def _build_missing_result(key: str) -> HeartbeatRunResult:
    return HeartbeatRunResult(
        key=key,
        agent_id="",
        agent_name=key,
        status="missing",
        summary="Agent was not found in the live Paperclip company.",
        last_invoked_at=_utcnow().isoformat(),
        last_completed_at=_utcnow().isoformat(),
    )


def _should_skip(previous: HeartbeatRunResult | None, now: datetime) -> tuple[bool, str | None]:
    if previous is None or previous.backoff_until is None:
        return False, None
    backoff_until = _parse_iso_datetime(previous.backoff_until)
    if backoff_until is None or now >= backoff_until:
        return False, None
    return True, backoff_until.isoformat()


def _run_lane(
    repo_root: Path,
    *,
    key: str,
    live_agent: dict[str, object] | None,
    api_base: str,
    timeout_ms: int,
) -> HeartbeatRunResult:
    now = _utcnow()
    previous = _load_previous_result(repo_root, key)
    live_status = str(live_agent.get("status") or "").strip().lower() if live_agent is not None else ""

    if live_agent is None:
        result = _build_missing_result(key)
        _save_result(repo_root, result)
        return result

    if live_status == "running":
        result = HeartbeatRunResult(
            key=key,
            agent_id=str(live_agent["id"]),
            agent_name=str(live_agent["name"]),
            status="running",
            summary="Paperclip reports an active heartbeat run; skipping duplicate invoke.",
            last_invoked_at=previous.last_invoked_at if previous else now.isoformat(),
            last_completed_at=previous.last_completed_at if previous else None,
            consecutive_failures=previous.consecutive_failures if previous else 0,
            consecutive_rate_limits=previous.consecutive_rate_limits if previous else 0,
        )
        _save_result(repo_root, result)
        return result

    if previous is not None:
        should_skip, backoff_until = _should_skip(previous, now)
        if should_skip:
            result = HeartbeatRunResult(
                key=key,
                agent_id=str(live_agent["id"]),
                agent_name=str(live_agent["name"]),
                status="skipped",
                summary=f"Backoff active until {backoff_until}.",
                backoff_until=backoff_until,
                last_invoked_at=previous.last_invoked_at,
                last_completed_at=previous.last_completed_at,
                consecutive_failures=previous.consecutive_failures,
                consecutive_rate_limits=previous.consecutive_rate_limits,
            )
            _save_result(repo_root, result)
            return result

    try:
        completed = _run_heartbeat(str(live_agent["id"]), api_base, timeout_ms)
        combined_output = _combine_output(completed.stdout, completed.stderr)
    except subprocess.TimeoutExpired as exc:
        combined_output = _combine_output(exc.stdout, exc.stderr)
        run_id = _parse_run_id(combined_output)
        excerpt = combined_output[-600:] if combined_output else None
        result = HeartbeatRunResult(
            key=key,
            agent_id=str(live_agent["id"]),
            agent_name=str(live_agent["name"]),
            status="running",
            summary="Heartbeat invocation exceeded the local wait budget; leaving the server-side run active.",
            run_id=run_id,
            last_invoked_at=now.isoformat(),
            last_completed_at=previous.last_completed_at if previous else None,
            consecutive_failures=0,
            consecutive_rate_limits=previous.consecutive_rate_limits if previous else 0,
            output_excerpt=excerpt,
        )
        _save_result(repo_root, result)
        return result

    run_id = _parse_run_id(combined_output)
    excerpt = combined_output[-600:] if combined_output else None

    consecutive_failures = previous.consecutive_failures if previous else 0
    consecutive_rate_limits = previous.consecutive_rate_limits if previous else 0
    backoff_until: str | None = None

    if completed.returncode == 0 or _is_idle(combined_output) or _is_success_output(combined_output):
        status: Literal["idle", "running", "succeeded", "rate_limited", "failed", "skipped", "missing"] = "idle" if _is_idle(combined_output) else "succeeded"
        summary = "Heartbeat completed without assigned work." if status == "idle" else "Heartbeat completed successfully."
        consecutive_failures = 0
        consecutive_rate_limits = 0
    elif _is_rate_limited(combined_output):
        status = "rate_limited"
        consecutive_failures = 0
        consecutive_rate_limits += 1
        delay_seconds = _next_backoff(consecutive_rate_limits)
        backoff_until = (now + timedelta(seconds=delay_seconds)).isoformat()
        summary = f"Rate limited. Backing off for {delay_seconds} seconds."
    else:
        status = "failed"
        consecutive_failures += 1
        consecutive_rate_limits = 0
        summary = "Heartbeat execution failed."

    result = HeartbeatRunResult(
        key=key,
        agent_id=str(live_agent["id"]),
        agent_name=str(live_agent["name"]),
        status=status,
        summary=summary,
        run_id=run_id,
        backoff_until=backoff_until,
        exit_code=completed.returncode,
        last_invoked_at=now.isoformat(),
        last_completed_at=_utcnow().isoformat(),
        consecutive_failures=consecutive_failures,
        consecutive_rate_limits=consecutive_rate_limits,
        output_excerpt=excerpt,
    )
    _save_result(repo_root, result)
    return result


def run_swarm_supervisor(
    repo_root: Path,
    *,
    agent_keys: list[str] | None = None,
    sleep_seconds: int = 90,
    timeout_ms: int = 600000,
    max_cycles: int | None = None,
    once: bool = False,
) -> SupervisorSnapshot:
    company_id = _company_id()
    api_base = _paperclip_api_base()
    lane_keys = _select_lane_keys(repo_root, agent_keys)

    cycle = 0
    latest_results: list[HeartbeatRunResult] = []

    while True:
        cycle += 1
        live_agents = _list_live_agents(company_id, api_base)
        latest_results = []
        for key in lane_keys:
            latest_results.append(
                _run_lane(
                    repo_root,
                    key=key,
                    live_agent=live_agents.get(key),
                    api_base=api_base,
                    timeout_ms=timeout_ms,
                )
            )

        snapshot = SupervisorSnapshot(
            generated_at=_utcnow().isoformat(),
            company_id=company_id,
            cycle=cycle,
            results=latest_results,
        )
        _save_snapshot(repo_root, snapshot)

        if once or (max_cycles is not None and cycle >= max_cycles):
            return snapshot
        time.sleep(max(sleep_seconds, 5))
