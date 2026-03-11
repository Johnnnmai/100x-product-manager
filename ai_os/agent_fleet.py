from __future__ import annotations

import shutil
from pathlib import Path
from functools import lru_cache
from typing import Optional

from pydantic import BaseModel, Field

from .fs_utils import load_yaml


class FleetDefaults(BaseModel):
    working_directory: str = "."
    instructions_file: str = "AGENTS.md"
    heartbeat: bool = False


class AgentFleetSpec(BaseModel):
    key: str
    name: str
    role: str | None = None
    assignment_role: str | None = None
    department: str | None = None
    runtime_class: str | None = None
    fallback_agent_key: str | None = None
    title: str
    icon: str | None = None
    capabilities: str | None = None
    adapter_type: str
    reports_to: str | None = None
    command: str | None = None
    model: str | None = None
    thinking_effort: str | None = None
    enable_chrome: bool | None = None
    skip_permissions: bool | None = None
    max_turns_per_run: int | None = None
    enable_search: bool | None = None
    bypass_sandbox: bool | None = None
    bootstrap_prompt_file: str | None = None
    gateway_url_env: str | None = None


class FleetFile(BaseModel):
    company: str
    version: int = 1
    defaults: FleetDefaults = Field(default_factory=FleetDefaults)
    agents: list[AgentFleetSpec] = Field(default_factory=list)


class ResolvedAgent(BaseModel):
    key: str
    name: str
    role: str | None = None
    assignment_role: str | None = None
    department: str | None = None
    runtime_class: str | None = None
    fallback_agent_key: str | None = None
    title: str
    icon: str | None = None
    capabilities: str | None = None
    adapter_type: str
    reports_to: str | None = None
    working_directory: str | None = None
    instructions_file: str | None = None
    bootstrap_prompt_file: str | None = None
    command: str | None = None
    command_available: bool | None = None
    model: str | None = None
    thinking_effort: str | None = None
    enable_chrome: bool | None = None
    skip_permissions: bool | None = None
    max_turns_per_run: int | None = None
    enable_search: bool | None = None
    bypass_sandbox: bool | None = None
    gateway_url_env: str | None = None
    gateway_url: str | None = None
    ready: bool
    blockers: list[str] = Field(default_factory=list)


def load_fleet(path: Path) -> FleetFile:
    return FleetFile.model_validate(load_yaml(path))


def _preferred_workspace_root(repo_root: Path) -> Path:
    import os

    resolved_repo_root = repo_root.resolve()
    env_root = os.getenv("PAPERCLIP_WORKSPACE_ROOT", "").strip()
    if env_root:
        candidate = Path(os.path.abspath(os.path.expanduser(env_root)))
        if candidate.exists():
            return candidate

    repo_root_str = str(resolved_repo_root)
    if any(ord(char) > 127 for char in repo_root_str):
        alias_root = Path(os.path.abspath("C:/paperclip-work/brand-book"))
        if alias_root.exists():
            return alias_root

    return resolved_repo_root


def _resolve_command(base_root: Path, command: str) -> tuple[str, bool]:
    import os

    command_path = Path(command)
    if command_path.is_absolute():
        return str(command_path), command_path.exists()

    if any(sep in command for sep in ("/", "\\")) or command_path.suffix.lower() in {".cmd", ".bat", ".ps1", ".exe"}:
        candidate = Path(os.path.abspath(base_root / command_path))
        return str(candidate), candidate.exists()

    resolved = shutil.which(command)
    return (resolved or command), resolved is not None


def _is_workspace_alias_active(repo_root: Path, workspace_root: Path) -> bool:
    """Check if workspace alias is actively being used (different from repo_root)."""
    return workspace_root.resolve() != repo_root.resolve()


def _get_workspace_command(workspace_root: Path, agent_key: str, agent_role: str | None, agent_assignment_role: str | None = None) -> str | None:
    """Get command from workspace bin directory based on agent key, role, or assignment_role."""
    bin_dir = workspace_root / "paperclip" / "bin"

    # Try assignment_role first (most specific), then role, then key
    # Normalize underscores to hyphens to match file naming convention
    candidates = []
    if agent_assignment_role:
        candidates.append(f"{agent_assignment_role.replace('_', '-')}-paperclip.cmd")
    if agent_role:
        candidates.append(f"{agent_role.replace('_', '-')}-paperclip.cmd")
    candidates.append(f"{agent_key.replace('_', '-')}-paperclip.cmd")

    for candidate in candidates:
        script_path = bin_dir / candidate
        if script_path.exists():
            return str(script_path)

    return None


