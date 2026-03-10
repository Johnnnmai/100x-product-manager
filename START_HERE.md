# Start Here

If you are new here, think of **100X PM** as a system for multiplying judgment, not just writing faster.

## Fastest Path

1. Open [commands/pm-command-center.md](commands/pm-command-center.md)
2. If all you have is a rough idea, start with [commands/shape-idea.md](commands/shape-idea.md)
3. If you need proof before motion, start with [commands/validate-demand.md](commands/validate-demand.md)
4. If scope is approved and execution needs a spec, start with [commands/agent-prd.md](commands/agent-prd.md)
5. If you are planning work across humans and agents, start with [commands/run-roadmap.md](commands/run-roadmap.md)

## If Your Situation Looks Like This

- “I only have a rough idea.” -> `shape-idea`
- “I have feedback and signals, but I do not know if demand is real.” -> `validate-demand`
- “I need a PRD that an engineer and an agent can both use.” -> `agent-prd`
- “I need to decide what to cut or defer.” -> `prioritize`
- “I need metrics, thresholds, and instrumentation.” -> `define-metrics`
- “I need to test a hypothesis in the market.” -> `design-experiment`
- “I am shipping an AI feature and need evals.” -> `design-eval`
- “I need a roadmap with ownership and tracking.” -> `run-roadmap`
- “I want to turn the work into public content.” -> `make-content`

## Recommended Prompt Pattern

```text
Using commands/<command-name>.md:
1. Follow the command exactly.
2. If ambiguity is high, surface meaningful options before acting.
3. Make assumptions explicit.
4. Produce markdown I can reuse.
5. End with risks, open questions, and the next recommended command.
```

## Chinese Quick Guide

- 只有一个粗糙想法：先跑 `shape-idea`
- 有很多反馈但不知道值不值得做：先跑 `validate-demand`
- 方向大致确定，需要给 human 和 agent 都能执行的规格：先跑 `agent-prd`
- 要把方向拆成 roadmap 和任务：先跑 `run-roadmap`

## What Good Output Looks Like

A good first run should not give you generic text. It should give you:

- a sharper problem statement
- a narrower scope
- explicit trade-offs
- a success metric draft
- a concrete next move

If the output still feels vague, use [commands/pm-command-center.md](commands/pm-command-center.md) and route to the shortest tighter loop.
