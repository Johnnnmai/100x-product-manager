from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .agent_fleet import resolve_fleet
from .config import load_settings
from .contracts import ApprovalStatus, DiscordEvent, TaskEnvelope
from .context_hub import fetch_doc
from .discord_bridge import (
    create_approval_request,
    emit_event,
    event_from_approval,
    resolve_approval_request,
)
from .evidence_worker import ingest_url
from .legacy_adapter import build_paperclip_run_request, queue_legacy_task, queue_paperclip_request
from .local_worker import run_local_worker_once
from .ops_state import summarize_status
from .order_flow import dispatch_order
from .pm_compiler import compile_pm_spec, load_pm_spec
from .paperclip_watchdog import run_paperclip_watchdog
from .secret_audit import scan_repo
from .swarm_supervisor import run_swarm_supervisor
from .strategy_lab import load_forecast_request, persist_mock_forecast


def _load_envelope(path: Path) -> TaskEnvelope:
    return TaskEnvelope.model_validate_json(path.read_text(encoding="utf-8"))


def _emit(value: object) -> None:
    text = str(value)
    sys.stdout.buffer.write((text + "\n").encode(sys.stdout.encoding or "utf-8", errors="backslashreplace"))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="ai-os")
    subparsers = parser.add_subparsers(dest="command", required=True)

    compile_parser = subparsers.add_parser("compile-pm")
    compile_parser.add_argument("--input", required=True)
    compile_parser.add_argument("--repo-root", default=".")

    legacy_parser = subparsers.add_parser("enqueue-legacy")
    legacy_parser.add_argument("--envelope", required=True)
    legacy_parser.add_argument("--repo-root", default=".")

    paperclip_parser = subparsers.add_parser("queue-paperclip")
    paperclip_parser.add_argument("--envelope", required=True)
    paperclip_parser.add_argument("--repo-root", default=".")
    paperclip_parser.add_argument("--company-id")

    approval_parser = subparsers.add_parser("request-approval")
    approval_parser.add_argument("--envelope", required=True)
    approval_parser.add_argument("--repo-root", default=".")

    resolve_parser = subparsers.add_parser("resolve-approval")
    resolve_parser.add_argument("--approval-id", required=True)
    resolve_parser.add_argument(
        "--status",
        choices=[status.value for status in ApprovalStatus],
        required=True,
    )
    resolve_parser.add_argument("--actor", required=True)
    resolve_parser.add_argument("--notes", default="")
    resolve_parser.add_argument("--repo-root", default=".")

    discord_parser = subparsers.add_parser("emit-discord-event")
    discord_parser.add_argument("--event", required=True)
    discord_parser.add_argument("--repo-root", default=".")

    context_parser = subparsers.add_parser("fetch-context")
    context_parser.add_argument("--doc-id", required=True)
    context_parser.add_argument("--lang", default="py")
    context_parser.add_argument("--repo-root", default=".")

    evidence_parser = subparsers.add_parser("ingest-evidence")
    evidence_parser.add_argument("--url", required=True)
    evidence_parser.add_argument("--slug")
    evidence_parser.add_argument("--repo-root", default=".")

    forecast_parser = subparsers.add_parser("mock-forecast")
    forecast_parser.add_argument("--input", required=True)
    forecast_parser.add_argument("--repo-root", default=".")

    dispatch_parser = subparsers.add_parser("dispatch-order")
    dispatch_parser.add_argument("--input", required=True)
    dispatch_parser.add_argument("--task-id")
    dispatch_parser.add_argument("--repo-root", default=".")
    dispatch_parser.add_argument("--company-id")

    status_parser = subparsers.add_parser("status")
    status_parser.add_argument("--repo-root", default=".")

    fleet_parser = subparsers.add_parser("fleet-check")
    fleet_parser.add_argument("--repo-root", default=".")

    worker_parser = subparsers.add_parser("run-local-worker")
    worker_parser.add_argument("--agent-key", default="local_builder")
    worker_parser.add_argument("--task-id")
    worker_parser.add_argument("--repo-root", default=".")
    worker_parser.add_argument("--dry-run", action="store_true")

    supervisor_parser = subparsers.add_parser("run-swarm-supervisor")
    supervisor_parser.add_argument("--repo-root", default=".")
    supervisor_parser.add_argument("--agent-key", action="append", dest="agent_keys")
    supervisor_parser.add_argument("--sleep-seconds", type=int, default=90)
    supervisor_parser.add_argument("--timeout-ms", type=int, default=600000)
    supervisor_parser.add_argument("--max-cycles", type=int)
    supervisor_parser.add_argument("--once", action="store_true")

    watchdog_parser = subparsers.add_parser("run-paperclip-watchdog")
    watchdog_parser.add_argument("--repo-root", default=".")
    watchdog_parser.add_argument("--api-base")
    watchdog_parser.add_argument("--instance", default="default")
    watchdog_parser.add_argument("--check-interval-seconds", type=int, default=30)
    watchdog_parser.add_argument("--once", action="store_true")

    secret_parser = subparsers.add_parser("secret-scan")
    secret_parser.add_argument("--repo-root", default=".")

    args = parser.parse_args(argv)
    repo_root = Path(getattr(args, "repo_root", ".")).resolve()
    settings = load_settings(repo_root)

    if args.command == "compile-pm":
        spec = load_pm_spec(Path(args.input))
        result = compile_pm_spec(spec, repo_root)
        _emit(json.dumps(result.model_dump(mode="json"), ensure_ascii=True, indent=2))
        return

    if args.command == "enqueue-legacy":
        task_path = queue_legacy_task(_load_envelope(Path(args.envelope)), repo_root)
        _emit(task_path)
        return

    if args.command == "queue-paperclip":
        envelope = _load_envelope(Path(args.envelope))
        company_id = args.company_id or settings.paperclip_company_id
        request = build_paperclip_run_request(envelope, company_id)
        outbox_path = queue_paperclip_request(request, repo_root)
        _emit(outbox_path)
        return

    if args.command == "request-approval":
        envelope = _load_envelope(Path(args.envelope))
        approval = create_approval_request(envelope, repo_root)
        event = event_from_approval(approval)
        delivery = emit_event(
            event,
            repo_root,
            settings.discord_bot_token,
            settings.discord_channel_id,
        )
        _emit(
            json.dumps(
                {"approval_id": approval.approval_id, **delivery.model_dump()},
                ensure_ascii=True,
                indent=2,
            )
        )
        return

    if args.command == "resolve-approval":
        path = resolve_approval_request(
            args.approval_id,
            ApprovalStatus(args.status),
            args.actor,
            args.notes,
            repo_root,
        )
        _emit(path)
        return

    if args.command == "emit-discord-event":
        event = DiscordEvent.model_validate_json(Path(args.event).read_text(encoding="utf-8"))
        delivery = emit_event(
            event,
            repo_root,
            settings.discord_bot_token,
            settings.discord_channel_id,
        )
        _emit(json.dumps(delivery.model_dump(mode="json"), ensure_ascii=True, indent=2))
        return

    if args.command == "fetch-context":
        path = fetch_doc(args.doc_id, args.lang, repo_root)
        _emit(path)
        return

    if args.command == "ingest-evidence":
        ref = ingest_url(args.url, repo_root, args.slug)
        _emit(json.dumps(ref.model_dump(mode="json"), ensure_ascii=True, indent=2))
        return

    if args.command == "mock-forecast":
        report_path = persist_mock_forecast(load_forecast_request(Path(args.input)), repo_root)
        _emit(report_path)
        return

    if args.command == "dispatch-order":
        result = dispatch_order(
            pm_spec_path=Path(args.input),
            repo_root=repo_root,
            company_id=args.company_id or settings.paperclip_company_id,
            task_id=args.task_id,
            discord_bot_token=settings.discord_bot_token,
            discord_channel_id=settings.discord_channel_id,
        )
        _emit(json.dumps(result.model_dump(mode="json"), ensure_ascii=True, indent=2))
        return

    if args.command == "status":
        _emit(json.dumps(summarize_status(repo_root), ensure_ascii=True, indent=2))
        return

    if args.command == "fleet-check":
        _emit(
            json.dumps(
                [item.model_dump(mode="json") for item in resolve_fleet(repo_root)],
                ensure_ascii=True,
                indent=2,
            )
        )
        return

    if args.command == "run-local-worker":
        result = run_local_worker_once(
            repo_root=repo_root,
            agent_key=args.agent_key,
            task_id=args.task_id,
            dry_run=args.dry_run,
        )
        _emit(json.dumps(result.model_dump(mode="json"), ensure_ascii=True, indent=2))
        return

    if args.command == "run-swarm-supervisor":
        snapshot = run_swarm_supervisor(
            repo_root=repo_root,
            agent_keys=args.agent_keys,
            sleep_seconds=args.sleep_seconds,
            timeout_ms=args.timeout_ms,
            max_cycles=args.max_cycles,
            once=args.once,
        )
        _emit(json.dumps(snapshot.model_dump(mode="json"), ensure_ascii=True, indent=2))
        return

    if args.command == "run-paperclip-watchdog":
        snapshot = run_paperclip_watchdog(
            repo_root=repo_root,
            api_base=args.api_base,
            instance=args.instance,
            check_interval_seconds=args.check_interval_seconds,
            once=args.once,
        )
        _emit(json.dumps(snapshot.model_dump(mode="json"), ensure_ascii=True, indent=2))
        return

    if args.command == "secret-scan":
        findings = scan_repo(repo_root)
        if findings:
            _emit(json.dumps([item.model_dump(mode="json") for item in findings], ensure_ascii=True, indent=2))
            raise SystemExit(1)
        _emit("No secrets detected.")


if __name__ == "__main__":
    main()
