# 100x PM - Product Strategy OS

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-0.1.0-orange)](https://pypi.org/project/100xpm/)

Turn rough ideas into product direction, executive-ready PRDs, and roadmaps.

## Is 100x PM Right for You?

- **Yes** if you're a founder with a rough idea and need strategic direction
- **Yes** if you're a PM validating product directions before roadmap planning
- **Yes** if you need executive-ready PRDs that hold up in meetings
- **No** if you need full autonomous company orchestration
- **No** if you need high-fidelity digital twin visualization
- **No** if you need multi-tenant enterprise controls

## Features

- **Product Direction Pack** - Generate comprehensive product strategy documents
- **PRD Generation** - Create professional Product Requirements Documents
- **Market Validation** - Analyze signals and validate product directions
- **Roadmap Planning** - Build actionable implementation roadmaps

## Demo

```bash
$ 100xpm deploy --text "AI-powered meal planning app for busy professionals"

Running in shape mode...
Input source: text
Initializing LightCube engine...
Success! Output written to:
  - decision-pack.md
  - decision-pack.json
```

### Sample Output

The generated `decision-pack.md` includes:

- **Executive Summary** - One-paragraph strategic recommendation
- **Signal Brief** - Evidence and market signals analyzed
- **Problem Map** - Key challenges identified
- **Conditional Validation Stack** - 5-layer validation framework
- **Strategy Memo** - Target user, wedge, core flow
- **PRD** - Build-ready requirements
- **Roadmap** - 0-30-60-90 day plan
- **Tasks** - Engineering-ready task list

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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License
