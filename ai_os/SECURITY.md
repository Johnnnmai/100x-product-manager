# AI OS Security Documentation

## Agent Fleet

| Agent | Role | Capabilities | Trust Level |
|-------|------|--------------|-------------|
| Zoe (CEO) | CTRL-01 | Full control plane access, approval routing, agent hiring | Highest |
| Mira (PM Compiler) | PLAN-01 | Task compilation, planning, ContextBundle creation | High |
| Builder Agents | BUILD-* | Code implementation, testing | Medium |
| Worker Agents | WORK-* | Task execution, evidence collection | Medium |

## Execution Surface

### Paperclip API Endpoints
- Base: `$PAPERCLIP_API_URL/api/`
- Agents: `/agents/me`, `/agents/{id}`
- Issues: `/companies/{companyId}/issues`, `/issues/{issueId}/checkout`
- Projects: `/companies/{companyId}/projects`, `/projects/{id}/workspaces`
- Approvals: `/approvals/{id}`, `/approvals/{id}/issues`

### Local Execution
- Adapter: `claude_local`
- Working directory: `C:\paperclip-work\brand-book`
- Heartbeat interval: 180s (configurable)

## ops/ Directory Structure

| Directory | Purpose | Sensitivity |
|-----------|---------|-------------|
| `ops/context_cache/` | Cached context | Medium |
| `ops/context_bundles/` | Task contexts | Medium |
| `ops/approvals/pending/` | Pending approvals | High |
| `ops/approvals/approved/` | Approved items | High |
| `ops/approvals/rejected/` | Rejected items | Medium |
| `ops/discord/outbox/` | Discord messages | Low |
| `ops/evidence/raw/` | Raw evidence | Low |
| `ops/evidence/processed/` | Processed evidence | Low |
| `ops/paperclip/outbox/` | Paperclip sync | Medium |
| `ops/strategy_lab/requests/` | Strategy requests | Medium |
| `ops/strategy_lab/reports/` | Strategy reports | Low |
| `ops/tasks/compiled/` | Compiled tasks | Medium |

## Security Boundaries

1. **No secrets in repo**: All secrets via `.env` (excluded from git)
2. **API keys via env vars**: `PAPERCLIP_API_KEY`, `PAPERCLIP_API_URL`
3. **Run isolation**: Each heartbeat includes `X-Paperclip-Run-Id`
4. **Approval gates**: Cross-team work requires approval
5. **Local-only execution**: No cloud execution without explicit config
