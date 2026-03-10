# Local Repo Workflow

## Goal

Keep one canonical local repo for 100X PM.

## Canonical Setup

- local folder name: `100x-pm-skills`
- keep one long-lived local checkout only
- keep `main` clean
- use one worktree per major initiative

## Keep / Retire

- Keep the mature repo history now served from `100x-pm-skills`
- Retire `100x-product-manager-skills`

## Local Migration Rule

1. keep `100x-pm-skills` as the only long-lived local repo
2. treat the old `100x-product-managers` local folder as temporary archive only
3. delete the old local folder once the new canonical clone is fully verified

## Worktree Pattern

Recommended structure:

```text
c:\Users\14153\Documents\个人品牌书籍制作\
  100x-pm-skills\
  100x-pm-skills-feature-readme\
  100x-pm-skills-feature-agent-prd\
```

## Branch Hygiene

- one major initiative per branch
- do not use duplicate local folders as pseudo-branches
- tag or archive important historical states instead of copying folders

## Current Remote Reality

The canonical public slug is `100x-pm-skills`.
