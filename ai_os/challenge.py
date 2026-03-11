"""Challenge Agent - Adversarial Testing & Critical Analysis

This module implements the Challenge Agent functionality for questioning
assumptions, stress-testing designs, and identifying weaknesses.
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import StrEnum
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

from .fs_utils import ensure_dir, write_json


class ChallengeSeverity(StrEnum):
    CRITICAL = "critical"
    MAJOR = "major"
    MINOR = "minor"


class ChallengeCategory(StrEnum):
    ASSUMPTIONS = "assumptions"
    EDGE_CASES = "edge_cases"
    FAILURE_MODES = "failure_modes"
    SECURITY = "security"
    SCALABILITY = "scalability"
    COMPLETENESS = "completeness"


class ChallengeIssue(BaseModel):
    issue_id: str
    category: ChallengeCategory
    severity: ChallengeSeverity
    title: str
    description: str
    impact: str
    recommendation: str
    target_component: str | None = None


class ChallengeReport(BaseModel):
    report_id: str
    target_name: str
    target_type: str  # code, design, strategy, document
    challenge_type: str  # assumptions, edge_cases, failure_modes, security
    depth_level: str = "medium"  # surface, medium, deep
    issues: list[ChallengeIssue] = Field(default_factory=list)
    questions: list[str] = Field(default_factory=list)
    alternatives_considered: list[str] = Field(default_factory=list)
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class StressTestScenario(BaseModel):
    scenario_id: str
    name: str
    description: str
    load_factor: float = 1.0
    failure_injection: str | None = None
    expected_behavior: str


def _get_challenges_path(repo_root: Path) -> Path:
    return ensure_dir(repo_root / "ops/challenges")


def _get_reports_path(repo_root: Path) -> Path:
    return ensure_dir(_get_challenges_path(repo_root) / "reports")


def _get_stress_tests_path(repo_root: Path) -> Path:
    return ensure_dir(_get_challenges_path(repo_root) / "stress_tests")


def _load_report_index(repo_root: Path) -> dict[str, str]:
    index_path = _get_reports_path(repo_root) / "index.json"
    if index_path.exists():
        import json
        return json.loads(index_path.read_text(encoding="utf-8"))
    return {}


def _save_report_index(repo_root: Path, index: dict[str, str]) -> None:
    index_path = _get_reports_path(repo_root) / "index.json"
    import json
    write_json(index_path, index)


def create_challenge_report(
    repo_root: Path,
    target_name: str,
    target_type: str,
    challenge_type: str,
    depth_level: str = "medium",
) -> ChallengeReport:
    """Create a new challenge report for adversarial testing."""
    index = _load_report_index(repo_root)
    report_num = len(index) + 1
    report_id = f"challenge-{report_num:04d}"

    report = ChallengeReport(
        report_id=report_id,
        target_name=target_name,
        target_type=target_type,
        challenge_type=challenge_type,
        depth_level=depth_level,
    )

    # Save report
    report_path = _get_reports_path(repo_root) / f"{report_id}.json"
    write_json(report_path, report.model_dump(mode="json"))

    # Update index
    index[report_id] = str(report_path)
    _save_report_index(repo_root, index)

    return report


def add_challenge_issue(
    repo_root: Path,
    report_id: str,
    category: str,
    severity: str,
    title: str,
    description: str,
    impact: str,
    recommendation: str,
    target_component: str | None = None,
) -> ChallengeIssue:
    """Add an issue to an existing challenge report."""
    report_path = _get_reports_path(repo_root) / f"{report_id}.json"

    if not report_path.exists():
        raise ValueError(f"Report {report_id} not found")

    import json
    report_data = json.loads(report_path.read_text(encoding="utf-8"))
    report = ChallengeReport.model_validate(report_data)

    issue_num = len(report.issues) + 1
    issue_id = f"{report_id}-issue-{issue_num:02d}"

    issue = ChallengeIssue(
        issue_id=issue_id,
        category=ChallengeCategory(category),
        severity=ChallengeSeverity(severity),
        title=title,
        description=description,
        impact=impact,
        recommendation=recommendation,
        target_component=target_component,
    )

    report.issues.append(issue)

    # Save updated report
    write_json(report_path, report.model_dump(mode="json"))

    return issue


def add_challenge_question(
    repo_root: Path,
    report_id: str,
    question: str,
) -> None:
    """Add a question to a challenge report for further investigation."""
    report_path = _get_reports_path(repo_root) / f"{report_id}.json"

    if not report_path.exists():
        raise ValueError(f"Report {report_id} not found")

    import json
    report_data = json.loads(report_path.read_text(encoding="utf-8"))
    report = ChallengeReport.model_validate(report_data)

    report.questions.append(question)

    write_json(report_path, report.model_dump(mode="json"))


def add_alternative(
    repo_root: Path,
    report_id: str,
    alternative: str,
) -> None:
    """Add an alternative approach considered during challenge analysis."""
    report_path = _get_reports_path(repo_root) / f"{report_id}.json"

    if not report_path.exists():
        raise ValueError(f"Report {report_id} not found")

    import json
    report_data = json.loads(report_path.read_text(encoding="utf-8"))
    report = ChallengeReport.model_validate(report_data)

    report.alternatives_considered.append(alternative)

    write_json(report_path, report.model_dump(mode="json"))


def get_challenge_report(repo_root: Path, report_id: str) -> ChallengeReport | None:
    """Retrieve a challenge report by ID."""
    report_path = _get_reports_path(repo_root) / f"{report_id}.json"

    if not report_path.exists():
        return None

    import json
    report_data = json.loads(report_path.read_text(encoding="utf-8"))
    return ChallengeReport.model_validate(report_data)


def get_all_reports(repo_root: Path) -> list[ChallengeReport]:
    """Get all challenge reports."""
    reports_path = _get_reports_path(repo_root)
    reports = []

    for report_file in reports_path.glob("*.json"):
        if report_file.name == "index.json":
            continue
        import json
        report_data = json.loads(report_file.read_text(encoding="utf-8"))
        reports.append(ChallengeReport.model_validate(report_data))

    return sorted(reports, key=lambda r: r.created_at, reverse=True)


def get_reports_by_severity(
    repo_root: Path,
    severity: str,
) -> list[ChallengeReport]:
    """Get challenge reports filtered by severity level."""
    all_reports = get_all_reports(repo_root)
    return [
        r for r in all_reports
        if any(issue.severity == severity for issue in r.issues)
    ]


def create_stress_test_scenario(
    repo_root: Path,
    name: str,
    description: str,
    load_factor: float = 1.0,
    failure_injection: str | None = None,
    expected_behavior: str = "",
) -> StressTestScenario:
    """Create a stress test scenario for chaos engineering."""
    index_path = _get_stress_tests_path(repo_root) / "index.json"

    if index_path.exists():
        import json
        index = json.loads(index_path.read_text(encoding="utf-8"))
    else:
        index = {}

    scenario_num = len(index) + 1
    scenario_id = f"stress-{scenario_num:03d}"

    scenario = StressTestScenario(
        scenario_id=scenario_id,
        name=name,
        description=description,
        load_factor=load_factor,
        failure_injection=failure_injection,
        expected_behavior=expected_behavior,
    )

    # Save scenario
    scenario_path = _get_stress_tests_path(repo_root) / f"{scenario_id}.json"
    write_json(scenario_path, scenario.model_dump(mode="json"))

    # Update index
    index[scenario_id] = str(scenario_path)
    write_json(index_path, index)

    return scenario


def get_stress_test_scenarios(repo_root: Path) -> list[StressTestScenario]:
    """Get all stress test scenarios."""
    stress_path = _get_stress_tests_path(repo_root)
    scenarios = []

    for scenario_file in stress_path.glob("*.json"):
        if scenario_file.name == "index.json":
            continue
        import json
        data = json.loads(scenario_file.read_text(encoding="utf-8"))
        scenarios.append(StressTestScenario.model_validate(data))

    return sorted(scenarios, key=lambda s: s.scenario_id)


# Convenient function for quick adversarial testing
def quick_challenge(
    repo_root: Path,
    target_name: str,
    target_type: str,
    assumptions: list[str],
) -> ChallengeReport:
    """Quick challenge - create a report and add assumption-based issues."""
    report = create_challenge_report(
        repo_root=repo_root,
        target_name=target_name,
        target_type=target_type,
        challenge_type="assumptions",
        depth_level="surface",
    )

    for i, assumption in enumerate(assumptions):
        add_challenge_issue(
            repo_root=repo_root,
            report_id=report.report_id,
            category="assumptions",
            severity="minor" if i > 2 else "major",
            title=f"Assumption: {assumption}",
            description=f"This assumption may not hold in all scenarios: {assumption}",
            impact="If false, the target design may fail in specific conditions",
            recommendation=f"Verify '{assumption}' through testing or validation",
        )
        add_challenge_question(
            repo_root=repo_root,
            report_id=report.report_id,
            question=f"What if '{assumption}' is completely wrong?",
        )

    return report
