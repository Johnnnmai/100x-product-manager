# Start Here

If you are new here, think of **100X PM** as a public operating system for multiplying judgment, not just writing faster.

By default, interact with 100X PM through **Lighty**, the mascot-guide that asks one routing question first:

**Are we auditing a product, shaping a new idea, or building long-range vision?**

## Fastest Path

1. Open [commands/pm-command-center.md](commands/pm-command-center.md)
2. If you are a PM or founder with a rough idea and need direction, business model, and channel, run [commands/find-winning-direction.md](commands/find-winning-direction.md)
3. If all you need is idea shaping, run [commands/shape-idea.md](commands/shape-idea.md)
4. If you need proof before motion, run [commands/validate-demand.md](commands/validate-demand.md)
5. If scope is approved and execution needs a spec, run [commands/agent-prd.md](commands/agent-prd.md)
6. If you are planning work across humans and agents, run [commands/run-roadmap.md](commands/run-roadmap.md)

## Lighty Routing Modes

- **Product audit mode**: use when the input is a site, app, product, review set, support log, or competitor context
- **New idea mode**: use when the input is a rough product or startup idea
- **Long-range vision mode**: use when the input is a pile of docs, strategy notes, or fragmented context

If you are unsure, let Lighty route for you through `pm-command-center`.

## If Your Situation Looks Like This

- "I want to audit an existing product with social signals and simulation." -> `find-winning-direction`
- "I have a rough startup idea and need the wedge, business model, and launch channel." -> `find-winning-direction`
- "I need to turn scattered context into a 3-5 year product direction." -> `find-winning-direction`
- "I only have a rough idea." -> `shape-idea`
- "I have signals, but I do not know if demand is real." -> `validate-demand`
- "I need a PRD that an engineer and an agent can both execute." -> `agent-prd`
- "I need to decide what to cut or defer." -> `prioritize`
- "I need metrics, thresholds, and instrumentation." -> `define-metrics`
- "I need to test a hypothesis in the market." -> `design-experiment`
- "I am shipping an AI feature and need evals." -> `design-eval`
- "I need a roadmap with ownership and tracking." -> `run-roadmap`
- "I want to turn the work into public content." -> `make-content`

## Recommended Prompt Pattern

```text
Using commands/<command-name>.md:
1. Follow the command exactly.
2. If ambiguity is high, surface meaningful options before acting.
3. Make assumptions explicit.
4. Produce markdown I can reuse.
5. End with risks, open questions, and the next recommended command.
```

Founder prompt shortcut:

```text
Using commands/find-winning-direction.md with Lighty:
First decide whether this is product audit mode, new idea mode, or long-range vision mode.
Use market signals and OASIS-style persona simulation where useful.
Recommend the best wedge, business model, first channel, and strategic narrative.
End with the next execution command.
```

## Chinese Quick Guide

- 只有一个粗糙想法：先跑 `shape-idea`
- 有很多反馈但不知道值不值得做：先跑 `validate-demand`
- 方向大致确定，需要给 human 和 agent 都能执行的规格：先跑 `agent-prd`
- 要把方向拆成 roadmap 和任务：先跑 `run-roadmap`

## What Good Output Looks Like

A good first run should not give you generic text. It should give you:

- a sharper product direction
- a tighter wedge
- a plausible business model
- a realistic first channel
- a hypothesis set worth testing
- a clearer user or market pain map
- explicit trade-offs
- a concrete next move

If the output still feels vague, use [commands/pm-command-center.md](commands/pm-command-center.md) and route to the shortest tighter loop.
