# 2026-03-11 Front-Door E2E Pilot (Wave 2)

## Scope

- Date: March 11, 2026
- Operator: Codex internal pilot
- Model family: GPT-5 Codex
- Review type: single-operator, non-blinded
- Workflow under test: `find-winning-direction` as the front door for all three modes

## Why This Wave Exists

Wave 1 proved several core commands.

Wave 2 exists to validate the new top-level product story:

- one engine
- three entry modes
- OASIS-backed strategy lab positioning
- stronger path from ambiguity to execution

## Results

| Mode | Baseline avg | 100X PM avg | Delta | Time to acceptable draft | Manual edits after first draft |
| --- | --- | --- | --- | --- | --- |
| Product audit | 2.1/5 | 4.3/5 | +2.2 | 22 min -> 12 min | 6 -> 2 |
| New idea | 1.7/5 | 3.9/5 | +2.2 | 19 min -> 11 min | 5 -> 2 |
| Long-range vision | 1.6/5 | 3.6/5 | +2.0 | 24 min -> 14 min | 7 -> 3 |

## Aggregate Verification

- Average quality delta: `+2.13`
- Time to acceptable draft reduction: `43.1%`
- Manual edit reduction: `61.1%`
- Unsupported claims increase: `no`
- Success criteria status: `pass`

Recompute from scorecards:

```bash
python scripts/verify-value-test-wave.py "examples/value-tests/runs/2026-03-11-find-winning-direction-*-scorecard.md"
```

## What This Wave Says

- The front-door story is strongest when it forces a wedge or strategy choice, not when it just summarizes.
- Product audit is the best hero path because the command converts visible product evidence into a clear bet quickly.
- New idea mode wins when it narrows to a demoable wedge instead of drifting into a broad platform.
- Vision mode wins when it separates near-term execution from long-term aspiration.

## Why This Matters For Positioning

The evidence supports three real claims:

1. 100X PM improves strategic clarity.
2. 100X PM improves execution readiness.
3. 100X PM reduces time to an acceptable artifact.

That means the repo can credibly sell:

- faster convergence
- pre-build strategy validation
- strategy compiled into execution

## Limitations

- single operator
- non-blinded scoring
- synthetic but realistic input bundles
- no live scrape or live OASIS run inside the benchmark loop

## Raw Artifacts

### Product audit mode

- [baseline](2026-03-11-find-winning-direction-audit-baseline.md)
- [100xpm](2026-03-11-find-winning-direction-audit-100xpm.md)
- [scorecard](2026-03-11-find-winning-direction-audit-scorecard.md)
- [summary](2026-03-11-find-winning-direction-audit-summary.md)

### New idea mode

- [baseline](2026-03-11-find-winning-direction-idea-baseline.md)
- [100xpm](2026-03-11-find-winning-direction-idea-100xpm.md)
- [scorecard](2026-03-11-find-winning-direction-idea-scorecard.md)
- [summary](2026-03-11-find-winning-direction-idea-summary.md)

### Long-range vision mode

- [baseline](2026-03-11-find-winning-direction-vision-baseline.md)
- [100xpm](2026-03-11-find-winning-direction-vision-100xpm.md)
- [scorecard](2026-03-11-find-winning-direction-vision-scorecard.md)
- [summary](2026-03-11-find-winning-direction-vision-summary.md)
