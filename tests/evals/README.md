# 100x PM Evals Framework

This module provides evaluation criteria for assessing 100x PM command outputs.

## Overview

The evals framework evaluates command outputs across four dimensions:
- **Completeness**: Does the output include all necessary sections?
- **Accuracy**: Are the conclusions supported by evidence?
- **Actionability**: Can the output be directly acted upon?
- **Format**: Is the output in the expected format?

## Usage

```python
from tests.evals.framework import evaluate_command_output, calculate_pass_rate

# Evaluate a command output
results = evaluate_command_output("find-winning-direction", output_text)

# Calculate pass rate
pass_rate = calculate_pass_rate(results)
print(f"Pass rate: {pass_rate:.0%}")
```

## Supported Commands

- `find-winning-direction` - Market direction analysis
- `agent-prd` - Product Requirements Document generation
- `write-prd` - PRD writing
- `validate-product-direction` - Product direction validation

## Evaluation Criteria

Each command is evaluated on multiple criteria with weighted scores.

## Running Evals

```bash
# Run the framework test
python -m tests.evals.framework
```
