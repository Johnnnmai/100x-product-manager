# Codex Paperclip Swarm Design

## Goal

Use local Paperclip as the control plane, promote Codex to the primary CEO lane, keep Claude as the planning and cleanup lane, and retain OpenClaw as the cloud execution swarm.

## Control Model

- Paperclip is the source of truth for company, agents, issues, approvals, and heartbeats.
- Git and `ops/` remain the durable execution surface for reports, context bundles, and artifacts.
- Discord stays notification-first in phase one.

## Local Lanes

- `CTRL-01 / Codex CEO` (`ceo`): routes work, keeps the loop moving, and owns closure.
- `PLAN-01 / PM Compiler` (`pm_compiler`): compiles strategy into bounded execution.
- `BUILD-01 / Codex Builder` (`local_builder`): fast implementation and runtime fixes.
- `BUILD-02 / Claude Builder` (`local_claude_builder`): cleanup, docs, tests, and bounded Claude execution.

## Cloud Lanes

- `ENG-01 / CTO Core`
- `QA-01 / Quality Director`
- `RSR-01 / Research Lead`
- `GTM-01 / Growth Lead`
- `CLOUD-BUILD-01 / Atlas`
- `CLOUD-VERIFY-01 / Sentinel`
- `CLOUD-RESEARCH-01 / Scout`

All cloud lanes stay on `openclaw_gateway`.

## Runtime

- Local Paperclip heartbeats are driven by a long-running swarm supervisor.
- The supervisor invokes `paperclipai heartbeat run` for local lanes.
- Each lane writes heartbeat state into `ops/paperclip/heartbeat/`.
- The latest supervisor snapshot is written to `ops/reports/paperclip-swarm-latest.json`.
- When Codex rate limits appear, the supervisor backs off and retries later instead of stopping the whole swarm.

## Project Structure

Two Paperclip projects drive the system:

1. `Internal AI OS v1`
2. `AI Revenue Flywheel`

The first project bootstraps the control plane. The second uses it to run the business flywheel.
