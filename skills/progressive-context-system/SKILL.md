---
name: progressive-context-system
description: Use when agents work on long-running PM workflows and you need progressive context disclosure with layered memory architecture.
type: component
tier: core
pack: memory-optimization
best_for:
  - long-running PM workflows with multiple phases
  - projects requiring context compression over time
  - teams wanting to optimize token usage while maintaining quality
outputs:
  - three-tier context architecture
  - progressive disclosure strategy
  - memory retrieval triggers
xpm_dimension:
  - leverage
  - ai_behavior
xpm_rules:
  - leverage_beats_effort
  - artifacts_are_outputs
---

## Purpose

Implement a progressive context disclosure system for AI agents working on complex, multi-phase PM workflows. This skill provides a layered memory architecture that reveals information progressively based on relevance and urgency, optimizing both token usage and output quality.

This is not about storing everything. It is about designing a system that reveals the right information at the right time.

## Key Concepts

### Three-Tier Context Architecture

**Tier 1: Active Working Context (Keep Now)**
- Current task in focus
- Immediate constraints and success criteria
- Last 1-2 outputs being refined
- ~2,000-4,000 tokens typical
- Refreshed every few turns

**Tier 2: Episodic Context (Compress Periodically)**
- Completed phases with key decisions
- Summarized stakeholder inputs
- Milestone outcomes
- ~4,000-8,000 tokens typical
- Compressed at each phase boundary

**Tier 3: Persistent Memory (Retrieve on Demand)**
- Project background and context
- Company/process documentation
- Previous project learnings
- No fixed token limit
- Retrieved via explicit queries

### Progressive Disclosure Pattern

Following claude-mem's proven approach:
1. **Search** → Get compact index + IDs (~50-100 tokens/result)
2. **Timeline** → Get surrounding context in time order
3. **Get Details** → Full details for filtered items (~500-1000 tokens/item)

### Why Progressive Disclosure Matters

- **Token efficiency** — Only pay for what you need
- **Reduced noise** — Less context means less distraction
- **Better quality** — Agents focus on what's relevant
- **Cost predictability** — Budget becomes more predictable

## Application

Use this skill when:
1. Starting a long-running PM workflow (multi-week project)
2. Noticing quality degradation in later phases
3. Need to optimize token costs without losing quality
4. Working with multiple agents or hand-offs

### Input Requirements

- Project scope and phases
- Current phase and progress
- Available context window size
- Token budget constraints

### Output Structure

```
Context Architecture:

Active Working Context (~X tokens):
- [Current focus]
- [Immediate constraints]
- [Recent outputs]

Episodic Context (~Y tokens):
- [Phase 1 summary]
- [Phase 2 summary]
- [Key decisions made]

Persistent Memory:
- [Project background]
- [Retrieval triggers]
```

## Examples

### Example 1: PRD Development

```
Phase 1: Problem Definition
Active: Current problem statement being refined
Episodic: (none yet)
Memory: Company background, market context

Phase 2: Solution Exploration
Active: Solution options being evaluated
Episodic: Problem definition compressed to key insights
Memory: Company background, market context

Phase 3: PRD Writing
Active: PRD sections being drafted
Episodic: Problem + Solutions compressed
Memory: Full retrieval available
```

### Example 2: Research Sprint

```
Week 1: Discovery
Active: Interview 1-3 analysis
Episodic: (none yet)
Memory: Research goals, company context

Week 2: Deep Dive
Active: Interview 4-6 analysis
Episodic: Week 1 themes compressed
Memory: Full retrieval available
```

## Common Pitfalls

### Pitfall 1: Everything in Active Context
**Symptom:** Keeping all information in active context "just in case."

**Consequence:** Quality degrades, costs increase, agent attention diffuses.

**Fix:** Strict tier discipline. Only active work goes in Tier 1.

### Pitfall 2: Never Compressing
**Symptom:** Keeping full context from early phases throughout.

**Consequence:** Hit context limits, lose important information.

**Fix:** Compress at each phase boundary. Summarize decisions and outcomes.

### Pitfall 3: No Retrieval Strategy
**Symptom:** Having memory but no way to access it.

**Consequence:** Relevant information remains buried.

**Fix:** Define clear retrieval triggers. "If X, query memory for Y."

### Pitfall 4: Losing Context
**Symptom:** Compressing too aggressively, losing important context.

**Consequence:** Agent makes decisions without full information.

**Fix:** Keep key decisions and constraints in episodic tier. Don't compress everything.

## References

### Related Skills
- `skills/token-budget-optimizer/SKILL.md` — Optimize token usage
- `skills/task-delegation-planner/SKILL.md` — Define delegation
- `skills/context-engineering-advisor/SKILL.md` — Design effective prompts

### External Resources
- claude-mem (thedotmack) — Progressive disclosure pattern
- Anthropic context window best practices
- "Building Agentic Systems" — Context management patterns
