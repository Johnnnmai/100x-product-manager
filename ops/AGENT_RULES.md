# Legacy Agent Rules - OpenClaw

These rules apply to the existing OpenClaw worker while AI OS v1 is being layered on top.

## Core Principles

- No SSH-based command passing.
- Pull-based execution only.
- Task envelopes own intent; the worker executes, it does not redefine scope.

## Task Flow

1. AI OS tooling compiles a PM spec into a `TaskEnvelope`.
2. The legacy adapter writes the markdown task to `ops/tasks/pending/`.
3. Cloud OpenClaw polls, claims the task, executes it, and writes a report to `ops/reports/`.

## What OpenClaw Should Do

- Build with the repo's standard install and build commands
- Run tests and smoke checks needed for the queued task
- Capture screenshots or artifacts when the task requires proof
- Write an execution report with status, duration, and errors

## What OpenClaw Must Not Do

- Wait for SSH commands
- Redefine task requirements
- Make product or prioritization decisions
- Bypass approval requirements encoded in the task envelope

## Communication

- All execution outputs go to `ops/reports/`
- Report format remains `YYYY-MM-DD-HHMMSS-{task-name}.md`
- Reports should include status, duration, errors, screenshots, and artifact references when available
