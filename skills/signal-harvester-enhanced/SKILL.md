---
name: signal-harvester-enhanced
description: Use when you need to collect market signals from the web, enhanced to output simulation-ready seed data for MiroFish/OASIS persona simulation.
type: component
tier: advanced
pack: ai-prediction
best_for:
  - gathering market signals for product validation
  - collecting user opinions and pain points
  - preparing seed data for simulation
  - competitive intelligence gathering
outputs:
  - structured signal summary
  - sentiment analysis
  - key themes and topics
  - simulation-ready seed data (JSON)
xpm_dimension:
  - discovery
  - evidence
xpm_rules:
  - evidence_beats_opinion
  - speed_is_strategy
---

## Purpose

Enhanced market signal collection that goes beyond basic research to produce simulation-ready seed data for persona simulation in MiroFish/OASIS. This skill combines web scraping, sentiment analysis, and structured output to feed directly into the simulation pipeline.

This skill is built on top of `market-signal-harvester` with additional capabilities for simulation preparation.

## Key Concepts

### Signal vs Seed Data

| Raw Signals | Simulation Seed Data |
|------------|---------------------|
| Unstructured text | Structured JSON |
| General themes | Persona-specific attitudes |
| Qualitative insights | Quantitative parameters |
| Human-readable | Agent-consumable |

### Seed Data Structure

For simulation, signals need to be converted to:

```json
{
  "seed_topics": [
    {
      "topic": "AI customer support",
      "sentiment": "mixed",
      "intensity": 0.7,
      "source_distribution": {
        "twitter": 0.4,
        "reddit": 0.3,
        "reviews": 0.3
      },
      "key_themes": [
        "implementation_complexity",
        "cost_benefit",
        "time_to_value"
      ],
      "persona_relevance": {
        "early_adopter": "positive",
        "skeptical_user": "negative",
        "budget_conscious": "concerned"
      }
    }
  ],
  "attitudinal_statements": [
    {
      "statement": "AI support can't understand complex issues",
      "sentiment": "negative",
      "prevalence": 0.35,
      "source": "reddit/support"
    },
    {
      "statement": "Saves our team 10 hours/week",
      "sentiment": "positive",
      "prevalence": 0.45,
      "source": "reviews/g2"
    }
  ],
  "competitive_signals": [
    {
      "competitor": "Intercom",
      "perception": "expensive but reliable",
      "pain_points": ["cost", "complexity"]
    }
  ]
}
```

### Signal Collection Sources

1. **Review Platforms**: G2, Capterra, TrustRadius, App Store, Play Store
2. **Social Media**: Twitter/X, Reddit, LinkedIn
3. **Q&A Sites**: Quora, Stack Overflow
4. **Forums**: Industry-specific forums, Discord communities
5. **News**: Press releases, announcement articles

## Application

### When to Use

- Before running persona simulations
- As input to `product-direction-validation` workflow
- When validating product assumptions
- When building competitive intelligence

### Input Requirements

```
Product Context:
- Product/service category
- Target market segment
- Key competitors (if known)

Search Queries:
- Product-related terms
- Problem-related terms
- Competitor mentions

Scope:
- Time period (last 3/6/12 months)
- Sources to prioritize
- Geographic focus (optional)
```

### Signal Collection Workflow

#### Step 1: Define Search Strategy

Create search queries for:
- Problem-focused: "[problem] + frustration + help"
- Solution-focused: "[solution] + review + vs"
- Competitor-focused: "[competitor] + alternative +替代"
- Category: "[category] + best + for + [segment]"

#### Step 2: Execute Collection

Use Scrapling or manual search to gather:
- Reviews (2-stars and below for pain points)
- Discussions (Reddit threads, forum posts)
- Social media (Twitter, LinkedIn)
- Q&A (Quora, Stack Overflow)

#### Step 3: Extract and Structure

For each signal source:
- Extract key themes
- Note sentiment (positive/negative/mixed)
- Identify persona relevance
- Document source and prevalence

#### Step 4: Convert to Seed Data

Transform into simulation-ready JSON:
- Categorize by topic
- Assign sentiment scores
- Map to persona attitudes
- Include competitive context

