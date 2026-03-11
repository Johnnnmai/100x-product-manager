# AI OS Troubleshooting Guide

This guide covers common issues and solutions for the AI OS Agent Team & Swarm system.

## Common Issues

### 1. Import Errors

**Symptom**: `ModuleNotFoundError: No module named 'ai_os'`

**Solution**:
```bash
# Install the package in development mode
pip install -e .

# Or add the project to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### 2. Local Worker Issues

#### Task Not Found

**Symptom**: `Status: no_task`

**Cause**: Task discovery filter doesn't match

**Solution**:
- Check that task file exists in `ops/tasks/pending/`
- Ensure `executor_type` in TaskEnvelope matches agent configuration
- Verify file naming follows convention: `{initiative_id}-{epic_id}-{task_id}.md`

```python
# Verify executor type match
from ai_os.contracts import ExecutorType

# Task envelope should use matching executor
envelope = TaskEnvelope(
    executor_type=ExecutorType.claude_code,  # matches local_builder
    ...
)
```

#### Claude Code Nested Session

**Symptom**: `Error: Claude Code cannot be launched inside another Claude Code session`

**Cause**: Running Claude Code within a Claude Code session

**Solution**:
- This is expected behavior - use dry-run mode for testing
- For production execution, run from terminal outside Claude Code

```python
# Use dry-run for testing
result = run_local_worker_once(
    repo_root=Path('.'),
    agent_key='local_builder',
    dry_run=True  # Test without actual execution
)
```

### 3. Test Failures

#### Fixture Issues

**Symptom**: Tests fail with fixture errors

**Solution**:
```bash
# Clear pytest cache
rm -rf .pytest_cache __pycache__ tests/__pycache__

# Re-run tests
python -m pytest tests/ -v
```

#### Executor Type Mismatch

**Symptom**: `test_local_worker_dry_run` returns `no_task`

**Cause**: Task envelope uses wrong executor type

**Solution**:
- Ensure TaskEnvelope uses `ExecutorType.codex` for codex_local adapter
- Or use `ExecutorType.claude_code` for claude_local adapter

```python
from ai_os.contracts import ExecutorType

# For local_builder (claude_local)
envelope = TaskEnvelope(executor_type=ExecutorType.claude_code)

# For codex_builder (codex_local)
envelope = TaskEnvelope(executor_type=ExecutorType.codex)
```

### 4. Memory System Issues

#### Index Corruption

**Symptom**: Memory search returns stale results

**Solution**:
```python
# Rebuild memory index
import json
from pathlib import Path

memory_dir = Path('ops/memory')
entries = list(memory_dir.glob('*.json'))

# Rebuild index
index = {"entries": []}
for entry in entries:
    if entry.name != 'index.json':
        data = json.loads(entry.read_text())
        index["entries"].append({
            "entry_id": data.get("entry_id"),
            "type": data.get("type"),
            "tags": data.get("tags", [])
        })

(memory_dir / 'index.json').write_text(json.dumps(index, indent=2))
```

#### Empty Search Results

**Symptom**: `search_memory()` returns no results

**Solution**:
- Check that memory files exist in `ops/memory/`
- Verify the query matches stored entries
- Search is case-insensitive

```python
# Debug: print all entries
from ai_os.memory import get_memory_entries
entries = get_memory_entries(Path('.'), 'lesson')
print(f"Found {len(entries)} entries")
```

### 5. File System Issues

#### Permission Denied

**Symptom**: Cannot write to `ops/` directories

**Solution**:
```bash
# Check directory permissions
ls -la ops/

# Fix permissions (Unix)
chmod -R 755 ops/
```

#### Path Issues (Windows)

**Symptom**: Path separators wrong on Windows

**Solution**:
- Always use `pathlib.Path` for file operations
- Use forward slashes in configuration files

```python
from pathlib import Path

# Good
path = Path('ops') / 'tasks' / 'pending'

# Bad (avoid)
path = 'ops\\tasks\\pending'
```

### 6. Configuration Issues

#### Agent Fleet Not Loading

**Symptom**: `agent_fleet.yaml` not found

**Solution**:
```python
# Verify config file exists
from pathlib import Path
config_path = Path('paperclip/agent_fleet.yaml')
print(f"Config exists: {config_path.exists()}")

# Reload configuration
from ai_os.agent_fleet import resolve_fleet
fleet = resolve_fleet(Path('.'))
```

#### Company Portfolio Issues

**Symptom**: Portfolio not loading correctly

**Solution**:
- Check YAML syntax in `paperclip/company_portfolio.yaml`
- Verify project names match expected format

```bash
# Validate YAML
python -c "import yaml; yaml.safe_load(open('paperclip/company_portfolio.yaml'))"
```

### 7. Discord Bridge Issues

**Symptom**: Discord messages not sending

**Solution**:
- Check `.env` has valid Discord bot token
- Verify bot has required permissions
- Check Discord gateway is accessible

```python
# Test Discord connection
from ai_os.discord_bridge import DiscordBridge
bridge = DiscordBridge()
# Check connection status
```

### 8. Evidence Worker Issues

#### Scrapling Not Available

**Symptom**: `ModuleNotFoundError: No module named 'scrapling'`

**Solution**:
```bash
pip install scrapling
```

#### URL Fetch Failed

**Symptom**: Evidence collection fails

**Solution**:
- Check URL is accessible
- Verify network connection
- Some sites may block scraping - use alternative sources

## Debugging Tips

### Enable Verbose Logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check System State

```bash
# View pending tasks
ls ops/tasks/pending/

# View running tasks
ls ops/tasks/running/

# View completed reports
ls ops/reports/
```

### Test Individual Components

```python
# Test PM Compiler
from ai_os.pm_compiler import compile_pm_spec
from ai_os.contracts import PMSpec

# Test Local Worker
from ai_os.local_worker import run_local_worker_once

# Test Memory
from ai_os.memory import get_memory_entries

# Test Agent Fleet
from ai_os.agent_fleet import resolve_fleet
```

## Performance Issues

### Slow Task Execution

**Possible Causes**:
1. Network latency for cloud agents
2. Large context bundles
3. Complex tasks

**Solutions**:
- Use local execution when possible
- Minimize context bundle size
- Break complex tasks into smaller ones

### Memory Leaks

**Symptom**: System slows down over time

**Solution**:
- Clear `ops/tasks/done/` periodically
- Restart worker processes
- Monitor disk space

## Getting Help

### Run Full Test Suite

```bash
python -m pytest tests/ -v
```

All tests should pass (105 tests currently).

### Check Git Status

```bash
git status
git diff
```

### Review Recent Commits

```bash
git log --oneline -10
```

### Check Activity Log

See `activity.md` for recent changes and fixes.

## Known Limitations

1. **Nested Sessions**: Claude Code cannot run within Claude Code - use dry-run
2. **Local Execution Only**: Paperclip not used - all execution via Claude Code/Codex
3. **Windows Path Handling**: Use pathlib for cross-platform compatibility

## Error Codes

| Code | Meaning |
|------|---------|
| `no_task` | No pending task matches filter |
| `succeeded` | Task completed successfully |
| `failed` | Task failed during execution |
| `pending` | Task waiting for approval |
| `blocked` | Task blocked by dependency |
