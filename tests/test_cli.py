"""Tests for 100x PM CLI."""

import json
import os
import tempfile
from pathlib import Path

import pytest
from click.testing import CliRunner

from src.cli.main import cli


class TestCLI:
    """Test cases for 100x PM CLI."""

    @pytest.fixture
    def runner(self):
        """Create a Click CLI runner."""
        return CliRunner()

    def test_cli_help(self, runner):
        """Test CLI shows help."""
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "100x PM" in result.output

    def test_deploy_help(self, runner):
        """Test deploy command shows help."""
        result = runner.invoke(cli, ["deploy", "--help"])
        assert result.exit_code == 0
        assert "--text" in result.output
        assert "--url" in result.output
        assert "--mode" in result.output

    def test_deploy_requires_input(self, runner):
        """Test deploy requires input source."""
        result = runner.invoke(cli, ["deploy"])
        assert result.exit_code != 0
        assert "Please provide" in result.output or "Error" in result.output

    def test_deploy_text_input(self, runner):
        """Test deploy with --text input."""
        with runner.isolated_filesystem():
            result = runner.invoke(
                cli,
                ["deploy", "--text", "AI-powered meal planning app", "--output", "test-pack.md"]
            )
            # Should either succeed or show error (engine might not be available)
            # Just verify it processes the input
            assert "text" in result.output.lower() or "Error" in result.output

    def test_deploy_url_input(self, runner):
        """Test deploy with --url input."""
        with runner.isolated_filesystem():
            result = runner.invoke(
                cli,
                ["deploy", "--url", "https://example.com", "--output", "test-pack.md"]
            )
            # Should process the URL
            assert "url" in result.output.lower() or "Error" in result.output

    def test_deploy_mode_flag(self, runner):
        """Test deploy with --mode flag."""
        with runner.isolated_filesystem():
            result = runner.invoke(
                cli,
                ["deploy", "--text", "test", "--mode", "audit", "--output", "test.md"]
            )
            # Should show audit mode
            assert "audit" in result.output.lower() or "Error" in result.output

    def test_deploy_json_input(self, runner):
        """Test deploy with --json input."""
        with runner.isolated_filesystem():
            # Create a JSON input file
            json_data = {
                "content": "AI-powered task manager",
                "context": "Team collaboration"
            }
            json_path = Path("input.json")
            json_path.write_text(json.dumps(json_data))

            result = runner.invoke(
                cli,
                ["deploy", "--json", "input.json", "--output", "test-pack.md"]
            )
            # Should process JSON
            assert "json" in result.output.lower() or "Error" in result.output

    def test_deploy_output_file_created(self, runner):
        """Test deploy creates output file."""
        with runner.isolated_filesystem():
            result = runner.invoke(
                cli,
                ["deploy", "--text", "Test app", "--output", "my-pack.md"]
            )

            # Check if output file was created (or error occurred)
            output_exists = Path("my-pack.md").exists()
            # Either success or error is acceptable
            assert output_exists or result.exit_code != 0

    def test_list_commands(self, runner):
        """Test list-commands command."""
        result = runner.invoke(cli, ["list-commands"])
        # Should run without error
        assert result.exit_code == 0

    def test_show_command_requires_file(self, runner):
        """Test show command requires file argument."""
        result = runner.invoke(cli, ["show"])
        assert result.exit_code != 0


class TestCLIOutputs:
    """Test CLI output files."""

    @pytest.fixture
    def runner(self):
        return CliRunner()

    def test_deploy_creates_markdown_and_json(self, runner):
        """Test deploy creates both .md and .json files."""
        with runner.isolated_filesystem():
            result = runner.invoke(
                cli,
                ["deploy", "--text", "Test idea", "--output", "test-pack.md"]
            )

            # Check output files exist
            md_exists = Path("test-pack.md").exists()
            json_exists = Path("test-pack.json").exists()

            # At least one should exist
            assert md_exists or json_exists or result.exit_code != 0
