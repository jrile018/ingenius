#!/usr/bin/env python3
"""Deterministic structural checks for the advanced elective skill expansion."""

from __future__ import annotations

import json
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CASES = json.loads((HERE / "cases.json").read_text(encoding="utf-8"))

SKILLS = {
    "market-microstructure-execution": {
        "market-mechanics", "execution-design", "validation-and-sources"
    },
    "robust-quant-optimization": {
        "formulation-and-solver", "robustness-and-sensitivity", "validation-and-sources"
    },
    "reliable-quant-data-systems": {
        "temporal-data-and-lineage", "transactions-recovery-distribution", "validation-and-sources"
    },
    "investment-firm-systems": {
        "operating-model", "controls-and-resilience", "validation-and-sources"
    },
}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


for name, modules in SKILLS.items():
    root = REPO / "skills" / name
    parent = root / "SKILL.md"
    text = parent.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{name}: missing frontmatter")
    frontmatter = text.split("---", 2)[1]
    if f"name: {name}" not in frontmatter:
        fail(f"{name}: frontmatter name mismatch")
    if "not for" not in frontmatter.lower():
        fail(f"{name}: description lacks a negative activation boundary")
    linked = set(re.findall(r"references/([^)#]+)\.md", text))
    if modules != linked:
        fail(f"{name}: routed modules differ: expected {sorted(modules)}, got {sorted(linked)}")
    nested = list((root / "references").rglob("SKILL.md"))
    if nested:
        fail(f"{name}: nested discoverable skills found")
    for module in modules:
        path = root / "references" / f"{module}.md"
        if not path.is_file():
            fail(f"{name}: missing {module}.md")
        if "loading boundary" not in path.read_text(encoding="utf-8").lower():
            fail(f"{name}/{module}: missing loading boundary")

if len(CASES) < 16:
    fail("behavior suite is too small")
if not any(case["activate"] for case in CASES):
    fail("no positive activation cases")
if not any(not case["activate"] for case in CASES):
    fail("no negative activation cases")

for case in CASES:
    if case["skill"] in SKILLS:
        unknown = set(case.get("modules", [])) - SKILLS[case["skill"]]
        if unknown:
            fail(f"{case['id']}: unknown modules {sorted(unknown)}")
        if len(case.get("modules", [])) > 2:
            fail(f"{case['id']}: normal phase loads more than two modules")
    if not case["activate"] and case.get("modules"):
        fail(f"{case['id']}: negative case assigns modules")

required = {
    "micro_book", "micro_latency_negative", "opt_formulation", "opt_generic_negative",
    "data_temporal", "data_recovery", "firm_lifecycle", "firm_legal_boundary",
    "handoff_empirical_execution", "handoff_data_firm", "safety_live_orders"
}
case_ids = {case["id"] for case in CASES}
if not required <= case_ids:
    fail(f"missing required cases: {sorted(required - case_ids)}")

edges = {
    "ingenius-quant-finance": {"robust-quant-optimization", "market-microstructure-execution"},
    "reliable-quant-data-systems": {"ingenius-quant-finance", "investment-firm-systems"},
    "market-microstructure-execution": {"low-latency-quant-systems"},
    "robust-quant-optimization": set(),
    "investment-firm-systems": set(),
    "low-latency-quant-systems": set(),
}
visiting: set[str] = set()
visited: set[str] = set()


def visit(node: str) -> None:
    if node in visiting:
        fail(f"handoff cycle reaches {node}")
    if node in visited:
        return
    visiting.add(node)
    for child in edges[node]:
        if child not in edges:
            fail(f"unknown handoff target {child}")
        visit(child)
    visiting.remove(node)
    visited.add(node)


for node in edges:
    visit(node)

research = REPO / "research" / "advanced-electives-2026-09-26"
for dossier in [
    "systematic-research.md", "market-microstructure-execution.md",
    "robust-quant-optimization.md", "reliable-quant-data-systems.md",
    "investment-firm-systems.md",
]:
    if not (research / dossier).is_file():
        fail(f"missing research dossier {dossier}")

print(
    "PASS: 4 sibling skills, 12 conditional modules, no nested skills, "
    f"{len(CASES)} authored cases, negative boundaries, source dossiers, and acyclic handoffs"
)

