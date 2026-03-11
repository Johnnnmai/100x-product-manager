---
name: product-direction-simulator
description: Use when you need to simulate product direction outcomes using persona-driven simulation, or when validating strategic decisions before committing resources.
type: workflow
tier: advanced
pack: ai-prediction
best_for:
  - simulating product direction outcomes
  - validating strategic decisions before committing
  - stress-testing assumptions with diverse personas
outputs:
  - scenario simulations
  - risk identification
  - decision recommendations
xpm_dimension:
  - strategy
  - discovery
xpm_rules:
  - evidence_beats_opinion
  - speed_is_strategy
---

## Purpose

Simulate product direction outcomes using persona-driven simulation to validate strategic decisions before committing significant resources. This skill helps PMs stress-test their assumptions, identify blind spots, and make better-informed strategic choices.

This is not about predicting the future. It is about exploring possible futures to make better decisions today.

## Key Concepts

### Persona-Driven Simulation

Based on Oasis/MiroFish research, persona-driven simulation involves:
1. **Define stakeholder personas** — Create diverse perspectives that will react to your direction
2. **Simulate reactions** — Model how each persona would respond to your product direction
3. **Identify patterns** — Find common concerns and opportunities across personas
4. **Stress-test assumptions** — Challenge your thesis with adversarial thinking

### Why Simulate Product Directions

- **Validate before committing** — Test ideas before investing resources
- **Identify blind spots** — Discover issues you hadn't considered
- **Build conviction** — Strengthen your direction with evidence
- **Prepare for objections** — Anticipate stakeholder concerns

### Simulation Scenarios

**Best Case** — Everything goes right
- What could make this direction highly successful?
- What conditions would need to hold?

**Base Case** — Expected outcome
- What does success look like?
- What are the key dependencies?

**Worst Case** — Things go wrong
- What could cause this direction to fail?
- What are the biggest risks?

**Adversarial** — Someone actively opposes
- What would competitors do?
- What objections would stakeholders raise?

## Application

Use this skill when:
1. Validating a new product direction before development
2. Exploring strategic alternatives
3. Preparing for stakeholder conversations
4. Building confidence in a decision

### Input Requirements

- Product direction or hypothesis
- Target personas (internal and external)
- Market context
- Success criteria

### Output Structure

```
Product Direction Simulation:

Direction: [Your product direction]

Persona Reactions:
- Persona 1: [Reaction]
- Persona 2: [Reaction]
- ...

Scenario Analysis:
- Best Case: [Outcome]
- Base Case: [Outcome]
- Worst Case: [Outcome]
- Adversarial: [Response]

Key Insights:
- [Pattern 1]
- [Pattern 2]

Recommendations:
- [Recommendation 1]
- [Recommendation 2]
```

## Examples

### Example 1: New Feature Direction

```
Direction: Add AI-powered recommendations to existing product

Persona Reactions:
- Power User: Excited about personalization, wants customization
- Casual User: Skeptical about privacy, wants simplicity
- Executive: Wants revenue impact, concerned about cost
- Support Team: Worried about complexity, needs training

Scenario Analysis:
- Best Case: 30% engagement increase, 15% retention lift
- Base Case: 10% engagement increase, neutral retention
- Worst Case: User backlash, privacy concerns dominate
- Adversarial: Competitor releases better alternative

Key Insights:
- Privacy concerns are significant barrier
- Need clear value proposition for casual users
- Executive buy-in requires ROI model

Recommendations:
- Lead with value, not AI
- Provide privacy controls upfront
- Build ROI model before presenting
```

### Example 2: Market Entry Strategy

```
Direction: Enter emerging market with simplified product

Persona Reactions:
- Early Adopter: Excited, wants features
- Mainstream: Needs reliability, support
- Partner: Wants integration, co-marketing
- Competitor: Will likely discount, litigate

Scenario Analysis:
- Best Case: 20% market share in 2 years
- Base Case: 5% market share, steady growth
- Worst Case: Legal challenges, price war
- Adversarial: Aggressive competitor response

Key Insights:
- Partner strategy is critical
- Need localization support
- Legal review required before launch

Recommendations:
- Secure partnerships early
- Budget for localization
- Prepare legal defense
```

## Common Pitfalls

### Pitfall 1: Confirmation Bias
**Symptom:** Only simulating scenarios that support your direction.

**Consequence:** Missing critical risks.

**Fix:** Include adversarial scenarios. Challenge your assumptions.

### Pitfall 2: Too Many Personas
**Symptom:** Simulating with 10+ personas, losing focus.

**Consequence:** Analysis paralysis, no insights.

**Fix:** Limit to 4-6 key personas. Focus on diverse perspectives.

### Pitfall 3: No Action
**Symptom:** Running simulations but not changing direction.

**Consequence:** Wasted effort, no improvement.

**Fix:** Define action triggers. "If X simulation result, then Y action."

### Pitfall 4: One-Time Exercise
**Simulating direction only at the beginning of a project.

**Consequence:** Missing changes in market conditions.

**Fix:** Re-simulate at key milestones. Update assumptions regularly.

## References

### Related Skills
- `skills/direction-engine/SKILL.md` — Continuous direction calibration
- `skills/10x-hypothesis-framework/SKILL.md` — Hypothesis testing
- `skills/opportunity-solution-tree/SKILL.md` — Solution exploration

### External Resources
- Oasis research — Large-scale simulation methodologies
- MiroFish — Digital twin prediction engines
- "The Art of War" — Strategic thinking frameworks
