from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

from .contracts import ArtifactKind, ArtifactRef
from .fs_utils import ensure_dir, slugify, to_repo_path, write_json

try:
    from scrapling.fetchers import Fetcher
except ImportError:  # pragma: no cover - optional at runtime
    Fetcher = None


def _fetch_with_scrapling(url: str) -> dict[str, Any]:
    if Fetcher is None:
        raise RuntimeError("Scrapling is not available")

    fetcher = Fetcher()
    response = fetcher.get(url, verify=False)
    title = ""
    if hasattr(response, "css"):
        title = response.css("title::text").get(default="") or ""
    return {
        "engine": "scrapling",
        "url": getattr(response, "url", url),
        "status": getattr(response, "status", None),
        "title": title.strip(),
        "html": str(getattr(response, "html_content", "")),
    }


def _fetch_with_requests(url: str) -> dict[str, Any]:
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    title = ""
    if "<title>" in response.text.lower():
        lower = response.text.lower()
        start = lower.find("<title>")
        end = lower.find("</title>", start)
        if start != -1 and end != -1:
            title = response.text[start + 7 : end].strip()
    return {
        "engine": "requests",
        "url": response.url,
        "status": response.status_code,
        "title": title,
        "html": response.text,
    }


def ingest_url(url: str, repo_root: Path, slug: str | None = None) -> ArtifactRef:
    raw_dir = ensure_dir(repo_root / "ops/evidence/raw")
    processed_dir = ensure_dir(repo_root / "ops/evidence/processed")
    artifact_slug = slugify(slug or url)

    try:
        payload = _fetch_with_scrapling(url)
    except Exception:
        payload = _fetch_with_requests(url)

    html_path = raw_dir / f"{artifact_slug}.html"
    html_path.write_text(payload["html"], encoding="utf-8")

    manifest = {
        "url": payload["url"],
        "title": payload["title"],
        "status": payload["status"],
        "engine": payload["engine"],
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "html_path": to_repo_path(html_path, repo_root),
    }
    manifest_path = write_json(processed_dir / f"{artifact_slug}.json", manifest)
    return ArtifactRef(
        kind=ArtifactKind.evidence,
        path=to_repo_path(manifest_path, repo_root),
        description=payload["title"] or payload["url"],
    )
