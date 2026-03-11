# Paperclip Operator Guide

## Operating Principle

Paperclip is the company control plane.

The company is no longer modeled as "all local agents plus a few cloud helpers". The core owners are cloud-backed, and local agents are fallback execution lanes.

## 1. Start Paperclip

```bash
npx paperclipai onboard --yes
```

Or:

```bash
npm run paperclip:onboard
```

## 2. Sync Existing Agents

After changing role definitions or prompts:

```bash
python scripts/sync_paperclip_agents.py --company-id <company-id>
```

This patches live Paperclip agents with repo-defined metadata such as:

- `fleet_key`
- `assignment_role`
- `runtime_class`
- `fallback_agent_key`

## 3. Dry-Run The Company Model

Default operator behavior should be inspection first:

```bash
python scripts/provision_company_portfolio.py --company-id <company-id> --dry-run
```

Or:

```bash
npm run paperclip:provision-company
```

The dry-run report shows:

- missing local fallback roles that can be hired
- cloud-backed roles that still require OpenClaw onboarding
- projects and workspaces that would be created
- seeded issue routing by assignment role

Report path:

```text
ops/reports/company-portfolio-provision.json
```

## 4. Apply The Company Model

Only after the dry-run looks right:

```bash
python scripts/provision_company_portfolio.py --company-id <company-id> --auto-approve
```

Or:

```bash
npm run paperclip:apply-company
```

What this does:

1. syncs existing live agents
2. creates missing local fallback roles through governed hire approvals
3. creates projects from `paperclip/company_portfolio.yaml`
4. attaches project workspaces
5. seeds role-based issue trees into Paperclip

What it does not do:

- it does not auto-hire OpenClaw core roles through local CLI
- it reports those as `cloud_onboarding_required`

## 5. Onboard Cloud Core Roles

Core cloud roles are:

- `CEO`
- `Chief of Staff`
- `CTO`
- `QA Director`
- `Research Lead`
- `Growth Lead`

These must be connected through the OpenClaw / Paperclip cloud join path.

Required gateway env vars:

- `OPENCLAW_GATEWAY_CONTROL_URL`
- `OPENCLAW_GATEWAY_BUILD_URL`
- `OPENCLAW_GATEWAY_VERIFY_URL`
- `OPENCLAW_GATEWAY_RESEARCH_URL`

## 6. Seed Local Fallback Credentials

Only local fallback agents need wrapper-based user-scoped env vars:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/seed_paperclip_agent_env.ps1 -CompanyId <company-id>
```

This stores:

- `PAPERCLIP_AGENT_ID_LOCAL_CODEX_BUILDER`
- `PAPERCLIP_AGENT_ID_STAFF_ENGINEER`

Do not commit secrets.

## 7. Validate The Operating Model

```bash
python -m ai_os.cli fleet-check
npx paperclipai company get <company-id> --json
npx paperclipai issue list -C <company-id> --json
```

If you want to test a local fallback lane:

```bash
npm run aios:worker:codex
npm run aios:worker:claude
```

## 8. Expected Result

After rollout, the company should behave like this:

- core routing stays alive even if the laptop is off
- RoomJoy exists as the first real Paperclip project
- issue ownership maps to stable company roles
- local builders are optional fallback, not the operating system
