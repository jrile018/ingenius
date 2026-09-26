#!/usr/bin/env python3
"""Deterministic structural and context-budget checks for the Ingenius skill tree."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-path", type=Path)
    parser.add_argument("--package-root", type=Path)
    parser.add_argument("--baseline-skill-path", type=Path)
    parser.add_argument("--baseline-git-ref")
    parser.add_argument("--max-added-words", type=int, default=40)
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[2]
    package = args.package_root or repo / "skills" / "ingenius-quant-finance"
    root = args.skill_path or package / "SKILL.md"
    text = root.read_text(encoding="utf-8")
    skill_files = sorted(package.rglob("SKILL.md"))
    linked = sorted(set(re.findall(r"\]\((references/[^)#]+\.md)\)", text)))
    missing = [path for path in linked if not (package / path).is_file()]
    description_match = re.search(r"^description:\s*(.+)$", text, re.MULTILINE)
    description = description_match.group(1).strip() if description_match else ""
    agent_text = (package / "agents" / "openai.yaml").read_text(encoding="utf-8")

    baseline_words = None
    if args.baseline_skill_path:
        baseline_words = len(args.baseline_skill_path.read_text(encoding="utf-8").split())
    elif args.baseline_git_ref:
        relative_root = (package / "SKILL.md").relative_to(repo).as_posix()
        baseline_text = subprocess.run(
            ["git", "show", f"{args.baseline_git_ref}:{relative_root}"],
            cwd=repo,
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        baseline_words = len(baseline_text.split())

    checks = {
        "exactly_one_skill_md": len(skill_files) == 1,
        "all_parent_links_resolve": not missing,
        "all_reference_files_are_reachable": {
            path.relative_to(package).as_posix() for path in package.glob("references/*.md")
        }.issubset(set(linked)),
        "default_prompt_names_skill": "$ingenius-quant-finance" in agent_text,
        "description_is_discriminating": (
            "financial applications" in description
            and "generic statistics or mathematics" in description
        ),
        "root_word_budget_le_750": len(text.split()) <= 750,
        "description_character_budget_le_600": len(description) <= 600,
        "baseline_relative_word_growth_within_limit": (
            baseline_words is None
            or len(text.split()) - baseline_words <= args.max_added_words
        ),
    }
    result = {
        "passed": all(checks.values()),
        "checks": checks,
        "metrics": {
            "root_words": len(text.split()),
            "root_bytes": len(text.encode("utf-8")),
            "description_characters": len(description),
            "baseline_words": baseline_words,
            "added_words": None if baseline_words is None else len(text.split()) - baseline_words,
            "linked_references": linked,
            "missing_references": missing,
            "skill_md_files": [path.relative_to(repo).as_posix() for path in skill_files],
        },
        "note": "Word and byte budgets are deterministic bloat guards, not model token or billing measurements.",
    }
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
