"""Unit tests for Challenge Agent module."""

import tempfile
from pathlib import Path

import pytest

from ai_os.challenge import (
    ChallengeCategory,
    ChallengeReport,
    ChallengeSeverity,
    StressTestScenario,
    add_alternative,
    add_challenge_issue,
    add_challenge_question,
    create_challenge_report,
    create_stress_test_scenario,
    get_all_reports,
    get_challenge_report,
    get_reports_by_severity,
    get_stress_test_scenarios,
    quick_challenge,
)


@pytest.fixture
def temp_repo():
    """Create a temporary repo directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo = Path(tmpdir)
        # Create ops/challenges structure
        (repo / "ops/challenges/reports").mkdir(parents=True)
        (repo / "ops/challenges/stress_tests").mkdir(parents=True)
        yield repo


def test_create_challenge_report(temp_repo):
    """Test creating a challenge report."""
    report = create_challenge_report(
        repo_root=temp_repo,
        target_name="Test Component",
        target_type="code",
        challenge_type="assumptions",
        depth_level="deep",
    )

    assert report.report_id == "challenge-0001"
    assert report.target_name == "Test Component"
    assert report.target_type == "code"
    assert report.challenge_type == "assumptions"
    assert report.depth_level == "deep"
    assert len(report.issues) == 0


def test_add_challenge_issue(temp_repo):
    """Test adding an issue to a challenge report."""
    report = create_challenge_report(
        repo_root=temp_repo,
        target_name="API Design",
        target_type="design",
        challenge_type="security",
    )

    issue = add_challenge_issue(
        repo_root=temp_repo,
        report_id=report.report_id,
        category="security",
        severity="critical",
        title="SQL Injection Vulnerability",
        description="User input not sanitized in query builder",
        impact="Attackers can execute arbitrary SQL commands",
        recommendation="Use parameterized queries",
        target_component="database.py",
    )

    assert issue.issue_id == f"{report.report_id}-issue-01"
    assert issue.severity == ChallengeSeverity.CRITICAL
    assert issue.category == ChallengeCategory.SECURITY

    # Verify saved to disk
    retrieved = get_challenge_report(temp_repo, report.report_id)
    assert len(retrieved.issues) == 1
    assert retrieved.issues[0].title == "SQL Injection Vulnerability"


def test_add_challenge_question(temp_repo):
    """Test adding questions to a challenge report."""
    report = create_challenge_report(
        repo_root=temp_repo,
        target_name="Strategy",
        target_type="document",
        challenge_type="assumptions",
    )

    add_challenge_question(
        repo_root=temp_repo,
        report_id=report.report_id,
        question="What if market conditions change?",
    )

    retrieved = get_challenge_report(temp_repo, report.report_id)
    assert len(retrieved.questions) == 1
    assert "market conditions" in retrieved.questions[0]


def test_add_alternative(temp_repo):
    """Test adding alternative approaches."""
    report = create_challenge_report(
        repo_root=temp_repo,
        target_name="Implementation",
        target_type="code",
        challenge_type="design",
    )

    add_alternative(
        repo_root=temp_repo,
        report_id=report.report_id,
        alternative="Use async/await instead of callbacks",
    )

    retrieved = get_challenge_report(temp_repo, report.report_id)
    assert len(retrieved.alternatives_considered) == 1
    assert "async/await" in retrieved.alternatives_considered[0]


def test_get_all_reports(temp_repo):
    """Test retrieving all challenge reports."""
    create_challenge_report(temp_repo, "Target 1", "code", "assumptions")
    create_challenge_report(temp_repo, "Target 2", "design", "security")

    reports = get_all_reports(temp_repo)
    assert len(reports) == 2


def test_get_reports_by_severity(temp_repo):
    """Test filtering reports by severity."""
    report = create_challenge_report(temp_repo, "API", "code", "security")

    add_challenge_issue(
        temp_repo, report.report_id, "security", "critical",
        "Issue 1", "Desc", "Impact", "Fix"
    )
    add_challenge_issue(
        temp_repo, report.report_id, "security", "minor",
        "Issue 2", "Desc", "Impact", "Fix"
    )

    critical_reports = get_reports_by_severity(temp_repo, "critical")
    assert len(critical_reports) == 1

    minor_reports = get_reports_by_severity(temp_repo, "minor")
    assert len(minor_reports) == 1


def test_create_stress_test_scenario(temp_repo):
    """Test creating stress test scenarios."""
    scenario = create_stress_test_scenario(
        repo_root=temp_repo,
        name="Load Test 10x",
        description="Test with 10x normal load",
        load_factor=10.0,
        failure_injection="network_timeout",
        expected_behavior="Graceful degradation",
    )

    assert scenario.scenario_id == "stress-001"
    assert scenario.load_factor == 10.0
    assert scenario.failure_injection == "network_timeout"


def test_get_stress_test_scenarios(temp_repo):
    """Test retrieving stress test scenarios."""
    create_stress_test_scenario(temp_repo, "Test 1", "Desc 1", 1.0)
    create_stress_test_scenario(temp_repo, "Test 2", "Desc 2", 5.0)

    scenarios = get_stress_test_scenarios(temp_repo)
    assert len(scenarios) == 2


def test_quick_challenge(temp_repo):
    """Test the quick_challenge convenience function."""
    report = quick_challenge(
        repo_root=temp_repo,
        target_name="New Feature",
        target_type="code",
        assumptions=["No bugs exist", "Users love it"],
    )

    # Verify issues were created
    retrieved = get_challenge_report(temp_repo, report.report_id)
    assert len(retrieved.issues) == 2
    assert len(retrieved.questions) == 2

    # Verify first issue is major (first 3 assumptions)
    assert retrieved.issues[0].severity == ChallengeSeverity.MAJOR
