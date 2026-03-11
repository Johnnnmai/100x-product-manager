---
name: simulation-analyst
description: Use when you need to analyze simulation results from MiroFish/OASIS, synthesizing raw data into data-backed product recommendations with confidence levels.
type: component
tier: advanced
pack: ai-prediction
best_for:
  - analyzing persona simulation results
  - generating data-backed recommendations
  - identifying risks and opportunities from simulation
  - synthesizing signals + simulation into insights
outputs:
  - key findings summary
  - hypothesis validation results
  - data-backed recommendations
  - confidence levels
xpm_dimension:
  - strategy
  - evidence
xpm_rules:
  - evidence_beats_opinion
  - define_success_before_shipping
  - make_tradeoffs_explicit
---

## Purpose

Analyze raw simulation results from MiroFish/OASIS and combine with market signals to produce data-backed product recommendations. This skill transforms complex simulation outputs into actionable insights with clear confidence levels.

This skill is essential because simulations are thinking tools, not prediction engines. The analyst's job is to interpret results with appropriate skepticism and translate them into product decisions.

## Key Concepts

### Simulation vs Prediction

| Simulation | Prediction |
|------------|-----------|
| Explore possible futures | Forecast one future |
| Identifies patterns | Assigns probabilities |
| Multiple scenarios | Single outcome |
| Decision support | Crystal ball (fallacy) |

### Confidence Calibration

Always report confidence levels honestly:

- **High Confidence (80%+)**: Strong signal from multiple sources, validated by simulation
- **Medium Confidence (60-80%)**: Some signal, mixed simulation results
- **Low Confidence (40-60%)**: Weak signal, inconsistent simulation
- **Very Low (<40%)**: No clear signal, highly uncertain

### Signal + Simulation Synthesis

The best insights come from combining:

1. **Web Signals**: What users actually say (reviews, social, forums)
2. **Persona Reactions**: How simulated personas respond
3. **Scenario Analysis**: Best/worst/base case outcomes
4. **Competitive Context**: What alternatives exist

## Application

### When to Use

- After running MiroFish/OASIS simulations
- When combining multiple data sources
- When preparing recommendations for stakeholders
- When validating product directions

### Input Requirements

```
Simulation Results:
- Raw persona reaction data
- Scenario outcomes
- Behavioral patterns observed

Market Signals (from signal-harvester-enhanced):
- Structured signal summary
- Sentiment analysis
- Key themes

Product Context:
- Original hypothesis
- Target market
- Success criteria
```

### Analysis Framework

#### Step 1: Pattern Detection

Look for:
- Consistent reactions across personas
- Divergent reactions (adversarial validation)
- Unexpected behaviors
- Edge cases that emerged

#### Step 2: Signal Integration

Map simulation results to signals:
- Do simulations confirm or contradict signals?
- Where do they align? Diverge?
- What explains discrepancies?

#### Step 3: Hypothesis Testing

For each hypothesis:
- Support: Persona reactions + signals
- Refute: Persona reactions + signals
- Inconclusive: Mixed results

#### Step 4: Recommendation Generation

Translate findings to recommendations:
- Lead with evidence
- Include confidence level
- Acknowledge limitations
- Define next actions

### Output Structure

```
# Simulation Analysis Report

## Executive Summary
[2-3 sentence recommendation with overall confidence]

## Hypothesis Validation

### Hypothesis 1: [Original hypothesis]
**Status**: [SUPPORTED / REFUTED / INCONCLUSIVE]
**Confidence**: [X]%
**Evidence**:
- Signal evidence: [Description]
- Simulation evidence: [Description]

### Hypothesis 2: ...

## Persona Reaction Analysis

### Key Patterns Identified
1. Pattern 1: [Description] - [X]% of personas
2. Pattern 2: [Description] - [X]% of personas

### Unexpected Findings
- Finding 1: [Description]
- Finding 2: [Description]

## Risk Assessment

### High Priority Risks
1. Risk 1: [Description]
   - Likelihood: [X]%
   - Impact: [High/Medium/Low]
   - Mitigation: [Description]

### Medium Priority Risks
...

## Data-Backed Recommendations

1. **Recommendation 1** (Confidence: X%)
   - Evidence: [Summary]
   - Next Action: [Description]

2. **Recommendation 2** (Confidence: Y%)
   - Evidence: [Summary]
   - Next Action: [Description]

## Confidence Summary
- Overall confidence: [X]%
- Based on:
  - Signal strength: [Strong/Medium/Weak]
  - Simulation consistency: [High/Medium/Low]
  - Sample diversity: [High/Medium/Low]

## Limitations
- [Limitation 1]
- [Limitation 2]

## Next Steps
- [Action 1]
- [Action 2]
```

