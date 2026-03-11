import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class CLIEntrypointTests(unittest.TestCase):
    def test_python_m_ai_os_cli_executes_main(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "ai_os.cli",
                    "secret-scan",
                    "--repo-root",
                    str(repo_root),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("No secrets detected.", completed.stdout)


if __name__ == "__main__":
    unittest.main()
