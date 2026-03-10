---
name: prd-coverage-checker
description: Use when a draft PRD may have gaps and you need to check scope, dependencies, metrics, edge cases, and execution readiness.
title: PRD Coverage Checker
type: interactive
tier: core
pack: prd-scope
brand_mode: off
public_safe: false
best_for:
  - PMs writing specs under time pressure
  - Teams trying to improve review quality
outputs:
  - Recommendation
  - Top issues or gaps
  - Next-step plan
  - Review checklist
xpm_dimension:
  - execution
xpm_rules:
  - define_problem_first
  - define_success_before_shipping
  - artifacts_are_outputs
---

# What you get

- Recommendation
- Top issues or gaps
- Next-step plan
- Review checklist

# Common failure

Most teams start drafting too early. This skill slows down the right part of the work, speeds up the expensive part, and helps the AI produce something a PM can actually review.

# Best for

- PMs writing specs under time pressure
- Teams trying to improve review quality

# 3–5 key questions

1. What product or feature is this for?
2. Who is the primary user?
3. What outcome matters most?
4. What is out of scope or constrained?

# Working logic

1. Clarify the job-to-be-done.
2. Reduce ambiguity before adding detail.
3. Make trade-offs, evidence quality, and open risks explicit.
4. Produce a review-ready artifact instead of a loose brainstorm.
5. Recommend the shortest useful next step.

# Output format

- A short recommendation or draft tailored to the task
- The critical gaps or risks
- A review checklist
- Suggested next skills to call

# Review checklist

- Does the output make the problem, user, and desired outcome explicit?
- Are trade-offs, assumptions, and risks visible instead of hidden?
- Is the artifact concrete enough for a PM, engineer, or stakeholder to review?
- Is there a clear next step instead of generic advice?

# Next skill

- success-metric-spec-writer
- release-readiness-check

# Notes

Scan a PRD for missing logic, missing sections, and weak review readiness.
