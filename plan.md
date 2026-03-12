# 100x PM / LightCube Project - Ralph Loop Task List

## Overview
Building a CLI tool that helps PMs and founders turn rough ideas into product direction, executive-ready PRDs, and roadmaps.

**Success Gate**: CLI tool working, outputting Product Direction Pack, ready for GitHub

---

## Task List
```json
[
  {
    "category": "setup",
    "description": "Create project directory structure",
    "steps": [
      "Create app/ directory for LightCube core",
      "Create src/cli/ directory for CLI",
      "Create tests/evals/ directory for Evals",
      "Verify directories exist"
    ],
    "passes": true
  },
  {
    "category": "integration",
    "description": "Integrate LightCube v1 core code",
    "steps": [
      "Copy app/engine.py from company_asset",
      "Copy app/integrations.py from company_asset",
      "Copy app/models.py from company_asset",
      "Copy app/main.py from company_asset",
      "Verify imports work"
    ],
    "passes": true
  },
  {
    "category": "integration",
    "description": "Integrate existing 100x PM commands",
    "steps": [
      "Copy commands/ from 100x-product-managers",
      "Verify commands accessible",
      "Test command loading"
    ],
    "passes": true
  },
  {
    "category": "cli",
    "description": "Add CLI entry point",
    "steps": [
      "Create src/cli/main.py with Click",
      "Implement deploy command",
      "Support --text, --url, --path, --json flags",
      "Test CLI works"
    ],
    "passes": true
  },
  {
    "category": "cli",
    "description": "Connect CLI to LightCube engine",
    "steps": [
      "Wire deploy command to engine.run()",
      "Test full workflow: input -> pack -> output",
      "Verify decision-pack.md generation"
    ],
    "passes": true
  },
  {
    "category": "evals",
    "description": "Add Skills Evals framework",
    "steps": [
      "Create tests/evals/ directory",
      "Define evaluation criteria for commands",
      "Write test prompts for good output",
      "Verify Evals framework works"
    ],
    "passes": true
  },
  {
    "category": "evals",
    "description": "Run Evals on key commands",
    "steps": [
      "Test find-winning-direction command",
      "Test agent-prd command",
      "Verify pass rate >10%"
    ],
    "passes": true
  },
  {
    "category": "readme",
    "description": "Write professional README",
    "steps": [
      "Write product definition",
      "Write installation instructions",
      "Write usage examples",
      "Write output format documentation"
    ],
    "passes": true
  },
  {
    "category": "verification",
    "description": "Final verification",
    "steps": [
      "Run full CLI test",
      "Verify decision-pack output",
      "Run all Evals",
      "Verify ready for GitHub"
    ],
    "passes": true
  }
]
```

---

## Completion Criteria
- [ ] All tasks have "passes": true
- [ ] CLI command works: 100xpm deploy --text "..."
- [ ] Output format correct (decision-pack.md/json)
- [ ] Evals validate command quality
- [ ] README complete and professional
