# Contributing to 100X PM

This repository is the shared build surface for **100X PM**, an AI Product OS for PMs and founders.

## What Belongs Here

Contribute work that improves one of these layers:

- `Direction`: shape ideas, validate demand, define the right wedge
- `Decision`: specs, trade-offs, metrics, experiments, evals, fallback
- `Delegation`: roadmap orchestration, human/agent split, tracking, reuse

Good contributions usually improve one of:

- a front-door command
- a reusable skill behind a command
- a pack that reduces time-to-value
- examples that show before/after quality
- installation or operating docs

## What Not To Add

- generic prompt dumps
- one-off advice with no reusable pattern
- bloated theory with no operator value
- duplicate commands that fragment the front door
- docs that still market the repo as a loose skill catalog

## Contribution Standard

Every meaningful addition should answer:

1. What user job does this help complete?
2. What output should the user get?
3. What existing command or pack does it strengthen?
4. What failure mode does it prevent?

## Skills

When creating or editing skills:

- keep the name in lowercase kebab-case
- put the main file at `skills/<skill-name>/SKILL.md`
- keep the skill portable across Codex, Claude Code, and similar agents
- prefer explicit output formats and review checklists
- add the next recommended skill when sequencing matters

If the skill is part of the new 100X PM system, prefer metadata that includes:

- `tier`
- `pack`
- `xpm_dimension`
- `xpm_rules`

## Commands

Commands are the public front door.

Do not add new commands casually. Strengthen these first:

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

## GitHub Flow

1. Create a branch for the change.
2. Keep the change scoped.
3. Update linked docs when the public story changes.
4. Verify file paths and references.
5. Open a pull request with:
   - summary
   - why it matters
   - what command, skill, or pack changed
   - any follow-up work still open

## Local Workflow

The public repo slug is `100x-product-manager`.

Use one canonical local repo and worktrees for major initiatives. See [docs/local-repo-workflow.md](docs/local-repo-workflow.md).

## Related Docs

- [README.md](README.md)
- [PRINCIPLES.md](PRINCIPLES.md)
- [MUST_INSTALL.md](MUST_INSTALL.md)
- [PACKS.md](PACKS.md)
- [docs/100x-pm-codex-master-brief.md](docs/100x-pm-codex-master-brief.md)
