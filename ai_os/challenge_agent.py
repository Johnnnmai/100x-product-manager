# Challenge Agent - Adversarial Testing Implementation

"""
Challenge Agent provides adversarial testing capabilities by:
- Questioning assumptions
- Stress-testing designs
- Finding edge cases and failure modes
- Performing security probes
"""

from pathlib import Path
from typing import Any
from datetime import datetime
import json


class ChallengeReport:
    """Report from Challenge Agent adversarial testing."""

    def __init__(
        self,
        target: str,
        target_type: str,
        critical_issues: list[dict[str, str]] | None = None,
        major_issues: list[dict[str, str]] | None = None,
        minor_issues: list[dict[str, str]] | None = None,
        questions: list[str] | None = None,
        recommendations: list[str] | None = None,
    ):
        self.target = target
        self.target_type = target_type
        self.critical_issues = critical_issues or []
        self.major_issues = major_issues or []
        self.minor_issues = minor_issues or []
        self.questions = questions or []
        self.recommendations = recommendations or []
        self.timestamp = datetime.now().isoformat()

    def to_dict(self) -> dict[str, Any]:
        return {
            "target": self.target,
            "target_type": self.target_type,
            "critical_issues": self.critical_issues,
            "major_issues": self.major_issues,
            "minor_issues": self.minor_issues,
            "questions": self.questions,
            "recommendations": self.recommendations,
            "timestamp": self.timestamp,
        }

    def to_markdown(self) -> str:
        """Convert challenge report to markdown format."""
        lines = [
            f"# Challenge Report: {self.target}",
            f"**Type:** {self.target_type}",
            f"**Date:** {self.timestamp}",
            "",
        ]

        if self.critical_issues:
            lines.append("## Critical Issues")
            for i, issue in enumerate(self.critical_issues, 1):
                lines.append(f"{i}. {issue.get('description', 'N/A')}")
                lines.append(f"   - Impact: {issue.get('impact', 'N/A')}")
                lines.append(f"   - Recommendation: {issue.get('recommendation', 'N/A')}")
            lines.append("")

        if self.major_issues:
            lines.append("## Major Issues")
            for i, issue in enumerate(self.major_issues, 1):
                lines.append(f"{i}. {issue.get('description', 'N/A')}")
                lines.append(f"   - Impact: {issue.get('impact', 'N/A')}")
                lines.append(f"   - Recommendation: {issue.get('recommendation', 'N/A')}")
            lines.append("")

        if self.minor_issues:
            lines.append("## Minor Issues")
            for i, issue in enumerate(self.minor_issues, 1):
                lines.append(f"{i}. {issue.get('description', 'N/A')}")
                lines.append(f"   - Impact: {issue.get('impact', 'N/A')}")
            lines.append("")

        if self.questions:
            lines.append("## Questions for Team")
            for q in self.questions:
                lines.append(f"- {q}")
            lines.append("")

        if self.recommendations:
            lines.append("## Recommendations")
            for r in self.recommendations:
                lines.append(f"- {r}")
            lines.append("")

        return "\n".join(lines)