# Cache for fleet resolution
_fleet_cache: dict[str, tuple[float, list[ResolvedAgent]]] = {}
_fleet_cache_lock = __import__('threading').Lock()
_FLEET_CACHE_TTL = 30.0  # Cache TTL in seconds


def resolve_fleet(repo_root: Path, fleet_path: Path | None = None) -> list[ResolvedAgent]:
    import os
    import time

    path = fleet_path or repo_root / "paperclip/agent_fleet.yaml"
    cache_key = str(path.resolve())

    # Check cache first
    now = time.time()
    with _fleet_cache_lock:
        if cache_key in _fleet_cache:
            cached_time, cached_agents = _fleet_cache[cache_key]
            if now - cached_time < _FLEET_CACHE_TTL:
                return [a.model_copy() for a in cached_agents]

    # Original resolution logic
    fleet = load_fleet(path)
    workspace_root = _preferred_workspace_root(repo_root)
    resolved: list[ResolvedAgent] = []

    # Check if workspace alias is active (workspace different from repo)
    workspace_alias_active = _is_workspace_alias_active(repo_root, workspace_root)

    for agent in fleet.agents:
        blockers: list[str] = []
        working_directory = os.path.abspath(workspace_root / fleet.defaults.working_directory)
        instructions_file = os.path.abspath(workspace_root / fleet.defaults.instructions_file)
        bootstrap_prompt_file = (
            os.path.abspath(workspace_root / agent.bootstrap_prompt_file)
            if agent.bootstrap_prompt_file
            else None
        )

        command_available: bool | None = None
        if agent.command:
            # If workspace alias is active, check for workspace-specific command first
            resolved_command = None
            if workspace_alias_active:
                workspace_cmd = _get_workspace_command(workspace_root, agent.key, agent.role, agent.assignment_role)
                if workspace_cmd:
                    resolved_command = workspace_cmd
                    command_available = True

            # Fall back to standard command resolution
            if not resolved_command:
                resolved_command, command_available = _resolve_command(workspace_root, agent.command)

            if not command_available:
                blockers.append(f"command_not_found:{agent.command}")
        else:
            resolved_command = None

        gateway_url = None
        if agent.gateway_url_env:
            import os

            gateway_url = os.getenv(agent.gateway_url_env)
            if not gateway_url:
                blockers.append(f"missing_env:{agent.gateway_url_env}")

        if not Path(instructions_file).exists():
            blockers.append(f"missing_file:{instructions_file}")
        if bootstrap_prompt_file and not Path(bootstrap_prompt_file).exists():
            blockers.append(f"missing_file:{bootstrap_prompt_file}")

        resolved.append(
            ResolvedAgent(
                key=agent.key,
                name=agent.name,
                role=agent.role,
                assignment_role=agent.assignment_role or agent.key,
                department=agent.department,
                runtime_class=agent.runtime_class,
                fallback_agent_key=agent.fallback_agent_key,
                title=agent.title,
                icon=agent.icon,
                capabilities=agent.capabilities,
                adapter_type=agent.adapter_type,
                reports_to=agent.reports_to,
                working_directory=working_directory if agent.adapter_type != "openclaw_gateway" else None,
                instructions_file=instructions_file if agent.adapter_type != "openclaw_gateway" else None,
                bootstrap_prompt_file=bootstrap_prompt_file,
                command=resolved_command,
                command_available=command_available,
                model=agent.model,
                thinking_effort=agent.thinking_effort,
                enable_chrome=agent.enable_chrome,
                skip_permissions=agent.skip_permissions,
                max_turns_per_run=agent.max_turns_per_run,
                enable_search=agent.enable_search,
                bypass_sandbox=agent.bypass_sandbox,
                gateway_url_env=agent.gateway_url_env,
                gateway_url=gateway_url,
                ready=not blockers,
                blockers=blockers,
            )
        )

    # Update cache
    with _fleet_cache_lock:
        _fleet_cache[cache_key] = (now, resolved.copy())

    return resolved
