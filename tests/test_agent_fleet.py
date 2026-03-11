import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from ai_os.agent_fleet import resolve_fleet


class AgentFleetTests(unittest.TestCase):
    def test_resolve_fleet_reports_cloud_core_blocked_and_local_fallback_ready_without_env(self) -> None:
        source_root = Path(__file__).resolve().parents[1]

        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            (repo_root / "paperclip/bootstrap").mkdir(parents=True, exist_ok=True)
            (repo_root / "paperclip/bin").mkdir(parents=True, exist_ok=True)

            agents_md = source_root / "AGENTS.md"
            if agents_md.exists():
                (repo_root / "AGENTS.md").write_text(agents_md.read_text(encoding="utf-8"), encoding="utf-8")
            else:
                (repo_root / "AGENTS.md").write_text("# Agents\n", encoding="utf-8")

            fleet_yaml = source_root / "paperclip/agent_fleet.yaml"
            if fleet_yaml.exists():
                (repo_root / "paperclip/agent_fleet.yaml").write_text(fleet_yaml.read_text(encoding="utf-8"), encoding="utf-8")

            for name in ("ceo_codex.md", "pm_compiler.md", "local_builder.md", "local_claude_builder.md"):
                bootstrap_src = source_root / "paperclip/bootstrap" / name
                if bootstrap_src.exists():
                    (repo_root / "paperclip/bootstrap" / name).write_text(bootstrap_src.read_text(encoding="utf-8"), encoding="utf-8")
                else:
                    (repo_root / "paperclip/bootstrap" / name).write_text(f"# {name}\nBootstrap\n", encoding="utf-8")

            for name in (
                "claude-paperclip.cmd",
                "codex-paperclip.cmd",
                "zoe-paperclip.cmd",
                "mira-paperclip.cmd",
                "forge-paperclip.cmd",
                "quill-paperclip.cmd",
            ):
                bin_src = source_root / "paperclip/bin" / name
                if bin_src.exists():
                    (repo_root / "paperclip/bin" / name).write_text(bin_src.read_text(encoding="utf-8"), encoding="utf-8")
                else:
                    (repo_root / "paperclip/bin" / name).write_text(f"echo {name}\n", encoding="utf-8")

            with patch.dict(os.environ, {}, clear=False):
                fleet = resolve_fleet(repo_root)

            by_key = {item.key: item for item in fleet}
            self.assertTrue(by_key["local_builder"].ready)
            self.assertTrue(by_key["local_claude_builder"].ready)
            self.assertTrue(by_key["ceo"].ready)
            self.assertTrue(by_key["pm_compiler"].ready)
            self.assertEqual(by_key["local_builder"].assignment_role, "local_codex_builder")
            self.assertEqual(by_key["pm_compiler"].assignment_role, "chief_of_staff")
            self.assertFalse(by_key["chief_of_staff"].ready)
            self.assertIn("missing_env:OPENCLAW_GATEWAY_CONTROL_URL", by_key["chief_of_staff"].blockers)
            self.assertFalse(by_key["cto_core"].ready)
            self.assertIn("missing_env:OPENCLAW_GATEWAY_BUILD_URL", by_key["cto_core"].blockers)
            self.assertFalse(by_key["qa_lead"].ready)
            self.assertIn("missing_env:OPENCLAW_GATEWAY_VERIFY_URL", by_key["qa_lead"].blockers)
            self.assertFalse(by_key["research_lead"].ready)
            self.assertIn("missing_env:OPENCLAW_GATEWAY_RESEARCH_URL", by_key["research_lead"].blockers)
            self.assertFalse(by_key["growth_lead"].ready)
            self.assertIn("missing_env:OPENCLAW_GATEWAY_CONTROL_URL", by_key["growth_lead"].blockers)
            self.assertFalse(by_key["cloud_exec_a"].ready)
            self.assertIn("missing_env:OPENCLAW_GATEWAY_BUILD_URL", by_key["cloud_exec_a"].blockers)
            self.assertFalse(by_key["cloud_verify_b"].ready)
            self.assertIn("missing_env:OPENCLAW_GATEWAY_VERIFY_URL", by_key["cloud_verify_b"].blockers)
            self.assertFalse(by_key["cloud_research_c"].ready)
            self.assertIn("missing_env:OPENCLAW_GATEWAY_RESEARCH_URL", by_key["cloud_research_c"].blockers)

    def test_workspace_alias_env_overrides_repo_root(self) -> None:
        source_root = Path(__file__).resolve().parents[1]

        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir) / "repo"
            alias_root = Path(tmpdir) / "alias"
            (repo_root / "paperclip/bootstrap").mkdir(parents=True, exist_ok=True)
            (repo_root / "paperclip/bin").mkdir(parents=True, exist_ok=True)
            (alias_root / "paperclip/bootstrap").mkdir(parents=True, exist_ok=True)
            (alias_root / "paperclip/bin").mkdir(parents=True, exist_ok=True)

            for root in (repo_root, alias_root):
                agents_md = source_root / "AGENTS.md"
                if agents_md.exists():
                    (root / "AGENTS.md").write_text(agents_md.read_text(encoding="utf-8"), encoding="utf-8")
                else:
                    (root / "AGENTS.md").write_text("# Agents\n", encoding="utf-8")

                fleet_yaml = source_root / "paperclip/agent_fleet.yaml"
                if fleet_yaml.exists():
                    (root / "paperclip/agent_fleet.yaml").write_text(fleet_yaml.read_text(encoding="utf-8"), encoding="utf-8")

                for name in ("ceo_codex.md", "pm_compiler.md", "local_builder.md", "local_claude_builder.md"):
                    bootstrap_src = source_root / "paperclip/bootstrap" / name
                    if bootstrap_src.exists():
                        (root / "paperclip/bootstrap" / name).write_text(bootstrap_src.read_text(encoding="utf-8"), encoding="utf-8")
                    else:
                        (root / "paperclip/bootstrap" / name).write_text(f"# {name}\nBootstrap\n", encoding="utf-8")

                for name in (
                    "claude-paperclip.cmd",
                    "codex-paperclip.cmd",
                    "zoe-paperclip.cmd",
                    "mira-paperclip.cmd",
                    "forge-paperclip.cmd",
                    "quill-paperclip.cmd",
                ):
                    bin_src = source_root / "paperclip/bin" / name
                    if bin_src.exists():
                        (root / "paperclip/bin" / name).write_text(bin_src.read_text(encoding="utf-8"), encoding="utf-8")
                    else:
                        (root / "paperclip/bin" / name).write_text(f"echo {name}\n", encoding="utf-8")

            with patch.dict(os.environ, {"PAPERCLIP_WORKSPACE_ROOT": str(alias_root)}, clear=False):
                fleet = resolve_fleet(repo_root)

            by_key = {item.key: item for item in fleet}
            self.assertEqual(by_key["local_builder"].working_directory, str(alias_root.absolute()))
            self.assertEqual(by_key["local_builder"].instructions_file, str((alias_root / "AGENTS.md").absolute()))
            self.assertEqual(
                by_key["local_builder"].command,
                str((alias_root / "paperclip/bin/forge-paperclip.cmd").absolute()),
            )

    def test_unicode_repo_root_prefers_existing_ascii_alias(self) -> None:
        source_root = Path(__file__).resolve().parents[1]

        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            repo_root = tmp_path / "个人项目"
            alias_root = Path("C:/paperclip-work/brand-book")
            (repo_root / "paperclip/bootstrap").mkdir(parents=True, exist_ok=True)
            (repo_root / "paperclip/bin").mkdir(parents=True, exist_ok=True)

            agents_md = source_root / "AGENTS.md"
            if agents_md.exists():
                (repo_root / "AGENTS.md").write_text(agents_md.read_text(encoding="utf-8"), encoding="utf-8")
            else:
                (repo_root / "AGENTS.md").write_text("# Agents\n", encoding="utf-8")

            fleet_yaml = source_root / "paperclip/agent_fleet.yaml"
            if fleet_yaml.exists():
                (repo_root / "paperclip/agent_fleet.yaml").write_text(fleet_yaml.read_text(encoding="utf-8"), encoding="utf-8")

            for name in ("ceo_codex.md", "pm_compiler.md", "local_builder.md", "local_claude_builder.md"):
                bootstrap_src = source_root / "paperclip/bootstrap" / name
                if bootstrap_src.exists():
                    (repo_root / "paperclip/bootstrap" / name).write_text(bootstrap_src.read_text(encoding="utf-8"), encoding="utf-8")
                else:
                    (repo_root / "paperclip/bootstrap" / name).write_text(f"# {name}\nBootstrap\n", encoding="utf-8")

            for name in (
                "claude-paperclip.cmd",
                "codex-paperclip.cmd",
                "zoe-paperclip.cmd",
                "mira-paperclip.cmd",
                "forge-paperclip.cmd",
                "quill-paperclip.cmd",
            ):
                bin_src = source_root / "paperclip/bin" / name
                if bin_src.exists():
                    (repo_root / "paperclip/bin" / name).write_text(bin_src.read_text(encoding="utf-8"), encoding="utf-8")
                else:
                    (repo_root / "paperclip/bin" / name).write_text(f"echo {name}\n", encoding="utf-8")

            if not alias_root.exists():
                self.skipTest("ASCII alias root is not present on this machine")

            with patch.dict(os.environ, {}, clear=False):
                fleet = resolve_fleet(repo_root)

            by_key = {item.key: item for item in fleet}
            self.assertEqual(by_key["local_builder"].working_directory, str(alias_root.absolute()))


if __name__ == "__main__":
    unittest.main()
