# 2026-03-10 Company Operating Model Design

## Decision

Adopt a role-based, multi-project Paperclip operating model.

## What Changed

- human-name agent labels were demoted in favor of role-first identities
- the control plane now has a project portfolio spec, not just an agent fleet spec
- RoomJoy is modeled as the first active project, not the whole system
- provisioning now covers agents, projects, workspaces, and seeded issue trees
- core ownership roles were moved to cloud-backed runtimes so the org does not stop when a laptop is offline

## Chosen Structure

### Shared company roles

Cloud core:

- CEO
- Chief of Staff
- CTO
- QA Director
- Research Lead
- Growth Lead

Local fallback:

- Staff Engineer
- Local Codex Builder

### Shared cloud lanes

- Cloud Build
- Cloud QA
- Cloud Research

### Project source of truth

- `paperclip/company_portfolio.yaml`

Each project carries:

- repo/local workspace hints
- background document paths
- role-based issue seeds

## Why This Over The Old Model

The old fleet model was still operator-centric: it assumed someone would remember which named agent to poke.

The new model is organization-centric:

- work is assigned by role
- projects are first-class objects
- launches are repeatable templates
- future products can be added without redesigning the control plane

## First Live Project

RoomJoy is the first project seeded into this architecture because it already has:

- a real product repo
- company background docs
- a credible near-term sales objective

## Provisioning Rule

The repo must be able to do one command that creates or aligns:

1. agents
2. projects
3. workspaces
4. initial issue trees

That command is `scripts/provision_company_portfolio.py`.
