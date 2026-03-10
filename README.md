# 100X PM

**AI Product OS for PMs and Founders**

Turn rough ideas into compelling, scoped, shippable product direction.

- Shape rough ideas into wedges, scope, and first moves
- Validate whether demand is real with evidence, not noise
- Write specs for both humans and agents
- Define metrics, experiments, evals, fallback, and guardrails
- Turn roadmaps into delegated human and agent execution

中文一句话：
**100X PM 不是让 AI 更会写，而是让 PM 和 founder 更快把模糊问题收敛成可落地的判断与执行。**

## Start Here

- [START_HERE.md](START_HERE.md)
- [MUST_INSTALL.md](MUST_INSTALL.md)
- [PACKS.md](PACKS.md)
- [PRINCIPLES.md](PRINCIPLES.md)
- [INSTALL.md](INSTALL.md)

## What Is 100X PM?

100X PM is not about doing 100x more work.

It means becoming the kind of PM or founder who can:

- frame the right problem before drafting solutions
- make explicit trade-offs instead of hiding behind process
- define success with evidence, metrics, guardrails, and time windows
- design AI behavior through prompts, evals, fallback logic, and constraints
- ship the smallest viable test when execution cost is lower than more internal debate
- use systems, workflows, and leverage to create outsized outcomes

中文理解：

- 先定义问题，再给方案
- 先讲取舍，再讲功能
- 先定义成功，再开始执行
- 不只是使用 AI，而是定义 AI 的行为
- 当执行成本低于继续空想的成本，就更快落地去验证

**100X PM is not faster typing. It is sharper judgment, faster convergence, and stronger leverage.**

## What Do You Need To Do Today?

- Rough idea, weak instinct, no clear wedge yet: [shape-idea](commands/shape-idea.md)
- Need to know if demand is real: [validate-demand](commands/validate-demand.md)
- Need a spec that humans and agents can execute: [agent-prd](commands/agent-prd.md)
- Need to decide what to do now vs later: [prioritize](commands/prioritize.md)
- Need success metrics and thresholds: [define-metrics](commands/define-metrics.md)
- Need a test design, not just an opinion: [design-experiment](commands/design-experiment.md)
- Shipping an AI feature and need evals: [design-eval](commands/design-eval.md)
- Need to turn a direction into delegated execution: [run-roadmap](commands/run-roadmap.md)
- Need to turn work into distribution: [make-content](commands/make-content.md)
- Not sure where to start: [pm-command-center](commands/pm-command-center.md)

## 10 Must-Install Commands

1. `pm-command-center`: route the job, stage, and shortest next workflow
2. `shape-idea`: go from rough idea to wedge, scope, risk, and next move
3. `validate-demand`: turn comments, notes, tickets, and URLs into evidence-backed demand judgment
4. `agent-prd`: produce a PRD that works for both human review and agent execution
5. `prioritize`: force explicit trade-offs and what to defer
6. `define-metrics`: define success metrics, counter metrics, thresholds, and windows
7. `design-experiment`: turn a hypothesis into a real experiment plan
8. `design-eval`: define pass/fail criteria, test cases, fallback, and review triggers
9. `run-roadmap`: split a direction into milestones, ownership, and tracking rules
10. `make-content`: convert product work into reusable public content

Full details live in [MUST_INSTALL.md](MUST_INSTALL.md).

## Core Capabilities

### Direction

- rough idea to problem framing
- target user hypothesis
- first wedge
- scope down
- evidence-backed demand judgment

### Decision

- dual-mode PRDs for humans and agents
- explicit trade-offs
- metrics and thresholds
- experiments
- AI evals, fallback, and guardrails

### Delegation

- roadmap themes and milestones
- human vs agent work split
- task contracts
- tracking cadence
- reuse and content packaging

## Proof Of Value

We are not going to invent benchmark numbers for the homepage.

Proof should come from public artifacts, a documented test plan, and raw runs other people can inspect.

| Proof layer | What it compares | Status |
| --- | --- | --- |
| Before/after artifacts | same input, plain output vs command-guided output | live |
| Blind-scored benchmark | baseline vs 100X PM across canonical PM tasks | planned |
| Real workflow metrics | time to acceptable draft, edit burden, reuse | planned |

Current proof:

- [PRD before/after](examples/before-after/prd-before-after.md)
- [Prioritization before/after](examples/before-after/prioritization-before-after.md)
- [AI eval before/after](examples/before-after/eval-before-after.md)
- [Public value test plan](docs/value-test-plan.md)

Benchmark templates:

- [Scorecard template](examples/value-tests/scorecard-template.md)
- [Task run template](examples/value-tests/task-run-template.md)

## Packs

This repo is organized around practical packs, not a random skill supermarket.

- [Direction & Discovery](PACKS.md#direction--discovery)
- [Demand & Insights](PACKS.md#demand--insights)
- [PRD & Scope](PACKS.md#prd--scope)
- [Metrics & Experiments](PACKS.md#metrics--experiments)
- [AI PM & Evals](PACKS.md#ai-pm--evals)
- [Roadmaps & Delegation](PACKS.md#roadmaps--delegation)
- [Career & Interviews](PACKS.md#career--interviews)
- [Content & Distribution](PACKS.md#content--distribution)

## Integrations

Supported as optional layers, not mandatory runtime dependencies:

- `Scrapling`: web evidence ingestion and market signal collection
- `Context Hub`: curated external context and versioned knowledge
- `claude-mem`: working memory and context compression
- `Paperclip`: optional orchestration layer for business goals and agent assignment
- `OASIS` and `MiroFish`: optional strategy lab for simulation, not default day-to-day PM execution

## Install

Clone the final canonical repo:

```bash
git clone https://github.com/Johnnnmai/100x-pm-skills.git
cd 100x-pm-skills
```

If the GitHub rename has not been completed yet, the local implementation still lives on top of the mature `100x-product-managers` history. See [INSTALL.md](INSTALL.md) and [docs/local-repo-workflow.md](docs/local-repo-workflow.md).

Platform guides:

- [docs/Using PM Skills with Claude.md](docs/Using%20PM%20Skills%20with%20Claude.md)
- [docs/Using PM Skills with Codex.md](docs/Using%20PM%20Skills%20with%20Codex.md)
- [docs/Using PM Skills with ChatGPT.md](docs/Using%20PM%20Skills%20with%20ChatGPT.md)

## Why This Is Different

Most PM + AI repos stop at “write better prompts.”

100X PM is built around a stronger claim:

- average PM work gets stuck in ambiguity, weak prioritization, noisy demand, and unclear success
- top PM work is nonlinear because it converges faster, wastes less work, and turns decisions into operating systems
- AI is useful when it helps shape direction, define behavior, and split execution, not when it only drafts text

If you want the short version:

**This repo is not a PM skills library. It is an AI Product OS for turning idea -> evidence -> scope -> spec -> metrics -> eval -> roadmap -> delegated execution.**

## License

CC BY-NC-SA 4.0
