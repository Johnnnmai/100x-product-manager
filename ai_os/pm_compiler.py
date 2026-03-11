from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, Field

from .contracts import ContextBundle, PMSpec, TaskEnvelope
from .fs_utils import ensure_dir, load_yaml, to_repo_path, write_json


class CompileResult(BaseModel):
    manifest_path: str
    context_bundle_paths: list[str] = Field(default_factory=list)
    envelope_paths: list[str] = Field(default_factory=list)


def load_pm_spec(path: Path) -> PMSpec:
    return PMSpec.model_validate(load_yaml(path))


def compile_pm_spec(spec: PMSpec, repo_root: Path) -> CompileResult:
    context_dir = ensure_dir(repo_root / "ops/context_bundles")
    compiled_dir = ensure_dir(repo_root / "ops/tasks/compiled")
    artifact_root = spec.artifact_root.strip("/") or "ops/artifacts"

    result = CompileResult(manifest_path="")
    manifest: dict[str, object] = {
        "goal_id": spec.goal_id,
        "mission": spec.mission,
        "initiative_id": spec.initiative_id,
        "initiative_title": spec.initiative_title,
        "epics": [],
    }

    for epic in spec.epics:
        epic_manifest: dict[str, object] = {
            "epic_id": epic.epic_id,
            "title": epic.title,
            "tasks": [],
        }
        for task in epic.tasks:
            bundle_id = f"{spec.initiative_id}__{epic.epic_id}__{task.task_id}"
            bundle = ContextBundle(
                bundle_id=bundle_id,
                mission=spec.mission,
                constraints=[*spec.constraints, *epic.constraints, *task.constraints],
                evidence_refs=[*epic.evidence_refs, *task.evidence_refs],
                glossary=spec.glossary,
                latest_decisions=spec.latest_decisions,
            )
            bundle_path = write_json(
                context_dir / f"{bundle_id}.json",
                bundle.model_dump(mode="json"),
            )

            artifact_output_path = (
                task.artifact_output_path
                or f"{artifact_root}/{spec.initiative_id}/{epic.epic_id}/{task.task_id}"
            )
            envelope = TaskEnvelope(
                envelope_id=bundle_id,
                goal_id=spec.goal_id,
                initiative_id=spec.initiative_id,
                initiative_title=spec.initiative_title,
                epic_id=epic.epic_id,
                task_id=task.task_id,
                title=task.title,
                executor_type=task.executor_type or epic.executor_type,
                budget_cap=task.budget_cap or epic.budget_cap,
                acceptance_criteria=task.acceptance_criteria or epic.acceptance_criteria,
                context_bundle_ref=to_repo_path(bundle_path, repo_root),
                artifact_output_path=artifact_output_path,
                approval_required=task.approval_required or epic.approval_required,
                mission=spec.mission,
                objective=task.objective,
                steps=task.steps,
                constraints=bundle.constraints,
                evidence_refs=bundle.evidence_refs,
                priority=task.priority,
            )
            envelope_path = write_json(
                compiled_dir / f"{bundle_id}.json",
                envelope.model_dump(mode="json"),
            )

            result.context_bundle_paths.append(str(bundle_path))
            result.envelope_paths.append(str(envelope_path))
            epic_manifest["tasks"].append(
                {
                    "task_id": task.task_id,
                    "envelope_path": to_repo_path(envelope_path, repo_root),
                    "context_bundle_ref": to_repo_path(bundle_path, repo_root),
                }
            )
        manifest["epics"].append(epic_manifest)

    manifest_path = write_json(
        compiled_dir / f"{spec.initiative_id}-manifest.json",
        manifest,
    )
    result.manifest_path = str(manifest_path)
    return result
