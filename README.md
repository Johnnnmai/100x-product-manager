# 100X PM Skills / 100X 产品经理技能体系

**52 battle-tested PM skills** for Claude Code, Codex, ChatGPT, and agentic product work.

This repo is for PMs who want more than prompt templates.

- Structured PM skills, not one-off prompts
- Fast entry points, not prompt archaeology
- Stronger judgment, not just nicer wording
- A practical 100X PM lens after the install path is clear

Supported paths:
- `Claude Code`
- `Codex`
- `ChatGPT + GitHub / Projects / custom GPTs`
- `skills.sh`
- `Streamlit (beta)` local playground

## Updates & Announcements

- **2026-03-09:** [GitHub Refresh + XHS Launch Asset Set](docs/announcements/2026-03-09-github-refresh-xhs-launch.md)
- **Announcement index:** [docs/announcements/README.md](docs/announcements/README.md)

## Why This Exists

Most AI PM work breaks in the same place:

The model can produce text, but it does not reliably understand PM judgment, trade-offs, sequencing, or validation logic.

This repo packages repeatable product frameworks into reusable skills so the agent can:
- ask sharper questions before drafting
- turn fuzzy inputs into decision-ready outputs
- connect discovery, strategy, execution, and business thinking
- help PMs work in more agentic, AI-shaped ways

中文说明：
- 这不是“提示词大全”，而是一套可安装、可复用、可组合的 PM skills。
- 重点不是让 AI 更会写，而是让 AI 更像一个懂 PM 逻辑、验证逻辑、商业逻辑的工作伙伴。
- GitHub 首页优先解决“我现在能怎么用”，100X PM 方法论放在后面做差异化。

## What You Get

Current catalog:
- **52 skills total**
- **22 component skills**
- **22 interactive skills**
- **8 workflow skills**

High-signal categories:

| Category | What it helps with | Example skills |
| --- | --- | --- |
| PM Job Hunt | Resume positioning, mock interviews, role selection | `pm-resume-teardown`, `pm-mock-interview-workflow`, `bigtech-vs-startup-decision-advisor` |
| Discovery & Validation | Customer interviews, problem framing, opportunity mapping | `discovery-interview-prep`, `problem-framing-canvas`, `opportunity-solution-tree` |
| Delivery & Artifacts | PRDs, roadmaps, stories, epic framing | `prd-development`, `roadmap-planning`, `user-story`, `epic-breakdown-advisor` |
| Growth & Finance | Business health, pricing, SaaS metrics, market sizing | `business-health-diagnostic`, `finance-based-pricing-advisor`, `acquisition-channel-advisor`, `tam-sam-som-calculator` |
| AI-Shaped PM | Context engineering, agent orchestration, org readiness | `context-engineering-advisor`, `ai-shaped-readiness-advisor`, `pol-probe-advisor`, `skill-authoring-workflow` |

## Start Here

If you only have 10-15 minutes, start with [START_HERE.md](START_HERE.md).

### Starter Packs

| Starter pack | Best for | Start with | Then use |
| --- | --- | --- | --- |
| **PM Job Hunt** | PM 求职、面试准备、职业选择 | `pm-resume-teardown` | `pm-mock-interview-workflow`, `bigtech-vs-startup-decision-advisor` |
| **Discovery & Validation** | 把模糊问题变成可验证的 PM 判断 | `discovery-interview-prep` | `problem-framing-canvas`, `opportunity-solution-tree` |
| **Growth & Finance** | 看清业务健康度、定价和增长问题 | `business-health-diagnostic` | `finance-based-pricing-advisor`, `acquisition-channel-advisor` |
| **AI-Shaped PM** | 让 PM 工作从“会写字”升级到“会跑系统” | `ai-shaped-readiness-advisor` | `context-engineering-advisor`, `pol-probe-advisor` |

Recommended first-skill prompts:

