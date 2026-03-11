# AI OS User Guide

This guide explains how to use the AI OS Agent Team & Swarm system for local execution.

## System Overview

AI OS is a local-first agent orchestration system that uses Claude Code or Codex for task execution.

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   PM Spec   │────▶│ PM Compiler  │────▶│TaskEnvelope│
└─────────────┘     └──────────────┘     └─────────────┘
                                                   │
                                                   ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Report    │◀────│Local Worker  │◀────│  Context    │
└─────────────┘     └──────────────┘     └─────────────┘
```

## Quick Start

### 1. Prerequisites

- Python 3.10+
- Claude Code or Codex installed
- Git for version control

### 2. Installation

```bash
# Clone the repository
git clone <your-repo>
cd <your-repo>

# Install dependencies
pip install -e .
```

### 3. Running a Simple Task

```bash
# Run the local worker
python -m ai_os.local_worker --help

# Dry-run test
python -c "from ai_os.local_worker import run_local_worker_once; from pathlib import Path; r = run_local_worker_once(Path('.'), 'local_builder', dry_run=True)"
```

## Core Components

### PM Compiler

Compiles Product Manager specifications into executable TaskEnvelopes.

```python
from ai_os.pm_compiler import compile_pm_spec
from ai_os.contracts import PMSpec, PMEpic, PMTask

# Create a PM spec
spec = PMSpec(
    goal_id='my-goal',
    mission='Build a landing page',
    initiative_id='my-initiative',
    initiative_title='My Project',
    epics=[
        PMEpic(
            epic_id='epic-001',
            title='Landing Page',
            tasks=[
                PMTask(
                    task_id='task-001',
                    title='Design hero section',
                    description='Create hero section with CTA'
                )
            ]
        )
    ]
)

# Compile to TaskEnvelope
result = compile_pm_spec(spec, Path('.'))
```

### Local Worker

Executes tasks using Claude Code or Codex.

```python
from ai_os.local_worker import run_local_worker_once
from pathlib import Path

# Execute a task
result = run_local_worker_once(
    repo_root=Path('.'),
    agent_key='local_builder',
    dry_run=False
)
```

### Context Hub

Manages bounded context compilation for agents.

```python
from ai_os.context_hub import compile_context_bundle

# Compile context for a task
context = compile_context_bundle(
    repo_root=Path('.'),
    task_envelope=envelope
)
```

### Evidence Worker

Collects evidence using Scrapling.

```python
from ai_os.evidence_worker import ingest_url

# Collect evidence from a URL
result = ingest_url(
    url='https://example.com',
    repo_root=Path('.'),
    task_id='task-001'
)
```

### Memory System

Stores organizational memory and lessons learned.

```python
from ai_os.memory import record_lesson_learned, search_memory
from pathlib import Path

# Record a lesson
entry = record_lesson_learned(
    repo_root=Path('.'),
    title='Task failed due to missing context',
    content='Always include context bundle with tasks'
)

# Search memory
results = search_memory(
    repo_root=Path('.'),
    query='context'
)
```

## Agent Team Roles

| Role | Description |
|------|-------------|
| Architect | System design, component architecture |
| Implementer | Code implementation, skill creation |
| Reviewer | Code review, quality check |
| Tester | Unit tests, E2E tests, validation |
| Challenge | Questions assumptions, stress-tests |
| Integrator | Ensures components work together |

## Revenue Flywheel

The system implements a 10-stage revenue flywheel:

```
Signal → Offer → Asset → Content → Distribution → Funnel → Sales → Retention → Analytics → Memory → (back to Signal)
```

### Available Skills

| Skill | Path | Description |
|-------|------|-------------|
| Trend Scout | `skills/flywheel/signal/trend-scout/` | Trend detection |
| Offer Architect | `skills/flywheel/offer/offer-architect/` | Product design |
| Ebook Factory | `skills/flywheel/asset/ebook-factory/` | Digital asset creation |
| Content Factory | `skills/flywheel/content/content-factory/` | Content generation |
| Landing Page | `skills/flywheel/sales/landing-page-generator/` | Page generation |
| Experiment Tracker | `skills/flywheel/analytics/experiment-tracker/` | A/B testing |

## CLI Commands

### Run Local Worker

```bash
# Dry-run mode
python -m ai_os.cli worker --dry-run

# Execute tasks
python -m ai_os.cli worker --agent local_builder
```

### Run Tests

```bash
# All tests
python -m pytest tests/ -v

# Specific test file
python -m pytest tests/test_local_worker.py -v

# E2E tests
python -m pytest tests/e2e/ -v
```

### Memory Operations

```bash
# Add lesson
python -c "from ai_os.memory import record_lesson_learned; from pathlib import Path; record_lesson_learned(Path('.'), 'title', 'content')"

# Search memory
python -c "from ai_os.memory import search_memory; from pathlib import Path; print(search_memory(Path('.'), 'query'))"
```

## Configuration

### Agent Fleet Configuration

Located at `paperclip/agent_fleet.yaml`:

```yaml
agents:
  local_builder:
    adapter_type: claude_local
    command: claude
    ready: true
```

### Company Portfolio

Located at `paperclip/company_portfolio.yaml`:

```yaml
company: YourCompany
projects:
  - name: project-name
    workspace: workspace-id
```

## File Structure

```
.
├── ai_os/                    # Core modules
│   ├── local_worker.py      # Local execution engine
│   ├── pm_compiler.py       # PM spec compiler
│   ├── context_hub.py       # Context management
│   ├── evidence_worker.py   # Evidence collection
│   ├── memory.py            # Memory system
│   ├── swarm_orchestrator.py # Agent swarm
│   └── challenge_agent.py   # Adversarial testing
├── ops/                      # Operational directories
│   ├── tasks/               # Task queue
│   ├── context_bundles/     # Compiled contexts
│   ├── evidence/           # Collected evidence
│   ├── memory/              # Stored memories
│   └── reports/            # Execution reports
├── skills/                  # Agent skills
│   └── flywheel/           # Revenue flywheel skills
├── paperclip/               # Configuration
│   ├── agent_fleet.yaml    # Agent definitions
│   └── company_portfolio.yaml # Project definitions
└── tests/                   # Test suite
```

## Best Practices

1. **Always use dry-run first** - Test task flow before execution
2. **Include context bundles** - Always provide context to agents
3. **Record lessons learned** - Build organizational memory
4. **Run tests regularly** - Use `pytest tests/ -v`
5. **Use meaningful task IDs** - Follow naming conventions

## Common Workflows

### Creating a New Task

1. Write PM spec in `ops/tasks/pending/`
2. Run PM Compiler to generate TaskEnvelope
3. Local Worker picks up pending task
4. Execution generates report in `ops/reports/`
5. Task moved to `ops/tasks/done/`

### Running E2E Tests

```bash
# Run complete test suite
python -m pytest tests/ -v

# Run specific E2E test
python -m pytest tests/e2e/test_flywheel.py -v

# Run with coverage
python -m pytest tests/ --cov=ai_os -v
```

### Debugging Issues

See [AI_OS_TROUBLESHOOTING.md](./AI_OS_TROUBLESHOOTING.md) for common issues and solutions.
