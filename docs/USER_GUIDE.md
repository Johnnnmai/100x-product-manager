# AI OS User Guide

## Getting Started

### Prerequisites

- Python 3.11+
- Claude Code (recommended) or Codex
- Git

### Installation

```bash
# Clone the repository
git clone <your-repo>
cd <your-repo>

# Install dependencies
pip install -r requirements.txt
```

### Environment Setup

1. Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

2. Configure your environment variables in `.env`:
```
# Claude Code path (optional, auto-detected)
CLAUDE_CODE_PATH=claude

# Discord webhook (optional)
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
```

## Basic Usage

### Running the Local Worker

The Local Worker is the core execution engine. It discovers pending tasks and executes them using Claude Code.

```bash
# Run a single task (dry-run - no actual execution)
python -c "from ai_os.local_worker import run_local_worker_once; from pathlib import Path; result = run_local_worker_once(Path('.'), 'local_builder', dry_run=True); print(result.status)"

# Run with actual execution
python -c "from ai_os.local_worker import run_local_worker_once; from pathlib import Path; result = run_local_worker_once(Path('.'), 'local_builder', dry_run=False)"
```

### Compiling PM Specifications

The PM Compiler transforms PM specifications into executable task envelopes.

```python
from ai_os.pm_compiler import compile_pm_spec
from ai_os.contracts import PMSpec, PMEpic, PMTask
from pathlib import Path

# Create a PM spec
spec = PMSpec(
    goal_id='goal-001',
    mission='Build a new feature',
    initiative_id='init-001',
    initiative_title='Feature Launch',
    epics=[
        PMEpic(
            epic_id='epic-001',
            title='Backend API',
            description='Build REST API',
            tasks=[
                PMTask(
                    task_id='task-001',
                    title='Create endpoint',
                    description='Create /api/users endpoint'
                )
            ]
        )
    ]
)

# Compile to TaskEnvelope
result = compile_pm_spec(spec, Path('.'))
print(f"Generated {len(result['envelopes'])} tasks")
```

### Using the Context Hub

The Context Hub manages bounded contexts to prevent token overflow.

```python
from ai_os.context_hub import compile_context
from ai_os.contracts import ContextBundle
from pathlib import Path

bundle = ContextBundle(
    context_id='ctx-001',
    tasks=[...],
    evidence_refs=[...],
    memories=[...]
)

compiled = compile_context(bundle, Path('.'))
```

### Collecting Evidence

The Evidence Worker fetches web content for analysis.

```python
from ai_os.evidence_worker import ingest_url
from pathlib import Path

# Fetch and process a URL
result = ingest_url('https://example.com', Path('.'))
print(f"Evidence ID: {result['evidence_id']}")
```

### Memory System

Store and retrieve organizational knowledge.

```python
from ai_os.memory import add_memory_entry, get_memory_entries, search_memory
from pathlib import Path

# Add a lesson learned
entry = add_memory_entry(
    Path('.'),
    category='lesson',
    title='Feature launched successfully',
    content='Launched new feature with 95% success rate'
)

# Search memories
results = search_memory(Path('.'), 'launch')
```

## Running Tests

### All Tests

```bash
python -m pytest tests/ -v
```

### E2E Tests

```bash
python -m pytest tests/e2e/ -v
```

### Specific Test File

```bash
python -m pytest tests/test_local_worker.py -v
```

### Benchmark

```bash
python -m pytest tests/test_benchmark.py -v
```

## CLI Commands

### Task Discovery

```bash
# List pending tasks
python -c "from ai_os.local_worker import discover_tasks; from pathlib import Path; tasks = discover_tasks(Path('.'), 'local_builder'); print(tasks)"
```

### Agent Fleet Status

```bash
# Check available agents
python -c "from ai_os.agent_fleet import resolve_fleet; from pathlib import Path; fleet = resolve_fleet(Path('.')); print([a.key for a in fleet])"
```

## Workflows

### Creating a New Task

1. Create a PM specification in `ops/tasks/pending/`
2. Run the PM Compiler to generate TaskEnvelope
3. Local Worker discovers and executes the task
4. Results written to `ops/reports/`

### Revenue Flywheel

To run a complete revenue flywheel:

```python
from ai_os.local_worker import run_local_worker_once
from pathlib import Path

# Execute each flywheel stage
stages = ['signal', 'offer', 'asset', 'content', 'distribution', 'funnel', 'sales']

for stage in stages:
    result = run_local_worker_once(Path('.'), 'local_builder', dry_run=True)
    print(f"{stage}: {result.status}")
```

## Configuration

### Agent Fleet Configuration

Edit `paperclip/agent_fleet.yaml` to configure agents:

```yaml
agents:
  - key: local_builder
    display_name: Local Claude Builder
    adapter_type: claude_local
    command: claude
    ready: true
```

### Company Portfolio

Edit `paperclip/company_portfolio.yaml` to configure projects:

```yaml
company: YourCompany
projects:
  - name: Project Name
    workspace: project-workspace
```

## Advanced Usage

### Swarm Orchestration

```python
from ai_os.swarm_orchestrator import SwarmOrchestrator
from pathlib import Path

orchestrator = SwarmOrchestrator(Path('.'))

# Execute tasks in parallel
results = orchestrator.execute_parallel(tasks, agents)
```

### Challenge Agent

```python
from ai_os.challenge_agent import create_challenge_report

# Create a challenge report
report = create_challenge_report(
    title='Performance concerns',
    issues=['Slow query', 'Memory leak']
)
```

### Benchmarking

```python
from ai_os.benchmark import Benchmark

benchmark = Benchmark()
results = benchmark.run_swarm_orchestrator_benchmark(iterations=100)
print(f"Average: {results.avg_ms:.2f}ms")
```

## Troubleshooting

See [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) for common issues and solutions.
