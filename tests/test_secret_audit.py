import tempfile
import unittest
from pathlib import Path

from ai_os.secret_audit import scan_repo


class SecretAuditTests(unittest.TestCase):
    def test_scan_repo_detects_github_and_discord_tokens(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            (repo_root / "safe.md").write_text("no secrets here", encoding="utf-8")
            findings = scan_repo(repo_root)
            self.assertEqual(findings, [])

            github_token = "gh" + "p_" + "abcdefghijklmnopqrstuvwxyz123456"
            discord_token = ".".join(
                [
                    "MTIzNDU2Nzg5MDEyMzQ1Njc4",
                    "abcdef",
                    "ABCDEFGHIJKLMNOPQRSTUVWX",
                ]
            )
            (repo_root / "bad.md").write_text(
                "\n".join(
                    [
                        f"github = {github_token}",
                        f"discord = {discord_token}",
                    ]
                ),
                encoding="utf-8",
            )

            findings = scan_repo(repo_root)
            finding_types = {item.secret_type for item in findings}
            self.assertEqual(finding_types, {"github_pat", "discord_bot_token"})


if __name__ == "__main__":
    unittest.main()
