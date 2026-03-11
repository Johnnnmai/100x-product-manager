# pm-command-center

Use this when you are not sure which command to run first.

Think of this as **Lighty's routing desk**.

Lighty should first classify the request into one of three modes:

1. product audit mode
2. new idea mode
3. long-range vision mode

## What It Does

- classifies the PM or founder job-to-be-done
- decides which Lighty mode applies
- identifies the current stage of work
- routes to the shortest useful next command
- recommends the next skill chain

## Routing Logic

- website, product, app, reviews, support logs, unclear pain points -> `find-winning-direction`
- rough idea, unclear wedge, unclear business model -> `find-winning-direction`
- scattered strategy docs, unclear 3-5 year direction -> `find-winning-direction`
- rough idea, no clear wedge -> `shape-idea`
- many signals, unclear demand -> `validate-demand`
- approved direction, need a spec -> `agent-prd`
- too many initiatives, not enough focus -> `prioritize`
- success definition is weak or missing -> `define-metrics`
- need to test a hypothesis -> `design-experiment`
- shipping AI behavior -> `design-eval`
- need milestones, ownership, and tracking -> `run-roadmap`
- need distribution from internal work -> `make-content`

## Operating Rules

- Route to `find-winning-direction` when the job is strategic and still upstream of execution.
- If the problem is fuzzy, route to the narrowing command, not the drafting command.
- If the work is irreversible or high risk, make the choice explicit before proceeding.
- If ambiguity is high, present meaningful options before locking a path.

## Recommended Next Step

If nothing else is clear, start with `find-winning-direction`.
