# Find Winning Direction Audit Baseline Run

## Run Metadata

- Task: front-door product audit
- Command: plain prompt baseline
- Date: 2026-03-11
- Operator: Codex internal pilot
- Model: GPT-5 Codex
- Temperature: default
- Arm: `baseline`

## Input Bundle

- Source files: `examples/value-tests/input-bundles/2026-03-11-product-audit-input.md`
- Problem statement: audit an existing AI customer-success product and recommend improvements
- Constraints: 2 engineers, 1 designer, 8 weeks, no CRM writeback
- Success criteria: find the strongest strategic move and next step

## Prompt Used

```text
Review this product snapshot and suggest what the team should improve next.

Please identify product weaknesses, opportunities, and recommendations.

Use the provided website and signal bundle as context.
```

## Output Artifact

```md
# Product Audit: PulsePilot

The product seems promising but needs clearer positioning.

## Observed issues

- churn scores are not trusted
- alerts may create noise
- setup may be too heavy

## Recommendations

1. Improve the model so the scores are more accurate.
2. Reduce false alerts.
3. Add better CRM integration.
4. Simplify onboarding.

## Opportunity

The team could become a strong AI assistant for customer success.

## Next steps

- interview users
- improve the score
- refine the dashboard
```

## Workflow Metrics

- Total turns: 1
- Clarification turns: 0
- Time to first draft: 14 min
- Time to acceptable draft: 22 min
- Manual edits after first draft: 6

## Notes

- What improved: basic issues were identified
- What failed: no wedge, weak business model logic, no channel or execution path
- Should this run count toward the public benchmark: `yes`
