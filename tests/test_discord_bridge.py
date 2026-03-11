import json
import tempfile
import unittest
from pathlib import Path

from ai_os.contracts import ArtifactKind, ArtifactRef, ApprovalStatus, ExecutorType, TaskEnvelope
from ai_os.discord_bridge import (
    create_approval_request,
    emit_event,
    event_from_approval,
    resolve_approval_request,
)


def build_envelope() -> TaskEnvelope:
    return TaskEnvelope(
        envelope_id="growth-loop__activation-fix__activation-instrumentation-fix",
        goal_id="company-ai-os-v1",
        initiative_id="growth-loop",
        initiative_title="Growth Loop Hardening",
        epic_id="activation-fix",
        task_id="activation-instrumentation-fix",
        title="Fix activation instrumentation",
        executor_type=ExecutorType.openclaw,
        budget_cap=120,
        acceptance_criteria=["Missing events are tracked"],
        context_bundle_ref="ops/context_bundles/growth-loop__activation-fix__activation-instrumentation-fix.json",
        artifact_output_path="ops/artifacts/growth-loop/activation-fix/activation-instrumentation-fix",
        approval_required=True,
        mission="Build the internal AI OS safely.",
        objective="Patch missing activation events.",
        steps=["Map missing events", "Ship the smallest safe patch"],
        constraints=["No redesigns"],
        evidence_refs=[
            ArtifactRef(
                kind=ArtifactKind.markdown,
                path="docs/EXECUTION_PROTOCOL.md",
                description="Execution protocol",
            )
        ],
        priority="medium",
    )


class DiscordBridgeTests(unittest.TestCase):
    def test_approval_lifecycle_and_dry_run_emit(self) -> None:
        envelope = build_envelope()
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            compiled_dir = repo_root / "ops/tasks/compiled"
            compiled_dir.mkdir(parents=True, exist_ok=True)
            (compiled_dir / f"{envelope.envelope_id}.json").write_text(
                envelope.model_dump_json(indent=2),
                encoding="utf-8",
            )

            approval = create_approval_request(envelope, repo_root)
            pending_path = repo_root / "ops/approvals/pending" / f"{approval.approval_id}.json"
            self.assertTrue(pending_path.exists())

            delivery = emit_event(event_from_approval(approval), repo_root)
            self.assertFalse(delivery.delivered)
            self.assertEqual(delivery.mode, "dry_run")
            self.assertTrue(Path(delivery.event_path).exists())

            approved_path = resolve_approval_request(
                approval.approval_id,
                ApprovalStatus.approved,
                "ops-owner",
                "Proceed",
                repo_root,
            )
            approved = json.loads(approved_path.read_text(encoding="utf-8"))
            self.assertEqual(approved["status"], "approved")
            self.assertFalse(pending_path.exists())


if __name__ == "__main__":
    unittest.main()
