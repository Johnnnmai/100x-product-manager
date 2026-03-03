# Skill Card: Launch Readiness Review (LRR)

## Definition

Verify all launch requirements are met before releasing to users, including operational readiness.

---

## When to Use

- Before any feature or product launch
- Before any significant change to production
- When launch gates are required

---

## Outputs (Artifacts)

| Artifact | Description | Required? |
|----------|-------------|------------|
| Launch Checklist | Comprehensive launch checklist | Yes |
| Operational Readiness | Monitoring, rollbacks, support | Yes |
| Staging Sign-off | Staging verification | Yes |
| Go/No-Go Decision | Final decision document | Yes |
| Rollback Plan | How to revert if needed | Yes |

---

## Pass Criteria

- [ ] All checklist items marked "Pass"
- [ ] Monitoring dashboards operational
- [ ] Rollback tested in staging
- [ ] Support team briefed
- [ ] All stakeholders have given sign-off

---

## Red Flags

- ⚠️ Checklist incomplete
- ⚠️ Rollback not tested
- ⚠️ Monitoring not set up
- ⚠️ Support team not briefed
- ⚠️ Last-minute additions to launch

---

## Example

**Scenario:** Launching new checkout flow

**Launch Checklist:**
- [x] Code review complete
- [x] All tests passing
- [x] Performance within SLA
- [x] Security review passed
- [x] Monitoring dashboards live
- [x] Rollback tested
- [x] Support FAQ updated

---

## Context Adapter

### Startup Version
- Minimum artifacts: Launch Checklist + Rollback Plan
- Timeline: 1 day
- Focus: Core functionality + monitoring

### Big Tech Version
- Required artifacts: All 5 artifacts
- Timeline: 1 week
- Full LRR with multi-team sign-offs

---

## Related Skills

- 04_experiment_design
- 09_rollout_rollback
- 10_threat_model
