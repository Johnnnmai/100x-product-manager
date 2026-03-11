"""Swarm Orchestrator - Multi-Agent Coordination System

This module provides:
- Parallel task distribution across agents
- Cross-agent verification mechanism
- Iterative refinement flow
- Task dependency management
"""
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable
import uuid
from datetime import datetime
from pathlib import Path


class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    BLOCKED = "blocked"
    VERIFYING = "verifying"
    NEEDS_REVISION = "needs_revision"


class AgentRole(Enum):
    ARCHITECT = "architect"
    IMPLEMENTER = "implementer"
    REVIEWER = "reviewer"
    TESTER = "tester"
    CHALLENGE = "challenge"
    INTEGRATOR = "integrator"


class VerificationResult(Enum):
    PASSED = "passed"
    FAILED = "failed"
    NEEDS_WORK = "needs_work"


@dataclass
class VerificationRecord:
    """Record of a verification check between agents"""
    verification_id: str
    task_id: str
    verifier_role: AgentRole
    result: VerificationResult
    feedback: str
    issues: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class SwarmTask:
    """Individual task within a swarm execution"""
    task_id: str
    agent_role: AgentRole
    description: str
    inputs: dict[str, Any] = field(default_factory=dict)
    status: TaskStatus = TaskStatus.PENDING
    output: dict[str, Any] = field(default_factory=dict)
    error: str | None = None
    created_at: datetime = field(default_factory=datetime.now)
    started_at: datetime | None = None
    completed_at: datetime | None = None
    depends_on: list[str] = field(default_factory=list)


@dataclass
class SwarmExecution:
    """Complete swarm execution with multiple parallel tasks"""
    execution_id: str
    tasks: list[SwarmTask] = field(default_factory=list)
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime = field(default_factory=datetime.now)
    completed_at: datetime | None = None
    results: dict[str, Any] = field(default_factory=dict)

    def get_ready_tasks(self) -> list[SwarmTask]:
        """Get tasks that are ready to run (dependencies met)"""
        ready = []
        for task in self.tasks:
            if task.status != TaskStatus.PENDING:
                continue
            # Check if all dependencies are completed
            deps_completed = all(
                any(t.task_id == dep and t.status == TaskStatus.COMPLETED
                    for t in self.tasks)
                for dep in task.depends_on
            )
            if deps_completed:
                ready.append(task)
        return ready

    def get_task(self, task_id: str) -> SwarmTask | None:
        """Get task by ID"""
        return next((t for t in self.tasks if t.task_id == task_id), None)

    def update_task_status(self, task_id: str, status: TaskStatus,
                          output: dict[str, Any] | None = None,
                          error: str | None = None) -> None:
        """Update task status"""
        task = self.get_task(task_id)
        if task:
            task.status = status
            if output:
                task.output = output
            if error:
                task.error = error
            if status == TaskStatus.RUNNING:
                task.started_at = datetime.now()
            elif status in (TaskStatus.COMPLETED, TaskStatus.FAILED):
                task.completed_at = datetime.now()

    def is_complete(self) -> bool:
        """Check if all tasks are complete"""
        return all(t.status in (TaskStatus.COMPLETED, TaskStatus.FAILED)
                   for t in self.tasks)

    def has_failures(self) -> bool:
        """Check if any task failed"""
        return any(t.status == TaskStatus.FAILED for t in self.tasks)


