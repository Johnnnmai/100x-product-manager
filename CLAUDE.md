# 100X Product Managers - Claude Guide

## Overview

This repository is a PM skill library for agent-assisted product work.

Use it when the user needs help with:
- product discovery
- prioritization
- PM artifacts like PRDs and user stories
- SaaS metrics, pricing, and business diagnostics
- AI-shaped PM operating systems

## Current Catalog

- 77 skills total
- 31 component skills
- 32 interactive skills
- 14 workflow skills

## Recommended Skill Tracks

### 100X Core
- `market-driven-prioritization`
- `rapid-iteration-cycle`
- `10x-hypothesis-framework`

### Discovery and Strategy
- `discovery-interview-prep`
- `positioning-workshop`
- `opportunity-solution-tree`
- `product-strategy-session`

### Delivery and Execution
- `prd-development`
- `roadmap-planning`
- `user-story`
- `epic-breakdown-advisor`

### Business and Growth
- `business-health-diagnostic`
- `finance-based-pricing-advisor`
- `saas-revenue-growth-metrics`
- `tam-sam-som-calculator`

### AI-Shaped PM Leadership
- `context-engineering-advisor`
- `ai-shaped-readiness-advisor`
- `director-readiness-advisor`
- `vp-cpo-readiness-advisor`

## Core Principles

### 1. Market Evidence Beats Internal Opinion
Default to real demand signals, not stakeholder confidence.

### 2. Speed Is Strategy
Prefer fast validation and short learning loops over large speculative builds.

### 3. 10x Thinking Is About Leverage
Use exponential framing to find leverage, not to avoid execution discipline.

### 4. AI Should Improve PM Judgment, Not Just Output Volume
The best skills in this repo help users make better decisions and create stronger operating systems.

## Working Norms

- Point users to `START_HERE.md` when they do not know which skill to use first.
- Prefer explicit skill paths such as `skills/prd-development/SKILL.md`.
- If the user is unclear, recommend one skill first instead of dumping a long catalog.
- Keep the repo differentiated from generic project-management packs.
- Favor PM + AI execution skills over broad PMO/admin content when expanding the catalog.

## Repo Map

- `skills/` contains the skill library
- `docs/` contains usage guides and launch docs
- `research/` contains source essays and notes
- `app/` contains the Streamlit playground
- `scripts/` contains packaging, validation, and helper utilities

## Quality Expectations

Before shipping changes:
- run `python scripts/check-skill-metadata.py`
- verify install instructions still match the current GitHub repo
- remove stale repo-owner references from user-facing docs
- keep onboarding simple for first-time users
