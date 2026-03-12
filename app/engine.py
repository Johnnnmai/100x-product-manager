from __future__ import annotations

from typing import Any

from .integrations import MiroFishAdapter, OasisAdapter, PaperclipAdapter, ScraplingAdapter
from .models import DecisionPack, RunRequest, SignalItem, TaskItem, ValidationLayer
from .utils import make_run_id


class LightCubeEngine:
    def __init__(self) -> None:
        self.scrapling = ScraplingAdapter()
        self.oasis = OasisAdapter()
        self.mirofish = MiroFishAdapter()
        self.paperclip = PaperclipAdapter()

    async def run(self, req: RunRequest) -> tuple[DecisionPack, dict[str, Any]]:
        run_id = make_run_id(req.mode.value)
        signals = await self.scrapling.collect(
            url=str(req.url) if req.url else None,
            idea=req.idea,
            context=req.context,
        )
        problem_map = self._build_problem_map(req, signals)
        validation_stack = self._build_validation_stack(req, signals)
        strategy_memo = self._build_strategy_memo(req, signals, problem_map)
        forecast = await self.mirofish.forecast(strategy_memo)
        simulation_summary = await self.oasis.simulate(req.mode.value, signals)
        simulation_summary["forecast"] = forecast
        prd = self._build_prd(req, strategy_memo)
        roadmap = self._build_roadmap(strategy_memo)
        tasks = self._build_tasks(strategy_memo)
        paperclip_export = await self.paperclip.export_tasks(tasks)

        pack = DecisionPack(
            project_name=req.project_name,
            run_id=run_id,
            mode=req.mode,
            executive_summary=self._build_summary(req, signals, strategy_memo),
            signal_brief=signals,
            problem_map=problem_map,
            conditional_validation_stack=validation_stack,
            strategy_memo=strategy_memo,
            prd=prd,
            roadmap=roadmap,
            tasks=tasks,
            simulation_summary=simulation_summary,
            metadata={"paperclip": paperclip_export},
        )
        return pack, paperclip_export

    def _build_problem_map(self, req: RunRequest, signals: list[SignalItem]) -> list[str]:
        if req.mode.value == "audit":
            return [
                "Positioning may be broader than the first convincing use case.",
                "First-value moment may arrive too late for cold traffic.",
                "Proof and social trust may be weaker than the product promise.",
                f"Observed signal anchors: {', '.join(s.title for s in signals[:3])}",
            ]
        return [
            "Core user and wedge may still be blended together.",
            "The product may solve too many adjacent jobs at once.",
            "Distribution logic is not yet tightly bound to the product loop.",
            f"Idea evidence anchors: {', '.join(s.title for s in signals[:3])}",
        ]

    def _build_validation_stack(self, req: RunRequest, signals: list[SignalItem]) -> list[ValidationLayer]:
        return [
            ValidationLayer(layer=1, claim="Target user enters the core flow", risk="unclear hook", signal_needed="landing page click or signup intent"),
            ValidationLayer(layer=2, claim="User reaches first value within one session", risk="time-to-value too slow", signal_needed="activation event completion"),
            ValidationLayer(layer=3, claim="User repeats the core loop", risk="value too episodic", signal_needed="7-day repeat behavior"),
            ValidationLayer(layer=4, claim="Users spread or invite naturally", risk="weak social or workflow pull", signal_needed="share or invite rate"),
            ValidationLayer(layer=5, claim="Channel scales without breaking economics", risk="CAC or effort too high", signal_needed="channel conversion and cost"),
        ]

    def _build_strategy_memo(self, req: RunRequest, signals: list[SignalItem], problem_map: list[str]) -> dict[str, Any]:
        if req.mode.value == "audit":
            target_user = "Founder or PM with an existing product and ambiguous growth friction"
            wedge = "product-direction audit before roadmap or feature expansion"
        else:
            target_user = "Founder or PM with a rough idea and no sharp wedge yet"
            wedge = "signal-backed idea shaping into a first buildable scope"
        return {
            "target_user": target_user,
            "wedge": wedge,
            "core_problem": problem_map[0],
            "core_flow": "Input context → collect signals → pressure-test direction → compile build plan",
            "distribution_hypothesis": "High-signal audits and decision packs can act as both acquisition and trust-building content.",
            "business_model": "Subscription with premium strategy runs and optional execution orchestration.",
            "evidence_used": [s.model_dump() for s in signals],
        }

    def _build_prd(self, req: RunRequest, strategy_memo: dict[str, Any]) -> dict[str, Any]:
        return {
            "title": f"{req.project_name} LightCube v1",
            "objective": "Turn messy product inputs into decision-ready direction and agent-ready execution.",
            "primary_user": strategy_memo["target_user"],
            "must_have_features": [
                "Input form for URL or idea",
                "Decision Pack generation",
                "Project run storage",
                "Task export for engineering execution",
            ],
            "non_goals": [
                "Full autonomous company orchestration",
                "High-fidelity digital twin visualization",
                "Multi-tenant enterprise controls in v1",
            ],
            "success_metrics": [
                "Time to first decision pack",
                "Manual edits after first pack",
                "Percent of generated tasks accepted by the team",
            ],
        }

    def _build_roadmap(self, strategy_memo: dict[str, Any]) -> list[dict[str, Any]]:
        return [
            {"window": "0-30 days", "goal": "Ship audit and shape workflows", "milestones": ["web form", "pack generation", "local storage"]},
            {"window": "31-60 days", "goal": "Close execution loop", "milestones": ["task status tracking", "run comparison", "team feedback capture"]},
            {"window": "61-90 days", "goal": "Add advanced simulation", "milestones": ["deeper OASIS scenarios", "optional MiroFish forecasting", "better evidence connectors"]},
        ]

    def _build_tasks(self, strategy_memo: dict[str, Any]) -> list[TaskItem]:
        return [
            TaskItem(title="Implement intake workflow", owner="eng", description="Build URL and idea submission flow.", priority="high"),
            TaskItem(title="Generate Decision Pack", owner="eng", description="Compile markdown and JSON outputs.", priority="high"),
            TaskItem(title="Review strategy wedge", owner="pm", description="Confirm target user and core wedge.", priority="high"),
            TaskItem(title="Design activation metric", owner="pm", description="Define first-value event and success threshold.", priority="medium"),
        ]

    def _build_summary(self, req: RunRequest, signals: list[SignalItem], strategy_memo: dict[str, Any]) -> str:
        source_hint = str(req.url) if req.url else "idea input"
        return (
            f"LightCube analyzed {source_hint} in {req.mode.value} mode and recommends focusing on "
            f"{strategy_memo['wedge']}. The strongest near-term move is to tighten the first convincing use case, "
            f"reduce time-to-value, and validate repeat behavior before broadening scope."
        )
