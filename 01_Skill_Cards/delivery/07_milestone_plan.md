# Skill Card: Milestone Plan & Critical Path

## Definition

Create a time-bound execution plan with clear milestones, dependencies, and acceptance criteria for each phase.

---

## When to Use

- Before starting any significant effort
- When multiple teams are involved
- When timeline is fixed
- When dependencies are complex

---

## Outputs (Artifacts)

| Artifact | Description | Required? |
|----------|-------------|------------|
| Milestone Plan | Time-bound phases with dates | Yes |
| Critical Path | Longest dependency chain | Yes |
| Dependency Map | What depends on what | Yes |
| Buffer Allocation | Risk buffers identified | Yes |
| Demo Criteria | What gets shown at each milestone | Yes |

---

## Pass Criteria

- [ ] Each milestone has clear acceptance criteria
- [ ] Critical path identified with buffer
- [ ] All dependencies mapped with owners
- [ ] Demo criteria defined for each milestone
- [ ] Timeline accounts for review/approval cycles

---

## Red Flags

- ⚠️ No clear milestones
- ⚠️ Dependencies not mapped
- ⚠️ No buffer for risks
- ⚠️ Demo criteria unclear
- ⚠️ Timeline doesn't account for reviews

---

## Example

**Scenario:** Building a new mobile feature

**Milestones:**
- Week 1: API ready (acceptance: contracts defined, stubbed)
- Week 2: Beta UI ready (acceptance: internal testing)
- Week 3: Integration complete (acceptance: E2E tests pass)
- Week 4: Launch ready (acceptance: App Store approved)

**Critical Path:** API → Integration → Launch

---

## Context Adapter

### Startup Version
- Minimum artifacts: Milestone Plan + Critical Path
- Timeline: 1 day
- Granularity: Weekly milestones OK

### Big Tech Version
- Required artifacts: All 5 artifacts
- Timeline: 1 week
- Granularity: Daily or bi-weekly
- Cross-team dependencies with owners + SLAs

---

## Related Skills

- 05_mvp_cutline
- 08_launch_readiness
- 11_stakeholder_map
