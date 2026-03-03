# Playbook: Regulated Platform Change

## When to Use

- Financial products
- Security/Infrastructure products
- Healthcare/Legal compliance required
- Audit trail necessary

## Duration

**8-12 weeks**

## Required Skills

| Order | Skill Card | Artifacts | Duration |
|-------|------------|-----------|----------|
| 1 | 01_problem_framing | Problem Statement, Outcome Spec, Compliance Requirements | 1-2 weeks |
| 2 | 02_service_blueprint | Service Blueprint, SLA, Ownership | 1 week |
| 3 | 03_metrics_tree | Metrics Tree, Counter Metrics, Compliance Metrics | 1 week |
| 4 | 06_edge_cases | Edge Cases, NFR Checklist, Compliance Checklist | 1-2 weeks |
| 5 | 10_threat_model | Threat Model, Abuse Cases, Logging Requirements | 1-2 weeks |
| 6 | 08_launch_readiness | Launch Checklist, Compliance Sign-off, Audit Readiness | 1-2 weeks |
| 7 | 09_rollout_rollback | Rollout Plan, Rollback, Kill Switch | 1 week |
| 8 | 11_stakeholder_map | Stakeholder Map, Compliance Owners, Audit Contacts | 1 week |
| 9 | 12_exec_narrative | One-Pager, Risk Assessment, Compliance Summary | 1 week |

## Extra Artifacts Required

| Artifact | Description |
|----------|-------------|
| Compliance Checklist | Regulatory requirements mapping |
| Audit Logging Spec | What must be logged and for how long |
| Data Retention Policy | How long data must be kept |
| Incident Response Plan | How to handle compliance incidents |

## Execution Flow

```
Week 1-2: Discovery & Compliance Assessment
├── Problem Framing
│   ├── Business problem
│   ├── Compliance requirements
│   └── Regulatory constraints
│
└── Stakeholder Map
    ├── Compliance team
    ├── Legal
    ├── Security
    └── Audit

Week 3-4: Architecture & Compliance Design
├── Service Blueprint
│   ├── User journey
│   ├── Handoffs
│   └── SLA definitions
│
├── Threat Model
│   ├── Security review
│   ├── Data protection
│   └── Abuse prevention
│
└── Compliance Mapping
    ├── Requirements list
    ├── Gap analysis
    └── Mitigation plan

Week 5-6: Metrics & Logging Design
├── Metrics Tree
│   ├── Business metrics
│   ├── Compliance metrics
│   └── Audit metrics
│
└── Audit Logging
    ├── What to log
    ├── Retention period
    └── Access controls

Week 7-8: Edge Cases & Controls
├── Edge Cases
│   ├── Compliance edge cases
│   ├── Error handling
│   └── Data validation
│
└── Compliance Checklist
    ├── Pre-launch verification
    └── Documentation

Week 9-10: Launch Preparation
├── Launch Readiness
│   ├── Full checklist
│   ├── Compliance sign-off
│   └── Audit prep
│
├── Rollout Plan
│   ├── Phased rollout
│   └── Monitoring
│
└── Incident Response
    ├── Escalation path
    └── Communication plan

Week 11-12: Launch & Audit
├── Execute rollout
├── Monitoring
└── Documentation
```

## Success Criteria

- [ ] Compliance review passed
- [ ] Legal sign-off obtained
- [ ] Security review passed
- [ ] Audit logging operational
- [ ] Incident response tested
- [ ] Full documentation complete

## Key Principles

1. **Compliance first**: Don't even start without understanding requirements
2. **Document everything**: Audit trail is critical
3. **Defense in depth**: Multiple layers of protection
4. **Audit ready**: Can prove compliance at any time

## Common Mistakes to Avoid

- ⚠️ Starting without compliance assessment
- ⚠️ Insufficient audit logging
- ⚠️ No incident response plan
- ⚠️ Skipping compliance sign-off
- ⚠️ Incomplete documentation
