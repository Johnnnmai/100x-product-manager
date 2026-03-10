# Install 100X PM

## Canonical Identity

- Public brand: `100X PM`
- Target repo slug: `100x-pm-skills`
- Subtitle: `AI Product OS for PMs and Founders`

## Clone

Preferred final form:

```bash
git clone https://github.com/Johnnnmai/100x-pm-skills.git
cd 100x-pm-skills
```

If the GitHub rename is not completed yet, clone the mature source repo and keep the local folder named `100x-pm-skills`:

```bash
git clone https://github.com/Johnnnmai/100x-product-managers.git 100x-pm-skills
cd 100x-pm-skills
```

## Use It As A Command System

Start with one of these files:

- `commands/pm-command-center.md`
- `commands/shape-idea.md`
- `commands/validate-demand.md`
- `commands/agent-prd.md`
- `commands/run-roadmap.md`

Prompt pattern:

```text
Using commands/shape-idea.md:
Run the command exactly.
Make assumptions explicit.
Give me 2-3 scoped options, recommend one, and show the next best action.
```

## Platforms

- Claude Code: [docs/Using PM Skills with Claude.md](docs/Using%20PM%20Skills%20with%20Claude.md)
- Codex: [docs/Using PM Skills with Codex.md](docs/Using%20PM%20Skills%20with%20Codex.md)
- ChatGPT: [docs/Using PM Skills with ChatGPT.md](docs/Using%20PM%20Skills%20with%20ChatGPT.md)

## Local Workflow

- one canonical local repo
- clean `main`
- one worktree per major initiative
- no duplicate long-lived local copies

See [docs/local-repo-workflow.md](docs/local-repo-workflow.md).
