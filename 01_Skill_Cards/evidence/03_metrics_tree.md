# Skill Card: Metrics Tree & Counter Metrics

## Definition

Build a hierarchical metrics system where every primary metric has counter metrics to prevent gaming and provide holistic view.

---

## When to Use

- Before launching any feature or product
- When setting OKRs or success metrics
- When single metrics have been gamed before
- For any experiment design

---

## Outputs (Artifacts)

| Artifact | Description | Required? |
|----------|-------------|------------|
| Metrics Tree | Hierarchical metric structure | Yes |
| Primary Metrics | Top-level success metrics | Yes |
| Counter Metrics | Metrics that prevent gaming | Yes |
| Instrumentation Plan | What to track and how | Yes |
| Baseline Data | Current metric values | Yes |

---

## Pass Criteria

- [ ] Every primary metric has at least 2 counter metrics
- [ ] Metrics cover all stages: acquisition → activation → retention → revenue
- [ ] Each metric has clear calculation definition and method
- [ ] Baseline data exists for all key metrics
- [ ] Instrumentation plan covers all required events

---

## Red Flags

- ⚠️ Only one metric used for success
- ⚠️ No counter metrics defined
- ⚠️ Metrics can be easily gamed (e.g., click count without conversion)
- ⚠️ Missing baseline data

---

## Example

**Scenario:** E-commerce checkout optimization

**Primary Metric:** Checkout completion rate

**Counter Metrics:**
- Cart abandonment rate (prevents adding then removing items)
- Time to complete checkout (prevents bot spam)
- Payment failure rate (ensures real purchases)
- Repeat purchase rate (ensures quality, not just one-time)

**Result:** Improved completion rate without gaming

---

## Context Adapter

### Startup Version
- Minimum artifacts: Metrics Tree + Primary Metrics
- Counter metrics: At least 1 per primary metric
- Timeline: 1-2 days
- Baseline: Use proxy data if needed

### Big Tech Version
- Required artifacts: All 5 artifacts
- Counter metrics: 2+ per primary metric
- Cohort and segmentation required
- Timeline: 1-2 weeks

---

## Related Skills

- 01_problem_framing
- 04_experiment_design
- 05_mvp_cutline