```text
Using skills/pm-resume-teardown/SKILL.md, pressure-test my PM resume for senior PM roles. Ask clarifying questions first, then show the highest-impact fixes.
```

```text
Use skills/discovery-interview-prep/SKILL.md to prepare 6 churn interviews for mid-market B2B customers. Give me a sharp question guide and the mistakes to avoid.
```

```text
Use skills/business-health-diagnostic/SKILL.md to assess our SaaS business health. Show red flags, what matters most, and what to do next.
```

```text
Use skills/ai-shaped-readiness-advisor/SKILL.md to assess whether my PM org is just using AI tools or actually redesigning work around AI.
```

## Featured Skills

If you are deciding what to try first, these are the strongest front-door skills right now:

- `pm-resume-teardown` - Diagnose why a PM resume will or will not convert, then rewrite the highest-value bullets
- `pm-mock-interview-workflow` - Run a full interview prep loop: target role, story inventory, mock questions, debrief, 7-day practice plan
- `discovery-interview-prep` - Turn messy research goals into a focused interview plan with the right method
- `business-health-diagnostic` - Connect growth, retention, unit economics, and capital efficiency instead of staring at one metric
- `finance-based-pricing-advisor` - Evaluate pricing changes with revenue, churn, conversion, and payback trade-offs
- `ai-shaped-readiness-advisor` - Separate AI theater from real operating-model change

## How To Use

### Option 1: Use Skills Directly From This Repo

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
npx skills add Johnnnmai/100x-product-managers --skill pm-resume-teardown -a codex -g
```

Install one for Claude Code:

```bash
npx skills add Johnnnmai/100x-product-managers --skill discovery-interview-prep -a claude-code -g
```

Platform guides:
- [Using PM Skills with Claude](docs/Using%20PM%20Skills%20with%20Claude.md)
- [Using PM Skills with Codex](docs/Using%20PM%20Skills%20with%20Codex.md)
- [Using PM Skills with ChatGPT](docs/Using%20PM%20Skills%20with%20ChatGPT.md)
- [PM Skills Playground (beta)](app/STREAMLIT_INTERFACE.md)

## Why 100X PM

This repo is positioned as a practical PM skills marketplace first, but it is not generic.

The differentiator is the **100X PM** lens:
- market-driven decisions over internal opinion
- speed as strategy, not just execution hygiene
- validation before heavy investment
- leverage systems over isolated heroic work
- AI-shaped PM operating models over prompt theater

### 10X vs 100X

| Concept | Focus | Description |
| --- | --- | --- |
| **10X PM** | Personal efficiency | The PM works faster |
| **100X PM** | Organizational leverage | The team makes better decisions faster with more reusable systems |

### The 6 MECE Decision Categories

| Category | Core question | Failure mode |
| --- | --- | --- |
| **Outcome** | What result should users get? | Building something useless |
| **Evidence** | How do we know this works? | Blind optimization |
| **Solution** | What do we build or not build? | Endless rework |
| **Delivery** | How do we ship without drift? | Delay and confusion |
| **Risk** | How do we fail safely? | Bad launches with no rollback |
| **Alignment** | Who decides, who blocks, who needs context? | Internal drag |

## Repository Structure

```text
100x-product-managers/
├── skills/                         # Skill folders, each with SKILL.md
├── docs/                           # Usage guides, launch copy, maintenance notes
├── research/                       # Source material and essays
├── app/                            # Streamlit playground
├── scripts/                        # Packaging, search, validation, helper scripts
└── START_HERE.md                   # Fast first-run paths
```

## Quality Bar

Before promotion or release, this repo should always have:
- current install instructions
- working feedback links
- a clear first-skill onboarding path
- metadata-conformant skill files
- no stale repo-owner references in active user-facing docs

## Contributing

See:
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [docs/Building PM Skills.md](docs/Building%20PM%20Skills.md)

## License

CC BY-NC-SA 4.0