## Examples

### Example 1: B2B SaaS Product

```
Analysis of: AI Customer Support for SMBs

Hypothesis Validation:
- H1: "SMBs want AI support to reduce costs"
  - Status: SUPPORTED
  - Confidence: 75%
  - Evidence: 68% positive sentiment + 72% of personas would try

- H2: "Price is the main barrier"
  - Status: SUPPORTED
  - Confidence: 80%
  - Evidence: Price mentioned in 34% of negative reviews + 3/5 personas price-sensitive

- H3: "Implementation complexity is a concern"
  - Status: INCONCLUSIVE
  - Confidence: 55%
  - Evidence: Mixed signals + personas split evenly

Recommendations:
1. LEAD with cost savings messaging (75% confidence)
   - Next: A/B test pricing pages

2. ADDRESS implementation concerns in onboarding (55% confidence)
   - Next: Create simplified setup wizard

3. DON'T lead with "AI" - lead with "support automation" (80% confidence)
   - Next: Update marketing copy
```

### Example 2: Consumer App

```
Analysis of: Habit Tracking with Social Features

Hypothesis Validation:
- H1: "Users want social features"
  - Status: INCONCLUSIVE
  - Confidence: 50%
  - Evidence: Reddit divided + personas split 50/50

- H2: "Privacy concerns will limit adoption"
  - Status: SUPPORTED
  - Confidence: 72%
  - Evidence: Privacy mentioned in 19% of negative reviews + 2 personas strongly negative

Recommendations:
1. MAKE SOCIAL OPTIONAL (72% confidence)
   - Evidence: Privacy concerns validated
   - Next: Default to private, make sharing a choice

2. TEST social features with small group first (50% confidence)
   - Evidence: Inconclusive response
   - Next: Run cohort test before full launch

3. DON'T launch with aggressive social sharing (80% confidence)
   - Evidence: Strong negative reactions from privacy-focused personas
   - Next: Gentle prompts only
```

## Common Pitfalls

### Pitfall 1: Over-interpreting Noise
**Symptom**: Treating random variation as meaningful.

**Consequence**: False confidence in recommendations.

**Fix**: Focus on consistent patterns across personas, not individual reactions.

### Pitfall 2: Ignoring Contradictions
**Symptom**: Highlighting supporting evidence, ignoring refuting.

**Consequence**: Biased recommendations.

**Fix**: Report both supporting and refuting evidence. Be balanced.

### Pitfall 3: False Precision
**Symptom**: "73.4% of users prefer X"

**Consimulation**: Fake accuracy.

**Fix**: Use ranges and confidence intervals. "Approximately 70-80%"

### Pitfall 4: Simulation as Truth
**Symptom**: Treating simulation as prediction.

**Consequence**: Overconfident decisions.

**Fix**: Always include limitations section. Simulation is a tool, not truth.

### Pitfall 5: Analysis Paralysis
**Symptom**: Collecting more data without acting.

**Consequence**: Analysis never ends.

**Fix**: Set decision thresholds. "If confidence > 70%, proceed."

## References

### Related Skills
- `skills/product-direction-validation/SKILL.md` — Full validation workflow
- `skills/signal-harvester-enhanced/SKILL.md` — Signal collection
- `skills/persona-simulation-builder/SKILL.md` — Persona building

### External Resources
- [MiroFish](https://github.com/666ghj/MiroFish) — Prediction platform
- [OASIS](https://github.com/camel-ai/oasis) — Simulation engine

### Analytical Frameworks
- Bayesian reasoning for confidence calibration
- Scenario planning methodologies
- Decision analysis frameworks
