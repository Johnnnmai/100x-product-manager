# Shape Idea 100X PM Run

## Run Metadata

- Task: rough idea shaping
- Command: `shape-idea`
- Date: 2026-03-10
- Operator: Codex internal pilot
- Model: GPT-5 Codex
- Temperature: default
- Arm: `100xpm`

## Input Bundle

- Source files: `commands/shape-idea.md`
- Problem statement: founder has a rough idea for AI support in customer success
- Constraints: 2-person team, no CRM writeback, 6 weeks to prove value
- Success criteria: produce a first direction worth validating

## Prompt Used

```text
Using commands/shape-idea.md:

We are a 2-person team building AI software for mid-market SaaS customer success managers.

Idea:
- use Zoom transcripts to summarize calls
- estimate churn risk
- suggest follow-ups

Constraints:
- we do not have CRM writeback yet
- we have 6 weeks to prove value

Follow the command exactly.
Generate 2-3 viable directions before recommending one.
Make assumptions explicit.
End with the next recommended command.
```

## Output Artifact

```md
# Shape Idea: AI Workflow for Customer Success

## Assumptions

- The team can access transcripts quickly but cannot push data back into a system of record.
- The first proof point must be visible to a CSM without requiring IT-heavy setup.
- A 6-week win is more likely to come from workflow compression than from a high-confidence risk model.

## Viable directions

### Option A: Post-call risk brief

After every customer call, generate a short brief with account health signals, renewal risk cues, and next-step suggestions.

Why it works:
- fits the transcript-only constraint
- easy for a CSM to trial immediately
- avoids deep systems integration

### Option B: Portfolio churn radar

Roll multiple calls into an account-level risk view.

Why it is weaker first:
- needs more historical context
- higher false-confidence risk
- harder to prove value in 6 weeks

### Option C: Renewal prep assistant

Generate renewal prep packs before QBRs and renewals.

Why it is promising:
- tied to a clear business moment
- easier to explain internally

Why it loses first:
- less frequent workflow than post-call usage

## Recommended wedge

Start with **Option A: post-call risk brief**.

This is the smallest wedge that:
- uses the data you already have
- creates immediate user-visible value
- gives you artifacts that can later feed a renewal prep workflow

## Scope-down recommendation

Version 1 should do only four things:
- generate a 5-bullet call summary
- flag 2-3 risk cues from transcript language
- propose next-step follow-ups
- let a CSM edit and copy the brief

Do not build:
- account health scoring across the full book
- CRM writeback
- automated playbooks

## Top risks

1. Risk labels may look more confident than the transcript evidence deserves.
2. CSMs may value concise summaries more than abstract churn scores.
3. Without a clear usage loop, the product may become a novelty rather than a weekly workflow.

## First success metric draft

Within 6 weeks, at least 5 pilot CSMs should use the post-call brief on 3 or more calls per week, and at least 60% should say the brief saved them time on follow-up preparation.

## Next recommended command

`validate-demand`
```

## Workflow Metrics

- Total turns: 1
- Clarification turns: 0
- Time to first draft: 7 min
- Time to acceptable draft: 10 min
- Manual edits after first draft: 2 minor edits

## Notes

- What improved: wedge comparison, scope discipline, explicit assumptions, stronger metric draft
- What failed: still no external evidence because this was idea-shaping only
- Should this run count toward the public benchmark: `yes`
