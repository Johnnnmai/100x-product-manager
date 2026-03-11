---
name: persona-simulation-builder
description: Use when you need to build realistic user personas for simulation, creating agent profiles that can react authentically to product directions in MiroFish/OASIS.
type: component
tier: advanced
pack: ai-prediction
best_for:
  - building simulation-ready personas
  - creating diverse user profiles for testing
  - generating OASIS-compatible agent profiles
  - defining behavioral characteristics for simulation
outputs:
  - persona profiles (JSON)
  - behavioral characteristic definitions
  - key attitudes and preferences
  - simulation-ready agent configurations
xpm_dimension:
  - discovery
  - strategy
xpm_rules:
  - evidence_beats_opinion
  - speed_is_strategy
---

## Purpose

Build realistic user personas specifically designed for agent simulation in MiroFish/OASIS. This skill helps you create diverse, authentic user profiles that will react realistically when exposed to your product direction in a simulated environment.

This is NOT about creating marketing personas. It is about creating simulation profiles with the right behavioral characteristics, attitudes, and constraints that will generate meaningful insights when simulated.

## Key Concepts

### Persona vs Simulation Profile

| Marketing Persona | Simulation Profile |
|-----------------|-------------------|
| Qualitative description | Quantitative parameters |
| Narrative, story-driven | Behavior-driven, actionable |
| For human understanding | For agent simulation |
| 1-2 pages of text | Structured JSON (200-500 lines) |

### OASIS Agent Profile Structure

Based on OASIS/MiroFish research, a simulation profile contains:

```json
{
  "user_id": "unique_identifier",
  "demographics": {
    "age_range": "25-34",
    "location": "urban",
    "income_level": "middle"
  },
  "interests": [
    "technology",
    "productivity"
  ],
  "behavioral_traits": {
    "openness": 0.8,
    "conscientiousness": 0.6,
    "tech_savviness": 0.9
  },
  "preferences": {
    "privacy_sensitivity": "high",
    "price_sensitivity": "medium",
    "feature_complexity_tolerance": "low"
  },
  "pain_points": [
    "time_consuming_support",
    "complex_setup"
  ],
  "goals": [
    "reduce_costs",
    "improve_efficiency"
  ],
  "platform_usage": {
    "twitter": "daily",
    "reddit": "weekly",
    "linkedin": "monthly"
  }
}
```

### Key Behavioral Dimensions

1. **Tech Savviness**: Low to High — How comfortable with new technology
2. **Price Sensitivity**: Low/Medium/High — Price as decision factor
3. **Privacy Sensitivity**: Low/Medium/High — Data sharing comfort
4. **Feature Complexity Tolerance**: Low/Medium/High — Desire for simple vs feature-rich
5. **Brand Loyalty**: Low/Medium/High — Switch behavior
6. **Social Influence**: Low/Medium/High — Susceptibility to social proof

## Application

### When to Use

- Before running product direction simulations
- When building validation workflows
- When stress-testing assumptions with diverse perspectives
- When preparing for stakeholder conversations

### Input Requirements

```
Target Market:
- Industry: [e.g., B2B SaaS]
- Segment: [e.g., SMBs, 5-50 employees]
- Users: [e.g., Support Managers]

Existing Research:
- Customer interviews (if any)
- Survey data (if any)
- Support tickets
- Reviews

Simulation Context:
- Product direction to test
- Key hypotheses
- Competitors to consider
```

### Building Personas

#### Step 1: Define Diversity Dimensions

Identify 4-6 dimensions that create meaningful diversity:

- Role (e.g., Executive, User, Buyer)
- Experience level (e.g., Expert, Novice)
- Tech comfort (e.g., Early adopter, Laggard)
- Budget authority (e.g., Decision maker, Influencer)
- Company size (e.g., SMB, Enterprise)

#### Step 2: Create Behavioral Profiles

For each persona, define:

```
Persona: "Skeptical Sarah"
- Role: Support Manager
- Company: 50-person startup
- Pain points: Implementation time, hidden costs
- Goals: Reduce support tickets, keep team happy
- Behavioral traits:
  - Tech savviness: 5/10 (can use tools, but skeptical of new ones)
  - Price sensitivity: 8/10 (budget-conscious)
  - Privacy sensitivity: 6/10 (reasonable concerns)
  - Complexity tolerance: 3/10 (wants simple)
- Typical reactions:
  - Positive: "Quick to set up", "Clear pricing"
  - Negative: "Too complex", "Hidden fees"
```

