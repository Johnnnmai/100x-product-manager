# Prioritize 100X PM Run

## Run Metadata

- Task: prioritization
- Command: `prioritize`
- Date: 2026-03-10
- Operator: Codex internal pilot
- Model: GPT-5 Codex
- Temperature: default
- Arm: `100xpm`

## Input Bundle

- Source files: `commands/prioritize.md`
- Problem statement: choose which requests should ship in the next 6 weeks
- Constraints: 2 engineers, 1 designer
- Success criteria: clear ranked priority list with trade-offs

## Prompt Used

```text
Using commands/prioritize.md:

We have 2 engineers and 1 designer for the next 6 weeks.

Please prioritize these requests:
- Slack digest
- HubSpot sync
- health score explanation
- exec dashboard
- auto playbooks
- bulk CSV import

Goal:
- help customer success teams retain at-risk accounts
- prove weekly product usage

Follow the command exactly.
Force an order.
Make explicit what loses when something wins.
```

## Output Artifact

```md
# Prioritization Decision

## Objective

In the next 6 weeks, maximize weekly CSM usage tied to at-risk account follow-up.

## Recommendation

### Do now

1. Slack digest
2. health score explanation
3. HubSpot sync

### Do later

4. bulk CSV import
5. auto playbooks

### Do not do in this cycle

6. exec dashboard

## Why this order wins

### 1. Slack digest

This is the shortest path to repeat weekly visibility. If users do not see the product in their daily workflow, nothing else matters.

### 2. Health score explanation

If the product flags risk without explaining why, trust drops. This directly supports retention-oriented usage.

### 3. HubSpot sync

Useful, but only after the core signal is visible and understandable. It improves workflow completion, not first-order trust.

## Explicit trade-offs

- choosing Slack digest first means delaying deeper systems integration
- choosing explanation before automation means better trust now, less workflow compression now
- not doing the exec dashboard means leadership reporting loses this cycle so operator workflow can win

## Downside of the chosen path

- manual copy/paste pain remains longer
- some stakeholders will ask why leadership visibility is delayed

## Review checkpoint

Re-rank after 3 pilot accounts or 2 weeks of active usage data, whichever comes first.
```

## Workflow Metrics

- Total turns: 1
- Clarification turns: 0
- Time to first draft: 6 min
- Time to acceptable draft: 9 min
- Manual edits after first draft: 2 substantive edits

## Notes

- What improved: objective alignment, explicit losers, stakeholder impact, review checkpoint
- What failed: still no quantitative cost model, but the decision is much more usable
- Should this run count toward the public benchmark: `yes`
