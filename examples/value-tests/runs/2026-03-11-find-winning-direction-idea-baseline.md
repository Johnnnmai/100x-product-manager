# Find Winning Direction Idea Baseline Run

## Run Metadata

- Task: front-door new idea mode
- Command: plain prompt baseline
- Date: 2026-03-11
- Operator: Codex internal pilot
- Model: GPT-5 Codex
- Temperature: default
- Arm: `baseline`

## Input Bundle

- Source files: `examples/value-tests/input-bundles/2026-03-11-new-idea-input.md`
- Problem statement: founder wants an idea worth betting on
- Constraints: solo founder, one contract engineer, 6 weeks, one strong demo
- Success criteria: choose a viable direction

## Prompt Used

```text
Given this startup idea, suggest the best product direction, target user, and GTM strategy.
```

## Output Artifact

```md
# Product Direction Suggestion

You should build an AI platform for founders and product teams.

## Suggested features

- idea validation
- roadmap generation
- PRD writing
- user persona creation

## Go-to-market

- target startups
- create content on LinkedIn
- offer a free trial

## Why it could work

People need faster product strategy.
```

## Workflow Metrics

- Total turns: 1
- Clarification turns: 0
- Time to first draft: 12 min
- Time to acceptable draft: 19 min
- Manual edits after first draft: 5

## Notes

- What improved: broad category framing
- What failed: no wedge, weak sequencing, no explicit validation path
- Should this run count toward the public benchmark: `yes`
