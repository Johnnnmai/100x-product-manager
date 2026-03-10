<p align="center">
  <img src="assets/readme-hero.svg" alt="100X PM" width="100%">
</p>

# 100X PM

<p align="center"><strong>AI Product OS for PMs and Founders</strong></p>
<p align="center">Turn rough ideas into scoped direction, agent-readable specs, evals, and delegated execution.</p>

<p align="center">
  <img alt="Public repo" src="https://img.shields.io/badge/repo-public-111827?style=flat-square">
  <img alt="10 commands" src="https://img.shields.io/badge/commands-10-111827?style=flat-square">
  <img alt="Pilot benchmark" src="https://img.shields.io/badge/pilot%20benchmark-4%20tasks-111827?style=flat-square">
  <img alt="License" src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-111827?style=flat-square">
</p>

> 100X PM is not about writing faster. It is about reducing ambiguity, forcing trade-offs, and getting to shippable product judgment faster.

中文一句话：  
**100X PM 不是让 AI 更会写，而是让 PM 和 founder 更快把模糊问题收敛成可落地的判断与执行。**

## Start Here

- [START_HERE.md](START_HERE.md)
- [INSTALL.md](INSTALL.md)
- [MUST_INSTALL.md](MUST_INSTALL.md)
- [PACKS.md](PACKS.md)
- [PRINCIPLES.md](PRINCIPLES.md)

## What You Can Do Today

| If your situation looks like this | Run this | Expected output |
| --- | --- | --- |
| I only have a rough idea | [shape-idea](commands/shape-idea.md) | 2-3 scoped directions, a recommended wedge, risks, and first move |
| I need to know if demand is real | [validate-demand](commands/validate-demand.md) | evidence-backed demand memo |
| I need a spec humans and agents can execute | [agent-prd](commands/agent-prd.md) | dual-mode PRD with constraints and review rules |
| I need to decide what wins now vs later | [prioritize](commands/prioritize.md) | ranked decision with explicit trade-offs |
| I am shipping an AI feature | [design-eval](commands/design-eval.md) | pass/fail logic, red flags, fallback, and review triggers |
| I need to turn direction into execution | [run-roadmap](commands/run-roadmap.md) | milestones, ownership, dependencies, and tracking cadence |
| I do not know where to start | [pm-command-center](commands/pm-command-center.md) | routed next command and shortest path |

## Install In 2 Minutes

```bash
git clone https://github.com/Johnnnmai/100x-product-manager.git
cd 100x-product-manager
```

Use one of these prompt patterns:

```text
Using commands/shape-idea.md:
Run the command exactly.
Make assumptions explicit.
Give me 2-3 scoped options, recommend one, and end with the next command.
```

Platform guides:

- [Using 100X PM with Claude](docs/Using%20PM%20Skills%20with%20Claude.md)
- [Using 100X PM with Codex](docs/Using%20PM%20Skills%20with%20Codex.md)
- [Using 100X PM with ChatGPT](docs/Using%20PM%20Skills%20with%20ChatGPT.md)

## 10 Public Commands

1. `pm-command-center`
2. `shape-idea`
3. `validate-demand`
4. `agent-prd`
5. `prioritize`
6. `define-metrics`
7. `design-experiment`
8. `design-eval`
9. `run-roadmap`
10. `make-content`

Full details live in [MUST_INSTALL.md](MUST_INSTALL.md).

## Why This Repo Exists

Most PM + AI repos stop at "write better prompts."

100X PM is built around a stronger claim:

- average PM work gets stuck in ambiguity, weak prioritization, noisy demand, and unclear success
- top PM work is nonlinear because it converges faster, wastes less work, and turns decisions into operating systems
- AI matters when it shapes direction, defines behavior, and splits execution, not when it only drafts text

If you want the short version:

**This is not a loose prompt library. It is a public operating system for turning idea -> evidence -> scope -> spec -> metrics -> eval -> roadmap -> delegated execution.**

## Proof Of Value

We are not publishing invented homepage metrics. We are publishing inspectable artifacts.

### Live proof layers

| Proof layer | What it compares | Status |
| --- | --- | --- |
| Before/after artifacts | same input, plain prompt vs command-guided output | live |
| Pilot benchmark wave 1 | same-model baseline vs 100X PM on 4 canonical tasks | live |
| Blind-scored benchmark | reviewer-blinded scoring across canonical tasks | planned |

### Before / after examples

- [PRD before/after](examples/before-after/prd-before-after.md)
- [Prioritization before/after](examples/before-after/prioritization-before-after.md)
- [AI eval before/after](examples/before-after/eval-before-after.md)

### Pilot benchmark wave 1

Wave 1 is a same-model, single-operator pilot. It is public because the raw prompts, outputs, and scorecards are in the repo. It is not yet blinded.

| Task | Baseline avg | 100X PM avg | Delta | Time to acceptable draft | Summary |
| --- | --- | --- | --- | --- | --- |
| `shape-idea` | 2.3/5 | 4.1/5 | +1.8 | 18 min -> 10 min | [run](examples/value-tests/runs/2026-03-10-shape-idea-summary.md) |
| `agent-prd` | 2.9/5 | 4.4/5 | +1.5 | 25 min -> 14 min | [run](examples/value-tests/runs/2026-03-10-agent-prd-summary.md) |
| `prioritize` | 3.0/5 | 4.3/5 | +1.3 | 16 min -> 9 min | [run](examples/value-tests/runs/2026-03-10-prioritize-summary.md) |
| `design-eval` | 2.1/5 | 4.4/5 | +2.3 | 20 min -> 11 min | [run](examples/value-tests/runs/2026-03-10-design-eval-summary.md) |

Full benchmark package:

- [Value test plan](docs/value-test-plan.md)
- [Wave 1 summary](examples/value-tests/runs/2026-03-10-wave-1-summary.md)
- [Scorecard template](examples/value-tests/scorecard-template.md)
- [Task run template](examples/value-tests/task-run-template.md)

## Repo Layout

- `commands/`: the public front door
- `skills/`: the reusable execution layer behind commands
- `packs/`: grouped operating paths for common PM jobs
- `examples/`: before/after artifacts and benchmark runs
- `docs/`: setup, usage, and operating guidance
- `app/`: Streamlit beta playground

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

## Optional Integrations

Supported as optional layers, not mandatory runtime dependencies:

- `Scrapling`: web evidence ingestion and market signal collection
- `Context Hub`: curated external context and versioned knowledge
- `claude-mem`: working memory and context compression
- `Paperclip`: optional orchestration layer for business goals and agent assignment
- `OASIS` and `MiroFish`: optional strategy lab for simulation, not default day-to-day execution

## License

CC BY-NC-SA 4.0
