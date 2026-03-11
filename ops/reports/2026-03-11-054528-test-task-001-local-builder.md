# Execution Report: Test Task - Verify Local Worker

## Status
- agent: local_builder
- adapter_type: claude_local
- status: failed
- duration_seconds: 35.16

## Summary
Local worker crashed: 9 validation errors for AgentExecution
response.is_error
  Input should be a valid string [type=string_type, input_value=False, input_type=bool]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
response.duration_ms
  Input should be a valid string [type=string_type, input_value=33581, input_type=int]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
response.duration_api_ms
  Input should be a valid string [type=string_type, input_value=32657, input_type=int]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
response.num_turns
  Input should be a valid string [type=string_type, input_value=10, input_type=int]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
response.total_cost_usd
  Input should be a valid string [type=string_type, input_value=0.14499300000000004, input_type=float]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
response.usage
  Input should be a valid string [type=string_type, input_value={'input_tokens': 15326, '...[], 'speed': 'standard'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
response.modelUsage
  Input should be a valid string [type=string_type, input_value={'MiniMax-M2.5': {'inputT...axOutputTokens': 32000}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
response.permission_denials
  Input should be a valid string [type=string_type, input_value=[], input_type=list]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
response.structured_output
  Input should be a valid string [type=string_type, input_value={'report_path': 'ops/repo...directory is writable.'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

## Verification
worker exception

## Task
- envelope_id: test-envelope-001
- task_id: test-task-001
- objective: Verify that the local worker can execute tasks using Claude Code
- context_bundle_ref: ops/context_bundles/test-context-001.json
- artifact_output_path: 

## Agent Stdout
```text
(empty)
```

## Agent Stderr
```text
9 validation errors for AgentExecution
response.is_error
  Input should be a valid string [type=string_type, input_value=False, input_type=bool]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
response.duration_ms
  Input should be a valid string [type=string_type, input_value=33581, input_type=int]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
response.duration_api_ms
  Input should be a valid string [type=string_type, input_value=32657, input_type=int]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
response.num_turns
  Input should be a valid string [type=string_type, input_value=10, input_type=int]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
response.total_cost_usd
  Input should be a valid string [type=string_type, input_value=0.14499300000000004, input_type=float]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
response.usage
  Input should be a valid string [type=string_type, input_value={'input_tokens': 15326, '...[], 'speed': 'standard'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
response.modelUsage
  Input should be a valid string [type=string_type, input_value={'MiniMax-M2.5': {'inputT...axOutputTokens': 32000}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
response.permission_denials
  Input should be a valid string [type=string_type, input_value=[], input_type=list]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
response.structured_output
  Input should be a valid string [type=string_type, input_value={'report_path': 'ops/repo...directory is writable.'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
```
