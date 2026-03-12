from __future__ import annotations

from app.models import DecisionPack


def decision_pack_markdown(pack: DecisionPack) -> str:
    lines: list[str] = []
    lines.append(f"# {pack.project_name} Decision Pack")
    lines.append("")
    lines.append(f"- Run ID: `{pack.run_id}`")
    lines.append(f"- Mode: `{pack.mode.value}`")
    lines.append(f"- Created: `{pack.created_at}`")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append(pack.executive_summary)
    lines.append("")
    lines.append("## Signal Brief")
    for item in pack.signal_brief:
        lines.append(f"- **{item.title}** ({item.source}, confidence={item.confidence}): {item.summary}")
    lines.append("")
    lines.append("## Problem Map")
    for item in pack.problem_map:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Conditional Validation Stack")
    for layer in pack.conditional_validation_stack:
        lines.append(f"- L{layer.layer}: {layer.claim} | risk: {layer.risk} | signal: {layer.signal_needed}")
    lines.append("")
    lines.append("## Strategy Memo")
    for key, value in pack.strategy_memo.items():
        lines.append(f"- **{key}**: {value}")
    lines.append("")
    lines.append("## PRD")
    for key, value in pack.prd.items():
        lines.append(f"- **{key}**: {value}")
    lines.append("")
    lines.append("## Roadmap")
    for row in pack.roadmap:
        lines.append(f"- **{row['window']}**: {row['goal']} | milestones: {', '.join(row['milestones'])}")
    lines.append("")
    lines.append("## Tasks")
    for task in pack.tasks:
        lines.append(f"- **{task.title}** [{task.owner}/{task.priority}] {task.description}")
    lines.append("")
    lines.append("## Simulation Summary")
    for key, value in pack.simulation_summary.items():
        lines.append(f"- **{key}**: {value}")
    lines.append("")
    return "\n".join(lines)
