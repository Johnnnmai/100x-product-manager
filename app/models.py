from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, HttpUrl


class RunMode(str, Enum):
    AUDIT = "audit"
    SHAPE = "shape"


class RunRequest(BaseModel):
    project_name: str = Field(min_length=2, max_length=80)
    mode: RunMode
    url: HttpUrl | None = None
    idea: str | None = Field(default=None, max_length=6000)
    context: str | None = Field(default=None, max_length=12000)


class SignalItem(BaseModel):
    source: str
    title: str
    summary: str
    confidence: float = Field(ge=0.0, le=1.0)


class ValidationLayer(BaseModel):
    layer: int
    claim: str
    risk: str
    signal_needed: str


class TaskItem(BaseModel):
    title: str
    owner: str
    description: str
    priority: str
    status: str = "todo"


class DecisionPack(BaseModel):
    project_name: str
    run_id: str
    mode: RunMode
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    executive_summary: str
    signal_brief: list[SignalItem]
    problem_map: list[str]
    conditional_validation_stack: list[ValidationLayer]
    strategy_memo: dict[str, Any]
    prd: dict[str, Any]
    roadmap: list[dict[str, Any]]
    tasks: list[TaskItem]
    simulation_summary: dict[str, Any]
    metadata: dict[str, Any] = Field(default_factory=dict)
