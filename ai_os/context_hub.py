from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from .fs_utils import ensure_dir


def is_chub_installed() -> bool:
    return shutil.which("chub") is not None


def fetch_doc(
    doc_id: str,
    lang: str,
    repo_root: Path,
    extra_args: list[str] | None = None,
) -> Path:
    if not is_chub_installed():
        raise RuntimeError("Context Hub CLI not found. Install with: npm install -g @aisuite/chub")

    args = ["chub", "get", doc_id, "--lang", lang]
    if extra_args:
        args.extend(extra_args)
    output = subprocess.run(args, check=True, capture_output=True, text=True)
    cache_dir = ensure_dir(repo_root / "ops/context_cache")
    cache_name = doc_id.replace("/", "__")
    cache_path = cache_dir / f"{cache_name}__{lang}.md"
    cache_path.write_text(output.stdout, encoding="utf-8")
    return cache_path
