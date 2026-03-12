# agent-prd

Use this when the direction is good enough to specify and the output must work for humans and agents.

## Input

- approved problem or direction
- chosen scope
- constraints
- known dependencies

## Output

- human-readable summary
- agent-readable task spec
- dependencies
- constraints
- success metrics
- fallback or escalation rules
- review checklist

## Default Workflow

1. Clarify the problem with `problem-statement`
2. Write the execution spec with `agent-readable-prd-writer`
3. Fill standard PM sections with `prd-development`
4. Check gaps with `prd-coverage-checker`

## Operating Rules

- The PRD should help a human review and an agent act.
- Make dependencies and constraints explicit.
- Include success conditions and escalation rules.

## Recommended Skills

- `skills/problem-statement/SKILL.md`
- `skills/agent-readable-prd-writer/SKILL.md`
- `skills/prd-development/SKILL.md`
- `skills/prd-coverage-checker/SKILL.md`

## Next Command

- `define-metrics`
- `design-eval`
- `run-roadmap`
