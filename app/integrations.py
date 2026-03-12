from __future__ import annotations

import os
from typing import Any
from urllib.parse import urlparse

import httpx
from bs4 import BeautifulSoup

from app.models import SignalItem, TaskItem


class ScraplingAdapter:
    def __init__(self) -> None:
        self.enabled = os.getenv("SCRAPLING_ENABLED", "false").lower() == "true"

    async def collect(self, url: str | None, idea: str | None, context: str | None) -> list[SignalItem]:
        signals: list[SignalItem] = []
        if url:
            signals.extend(await self._collect_from_url(url))
        if idea:
            signals.append(
                SignalItem(
                    source="idea_input",
                    title="Founder idea",
                    summary=idea[:280],
                    confidence=0.55,
                )
            )
        if context:
            signals.append(
                SignalItem(
                    source="context_input",
                    title="Additional context",
                    summary=context[:280],
                    confidence=0.5,
                )
            )
        if not signals:
            signals.append(
                SignalItem(
                    source="fallback",
                    title="No external evidence configured",
                    summary="Running in local mode with user-provided inputs only.",
                    confidence=0.35,
                )
            )
        return signals

    async def _collect_from_url(self, url: str) -> list[SignalItem]:
        try:
            async with httpx.AsyncClient(timeout=8, follow_redirects=True) as client:
                response = await client.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            title = (soup.title.string or url).strip() if soup.title else url
            paragraphs = " ".join(p.get_text(" ", strip=True) for p in soup.find_all("p")[:8])
            hostname = urlparse(url).netloc or "website"
            return [
                SignalItem(
                    source=hostname,
                    title=title[:120],
                    summary=(paragraphs[:400] or f"Collected landing-page level copy from {hostname}."),
                    confidence=0.7,
                )
            ]
        except Exception:
            return [
                SignalItem(
                    source="url_fetch",
                    title="URL fetch fallback",
                    summary=f"Could not fetch live content from {url}. Proceeding with URL-level analysis only.",
                    confidence=0.4,
                )
            ]


class OasisAdapter:
    def __init__(self) -> None:
        self.enabled = os.getenv("OASIS_ENABLED", "false").lower() == "true"

    async def simulate(self, mode: str, signals: list[SignalItem]) -> dict[str, Any]:
        themes = [s.title for s in signals[:3]]
        return {
            "engine": "oasis" if self.enabled else "local-sim",
            "audience_reaction": "curious but selective",
            "spread_potential": "medium",
            "retention_risk": "high if first value is delayed",
            "observed_themes": themes,
        }


class MiroFishAdapter:
    def __init__(self) -> None:
        self.enabled = os.getenv("MIROFISH_ENABLED", "false").lower() == "true"

    async def forecast(self, strategy_memo: dict[str, Any]) -> dict[str, Any]:
        return {
            "engine": "mirofish" if self.enabled else "disabled",
            "note": "Advanced forecasting is optional in v1.",
            "priority_scenarios": [
                "narrow wedge converts strongly",
                "broad positioning confuses users",
                "distribution fails without a repeatable signal loop",
            ],
        }


class PaperclipAdapter:
    def __init__(self) -> None:
        self.enabled = os.getenv("PAPERCLIP_ENABLED", "false").lower() == "true"

    async def export_tasks(self, tasks: list[TaskItem]) -> dict[str, Any]:
        return {
            "engine": "paperclip" if self.enabled else "local-export",
            "tasks": [task.model_dump() for task in tasks],
        }
