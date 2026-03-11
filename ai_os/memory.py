from __future__ import annotations

import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from functools import lru_cache

from pydantic import BaseModel, Field

from .fs_utils import ensure_dir, write_json


# Thread lock for concurrent write safety
_write_lock = threading.Lock()

# Simple in-memory cache for memory index to reduce file I/O
# Cache is scoped to each process invocation
_index_cache: dict[str, tuple[float, MemoryIndex]] = {}
_CACHE_TTL_SECONDS = 5.0  # Cache TTL in seconds


class MemoryEntry(BaseModel):
    entry_id: str
    category: str  # lesson, decision, pattern, insight
    title: str
    content: str
    tags: list[str] = Field(default_factory=list)
    source_task_id: str | None = None
    source_envelope_id: str | None = None
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    metadata: dict[str, Any] = Field(default_factory=dict)


class MemoryIndex(BaseModel):
    entries: dict[str, MemoryEntry] = Field(default_factory=dict)
    last_updated: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


def _get_memory_path(repo_root: Path) -> Path:
    return ensure_dir(repo_root / "ops/memory")


def _get_index_path(repo_root: Path) -> Path:
    return _get_memory_path(repo_root) / "index.json"


def _load_index(repo_root: Path) -> MemoryIndex:
    """Load memory index with simple caching."""
    import time
    index_path = _get_index_path(repo_root)
    cache_key = str(index_path.resolve())

    # Check cache
    now = time.time()
    if cache_key in _index_cache:
        cached_time, cached_index = _index_cache[cache_key]
        if now - cached_time < _CACHE_TTL_SECONDS:
            return cached_index

    # Load from file
    if index_path.exists():
        index = MemoryIndex.model_validate_json(index_path.read_text(encoding="utf-8"))
    else:
        index = MemoryIndex()

    # Update cache
    _index_cache[cache_key] = (now, index)
    return index


def _save_index(repo_root: Path, index: MemoryIndex) -> None:
    """Save memory index and invalidate cache."""
    index.last_updated = datetime.now(timezone.utc).isoformat()
    index_path = _get_index_path(repo_root)
    write_json(index_path, index.model_dump(mode="json"))

    # Invalidate cache
    cache_key = str(index_path.resolve())
    _index_cache.pop(cache_key, None)


def flush_all_writes() -> None:
    """No-op for backwards compatibility. Kept for API compatibility."""
    pass


def add_memory_entry(
    repo_root: Path,
    category: str,
    title: str,
    content: str,
    tags: list[str] | None = None,
    source_task_id: str | None = None,
    source_envelope_id: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> MemoryEntry:
    """Add a new memory entry to the organizational memory."""
    with _write_lock:
        index = _load_index(repo_root)

        entry_id = f"{category}__{len(index.entries) + 1:04d}"
        entry = MemoryEntry(
            entry_id=entry_id,
            category=category,
            title=title,
            content=content,
            tags=tags or [],
            source_task_id=source_task_id,
            source_envelope_id=source_envelope_id,
            metadata=metadata or {},
        )

        index.entries[entry_id] = entry
        _save_index(repo_root, index)

        # Also write individual entry file
        entry_path = _get_memory_path(repo_root) / f"{entry_id}.json"
        write_json(entry_path, entry.model_dump(mode="json"))

        return entry


def get_memory_entries(
    repo_root: Path,
    category: str | None = None,
    tags: list[str] | None = None,
) -> list[MemoryEntry]:
    """Retrieve memory entries, optionally filtered by category or tags."""
    index = _load_index(repo_root)
    entries = list(index.entries.values())

    if category:
        entries = [e for e in entries if e.category == category]

    if tags:
        entries = [e for e in entries if any(tag in e.tags for tag in tags)]

    return sorted(entries, key=lambda e: e.created_at, reverse=True)


def search_memory(repo_root: Path, query: str) -> list[MemoryEntry]:
    """Search memory entries by keyword in title or content."""
    index = _load_index(repo_root)
    query_lower = query.lower()

    return [
        entry
        for entry in index.entries.values()
        if query_lower in entry.title.lower() or query_lower in entry.content.lower()
    ]


def record_lesson_learned(
    repo_root: Path,
    title: str,
    lesson: str,
    source_task_id: str | None = None,
) -> MemoryEntry:
    """Convenience function to record a lesson learned."""
    return add_memory_entry(
        repo_root=repo_root,
        category="lesson",
        title=title,
        content=lesson,
        tags=["lesson", "learning"],
        source_task_id=source_task_id,
    )


def record_decision(
    repo_root: Path,
    title: str,
    rationale: str,
    source_task_id: str | None = None,
) -> MemoryEntry:
    """Convenience function to record a decision made."""
    return add_memory_entry(
        repo_root=repo_root,
        category="decision",
        title=title,
        content=rationale,
        tags=["decision", "rationale"],
        source_task_id=source_task_id,
    )
