# cli-run Decision Pack

- Run ID: `20260312-002531-shape`
- Mode: `shape`
- Created: `2026-03-12T00:25:31.331551+00:00`

## Executive Summary
LightCube analyzed idea input in shape mode and recommends focusing on signal-backed idea shaping into a first buildable scope. The strongest near-term move is to tighten the first convincing use case, reduce time-to-value, and validate repeat behavior before broadening scope.

## Signal Brief
- **Founder idea** (idea_input, confidence=0.55): AI-powered meal planning app for busy professionals

## Problem Map
- Core user and wedge may still be blended together.
- The product may solve too many adjacent jobs at once.
- Distribution logic is not yet tightly bound to the product loop.
- Idea evidence anchors: Founder idea

## Conditional Validation Stack
- L1: Target user enters the core flow | risk: unclear hook | signal: landing page click or signup intent
- L2: User reaches first value within one session | risk: time-to-value too slow | signal: activation event completion
- L3: User repeats the core loop | risk: value too episodic | signal: 7-day repeat behavior
- L4: Users spread or invite naturally | risk: weak social or workflow pull | signal: share or invite rate
- L5: Channel scales without breaking economics | risk: CAC or effort too high | signal: channel conversion and cost

## Strategy Memo
- **target_user**: Founder or PM with a rough idea and no sharp wedge yet
- **wedge**: signal-backed idea shaping into a first buildable scope
- **core_problem**: Core user and wedge may still be blended together.
- **core_flow**: Input context → collect signals → pressure-test direction → compile build plan
- **distribution_hypothesis**: High-signal audits and decision packs can act as both acquisition and trust-building content.
- **business_model**: Subscription with premium strategy runs and optional execution orchestration.
- **evidence_used**: [{'source': 'idea_input', 'title': 'Founder idea', 'summary': 'AI-powered meal planning app for busy professionals', 'confidence': 0.55}]

## PRD
- **title**: cli-run LightCube v1
- **objective**: Turn messy product inputs into decision-ready direction and agent-ready execution.
- **primary_user**: Founder or PM with a rough idea and no sharp wedge yet
- **must_have_features**: ['Input form for URL or idea', 'Decision Pack generation', 'Project run storage', 'Task export for engineering execution']
- **non_goals**: ['Full autonomous company orchestration', 'High-fidelity digital twin visualization', 'Multi-tenant enterprise controls in v1']
- **success_metrics**: ['Time to first decision pack', 'Manual edits after first pack', 'Percent of generated tasks accepted by the team']

## Roadmap
- **0-30 days**: Ship audit and shape workflows | milestones: web form, pack generation, local storage
- **31-60 days**: Close execution loop | milestones: task status tracking, run comparison, team feedback capture
- **61-90 days**: Add advanced simulation | milestones: deeper OASIS scenarios, optional MiroFish forecasting, better evidence connectors

## Tasks
- **Implement intake workflow** [eng/high] Build URL and idea submission flow.
- **Generate Decision Pack** [eng/high] Compile markdown and JSON outputs.
- **Review strategy wedge** [pm/high] Confirm target user and core wedge.
- **Design activation metric** [pm/medium] Define first-value event and success threshold.

## Simulation Summary
- **engine**: local-sim
- **audience_reaction**: curious but selective
- **spread_potential**: medium
- **retention_risk**: high if first value is delayed
- **observed_themes**: ['Founder idea']
- **forecast**: {'engine': 'disabled', 'note': 'Advanced forecasting is optional in v1.', 'priority_scenarios': ['narrow wedge converts strongly', 'broad positioning confuses users', 'distribution fails without a repeatable signal loop']}
