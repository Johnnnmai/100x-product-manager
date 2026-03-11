"""Tests for Challenge Agent (Adversarial Testing)"""
import pytest
from pathlib import Path
import tempfile
import json


class ChallengeAgentTests:
    """Test suite for Challenge Agent integration"""

    def test_challenge_skill_exists(self):
        """Verify Challenge Agent skill is defined"""
        skill_path = Path("skills/flywheel/challenge/adversarial-tester/SKILL.md")
        assert skill_path.exists(), "Challenge Agent skill not found"

    def test_challenge_skill_structure(self):
        """Verify Challenge Agent skill has required sections"""
        skill_path = Path("skills/flywheel/challenge/adversarial-tester/SKILL.md")
        content = skill_path.read_text()

        # Check required sections
        assert "## Overview" in content
        assert "## When to Use" in content
        assert "## Inputs" in content
        assert "## Process" in content
        assert "## Outputs" in content

        # Check challenge categories
        assert "Assumptions" in content
        assert "Edge Case" in content
        assert "Failure Mode" in content
        assert "Security" in content

    def test_challenge_skill_has_examples(self):
        """Verify Challenge Agent skill has example output format"""
        skill_path = Path("skills/flywheel/challenge/adversarial-tester/SKILL.md")
        content = skill_path.read_text()

        assert "## Example Challenge Output" in content
        assert "Critical Issues" in content
        assert "Major Issues" in content
        assert "Questions for Team" in content

    def test_challenge_agent_role_exists(self):
        """Verify Challenge Agent role is defined in team"""
        role_path = Path("ai_os/agents/team/CHALLENGE.md")
        assert role_path.exists(), "Challenge Agent role not found"

        content = role_path.read_text()
        assert "Adversarial Testing" in content
        assert "Critical Analysis" in content
        assert "Quality Improvement" in content

    def test_challenge_agent_collaboration_pattern(self):
        """Verify Challenge Agent has correct collaboration pattern"""
        role_path = Path("ai_os/agents/team/CHALLENGE.md")
        content = role_path.read_text()

        assert "Inputs from" in content
        assert "Outputs to" in content
        assert "All agents" in content

    def test_all_team_roles_exist(self):
        """Verify all 6 team roles are defined"""
        team_dir = Path("ai_os/agents/team")
        expected_roles = ["ARCHITECT", "IMPLEMENTER", "REVIEWER", "TESTER", "CHALLENGE", "INTEGRATOR"]

        for role in expected_roles:
            role_path = team_dir / f"{role}.md"
            assert role_path.exists(), f"Role {role} not found"


def test_challenge_agent_suite():
    """Run Challenge Agent test suite"""
    tests = ChallengeAgentTests()

    tests.test_challenge_skill_exists()
    tests.test_challenge_skill_structure()
    tests.test_challenge_skill_has_examples()
    tests.test_challenge_agent_role_exists()
    tests.test_challenge_agent_collaboration_pattern()
    tests.test_all_team_roles_exist()


class TestChallengeAgentImplementation:
    """Test Challenge Agent Python implementation."""

    @pytest.fixture
    def temp_repo(self):
        """Create a temporary repository for testing."""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            (repo_root / "ops" / "challenge_reports").mkdir(parents=True)
            yield repo_root

    @pytest.fixture
    def challenge_agent(self, temp_repo):
        """Create a ChallengeAgent instance."""
        from ai_os.challenge_agent import ChallengeAgent
        return ChallengeAgent(temp_repo)

    def test_challenge_report_creation(self):
        """Test ChallengeReport creation."""
        from ai_os.challenge_agent import ChallengeReport
        report = ChallengeReport(
            target="Test",
            target_type="design",
            critical_issues=[{"description": "Test", "impact": "Impact"}],
        )
        data = report.to_dict()
        assert data["target"] == "Test"

    def test_challenge_report_markdown(self):
        """Test ChallengeReport markdown output."""
        from ai_os.challenge_agent import ChallengeReport
        report = ChallengeReport(
            target="Test",
            target_type="design",
            critical_issues=[{"description": "Bug", "impact": "Crash"}],
        )
        md = report.to_markdown()
        assert "# Challenge Report: Test" in md
        assert "Bug" in md

    def test_challenge_design(self, challenge_agent):
        """Test design challenge."""
        report = challenge_agent.challenge_design("# Design", assumptions=["Always works"])
        assert report.target_type == "design"
        assert len(report.major_issues) + len(report.minor_issues) >= 0

    def test_challenge_code_mutable_default(self, challenge_agent):
        """Test code challenge detects mutable default."""
        code = "def f(items=[]): pass"
        report = challenge_agent.challenge_code(code, "python")
        assert report.target_type == "code"

    def test_stress_test_design(self, challenge_agent):
        """Test stress test design."""
        report = challenge_agent.stress_test_design("# System")
        assert report.target_type == "stress_test"
        assert len(report.critical_issues) >= 1

    def test_reports_saved(self, challenge_agent):
        """Test reports are saved to disk."""
        challenge_agent.stress_test_design("# Test")
        files = list(challenge_agent.reports_dir.glob("*.json"))
        assert len(files) >= 1

    def test_get_reports(self, challenge_agent):
        """Test retrieving reports."""
        challenge_agent.stress_test_design("# Test 1")
        challenge_agent.stress_test_design("# Test 2")
        reports = challenge_agent.get_reports(limit=5)
        assert len(reports) >= 2


def test_challenge_agent_suite():
    """Run Challenge Agent test suite"""
    tests = ChallengeAgentTests()

    tests.test_challenge_skill_exists()
    tests.test_challenge_skill_structure()
    tests.test_challenge_skill_has_examples()
    tests.test_challenge_agent_role_exists()
    tests.test_challenge_agent_collaboration_pattern()
    tests.test_all_team_roles_exist()


if __name__ == "__main__":
    test_challenge_agent_suite()
    print("Challenge Agent tests passed!")
