---
name: agent-lifecycle-hooks
description: Use when you need to implement lifecycle hooks for PM Agent sessions, including session start/end, turn boundaries, phase transitions, error handling, and quality gates.
type: component
tier: core
pack: memory-optimization
best_for:
  - implementing session management for PM agents
  - adding quality gates and checkpoints
  - monitoring token budgets and performance
outputs:
  - lifecycle hook definitions
  - quality gate criteria
  - checkpoint strategy
xpm_dimension:
  - execution
  - ai_behavior
xpm_rules:
  - leverage_beats_effort
  - artifacts_are_outputs
---

## Purpose

Implement lifecycle hooks for PM Agent sessions to ensure quality, manage resources, and enable proper handoffs. This skill provides hooks at key points in the agent workflow: session start, each turn, phase transitions, errors, and session end.

This is not about monitoring for surveillance. It is about creating checkpoints that ensure quality and enable continuous improvement.

## Key Concepts

### Lifecycle Hook Points

**1. Session Start Hook**
- Initialize context from memory
- Load relevant project background
- Set success criteria and constraints
- Check token budget allocation

**2. Turn Start Hook**
- Review previous output quality
- Check if escalation needed
- Update active context

**3. Turn End Hook**
- Validate output against quality gates
- Check token budget consumption
- Update tracking metrics
- Prepare context for next turn

**4. Phase Change Hook**
- Compress previous phase context
- Archive completed work
- Load new phase context
- Validate phase transition criteria

**5. Error Hook**
- Capture error context
- Log for debugging
- Trigger recovery workflow
- Notify if human intervention needed

**6. Session End Hook**
- Summarize session outcomes
- Archive final context
- Update persistent memory
- Release resources

### Quality Gates

Define explicit pass/fail criteria at each hook:
- **Output completeness** — Does output address all requirements?
- **Format compliance** — Does output match required format?
- **Quality threshold** — Does output meet quality bar?
- **Budget compliance** — Are we within token budget?

### Checkpoint Strategy

- Save state at each phase transition
- Enable rollback to last checkpoint
- Track decision history for audit
- Monitor performance trends

## Application

Use this skill when:
1. Building PM Agent systems that need monitoring
2. Implementing quality control for agent outputs
3. Managing token budgets across sessions
4. Creating audit trails for decisions

### Input Requirements

- Session objectives
- Quality requirements
- Token budget constraints
- Phase structure

### Output Structure

```
Lifecycle Hooks Configuration:

session_start:
  - Load [context]
  - Set [constraints]
  - Initialize [metrics]

turn_start:
  - Review [previous_output]
  - Check [escalation_criteria]

turn_end:
  - Validate [quality_gates]
  - Update [metrics]
  - Prepare [next_context]

phase_change:
  - Compress [previous_phase]
  - Archive [completed_work]
  - Load [next_phase_context]

error:
  - Capture [error_context]
  - Log [for_debugging]
  - Trigger [recovery]

session_end:
  - Summarize [outcomes]
  - Archive [final_context]
  - Update [persistent_memory]
```

## Examples

### Example 1: PRD Development Session

```
Session Start:
- Load: Project background, brand guidelines
- Set: Success criteria = "complete PRD with all sections"
- Initialize: Token budget = 50K tokens

Turn End Quality Gate:
- Completeness: All PRD sections addressed?
- Format: Follows PRD template?
- Quality: Clear, actionable specs?

Phase Change (Problem → Solution):
- Archive: Problem definition summary
- Load: Solution exploration context
- Validate: Problem is clearly defined?
```

### Example 2: Research Sprint

```
Session Start:
- Load: Research goals, stakeholder questions
- Set: Deliverable = "insights report"
- Initialize: 100K token budget

Turn End:
- Token budget remaining check
- Output quality validation
- Context compression trigger

Session End:
- Summarize key findings
- Update research memory
- Flag follow-up items
```

## Common Pitfalls

### Pitfall 1: No Quality Gates
**Symptom:** Agent outputs are accepted without validation.

**Consequence:** Poor quality deliverables, rework needed.

**Fix:** Define explicit quality criteria at each turn end.

### Pitfall 2: Over-Monitoring
**Symptom:** Too many hooks slow down execution.

**Consequence:** Agent becomes unusable, user frustrated.

**Fix:** Balance monitoring with usability. Focus on key checkpoints.

### Pitfall 3: No Checkpoints
**Symptom:** No way to recover from errors.

**Consequence:** Must restart entire session on failure.

**Fix:** Save state at each phase transition. Enable rollback.

### Pitfall 4: Ignoring Budget
**Symptom:** No token budget monitoring.

**Consequence:** Unexpected costs, session failures.

**Fix:** Track budget at each turn. Set alerts and auto-compress.

## References

### Related Skills
- `skills/token-budget-optimizer/SKILL.md` — Token budget management
- `skills/progressive-context-system/SKILL.md` — Context architecture
- `skills/task-tracking-operator/SKILL.md` — Progress tracking

### External Resources
- Anthropic agent patterns
- "Building Reliable Agents" — Error handling best practices
- "Agent Lifecycle Management" — Operational frameworks