class SwarmOrchestrator:
    """Orchestrates multiple agents working in parallel with coordination"""

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.executions: dict[str, SwarmExecution] = {}

    def create_execution(self, tasks: list[dict[str, Any]]) -> SwarmExecution:
        """Create a new swarm execution with tasks"""
        execution_id = f"swarm-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:6]}"
        swarm_tasks = []

        for task_def in tasks:
            task = SwarmTask(
                task_id=task_def.get("task_id", f"task-{uuid.uuid4().hex[:6]}"),
                agent_role=AgentRole(task_def["agent_role"]),
                description=task_def["description"],
                inputs=task_def.get("inputs", {}),
                depends_on=task_def.get("depends_on", [])
            )
            swarm_tasks.append(task)

        execution = SwarmExecution(execution_id=execution_id, tasks=swarm_tasks)
        self.executions[execution_id] = execution
        return execution

    def get_ready_tasks(self, execution_id: str) -> list[SwarmTask]:
        """Get tasks ready to run in an execution"""
        execution = self.executions.get(execution_id)
        if not execution:
            return []
        return execution.get_ready_tasks()

    def claim_task(self, execution_id: str, task_id: str) -> bool:
        """Mark a task as running (claim for execution)"""
        execution = self.executions.get(execution_id)
        if not execution:
            return False
        task = execution.get_task(task_id)
        if not task or task.status != TaskStatus.PENDING:
            return False
        execution.update_task_status(task_id, TaskStatus.RUNNING)
        return True

    def complete_task(self, execution_id: str, task_id: str,
                    output: dict[str, Any]) -> None:
        """Mark task as completed with output"""
        execution = self.executions.get(execution_id)
        if execution:
            execution.update_task_status(task_id, TaskStatus.COMPLETED, output=output)

    def fail_task(self, execution_id: str, task_id: str, error: str) -> None:
        """Mark task as failed with error"""
        execution = self.executions.get(execution_id)
        if execution:
            execution.update_task_status(task_id, TaskStatus.FAILED, error=error)

    def get_execution_status(self, execution_id: str) -> dict[str, Any]:
        """Get execution status summary"""
        execution = self.executions.get(execution_id)
        if not execution:
            return {"status": "not_found"}

        return {
            "execution_id": execution.execution_id,
            "status": execution.status.value,
            "total_tasks": len(execution.tasks),
            "completed": sum(1 for t in execution.tasks if t.status == TaskStatus.COMPLETED),
            "failed": sum(1 for t in execution.tasks if t.status == TaskStatus.FAILED),
            "running": sum(1 for t in execution.tasks if t.status == TaskStatus.RUNNING),
            "pending": sum(1 for t in execution.tasks if t.status == TaskStatus.PENDING),
            "is_complete": execution.is_complete(),
            "has_failures": execution.has_failures()
        }

    def run_parallel_phase(self, execution_id: str,
                          executor_fn) -> dict[str, Any]:
        """Run a parallel phase - execute all ready tasks concurrently"""
        execution = self.executions.get(execution_id)
        if not execution:
            return {"error": "Execution not found"}

        ready_tasks = execution.get_ready_tasks()
        results = {"executed": [], "errors": []}

        for task in ready_tasks:
            # Claim task
            if self.claim_task(execution_id, task.task_id):
                try:
                    # Execute task using provided function
                    output = executor_fn(task)
                    self.complete_task(execution_id, task.task_id, output)
                    results["executed"].append(task.task_id)
                except Exception as e:
                    self.fail_task(execution_id, task.task_id, str(e))
                    results["errors"].append({"task_id": task.task_id, "error": str(e)})

        # Check if all tasks complete
        if execution.is_complete():
            execution.status = TaskStatus.COMPLETED if not execution.has_failures() else TaskStatus.FAILED
            execution.completed_at = datetime.now()

        return results


def get_swarm_orchestrator(repo_root: Path | str) -> SwarmOrchestrator:
    """Get or create a swarm orchestrator instance"""
    if isinstance(repo_root, str):
        repo_root = Path(repo_root)
    return SwarmOrchestrator(repo_root)


# Extended methods for SwarmOrchestrator - adding cross-agent verification and iterative refinement

def add_cross_agent_verification(
    self,
    execution_id: str,
    task_id: str,
    verifier_role: AgentRole,
    verify_fn: Callable[[dict[str, Any]], tuple[VerificationResult, str, list[str]]],
) -> VerificationRecord:
    """Add a verification record for cross-agent verification.

    Args:
        execution_id: The execution ID
        task_id: The task to verify
        verifier_role: The role performing verification
        verify_fn: Function that takes task output and returns (result, feedback, issues)

    Returns:
        VerificationRecord with verification results
    """
    execution = self.executions.get(execution_id)
    if not execution:
        raise ValueError(f"Execution {execution_id} not found")

    task = execution.get_task(task_id)
    if not task:
        raise ValueError(f"Task {task_id} not found")

    # Mark task as verifying
    execution.update_task_status(task_id, TaskStatus.VERIFYING)

    # Run verification
    result, feedback, issues = verify_fn(task.output)

    # Create verification record
    verification = VerificationRecord(
        verification_id=f"verify-{uuid.uuid4().hex[:6]}",
        task_id=task_id,
        verifier_role=verifier_role,
        result=result,
        feedback=feedback,
        issues=issues,
    )

    # Update task status based on verification
    if result == VerificationResult.PASSED:
        execution.update_task_status(task_id, TaskStatus.COMPLETED, output=task.output)
    elif result == VerificationResult.NEEDS_WORK:
        execution.update_task_status(task_id, TaskStatus.NEEDS_REVISION, output=task.output)
    else:
        execution.update_task_status(task_id, TaskStatus.FAILED, error=feedback)

    return verification


