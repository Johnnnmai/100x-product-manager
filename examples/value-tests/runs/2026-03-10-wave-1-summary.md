# 2026-03-10 Pilot Benchmark Wave 1

## Scope

- Date: March 10, 2026
- Operator: Codex internal pilot
- Model family: GPT-5 Codex
- Review type: single-operator, non-blinded
- Tasks: `shape-idea`, `agent-prd`, `prioritize`, `design-eval`

This is a public pilot, not the final benchmark. It is useful because the raw prompts, outputs, scores, and summaries are all in-repo.

## Results

| Task | Baseline avg | 100X PM avg | Delta | Time to acceptable draft | Manual edits after first draft |
| --- | --- | --- | --- | --- | --- |
| `shape-idea` | 2.3/5 | 4.1/5 | +1.8 | 18 min -> 10 min | 5 -> 2 |
| `agent-prd` | 2.9/5 | 4.4/5 | +1.5 | 25 min -> 14 min | 7 -> 3 |
| `prioritize` | 3.0/5 | 4.3/5 | +1.3 | 16 min -> 9 min | 4 -> 2 |
| `design-eval` | 2.1/5 | 4.4/5 | +2.3 | 20 min -> 11 min | 6 -> 2 |

## What This Pilot Says

- The largest gains came from forcing explicit structure, not from adding more words.
- `shape-idea` improved because the command forced multiple wedges before picking one.
- `agent-prd` improved because the command required dual-mode output for both humans and agents.
- `prioritize` improved because the command forced explicit losers, trade-offs, and review checkpoints.
- `design-eval` improved the most because the baseline drifted into generic testing advice, while the command forced pass/fail logic and fallback.

## Limitations

- same operator created and scored the outputs
- no blinded review yet
- one run per task so far
- same-model pilot, not external user data

## Raw Artifacts

- [shape-idea baseline](2026-03-10-shape-idea-baseline.md)
- [shape-idea 100xpm](2026-03-10-shape-idea-100xpm.md)
- [shape-idea scorecard](2026-03-10-shape-idea-scorecard.md)
- [shape-idea summary](2026-03-10-shape-idea-summary.md)
- [agent-prd baseline](2026-03-10-agent-prd-baseline.md)
- [agent-prd 100xpm](2026-03-10-agent-prd-100xpm.md)
- [agent-prd scorecard](2026-03-10-agent-prd-scorecard.md)
- [agent-prd summary](2026-03-10-agent-prd-summary.md)
- [prioritize baseline](2026-03-10-prioritize-baseline.md)
- [prioritize 100xpm](2026-03-10-prioritize-100xpm.md)
- [prioritize scorecard](2026-03-10-prioritize-scorecard.md)
- [prioritize summary](2026-03-10-prioritize-summary.md)
- [design-eval baseline](2026-03-10-design-eval-baseline.md)
- [design-eval 100xpm](2026-03-10-design-eval-100xpm.md)
- [design-eval scorecard](2026-03-10-design-eval-scorecard.md)
- [design-eval summary](2026-03-10-design-eval-summary.md)
