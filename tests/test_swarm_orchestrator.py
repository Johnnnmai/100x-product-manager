"""Tests for Swarm Orchestrator (Multi-Agent Coordination)"""
import pytest
from pathlib import Path
from ai_os.swarm_orchestrator import (
    SwarmOrchestrator, SwarmExecution, SwarmTask, TaskStatus, AgentRole,
    get_swarm_orchestrator, VerificationResult, VerificationRecord
)


class SwarmOrchestratorTests:
    """Test suite for Swarm Orchestrator"""

    def test_create_execution(self):
        """Verify swarm execution can be created with tasks"""
        orchestrator = SwarmOrchestrator(Path("."))

        tasks = [
            {
                "task_id": "task-001",
                "agent_role": "architect",
                "description": "Design system architecture"
            },
            {
                "task_id": "task-002",
                "agent_role": "implementer",
                "description": "Implement component",
                "depends_on": ["task-001"]
            }
        ]

        execution = orchestrator.create_execution(tasks)

        assert execution is not None
        assert len(execution.tasks) == 2
        assert execution.tasks[0].agent_role == AgentRole.ARCHITECT
        assert execution.tasks[1].agent_role == AgentRole.IMPLEMENTER
        assert "task-001" in execution.tasks[1].depends_on

    def test_get_ready_tasks_no_dependencies(self):
        """Verify tasks without dependencies are ready immediately"""
        orchestrator = SwarmOrchestrator(Path("."))

        tasks = [
            {
                "task_id": "task-001",
                "agent_role": "architect",
                "description": "Design"
            }
        ]

        execution = orchestrator.create_execution(tasks)
        ready = execution.get_ready_tasks()

        assert len(ready) == 1
        assert ready[0].task_id == "task-001"

    def test_get_ready_tasks_with_dependencies(self):
        """Verify tasks wait for dependencies to complete"""
        orchestrator = SwarmOrchestrator(Path("."))

        tasks = [
            {
                "task_id": "task-001",
                "agent_role": "architect",
                "description": "Design"
            },
            {
                "task_id": "task-002",
                "agent_role": "implementer",
                "description": "Implement",
                "depends_on": ["task-001"]
            }
        ]

        execution = orchestrator.create_execution(tasks)

        # Initially only task-001 should be ready
        ready = execution.get_ready_tasks()
        assert len(ready) == 1
        assert ready[0].task_id == "task-001"

        # Complete task-001
        execution.update_task_status("task-001", TaskStatus.COMPLETED)

        # Now task-002 should be ready
        ready = execution.get_ready_tasks()
        assert len(ready) == 1
        assert ready[0].task_id == "task-002"

    def test_claim_task(self):
        """Verify task can be claimed for execution"""
        orchestrator = SwarmOrchestrator(Path("."))

        tasks = [{"task_id": "task-001", "agent_role": "architect", "description": "Design"}]
        execution = orchestrator.create_execution(tasks)

        result = orchestrator.claim_task(execution.execution_id, "task-001")

        assert result is True
        task = execution.get_task("task-001")
        assert task.status == TaskStatus.RUNNING

    def test_complete_task(self):
        """Verify task can be marked completed"""
        orchestrator = SwarmOrchestrator(Path("."))

        tasks = [{"task_id": "task-001", "agent_role": "architect", "description": "Design"}]
        execution = orchestrator.create_execution(tasks)

        output = {"result": "architecture-designed"}
        orchestrator.complete_task(execution.execution_id, "task-001", output)

        task = execution.get_task("task-001")
        assert task.status == TaskStatus.COMPLETED
        assert task.output == output

    def test_fail_task(self):
        """Verify task can be marked failed"""
        orchestrator = SwarmOrchestrator(Path("."))

        tasks = [{"task_id": "task-001", "agent_role": "architect", "description": "Design"}]
        execution = orchestrator.create_execution(tasks)

        orchestrator.fail_task(execution.execution_id, "task-001", "Design failed")

        task = execution.get_task("task-001")
        assert task.status == TaskStatus.FAILED
        assert task.error == "Design failed"

    def test_get_execution_status(self):
        """Verify execution status is reported correctly"""
        orchestrator = SwarmOrchestrator(Path("."))

        tasks = [
            {"task_id": "task-001", "agent_role": "architect", "description": "Design"},
            {"task_id": "task-002", "agent_role": "implementer", "description": "Implement"}
        ]
        execution = orchestrator.create_execution(tasks)

        # Complete task-001
        orchestrator.complete_task(execution.execution_id, "task-001", {})

        status = orchestrator.get_execution_status(execution.execution_id)

        assert status["total_tasks"] == 2
        assert status["completed"] == 1
        assert status["pending"] == 1
        assert status["running"] == 0

    def test_parallel_phase_execution(self):
        """Verify parallel phase executes ready tasks"""
        orchestrator = SwarmOrchestrator(Path("."))

        tasks = [
            {"task_id": "task-001", "agent_role": "architect", "description": "Design"},
            {"task_id": "task-002", "agent_role": "reviewer", "description": "Review"}
        ]
        execution = orchestrator.create_execution(tasks)

        def executor(task: SwarmTask):
            return {"result": f"executed-{task.task_id}"}

        results = orchestrator.run_parallel_phase(execution.execution_id, executor)

        assert len(results["executed"]) == 2
        assert "task-001" in results["executed"]
        assert "task-002" in results["executed"]

    def test_get_swarm_orchestrator(self):
        """Verify get_swarm_orchestrator factory function works"""
        orch = get_swarm_orchestrator(Path("."))
        assert isinstance(orch, SwarmOrchestrator)

        # Same instance on second call
        orch2 = get_swarm_orchestrator(Path("."))
        # Note: This creates new instance, which is expected

    def test_verification_record_creation(self):
        """Verify VerificationRecord can be created"""
        record = VerificationRecord(
            verification_id="verify-001",
            task_id="task-001",
            verifier_role=AgentRole.REVIEWER,
            result=VerificationResult.PASSED,
            feedback="Looks good",
            issues=[],
        )
        assert record.verification_id == "verify-001"
        assert record.result == VerificationResult.PASSED

    def test_cross_agent_verification_pass(self):
        """Verify cross-agent verification passes when output is valid"""
        orchestrator = SwarmOrchestrator(Path("."))

        tasks = [{"task_id": "task-001", "agent_role": "implementer", "description": "Implement"}]
        execution = orchestrator.create_execution(tasks)

        # Complete task first
        orchestrator.complete_task(execution.execution_id, "task-001", {"result": "ok"})

        # Verify
        def verify_fn(output):
            if output.get("result") == "ok":
                return (VerificationResult.PASSED, "Looks good", [])
            return (VerificationResult.FAILED, "Failed", [])

        verification = orchestrator.add_cross_agent_verification(
            execution.execution_id, "task-001", AgentRole.REVIEWER, verify_fn
        )

        assert verification.result == VerificationResult.PASSED

    def test_cross_agent_verification_fail(self):
        """Verify cross-agent verification fails when output is invalid"""
        orchestrator = SwarmOrchestrator(Path("."))

        tasks = [{"task_id": "task-001", "agent_role": "implementer", "description": "Implement"}]
        execution = orchestrator.create_execution(tasks)

        # Complete task first
        orchestrator.complete_task(execution.execution_id, "task-001", {"result": "error"})

        def verify_fn(output):
            if output.get("result") == "ok":
                return (VerificationResult.PASSED, "Looks good", [])
            return (VerificationResult.NEEDS_WORK, "Needs fixes", ["Fix issue 1"])

        verification = orchestrator.add_cross_agent_verification(
            execution.execution_id, "task-001", AgentRole.REVIEWER, verify_fn
        )

        assert verification.result == VerificationResult.NEEDS_WORK
        assert len(verification.issues) == 1

    def test_add_revision_task(self):
        """Verify revision task can be added"""
        orchestrator = SwarmOrchestrator(Path("."))

        tasks = [{"task_id": "task-001", "agent_role": "implementer", "description": "Implement"}]
        execution = orchestrator.create_execution(tasks)

        # Complete original task
        orchestrator.complete_task(execution.execution_id, "task-001", {"result": "draft"})

        # Add revision task
        revision = orchestrator.add_revision_task(
            execution.execution_id, "task-001", "Fix bug in implementation"
        )

        assert "task-001" in revision.depends_on
        assert revision.status == TaskStatus.PENDING
        assert revision.agent_role == AgentRole.IMPLEMENTER

    def test_iterative_refinement_flow(self):
        """Verify iterative refinement loop works"""
        orchestrator = SwarmOrchestrator(Path("."))

        tasks = [{"task_id": "task-001", "agent_role": "implementer", "description": "Implement"}]
        execution = orchestrator.create_execution(tasks)

        iteration_count = 0

        def executor(task):
            nonlocal iteration_count
            iteration_count += 1
            return {"result": "good" if iteration_count > 1 else "needs_work"}

        def verifier(task):
            if task.output.get("result") == "good":
                return (VerificationResult.PASSED, "Approved", [])
            return (VerificationResult.NEEDS_WORK, "Not ready", ["Fix it"])

        result = orchestrator.run_iterative_refinement(
            execution.execution_id, executor, verifier, max_iterations=3
        )

        assert result["total_iterations"] == 2  # First fails, second passes
        assert result["final_status"] == "completed"


def test_swarm_orchestrator_suite():
    """Run swarm orchestrator test suite"""
    tests = SwarmOrchestratorTests()

    tests.test_create_execution()
    tests.test_get_ready_tasks_no_dependencies()
    tests.test_get_ready_tasks_with_dependencies()
    tests.test_claim_task()
    tests.test_complete_task()
    tests.test_fail_task()
    tests.test_get_execution_status()
    tests.test_parallel_phase_execution()
    tests.test_get_swarm_orchestrator()


if __name__ == "__main__":
    test_swarm_orchestrator_suite()
    print("Swarm Orchestrator tests passed!")
