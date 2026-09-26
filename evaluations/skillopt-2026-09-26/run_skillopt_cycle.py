#!/usr/bin/env python3
"""Run the reviewed boundary suite with stricter package-safe SkillOpt gates."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from hashlib import sha256
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skillopt-root", type=Path, required=True)
    parser.add_argument("--codex-path", type=Path, required=True)
    parser.add_argument("--state-home", type=Path, required=True)
    parser.add_argument("--backend", choices=("mock", "codex"), default="codex")
    parser.add_argument("--model", default="gpt-5.6-sol")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.state_home.exists() and any(args.state_home.iterdir()):
        raise SystemExit("state-home must be new or empty for an auditable run")
    args.state_home.mkdir(parents=True, exist_ok=True)

    repo = Path(__file__).resolve().parents[2]
    tasks_path = Path(__file__).with_name("tasks-boundary.json")
    skill_path = repo / "skills" / "ingenius-quant-finance" / "SKILL.md"
    baseline_skill_sha256 = sha256(skill_path.read_bytes()).hexdigest()
    tasks_sha256 = sha256(tasks_path.read_bytes()).hexdigest()

    sys.path.insert(0, str(args.skillopt_root))
    from skillopt_sleep.config import load_config
    from skillopt_sleep.cycle import run_sleep_cycle
    from skillopt_sleep.staging import json_safe
    from skillopt_sleep.tasks_file import load_tasks_file

    tasks, metadata = load_tasks_file(str(tasks_path))
    if metadata.get("reviewed") is not True:
        raise SystemExit("refusing to run an unreviewed tasks file")

    preferences = (
        "Modify only parent-owned, cross-domain behavior: activation boundaries, "
        "minimal module routing, and the non-execution permission boundary. Keep the "
        "existing progressive-disclosure architecture. Do not add finance-domain solver "
        "procedures, duplicate an existing rule, or generalize beyond these reviewed cases. "
        "Prefer at most three bullets, each under 35 words, and no net parent bloat unless "
        "a rule improves multiple routes."
    )
    cfg = load_config(
        invoked_project=str(repo),
        projects="invoked",
        state_dir=str(args.state_home / "skillopt-state"),
        backend=args.backend,
        model=args.model if args.backend == "codex" else "",
        optimizer_backend="",
        optimizer_model="",
        target_backend="",
        target_model="",
        codex_path=str(args.codex_path),
        claude_home=str(args.state_home / "claude"),
        target_skill_path=str(skill_path),
        max_tasks_per_night=len(tasks),
        max_tokens_per_night=400_000,
        edit_budget=3,
        preferences=preferences,
        progress=True,
        gate_mode="on",
        gate_metric="mixed",
        gate_mixed_weight=0.5,
        gate_no_regression=True,
        dream_rollouts=1,
        dream_factor=0,
        recall_k=0,
        evolve_skill=True,
        evolve_memory=False,
        llm_mine=False,
        target_task_filter=False,
        multi_skill_fanout=False,
        multi_skill_report=False,
        auto_adopt=False,
        redact_secrets=True,
        seed=42,
    )
    outcome = run_sleep_cycle(cfg, seed_tasks=tasks, dry_run=args.dry_run)
    report = outcome.report
    events = []
    evidence_path = Path(outcome.staging_dir) / "evidence.jsonl" if outcome.staging_dir else None
    if evidence_path and evidence_path.is_file():
        for line in evidence_path.read_text(encoding="utf-8").splitlines():
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    model_calls = [event for event in events if event.get("event") == "model_call"]
    test_scores = [
        event for event in events
        if event.get("stage") == "test" and event.get("event") == "held_out_score"
    ]
    result_events = [event for event in events if event.get("event") == "result"]
    result_health = {
        "n_results": len(result_events),
        "non_finite_scores": sum(
            not isinstance(event.get("hard"), (int, float))
            or not isinstance(event.get("soft"), (int, float))
            for event in result_events
        ),
        "empty_responses": sum(not event.get("response_head") for event in result_events),
    }
    diagnostics = {}
    diagnostics_path = Path(outcome.staging_dir) / "diagnostics.json" if outcome.staging_dir else None
    if diagnostics_path and diagnostics_path.is_file():
        diagnostics = json.loads(diagnostics_path.read_text(encoding="utf-8"))
    try:
        skillopt_sha = subprocess.run(
            ["git", "-C", str(args.skillopt_root), "rev-parse", "HEAD"],
            check=True, capture_output=True, text=True
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        skillopt_sha = "unknown"
    try:
        codex_version = subprocess.run(
            [str(args.codex_path), "--version"],
            check=True, capture_output=True, text=True
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        codex_version = "unknown"
    proposed_path = Path(outcome.staging_dir) / "proposed_SKILL.md" if outcome.staging_dir else None
    candidate = proposed_path.read_bytes() if proposed_path and proposed_path.is_file() else b""
    live_skill_sha256_after_run = sha256(skill_path.read_bytes()).hexdigest()
    payload = {
        "status": "candidate_accepted" if report.accepted else "candidate_rejected",
        "accepted": report.accepted,
        "gate_action": report.gate_action,
        "gate_no_regression": report.gate_no_regression,
        "baseline": report.baseline_score,
        "candidate": report.candidate_score,
        "n_tasks": report.n_tasks,
        "n_sessions": report.n_sessions,
        "tokens_used": report.tokens_used,
        "holdout_leaked": report.holdout_leaked,
        "gate_trials": report.gate_trials,
        "test_scores": test_scores,
        "result_health": result_health,
        "cache": {
            "model_calls": len(model_calls),
            "hits": sum(bool(event.get("cache_hit")) for event in model_calls),
            "misses": sum(not bool(event.get("cache_hit")) for event in model_calls),
        },
        "errors": {
            "call_error": diagnostics.get("call_error", ""),
            "judge_parse_failures": sum(
                "parse-failed" in str(item.get("why", ""))
                for item in diagnostics.get("holdout_detail", [])
            ),
        },
        "edits": [edit.__dict__ for edit in report.edits],
        "rejected_edits": [edit.__dict__ for edit in report.rejected_edits],
        "staging_dir": outcome.staging_dir,
        "adopted": outcome.adopted,
        "baseline_skill_sha256": baseline_skill_sha256,
        "live_skill_sha256_after_run": live_skill_sha256_after_run,
        "concurrent_mutation_detected": live_skill_sha256_after_run != baseline_skill_sha256,
        "candidate_skill_sha256": sha256(candidate).hexdigest() if candidate else "",
        "candidate_bytes": len(candidate),
        "tasks_sha256": tasks_sha256,
        "toolchain": {
            "skillopt_git_sha": skillopt_sha,
            "codex_path": str(args.codex_path),
            "codex_version": codex_version,
            "codex_home": os.environ.get("CODEX_HOME", str(Path.home() / ".codex")),
        },
        "effective_config": {
            key: cfg.get(key)
            for key in (
                "backend", "model", "optimizer_backend", "optimizer_model",
                "target_backend", "target_model", "gate_mode", "gate_metric",
                "gate_mixed_weight", "gate_no_regression", "edit_budget",
                "dream_rollouts", "dream_factor", "recall_k", "evolve_skill",
                "evolve_memory", "multi_skill_fanout", "auto_adopt", "seed"
            )
        },
        "limitations": [
            "Authored surrogate tasks, not mined production usage.",
            "Root text is injected; this is not a native skill-discovery or reference-read test.",
            "A mock-backend run is a control-flow smoke test only."
        ]
    }
    print(json.dumps(json_safe(payload), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
