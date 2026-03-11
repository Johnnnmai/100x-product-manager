---
name: task-delegation-planner
description: Use when teams need to split work between humans and agents, or when PMs need to define execution contracts between human team members and AI agents.
type: interactive
tier: core
pack: roadmaps-delegation
best_for:
  - teams splitting work between humans and agents
  - PMs defining execution contracts
outputs:
  - human vs agent split
  - task contracts
  - context requirements
xpm_dimension:
  - leverage
  - ai_behavior
xpm_rules:
  - leverage_beats_effort
  - prds_for_humans_and_agents
---

## Purpose

Split work between human team members and AI agents with clear ownership, context, and handoff rules. This skill helps PMs define who (human or agent) owns what work, what context each actor needs, and what triggers escalation.

This is not just a task list. It is a delegation framework that ensures agent work has explicit contracts while human judgment is preserved where needed.

## Key Concepts

### What is Task Delegation Planning?

Task delegation planning is the process of:
1. **Separating judgment-heavy from execution-heavy work** — Identify which tasks require human intuition, creativity, or stakeholder management vs. which can be automated
2. **Defining explicit contracts** — For agent-owned work, specify inputs, constraints, expected outputs, and success criteria
3. **Determining context needs** — Each actor (human or agent) needs different context to make decisions
4. **Setting escalation triggers** — Define when agent work should be escalated to human review

### Why This Matters for AI-Shaped PM

- **Agent capabilities are not human capabilities** — Agents excel at structured, repetitive tasks but lack contextual judgment
- **Explicit contracts prevent rework** — Vague agent instructions lead to outputs that need extensive revision
- **Human judgment is scarce** — Preserve human time for decisions that truly require it

### Delegation Decision Framework

**Delegate to Agent When:**
- Output criteria can be explicit and measurable
- Input format is structured (PRD, spec, data)
- Task is repetitive or follows known patterns
- Quality can be validated through checks

**Keep with Human When:**
- Decision requires stakeholder intuition
- Output needs creative or strategic framing
- Context spans multiple domains
- Risk of misjudgment is high

## Application

Use this skill when:
1. Starting a new project that will involve both human and agent work
2. Onboarding a new agent capability to the team
3. Breaking down a large initiative into executable tasks
4. Reviewing current workload to identify automation opportunities

### Input Requirements

- Project scope and objectives
- Available human capacity
- Agent capabilities and limitations
- Existing documentation (PRDs, specs, process docs)

### Output Structure

```
Human-Owned Tasks:
- [Task]: [Why human judgment required]
- ...

Agent-Owned Tasks:
- [Task]: [Success criteria] → [Output format]
- ...

Context Requirements:
- Human tasks need: [context]
- Agent tasks need: [context + constraints]

Escalation Triggers:
- [Condition]: [Escalation path]
```

## Examples

### Example 1: Feature Development

```
Human-Owned:
- Define product strategy and positioning
- Lead stakeholder communication
- Make trade-off decisions on scope
- Final quality review and approval

Agent-Owned:
- Generate initial PRD draft → Structured document
- Create user story specifications → Gherkin format
- Research competitor features → Comparison table
- Draft technical specification → Markdown spec

Context:
- Agents receive: Business context, success metrics, constraints
- Humans receive: Full project context, stakeholder input
```

### Example 2: Research Project

```
Human-Owned:
- Frame research questions
- Interpret ambiguous findings
- Make strategic recommendations

Agent-Owned:
- Conduct competitive analysis → Findings doc
- Summarize interview notes → Key themes
- Compile market data → Data tables
```

## Common Pitfalls

### Pitfall 1: Delegating Based on Convenience
**Symptom:** Assigning tasks to agents because they're "faster" without considering judgment requirements.

**Consequence:** Agent outputs that can't be used, requiring human rework.

**Fix:** Judge delegation by judgment requirements, not speed.

### Pitfall 2: Vague Agent Contracts
**Symptom:** Agent instructions like "write a good PRD" without success criteria.

**Consequence:** Outputs that miss the point, extensive revision cycles.

**Fix:** Define explicit inputs, constraints, and output format for each agent task.

### Pitfall 3: Missing Escalation Paths
**Symptom:** No defined criteria for when agent should escalate to human.

**Consequence:** Agents silently produce poor output or get stuck.

**Fix:** Define clear escalation triggers (e.g., "if requirements conflict," "if no clear answer in 3 attempts").

### Pitfall 4: Context Overload
**Symptom:** Giving agents all context "just in case."

**Consequence:** Agent performance degrades with too much context, higher token costs.

**Fix:** Provide minimum viable context for each task.

## References

### Related Skills
- `skills/task-tracking-operator/SKILL.md` — Track progress of delegated tasks
- `skills/token-budget-optimizer/SKILL.md` — Optimize context for agent tasks
- `skills/context-engineering-advisor/SKILL.md` — Design effective context for agents

### External Resources
- "The Manager's Path" — Delegation frameworks
- "Rework" by Basecamp — Minimal delegation philosophy
- Anthropic AI best practices — Agent instruction patterns
