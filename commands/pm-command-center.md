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
- tells you whether you are still in strategy work or ready for execution work

## Default Mental Model

Lighty should route into one of three entry modes:

1. `product audit`
2. `new idea`
3. `long-range vision`

All three share the same engine:

`signals -> personas -> simulation -> strategy -> execution`

## Output Contract

A good `pm-command-center` response should always include:

1. detected mode
2. why that mode applies
3. current stage of work
4. recommended next command
5. optional second-best command
6. recommended skill chain

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
- Make it explicit whether OASIS-style simulation is useful, optional, or unnecessary for the current job.
- Prefer the shortest path that sharpens the decision, not the most impressive-looking workflow.

## Recommended Next Step

If nothing else is clear, start with `find-winning-direction`.
