---
name: task-tracking-operator
description: Use when teams run weekly operating cadence across humans and agents, or when PMs need clear status reporting and replanning rules for delegated work.
type: component
tier: core
pack: roadmaps-delegation
best_for:
  - teams running weekly operating cadence across humans and agents
  - PMs who need clearer status and replan rules
outputs:
  - tracking format
  - status rules
  - blocker template
xpm_dimension:
  - execution
  - leverage
xpm_rules:
  - leverage_beats_effort
  - artifacts_are_outputs
---

## Purpose

Track progress of delegated tasks (both human and agent) with clear status categories, structured blocker reporting, and explicit replanning triggers. This skill transforms task tracking from a status ritual into a mechanism for replanning.

This is not just a checklist. It is an operating system for tracking work that spans human and agent ownership.

## Key Concepts

### What is Task Tracking for Delegated Work?

Task tracking for delegated work includes:
1. **Status categories that drive decisions** — Not just "done/in progress" but categories that trigger action
2. **Structured blocker reporting** — Standardized format for identifying and escalating blockers
3. **Replanning triggers** — Explicit criteria for when to revisit plans
4. **Cadence definition** — How often to review and what to review

### Why Standard Tracking Matters

- **Agent work lacks intuition** — Unlike humans, agents won't surface issues unless explicitly prompted
- **Blockers compound faster** — Delegated work can go off-track quickly without visibility
- **Replanning is normal** — Original plans should change based on learning

### Status Categories That Drive Action

**Recommended Status Categories:**
- **On Track** — Progressing as planned, no concerns
- **At Risk** — May miss deadline, needs attention
- **Blocked** — Cannot proceed, needs resolution
- **Done** — Completed and validated
- **Needs Replan** — Original assumption no longer valid

**Anti-Patterns:**
- "In Progress" without clarity on completion criteria
- "Waiting" without owner or timeline for resolution

### Blocker Categories

- **Resource Blocker** — Missing information, access, or person
- **Technical Blocker** — Technical constraint or dependency
- **Decision Blocker** — Awaiting decision from stakeholder
- **Scope Blocker** — Requirement change or unclear requirement

## Application

Use this skill when:
1. Starting a new project with delegated human/agent work
2. Running weekly team syncs
3. Identifying why work is behind schedule
4. Deciding when to replan vs. push through

### Input Requirements

- Task list from task-delegation-planner
- Current progress status
- Known blockers or issues

### Output Structure

```
Weekly Check-In Template:

Status Report:
| Task | Owner | Status | Confidence | Notes |
|------|-------|--------|------------|-------|
| ...  | ...   | ...    | ...        | ...   |

Blocker Report:
| Blocker | Category | Owner | Resolution | ETA |
|---------|----------|-------|------------|-----|
| ...     | ...      | ...   | ...        | ... |

Replanning Triggers:
- [Trigger]: [Action]
- ...
```

## Examples

### Example 1: Weekly Team Sync

```
Status Categories in Practice:

Task: "Write PRD for Feature X"
Owner: Agent
Status: At Risk
Confidence: 60%
Notes: Agent produced first draft but needs stakeholder input on scope

Task: "Review PRD"
Owner: PM
Status: Blocked
Confidence: N/A
Notes: Waiting for design team to finalize wireframes

Replanning Trigger:
- If "At Risk" persists for 2+ weeks → Reassess scope or add resources
- If "Blocked" for 1+ week → Escalate to project sponsor
```

### Example 2: Agent Work Tracking

```
Agent-Specific Tracking:
- Last output date: [date]
- Output quality check: [pass/needs revision]
- Token budget used: [amount]
- Context still valid: [yes/no]

Agent Blocker Flags:
- Requirements unclear → Request human clarification
- Conflicting constraints → Flag for PM decision
- Missing required input → Request from owner
```

## Common Pitfalls

### Pitfall 1: Status as Ritual
**Symptom:** Tracking becomes a checkbox exercise without driving decisions.

**Consequence:** Team ignores tracking, issues emerge too late.

**Fix:** Ensure each status category has an associated action or escalation.

### Pitfall 2: No Standard Blocker Format
**Symptom:** Blockers reported informally ("we're blocked on X").

**Consequence:** Can't prioritize unblocking, same blockers repeat.

**Fix:** Require category, owner, resolution path, and ETA for each blocker.

### Pitfall 3: Never Replanning
**Symptom:** Original plan is treated as commitment despite changing circumstances.

**Consequence:** Team chases impossible goals, morale drops.

**Fix:** Define explicit replanning triggers (e.g., "if >20% over estimate").

### Pitfall 4: Tracking Too Frequently
**Symptom:** Daily standups for long-term projects.

**Consequence:** Tracking becomes overhead, team resents the process.

**Fix:** Match cadence to project type (weekly for multi-week projects, bi-weekly for quarters).

## References

### Related Skills
- `skills/task-delegation-planner/SKILL.md` — Define delegated tasks
- `skills/roadmap-orchestrator/SKILL.md` — Coordinate roadmap-level tracking
- `skills/rapid-iteration-cycle/SKILL.md` — Short-cycle execution with frequent replanning

### External Resources
- "Speed Is Strategy" — Lean operating cadence philosophy
- AOR Board — Visual tracking methodologies
- Agile standup practices — Effective daily/weekly sync formats
