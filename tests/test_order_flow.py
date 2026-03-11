import json
import tempfile
import unittest
from pathlib import Path

from ai_os.order_flow import dispatch_order


EXAMPLE_PM_SPEC = Path(__file__).resolve().parents[1] / "examples/pm_spec.yaml"


class OrderFlowTests(unittest.TestCase):
    def test_dispatch_order_creates_all_expected_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            result = dispatch_order(
                pm_spec_path=EXAMPLE_PM_SPEC,
                repo_root=repo_root,
                company_id="acme-company",
                task_id="signup-dropoff-audit",
            )

            self.assertTrue(Path(result.envelope_path).exists())
            self.assertTrue(Path(result.legacy_task_path).exists())
            self.assertTrue(Path(result.paperclip_request_path).exists())
            self.assertEqual(
                result.approval_id,
                "approval__growth-loop__activation-fix__signup-dropoff-audit",
            )
            self.assertEqual(result.discord_delivery_mode, "dry_run")

            queued_request = json.loads(Path(result.paperclip_request_path).read_text(encoding="utf-8"))
            self.assertEqual(queued_request["company_id"], "acme-company")


if __name__ == "__main__":
    unittest.main()
