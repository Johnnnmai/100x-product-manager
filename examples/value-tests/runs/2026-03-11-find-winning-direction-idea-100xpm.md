# Find Winning Direction Idea 100X PM Run

## Run Metadata

- Task: front-door new idea mode
- Command: `find-winning-direction`
- Date: 2026-03-11
- Operator: Codex internal pilot
- Model: GPT-5 Codex
- Temperature: default
- Arm: `100xpm`

## Input Bundle

- Source files: `examples/value-tests/input-bundles/2026-03-11-new-idea-input.md`
- Problem statement: founder wants a bet with a convincing first demo
- Constraints: solo founder, one contract engineer, 6 weeks, one clear proof point
- Success criteria: choose a wedge, business model, channel, and next validation step

## Prompt Used

```text
Using commands/find-winning-direction.md with Lighty:

Classify the input mode first.
Use the new-idea input bundle exactly.
Generate 2-3 viable directions before recommending one.
Make the wedge, business model, and first channel explicit.
End with the next command.
```

## Output Artifact

```md
# Find Winning Direction: New Idea Mode

## Detected mode

New idea mode.

## Direction options

### Option A: Founder website audit + strategy compiler

Start from a live website or landing page.
Return pain points, wedge, business model moves, and a build plan.

Why it is strong:
- concrete input
- easy to demo
- naturally leads into PRD and roadmap generation

### Option B: Full founder strategy OS

Handle idea validation, planning, content, and delegation in one product.

Why it is too broad first:
- too many jobs at once
- harder to explain in one demo
- higher implementation surface

### Option C: PM internal copilot

Focus on PRDs, prioritization, and roadmap writing.

Why it is weaker:
- easier to copy
- sounds like "better doc writing"
- loses the simulation moat

## Recommended wedge

Start with **website audit + strategy compiler for founders and PMs**.

This wedge is more concrete than a vague "product OS" claim and better showcases the market-signal plus simulation story.

## Business model

Sell as a premium workflow for strategy compression:
- audit a site or product
- surface the strongest bet
- compile into PRD and roadmap

## First channel

Use public teardown content:
- audit a real website
- show the pain-point map and stronger wedge
- end with the compiled execution plan

## What to validate next

Validate whether users care more about:
- pain-point discovery
- strategic narrative
- or agent-ready execution outputs

## Next command

`validate-demand`
```

## Workflow Metrics

- Total turns: 1
- Clarification turns: 0
- Time to first draft: 8 min
- Time to acceptable draft: 11 min
- Manual edits after first draft: 2

## Notes

- What improved: better wedge choice, cleaner sequencing, stronger demo path
- What failed: still assumption-heavy because no live market data was added in this run
- Should this run count toward the public benchmark: `yes`
