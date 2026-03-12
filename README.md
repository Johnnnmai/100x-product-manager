# 100x PM - Product Strategy OS

Turn rough ideas into product direction, executive-ready PRDs, and roadmaps.

## Overview

100x PM is a CLI tool that helps Product Managers and founders validate ideas, create strategic documents, and generate actionable roadmaps. Powered by LightCube AI engine.

## Features

- **Product Direction Pack** - Generate comprehensive product strategy documents
- **PRD Generation** - Create professional Product Requirements Documents
- **Market Validation** - Analyze signals and validate product directions
- **Roadmap Planning** - Build actionable implementation roadmaps

## Installation

```bash
# Clone the repository
git clone https://github.com/your-org/100x-pm.git
cd 100x-pm

# Install dependencies
pip install -r requirements.txt

# Install CLI
pip install -e .
```

## Quick Start

```bash
# Generate a product direction pack from an idea
100xpm deploy --text "AI-powered meal planning app for busy professionals"

# Analyze a website/product
100xpm deploy --url "https://example.com" --mode audit

# From a JSON file
100xpm deploy --json input.json
```

## CLI Commands

### deploy

Generate a Product Direction Pack from various input sources:

```bash
100xpm deploy --text "Your product idea"
100xpm deploy --url "https://example.com"
100xpm deploy --path ./spec.yaml
100xpm deploy --json input.json
```

Options:
- `--text TEXT` - Product idea or description text
- `--url TEXT` - URL to analyze (website/product audit)
- `--path PATH` - Path to existing spec/context file
- `--json PATH` - JSON file with structured input
- `--mode [audit|shape]` - Analysis mode (default: shape)
- `-o, --output PATH` - Output file path

### list-commands

List available 100x PM commands:

```bash
100xpm list-commands
```

### show

Show the contents of a command file:

```bash
100xpm show commands/find-winning-direction.md
```

## Output Format

The CLI generates two output files:

1. **decision-pack.md** - Markdown document with:
   - Executive Summary
   - Signal Brief
   - Problem Map
   - Conditional Validation Stack
   - Strategy Memo
   - PRD
   - Roadmap
   - Tasks

2. **decision-pack.json** - Structured JSON output

## Architecture

```
100x PM CLI
    |
    ├── src/cli/          # CLI entry point
    |   └── main.py       # Click-based CLI
    |
    ├── app/              # LightCube v1 core
    |   ├── engine.py     # Main engine
    |   ├── models.py     # Data models
    |   └── integrations.py
    |
    ├── commands/         # 100x PM commands
    |   ├── find-winning-direction.md
    |   ├── agent-prd.md
    |   └── ...
    |
    └── tests/evals/      # Evaluation framework
        └── framework.py
```

## Development

```bash
# Run tests
pytest tests/

# Run CLI
python -m src.cli.main --help
python -m src.cli.main deploy --text "test"
```

## License

MIT License
