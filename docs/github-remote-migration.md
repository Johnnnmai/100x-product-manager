# GitHub Remote Migration Record

Migration status as of March 10, 2026:

- mature repo renamed from `Johnnnmai/100x-product-managers`
- canonical repo first moved to `Johnnnmai/100x-pm-skills`
- canonical public repo is now `Johnnnmai/100x-product-manager`
- repo visibility is now `public`
- local `origin` should point to `https://github.com/Johnnnmai/100x-product-manager.git`
- thin repo `Johnnnmai/100x-product-manager-skills` has been archived

## Canonical Remote

```bash
git remote set-url origin https://github.com/Johnnnmai/100x-product-manager.git
git remote -v
```

## Thin Repo Retirement

Useful assets were migrated before retirement:

- `commands/`
- `packs/`
- `brand/`
- `catalog/`
- root docs
- before/after examples

If you want the GitHub account to expose only one repo identity, the next cleanup step is deleting the archived thin repo from the GitHub web UI or API.

## Local Cleanup

After the new canonical local folder is fully verified:

- keep `c:\Users\14153\Documents\个人品牌书籍制作\100x-pm-skills` temporarily or rename it to `100x-product-manager`
- retire the old local `100x-product-managers` folder
