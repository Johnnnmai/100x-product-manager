"""End-to-end tests for the AI OS Flywheel."""

import pytest
import json
from pathlib import Path
import tempfile
import shutil

from ai_os.agent_fleet import resolve_fleet
from ai_os.local_worker import run_local_worker_once
from ai_os.pm_compiler import compile_pm_spec
from ai_os.contracts import PMSpec, PMEpic, PMTask, ExecutorType
from ai_os.memory import add_memory_entry, get_memory_entries, search_memory


@pytest.fixture
def temp_repo(tmp_path):
    """Create a temporary repository structure for testing."""
    # Create necessary directories
    (tmp_path / "ops" / "tasks" / "compiled").mkdir(parents=True)
    (tmp_path / "ops" / "tasks" / "pending").mkdir(parents=True)
    (tmp_path / "ops" / "tasks" / "running").mkdir(parents=True)
    (tmp_path / "ops" / "tasks" / "done").mkdir(parents=True)
    (tmp_path / "ops" / "context_bundles").mkdir(parents=True)
    (tmp_path / "ops" / "reports").mkdir(parents=True)
    (tmp_path / "ops" / "evidence" / "raw").mkdir(parents=True)
    (tmp_path / "ops" / "evidence" / "processed").mkdir(parents=True)
    (tmp_path / "ops" / "memory").mkdir(parents=True)

    # Create a minimal paperclip config
    (tmp_path / "paperclip").mkdir(parents=True)
    fleet_config = """company: TestCompany
version: 1
defaults:
  working_directory: "."
  instructions_file: "AGENTS.md"
  heartbeat: false
agents:
  - key: local_builder
    title: Local Builder Agent
    name: Local Builder
    role: builder
    assignment_role: local_codex_builder
    adapter_type: claude_local
    command: claude
    model: default
    enable_search: true
    ready: true
"""
    (tmp_path / "paperclip" / "agent_fleet.yaml").write_text(fleet_config)

    # Create AGENTS.md
    (tmp_path / "AGENTS.md").write_text("# Agent Instructions\n")

    # Create test task envelope in compiled dir (required by local_worker)
    # The legacy_task_name uses slugify(initiative_id-epic_id-task_id)
    envelope_json = {
        "envelope_id": "test-initiative-test-epic-001-test-task-001",
        "goal_id": "test-goal",
        "initiative_id": "test-initiative",
        "initiative_title": "Test Initiative",
        "epic_id": "test-epic-001",
        "task_id": "test-task-001",
        "title": "Test Task",
        "description": "A test task for local worker dry-run",
        "executor_type": "claude_code",
        "budget_cap": 100.0,
        "acceptance_criteria": [],
        "context_bundle_ref": "test-context",
        "artifact_output_path": "ops/reports/test-output.md",
        "approval_required": False,
        "mission": "Test mission",
        "objective": "Test objective",
        "steps": [],
        "constraints": [],
        "evidence_refs": [],
        "priority": "medium",
    }
    # Filename must be {slugified(initiative_id-epic_id-task_id)}.json
    compiled_filename = "test-initiative-test-epic-001-test-task-001.json"
    (tmp_path / "ops" / "tasks" / "compiled" / compiled_filename).write_text(
        json.dumps(envelope_json, indent=2)
    )

    # Create pending task file (legacy format) - must match compiled filename without .json
    (tmp_path / "ops" / "tasks" / "pending" / compiled_filename.replace(".json", ".md")).write_text("# Test Task\n")

    return tmp_path


def test_agent_fleet_resolution(temp_repo):
    """Test that agent fleet can be resolved."""
    agents = resolve_fleet(temp_repo)
    assert len(agents) > 0
    local_builder = next((a for a in agents if a.key == "local_builder"), None)
    assert local_builder is not None
    assert local_builder.ready is True


def test_pm_compiler_generates_envelope(temp_repo):
    """Test that PM Compiler can generate TaskEnvelope from PMSpec."""
    spec = PMSpec(
        goal_id="test-goal",
        mission="Test mission",
        initiative_id="test-initiative",
        initiative_title="Test Initiative",
        summary="Test summary",
        epics=[
            PMEpic(
                epic_id="test-epic",
                title="Test Epic",
                tasks=[
                    PMTask(
                        task_id="test-task",
                        title="Test Task",
                        objective="Test objective",
                        executor_type=ExecutorType.claude_code,
                        priority="medium",
                    )
                ],
            )
        ],
    )

    result = compile_pm_spec(spec, temp_repo)
    assert len(result.envelope_paths) == 1
    assert len(result.context_bundle_paths) == 1


def test_memory_system(temp_repo):
    """Test the memory system for storing lessons learned."""
    # Add a memory entry
    entry = add_memory_entry(
        repo_root=temp_repo,
        category="lesson",
        title="Test Lesson",
        content="This is a test lesson",
        tags=["test"],
    )
    assert entry.entry_id is not None

    # Retrieve entries
    entries = get_memory_entries(temp_repo, category="lesson")
    assert len(entries) == 1
    assert entries[0].title == "Test Lesson"

    # Search memory
    results = search_memory(temp_repo, "test")
    assert len(results) == 1


def test_local_worker_dry_run(temp_repo):
    """Test that local worker can run in dry-run mode."""
    # Run local worker in dry-run mode (no actual agent invocation)
    result = run_local_worker_once(temp_repo, "local_builder", dry_run=True)

    # Verify the worker processed the task
    assert result is not None
    assert result.status in ["succeeded", "failed", "pending"]
    assert result.task_id is not None
