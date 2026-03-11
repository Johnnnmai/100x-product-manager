from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any
from functools import lru_cache

import yaml

# Try to use C-based YAML loader for better performance
try:
    from yaml import CSafeLoader as SafeLoader, CSafeDumper as SafeDumper
except ImportError:
    from yaml import SafeLoader, SafeDumper

# Cache for file existence checks
_exists_cache: dict[str, float] = {}
_EXISTS_CACHE_TTL = 1.0


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_json(path: Path, payload: Any) -> Path:
    ensure_dir(path.parent)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


@lru_cache(maxsize=128)
def _cached_load_yaml(path_str: str) -> dict[str, Any]:
    """Cached YAML loading for frequently accessed files."""
    resolved_path = Path(path_str)
    return yaml.load(resolved_path.read_text(encoding="utf-8"), Loader=SafeLoader)


def load_yaml(path: str | os.PathLike[str] | Path) -> dict[str, Any]:
    path_str = str(path)
    # Use caching for repeated loads of the same file
    try:
        return _cached_load_yaml(path_str)
    except Exception:
        # Fallback to non-cached version if caching fails
        resolved_path = Path(path)
        return yaml.load(resolved_path.read_text(encoding="utf-8"), Loader=SafeLoader)


def to_repo_path(path: Path, repo_root: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "task"
