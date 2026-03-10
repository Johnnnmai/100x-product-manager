# design-experiment

Use this when you have a hypothesis and need the smallest real test.

## Input

- hypothesis
- proposed intervention
- target segment
- constraints

## Output

- experiment design
- primary metric
- guardrails
- segmentation logic
- runtime guidance
- readout template

## Default Workflow

1. Define the measurable success condition
2. Design the experiment with `ab-test-designer`
3. Use `rapid-iteration-cycle` if the right move is a faster, smaller learning loop

## Operating Rules

- If execution cost is lower than more thinking, run the smallest viable test.
- Make guardrails explicit.
- Separate what the experiment can prove from what it cannot.

## Recommended Skills

- `skills/ab-test-designer/SKILL.md`
- `skills/rapid-iteration-cycle/SKILL.md`
- `skills/success-metric-spec-writer/SKILL.md`

## Next Command

- `define-metrics`
- `run-roadmap`
