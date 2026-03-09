# 100X Product Managers

Structured PM skills for Claude Code, Codex, and agent-driven product work.

English | 中文

## Why This Repo Exists

Most PM AI outputs fail for the same reason: the model can generate text, but it does not understand the operating system behind strong product work.

This repository packages PM frameworks into reusable skills so the agent can:
- ask better questions before generating artifacts
- move from vague ideas to decision-ready outputs
- keep speed, evidence, and leverage at the center of product work

This repo is especially opinionated about four things:
- Market-driven decisions over internal opinion
- Speed as strategy
- Rapid validation before heavy investment
- AI-shaped PM work, not prompt theater

中文说明：
- 这不是一个“提示词大礼包”，而是一套可复用的 PM 工作技能库。
- 重点不是让 AI 写得更像，而是让 AI 更懂 PM 的判断逻辑、验证逻辑和交付逻辑。
- 核心理念是：市场驱动、快速验证、指数思维、AI 协作。

## What You Get

Current catalog:
- 49 skills total
- 22 component skills
- 20 interactive skills
- 7 workflow skills

High-signal tracks:

| Track | What it helps with | Recommended starting skills |
| --- | --- | --- |
| 100X Core | Market-first prioritization, fast validation, leverage thinking | `market-driven-prioritization`, `rapid-iteration-cycle`, `10x-hypothesis-framework` |
| Discovery & Strategy | Problem framing, positioning, opportunity mapping | `discovery-interview-prep`, `positioning-workshop`, `opportunity-solution-tree`, `product-strategy-session` |
| Delivery & Artifacts | PRDs, roadmaps, user stories, epic breakdown | `prd-development`, `roadmap-planning`, `user-story`, `epic-breakdown-advisor` |
| Business & Growth | SaaS health, pricing, revenue, market sizing | `business-health-diagnostic`, `finance-based-pricing-advisor`, `saas-revenue-growth-metrics`, `tam-sam-som-calculator` |
| AI-Shaped PM Leadership | Context engineering, AI readiness, PM leadership leverage | `context-engineering-advisor`, `ai-shaped-readiness-advisor`, `director-readiness-advisor`, `vp-cpo-readiness-advisor` |

## Start Here

If you only have 15 minutes, start with [START_HERE.md](START_HERE.md).

Suggested first paths:

| Your goal | Start with | Then use |
| --- | --- | --- |
| Pick the right next bet | `market-driven-prioritization` | `rapid-iteration-cycle` |
| Turn messy discovery into a shippable plan | `problem-framing-canvas` | `prd-development` |
| Improve roadmap quality | `prioritization-advisor` | `roadmap-planning` |
| Diagnose a SaaS business | `business-health-diagnostic` | `saas-revenue-growth-metrics` |
| Make your PM team more AI-native | `context-engineering-advisor` | `ai-shaped-readiness-advisor` |

中文建议：
- 如果你想先感受到差异化价值，优先试 `market-driven-prioritization`、`rapid-iteration-cycle`、`business-health-diagnostic`。
- 如果你想直接落地团队协作，优先试 `prd-development`、`user-story`、`roadmap-planning`。
- 如果你在探索“PM + Claude Code”工作流，优先试 `context-engineering-advisor` 和 `ai-shaped-readiness-advisor`。

## How To Use

### Option 1: Use Directly From This Repo

```bash
git clone https://github.com/Johnnnmai/100x-product-managers.git
cd 100x-product-managers
```

Then call a skill by path in your agent:

```text
Using skills/prd-development/SKILL.md, create a PRD for a mobile onboarding redesign. Ask up to 3 clarifying questions first.
```

### Option 2: Install With `skills.sh`

List the skills:

```bash
npx skills add Johnnnmai/100x-product-managers --list
```

Install one for Codex:

```bash
npx skills add Johnnnmai/100x-product-managers --skill prd-development -a codex -g
```

Install one for Claude Code:

```bash
npx skills add Johnnnmai/100x-product-managers --skill market-driven-prioritization -a claude-code -g
```

More detailed platform guides:
- [Using PM Skills with Claude](docs/Using%20PM%20Skills%20with%20Claude.md)
- [Using PM Skills with Codex](docs/Using%20PM%20Skills%20with%20Codex.md)
- [Using PM Skills with ChatGPT](docs/Using%20PM%20Skills%20with%20ChatGPT.md)

## How This Repo Is Positioned

This repo is not trying to be a generic project-management pack.

Our positioning:
- strong on PM judgment, validation, prioritization, and business thinking
- increasingly strong on AI-shaped PM operating systems
- intentionally narrow on generic PMO/admin workflows unless they directly improve product decisions or shipping quality

Practical rule:
- include Claude Code and agent-workflow skills when they help PMs ship better decisions faster
- avoid broad, generic project-management content that dilutes the PM + AI thesis

## Repository Structure

```text
100x-product-managers/
├── skills/                         # All skills
├── docs/                           # Usage guides, launch docs, maintenance notes
├── research/                       # Source material and essays
├── app/                            # Streamlit playground
├── scripts/                        # Packaging, search, validation, and helper scripts
└── START_HERE.md                   # Recommended first-run paths
```

## Quality Bar

Before promotion or release, this repo should always have:
- current install instructions
- working feedback links
- a clear first-skill onboarding path
- metadata-conformant skill files
- no stale repo-owner references in user-facing docs

## Contributing

See:
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [docs/Building PM Skills.md](docs/Building%20PM%20Skills.md)

## License

CC BY-NC-SA 4.0
