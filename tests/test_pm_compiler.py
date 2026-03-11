import json
import tempfile
import unittest
from pathlib import Path

from ai_os.pm_compiler import compile_pm_spec, load_pm_spec


EXAMPLE_PM_SPEC = Path(__file__).resolve().parents[1] / "examples/pm_spec.yaml"


class PMCompilerTests(unittest.TestCase):
    def test_compile_pm_spec_emits_manifest_bundles_and_envelopes(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            spec = load_pm_spec(EXAMPLE_PM_SPEC)

            result = compile_pm_spec(spec, repo_root)

            manifest = json.loads(Path(result.manifest_path).read_text(encoding="utf-8"))
            self.assertEqual(manifest["goal_id"], "company-ai-os-v1")
            self.assertEqual(manifest["initiative_id"], "growth-loop")
            self.assertEqual(len(result.context_bundle_paths), 2)
            self.assertEqual(len(result.envelope_paths), 2)

            first_envelope = json.loads(Path(result.envelope_paths[0]).read_text(encoding="utf-8"))
            self.assertEqual(first_envelope["epic_id"], "activation-fix")
            self.assertEqual(first_envelope["task_id"], "signup-dropoff-audit")
            self.assertEqual(
                first_envelope["context_bundle_ref"],
                "ops/context_bundles/growth-loop__activation-fix__signup-dropoff-audit.json",
            )
            self.assertTrue((repo_root / first_envelope["context_bundle_ref"]).exists())


if __name__ == "__main__":
    unittest.main()
