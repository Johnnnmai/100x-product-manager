"""
100x PM Evals Framework

This module provides evaluation criteria for assessing 100x PM command outputs.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any


class EvalCategory(Enum):
    """Categories of evaluation criteria."""
    COMPLETENESS = "completeness"
    ACCURACY = "accuracy"
    ACTIONABILITY = "actionability"
    FORMAT = "format"


@dataclass
class EvalCriteria:
    """Evaluation criteria for a command."""
    category: EvalCategory
    description: str
    weight: float = 1.0


@dataclass
class EvalResult:
    """Result of an evaluation."""
    command: str
    category: EvalCategory
    score: float  # 0-1
    feedback: str
    passed: bool


# Command evaluation criteria
COMMAND_EVALS = {
    "find-winning-direction": [
        EvalCriteria(EvalCategory.COMPLETENESS, "Includes market signals analysis", 1.0),
        EvalCriteria(EvalCategory.ACCURACY, "Identifies valid target user", 1.0),
        EvalCriteria(EvalCategory.ACTIONABILITY, "Provides concrete next steps", 1.0),
        EvalCriteria(EvalCategory.FORMAT, "Follows decision-pack format", 0.5),
    ],
    "agent-prd": [
        EvalCriteria(EvalCategory.COMPLETENESS, "Includes all PRD sections", 1.0),
        EvalCriteria(EvalCategory.ACCURACY, "Features align with user needs", 1.0),
        EvalCriteria(EvalCategory.ACTIONABILITY, "Acceptance criteria are testable", 1.0),
        EvalCriteria(EvalCategory.FORMAT, "Follows PRD template", 0.5),
    ],
    "write-prd": [
        EvalCriteria(EvalCategory.COMPLETENESS, "Problem statement clear", 1.0),
        EvalCriteria(EvalCategory.ACCURACY, "Solution is feasible", 1.0),
        EvalCriteria(EvalCategory.ACTIONABILITY, "Has success metrics", 1.0),
        EvalCriteria(EvalCategory.FORMAT, "Professional PRD format", 0.5),
    ],
    "validate-product-direction": [
        EvalCriteria(EvalCategory.COMPLETENESS, "Covers all validation dimensions", 1.0),
        EvalCriteria(EvalCategory.ACCURACY, "Evidence supports conclusions", 1.0),
        EvalCriteria(EvalCategory.ACTIONABILITY, "Provides risk mitigation", 1.0),
        EvalCriteria(EvalCategory.FORMAT, "Structured validation report", 0.5),
    ],
}


def evaluate_command_output(command: str, output: str) -> list[EvalResult]:
    """
    Evaluate the output of a command.

    Args:
        command: Command name
        output: Command output

    Returns:
        List of evaluation results
    """
    results = []

    criteria = COMMAND_EVALS.get(command, [])
    for crit in criteria:
        # Simple heuristic evaluation
        score = 0.5  # Default score
        feedback = "Automated evaluation"

        # Check for keywords based on category
        if crit.category == EvalCategory.COMPLETENESS:
            if len(output) > 200:
                score = 0.8
            if len(output) > 500:
                score = 1.0

        elif crit.category == EvalCategory.ACTIONABILITY:
            action_words = ["should", "must", "next step", "implement", "create"]
            if any(word in output.lower() for word in action_words):
                score = 0.8

        elif crit.category == EvalCategory.FORMAT:
            if "#" in output or "##" in output:  # Has markdown headers
                score = 0.9

        results.append(EvalResult(
            command=command,
            category=crit.category,
            score=score,
            feedback=feedback,
            passed=score >= 0.5,
        ))

    return results


def calculate_pass_rate(results: list[EvalResult]) -> float:
    """Calculate the pass rate from evaluation results."""
    if not results:
        return 0.0
    passed = sum(1 for r in results if r.passed)
    return passed / len(results)


if __name__ == "__main__":
    # Test evaluation
    test_output = """
    # Product Direction

    ## Problem Statement
    Busy professionals need meal planning

    ## Target User
    Working parents with limited time

    ## Next Steps
    1. Conduct user interviews
    2. Build MVP
    3. Test with beta users
    """

    results = evaluate_command_output("find-winning-direction", test_output)
    for r in results:
        print(f"{r.category.value}: {r.score:.1f} - {'PASS' if r.passed else 'FAIL'}")

    pass_rate = calculate_pass_rate(results)
    print(f"\nPass rate: {pass_rate:.0%}")