### Output Structure

```
## Signal Summary

### Key Themes Identified
1. Theme 1: [Description] - [Prevalence: X%]
2. Theme 2: [Description] - [Prevalence: X%]
...

### Sentiment Analysis
- Overall: [X% positive / Y% negative / Z% mixed]
- By source: [Twitter: X%, Reddit: Y%, Reviews: Z%]

### Top Pain Points
1. Pain point 1
2. Pain point 2
...

### Opportunities Identified
1. Opportunity 1
2. Opportunity 2
...

### Competitive Landscape
- Competitor A: [Positioning]
- Competitor B: [Positioning]

## Seed Data (JSON)

```json
{
  "seed_topics": [...],
  "attitudinal_statements": [...],
  "competitive_signals": [...]
}
```

### Sources Analyzed
- [Source 1]: [X] items
- [Source 2]: [Y] items
...
```

## Examples

### Example 1: AI Customer Support

```
Input:
- Product: AI Customer Support
- Target: SMBs
- Competitors: Intercom, Zendesk, Freshdesk

Signal Collection:
- G2: 127 reviews analyzed
- Reddit: 34 threads analyzed
- Twitter: 89 posts analyzed
- Capterra: 45 reviews analyzed

Key Findings:
- Pain points: "Setup too complex" (23%), "Price too high" (18%), "Not smart enough" (15%)
- Positive: "Saves time" (34%), "Easy to use" (22%), "Good support" (15%)
- Competitive: Intercom seen as "enterprise only", Zendesk as "expensive"

Seed Data Generated:
- 8 topic clusters
- 24 attitudinal statements
- 3 competitor profiles
```

### Example 2: Habit Tracking App

```
Input:
- Product: Habit Tracking with Social
- Target: Gen Z / Millennials
- Competitors: Habitica, Streaks, Loop

Signal Collection:
- App Store: 200 reviews
- Reddit r/habits: 45 threads
- Twitter: 120 posts

Key Findings:
- Pain points: "Social features feel forced" (19%), "Privacy concerns" (16%), "Lost data" (12%)
- Positive: "Gamification works" (28%), "Simple interface" (24%), "Reminders helpful" (18%)
- Opportunities: Privacy-first option, Cross-platform sync

Seed Data Generated:
- 6 topic clusters
- 20 attitudinal statements
- 2 competitor profiles
```

## Common Pitfalls

### Pitfall 1: Confirmation Bias
**Symptom**: Only looking at positive signals.

**Consequence**: Missing real pain points, overconfident validation.

**Fix**: Prioritize negative reviews, critical discussions.

### Pitfall 2: Sample Bias
**Symptom**: Only checking one source type.

**Consequence**: Incomplete picture.

**Fix**: Multi-source collection: reviews + social + forums.

### Pitfall 3: Outdated Signals
**Symptom**: Using old data.

**Consequence**: Missing recent market changes.

**Fix**: Set time windows, prioritize recent signals.

### Pitfall 4: Surface-Level Collection
**Symptom**: Only collecting headline reviews.

**Consequence**: Missing nuance.

**Fix**: Read full reviews, follow discussion threads.

### Pitfall 5: No Competitor Context
**Symptom**: Only looking at product in isolation.

**Consequence**: Missing competitive alternatives.

**Fix**: Include competitor signals in seed data.

## References

### Related Skills
- `skills/product-direction-validation/SKILL.md` — Full validation workflow
- `skills/market-signal-harvester/SKILL.md` — Base skill (prerequisite)
- `skills/persona-simulation-builder/SKILL.md` — Build personas from signals
- `skills/evidence-collector/SKILL.md` — Evidence gathering

### External Resources
- [Scrapling](https://github.com/D4Vinci/Scrapling) — Adaptive web scraping
- [OASIS](https://github.com/camel-ai/oasis) — Simulation engine
- [MiroFish](https://github.com/666ghj/MiroFish) — Prediction platform

### Prerequisites
- Scrapling installed (recommended) or manual search
- Basic understanding of sentiment analysis
- Familiarity with target market
