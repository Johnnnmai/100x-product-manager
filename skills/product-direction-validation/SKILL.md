---
name: product-direction-validation
description: Use when you need end-to-end validation of a product direction using web signals and persona-driven simulation, providing data-backed recommendations before committing resources.
type: workflow
tier: advanced
pack: ai-prediction
best_for:
  - validating product ideas with real-world signals
  - testing user reactions before building
  - data-backed product decisions
  - reducing risk through simulation
outputs:
  - validated product hypothesis
  - market signal summary
  - persona reaction simulations
  - data-backed recommendations
xpm_dimension:
  - strategy
  - discovery
  - evidence
xpm_rules:
  - evidence_beats_opinion
  - speed_is_strategy
  - define_success_before_shipping
---

## Purpose

End-to-end product direction validation that combines web signal collection with persona-driven simulation to provide data-backed product recommendations. This is NOT about predicting the future with certainty — it is about reducing uncertainty before committing significant resources.

Use this skill when:
- You have a product idea but uncertain about market reception
- You want to stress-test assumptions with diverse user personas
- You need data to support your product decision
- You want to identify blind spots before building

## Key Concepts

### The Validation Pipeline

```
[Product Idea] → [Signal Collection] → [Persona Building] → [Simulation] → [Analysis] → [Recommendation]
```

1. **Signal Collection**: Use Scrapling to gather real-world opinions, reviews, discussions about similar products/features
2. **Persona Building**: Create simulation-ready user profiles based on target market
3. **Simulation**: Run MiroFish/OASIS to model persona reactions
4. **Analysis**: Synthesize signals + simulation into actionable recommendations

### Why Validate Before Building

- **Reduce waste**: Catch bad ideas early, before investment
- **Build conviction**: Strengthen good ideas with evidence
- **Identify objections**: Preempt stakeholder concerns
- **Plan mitigations**: Prepare for predictable challenges

### Data-Backed vs Opinion-Based

| Opinion-Based | Data-Backed |
|--------------|-------------|
| "I think users want X" | "Users on Reddit/Twitter express X as a pain point" |
| "This will be popular" | "Simulation shows 73% positive reception among target personas" |
| "No competitor does this" | "3 competitors identified, 2 in adjacent spaces" |

## Application

### When to Use

- Before committing to a new product direction
- Before significant resource allocation
- When stakeholder alignment is needed
- When you want to stress-test your assumptions

### Input Requirements

```
Product Direction:
- What are you building?
- Who is it for?
- What problem does it solve?

Target Market:
- Industry/market segment
- Competitors
- Market size (if known)

Success Criteria:
- What does success look like?
- What metrics matter?

Constraints:
- Budget/timeline
- Technical limitations
```

### The Validation Workflow

#### Phase 1: Signal Collection (1-2 hours)
- Run `signal-harvester-enhanced` to gather web signals
- Focus on: reviews, discussions, complaints, requests
- Output: Structured signal summary

#### Phase 2: Persona Building (30 min)
- Run `persona-simulation-builder` with signal inputs
- Create 4-6 diverse personas
- Output: JSON persona profiles

#### Phase 3: Simulation (2-4 hours)
- Run MiroFish simulation with personas
- Test reactions to product direction
- Output: Raw simulation data

#### Phase 4: Analysis (1 hour)
- Run `simulation-analyst` on simulation results
- Combine with signal inputs
- Output: Final recommendations

### Output Structure

```
# Product Direction Validation Report

## Executive Summary
[2-3 sentence recommendation]

## Signal Summary
- Key themes from web research
- Sentiment analysis
- Top opportunities identified

## Persona Reactions
- Persona 1: [Reaction + Confidence]
- Persona 2: [Reaction + Confidence]
- ...

## Simulation Results
- Scenario outcomes
- Risk factors identified
- Opportunities identified

## Data-Backed Recommendations
1. [Recommendation with evidence]
2. [Recommendation with evidence]
3. [Recommendation with evidence]

## Confidence Level
- Overall: X%
- Based on: [factors]

## Next Steps
- [Action 1]
- [Action 2]
```

## Examples

### Example 1: B2B SaaS Product

```
Input:
- Product: AI-powered customer support for SMBs
- Target: Small businesses (5-50 employees)
- Problem: Support costs too high

Signal Collection Results:
- G2/Capterra: 127 reviews mentioning "AI support" - 68% positive
- Reddit r/smallbusiness: 34 threads about support automation - mixed sentiment
- Twitter: 89 tweets about AI customer service - excitement + skepticism

Persona Reactions:
- SMB Owner: Positive (cost savings) - 80% confidence
- Support Manager: Cautious (implementation effort) - 75% confidence
- Technical User: Positive (customization) - 70% confidence

Simulation Results:
- 72% would try
- 45% would pay
- Top concern: Implementation complexity

Recommendation:
- PROCEED with caution
- Lead with "reduce support tickets" not "AI"
- Provide free trial + onboarding support
- Confidence: 75%
```

### Example 2: Consumer App

```
Input:
- Product: Habit tracking app with social features
- Target: Gen Z (18-25)
- Problem: Existing apps too solitary

Signal Collection Results:
- App Store reviews: 89% want "social features"
- Twitter: 234 posts about gamification - high engagement
- Reddit r/productivity: 67 threads about habit apps - privacy concerns

Persona Reactions:
- Social Learner: Very positive - 85% confidence
- Privacy Conscious: Negative - 70% confidence
- Gamification Lover: Positive - 80% confidence

Recommendation:
- PROCEED with privacy-first approach
- Make social features optional
- Lead with personal tracking, social as secondary
- Confidence: 72%
```

## Common Pitfalls

### Pitfall 1: Cherry-Picking Signals
**Symptom**: Only looking at signals that support your direction.

**Consequence**: Biased validation, missed risks.

**Fix**: Actively seek contradictory signals. Use adversarial personas.

### Pitfall 2: Too Many Personas
**Symptom**: Creating 10+ personas, analysis paralysis.

**Consequence**: No clear insights, wasted time.

**Fix**: Limit to 4-6 diverse personas. Focus on decision-relevant diversity.

### Pitfall 3: Ignoring Low-Confidence Results
**Symptom**: Dismissing simulation results that contradict your opinion.

**Consequence**: Overconfidence, missed warnings.

**Fix**: Report confidence levels honestly. "Don't know" is a valid answer.

### Pitfall 4: One-Time Exercise
**Symptom**: Validating once at the start, never updating.

**Consequence**: Missing market changes.

**Fix**: Re-validate at key milestones. Markets evolve.

### Pitfall 5: Simulation as Truth
**Symptom**: Treating simulation as prediction of real behavior.

**Consequence**: False confidence.

**Fix**: Simulation is a thinking tool, not a crystal ball. Use with other evidence.

## References

### Related Skills
- `skills/signal-harvester-enhanced/SKILL.md` — Enhanced web signal collection
- `skills/persona-simulation-builder/SKILL.md` — Build simulation personas
- `skills/simulation-analyst/SKILL.md` — Analyze simulation results
- `skills/direction-engine/SKILL.md` — Continuous direction calibration

### External Resources
- [MiroFish](https://github.com/666ghj/MiroFish) — Digital twin prediction platform
- [OASIS](https://github.com/camel-ai/oasis) — Large-scale agent simulation
- [Scrapling](https://github.com/D4Vinci/Scrapling) — Adaptive web scraping

### Prerequisites
- Claude Code or similar LLM with skill execution capability
- Scrapling installed for signal collection
- MiroFish/OASIS for simulation (or use skill without for manual approach)
