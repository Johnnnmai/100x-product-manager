from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

from .fs_utils import load_yaml


class WorkspaceSpec(BaseModel):
    name: str | None = None
    cwd: str | None = None
    repo_url: str | None = None
    repo_ref: str | None = None
    is_primary: bool = True
    metadata: dict[str, str] = Field(default_factory=dict)


class IssueSeed(BaseModel):
    key: str
    title: str
    description: str
    assignee_role: str
    priority: Literal["critical", "high", "medium", "low"] = "medium"
    status: Literal["backlog", "todo"] = "todo"
    goal_id: str | None = None
    billing_code: str | None = None
    request_depth: int | None = None
    children: list["IssueSeed"] = Field(default_factory=list)


class ProjectSpec(BaseModel):
    key: str
    name: str
    description: str | None = None
    status: Literal["planned", "active", "paused", "completed", "archived"] = "planned"
    color: str | None = None
    target_date: str | None = None
    lead_role: str | None = None
    billing_code: str | None = None
    workspace: WorkspaceSpec | None = None
    secondary_workspaces: list[WorkspaceSpec] = Field(default_factory=list)
    background_paths: list[str] = Field(default_factory=list)
    issue_seeds: list[IssueSeed] = Field(default_factory=list)


class PortfolioDefaults(BaseModel):
    project_status: Literal["planned", "active", "paused", "completed", "archived"] = "planned"
    issue_status: Literal["backlog", "todo"] = "todo"
    billing_code_prefix: str = "PORTFOLIO"


class CompanyPortfolio(BaseModel):
    company: str
    version: int = 1
    defaults: PortfolioDefaults = Field(default_factory=PortfolioDefaults)
    projects: list[ProjectSpec] = Field(default_factory=list)


IssueSeed.model_rebuild()


def load_company_portfolio(path: Path) -> CompanyPortfolio:
    return CompanyPortfolio.model_validate(load_yaml(path))
