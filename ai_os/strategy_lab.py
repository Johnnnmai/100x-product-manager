from __future__ import annotations

from pathlib import Path

from .contracts import ForecastReport, ForecastRequest
from .fs_utils import ensure_dir, load_yaml, write_json


def load_forecast_request(path: Path) -> ForecastRequest:
    return ForecastRequest.model_validate(load_yaml(path))


def generate_mock_forecast(request: ForecastRequest) -> ForecastReport:
    scenario_summary = (
        f"Within {request.time_horizon}, the strongest scenario for "
        f"'{request.decision_question}' is a staged rollout with manual review gates."
    )
    key_drivers = [
        "bounded-context execution reduces coordination drift",
        "approval gates prevent runaway autonomous work",
        "evidence-backed planning improves roadmap confidence",
    ]
    risk_signals = [
        "missing owner for context boundaries",
        "budget thresholds not enforced at executor level",
        "prediction inputs dominated by weak or stale seed material",
    ]
    roadmap_implications = [
        "ship Paperclip control-plane integration before adding new worker types",
        "stabilize Discord approvals before automating more escalation paths",
        "treat Strategy Lab as an isolated lane until mock forecasts match operator expectations",
    ]
    return ForecastReport(
        report_id=f"report__{request.request_id}",
        request_id=request.request_id,
        scenario_summary=scenario_summary,
        key_drivers=key_drivers,
        risk_signals=risk_signals,
        roadmap_implications=roadmap_implications,
    )


def persist_mock_forecast(request: ForecastRequest, repo_root: Path) -> Path:
    request_dir = ensure_dir(repo_root / "ops/strategy_lab/requests")
    report_dir = ensure_dir(repo_root / "ops/strategy_lab/reports")
    write_json(
        request_dir / f"{request.request_id}.json",
        request.model_dump(mode="json"),
    )
    report = generate_mock_forecast(request)
    return write_json(
        report_dir / f"{report.report_id}.json",
        report.model_dump(mode="json"),
    )
