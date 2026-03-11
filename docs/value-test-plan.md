# 100X PM Value Test Plan

This is the public test plan for proving whether 100X PM skills create better PM and founder outputs than plain prompting.

We are not going to publish fake benchmark numbers.

Proof should come from repeatable tasks, blinded scoring, and raw artifacts that other people can inspect.

## Goal

Answer one question:

**Do 100X PM commands help people get to sharper, more usable product artifacts faster than a plain prompt?**

## Primary Hypotheses

### H1: Artifact quality

Using a 100X PM command on the same input should produce a stronger first draft than a plain prompt.

Expected deltas:

- clearer problem framing
- fewer hidden assumptions
- more explicit trade-offs
- stronger execution readiness
- better next-step recommendation

### H2: Workflow efficiency

Using a 100X PM command should reduce the time and editing effort needed to reach an acceptable artifact.

Expected deltas:

- fewer clarification turns
- less manual restructuring
- shorter time to acceptable draft

### H3: Decision usefulness

Using a 100X PM command should increase how often the output is judged immediately usable by a PM, founder, or operator.

## Benchmark Structure

Keep the model constant when isolating prompt or skill quality.

For each task, run at least two arms:

- `Baseline`: plain prompt with the same input bundle
- `100X PM`: prompt explicitly routed through the relevant command file

Optional third arm:

- `100X PM + follow-up`: same command plus one clarification round if the workflow naturally requires it

## Canonical Task Set

Use one task per front-door command.

| Task | Command | Input bundle | Expected artifact |
| --- | --- | --- | --- |
| Ambiguous product request routing | `pm-command-center` | messy ask from founder or leadership | routed job + recommended next command |
| Rough idea shaping | `shape-idea` | vague idea, weak instinct, some constraints | wedge recommendation + risks + first move |
| Demand validation | `validate-demand` | support tickets, reviews, notes, URLs | demand memo with evidence judgment |
| Spec writing | `agent-prd` | approved direction + constraints | dual-mode PRD |
| Prioritization | `prioritize` | 5-8 requests with limited capacity | ranked decision + defer list + trade-offs |
| Metrics definition | `define-metrics` | goal statement + product context | success metric spec |
| Experiment design | `design-experiment` | product hypothesis | experiment plan |
| AI eval design | `design-eval` | AI feature concept + risk profile | eval and guardrail plan |
| Roadmap delegation | `run-roadmap` | approved scope + team constraints | roadmap with milestones and ownership |
| Distribution packaging | `make-content` | shipped work or PRD | content brief or post draft |

## Scoring Rubric

Each artifact should be scored by at least two reviewers blinded to which arm produced it.

Use a 1-5 scale for:

- problem clarity
- scope sharpness
- trade-off explicitness
- evidence quality
- execution readiness
- metric quality
- next-step clarity

Use binary or penalty checks for:

- unsupported claims present
- obvious ambiguity left unresolved
- missing owner or decision point
- false confidence

Recommended scorecard:

- [examples/value-tests/scorecard-template.md](../examples/value-tests/scorecard-template.md)

## Workflow Metrics

For each run, also capture:

- model used
- turns required
- elapsed time to first acceptable draft
- manual edits after first draft
- whether the evaluator would actually use the output

Recommended run log:

- [examples/value-tests/task-run-template.md](../examples/value-tests/task-run-template.md)

## Success Criteria

Claim success only if the command-guided arm beats baseline on both quality and efficiency.

Minimum bar for a command to count as proven:

- average quality score improvement of at least `+0.8` on a 5-point scale
- at least `25%` reduction in time to acceptable draft, or
- at least `30%` reduction in manual edits after first draft
- no increase in unsupported-claim rate

## Test Execution Rules

To keep the benchmark honest:

1. Use the same input bundle across arms.
2. Keep the model, temperature, and token budget fixed where possible.
3. Randomize review order.
4. Blind reviewers to which arm produced the artifact.
5. Save raw prompts and outputs.
6. Record failures, not just wins.

## Public Proof Artifacts

Each benchmarked task should produce four public artifacts:

1. before/after pair
2. scored rubric sheet
3. task run log
4. short summary of why the command won, lost, or tied

Store public artifacts under:

```text
examples/
  value-tests/
    runs/
      <date>-<task-name>-baseline.md
      <date>-<task-name>-100xpm.md
      <date>-<task-name>-scorecard.md
      <date>-<task-name>-summary.md
```

## README / Homepage Proof Design

Popular repos usually do one of two things well:

- compact benchmark table near the top
- direct before/after examples with raw artifacts linked

For 100X PM, use both.

### Layer 1: compact proof table

Put one small table in `README.md`:

| Proof layer | What it compares | Status |
| --- | --- | --- |
| Before/after artifacts | same input, plain prompt vs command-guided output | live |
| Pilot benchmark wave 1 | baseline vs 100X PM on 4 canonical PM tasks | live |
| Blind-scored benchmark | baseline vs 100X PM across canonical PM tasks | planned |
| Real workflow metrics | time to acceptable draft, edit burden, reuse | planned |

### Layer 2: artifact proof

Link 3-5 strong before/after examples directly from README.

Best categories:

- PRD
- prioritization
- AI eval
- idea shaping
- roadmap delegation

### Layer 3: benchmark summary table

Add this only after real data exists:

| Task | Baseline | 100X PM | Delta |
| --- | --- | --- | --- |
| PRD completeness | `x/5` | `y/5` | `+z` |
| Time to acceptable draft | `x min` | `y min` | `-z%` |
| Unsupported claims | `x` | `y` | `-z` |

## Recommended First Benchmark Wave

Start with 4 tasks before expanding to all 10:

1. `shape-idea`
2. `agent-prd`
3. `prioritize`
4. `design-eval`

These four best represent the repo's value proposition:

- rough ambiguity to sharper scope
- human + agent execution spec
- explicit trade-offs
- AI behavior quality

## What Not To Do

- do not compare different models and call it a skill win
- do not cherry-pick only the best examples
- do not publish percentages without raw task counts
- do not turn subjective vibes into benchmark claims
- do not ship homepage metrics that cannot be traced back to artifacts

## Current Status

Current public proof:

- [examples/before-after/prd-before-after.md](../examples/before-after/prd-before-after.md)
- [examples/before-after/prioritization-before-after.md](../examples/before-after/prioritization-before-after.md)
- [examples/before-after/eval-before-after.md](../examples/before-after/eval-before-after.md)
- [examples/value-tests/runs/2026-03-10-wave-1-summary.md](../examples/value-tests/runs/2026-03-10-wave-1-summary.md)
- [examples/value-tests/runs/2026-03-11-wave-2-front-door-summary.md](../examples/value-tests/runs/2026-03-11-wave-2-front-door-summary.md)

Next build step:

- expand the front-door pilot into blinded review under `examples/value-tests/runs/`
