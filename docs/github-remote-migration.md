# GitHub Remote Migration Checklist

Use this once GitHub authentication is fixed.

## 1. Re-authenticate

```bash
gh auth login
gh auth status
```

## 2. Rename The Mature Repo

Keep this repo history and rename it:

```bash
gh repo rename -R Johnnnmai/100x-product-managers 100x-pm-skills --yes
```

## 3. Verify Redirect And New Slug

```bash
gh repo view Johnnnmai/100x-pm-skills
gh repo view Johnnnmai/100x-product-managers
```

The old slug should redirect.

## 4. Freeze The Thin Repo

Before deleting `Johnnnmai/100x-product-manager-skills`, verify that the useful assets were migrated locally:

- `commands/`
- `packs/`
- `brand/`
- `catalog/`
- root docs
- before/after examples

## 5. Archive Or Delete The Thin Repo

If you want a short safety window:

```bash
gh repo archive Johnnnmai/100x-product-manager-skills --yes
```

Then delete from the GitHub web UI after final verification.

## 6. Update Local Origin

In the canonical local repo:

```bash
git remote set-url origin https://github.com/Johnnnmai/100x-pm-skills.git
git remote -v
```

## 7. Retire The Old Local Folder

After the renamed remote is verified and the new local folder is your active workspace, the old `100x-product-managers` local folder can be deleted.
