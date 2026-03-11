---
name: token-budget-optimizer
description: Use when teams want to improve output quality on smaller or cheaper models, or when agents work across long product workflows requiring context optimization.
type: component
tier: core
pack: memory-optimization
best_for:
  - teams improving output quality on smaller or cheaper models
  - agents working across long product workflows
outputs:
  - context budget strategy
  - keep/compress/archive plan
  - escalation rules
xpm_dimension:
  - leverage
  - ai_behavior
xpm_rules:
  - leverage_beats_effort
  - artifacts_are_outputs
---

## Purpose

Optimize token usage for AI agents working on complex, multi-step PM workflows. This skill helps teams decide what must remain in active context, what can be compressed, what belongs in memory, and when to escalate to stronger models.

This is not about cutting costs by reducing context. It is about maximizing output quality within budget constraints.

## Key Concepts

### The Token Budget Problem

When agents work on long PM workflows:
- Context grows with each step
- Important information gets buried
- Quality degrades as context lengthens
- Costs spiral without visibility

### Three-Tier Context Architecture

**Tier 1: Active)**
- Current Context (Keep Now task requirements
- Recent outputs being refined
- Immediate constraints and success criteria
- ~2,000-4,000 tokens typical

**Tier 2: Compressed Context (Compress Now)**
- Completed phases with key decisions
- Summarized stakeholder inputs
- Archived but referenceable artifacts
- ~4,000-8,000 tokens typical

**Tier 3: Memory/Reference (Archive)**
- Project background and context
- Previous project learnings
- Company/process documentation
- Retrieved on demand

### Progressive Disclosure Pattern

Following claude-mem's proven approach:
1. **Search** → Get compact index + IDs (~50-100 tokens/result)
2. **Timeline** → Get surrounding context in time order
3. **Get Details** → Full details for filtered items (~500-1000 tokens/item)

### When to Escalate

Escalate to stronger model or human when:
- Task requires multi-domain synthesis
- Ambiguous requirements need judgment
- Output quality critical and budget exceeded
- Context window would need truncation

## Application

Use this skill when:
1. Starting a long-running PM workflow (multi-week project)
2. Noticing quality degradation in agent outputs
3. Budget concerns arise mid-project
4. Planning project scope and agent config

### Input Requirements

- Project scope and duration
- Available models and their context limits
- Quality requirements for outputs
- Budget constraints

### Output Structure

```
Context Budget Strategy:
- Active context allocation: [X] tokens
- Compressed context allocation: [Y] tokens
- Memory/reference allocation: [Z] tokens

Keep Now:
- [Item]: [Why active]

Compress Now:
- [Item]: [Summary approach]

Move to Memory:
- [Item]: [Retrieval trigger]

Escalate If:
- [Condition]: [Escalation path]
```

## Examples

### Example 1: PRD Development Workflow

```
Context Budget (Anthropic Haiku - 200K context):

Active (3K tokens):
- Current PRD section being drafted
- Success criteria for this section
- Recent feedback from stakeholders

Compressed (6K tokens):
- Problem statement (summarized)
- Target user research (key insights only)
- Competitor analysis (summary table)

Memory (retrieved):
- Company brand guidelines
- Product history and context
- Similar past PRDs for reference

Escalate:
- If section requires cross-team coordination → Human review
- If technical feasibility unclear → Escalate to CTO agent
```

### Example 2: Research Sprint

```
Context Budget (Claude Sonnet - 100K context):

Active (5K tokens):
- Research questions
- Current interview notes being analyzed
- Synthesis of last 3 interviews

Compressed (10K tokens):
- Interview summaries (one paragraph each)
- Competitor analysis (key points only)

Memory (retrieved):
- Industry background
- Company strategy docs

Escalate:
- If insights conflict → Synthesize with human
- If requires strategic judgment → Human decision
```

## Common Pitfalls

### Pitfall 1: Context Stuffing
**Symptom:** Putting everything "just in case" into active context.

**Consequence:** Quality degrades, costs increase, agent attention diffuses.

**Fix:** Strict tier discipline. Only active context gets full attention.

### Pitfall 2: Never Compressing
**Symptom:** Keep everything in active context, never summarize.

**Consequence:** Hit context limits, lose important information, forced to restart.

**Fix:** Compress completed phases proactively. At each milestone, compress and archive.

### Pitfall 3: No Escalation Rules
**Symptom:** Agents continue with degraded output instead of escalating.

**Consequence:** Poor quality deliverables, budget waste.

**Fix:** Define explicit escalation triggers. "If X, escalate to Y."

### Pitfall 4: Cheapest Model Mindset
**Symptom:** Always use cheapest model regardless of task.

**Consequence:** Rework due to quality issues, false economy.

**Fix:** Match model capability to task complexity. Some tasks need Sonnet/Opus.

## References

### Related Skills
- `skills/task-delegation-planner/SKILL.md` — Define what to delegate
- `skills/task-tracking-operator/SKILL.md` — Track ongoing work
- `skills/context-engineering-advisor/SKILL.md` — Design effective prompts

### External Resources
- claude-mem (thedotmack) — Progressive disclosure pattern
- Anthropic token optimization best practices
- "Token Budget Operations" — Cost management frameworks
