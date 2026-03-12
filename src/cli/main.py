"""
100x PM CLI - Command line interface for Product Direction Pack generation.
"""
from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

import click

# Import LightCube engine - will fail gracefully if not available
try:
    from app.engine import LightCubeEngine
    from app.models import RunMode, RunRequest
    ENGINE_AVAILABLE = True
except ImportError:
    ENGINE_AVAILABLE = False


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
@click.option("--mode", type=click.Choice(["audit", "shape"]), default="shape", help="Analysis mode")
@click.option("--output", "-o", type=click.Path(), help="Output file path (default: decision-pack.md)")
def deploy(input_text: str, input_url: str, input_path: str, input_json: str, mode: str, output: str):
    """
    Generate a Product Direction Pack from various input sources.

    Examples:

        # From text idea (shape mode)
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

    # Wire to LightCube engine if available
    if ENGINE_AVAILABLE:
        click.echo("Initializing LightCube engine...")

        # Map mode to RunMode
        mode_map = {
            "audit": RunMode.AUDIT,
            "shape": RunMode.SHAPE,
        }

        try:
            # Create run request
            req = RunRequest(
                project_name="cli-run",
                mode=mode_map[mode],
                url=input_data.get("url"),
                idea=input_data.get("content"),
                context=input_data.get("context"),
            )

            # Run the engine
            engine = LightCubeEngine()
            pack, export = asyncio.run(engine.run(req))

            # Determine output path
            if output is None:
                output = "decision-pack.md"

            output_path = Path(output)

            # Write decision pack
            from app.renderers import decision_pack_markdown
            output_path.write_text(decision_pack_markdown(pack), encoding="utf-8")

            # Also write JSON
            json_path = output_path.with_suffix(".json")
            json_path.write_text(pack.model_dump_json(indent=2), encoding="utf-8")

            click.echo(f"Success! Output written to:")
            click.echo(f"  - {output_path}")
            click.echo(f"  - {json_path}")

        except Exception as e:
            click.echo(f"Error running engine: {e}", err=True)
            sys.exit(1)
    else:
        click.echo("Engine not available - using CLI structure only")
        # Still create a basic output
        if output is None:
            output = "decision-pack.md"
        output_path = Path(output)
        output_path.write_text(f"# Product Direction Pack\n\nMode: {mode}\nSource: {input_source}\n", encoding="utf-8")
        click.echo(f"Basic output written to: {output_path}")


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
