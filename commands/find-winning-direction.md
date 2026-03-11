# find-winning-direction

Use this when you have a rough idea and need to turn it into a product direction that a PM or founder can actually bet on.

This is the founder-facing front door for:
- wedge selection
- business model design
- channel strategy
- strategic narrative
- execution handoff

## Input

- rough product idea
- target user or market guess
- constraints, if known
- any early signals, convictions, or fears

## Output

- 2-3 direction options with explicit trade-offs
- recommended wedge
- recommended business model
- recommended first channel
- strategic narrative that explains why this can become large
- top risks and open questions
- next execution command

## Default Workflow

1. Use `commands/shape-idea.md` logic to narrow the space
2. Pressure-test the best option with `commands/validate-demand.md`
3. If deeper strategy testing is needed, use `commands/validate-product-direction.md`
4. Translate the chosen direction into spec and execution via `commands/agent-prd.md` and `commands/run-roadmap.md`

## Operating Rules

- Start with strategic options, not a single answer
- Make the business model and channel explicit, not implied
- Optimize for the strongest plausible wedge, not the biggest vague market
- Separate fact, inference, and recommendation
- Include ambition, but keep the first move grounded

## Response Shape

1. Direction options
2. Recommended wedge
3. Business model
4. Channel strategy
5. Why this story can get big
6. Risks, assumptions, and unknowns
7. Next command

## Recommended Skills

- `skills/product-direction-validation/SKILL.md`
- `skills/market-signal-harvester/SKILL.md`
- `skills/signal-harvester-enhanced/SKILL.md`
- `skills/prioritization-advisor/SKILL.md`

## Optional Strategy Lab

If available, use `MiroFish` or `OASIS` as a second-layer strategy lab to simulate persona reactions. This is optional. The core output should still work without simulation.

## Next Command

- `validate-demand` if the direction needs stronger evidence
- `agent-prd` if the direction is chosen and needs execution detail
- `run-roadmap` if the plan is ready to delegate
- `make-content` if the narrative should be turned into public-facing content
