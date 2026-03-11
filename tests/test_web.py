import tempfile
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

from ai_os.web import create_app


class WebAppTests(unittest.TestCase):
    def test_status_and_dispatch_endpoints(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            examples_dir = repo_root / "examples"
            examples_dir.mkdir(parents=True, exist_ok=True)

            source_spec = Path(__file__).resolve().parents[1] / "examples/pm_spec.yaml"
            (examples_dir / "pm_spec.yaml").write_text(source_spec.read_text(encoding="utf-8"), encoding="utf-8")

            client = TestClient(create_app(repo_root))

            status_before = client.get("/api/status")
            self.assertEqual(status_before.status_code, 200)
            self.assertEqual(status_before.json()["pending_tasks"], 0)

            dispatched = client.post(
                "/api/dispatch",
                json={"input_path": "examples/pm_spec.yaml", "task_id": "signup-dropoff-audit"},
            )
            self.assertEqual(dispatched.status_code, 200)
            self.assertIn("legacy_task_path", dispatched.json())

            status_after = client.get("/api/status")
            self.assertEqual(status_after.status_code, 200)
            self.assertEqual(status_after.json()["pending_tasks"], 1)
            self.assertEqual(status_after.json()["paperclip_outbox"], 1)


if __name__ == "__main__":
    unittest.main()
