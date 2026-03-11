#!/usr/bin/env python3
"""Recompute benchmark metrics from markdown scorecards."""

from __future__ import annotations

import argparse
import glob
import re
import sys
from dataclasses import dataclass
from pathlib import Path


QUALITY_ROW_RE = re.compile(
    r"^\| (?P<category>[^|]+?) \| (?P<baseline>\d+(?:\.\d+)?) \| "
    r"(?P<pm>\d+(?:\.\d+)?) \| (?P<delta>[+-]?\d+(?:\.\d+)?) \|"
)
TIME_ROW_RE = re.compile(
    r"^\| Time to acceptable draft \| (?P<baseline>\d+) min \| (?P<pm>\d+) min \|$"
)
EDIT_ROW_RE = re.compile(
    r"^\| Manual edits after first draft \| (?P<baseline>\d+) \| (?P<pm>\d+) \|$"
)
UNSUPPORTED_ROW_RE = re.compile(
    r"^\| Unsupported claims present \| (?P<baseline>Yes|No) \| (?P<pm>Yes|No) \|"
)


@dataclass
class Scorecard:
    path: Path
    baseline_average: float
    pm_average: float
    baseline_minutes: int
    pm_minutes: int
    baseline_edits: int
    pm_edits: int
    baseline_unsupported: bool
    pm_unsupported: bool

    @property
    def average_delta(self) -> float:
        return round(self.pm_average - self.baseline_average, 2)

    @property
    def time_reduction_pct(self) -> float:
        return round((1 - (self.pm_minutes / self.baseline_minutes)) * 100, 1)

    @property
    def edit_reduction_pct(self) -> float:
        return round((1 - (self.pm_edits / self.baseline_edits)) * 100, 1)


def parse_scorecard(path: Path) -> Scorecard:
    quality_rows: list[tuple[float, float]] = []
    baseline_minutes = pm_minutes = None
    baseline_edits = pm_edits = None
    baseline_unsupported = pm_unsupported = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()

        quality_match = QUALITY_ROW_RE.match(line)
        if quality_match:
            quality_rows.append(
                (
                    float(quality_match.group("baseline")),
                    float(quality_match.group("pm")),
                )
            )
            continue

        time_match = TIME_ROW_RE.match(line)
        if time_match:
            baseline_minutes = int(time_match.group("baseline"))
            pm_minutes = int(time_match.group("pm"))
            continue

        edit_match = EDIT_ROW_RE.match(line)
        if edit_match:
            baseline_edits = int(edit_match.group("baseline"))
            pm_edits = int(edit_match.group("pm"))
            continue

        unsupported_match = UNSUPPORTED_ROW_RE.match(line)
        if unsupported_match:
            baseline_unsupported = unsupported_match.group("baseline") == "Yes"
            pm_unsupported = unsupported_match.group("pm") == "Yes"

    if not quality_rows:
        raise ValueError(f"{path} has no quality rows")
    if None in {
        baseline_minutes,
        pm_minutes,
        baseline_edits,
        pm_edits,
        baseline_unsupported,
        pm_unsupported,
    }:
        raise ValueError(f"{path} is missing workflow or penalty metadata")

    baseline_average = round(sum(row[0] for row in quality_rows) / len(quality_rows), 1)
    pm_average = round(sum(row[1] for row in quality_rows) / len(quality_rows), 1)

    return Scorecard(
        path=path,
        baseline_average=baseline_average,
        pm_average=pm_average,
        baseline_minutes=baseline_minutes,
        pm_minutes=pm_minutes,
        baseline_edits=baseline_edits,
        pm_edits=pm_edits,
        baseline_unsupported=baseline_unsupported,
        pm_unsupported=pm_unsupported,
    )


def expand_patterns(patterns: list[str]) -> list[Path]:
    paths: list[Path] = []
    for pattern in patterns:
        matches = sorted(Path(match) for match in glob.glob(pattern))
        if not matches:
            raise FileNotFoundError(f"No files matched: {pattern}")
        paths.extend(matches)
    unique_paths = sorted({path.resolve() for path in paths})
    return unique_paths


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Recompute value-test wave metrics from markdown scorecards."
    )
    parser.add_argument(
        "patterns",
        nargs="+",
        help="One or more glob patterns that match markdown scorecards.",
    )
    args = parser.parse_args()

    scorecards = [parse_scorecard(path) for path in expand_patterns(args.patterns)]

    for scorecard in scorecards:
        print(
            f"{scorecard.path.name}: "
            f"delta={scorecard.average_delta:+.2f}, "
            f"time_reduction={scorecard.time_reduction_pct:.1f}%, "
            f"edit_reduction={scorecard.edit_reduction_pct:.1f}%"
        )

    average_delta = round(
        sum(scorecard.average_delta for scorecard in scorecards) / len(scorecards), 2
    )
    total_baseline_minutes = sum(scorecard.baseline_minutes for scorecard in scorecards)
    total_pm_minutes = sum(scorecard.pm_minutes for scorecard in scorecards)
    total_baseline_edits = sum(scorecard.baseline_edits for scorecard in scorecards)
    total_pm_edits = sum(scorecard.pm_edits for scorecard in scorecards)
    time_reduction_pct = round(
        (1 - (total_pm_minutes / total_baseline_minutes)) * 100, 1
    )
    edit_reduction_pct = round(
        (1 - (total_pm_edits / total_baseline_edits)) * 100, 1
    )
    unsupported_claims_increase = any(
        (not scorecard.baseline_unsupported) and scorecard.pm_unsupported
        for scorecard in scorecards
    )

    quality_pass = average_delta >= 0.8
    efficiency_pass = time_reduction_pct >= 25 or edit_reduction_pct >= 30
    unsupported_pass = not unsupported_claims_increase
    overall_pass = quality_pass and efficiency_pass and unsupported_pass

    print("")
    print(f"average_score_delta={average_delta:+.2f}")
    print(f"time_reduction_pct={time_reduction_pct:.1f}%")
    print(f"edit_reduction_pct={edit_reduction_pct:.1f}%")
    print(f"unsupported_claims_increase={'yes' if unsupported_claims_increase else 'no'}")
    print(f"quality_gate={'pass' if quality_pass else 'fail'}")
    print(f"efficiency_gate={'pass' if efficiency_pass else 'fail'}")
    print(f"unsupported_claims_gate={'pass' if unsupported_pass else 'fail'}")
    print(f"overall={'pass' if overall_pass else 'fail'}")

    return 0 if overall_pass else 1


if __name__ == "__main__":
    sys.exit(main())
