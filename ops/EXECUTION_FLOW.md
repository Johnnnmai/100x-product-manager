# Legacy Execution Flow

This document defines the legacy OpenClaw adapter path. The control-plane architecture now lives in `docs/AI_OS_ARCHITECTURE.md`, and the adapter contract lives in `ops/legacy/LEGACY_EXECUTION_ADAPTER.md`.

## Architecture

```text
AI OS compiler -> GitHub-backed task queue -> Cloud OpenClaw worker
```

## Step-by-Step

### 1. Compile and queue the task

Write a structured PM spec, then compile it into:

- `ops/context_bundles/*.json`
- `ops/tasks/compiled/*.json`
- `ops/tasks/pending/*.md` for the legacy worker

### 2. Push to GitHub

```bash
git add ops/tasks/pending/ ops/tasks/compiled/ ops/context_bundles/
git commit -m "Queue task via AI OS legacy adapter"
git push
```

### 3. Cloud OpenClaw polls

- Runs every 30 minutes
- Checks `ops/tasks/pending/`
- Moves the task to `ops/tasks/running/`
- Executes the requested build, test, validation, or delivery work

### 4. Report result

- Writes the execution report to `ops/reports/`
- Moves the task to `ops/tasks/done/`
- Pushes the updated report and task state back to GitHub

## Task States

| State | Location | Description |
| --- | --- | --- |
| Pending | `ops/tasks/pending/` | Waiting to be executed |
| Running | `ops/tasks/running/` | Currently being executed |
| Done | `ops/tasks/done/` | Completed, succeeded, or failed |

## Retry Logic

- If a task fails, write the error to the report and move it to `ops/tasks/done/`.
- Do not retry automatically.
- Requeue only by generating a new `TaskEnvelope` and legacy markdown task.
