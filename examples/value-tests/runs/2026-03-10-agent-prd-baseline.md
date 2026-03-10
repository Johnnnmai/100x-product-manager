# Agent PRD Baseline Run

## Run Metadata

- Task: dual-mode PRD writing
- Command: none
- Date: 2026-03-10
- Operator: Codex internal pilot
- Model: GPT-5 Codex
- Temperature: default
- Arm: `baseline`

## Input Bundle

- Source files: none
- Problem statement: create a PRD for a post-call risk brief for CSMs
- Constraints: transcript-only input, no CRM writeback, 2 engineers, 1 designer, 6-week pilot
- Success criteria: produce a spec an engineer can start from

## Prompt Used

```text
Write a PRD for a product that creates a post-call risk brief for customer success managers.

Constraints:
- transcript-only input
- no CRM writeback
- 2 engineers and 1 designer
- 6-week pilot
```

## Output Artifact

```md
# PRD: Post-call Risk Brief

## Overview

Build an AI tool that turns customer call transcripts into summaries, risk signals, and next steps for CSMs.

## Goals

- save time
- improve follow-up quality
- help spot churn risk

## Features

- transcript ingestion
- summary generation
- churn signal detection
- recommended next actions

## Timeline

The team should launch an MVP in 6 weeks.

## Success

Users should adopt the tool and like the output.

## Risks

- low accuracy
- weak adoption
```

## Workflow Metrics

- Total turns: 1
- Clarification turns: 0
- Time to first draft: 11 min
- Time to acceptable draft: 25 min
- Manual edits after first draft: 7 substantive edits

## Notes

- What improved: quick draft
- What failed: no task contract, no dependencies, no fallback, weak success metrics
- Should this run count toward the public benchmark: `yes`
