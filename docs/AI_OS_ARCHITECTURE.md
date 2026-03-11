# AI OS Architecture v5

## Overview

AI OS is a local-first Agent Operating System that orchestrates multiple AI agents to execute product development workflows. This version (v5) uses Claude Code / Codex for local execution instead of Paperclip.

## Core Design Principles

1. **Local Execution First**: Use Claude Code / Codex running on the local machine
2. **GitHub as Persistence**: All code, tasks, and reports stored in Git
3. **Discord as Approval Layer**: Optional integration for human-in-the-loop approvals
4. **Bounded Contexts**: Each task has limited context to prevent token overflow

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        AI OS Core                               │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│  │   CLI       │  │   Web       │  │   Discord Bridge        │ │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────┐│
│  │              Agent Fleet Manager                            ││
│  │  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐  ││
│  │  │ Architect │ │Implementer│ │ Reviewer  │ │  Tester   │  ││
│  │  └───────────┘ └───────────┘ └───────────┘ └───────────┘  ││
│  │  ┌───────────┐ ┌───────────┐                               ││
│  │  │ Challenge │ │Integrator │                               ││
│  │  └───────────┘ └───────────┘                               ││
│  └─────────────────────────────────────────────────────────────┘│
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│  │ Local Worker│  │PM Compiler  │  │  Context Hub             │ │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘ │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│  │  Evidence  │  │  Challenge  │  │  Swarm Orchestrator     │ │
│  │   Worker   │  │   Agent     │  │                         │ │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘ │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│  │    Memory   │  │   Benchmark │  │  Strategy Lab           │ │
│  │   System    │  │             │  │                         │ │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Execution Layer                              │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐        ┌─────────────────────────────────┐ │
│  │ Claude Code     │        │   GitHub (Persistence)         │ │
│  │ (claude local)  │        │   - Code repository             │ │
│  └─────────────────┘        │   - Task tracking               │ │
│  ┌─────────────────┐        │   - Reports                    │ │
│  │ Codex           │        └─────────────────────────────────┘ │
│  │ (codex local)   │                                           │
│  └─────────────────┘                                           │
└─────────────────────────────────────────────────────────────────┘
```

## Core Modules

### 1. Agent Fleet (`ai_os/agent_fleet.py`)
Manages the pool of available agents and their capabilities.

**Key Functions:**
- `resolve_fleet(repo_root)` - Load and resolve agent fleet configuration
- `get_agent(key)` - Get a specific agent by key

### 2. Local Worker (`ai_os/local_worker.py`)
Executes tasks using Claude Code or Codex locally.

**Key Functions:**
- `run_local_worker_once(repo_root, agent_key, dry_run=False)` - Execute a single task
- `discover_tasks(repo_root, agent_key)` - Find pending tasks for an agent

### 3. PM Compiler (`ai_os/pm_compiler.py`)
Compiles PM specifications into executable task envelopes.

**Key Functions:**
- `compile_pm_spec(spec, repo_root)` - Compile PMSpec to TaskEnvelope

### 4. Context Hub (`ai_os/context_hub.py`)
Manages bounded contexts for task execution.

**Key Functions:**
- `compile_context(bundle)` - Compile context bundle

### 5. Evidence Worker (`ai_os/evidence_worker.py`)
Collects evidence from web sources using Scrapling.

**Key Functions:**
- `ingest_url(url)` - Fetch and process web evidence

### 6. Swarm Orchestrator (`ai_os/swarm_orchestrator.py`)
Coordinates multiple agents working in parallel.

**Key Functions:**
- `execute_parallel(tasks, agents)` - Execute tasks in parallel
- `manage_dependencies(task_graph)` - Manage task dependencies

### 7. Memory System (`ai_os/memory.py`, `ai_os/memory_system.py`)
Stores organizational knowledge and lessons learned.

**Key Functions:**
- `add_memory_entry(entry)` - Add a memory entry
- `search_memory(query)` - Search memory
- `get_signal_accuracy()` - Get signal detection accuracy

### 8. Challenge Agent (`ai_os/challenge.py`, `ai_os/challenge_agent.py`)
Provides adversarial testing and质疑假设.

**Key Functions:**
- `create_challenge_report(title, issues)` - Create challenge report
- `design_stress_test(scenario)` - Design stress test scenarios

### 9. Benchmark (`ai_os/benchmark.py`)
Performance benchmarking for the system.

**Key Functions:**
- `run_benchmark(component, iterations)` - Run performance benchmark

## Agent Team Roles

| Role | Purpose | Location |
|------|---------|----------|
| **Architect** | System design, component architecture | `ai_os/agents/team/ARCHITECT.md` |
| **Implementer** | Code implementation, skill creation | `ai_os/agents/team/IMPLEMENTER.md` |
| **Reviewer** | Code review, quality check | `ai_os/agents/team/REVIEWER.md` |
| **Tester** | Unit tests, E2E tests, validation | `ai_os/agents/team/TESTER.md` |
| **Challenge** | Questions assumptions, stress-tests | `ai_os/agents/team/CHALLENGE.md` |
| **Integrator** | Ensures components work together | `ai_os/agents/team/INTEGRATOR.md` |

## AI Revenue Flywheel

The system implements a 10-step revenue flywheel:

```
Signal (趋势信号) → Offer (产品供给) → Asset (交付资产) → Content (内容拆分)
    ↓
Distribution (渠道投放) → Funnel (引流转化) → Sales (成交)
    ↓
Retention (复购/升级) → Analytics (归因+实验) → Memory (经验沉淀)
    ↓
Signal (更强的趋势信号) → ...
```

### Skills

- **signal/trend-scout** - Trend signal identification
- **offer/offer-architect** - Product offering design
- **asset/ebook-factory** - Digital asset creation
- **content/content-factory** - Content factory
- **distribution/channel-distributor** - Channel distribution
- **sales/landing-page-generator** - Landing page generation
- **analytics/experiment-tracker** - Experiment tracking
- **memory/organization-memory** - Organizational memory

## Configuration Files

| File | Purpose |
|------|---------|
| `paperclip/agent_fleet.yaml` | Agent definitions and capabilities |
| `paperclip/company_portfolio.yaml` | Project definitions |
| `.env` | Environment variables (not committed) |

## Operations Directories

| Directory | Purpose |
|-----------|---------|
| `ops/tasks/pending/` | Tasks waiting to be executed |
| `ops/tasks/running/` | Tasks currently being executed |
| `ops/tasks/done/` | Completed tasks |
| `ops/context_bundles/` | Compiled context bundles |
| `ops/evidence/` | Collected evidence |
| `ops/reports/` | Execution reports |
| `ops/memory/` | Organizational memory |
| `ops/approvals/` | Approval workflow |

## Testing

```bash
# Run all tests
python -m pytest tests/ -v

# Run E2E tests
python -m pytest tests/e2e/ -v

# Run benchmark
python -c "from ai_os.benchmark import run_benchmark; run_benchmark()"
```

## Execution Flow

1. **Task Creation**: PM spec compiled to TaskEnvelope
2. **Task Discovery**: Local Worker finds pending tasks
3. **Task Execution**: Claude Code/Codex executes the task
4. **Report Generation**: Results written to ops/reports/
5. **Verification**: Reviewer/Challenge Agent validates results
6. **Memory Update**: Lessons learned stored in memory system
