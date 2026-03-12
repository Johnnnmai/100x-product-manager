"""
100x PM CLI - Command line interface for Product Direction Pack generation.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import click


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """100x PM - Turn rough ideas into product direction, executive-ready PRDs, and roadmaps."""
    pass


@cli.command()
@click.option("--text", "input_text", help="Product idea or description text")
@click.option("--url", "input_url", help="URL to analyze (website/product audit)")
@click.option("--path", "input_path", type=click.Path(exists=True), help="Path to existing spec/context file")
@click.option("--json", "input_json", type=click.Path(exists=True), help="JSON file with structured input")
@click.option("--mode", type=click.Choice(["audit", "idea", "vision"]), default="idea", help="Analysis mode")
@click.option("--output", "-o", type=click.Path(), help="Output file path (default: decision-pack.md)")
def deploy(input_text: str, input_url: str, input_path: str, input_json: str, mode: str, output: str):
    """
    Generate a Product Direction Pack from various input sources.

    Examples:

        # From text idea
        100xpm deploy --text "AI-powered meal planning app for busy professionals"

        # From website audit
        100xpm deploy --url "https://example.com" --mode audit

        # From existing file
        100xpm deploy --path ./spec.yaml

        # From JSON
        100xpm deploy --json input.json
    """
    # Validate input source
    input_source = None
    input_data = {}

    if input_text:
        input_source = "text"
        input_data["content"] = input_text
    elif input_url:
        input_source = "url"
        input_data["url"] = input_url
    elif input_path:
        input_source = "path"
        input_data["path"] = input_path
    elif input_json:
        input_source = "json"
        with open(input_json, "r") as f:
            input_data = json.load(f)
    else:
        click.echo("Error: Please provide one of: --text, --url, --path, or --json", err=True)
        sys.exit(1)

    click.echo(f"Running in {mode} mode...")
    click.echo(f"Input source: {input_source}")

    # TODO: Wire to LightCube engine
    click.echo("Engine integration pending - CLI structure ready")


@cli.command()
def list_commands():
    """List available 100x PM commands."""
    commands_dir = Path(__file__).parent.parent / "commands"
    if not commands_dir.exists():
        click.echo("No commands directory found")
        return

    cmd_files = list(commands_dir.glob("*.md"))
    click.echo("Available commands:")
    for f in sorted(cmd_files):
        click.echo(f"  - {f.stem}")


@cli.command()
@click.argument("command_file", type=click.Path(exists=True))
def show(command_file: str):
    """Show the contents of a command file."""
    with open(command_file, "r") as f:
        click.echo(f.read())


if __name__ == "__main__":
    cli()
