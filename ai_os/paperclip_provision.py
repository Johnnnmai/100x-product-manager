from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from .agent_fleet import AgentFleetSpec, ResolvedAgent
from .company_portfolio import IssueSeed, ProjectSpec, WorkspaceSpec


def live_agent_fleet_key(agent: dict[str, object]) -> str:
    metadata = dict(agent.get("metadata") or {})
    fleet_key = metadata.get("fleet_key")
    if isinstance(fleet_key, str) and fleet_key:
        return fleet_key
    url_key = str(agent.get("urlKey") or "")
    return url_key.replace("-", "_")


def live_agent_assignment_role(agent: dict[str, object]) -> str | None:
    metadata = dict(agent.get("metadata") or {})
    value = metadata.get("assignment_role")
    if isinstance(value, str) and value:
        return value
    return None


def match_live_agents(live_agents: Iterable[dict[str, object]]) -> dict[str, dict[str, object]]:
    matched: dict[str, dict[str, object]] = {}
    for agent in live_agents:
        key = live_agent_fleet_key(agent)
        existing = matched.get(key)
        if existing is None:
            matched[key] = agent
            continue

        existing_metadata = dict(existing.get("metadata") or {})
        current_metadata = dict(agent.get("metadata") or {})
        existing_has_fleet_key = isinstance(existing_metadata.get("fleet_key"), str) and bool(existing_metadata.get("fleet_key"))
        current_has_fleet_key = isinstance(current_metadata.get("fleet_key"), str) and bool(current_metadata.get("fleet_key"))

        # Prefer explicitly repo-managed agents over urlKey fallbacks when keys collide.
        if current_has_fleet_key and not existing_has_fleet_key:
            matched[key] = agent
    return matched


def align_live_agents_to_fleet(
    live_agents: Iterable[dict[str, object]],
    specs: Iterable[AgentFleetSpec],
) -> tuple[dict[str, dict[str, object]], dict[str, dict[str, object]]]:
    live_agents_list = list(live_agents)
    canonical_by_key = match_live_agents(live_agents_list)
    matched: dict[str, dict[str, object]] = {}
    used_ids: set[str] = set()

    name_lookup: dict[str, list[dict[str, object]]] = {}
    for agent in live_agents_list:
        name = str(agent.get("name") or "").strip().lower()
        if name:
            name_lookup.setdefault(name, []).append(agent)

    for spec in specs:
        agent = canonical_by_key.get(spec.key)
        if agent is None:
            continue
        matched[spec.key] = agent
        used_ids.add(str(agent.get("id") or ""))

    for spec in specs:
        if spec.key in matched:
            continue
        for candidate in name_lookup.get(spec.name.strip().lower(), []):
            candidate_id = str(candidate.get("id") or "")
            if candidate_id and candidate_id not in used_ids:
                matched[spec.key] = candidate
                used_ids.add(candidate_id)
                break

    orphaned: dict[str, dict[str, object]] = {}
    for key, agent in canonical_by_key.items():
        agent_id = str(agent.get("id") or "")
        if agent_id not in used_ids:
            orphaned[key] = agent

    return matched, orphaned


def workspace_display_name(project_key: str, workspace: WorkspaceSpec) -> str:
    if workspace.name:
        return workspace.name
    if workspace.repo_url:
        return workspace.repo_url.rstrip("/").rsplit("/", 1)[-1]
    if workspace.cwd:
        return Path(workspace.cwd).name
    return project_key


def normalize_project_status(status: str | None) -> str:
    mapping = {
        "planned": "planned",
        "active": "in_progress",
        "paused": "backlog",
        "completed": "completed",
        "archived": "cancelled",
    }
    return mapping.get((status or "planned").strip().lower(), "planned")


def build_project_create_body(project: ProjectSpec, lead_agent_id: str | None) -> dict[str, object]:
    return {
        "name": project.name,
        "description": project.description,
        "status": normalize_project_status(project.status),
        "leadAgentId": lead_agent_id,
        "targetDate": project.target_date,
        "color": project.color,
    }


def build_workspace_create_body(project_key: str, workspace: WorkspaceSpec) -> dict[str, object]:
    return {
        "name": workspace_display_name(project_key, workspace),
        "cwd": workspace.cwd,
        "repoUrl": workspace.repo_url,
        "repoRef": workspace.repo_ref,
        "metadata": workspace.metadata or None,
        "isPrimary": workspace.is_primary,
    }


def build_local_hire_payload(
    *,
    spec: AgentFleetSpec,
    resolved: ResolvedAgent,
    reports_to_id: str | None,
    prompt_template: str,
) -> dict[str, object]:
    if spec.adapter_type not in {"claude_local", "codex_local"}:
        raise ValueError(f"Unsupported local hire adapter type: {spec.adapter_type}")
    if not resolved.command or not resolved.instructions_file:
        raise ValueError(f"Agent {spec.key} is missing command or instructions path")

    runtime_config = {
        "heartbeat": {
            "enabled": True,
            "cooldownSec": 10,
            "intervalSec": 180,
            "wakeOnDemand": True,
            "maxConcurrentRuns": 1,
        }
    }

    if spec.adapter_type == "claude_local":
        adapter_config: dict[str, object] = {
            "cwd": resolved.working_directory,
            "chrome": bool(resolved.enable_chrome),
            "command": resolved.command,
            "graceSec": 15,
            "timeoutSec": 0,
            "maxTurnsPerRun": resolved.max_turns_per_run or 24,
            "instructionsFilePath": resolved.instructions_file,
            "dangerouslySkipPermissions": bool(resolved.skip_permissions),
            "promptTemplate": prompt_template,
        }
        if resolved.model and resolved.model != "Default":
            adapter_config["model"] = resolved.model
    else:
        adapter_config = {
            "cwd": resolved.working_directory,
            "command": resolved.command,
            "model": resolved.model,
            "enableSearch": bool(resolved.enable_search),
            "bypassSandbox": bool(resolved.bypass_sandbox),
            "instructionsFilePath": resolved.instructions_file,
            "dangerouslyBypassApprovalsAndSandbox": True,
            "promptTemplate": prompt_template,
        }

    metadata = {
        "fleet_key": spec.key,
        "assignment_role": resolved.assignment_role or spec.key,
        "department": resolved.department or "",
        "runtime_class": resolved.runtime_class or "",
        "fallback_agent_key": resolved.fallback_agent_key or "",
        "source": "paperclip/agent_fleet.yaml",
    }

    return {
        "icon": spec.icon,
        "name": spec.name,
        "role": spec.role,
        "title": spec.title,
        "metadata": metadata,
        "reportsTo": reports_to_id,
        "adapterType": spec.adapter_type,
        "capabilities": spec.capabilities,
        "adapterConfig": adapter_config,
        "runtimeConfig": runtime_config,
        "budgetMonthlyCents": 0,
        "requestedByAgentId": None,
        "requestedConfigurationSnapshot": {
            "adapterType": spec.adapter_type,
            "adapterConfig": adapter_config,
            "runtimeConfig": runtime_config,
        },
    }


@dataclass(slots=True)
class SeededIssue:
    seed: IssueSeed
    parent_key: str | None


def iter_seeded_issues(issue_seeds: Iterable[IssueSeed], parent_key: str | None = None) -> Iterable[SeededIssue]:
    for seed in issue_seeds:
        yield SeededIssue(seed=seed, parent_key=parent_key)
        yield from iter_seeded_issues(seed.children, seed.key)
