import json
import tempfile
import unittest
from pathlib import Path

from ai_os.contracts import ExecutorType, TaskEnvelope
from ai_os.discord_bridge import create_approval_request
from ai_os.local_worker import AgentExecution, run_local_worker_once
from ai_os.legacy_adapter import queue_legacy_task


class LocalWorkerTests(unittest.TestCase):
    def _write_repo_scaffold(self, repo_root: Path) -> None:
        source_root = Path(__file__).resolve().parents[1]
        (repo_root / "paperclip/bootstrap").mkdir(parents=True, exist_ok=True)
        (repo_root / "paperclip/bin").mkdir(parents=True, exist_ok=True)
        (repo_root / "ops/tasks/compiled").mkdir(parents=True, exist_ok=True)
        (repo_root / "ops/context_bundles").mkdir(parents=True, exist_ok=True)

        # Copy AGENTS.md if it exists
        agents_md = source_root / "AGENTS.md"
        if agents_md.exists():
            (repo_root / "AGENTS.md").write_text(agents_md.read_text(encoding="utf-8"), encoding="utf-8")
        else:
            (repo_root / "AGENTS.md").write_text("# Agents\n\nLocal Builder Agent\n", encoding="utf-8")

        # Copy agent_fleet.yaml if it exists
        fleet_yaml = source_root / "paperclip/agent_fleet.yaml"
        if fleet_yaml.exists():
            (repo_root / "paperclip/agent_fleet.yaml").write_text(fleet_yaml.read_text(encoding="utf-8"), encoding="utf-8")

        # Create minimal bootstrap files
        for agent_name in ("ceo_codex", "pm_compiler", "local_builder", "local_claude_builder"):
            bootstrap_path = repo_root / "paperclip/bootstrap" / f"{agent_name}.md"
            bootstrap_path.write_text(f"# {agent_name.title()} Agent\n\nBootstrap prompt for {agent_name}\n", encoding="utf-8")

        # Create minimal bin files
        for bin_name in ("claude-paperclip.cmd", "codex-paperclip.cmd", "zoe-paperclip.cmd", "mira-paperclip.cmd",
                        "forge-paperclip.cmd", "quill-paperclip.cmd"):
            bin_path = repo_root / "paperclip/bin" / bin_name
            bin_path.write_text(f"echo {bin_name}\n", encoding="utf-8")

    def _write_envelope(self, repo_root: Path, approval_required: bool = False) -> TaskEnvelope:
        envelope = TaskEnvelope(
            envelope_id="growth-loop__activation-fix__local-build-task",
            goal_id="growth-loop",
            initiative_id="activation-fix",
            initiative_title="Activation Fix",
            epic_id="signup",
            task_id="local-build-task",
            title="Implement the local build task",
            executor_type=ExecutorType.codex,
            budget_cap=50.0,
            acceptance_criteria=["Ship a bounded change", "Write a report"],
            context_bundle_ref="ops/context_bundles/local-build-task.json",
            artifact_output_path="ops/artifacts/local-build-task",
            approval_required=approval_required,
            mission="Improve activation",
            objective="Fix the local onboarding bug",
            steps=["Inspect the queue", "Implement the bugfix"],
            constraints=["Do not change unrelated files"],
            priority="high",
        )
        (repo_root / envelope.context_bundle_ref).write_text(
            json.dumps(
                {
                    "bundle_id": "local-build-task",
                    "mission": envelope.mission,
                    "constraints": envelope.constraints,
                    "evidence_refs": [],
                    "glossary": {},
                    "latest_decisions": [],
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        (repo_root / "ops/tasks/compiled" / f"{envelope.envelope_id}.json").write_text(
            envelope.model_dump_json(indent=2),
            encoding="utf-8",
        )
        queue_legacy_task(envelope, repo_root)
        return envelope

    def test_run_local_worker_claims_task_and_writes_fallback_report(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            self._write_repo_scaffold(repo_root)
            envelope = self._write_envelope(repo_root)

            def fake_runner(*args, **kwargs) -> AgentExecution:
                return AgentExecution(
                    exit_code=0,
                    response={
                        "status": "succeeded",
                        "summary": "Implemented the requested local task.",
                        "report_path": "ops/reports/worker-report.md",
                        "verification": "unit smoke complete",
                    },
                    stdout="ok",
                    stderr="",
                )

            result = run_local_worker_once(
                repo_root=repo_root,
                agent_key="local_builder",
                runner=fake_runner,
            )

            self.assertEqual(result.status, "succeeded")
            self.assertEqual(result.task_id, envelope.task_id)
            self.assertFalse((repo_root / "ops/tasks/pending").exists() and any((repo_root / "ops/tasks/pending").glob("*.md")))
            self.assertTrue(Path(result.done_task_path).exists())
            self.assertTrue(Path(result.report_path).exists())
            report_text = Path(result.report_path).read_text(encoding="utf-8")
            self.assertIn("Implemented the requested local task.", report_text)

    def test_run_local_worker_blocks_pending_approval(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            self._write_repo_scaffold(repo_root)
            envelope = self._write_envelope(repo_root, approval_required=True)
            create_approval_request(envelope, repo_root)

            result = run_local_worker_once(repo_root=repo_root, agent_key="local_builder")

            self.assertEqual(result.status, "blocked")
            self.assertIn("local-build-task:pending", result.blockers)
            pending_files = list((repo_root / "ops/tasks/pending").glob("*.md"))
            self.assertEqual(len(pending_files), 1)

    def test_run_local_worker_dry_run_completes_without_agent_invocation(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            self._write_repo_scaffold(repo_root)
            self._write_envelope(repo_root)
            (repo_root / "ops/tasks/compiled" / "activation-fix-manifest.json").write_text(
                json.dumps({"initiative_id": "activation-fix", "epics": []}, indent=2),
                encoding="utf-8",
            )

            result = run_local_worker_once(
                repo_root=repo_root,
                agent_key="local_builder",
                dry_run=True,
            )

            self.assertEqual(result.status, "succeeded")
            self.assertTrue(Path(result.report_path).exists())
            self.assertTrue(Path(result.done_task_path).exists())


if __name__ == "__main__":
    unittest.main()
