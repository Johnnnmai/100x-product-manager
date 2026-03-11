# Find Winning Direction Vision Baseline Run

## Run Metadata

- Task: front-door long-range vision mode
- Command: plain prompt baseline
- Date: 2026-03-11
- Operator: Codex internal pilot
- Model: GPT-5 Codex
- Temperature: default
- Arm: `baseline`

## Input Bundle

- Source files: `examples/value-tests/input-bundles/2026-03-11-long-range-vision-input.md`
- Problem statement: leadership wants a long-range product direction
- Constraints: next 12 months must stay focused; no vague platform story
- Success criteria: produce a usable long-range direction and roadmap

## Prompt Used

```text
Given these internal notes, create a 3-5 year product vision and roadmap.
```

## Output Artifact

```md
# Long-Range Vision

The company should become a product platform for PMs and founders.

## Vision

- help users with planning
- help users with execution
- create an ecosystem over time

## Roadmap

### Near term
- improve current features
- grow the user base

### Mid term
- expand into agents
- support more workflows

### Long term
- become the default operating system for product teams
```

## Workflow Metrics

- Total turns: 1
- Clarification turns: 0
- Time to first draft: 15 min
- Time to acceptable draft: 24 min
- Manual edits after first draft: 7

## Notes

- What improved: broad aspiration captured
- What failed: vague platform language, no phased themes, weak short-term vs long-term split
- Should this run count toward the public benchmark: `yes`
