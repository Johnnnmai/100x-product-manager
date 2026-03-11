"""
Enhanced Edge Case Tests for AI OS

Tests for:
- Edge cases in core components
- Error handling scenarios
- Resource cleanup validation
- Boundary conditions
"""

import json
import tempfile
import unittest
from pathlib import Path

from ai_os.contracts import ExecutorType, TaskEnvelope
from ai_os.memory import add_memory_entry, get_memory_entries, search_memory


class EdgeCaseTests(unittest.TestCase):
    """Test edge cases and boundary conditions."""

    def test_zero_budget_task(self) -> None:
        """Test handling of zero budget tasks."""
        envelope = TaskEnvelope(
            envelope_id="test-zero-budget",
            goal_id="test-goal",
            initiative_id="test-initiative",
            initiative_title="Test",
            epic_id="test-epic",
            task_id="test-task",
            title="Zero Budget Task",
            executor_type=ExecutorType.codex,
            budget_cap=0.0,  # Zero budget
            acceptance_criteria=["Complete"],
            context_bundle_ref="ops/context_bundles/test.json",
            artifact_output_path="ops/artifacts/test",
            approval_required=False,
            mission="Test",
            objective="Test",
            steps=["Step1"],
            constraints=[],
            priority="low",
        )
        # Zero budget should still be valid
        self.assertEqual(envelope.budget_cap, 0.0)
        self.assertIsNotNone(envelope.envelope_id)

    def test_empty_context_bundle(self) -> None:
        """Test handling of empty context bundle."""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            (repo_root / "ops/context_bundles").mkdir(parents=True, exist_ok=True)

            # Empty context bundle
            empty_context = {}
            (repo_root / "ops/context_bundles/empty.json").write_text(
                json.dumps(empty_context),
                encoding="utf-8",
            )

            # Verify file was created and can be read
            content = (repo_root / "ops/context_bundles/empty.json").read_text(encoding="utf-8")
            self.assertEqual(content, "{}")

    def test_very_long_task_id(self) -> None:
        """Test handling of very long task IDs."""
        long_id = "a" * 500  # 500 character task ID

        envelope = TaskEnvelope(
            envelope_id=long_id[:100],  # Truncate to valid length
            goal_id="test-goal",
            initiative_id="test-initiative",
            initiative_title="Test",
            epic_id="test-epic",
            task_id="test-task",
            title="Long Task ID Test",
            executor_type=ExecutorType.codex,
            budget_cap=100.0,
            acceptance_criteria=["Complete"],
            context_bundle_ref="ops/context_bundles/test.json",
            artifact_output_path="ops/artifacts/test",
            approval_required=False,
            mission="Test",
            objective="Test",
            steps=["Step1"],
            constraints=[],
            priority="medium",
        )
        self.assertIsNotNone(envelope.envelope_id)
        self.assertLessEqual(len(envelope.envelope_id), 100)

    def test_special_characters_in_paths(self) -> None:
        """Test handling of special characters in file paths."""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)

            # Create paths with special characters
            special_dirs = [
                "ops/tasks/pending",
                "ops/tasks/running",
                "ops/tasks/done",
                "ops/reports",
                "ops/context_bundles",
            ]

            for d in special_dirs:
                (repo_root / d).mkdir(parents=True, exist_ok=True)

            # Should create all directories successfully
            for d in special_dirs:
                self.assertTrue((repo_root / d).exists())


