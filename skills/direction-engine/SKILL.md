---
name: direction-engine
description: Use when you need continuous direction calibration for PM Agent, including hypothesis tracking, assumption drift detection, and evidence-based pivots.
type: workflow
tier: advanced
pack: ai-prediction
best_for:
  - ongoing direction validation and calibration
  - tracking hypothesis evolution over time
  - detecting when assumptions have drifted
outputs:
  - hypothesis tracking dashboard
  - assumption drift alerts
  - pivot recommendations
xpm_dimension:
  - strategy
  - discovery
xpm_rules:
  - evidence_beats_opinion
  - speed_is_strategy
---

## Purpose

Implement continuous direction calibration for PM Agent to track hypotheses, detect assumption drift, and trigger evidence-based pivots. This skill ensures product directions remain validated over time, not just at creation.

This is not about sticking to a plan. It is about having the discipline to change direction when evidence warrants.

## Key Concepts

### Hypothesis Tracking

Every product direction is based on hypotheses:
1. **Problem hypothesis** — Is this a real problem?
2. **Solution hypothesis** — Will this solve the problem?
3. **Business hypothesis** — Is this viable?
4. **Assumptions** — What must be true for this to work?

Track each hypothesis with:
- Initial confidence level
- Evidence collected
- Current confidence level
- Last validated date

### Assumption Drift Detection

Assumptions drift when:
- **Market conditions change** — Competitors, regulations, trends
- **User behavior shifts** — New data contradicts assumptions
- **Technical feasibility evolves** — New capabilities or constraints
- **Business context updates** — Resources, priorities, strategy

**Drift Indicators:**
- Conflicting evidence accumulates
- Key metrics diverge from predictions
- Stakeholder concerns increase
- New information challenges old assumptions

### Evidence-Based Pivots

A pivot is a significant direction change based on evidence. Types:
- **Problem pivot** — Different problem to solve
- **Solution pivot** — Different way to solve it
- **Business model pivot** — Different monetization
- **Zoom pivot** — Scale up or down

## Application

Use this skill when:
1. Running long-term product initiatives
2. Validating directions at regular intervals
3. Deciding whether to persist or pivot
4. Building evidence for strategic decisions

### Input Requirements

- Current product direction
- Initial hypotheses
- Key metrics to track
- Validation cadence

### Output Structure

```
Direction Calibration Dashboard:

Hypothesis Tracking:
| Hypothesis | Initial Confidence | Evidence | Current Confidence | Last Validated |
|------------|---------------------|----------|--------------------| ---------------|
| ...        | ...                 | ...      | ...                | ...            |

Assumption Drift:
| Assumption | Status | Drift Indicator | Severity |
|------------|--------|-----------------|----------|
| ...        | ...    | ...             | ...      |

Pivot Decision:
- [Current recommendation]
- [Supporting evidence]
- [Recommended actions]
```

## Examples

### Example 1: Feature Development

```
Initial Direction: Build mobile app for Gen Z users

Hypothesis Tracking:
| Hypothesis | Initial | Evidence | Current | Last Validated |
|------------|---------|----------|---------|----------------|
| Gen Z wants this | 70% | User interviews | 85% | 2 weeks ago |
| Mobile-first is right | 80% | Usage data | 60% | 1 month ago |
| Can acquire users | 60% | Ad tests | 40% | 1 week ago |

Assumption Drift:
| Assumption | Status | Indicator | Severity |
|------------|--------|-----------|----------|
| Gen Z mobile usage | DRIFTING | New data shows desktop preference | HIGH |
| Acquisition channels | STABLE | Tests ongoing | LOW |

Pivot Recommendation:
- Evidence: Acquisition hypothesis weakening
- Recommendation: Test desktop before investing in mobile
- Action: Run desktop MVP test in parallel
```

### Example 2: Market Expansion

```
Initial Direction: Expand to European market

Hypothesis Tracking:
| Hypothesis | Initial | Evidence | Current | Last Validated |
|------------|---------|----------|---------|----------------|
| Market size sufficient | 75% | Analyst reports | 70% | 1 month ago |
| Can comply with GDPR | 90% | Legal review | 90% | 2 weeks ago |
| Localization needed | 60% | User feedback | 80% | 1 week ago |

Assumption Drift:
| Assumption | Status | Indicator | Severity |
|------------|--------|-----------|----------|
| GDPR compliance | STABLE | Legal approved | LOW |
| Localization scope | DRIFTING | User feedback shows more needed | MEDIUM |

Pivot Recommendation:
- Evidence: Localization needs greater than expected
- Recommendation: Expand localization scope before launch
- Action: Add language support for 3 more markets
```

## Common Pitfalls

### Pitfall 1: No Tracking
**Symptom:** Direction set at start, never revisited.

**Consequence:** Stale assumptions guide decisions.

**Fix:** Regular calibration cadence. Track every assumption.

### Pitfall 2: Ignoring Drift
**Symptom:** Seeing drift indicators but not acting.

**Consequence:** Major pivots become harder.

**Fix:** Define drift thresholds. Trigger review when exceeded.

### Pitfall 3: Pivot Aversion
**Symptom:** Ignoring evidence that suggests pivot.

**Consequence:** Pursuing failing direction.

**Fix:** Normalize pivots. "Pivot" is not "failure."

### Pitfall 4: Over-Pivoting
**Symptom:** Changing direction at every piece of evidence.

**Consequence:** No momentum, no learning.

**Fix:** Require threshold of evidence before pivoting.

## References

### Related Skills
- `skills/product-direction-simulator/SKILL.md` — Direction simulation
- `skills/10x-hypothesis-framework/SKILL.md` — Hypothesis framework
- `skills/evidence-collector/SKILL.md` — Evidence collection

### External Resources
- "The Lean Startup" — Validated learning
- "Running Lean" — Hypothesis testing
- "The Hard Thing About Hard Things" — When to pivot
