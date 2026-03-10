# Local Repo Workflow

## Goal

Keep one canonical local repo for 100X PM.

## Canonical Setup

- local folder name: `100x-pm-skills`
- keep one long-lived local checkout only
- keep `main` clean
- use one worktree per major initiative

## Keep / Retire

- Keep the mature repo history from `100x-product-managers`
- Retire `100x-product-manager-skills` after useful assets are migrated

## Local Migration Rule

If the remote rename is not done yet:

1. keep the mature remote as the source of truth
2. use `100x-pm-skills` as the local folder name anyway
3. treat the old local folder as temporary archive only

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

The target public slug is `100x-pm-skills`.
Until the GitHub rename is completed, the mature history may still be served from `100x-product-managers`.
