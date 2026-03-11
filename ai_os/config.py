from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    github_username: str | None
    github_org_name: str | None
    github_auth_user: str | None
    github_browser_profile_dir: str | None
    discord_bot_token: str | None
    discord_channel_id: str | None
    paperclip_company_id: str
    paperclip_gateway_url: str | None
    openclaw_pending_dir: Path
    openclaw_compiled_dir: Path
    openclaw_reports_dir: Path
    approvals_dir: Path
    context_dir: Path
    context_cache_dir: Path
    evidence_dir: Path
    paperclip_outbox_dir: Path
    strategy_lab_dir: Path


def load_settings(repo_root: Path | None = None) -> Settings:
    root = Path("." if repo_root is None else repo_root)
    return Settings(
        github_username=os.getenv("GITHUB_USERNAME"),
        github_org_name=os.getenv("GITHUB_ORG_NAME"),
        github_auth_user=os.getenv("GITHUB_AUTH_USER"),
        github_browser_profile_dir=os.getenv("GITHUB_BROWSER_PROFILE_DIR"),
        discord_bot_token=os.getenv("DISCORD_BOT_TOKEN"),
        discord_channel_id=os.getenv("DISCORD_CHANNEL_ID"),
        paperclip_company_id=os.getenv("PAPERCLIP_COMPANY_ID", "default-company"),
        paperclip_gateway_url=os.getenv("PAPERCLIP_GATEWAY_URL"),
        openclaw_pending_dir=root / os.getenv("OPENCLAW_PENDING_DIR", "ops/tasks/pending"),
        openclaw_compiled_dir=root / os.getenv("OPENCLAW_COMPILED_DIR", "ops/tasks/compiled"),
        openclaw_reports_dir=root / os.getenv("OPENCLAW_REPORTS_DIR", "ops/reports"),
        approvals_dir=root / os.getenv("AI_OS_APPROVALS_DIR", "ops/approvals"),
        context_dir=root / os.getenv("AI_OS_CONTEXT_DIR", "ops/context_bundles"),
        context_cache_dir=root / os.getenv("AI_OS_CONTEXT_CACHE_DIR", "ops/context_cache"),
        evidence_dir=root / os.getenv("AI_OS_EVIDENCE_DIR", "ops/evidence"),
        paperclip_outbox_dir=root / os.getenv(
            "AI_OS_PAPERCLIP_OUTBOX_DIR",
            "ops/paperclip/outbox",
        ),
        strategy_lab_dir=root / os.getenv("AI_OS_STRATEGY_LAB_DIR", "ops/strategy_lab"),
    )
