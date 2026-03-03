# Skill Card: Experiment Design (A/B or Quasi-experiment)

## Definition

Design a rigorous experiment that can definitively answer whether a change works, with clear decision thresholds.

---

## When to Use

- Before launching any new feature
- When comparing two or more solutions
- When data-driven decision is required
- When sample size permits statistical validity

---

## Outputs (Artifacts)

| Artifact | Description | Required? |
|----------|-------------|------------|
| Experiment Design | Treatment/control setup | Yes |
| Sample Size Calculation | Power analysis | Conditional |
| Decision Thresholds | MDE, significance level | Yes |
| Guardrail Metrics | Metrics that must not degrade | Yes |
| Stop Conditions | When to abort early | Yes |
| Ramp Plan | How to roll out | Yes |

---

## Pass Criteria

- [ ] Clear hypothesis stated in "If X then Y because Z" format
- [ ] Sample size calculated (or rationale for alternative approach)
- [ ] Primary metric and guardrail metrics defined
- [ ] Decision thresholds defined (p-value, MDE)
- [ ] Stop conditions documented

---

## Red Flags

- ⚠️ No clear hypothesis
- ⚠️ Sample size not calculated
- ⚠️ No guardrail metrics
- ⚠️ Decision threshold not defined before experiment
- ⚠️ "Peeking" allowed (checking results before completion)

---

## Example

**Scenario:** Testing new onboarding flow

**Hypothesis:** "If we simplify onboarding from 5 steps to 2, then activation rate will increase 10% because fewer steps reduce drop-off"

**Design:**
- 50/50 split, 2 weeks
- Primary: Day-7 activation rate
- Guardrails: Day-1 retention, support tickets
- MDE: 10%, p < 0.05
- Stop: If guardrails degrade >5%

**Result:** Activated with 15% lift, guardrails stable

---

## Context Adapter

### Startup Version
- Minimum artifacts: Hypothesis + Decision Thresholds + Guardrails
- Alternative: Use sequential testing or quasi-experiment if sample limited
- Timeline: 1-2 days
- Document biases explicitly

### Big Tech Version
- Required artifacts: All 6 artifacts
- Power analysis required
- Full statistical review
- Timeline: 1-2 weeks

---

## Related Skills

- 03_metrics_tree
- 09_rollout_rollback
- 08_launch_readiness
