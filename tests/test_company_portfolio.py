import tempfile
import unittest
from pathlib import Path

from ai_os.company_portfolio import load_company_portfolio
from ai_os.paperclip_provision import (
    build_project_create_body,
    build_workspace_create_body,
    live_agent_fleet_key,
)


class CompanyPortfolioTests(unittest.TestCase):
    def test_load_company_portfolio_reads_roomjoy_project(self) -> None:
        source_root = Path(__file__).resolve().parents[1]

        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            (repo_root / "paperclip").mkdir(parents=True, exist_ok=True)
            (repo_root / "paperclip/company_portfolio.yaml").write_text(
                (source_root / "paperclip/company_portfolio.yaml").read_text(encoding="utf-8"),
                encoding="utf-8",
            )

            portfolio = load_company_portfolio(str(repo_root / "paperclip/company_portfolio.yaml"))

            self.assertEqual(portfolio.company, "JM Strategy Lab")
            self.assertEqual(len(portfolio.projects), 2)
            # First project is internal-ai-os-v1
            internal_ai_os = portfolio.projects[0]
            self.assertEqual(internal_ai_os.key, "internal-ai-os-v1")
            self.assertEqual(internal_ai_os.lead_role, "ceo_codex")
            self.assertEqual(internal_ai_os.workspace.name, "brand-book")

    def test_live_agent_fleet_key_prefers_metadata(self) -> None:
        live_agent = {
            "urlKey": "qa-director",
            "metadata": {"fleet_key": "qa_lead"},
        }
        self.assertEqual(live_agent_fleet_key(live_agent), "qa_lead")

    def test_project_and_workspace_payloads_are_api_shaped(self) -> None:
        source_root = Path(__file__).resolve().parents[1]
        portfolio = load_company_portfolio(str(source_root / "paperclip/company_portfolio.yaml"))
        # First project is internal-ai-os-v1
        internal_ai_os = portfolio.projects[0]

        project_body = build_project_create_body(internal_ai_os, lead_agent_id="agent-123")
        workspace_body = build_workspace_create_body(internal_ai_os.key, internal_ai_os.workspace)

        self.assertEqual(project_body["name"], "Internal AI OS v1")
        self.assertEqual(project_body["leadAgentId"], "agent-123")
        self.assertEqual(workspace_body["cwd"], ".")
        self.assertTrue(workspace_body["isPrimary"])


if __name__ == "__main__":
    unittest.main()
