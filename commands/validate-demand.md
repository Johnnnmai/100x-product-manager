# validate-demand

Use this when you have feedback, notes, tickets, comments, URLs, dashboards, or intuition and need to judge whether demand is real.

## Input

- interview notes
- support tickets
- sales feedback
- app reviews or comments
- URLs and competitor pages
- dashboards or product notes

## Output

- evidence bundle
- signal vs noise summary
- demand confidence level
- contradictions in the evidence
- risky assumptions
- next validation step

## Default Workflow

1. Normalize raw inputs with `evidence-collector`
2. Pull external or public signals with `market-signal-harvester`
3. Check internal consistency with `evidence-triangulator`
4. Judge whether the demand is real with `demand-reality-checker`
5. Synthesize implications with `user-insight-synthesizer`

## Operating Rules

- Do not confuse loudness with demand.
- Do not confuse simulated market logic with validated truth.
- Separate evidence, assumptions, and open questions.
- If evidence is weak, recommend the shortest useful next validation step.

## Recommended Skills

- `skills/evidence-collector/SKILL.md`
- `skills/market-signal-harvester/SKILL.md`
- `skills/evidence-triangulator/SKILL.md`
- `skills/demand-reality-checker/SKILL.md`
- `skills/user-insight-synthesizer/SKILL.md`

## Next Command

- If demand looks real and the idea is still fuzzy: `shape-idea`
- If scope is ready to spec: `agent-prd`
