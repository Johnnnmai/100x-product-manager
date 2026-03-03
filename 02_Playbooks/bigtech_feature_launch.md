# Playbook: Big Tech Feature Launch

## When to Use

- Launching a new feature in a large organization
- Multiple teams involved
- High reliability requirements

## Duration

**4-8 weeks**

## Required Skills

| Order | Skill Card | Artifacts | Duration |
|-------|------------|-----------|----------|
| 1 | 01_problem_framing | Problem Statement, Outcome Spec, Segment Definition | 1-2 weeks |
| 2 | 03_metrics_tree | Metrics Tree, Counter Metrics, Baseline Data | 1 week |
| 3 | 04_experiment_design | Experiment Design, Power Analysis | 1 week |
| 4 | 06_edge_cases | Edge Cases, NFR Checklist | 1 week |
| 5 | 08_launch_readiness | Launch Checklist, Operational Readiness | 1 week |
| 6 | 09_rollout_rollback | Rollout Plan, Kill Switch | 1-2 days |
| 7 | 10_threat_model | Threat Model, Mitigations | 1 week |
| 8 | 11_stakeholder_map | Stakeholder Map, Decision Owners | 2-3 days |
| 9 | 12_exec_narrative | One-Pager, FAQ | 2-3 days |

## Optional Skills

| Skill Card | When to Use |
|------------|-------------|
| 02_service_blueprint | If complex user journey |
| 05_mvp_cutline | If scope unclear |
| 07_milestone_plan | If complex dependencies |

## Execution Flow

```
Week 1-2: Discovery & Alignment
├── Problem Framing
│   ├── User research
│   ├── Data analysis
│   └── Segment definition
│
├── Stakeholder Map
│   ├── Identify all parties
│   ├── Decision rights
│   └── Escalation path
│
└── Exec Narrative
    ├── One-pager
    └── Get buy-in

Week 3-4: Design & Planning
├── Metrics Tree
│   ├── Primary + counter metrics
│   ├── Instrumentation
│   └── Baseline
│
├── Experiment Design
│   ├── Hypothesis
│   ├── Sample size
│   └── Guardrails
│
└── Edge Cases
    ├── 20+ edge cases
    └── NFR requirements

Week 5-6: Build & Prepare
├── Threat Model
│   ├── Security review
│   └── Compliance
│
├── Launch Readiness
│   ├── Checklist
│   ├── Operational readiness
│   └── Staging sign-off
│
└── Rollout Plan
    ├── Phased rollout
    ├── Kill switch
    └── Rollback triggers

Week 7-8: Launch & Measure
├── Experiment launch
├── Monitoring
└── Iteration
```

## Success Criteria

- [ ] All required approvals obtained
- [ ] Security review passed
- [ ] Experiment launched
- [ ] Monitoring operational
- [ ] Rollback tested
- [ ] Support team briefed

## Key Principles

1. **Process compliance**: Follow org standards
2. **Cross-team alignment**: Get buy-in early
3. **Full instrumentation**: Data-driven decisions
4. **Risk mitigation**: Prepare for failure

## Common Mistakes to Avoid

- ⚠️ Skipping stakeholder alignment
- ⚠️ Incomplete instrumentation
- ⚠️ No rollback tested
- ⚠️ Launching without guardrails
- ⚠️ Ignoring NFRs
