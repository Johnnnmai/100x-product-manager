"""Memory System - Organization Learning and Knowledge Management"""

from __future__ import annotations

import json
import threading
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field


class LessonEntry(BaseModel):
    id: str
    date: str
    category: str
    title: str
    what_worked: str
    what_didnt: str
    action_items: list[str] = Field(default_factory=list)
    confidence: float = 0.5


class SignalEntry(BaseModel):
    signal_id: str
    date: str
    predicted_outcome: str
    actual_outcome: str
    accuracy: bool
    lessons: str


class ExperimentEntry(BaseModel):
    experiment_id: str
    date: str
    hypothesis: str
    result: str
    metrics: dict[str, float] = Field(default_factory=dict)
    conclusion: str


class MemoryStore(BaseModel):
    version: str = "1.0"
    last_updated: str
    lessons: list[LessonEntry] = Field(default_factory=list)
    signals: list[SignalEntry] = Field(default_factory=list)
    experiments: list[ExperimentEntry] = Field(default_factory=list)


class MemorySystem:
    """Organization memory management system for AI Revenue Flywheel"""

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.memory_dir = repo_root / "ops" / "memory"
        self.lessons_file = self.memory_dir / "lessons-learned.json"
        self.signals_file = self.memory_dir / "signal-history.json"
        self.experiments_file = self.memory_dir / "experiment-results.json"
        # In-memory cache for performance
        self._cache: dict[str, tuple[float, dict[str, Any]]] = {}
        self._lock = threading.Lock()
        self._cache_ttl = 5.0  # Cache TTL in seconds

    def _load_json(self, path: Path) -> dict[str, Any]:
        if not path.exists():
            return {"version": "1.0", "last_updated": datetime.now(UTC).isoformat()}

        # Check cache first
        path_str = str(path)
        now = datetime.now(UTC).timestamp()
        with self._lock:
            if path_str in self._cache:
                cached_time, cached_data = self._cache[path_str]
                if now - cached_time < self._cache_ttl:
                    return cached_data.copy()

        # Load from file
        data = json.loads(path.read_text(encoding="utf-8"))

        # Update cache
        with self._lock:
            self._cache[path_str] = (now, data.copy())

        return data

    def _save_json(self, path: Path, data: dict[str, Any]) -> None:
        data["last_updated"] = datetime.now(UTC).isoformat()
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

        # Invalidate cache
        with self._lock:
            self._cache.pop(str(path), None)

    def add_lesson(self, category: str, title: str, what_worked: str, what_didnt: str, action_items: list[str] | None = None, confidence: float = 0.5) -> LessonEntry:
        """Add a new lesson to the memory store"""
        data = self._load_json(self.lessons_file)
        lessons = data.get("lessons", [])
        lesson_id = f"lesson-{len(lessons) + 1:03d}"

        entry = LessonEntry(
            id=lesson_id,
            date=datetime.now(UTC).isoformat()[:10],
            category=category,
            title=title,
            what_worked=what_worked,
            what_didnt=what_didnt,
            action_items=action_items or [],
            confidence=confidence,
        )
        lessons.append(entry.model_dump())
        data["lessons"] = lessons
        self._save_json(self.lessons_file, data)
        return entry

    def add_signal(self, predicted_outcome: str, actual_outcome: str, lessons: str) -> SignalEntry:
        """Record a signal detection result for future accuracy tracking"""
        data = self._load_json(self.signals_file)
        signals = data.get("signals", [])
        signal_id = f"signal-{len(signals) + 1:03d}"

        accuracy = predicted_outcome.lower().strip() == actual_outcome.lower().strip()

        entry = SignalEntry(
            signal_id=signal_id,
            date=datetime.now(UTC).isoformat()[:10],
            predicted_outcome=predicted_outcome,
            actual_outcome=actual_outcome,
            accuracy=accuracy,
            lessons=lessons,
        )
        signals.append(entry.model_dump())
        data["signals"] = signals
        self._save_json(self.signals_file, data)
        return entry

    def add_experiment(self, hypothesis: str, result: str, metrics: dict[str, float], conclusion: str) -> ExperimentEntry:
        """Record an experiment result"""
        data = self._load_json(self.experiments_file)
        experiments = data.get("experiments", [])
        experiment_id = f"exp-{len(experiments) + 1:03d}"

        entry = ExperimentEntry(
            experiment_id=experiment_id,
            date=datetime.now(UTC).isoformat()[:10],
            hypothesis=hypothesis,
            result=result,
            metrics=metrics,
            conclusion=conclusion,
        )
        experiments.append(entry.model_dump())
        data["experiments"] = experiments
        self._save_json(self.experiments_file, data)
        return entry

    def get_recent_lessons(self, category: str | None = None, limit: int = 10) -> list[LessonEntry]:
        """Retrieve recent lessons, optionally filtered by category"""
        data = self._load_json(self.lessons_file)
        lessons_data = data.get("lessons", [])
        lessons = [LessonEntry(**l) for l in lessons_data]

        if category:
            lessons = [l for l in lessons if l.category == category]

        return lessons[-limit:]

    def get_signal_accuracy(self) -> float:
        """Calculate overall signal detection accuracy"""
        data = self._load_json(self.signals_file)
        signals_data = data.get("signals", [])
        if not signals_data:
            return 0.0

        signals = [SignalEntry(**s) for s in signals_data]
        accurate = sum(1 for s in signals if s.accuracy)
        return accurate / len(signals)

    def get_all_lessons(self) -> list[LessonEntry]:
        """Get all lessons"""
        data = self._load_json(self.lessons_file)
        return [LessonEntry(**l) for l in data.get("lessons", [])]


def get_memory_system(repo_root: Path | str) -> MemorySystem:
    """Factory function to get MemorySystem instance"""
    if isinstance(repo_root, str):
        repo_root = Path(repo_root)
    return MemorySystem(repo_root)
