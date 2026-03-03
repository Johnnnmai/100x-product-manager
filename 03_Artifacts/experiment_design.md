# Experiment Design Template

## Experiment Name: [Name]

---

## Hypothesis

**If [change], then [metric] will [increase/decrease] by [X%] because [rationale]**

---

## Variants

| Variant | Description | Traffic % |
|---------|-------------|------------|
| Control | | % |
| Treatment | | % |

---

## Sample Size

| Parameter | Value |
|-----------|-------|
| Baseline conversion | |
| MDE (Minimum Detectable Effect) | |
| Statistical power | |
| Significance level (alpha) | |
| Required sample size | |

---

## Metrics

### Primary Metric

| Metric | Definition | Expected Direction |
|--------|------------|-------------------|
| | | Increase/Decrease |

### Guardrail Metrics

| Metric | Threshold | Alert Action |
|--------|-----------|--------------|
| | | |
| | | |

### Secondary Metrics

| Metric | Definition |
|--------|------------|
| | |

---

## Duration

| Parameter | Value |
|-----------|-------|
| Estimated duration | days |
| Daily traffic | |
| Required days | |

---

## Decision Thresholds

| Outcome | Action |
|---------|--------|
| Primary metric lift > X% with p < 0.05 | Ship |
| Primary metric lift < X% or p >= 0.05 | Don't ship |
| Guardrail metric degrades > Y% | Rollback |

---

## Stop Conditions

- [ ] Guardrail metric exceeds threshold
- [ ] Catastrophic bug
- [ ] Technical issue

---

## Ramp Plan

| Phase | Percentage | Duration |
|-------|------------|----------|
| 1 | 1% | 1 day |
| 2 | 5% | 1 day |
| 3 | 20% | 2 days |
| 4 | 50% | 2 days |
| 5 | 100% | - |
