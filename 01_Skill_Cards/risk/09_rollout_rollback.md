# Skill Card: Rollout & Rollback Plan

## Definition

Define how the feature will be released (gradual rollout) and how to quickly revert if issues occur.

---

## When to Use

- Before any production release
- For features with significant user impact
- When rollback speed matters

---

## Outputs (Artifacts)

| Artifact | Description | Required? |
|----------|-------------|------------|
| Rollout Plan | Phased rollout percentages | Yes |
| Rollback Triggers | Clear conditions to rollback | Yes |
| Rollback Procedure | Step-by-step rollback steps | Yes |
| Kill Switch | Quick disable mechanism | Conditional |
| Monitoring Setup | What to watch | Yes |

---

## Pass Criteria

- [ ] Rollout phases defined with percentages
- [ ] Rollback triggers are specific and measurable
- [ ] Rollback procedure documented and tested
- [ ] Kill switch mechanism exists (if applicable)
- [ ] Monitoring covers key health metrics

---

## Red Flags

- ⚠️ No gradual rollout (100% from start)
- ⚠️ Rollback triggers vague ("if major issues")
- ⚠️ Rollback procedure not documented
- ⚠️ No monitoring during rollout
- ⚠️ Rollback would take >1 hour

---

## Example

**Scenario:** New recommendation algorithm

**Rollout:**
- 1%: Internal + employees
- 5%: Beta users
- 20%: Random 20%
- 50%: Random 50%
- 100%: Full rollout

**Rollback Triggers:**
- Error rate > 1%
- Latency p99 > 2s
- Critical bug

**Result:** Issue at 20%, rolled back in 15 minutes

---

## Context Adapter

### Startup Version
- Minimum artifacts: Rollout Plan + Rollback Triggers
- Timeline: 1 day
- Approach: User segment rollout acceptable

### Big Tech Version
- Required artifacts: All 5 artifacts
- Timeline: 1 week
- Approach: Geographic + cohort + platform required

---

## Related Skills

- 04_experiment_design
- 08_launch_readiness
- 10_threat_model