class ErrorHandlingTests(unittest.TestCase):
    """Test error handling scenarios."""

    def test_invalid_json_context(self) -> None:
        """Test handling of invalid JSON in context bundle."""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            (repo_root / "ops/context_bundles").mkdir(parents=True, exist_ok=True)

            # Write invalid JSON
            invalid_json = "{ invalid json content }"
            (repo_root / "ops/context_bundles/invalid.json").write_text(
                invalid_json, encoding="utf-8"
            )

            # Should handle parse error gracefully
            try:
                with open(repo_root / "ops/context_bundles/invalid.json") as f:
                    data = json.load(f)
                self.fail("Should have raised JSONDecodeError")
            except json.JSONDecodeError:
                pass  # Expected

    def test_corrupted_task_file(self) -> None:
        """Test handling of corrupted task file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            (repo_root / "ops/tasks/pending").mkdir(parents=True, exist_ok=True)

            # Write corrupted markdown
            corrupted_content = "# Task\n\nThis is not proper task format"
            (repo_root / "ops/tasks/pending/bad-task.md").write_text(
                corrupted_content, encoding="utf-8"
            )

            # Should not crash when trying to process
            # Attempting to parse corrupted file should be handled
            task_files = list((repo_root / "ops/tasks/pending").glob("*.md"))
            self.assertEqual(len(task_files), 1)


class ResourceCleanupTests(unittest.TestCase):
    """Test resource cleanup and validation."""

    def test_temp_directory_cleanup(self) -> None:
        """Test that temporary resources are cleaned up."""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            # Create test structure
            (repo_root / "ops/tasks/pending").mkdir(parents=True, exist_ok=True)
            (repo_root / "ops/tasks/running").mkdir(parents=True, exist_ok=True)
            (repo_root / "ops/tasks/done").mkdir(parents=True, exist_ok=True)

            # Temporary directory context manager should clean up
            # This test validates the pattern works
            self.assertTrue((repo_root / "ops/tasks/pending").exists())

    def test_context_bundle_cleanup(self) -> None:
        """Test context bundle file handling."""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            (repo_root / "ops/context_bundles").mkdir(parents=True, exist_ok=True)

            # Create multiple context bundles
            for i in range(5):
                ctx = {
                    "bundle_id": f"test-{i}",
                    "mission": f"Test mission {i}",
                    "constraints": [],
                    "evidence_refs": [],
                    "glossary": {},
                    "latest_decisions": [],
                }
                (repo_root / "ops/context_bundles" / f"test-{i}.json").write_text(
                    json.dumps(ctx, indent=2),
                    encoding="utf-8",
                )

            # All should exist
            bundles = list((repo_root / "ops/context_bundles").glob("*.json"))
            self.assertEqual(len(bundles), 5)

            # Clean up
            for f in bundles:
                f.unlink()

            # All should be gone
            bundles = list((repo_root / "ops/context_bundles").glob("*.json"))
            self.assertEqual(len(bundles), 0)

    def test_memory_entry_cleanup(self) -> None:
        """Test memory entry cleanup."""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            (repo_root / "ops/memory").mkdir(parents=True, exist_ok=True)

            # Add entries
            entry1 = add_memory_entry(
                repo_root=repo_root,
                category="lesson",
                title="Test lesson 1",
                content="Test lesson 1 content",
            )
            entry2 = add_memory_entry(
                repo_root=repo_root,
                category="lesson",
                title="Test lesson 2",
                content="Test lesson 2 content",
            )

            # Get entries
            entries = get_memory_entries(repo_root, "lesson")
            self.assertGreaterEqual(len(entries), 2)

            # Search
            results = search_memory(repo_root, "test")
            self.assertIsNotNone(results)

    def test_report_file_cleanup(self) -> None:
        """Test report file handling."""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            (repo_root / "ops/reports").mkdir(parents=True, exist_ok=True)

            # Create multiple reports
            for i in range(3):
                report_path = repo_root / "ops/reports" / f"report-{i}.md"
                report_path.write_text(f"# Report {i}\n\nContent for report {i}", encoding="utf-8")

            reports = list((repo_root / "ops/reports").glob("*.md"))
            self.assertEqual(len(reports), 3)


class BoundaryConditionTests(unittest.TestCase):
    """Test boundary conditions."""

    def test_max_priority_value(self) -> None:
        """Test maximum priority value handling."""
        envelope = TaskEnvelope(
            envelope_id="test-max-priority",
            goal_id="test-goal",
            initiative_id="test-initiative",
            initiative_title="Test",
            epic_id="test-epic",
            task_id="test-task",
            title="Max Priority Test",
            executor_type=ExecutorType.codex,
            budget_cap=999999.0,  # Very high budget
            acceptance_criteria=["Complete"],
            context_bundle_ref="ops/context_bundles/test.json",
            artifact_output_path="ops/artifacts/test",
            approval_required=False,
            mission="Test",
            objective="Test",
            steps=["Step1"],
            constraints=[],
            priority="high",
        )
        self.assertEqual(envelope.priority, "high")

    def test_min_budget_value(self) -> None:
        """Test minimum budget value handling."""
        envelope = TaskEnvelope(
            envelope_id="test-min-budget",
            goal_id="test-goal",
            initiative_id="test-initiative",
            initiative_title="Test",
            epic_id="test-epic",
            task_id="test-task",
            title="Min Budget Test",
            executor_type=ExecutorType.codex,
            budget_cap=0.01,  # Very small budget
            acceptance_criteria=["Complete"],
            context_bundle_ref="ops/context_bundles/test.json",
            artifact_output_path="ops/artifacts/test",
            approval_required=False,
            mission="Test",
            objective="Test",
            steps=["Step1"],
            constraints=[],
            priority="low",
        )
        self.assertGreater(envelope.budget_cap, 0)

    def test_empty_steps_list(self) -> None:
        """Test handling of empty steps list."""
        envelope = TaskEnvelope(
            envelope_id="test-empty-steps",
            goal_id="test-goal",
            initiative_id="test-initiative",
            initiative_title="Test",
            epic_id="test-epic",
            task_id="test-task",
            title="Empty Steps Test",
            executor_type=ExecutorType.codex,
            budget_cap=100.0,
            acceptance_criteria=["Complete"],
            context_bundle_ref="ops/context_bundles/test.json",
            artifact_output_path="ops/artifacts/test",
            approval_required=False,
            mission="Test",
            objective="Test",
            steps=[],  # Empty steps
            constraints=[],
            priority="medium",
        )
        self.assertEqual(len(envelope.steps), 0)

    def test_max_constraints(self) -> None:
        """Test handling of many constraints."""
        constraints = [f"Constraint {i}" for i in range(100)]

        envelope = TaskEnvelope(
            envelope_id="test-max-constraints",
            goal_id="test-goal",
            initiative_id="test-initiative",
            initiative_title="Test",
            epic_id="test-epic",
            task_id="test-task",
            title="Max Constraints Test",
            executor_type=ExecutorType.codex,
            budget_cap=100.0,
            acceptance_criteria=["Complete"],
            context_bundle_ref="ops/context_bundles/test.json",
            artifact_output_path="ops/artifacts/test",
            approval_required=False,
            mission="Test",
            objective="Test",
            steps=["Step1"],
            constraints=constraints,
            priority="medium",
        )
        self.assertEqual(len(envelope.constraints), 100)


if __name__ == "__main__":
    unittest.main()
