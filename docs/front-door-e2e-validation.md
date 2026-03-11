# Front-Door E2E Validation Plan

This document defines how to prove that the new front door is effective and improves workflow efficiency.

## Goal

Validate the new 100X PM front door across the three core entry modes:

1. `product audit`
2. `new idea`
3. `long-range vision`

The goal is not prettier writing.
The goal is to prove the workflow is:

- more decision-useful
- more execution-ready
- faster to reach an acceptable artifact

## Claims Under Test

### Claim 1: Product audit is a real hero workflow

Given the same product input bundle, `find-winning-direction` in audit mode should produce:

- a sharper pain-point map
- stronger hypotheses
- clearer business model and channel implications
- a better execution path

than a plain prompt.

### Claim 2: The front door handles rough ideas better than generic prompting

Given the same idea input bundle, `find-winning-direction` should produce:

- tighter wedge definition
- stronger strategic narrative
- clearer next validation step

than a plain prompt.

### Claim 3: The front door handles messy strategy better than generic prompting

Given the same messy-context input bundle, `find-winning-direction` should produce:

- clearer 12-month vs 3-5 year separation
- sharper phased roadmap
- fewer unresolved ambiguities

than a plain prompt.

### Claim 4: The front door improves efficiency

Across all three modes, the command-guided workflow should reduce:

- time to acceptable draft
- manual restructuring after first draft
- clarification burden

relative to baseline prompting.

## Test Matrix

| Mode | Command | Input bundle | Evidence package |
| --- | --- | --- | --- |
| Product audit | `find-winning-direction` | `examples/value-tests/input-bundles/2026-03-11-product-audit-input.md` | baseline, 100xpm, scorecard, summary |
| New idea | `find-winning-direction` | `examples/value-tests/input-bundles/2026-03-11-new-idea-input.md` | baseline, 100xpm, scorecard, summary |
| Long-range vision | `find-winning-direction` | `examples/value-tests/input-bundles/2026-03-11-long-range-vision-input.md` | baseline, 100xpm, scorecard, summary |

## Success Criteria

- average quality improvement of at least `+0.8` on a 5-point scale
- at least `25%` reduction in time to acceptable draft, or
- at least `30%` reduction in manual edits after first draft
- no increase in unsupported claims

## Review Standard

Wave 2 remains an internal, single-operator pilot.

That makes it useful for shaping the product and homepage proof, but not enough for strong external claims without blinded follow-up.

## Executed Wave

- [Wave 2 front-door summary](../examples/value-tests/runs/2026-03-11-wave-2-front-door-summary.md)

Mode-level artifacts:

- [Audit summary](../examples/value-tests/runs/2026-03-11-find-winning-direction-audit-summary.md)
- [Idea summary](../examples/value-tests/runs/2026-03-11-find-winning-direction-idea-summary.md)
- [Vision summary](../examples/value-tests/runs/2026-03-11-find-winning-direction-vision-summary.md)

## How To Re-Run

1. Keep the input bundles fixed.
2. Use the same model across both arms.
3. Save exact prompts and raw outputs.
4. Score baseline and command-guided arms against the same rubric.
5. Record time, edits, and usability honestly.

Verification command:

```bash
python scripts/verify-value-test-wave.py "examples/value-tests/runs/2026-03-11-find-winning-direction-*-scorecard.md"
```