#### Step 3: Convert to OASIS Format

Translate behavioral description into OASIS-compatible JSON with numerical parameters.

#### Step 4: Validate

Ensure personas:
- Cover diverse perspectives
- Include adversarial (skeptical, critical) voices
- Are realistic, not stereotypes

### Output Structure

```
## Persona Profiles

### Persona 1: [Name]
**Role**: [Job title]
**Company**: [Type/size]
**Key Traits**:
- Tech savviness: X/10
- Price sensitivity: X/10
- Privacy sensitivity: X/10
- Complexity tolerance: X/10

**Behavioral Profile** (JSON):
```json
{
  ...
}
```

**Expected Reactions**:
- To product: [Reaction]
- To pricing: [Reaction]
- To feature X: [Reaction]

### Persona 2: [Name]
...
```

## Examples

### Example 1: B2B SaaS Support Product

```
Building personas for: AI Customer Support for SMBs

Dimension Analysis:
- Role: Support Manager, IT Director, Operations
- Tech comfort: Early adopter vs Laggard
- Budget: Decision maker vs Influencer
- Company: Startup vs Established

Created 5 Personas:

1. "Eager Emily" - Early adopter Support Manager, loves new tech
2. "Skeptical Sarah" - Traditional Support Manager, needs proof
3. "Budget Brian" - Ops manager, cost-focused decision maker
4. "Tech Tony" - IT Director, wants integration, API
5. "Time-Pressed Tara" - Overworked manager, wants quick wins

OASIS JSON generated for each persona.
```

### Example 2: Consumer Health App

```
Building personas for: Habit Tracking with Social Features

Dimension Analysis:
- Age: Gen Z vs Millennial vs Gen X
- Privacy: Sharing vs Private
- Motivation: Achievement vs Social vs Health
- Platform: Mobile-first vs Desktop

Created 6 Personas:

1. "Social Sam" - Gen Z, loves sharing, high engagement
2. "Private Pat" - Millennial, wants tracking, no social
3. "Achievement Alex" - All ages, gamification lover
4. "Health Helen" - Gen X, privacy-first, long-term
5. "Casual Chris" - Just wants simple tracking
6. "Influencer Iris" - Active on social, wants recognition
```

## Common Pitfalls

### Pitfall 1: Persona Homogeneity
**Symptom**: All personas think alike.

**Consequence**: Simulation shows false consensus.

**Fix**: Include diverse perspectives, including adversarial voices.

### Pitfall 2: Stereotyping
**Symptom**: Personas based on clichés, not research.

**Consequence**: Unrealistic reactions in simulation.

**Fix**: Ground personas in real data: interviews, support tickets, reviews.

### Pitfall 3: Too Many Personas
**Symptom**: 10+ personas for every simulation.

**Consequence**: Analysis paralysis, no insights.

**Fix**: Limit to 4-6 key personas. Quality over quantity.

### Pitfall 4: Perfect Personas
**Symptom**: Only positive, eager users.

**Consequence**: Missed adoption barriers.

**Include**: Skeptics, critics, price-sensitive users, non-technical users.

### Pitfall 5: Static Personas
**Symptom**: Same personas used for months.

**Consequence**: Missing market evolution.

**Fix**: Re-validate personas periodically. Markets change.

## References

### Related Skills
- `skills/product-direction-validation/SKILL.md` — Full validation workflow
- `skills/simulation-analyst/SKILL.md` — Analyzing simulation results
- `skills/proto-persona/SKILL.md` — Quick persona creation
- `skills/jobs-to-be-done/SKILL.md` — Understanding user jobs

### External Resources
- [OASIS GitHub](https://github.com/camel-ai/oasis) — Agent simulation engine
- [MiroFish](https://github.com/666ghj/MiroFish) — Digital twin platform
- [OASIS Agent Profiles](https://github.com/camel-ai/oasis/tree/main/data/reddit) — Example profiles

### Technical Notes
- OASIS expects JSON profiles in specific format
- MiroFish accepts OASIS profiles plus additional fields
- Profiles can be refined through multiple simulation iterations