class ChallengeAgent:
    """
    Challenge Agent performs adversarial testing by:
    - Questioning assumptions
    - Finding edge cases and failure modes
    - Stress-testing implementations
    - Probing for security vulnerabilities
    """

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.reports_dir = repo_root / "ops" / "challenge_reports"
        self.reports_dir.mkdir(parents=True, exist_ok=True)
        self._report_counter = 0

    def challenge_design(
        self,
        design_doc: str,
        assumptions: list[str] | None = None,
    ) -> ChallengeReport:
        """
        Challenge a design document by questioning assumptions.

        Args:
            design_doc: Content of the design document
            assumptions: List of stated assumptions to challenge

        Returns:
            ChallengeReport with identified issues
        """
        issues = []

        # Challenge common design assumptions
        if assumptions:
            for assumption in assumptions:
                # Check for unspoken constraints
                if "always" in assumption.lower() or "never" in assumption.lower():
                    issues.append({
                        "description": f"Absolute claim: '{assumption}'",
                        "impact": "May not hold in all scenarios",
                        "recommendation": "Add boundary conditions or exceptions",
                    })

        # Default challenges for any design
        default_challenges = [
            {
                "description": "No explicit error handling strategy",
                "impact": "Unknown failure modes",
                "recommendation": "Define error handling approach",
            },
            {
                "description": "Scalability not addressed",
                "impact": "May fail under load",
                "recommendation": "Add scalability requirements",
            },
            {
                "description": "Security considerations not explicit",
                "impact": "Potential vulnerabilities",
                "recommendation": "Add security review",
            },
        ]

        report = ChallengeReport(
            target="Design Review",
            target_type="design",
            major_issues=issues + default_challenges[:1] if issues else default_challenges[:1],
            minor_issues=default_challenges[1:] if not issues else [],
            questions=[
                "What happens when this design encounters unexpected input?",
                "What are the failure modes?",
                "How does this scale with 10x or 100x load?",
            ],
        )

        self._save_report(report)
        return report

    def challenge_code(
        self,
        code: str,
        language: str = "python",
    ) -> ChallengeReport:
        """
        Challenge code by finding edge cases and potential issues.

        Args:
            code: Source code to challenge
            language: Programming language

        Returns:
            ChallengeReport with identified issues
        """
        critical = []
        major = []
        minor = []

        # Check for common issues based on language
        if language == "python":
            # Check for bare except
            if "except:" in code:
                critical.append({
                    "description": "Bare except clause catches all exceptions",
                    "impact": "Hides bugs, may catch SystemExit",
                    "recommendation": "Use specific exception types",
                })

            # Check for mutable default args
            if "def " in code and "=[]" in code:
                major.append({
                    "description": "Mutable default argument detected",
                    "impact": "Shared state across calls",
                    "recommendation": "Use None and assign inside function",
                })

            # Check for hardcoded credentials
            if "password" in code.lower() or "api_key" in code.lower():
                if '"' in code or "'" in code:
                    critical.append({
                        "description": "Potential hardcoded credential",
                        "impact": "Security vulnerability",
                        "recommendation": "Use environment variables",
                    })

        # General checks
        lines = code.split("\n")
        if len(lines) > 500:
            major.append({
                "description": "Large function/module (>500 lines)",
                "impact": "Hard to maintain and test",
                "recommendation": "Break into smaller units",
            })

        # Check for missing error handling
        if "raise " in code and "try:" not in code:
            major.append({
                "description": "Exception raised without try-except",
                "impact": "Unhandled exceptions may crash",
                "recommendation": "Add error handling",
            })

        report = ChallengeReport(
            target="Code Review",
            target_type="code",
            critical_issues=critical,
            major_issues=major,
            minor_issues=minor,
            questions=[
                "What edge cases are not handled?",
                "What happens with invalid input?",
                "Are there race conditions?",
            ],
            recommendations=[
                "Add comprehensive error handling",
                "Write unit tests for edge cases",
                "Review for security vulnerabilities",
            ],
        )

        self._save_report(report)
        return report

    def stress_test_design(
        self,
        design_doc: str,
        load_scenarios: list[str] | None = None,
    ) -> ChallengeReport:
        """
        Design stress test scenarios for a system.

        Args:
            design_doc: System design document
            load_scenarios: Specific load scenarios to test

        Returns:
            ChallengeReport with stress test scenarios
        """
        default_scenarios = load_scenarios or [
            "10x normal load",
            "100x normal load",
            "Sudden traffic spike",
            "Prolonged high load",
            "Resource exhaustion (memory, CPU, disk)",
            "Network partition",
            "Database connection pool exhaustion",
            "Concurrent user operations",
        ]

        stress_tests = []
        for scenario in default_scenarios:
            stress_tests.append({
                "description": f"Test {scenario}",
                "expected_behavior": "Define expected behavior under this load",
                "success_criteria": "Define success criteria",
            })

        report = ChallengeReport(
            target="Stress Test Design",
            target_type="stress_test",
            critical_issues=[{
                "description": "No load testing strategy",
                "impact": "Unknown performance characteristics",
                "recommendation": "Add load testing to CI/CD",
            }],
            major_issues=stress_tests[:3],
            minor_issues=stress_tests[3:],
            questions=[
                "What's the breaking point?",
                "How does the system degrade?",
                "What's the recovery time?",
            ],
            recommendations=[
                "Implement continuous load testing",
                "Add performance monitoring",
                "Define SLAs",
            ],
        )

        self._save_report(report)
        return report

    def _save_report(self, report: ChallengeReport) -> Path:
        """Save challenge report to disk."""
        self._report_counter += 1
        filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}-{self._report_counter:03d}-{report.target_type}.json"
        filepath = self.reports_dir / filename
        with open(filepath, "w") as f:
            json.dump(report.to_dict(), f, indent=2)
        return filepath

    def get_reports(self, limit: int = 10) -> list[ChallengeReport]:
        """Get recent challenge reports."""
        reports = []
        for f in sorted(self.reports_dir.glob("*.json"), reverse=True)[:limit]:
            with open(f) as fp:
                data = json.load(fp)
                report = ChallengeReport(
                    target=data["target"],
                    target_type=data["target_type"],
                    critical_issues=data.get("critical_issues", []),
                    major_issues=data.get("major_issues", []),
                    minor_issues=data.get("minor_issues", []),
                    questions=data.get("questions", []),
                    recommendations=data.get("recommendations", []),
                )
                reports.append(report)
        return reports


def get_challenge_agent(repo_root: Path | str | None = None) -> ChallengeAgent:
    """Get a ChallengeAgent instance."""
    if repo_root is None:
        repo_root = Path(".")
    elif isinstance(repo_root, str):
        repo_root = Path(repo_root)
    return ChallengeAgent(repo_root)
