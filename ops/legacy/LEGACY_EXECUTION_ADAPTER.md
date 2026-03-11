# Legacy Execution Adapter

## Purpose

Preserve the current `GitHub -> OpenClaw` worker loop while the new AI OS control plane is layered on top.

## What the Adapter Accepts

The legacy adapter takes a compiled `TaskEnvelope` and emits a markdown task file under `ops/tasks/pending/`.

Required metadata carried forward:

- `goal_id`
- `initiative_id`
- `epic_id`
- `task_id`
- `executor_type`
- `budget_cap`
- `approval_required`
- `context_bundle_ref`
- `artifact_output_path`

## What the Existing Worker Still Does

- Polls `ops/tasks/pending/`
- Moves work to `ops/tasks/running/`
- Executes build, test, deploy, or validation steps
- Writes reports to `ops/reports/`
- Moves finished work to `ops/tasks/done/`

## What the Existing Worker Must Not Do

- Invent new scope outside the task envelope
- Read the entire repo when a `ContextBundle` is supplied
- Bypass approval requirements
- Become the source of truth for roadmap or budget state

## Adapter Outputs

- Markdown task for the current OpenClaw runtime
- `PaperclipRunRequest` JSON for the future control-plane bridge

## Migration Rule

Until Paperclip is fully wired in, every production task should be able to run through both paths:

1. compiled `TaskEnvelope`
2. legacy markdown task generated from that envelope
