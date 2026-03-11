# AI OS Security Documentation

This document outlines the security architecture, agent capabilities, and operational boundaries for the Internal AI OS v1 system.

---

## Agent Fleet

### Control Plane Agents (Highest Trust)

| Agent | Key | Role | Runtime | Capabilities |
|-------|-----|------|---------|--------------|
| **Zoe** (CEO) | ceo | CEO | local_control | Primary routing, approvals, delegation, loop closure |
| **Mira** (PM Compiler) | pm_compiler | PM | local_planning | Strategy compilation, TaskEnvelopes, ContextBundles, acceptance criteria |

### Build Agents (High Trust)

| Agent | Key | Role | Runtime | Capabilities |
|-------|-----|------|---------|--------------|
| **Forge** | local_builder | Engineer | local_build | Fast local implementation, bounded verification, runtime fixes |
| **Quill** | local_claude_builder | Engineer | local_build | Repo shaping, docs, cleanup, tests, Claude execution |

### Cloud Control Agents (Elevated Trust)

| Agent | Key | Role | Runtime | Capabilities |
|-------|-----|------|---------|--------------|
| **Chief of Staff** | chief_of_staff | PM | cloud_control | Cloud coordination, escalated planning, operator support |
| **CTO** | cto_core | Engineer | cloud_lead | Architecture, build routing, technical escalation |
| **QA Director** | qa_lead | QA | cloud_lead | Release verification, regressions, quality gates |
| **Research Lead** | research_lead | Researcher | cloud_lead | Evidence collection, competitor scans, signal discovery |
| **Growth Lead** | growth_lead | CMO | cloud_lead | Distribution, funnel, sales, experiment loops |

### Cloud Worker Agents (Bounded Trust)

| Agent | Key | Role | Runtime | Capabilities | Fallback |
|-------|-----|------|---------|--------------|----------|
| **Cloud Build (Atlas)** | cloud_exec_a | Engineer | cloud_worker | Cloud implementation, deployment | local_builder |
| **Cloud QA (Sentinel)** | cloud_verify_b | QA | cloud_worker | Preview checks, smoke tests, release verification | local_claude_builder |
| **Cloud Research (Scout)** | cloud_research_c | Researcher | cloud_worker | Evidence gathering, web research, market scans | pm_compiler |

---

## Paperclip API Endpoints

All agents interact with the Paperclip control plane via REST API. Base URL: `$PAPERCLIP_API_URL/api/`

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/agents/me` | GET | Agent identity and configuration |
| `/companies/{companyId}/issues` | GET | List issues, filter by status, assignee |
| `/issues/{issueId}` | GET | Get issue details with ancestors |
| `/issues/{issueId}/comments` | GET/POST | Read/post comments |
| `/issues/{issueId}/checkout` | POST | Claim ownership of issue |
| `/issues/{issueId}` | PATCH | Update status, assignee, priority |
| `/issues/{issueId}/release` | POST | Release issue ownership |
| `/companies/{companyId}/projects` | POST | Create projects |
| `/projects/{projectId}/workspaces` | POST | Add workspace config |
| `/approvals/{approvalId}` | GET | Review approval requests |
| `/approvals/{approvalId}/issues` | GET | Get approval-linked issues |

### Authentication

- **Local adapters**: Short-lived JWT via `PAPERCLIP_API_KEY` env var
- **Cloud adapters**: Via `OPENCLAW_GATEWAY_*` URL env vars for gateway routing

### Required Headers

```
Authorization: Bearer {api_key}
X-Paperclip-Run-Id: {run_id}  # Required for all mutating operations
```

---

## ops/ Directory Structure

The `ops/` directory is the runtime working area for agent operations. **All dynamic data is git-ignored.**

| Directory | Purpose | Sensitivity |
|-----------|---------|-------------|
| `ops/context_cache/` | Cached Context Hub documents | Medium |
| `ops/context_bundles/` | Compiled TaskEnvelope JSON files | Medium |
| `ops/approvals/pending/` | Awaiting approval | High |
| `ops/approvals/approved/` | Approved items | High |
| `ops/approvals/rejected/` | Rejected items | Medium |
| `ops/discord/outbox/` | Queued Discord notifications | Low |
| `ops/evidence/raw/` | Raw evidence data | Low |
| `ops/evidence/processed/` | Processed evidence | Low |
| `ops/paperclip/outbox/` | Queued Paperclip API calls | Medium |
| `ops/strategy_lab/requests/` | Planning requests | Medium |
| `ops/strategy_lab/reports/` | Generated reports | Low |
| `ops/tasks/compiled/` | Compiled TaskEnvelopes | Medium |
| `ops/memory/*.json` | Agent state memory | High |

---

## Security Boundaries and Trust Zones

### Zone 1: Local Control (Highest Trust)
- **Agents**: Zoe (CEO), Mira (PM Compiler), Forge, Quill
- **Access**: Full read/write to local filesystem, git operations
- **Runtime**: Local process execution
- **Trust Level**: Full local trust

### Zone 2: Cloud Control (Elevated Trust)
- **Agents**: Chief of Staff, CTO, QA Director, Research Lead, Growth Lead
- **Access**: Via OpenClaw gateway, limited local filesystem
- **Runtime**: Remote cloud workers
- **Trust Level**: Gateway-mediated, bounded execution

### Zone 3: Cloud Workers (Bounded Trust)
- **Agents**: Cloud Build, Cloud QA, Cloud Research
- **Access**: Via gateway, task-scoped operations only
- **Runtime**: Ephemeral cloud execution
- **Trust Level**: Minimal local access, work products reviewed before merge

---

## Hardening Checklist

- [x] **Secrets Audit**: No hardcoded API keys (sk-*), passwords, or tokens in codebase
- [x] **Local Config**: `.gitignore` configured with proper exclusions (.env, .env.local, venv, ops/*)
- [x] **Template Config**: `.env.example` exists with placeholder variables only
- [x] **Runtime Isolation**: Each heartbeat includes `X-Paperclip-Run-Id` for audit trail
- [x] **Approval Gates**: Cross-team work requires approval before execution
- [x] **Local-First**: No cloud execution without explicit OpenClaw gateway configuration
