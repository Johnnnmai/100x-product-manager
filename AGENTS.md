# 100X PM Repository Rules

This repository is the canonical implementation of **100X PM**: an AI Product OS for PMs and founders.

## Product Direction

- Brand name: `100X PM`
- Target repo slug: `100x-product-manager`
- Hero subtitle: `AI Product OS for PMs and Founders`
- Core promise: rough idea -> evidence -> scope -> agent-readable spec -> metrics -> eval -> roadmap -> delegated execution

## Working Model

Use this repo as a system, not a prompt dump.

- Commands are the front door.
- Skills are the execution layer behind commands.
- Packs are grouped operating paths, not random categories.
- Documentation should optimize for first-run usefulness, not internal completeness.

## Front-Door Priority

When editing public docs, keep these commands as the main entrypoints:

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

Do not reintroduce a "must-install skills" front door that fights this model.

## 100X PM Operating Rules

1. Define the problem before proposing the solution.
2. Use evidence, not noise, to validate demand.
3. Define success before shipping.
4. Make trade-offs explicit.
5. AI PM is not prompt writing; it includes evals, fallback, guardrails, and behavior design.
6. If execution cost is lower than thinking cost, ship the smallest viable test.
7. Aggressive iteration beats polished hesitation.
8. Leverage beats effort.
9. PRDs should increasingly be readable by both humans and agents.
10. The best PMs create non-linear outcomes, not just better documents.

## Agent Behavior In This Repo

When adding or editing commands, skills, or docs:

- Prefer autonomous-first exploration for rough ideas.
- If ambiguity is high, enumerate meaningful options before taking action.
- Before irreversible action, require a choice or make the chosen assumption explicit.
- Do not present simulated insight as validated truth.
- After review, reflection, or error discovery, capture the learning in repo docs or process notes when the lesson is reusable.

## PRD Standard

Command and skill outputs for specs should default to dual-mode artifacts:

- human-readable summary
- agent-readable task spec
- constraints and dependencies
- success metrics
- fallback or escalation rules
- required context
- output expectations

## Skill Standard

Skills should stay concise, portable, and composable.

- Folder name: lowercase kebab-case
- Main file: `skills/<skill-name>/SKILL.md`
- Prefer compact frontmatter and explicit output formats
- Include concrete anti-patterns or failure modes
- Reference the next skill when sequencing matters

If you add a new skill for the 100X PM system, prefer metadata that includes:

- `name`
- `title`
- `type`
- `tier`
- `pack`
- `brand_mode`
- `public_safe`
- `best_for`
- `outputs`
- `xpm_dimension`
- `xpm_rules`

## Documentation Standard

Public docs should answer three questions quickly:

1. What is 100X PM?
2. What should I run first?
3. What concrete output will I get?

Avoid stale counts, vague marketplace language, and mismatched headlines.

## Local Repo Management

- Keep one canonical local repo.
- Keep `main` clean.
- Use one worktree per major initiative.
- Do not keep long-lived duplicate local folders for old and new states.
- The public repo is `100x-product-manager`; local folder cleanup can happen separately.

See [docs/local-repo-workflow.md](docs/local-repo-workflow.md).
