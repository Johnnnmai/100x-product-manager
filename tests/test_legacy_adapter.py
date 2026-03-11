import json
import tempfile
import unittest
from pathlib import Path

from ai_os.contracts import ArtifactKind, ArtifactRef, ExecutorType, TaskEnvelope
from ai_os.legacy_adapter import (
    build_paperclip_run_request,
    envelope_to_markdown,
    queue_legacy_task,
    queue_paperclip_request,
)


def build_envelope() -> TaskEnvelope:
    return TaskEnvelope(
        envelope_id="growth-loop__activation-fix__signup-dropoff-audit",
        goal_id="company-ai-os-v1",
        initiative_id="growth-loop",
        initiative_title="Growth Loop Hardening",
        epic_id="activation-fix",
        task_id="signup-dropoff-audit",
        title="Audit signup drop-off",
        executor_type=ExecutorType.claude_code,
        budget_cap=80,
        acceptance_criteria=["A report is written", "Evidence is linked"],
        context_bundle_ref="ops/context_bundles/growth-loop__activation-fix__signup-dropoff-audit.json",
        artifact_output_path="ops/artifacts/growth-loop/activation-fix/signup-dropoff-audit",
        approval_required=True,
        mission="Build the internal AI OS safely.",
        objective="Audit the signup activation path.",
        steps=["Inspect current flow", "Write the audit report"],
        constraints=["No code changes"],
        evidence_refs=[
            ArtifactRef(
                kind=ArtifactKind.markdown,
                path="ops/EXECUTION_FLOW.md",
                description="Legacy execution flow",
            )
        ],
        priority="high",
    )


class LegacyAdapterTests(unittest.TestCase):
    def test_markdown_conversion_keeps_task_metadata(self) -> None:
        markdown = envelope_to_markdown(build_envelope())
        self.assertIn("# Task: Audit signup drop-off", markdown)
        self.assertIn("- [x] High", markdown)
        self.assertIn("context_bundle_ref: ops/context_bundles/growth-loop__activation-fix__signup-dropoff-audit.json", markdown)

    def test_queue_legacy_and_paperclip_requests(self) -> None:
        envelope = build_envelope()
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)

            task_path = queue_legacy_task(envelope, repo_root)
            self.assertTrue(task_path.exists())

            request = build_paperclip_run_request(envelope, "acme-company")
            outbox_path = queue_paperclip_request(request, repo_root)
            payload = json.loads(outbox_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["company_id"], "acme-company")
            self.assertEqual(payload["metadata"]["priority"], "high")


if __name__ == "__main__":
    unittest.main()
