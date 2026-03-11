# Find Winning Direction Audit 100X PM Run

## Run Metadata

- Task: front-door product audit
- Command: `find-winning-direction`
- Date: 2026-03-11
- Operator: Codex internal pilot
- Model: GPT-5 Codex
- Temperature: default
- Arm: `100xpm`

## Input Bundle

- Source files: `examples/value-tests/input-bundles/2026-03-11-product-audit-input.md`
- Problem statement: audit an existing AI customer-success product and recommend the strongest bet
- Constraints: 2 engineers, 1 designer, 8 weeks, no CRM writeback
- Success criteria: sharpen direction and define the next execution step

## Prompt Used

```text
Using commands/find-winning-direction.md with Lighty:

Classify this as product audit, new idea, or long-range vision mode.
Use the product-audit input bundle exactly.
Use market signals first.
State where evidence ends and inference begins.
Give me:
- direction options
- the best wedge
- business model move
- channel implication
- execution path
- next command
```

## Output Artifact

```md
# Find Winning Direction: PulsePilot Audit

## Detected mode

Product audit mode.

## Evidence summary

Evidence says the summary and follow-up workflow is trusted more than the churn score.
Evidence also says alert noise and setup friction weaken belief in the "AI risk engine" story.

## Direction options

### Option A: Post-call execution copilot

Turn every call into a concise recap, next-step draft, and manager-shareable brief.

Why it fits:
- trusted workflow already exists
- no CRM writeback needed
- weekly usage loop is obvious

### Option B: Churn prediction engine

Double down on risk scoring and alerts.

Why it is weak right now:
- trust gap is already visible
- proof burden is too high for 8 weeks
- likely to create false-confidence problems

### Option C: Manager inspection layer

Use call data to surface team-level customer risk patterns.

Why it is not first:
- depends on better account context
- less immediately useful to frontline CSMs

## Recommended wedge

Choose **post-call execution copilot**, not "AI churn prediction."

That wedge is stronger because the product is already trusted for compression of follow-up work, while the current risk narrative is overreaching.

## Business model move

Sell workflow compression first.

Do not price on "predictive intelligence" until the product earns trust.
Package around time saved per CSM workflow, then expand later into manager reporting.

## Channel implication

Lead through customer-success operators and CS leaders, not through abstract AI positioning.
The strongest channel story is:
"Save follow-up prep time after every customer call."

## Risks and unknowns

- teams may still ask for account-level context quickly
- summaries may become a feature unless next-step workflow is sticky
- score language must stay evidence-linked to avoid fake certainty

## Execution path

1. Narrow v1 to recap + follow-up + manager brief
2. Test weekly usage with 5 pilot CSMs
3. Measure time saved and repeat usage before reintroducing deeper prediction claims

## Next command

`agent-prd`
```

## Workflow Metrics

- Total turns: 1
- Clarification turns: 0
- Time to first draft: 8 min
- Time to acceptable draft: 12 min
- Manual edits after first draft: 2

## Notes

- What improved: sharper wedge, stronger business model logic, more believable channel story, cleaner next step
- What failed: still a simulation-light audit because no live web scrape was run inside this benchmark
- Should this run count toward the public benchmark: `yes`
