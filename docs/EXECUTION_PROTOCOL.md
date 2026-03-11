# RoomJoy Execution Protocol

## Objective
Minimize manual review while preserving product control.

## Roles

### Human Owner
Responsible for:
- approving scope
- approving next task
- deciding when the product is sellable enough
- refusing scope creep

### Claude Code
Responsible for:
- audit mode
- implementation planning
- code execution for approved task
- updating task board
- producing delivery summary

### OpenClaw
Responsible for:
- pull latest repo
- build
- typecheck
- smoke test
- screenshot key pages
- deploy preview
- write validation report

## Modes

### Mode 1: Audit Mode
Goal:
Understand current repo state and recommend exactly one next task.

Allowed:
- read code
- score current state
- identify blockers
- propose one next task

Not allowed:
- modify unrelated files
- redesign pages
- add new features

Output:
- ROOMJOY_SELLABILITY_AUDIT.md or equivalent one-page summary

### Mode 2: Execution Mode
Goal:
Implement exactly one approved task.

Allowed:
- code changes needed for approved task
- minimal supporting refactor
- tests/checks needed for approved task
- docs update related to approved task

Not allowed:
- extra features
- design rewrites
- adjacent scope creep

Output:
- code changes
- QA checklist
- DELIVERY_SUMMARY_TEMPLATE.md filled in

### Mode 3: Validation Mode
Goal:
Prove the approved task works.

Allowed:
- install
- build
- run
- screenshot
- smoke test
- deployment check

Output:
- validation report
- screenshots
- fail/pass summary

## Cycle
1. Audit
2. Human approval
3. Execution
4. Validation
5. Delivery summary
6. Task board update
7. Knowledge capture if reusable lesson found

## Golden Rules
1. One approved task per cycle
2. No silent scope expansion
3. No landing page redesign during backend cycles
4. Every cycle must end with a summary the human can read in under 2 minutes
5. Logs are secondary, summaries are primary
