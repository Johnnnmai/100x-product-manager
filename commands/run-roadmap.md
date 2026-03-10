# run-roadmap

Use this when a chosen direction needs milestones, ownership, and tracking across humans and agents.

## Input

- product direction
- objectives
- resources or constraints
- timeline assumptions

## Output

- roadmap themes
- milestones
- workstream split
- agent vs human assignment
- dependency chain
- check-in cadence
- tracking format

## Default Workflow

1. Create the milestone structure with `roadmap-orchestrator`
2. Split work by execution mode with `task-delegation-planner`
3. Define ongoing operating rules with `task-tracking-operator`
4. Use `roadmap-planning` when a traditional roadmap artifact is also needed

## Operating Rules

- Separate human judgment work from agent-executable work.
- Make dependencies visible.
- Define how work is tracked before work starts drifting.

## Recommended Skills

- `skills/roadmap-orchestrator/SKILL.md`
- `skills/task-delegation-planner/SKILL.md`
- `skills/task-tracking-operator/SKILL.md`
- `skills/roadmap-planning/SKILL.md`

## Next Command

- `make-content`
- `pm-command-center`
