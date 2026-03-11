# Execution Report: Test Task - Verify Local Worker

## Status
- agent: local_builder
- adapter_type: claude_local
- status: failed
- duration_seconds: 0.49

## Summary
The local worker finished without a summary.

## Verification
No verification summary supplied.

## Task
- envelope_id: test-envelope-001
- task_id: test-task-001
- objective: Verify that the local worker can execute tasks using Claude Code
- context_bundle_ref: 
- artifact_output_path: 

## Agent Stdout
```text
(empty)
```

## Agent Stderr
```text
Error: Claude Code cannot be launched inside another Claude Code session.
Nested sessions share runtime resources and will crash all active sessions.
To bypass this check, unset the CLAUDECODE environment variable.
```
