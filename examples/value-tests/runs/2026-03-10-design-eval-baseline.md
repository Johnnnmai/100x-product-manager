# Design Eval Baseline Run

## Run Metadata

- Task: AI eval design
- Command: none
- Date: 2026-03-10
- Operator: Codex internal pilot
- Model: GPT-5 Codex
- Temperature: default
- Arm: `baseline`

## Input Bundle

- Source files: none
- Problem statement: design evaluation for an AI post-call brief with risk labels and follow-up suggestions
- Constraints: medium-high trust risk because bad risk labels may mislead a CSM
- Success criteria: pass/fail logic before launch

## Prompt Used

```text
Design an evaluation plan for an AI feature that creates post-call customer briefs with risk labels and follow-up suggestions.

Risk level is medium-high because wrong risk labels could mislead a customer success manager.
```

## Output Artifact

```md
# Evaluation Plan

## Goals

- check output quality
- reduce hallucinations
- make sure risk labels are useful

## Test ideas

- use good examples
- use bad examples
- review outputs manually

## What to watch for

- wrong summaries
- wrong risk calls
- bad next steps

## Recommendation

Run sample transcripts through the model and see if the outputs look correct before launch.
```

## Workflow Metrics

- Total turns: 1
- Clarification turns: 0
- Time to first draft: 8 min
- Time to acceptable draft: 20 min
- Manual edits after first draft: 6 substantive edits

## Notes

- What improved: identified the right broad categories
- What failed: no pass/fail rules, no fallback, no escalation trigger
- Should this run count toward the public benchmark: `yes`
