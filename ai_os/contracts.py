from __future__ import annotations

from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, Field


class ArtifactKind(StrEnum):
    markdown = "markdown"
    json = "json"
    html = "html"
    screenshot = "screenshot"
    text = "text"
    report = "report"
    evidence = "evidence"


class ExecutorType(StrEnum):
    openclaw = "openclaw"
    claude_code = "claude_code"
    codex = "codex"
    manual = "manual"


class DiscordEventType(StrEnum):
    approval_requested = "approval_requested"
    run_blocked = "run_blocked"
    budget_threshold_hit = "budget_threshold_hit"
    run_completed = "run_completed"


class ApprovalStatus(StrEnum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"


class ArtifactRef(BaseModel):
    kind: ArtifactKind = ArtifactKind.markdown
    path: str
    description: str | None = None


class ContextBundle(BaseModel):
    bundle_id: str
    mission: str
    constraints: list[str] = Field(default_factory=list)
    evidence_refs: list[ArtifactRef] = Field(default_factory=list)
    glossary: dict[str, str] = Field(default_factory=dict)
    latest_decisions: list[str] = Field(default_factory=list)


class PMTask(BaseModel):
    task_id: str
    title: str
    objective: str
    steps: list[str] = Field(default_factory=list)
    acceptance_criteria: list[str] = Field(default_factory=list)
    executor_type: ExecutorType = ExecutorType.openclaw
    budget_cap: float = 0.0
    approval_required: bool = False
    priority: Literal["low", "medium", "high"] = "medium"
    artifact_output_path: str | None = None
    evidence_refs: list[ArtifactRef] = Field(default_factory=list)
    constraints: list[str] = Field(default_factory=list)


class PMEpic(BaseModel):
    epic_id: str
    title: str
    summary: str = ""
    acceptance_criteria: list[str] = Field(default_factory=list)
    budget_cap: float = 0.0
    approval_required: bool = False
    executor_type: ExecutorType = ExecutorType.openclaw
    tasks: list[PMTask] = Field(default_factory=list)
    constraints: list[str] = Field(default_factory=list)
    evidence_refs: list[ArtifactRef] = Field(default_factory=list)


class PMSpec(BaseModel):
    goal_id: str
    mission: str
    initiative_id: str
    initiative_title: str
    summary: str = ""
    constraints: list[str] = Field(default_factory=list)
    glossary: dict[str, str] = Field(default_factory=dict)
    latest_decisions: list[str] = Field(default_factory=list)
    epics: list[PMEpic] = Field(default_factory=list)
    artifact_root: str = "ops/artifacts"


class TaskEnvelope(BaseModel):
    envelope_id: str
    goal_id: str
    initiative_id: str
    initiative_title: str
    epic_id: str
    task_id: str
    title: str
    executor_type: ExecutorType
    budget_cap: float
    acceptance_criteria: list[str] = Field(default_factory=list)
    context_bundle_ref: str
    artifact_output_path: str
    approval_required: bool = False
    mission: str
    objective: str
    steps: list[str] = Field(default_factory=list)
    constraints: list[str] = Field(default_factory=list)
    evidence_refs: list[ArtifactRef] = Field(default_factory=list)
    priority: Literal["low", "medium", "high"] = "medium"


class PaperclipRunRequest(BaseModel):
    request_id: str
    company_id: str
    goal_id: str
    initiative_id: str
    epic_id: str
    task_id: str
    title: str
    summary: str
    executor_type: ExecutorType
    budget_cap: float
    approval_required: bool
    context_bundle_ref: str
    artifact_output_path: str
    metadata: dict[str, str] = Field(default_factory=dict)


class ApprovalRecord(BaseModel):
    approval_id: str
    status: ApprovalStatus = ApprovalStatus.pending
    title: str
    summary: str
    task_envelope_ref: str
    requested_by: str = "ai_os"
    decided_by: str | None = None
    notes: str | None = None


class DiscordEvent(BaseModel):
    event_id: str
    event_type: DiscordEventType
    title: str
    summary: str
    task_envelope_ref: str | None = None
    approval_id: str | None = None
    metadata: dict[str, str] = Field(default_factory=dict)


class ForecastRequest(BaseModel):
    request_id: str
    seed_material_refs: list[ArtifactRef] = Field(default_factory=list)
    decision_question: str
    time_horizon: str
    scenario_prompt: str


class ForecastReport(BaseModel):
    report_id: str
    request_id: str
    scenario_summary: str
    key_drivers: list[str] = Field(default_factory=list)
    risk_signals: list[str] = Field(default_factory=list)
    roadmap_implications: list[str] = Field(default_factory=list)
