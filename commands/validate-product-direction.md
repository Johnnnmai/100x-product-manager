# validate-product-direction

This command remains the narrower validation engine behind founder-facing direction work.

If you want the full founder workflow covering wedge, business model, channel, narrative, and execution path, start with `commands/find-winning-direction.md`.

Use this when you have a product idea and want to validate it with real-world data and persona simulation before committing significant resources.

## Input

- product idea or hypothesis
- target market or user segment
- existing research (if any)
- success criteria for validation
- constraints (budget, timeline, resources)

## Output

- validated product hypothesis
- market signal summary
- persona reaction simulations
- data-backed recommendations
- confidence level
- next recommended command

## Default Workflow

1. Run `skills/signal-harvester-enhanced/SKILL.md` to collect web signals
2. Run `skills/persona-simulation-builder/SKILL.md` to build personas
3. Run simulation (MiroFish/OASIS) - [manual step, requires setup]
4. Run `skills/simulation-analyst/SKILL.md` to analyze results
5. Synthesize into final recommendations

## Operating Rules

- Run full pipeline for comprehensive validation
- If MiroFish/OASIS not available, use manual persona simulation
- Report confidence levels honestly
- Include limitations and caveats

## Recommended Skills

- `skills/signal-harvester-enhanced/SKILL.md`
- `skills/persona-simulation-builder/SKILL.md`
- `skills/simulation-analyst/SKILL.md`
- `skills/product-direction-validation/SKILL.md`

## Prerequisites

For full simulation capability:
- MiroFish installed (http://localhost:5001) OR
- OASIS installed

For manual approach:
- Claude Code or similar LLM
- Web research capability

## Next Command

- `agent-prd` (if validated positively)
- `prioritize` (if multiple directions)
- `shape-idea` (if validation suggests pivot)
