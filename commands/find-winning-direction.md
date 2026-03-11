# find-winning-direction

Use this when the work is still upstream of execution and you need one workflow that can turn a product, an idea, or messy context into a direction a PM or founder can actually bet on.

This is the strategic front door for:
- wedge selection
- business model design
- channel strategy
- strategic narrative
- execution handoff

This is also **Lighty's primary workflow**.

Lighty should first decide which of these three modes applies:

1. **Product audit mode**: start from a live website, app, product, review set, or support log
2. **New idea mode**: start from a rough concept, thesis, or founder instinct
3. **Long-range vision mode**: start from fragmented internal context that needs a 3-5 year direction

## Input

- rough product idea
- target user or market guess
- constraints, if known
- any early signals, convictions, or fears
- website or product URL, if auditing
- messy docs, notes, or strategy context, if building long-range vision

## Output

- 2-3 direction options with explicit trade-offs
- recommended wedge
- recommended business model
- recommended first channel
- strategic narrative that explains why this can become large
- top risks and open questions
- execution path
- next execution command

## Entry Modes

### Product Audit Mode

Use when the user gives:
- a website
- an app
- a current product
- reviews, tickets, support logs, or competitor pages

Goal:
- discover hidden pain points
- generate stronger product hypotheses
- validate them with market signals and simulation logic
- turn them into strategy and execution

### New Idea Mode

Use when the user gives:
- a startup idea
- a fuzzy PM concept
- a market they want to enter

Goal:
- narrow the wedge
- make the business model explicit
- choose the first channel
- define the first operating plan

### Long-Range Vision Mode

Use when the user gives:
- scattered notes
- internal docs
- roadmap chaos
- fragmented product context

Goal:
- compress chaos into a 3-5 year direction
- separate strategic bets from near-term execution
- produce a phased roadmap and narrative

## Default Workflow

1. Let Lighty classify the request into product audit, new idea, or long-range vision mode
2. Use `Scrapling`-style signal gathering and `commands/validate-demand.md` logic to ground the work in external evidence
3. Build persona or market-twin inputs when user reaction and adoption uncertainty matter
4. Use the OASIS / MiroFish-style simulation chain when it will materially sharpen the bet
5. Use `commands/shape-idea.md` logic if the space is still too broad
6. Translate the chosen direction into spec and execution via `commands/agent-prd.md` and `commands/run-roadmap.md`

## Operating Rules

- Start with strategic options, not a single answer
- Make the business model and channel explicit, not implied
- Optimize for the strongest plausible wedge, not the biggest vague market
- Separate fact, inference, and recommendation
- Include ambition, but keep the first move grounded
- If the input is a live product, look for pain points and leverage before drafting solutions
- If the input is a vision question, separate 12-month execution from 3-5 year direction
- Separate strategic output from execution output
- State where evidence ends and simulation-backed inference begins

## Response Shape

### Strategic Layer

1. Detected mode
2. Direction options
3. Recommended wedge or hypothesis set
4. Business model
5. Channel strategy
6. Why this story can get big
7. Risks, assumptions, and unknowns

### Execution Layer

1. What should be validated next
2. What should be written into a PRD
3. What should enter the roadmap
4. Next command

## Recommended Skills

- `skills/product-direction-validation/SKILL.md`
- `skills/market-signal-harvester/SKILL.md`
- `skills/signal-harvester-enhanced/SKILL.md`
- `skills/persona-simulation-builder/SKILL.md`
- `skills/simulation-analyst/SKILL.md`
- `skills/prioritization-advisor/SKILL.md`

## Optional Strategy Lab

When simulation meaningfully improves the decision, use this stack:

- `Scrapling` for public web and social signals
- persona / market-twin building for simulation-ready profiles
- `OASIS` for persona-reaction and market-twin simulation
- `MiroFish` for richer reporting and digital-twin style outputs

The core output should still work without simulation, but the simulation layer is a core differentiator when available.

## Next Command

- `validate-demand` if the direction needs stronger evidence
- `agent-prd` if the direction is chosen and needs execution detail
- `run-roadmap` if the plan is ready to delegate
- `make-content` if the narrative should be turned into public-facing content
