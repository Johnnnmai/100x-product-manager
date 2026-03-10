# Shape Idea Baseline Run

## Run Metadata

- Task: rough idea shaping
- Command: none
- Date: 2026-03-10
- Operator: Codex internal pilot
- Model: GPT-5 Codex
- Temperature: default
- Arm: `baseline`

## Input Bundle

- Source files: none
- Problem statement: founder has a rough idea for AI support in customer success
- Constraints: 2-person team, no CRM writeback, 6 weeks to prove value
- Success criteria: produce a first direction worth validating

## Prompt Used

```text
We are a 2-person team building AI software for mid-market SaaS customer success managers.

Idea:
- use Zoom transcripts to summarize calls
- estimate churn risk
- suggest follow-ups

Constraints:
- we do not have CRM writeback yet
- we have 6 weeks to prove value

What should we build first?
```

## Output Artifact

```md
# AI Customer Success Copilot

You should build an AI copilot for customer success managers.

## Problem

CSMs do not have time to review calls and may miss churn signals.

## Users

Mid-market SaaS customer success managers.

## What to build

- call summaries
- churn risk scores
- next-step recommendations

## Why

This helps teams move faster and retain more customers.

## MVP

Start with summaries and churn flags from Zoom transcripts.

## Success metric

Teams use the product weekly and find it helpful.

## Next step

Talk to a few users and start building the MVP.
```

## Workflow Metrics

- Total turns: 1
- Clarification turns: 0
- Time to first draft: 8 min
- Time to acceptable draft: 18 min
- Manual edits after first draft: 5 substantive edits

## Notes

- What improved: fast first answer
- What failed: no wedge comparison, no explicit trade-offs, weak metric definition
- Should this run count toward the public benchmark: `yes`