def add_revision_task(
    self,
    execution_id: str,
    original_task_id: str,
    revision_description: str,
) -> SwarmTask:
    """Add a revision task based on verification feedback.

    Args:
        execution_id: The execution ID
        original_task_id: The task that needs revision
        revision_description: Description of what needs to be revised

    Returns:
        New SwarmTask for the revision
    """
    execution = self.executions.get(execution_id)
    if not execution:
        raise ValueError(f"Execution {execution_id} not found")

    # Get original task to copy metadata
    original_task = execution.get_task(original_task_id)
    if not original_task:
        raise ValueError(f"Task {original_task_id} not found")

    # Create revision task that depends on the original
    revision_task = SwarmTask(
        task_id=f"{original_task_id}-rev-{uuid.uuid4().hex[:4]}",
        agent_role=original_task.agent_role,
        description=f"Revision: {revision_description}",
        inputs={"original_output": original_task.output, "revision_required": revision_description},
        depends_on=[original_task_id],
    )

    execution.tasks.append(revision_task)
    return revision_task


def run_iterative_refinement(
    self,
    execution_id: str,
    executor_fn: Callable[[SwarmTask], dict[str, Any]],
    verifier_fn: Callable[[SwarmTask], tuple[VerificationResult, str, list[str]]],
    max_iterations: int = 3,
) -> dict[str, Any]:
    """Run iterative refinement loop until verification passes or max iterations.

    This implements the Challenge Agent pattern where:
    1. Implementer produces output
    2. Reviewer/Challenge verifies
    3. If issues found, Implementer revises
    4. Repeat until passed or max iterations

    Args:
        execution_id: The execution ID
        executor_fn: Function to execute a task
        verifier_fn: Function to verify task output
        max_iterations: Maximum refinement iterations

    Returns:
        Summary of refinement iterations
    """
    execution = self.executions.get(execution_id)
    if not execution:
        return {"error": "Execution not found"}

    iterations = []
    iteration = 1

    while iteration <= max_iterations:
        # Run all ready tasks in parallel
        results = self.run_parallel_phase(execution_id, executor_fn)

        # Collect completed tasks that need verification
        completed_tasks = [
            t for t in execution.tasks
            if t.status == TaskStatus.COMPLETED and t not in [iv.get("task") for iv in iterations if iv.get("task")]
        ]

        verification_results = []

        for task in completed_tasks:
            # Verify the task
            result, feedback, issues = verifier_fn(task)

            verification_results.append({
                "task_id": task.task_id,
                "result": result.value,
                "feedback": feedback,
                "issues": issues,
            })

            if result in (VerificationResult.FAILED, VerificationResult.NEEDS_WORK):
                # Mark as needs revision
                execution.update_task_status(task.task_id, TaskStatus.NEEDS_REVISION)

                # Create revision task
                revision_task = self.add_revision_task(
                    execution_id,
                    task.task_id,
                    f"Iteration {iteration}: {feedback}",
                )

        iterations.append({
            "iteration": iteration,
            "executed": results.get("executed", []),
            "verifications": verification_results,
        })

        # Check if all tasks passed verification
        all_passed = all(
            v["result"] == VerificationResult.PASSED.value
            for v in verification_results
        )

        if all_passed and execution.is_complete():
            execution.status = TaskStatus.COMPLETED
            break

        iteration += 1

        # Check if we've exceeded max iterations
        if iteration > max_iterations:
            execution.status = TaskStatus.FAILED

    return {
        "execution_id": execution_id,
        "total_iterations": iteration,
        "max_iterations": max_iterations,
        "iterations": iterations,
        "final_status": execution.status.value,
    }


# Monkey-patch the methods onto SwarmOrchestrator class
SwarmOrchestrator.add_cross_agent_verification = add_cross_agent_verification
SwarmOrchestrator.add_revision_task = add_revision_task
SwarmOrchestrator.run_iterative_refinement = run_iterative_refinement
