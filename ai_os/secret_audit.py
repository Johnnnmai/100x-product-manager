from __future__ import annotations

import re
from pathlib import Path

from pydantic import BaseModel

from .fs_utils import to_repo_path


SECRET_PATTERNS = {
    "github_pat": re.compile(r"gh[pousr]_[A-Za-z0-9]{20,255}"),
    "discord_bot_token": re.compile(
        r"\b[A-Za-z0-9_-]{20,32}\.[A-Za-z0-9_-]{6,8}\.[A-Za-z0-9_-]{20,}\b"
    ),
}

IGNORED_DIRS = {".git", "__pycache__", ".venv", "node_modules"}


class SecretFinding(BaseModel):
    secret_type: str
    path: str
    line_no: int
    line_preview: str


def iter_files(repo_root: Path) -> list[Path]:
    files: list[Path] = []
    for path in repo_root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        files.append(path)
    return files


def scan_repo(repo_root: Path) -> list[SecretFinding]:
    findings: list[SecretFinding] = []
    for path in iter_files(repo_root):
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_no, line in enumerate(content.splitlines(), start=1):
            for secret_type, pattern in SECRET_PATTERNS.items():
                if pattern.search(line):
                    findings.append(
                        SecretFinding(
                            secret_type=secret_type,
                            path=to_repo_path(path, repo_root),
                            line_no=line_no,
                            line_preview=line.strip(),
                        )
                    )
    return findings
