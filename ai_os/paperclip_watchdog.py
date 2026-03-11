from __future__ import annotations

import os
import shutil
import subprocess
import sys
import time
from datetime import UTC, datetime
from pathlib import Path

import requests
from pydantic import BaseModel

from .fs_utils import ensure_dir


def _utcnow() -> datetime:
    return datetime.now(UTC)


def _default_api_base() -> str:
    return (os.getenv("PAPERCLIP_LOCAL_API_URL") or os.getenv("PAPERCLIP_API_URL") or "http://127.0.0.1:3100").rstrip("/")


def _runtime_dir(repo_root: Path) -> Path:
    return ensure_dir(repo_root / "ops/paperclip/runtime")


def _watchdog_state_path(repo_root: Path) -> Path:
    return _runtime_dir(repo_root) / "watchdog-latest.json"


def _default_log_path(repo_root: Path) -> Path:
    return _runtime_dir(repo_root) / "paperclip-runtime.log"


def _paperclip_command() -> str:
    return shutil.which("npx") or shutil.which("npx.cmd") or "npx"


def _health_check(api_base: str) -> tuple[bool, str]:
    try:
        response = requests.get(f"{api_base}/api/health", timeout=10)
        if response.ok:
            return True, "healthy"
        return False, f"health returned {response.status_code}"
    except requests.RequestException as exc:
        return False, str(exc)


def _spawn_runtime(instance: str, log_path: Path) -> tuple[subprocess.Popen[str], object]:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_handle = log_path.open("a", encoding="utf-8")
    command = [_paperclip_command(), "paperclipai", "run", "-i", instance]
    kwargs: dict[str, object] = {
        "stdout": log_handle,
        "stderr": subprocess.STDOUT,
        "stdin": subprocess.DEVNULL,
        "text": True,
        "cwd": str(Path.cwd()),
    }
    if os.name == "nt":
        kwargs["creationflags"] = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
    else:
        kwargs["start_new_session"] = True
    process = subprocess.Popen(command, **kwargs)
    return process, log_handle


class PaperclipWatchdogSnapshot(BaseModel):
    monitored_at: str
    api_base: str
    instance: str
    healthy: bool
    health_detail: str
    child_pid: int | None = None
    child_alive: bool = False
    last_start_at: str | None = None
    restart_count: int = 0
    log_path: str


def run_paperclip_watchdog(
    repo_root: Path,
    *,
    api_base: str | None = None,
    instance: str = "default",
    check_interval_seconds: int = 30,
    once: bool = False,
    log_path: Path | None = None,
) -> PaperclipWatchdogSnapshot:
    resolved_api_base = (api_base or _default_api_base()).rstrip("/")
    resolved_log_path = (log_path or _default_log_path(repo_root)).resolve()

    child_process: subprocess.Popen[str] | None = None
    child_log_handle: object | None = None
    last_start_at: str | None = None
    restart_count = 0

    while True:
        healthy, health_detail = _health_check(resolved_api_base)
        child_alive = child_process is not None and child_process.poll() is None

        if healthy and child_process is not None and not child_alive:
            if child_log_handle is not None:
                child_log_handle.close()
            child_process = None
            child_log_handle = None

        if not healthy and not child_alive:
            child_process, child_log_handle = _spawn_runtime(instance, resolved_log_path)
            child_alive = True
            restart_count += 1
            last_start_at = _utcnow().isoformat()
            health_detail = f"runtime spawn requested after unhealthy check: {health_detail}"

        snapshot = PaperclipWatchdogSnapshot(
            monitored_at=_utcnow().isoformat(),
            api_base=resolved_api_base,
            instance=instance,
            healthy=healthy,
            health_detail=health_detail,
            child_pid=child_process.pid if child_process is not None else None,
            child_alive=child_alive,
            last_start_at=last_start_at,
            restart_count=restart_count,
            log_path=str(resolved_log_path),
        )
        _watchdog_state_path(repo_root).write_text(snapshot.model_dump_json(indent=2), encoding="utf-8")

        if once:
            return snapshot

        time.sleep(max(check_interval_seconds, 5))
