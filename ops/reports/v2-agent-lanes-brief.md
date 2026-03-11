# v2 Agent Lanes Operator Brief

**Date:** 2026-03-10
**Prepared by:** Mira (PLAN-01 / PM Compiler)
**Context:** JMS-2 - Review repo updates for v2 operating model

---

## Overview

The v2 agent operating model establishes a structured control plane above the existing GitHub → OpenClaw execution path, with distinct agent lanes for different task types.

## Agent Fleet

| Lane | Callsign | Role | Runtime | Status |
|------|----------|------|---------|--------|
| `CTRL-01` | `Zoe` | Orchestrator & delegation owner | Local Claude | Active |
| `PLAN-01` | `Mira` | PM compiler & context router | Local Claude | Active |
| `BUILD-01` | `Forge` | Local Codex implementation | Local Codex | Active |
| `BUILD-02` | `Quill` | Local Claude implementation | Local Claude | Active |
| `CLOUD-BUILD-01` | `Atlas` | Heavy cloud build | Tencent OpenClaw | Pending config |
| `CLOUD-VERIFY-01` | `Sentinel` | Validation & smoke checks | Tencent OpenClaw | Pending config |
| `CLOUD-RESEARCH-01` | `Scout` | External research | Tencent OpenClaw | Pending config |

## Routing Model

### Local Lanes (Low Latency)
- **Zoe (CEO)**: Routes work, owns delegation and loop closure
- **Mira (PM)**: Compiles intent into bounded tasks, defines acceptance criteria
- **Forge (Codex)**: Fast local implementation with bounded verification
- **Quill (Claude)**: Repo shaping, cleanup, bounded Claude execution

### Cloud Lanes (Heavy Work)
- **Atlas**: Heavy build loops, longer-running tasks
- **Sentinel**: Preview, smoke tests, validation checks
- **Scout**: External research, evidence gathering

## Identity Model

Each agent has a dedicated wrapper command:
- `paperclip/bin/zoe-paperclip.cmd`
- `paperclip/bin/mira-paperclip.cmd`
- `paperclip/bin/forge-paperclip.cmd`
- `paperclip/bin/quill-paperclip.cmd`

Each reads from dedicated env vars:
- `PAPERCLIP_AGENT_ID_<NAME>` / `PAPERCLIP_AGENT_KEY_<NAME>`

## Execution Flow

1. PM intent → bounded TaskEnvelope + ContextBundle
2. Same task written to `ops/tasks/pending/` (legacy) + `ops/paperclip/outbox/` (tracking)
3. Zoe routes by lane
4. Mira tightens scope and acceptance
5. Forge/Quill handle local work
6. Atlas/Sentinel/Scout handle cloud work
7. Every lane: repo evidence → comment → update issue status

## Key Contracts

- **ContextBundle**: Bounded execution context
- **TaskEnvelope**: Worker contract
- **PaperclipRunRequest**: Outbox payload
- **DiscordEvent**: Approval/notification payload

## Source of Truth

- Fleet spec: `paperclip/agent_fleet.yaml`
- Prompts: `paperclip/bootstrap/*.md`
- Sync tool: `scripts/sync_paperclip_agents.py`
- Env seeding: `scripts/seed_paperclip_agent_env.ps1`

## Current Limits

- Cloud lanes require: `OPENCLAW_GATEWAY_BUILD_URL`, `OPENCLAW_GATEWAY_VERIFY_URL`, `OPENCLAW_GATEWAY_RESEARCH_URL`
- On-demand heartbeat mode (no daemon)
- Discord = notification transport only, not system of record
