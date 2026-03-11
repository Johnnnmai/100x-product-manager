# AI OS Troubleshooting Guide

## Common Issues and Solutions

### Local Worker Issues

#### Issue: "no_task" status returned

**Symptoms:**
- Local worker returns `no_task` status instead of executing a task

**Causes:**
- Task discovery filtering by executor type mismatch
- No pending tasks in `ops/tasks/pending/`
- Task filename format mismatch

**Solutions:**
1. Check pending tasks exist:
   ```bash
   ls ops/tasks/pending/
   ```

2. Verify task envelope format matches expected:
   - Expected: `{initiative_id}-{epic_id}-{task_id}.json`
   - Example: `test-initiative-test-epic-001-test-task-001.json`

3. Check executor type in TaskEnvelope matches agent configuration:
   ```python
   from ai_os.contracts import ExecutorType
   # TaskEnvelope should use ExecutorType.claude_code
   ```

#### Issue: Claude Code execution fails

**Symptoms:**
- Error: "Claude Code cannot be launched inside another Claude Code session"

**Cause:**
- Running Claude Code from within a Claude Code session

**Solutions:**
1. Use `dry_run=True` for testing inside Claude Code sessions
2. Run the worker from a regular terminal outside Claude Code

### Import Errors

#### Issue: ModuleNotFoundError

**Symptoms:**
- `ModuleNotFoundError: No module named 'ai_os'`

**Solutions:**
```bash
# Ensure you're in the project root
cd <project-directory>

# Add to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

#### Issue: Pydantic validation errors

**Symptoms:**
- `ValidationError` when creating TaskEnvelope or other contracts

**Solutions:**
1. Check all required fields are present
2. Verify field types match contract definitions
3. See `docs/ai_os/TaskEnvelope_Schema.md` for required fields

### Memory System Issues

#### Issue: Memory entries not persisted

**Symptoms:**
- Memory entries disappear after restart

**Solutions:**
1. Check `ops/memory/` directory exists
2. Verify write permissions
3. Check `ops/memory/index.json` is being updated

### Test Failures

#### Issue: Test fixtures failing

**Symptoms:**
- Tests fail with fixture errors

**Solutions:**
```bash
# Run tests with verbose output
python -m pytest tests/ -v --tb=long

# Run specific failing test
python -m pytest tests/test_local_worker.py::test_name -v
```

#### Issue: All tests pass but functionality doesn't work

**Symptoms:**
- Tests pass but actual execution fails

**Solutions:**
1. Check environment variables are set correctly
2. Verify Claude Code/Codex is installed and in PATH
3. Use dry-run mode to debug

### Agent Fleet Issues

#### Issue: Agent not ready

**Symptoms:**
- Agent shows `ready: false` in fleet status

**Solutions:**
1. Check agent configuration in `paperclip/agent_fleet.yaml`
2. Verify the command executable exists:
   ```bash
   which claude  # or codex
   ```
3. Check agent bootstrap files exist in `paperclip/bootstrap/`

### Swarm Orchestrator Issues

#### Issue: Tasks not executing in parallel

**Symptoms:**
- Tasks execute sequentially instead of in parallel

**Solutions:**
1. Verify tasks have no dependencies
2. Check `parallel=True` parameter
3. Review task graph for hidden dependencies

### Performance Issues

#### Issue: Slow execution

**Symptoms:**
- Task execution takes longer than expected

**Solutions:**
1. Run benchmark to measure:
   ```bash
   python -m pytest tests/test_benchmark.py -v
   ```
2. Check context size - reduce bounded context
3. Verify no blocking I/O operations

### Discord Integration Issues

#### Issue: Webhook not working

**Symptoms:**
- Discord notifications not sent

**Solutions:**
1. Verify webhook URL is set in `.env`
2. Check Discord permissions for webhook
3. Test webhook manually:
   ```bash
   curl -X POST <webhook-url> -d "content=test"
   ```

### Data Consistency Issues

#### Issue: Task stuck in "running" state

**Symptoms:**
- Task in `ops/tasks/running/` but never moves to "done"

**Solutions:**
1. Check for orphaned process
2. Manually move task file to `ops/tasks/done/`
3. Check execution logs in `ops/reports/`

### File System Issues

#### Issue: Permission denied

**Symptoms:**
- `PermissionError` when writing files

**Solutions:**
1. Check file permissions on `ops/` directory
2. Verify directory exists:
   ```bash
   mkdir -p ops/tasks/{pending,running,done}
   mkdir -p ops/reports
   mkdir -p ops/memory
   ```

## Debugging Tips

### Enable Verbose Logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check System State

```bash
# List all tasks
ls -la ops/tasks/*/

# Check memory index
cat ops/memory/index.json

# View recent reports
ls -lt ops/reports/ | head -10
```

### Test Individual Components

```python
# Test agent fleet
python -c "from ai_os.agent_fleet import resolve_fleet; from pathlib import Path; print([(a.key, a.ready) for a in resolve_fleet(Path('.'))])"

# Test memory
python -c "from ai_os.memory import add_memory_entry; from pathlib import Path; print(add_memory_entry(Path('.'), 'test', 'test', 'test'))"

# Test context
python -c "from ai_os.context_hub import compile_context; print('OK')"
```

## Getting Help

If you encounter issues not covered here:

1. Check the test files for usage examples
2. Review `docs/USER_GUIDE.md` for correct usage
3. Check `activity.md` for recent fixes and changes
4. Run the test suite to verify system integrity:
   ```bash
   python -m pytest tests/ -v
   ```
