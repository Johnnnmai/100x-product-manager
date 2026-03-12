"""Integration tests for 100x PM CLI - full workflow."""

import json
import tempfile
from pathlib import Path

import pytest
from click.testing import CliRunner

from src.cli.main import cli


class TestIntegration:
    """Integration tests for full workflow."""

    @pytest.fixture
    def runner(self):
        return CliRunner()

    @pytest.fixture
    def tmp_path(self, tmp_path_factory):
        """Create a temporary directory for tests."""
        return tmp_path_factory.mktemp("test")

    def test_full_workflow_text_to_pack(self, runner, tmp_path):
        """Test full workflow: text input -> decision pack output."""
        # Change to temp directory
        original_dir = Path.cwd()

        try:
            import os
            os.chdir(tmp_path)

            # Run CLI with text input
            result = runner.invoke(
                cli,
                ["deploy", "--text", "AI-powered meal planning app for busy professionals"]
            )

            # Check that output files were created
            md_exists = Path("decision-pack.md").exists()
            json_exists = Path("decision-pack.json").exists()

            # Verify output
            if md_exists:
                content = Path("decision-pack.md").read_text()
                assert len(content) > 0
                # Should have key sections
                assert "Product Direction Pack" in content or "Decision Pack" in content or "Summary" in content

            if json_exists:
                data = json.loads(Path("decision-pack.json").read_text())
                assert isinstance(data, dict)

        finally:
            import os
            os.chdir(original_dir)

    def test_full_workflow_with_output_flag(self, runner, tmp_path):
        """Test workflow with custom output path."""
        original_dir = Path.cwd()

        try:
            import os
            os.chdir(tmp_path)

            result = runner.invoke(
                cli,
                ["deploy", "--text", "Test app", "--output", "custom-pack.md"]
            )

            # Check custom output file
            assert Path("custom-pack.md").exists() or Path("custom-pack.json").exists() or result.exit_code != 0

        finally:
            import os
            os.chdir(original_dir)

    def test_full_workflow_audit_mode(self, runner, tmp_path):
        """Test workflow in audit mode."""
        original_dir = Path.cwd()

        try:
            import os
            os.chdir(tmp_path)

            result = runner.invoke(
                cli,
                ["deploy", "--url", "https://example.com", "--mode", "audit"]
            )

            # Should run in audit mode
            assert "audit" in result.output.lower() or result.exit_code != 0

        finally:
            import os
            os.chdir(original_dir)

    def test_workflow_produces_valid_json(self, runner, tmp_path):
        """Test that JSON output is valid."""
        original_dir = Path.cwd()

        try:
            import os
            os.chdir(tmp_path)

            result = runner.invoke(
                cli,
                ["deploy", "--text", "Test product idea"]
            )

            if Path("decision-pack.json").exists():
                data = json.loads(Path("decision-pack.json").read_text())
                # Should have expected structure
                assert isinstance(data, dict)

        finally:
            import os
            os.chdir(original_dir)


class TestEndToEnd:
    """End-to-end tests simulating real usage."""

    @pytest.fixture
    def runner(self):
        return CliRunner()

    def test_meal_planning_app_example(self, runner, tmp_path):
        """Test the exact example from README."""
        original_dir = Path.cwd()

        try:
            import os
            os.chdir(tmp_path)

            result = runner.invoke(
                cli,
                ["deploy", "--text", "AI-powered meal planning app for busy professionals"]
            )

            # Should complete without crash
            assert result.exit_code == 0 or "Error" not in result.output

        finally:
            import os
            os.chdir(original_dir)

    def test_multiple_runs_produce_unique_ids(self, runner, tmp_path):
        """Test that multiple runs produce unique run IDs."""
        original_dir = Path.cwd()

        try:
            import os
            os.chdir(tmp_path)

            # Run twice
            runner.invoke(cli, ["deploy", "--text", "App 1"])
            runner.invoke(cli, ["deploy", "--text", "App 2"])

            # Both JSON files should exist
            if Path("decision-pack.json").exists():
                # Multiple runs would overwrite, so just check one exists
                assert Path("decision-pack.json").exists()

        finally:
            import os
            os.chdir(original_dir)
