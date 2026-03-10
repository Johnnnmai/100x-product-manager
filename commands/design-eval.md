# design-eval

Use this when you are shipping an AI feature, an internal agent, or any AI behavior that needs pass/fail logic.

## Input

- AI feature or behavior goal
- risk level
- expected user outcome
- known failure patterns

## Output

- eval objective
- pass/fail criteria
- strong cases
- red-flag cases
- scorecard
- human review trigger
- fallback trigger

## Default Workflow

1. Define behavior quality with `eval-design-for-ai-feature`
2. Define bad-output boundaries with `fallback-and-guardrail-designer`
3. Use `token-budget-optimizer` when context or memory shape affects behavior quality

## Operating Rules

- AI PM is not prompt writing alone.
- Define evals before launch when the risk is material.
- Specify fallback and human escalation conditions.

## Recommended Skills

- `skills/eval-design-for-ai-feature/SKILL.md`
- `skills/fallback-and-guardrail-designer/SKILL.md`
- `skills/token-budget-optimizer/SKILL.md`

## Next Command

- `agent-prd`
- `run-roadmap`
