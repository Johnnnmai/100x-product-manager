# define-metrics

Use this when a feature, workflow, or product direction needs a success definition before execution.

## Input

- feature or workflow goal
- target user or system behavior
- measurement constraints

## Output

- primary success metric
- supporting metrics
- counter metrics
- success threshold
- failure threshold
- measurement window

## Default Workflow

1. Define the main success condition with `success-metric-spec-writer`
2. Add supporting and guardrail logic
3. If needed, connect metrics to later experimentation through `ab-test-designer`

## Operating Rules

- Define success before shipping.
- Use a time window, not just a metric label.
- Add counter metrics when optimization can create damage.

## Recommended Skills

- `skills/success-metric-spec-writer/SKILL.md`
- `skills/ab-test-designer/SKILL.md`

## Next Command

- `design-experiment`
- `run-roadmap`
