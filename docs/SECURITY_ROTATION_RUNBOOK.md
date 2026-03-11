# Security Rotation Runbook

## Why This Exists

The repository previously contained live GitHub and Discord credentials. Phase zero of the AI OS rollout requires those credentials to be rotated and removed before any control-plane integration is considered complete.

## Files Sanitized in This Repo

- `create_org.js`
- `openclaw_discord_config.md`

## Immediate Actions

1. Revoke the previously exposed GitHub token in GitHub settings.
2. Rotate the previously exposed Discord bot token in the Discord developer portal.
3. Update local and cloud runtimes to load new values from environment variables or a secret manager.
4. Do not reintroduce credentials into markdown, scripts, screenshots, or shell history committed to the repo.

## Required Runtime Secrets

- `DISCORD_BOT_TOKEN`
- `DISCORD_CHANNEL_ID`
- `GITHUB_ORG_NAME`
- `GITHUB_BROWSER_PROFILE_DIR`

## Local Setup

```bash
cp .env.example .env
```

Populate `.env` locally, then keep it out of git.

## Cloud Setup

- Tencent Cloud VM or container: inject secrets as environment variables at boot.
- Secret manager preferred: map the secret values into runtime env vars used by the AI OS scripts.
- If OpenClaw and Paperclip run in separate services later, provision separate credentials and scopes.

## Verification

Run both checks before declaring the repository clean:

```bash
python -m ai_os.cli secret-scan
rg -n "gh[pousr]_|[A-Za-z0-9_-]{20,32}\\.[A-Za-z0-9_-]{6,8}\\.[A-Za-z0-9_-]{20,}" -S .
```

Expected result:

- `secret-scan` exits cleanly.
- The ripgrep search returns no live credentials.

## Operational Rule

If a secret ever lands in the repo again, treat it as compromised immediately, rotate it, and only then clean the file history if needed.
