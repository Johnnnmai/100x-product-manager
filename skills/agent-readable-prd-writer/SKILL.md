---
name: agent-readable-prd-writer
description: Use when a PRD must work for both human reviewers and coding agents, with explicit task contracts, constraints, and completion logic.
title: Agent-Readable PRD Writer
type: component
tier: core
pack: prd-scope
brand_mode: off
public_safe: false
best_for:
  - PMs writing PRDs for both human review and agent execution
  - AI product teams that need explicit task contracts
outputs:
  - dual-mode PRD
  - task contract
  - review checklist
xpm_dimension:
  - execution
  - ai_behavior
xpm_rules:
  - define_problem_first
  - define_success_before_shipping
  - prds_for_humans_and_agents
---

# What you get

- dual-mode PRD
- task contract
- review checklist

# Common failure

Traditional PRDs explain intent to humans but leave agents missing constraints, dependencies, and completion logic.

# Best for

- PMs writing PRDs for both human review and agent execution
- AI product teams that need explicit task contracts

# 3-5 key questions

1. What problem and scope are approved?
2. What must the agent do?
3. What constraints and dependencies matter?
4. How is success checked?

# Working logic

1. Keep the human summary concise.
2. Make the agent task contract explicit.
3. Add constraints, dependencies, metrics, and escalation rules.
4. Define the expected output shape.

# Output format

- human-readable summary
- agent-readable task spec
- constraints and dependencies
- success metrics
- fallback or escalation rules

# Review checklist

- Can a human review the intent quickly?
- Can an agent act without guessing hidden rules?
- Are success and escalation conditions explicit?

# Next skill

- prd-coverage-checker
- define-metrics
