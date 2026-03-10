---
name: token-budget-optimizer
description: Use when agent quality is degrading under long context and you need a keep/compress/archive strategy plus escalation rules.
title: Token Budget Optimizer
type: component
tier: core
pack: metrics-experimentation
brand_mode: off
public_safe: false
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

# What you get

- context budget strategy
- keep/compress/archive plan
- escalation rules

# Common failure

Teams keep stuffing more context into prompts instead of deciding what must stay active, what can be compressed, and what belongs in memory.

# Best for

- teams improving output quality on smaller or cheaper models
- agents working across long product workflows

# 3-5 key questions

1. What must remain in active context?
2. What can be summarized?
3. What belongs in memory or reference docs?
4. What requires escalation to a stronger model or a human?

# Working logic

1. Separate active context from reference context.
2. Compress aggressively when the same material repeats.
3. Define when to escalate instead of silently degrading output.

# Output format

- keep now
- compress now
- move to memory
- escalate if

# Review checklist

- Is active context minimal and high signal?
- Are summaries replacing repetition?
- Are escalation rules explicit?

# Next skill

- agent-readable-prd-writer
- design-eval
