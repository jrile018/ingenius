#!/usr/bin/env python3
"""Deterministic structural checks for the low-latency skill package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
SKILL = REPO / "skills" / "low-latency-quant-systems"
PARENT = SKILL / "SKILL.md"
REFERENCES = SKILL / "references"
CASES = HERE / "cases.json"
MIT_PARENT = REPO / "skills" / "mit-6172-performance-engineering" / "SKILL.md"

TECHNICAL = {
    "measurement-contract.md",
    "trading-correctness.md",
    "cpu-memory-compiler.md",
    "numerical-kernels.md",
    "concurrency-realtime.md",
    "networking-time.md",
    "system-architecture.md",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


text = PARENT.read_text(encoding="utf-8")
if not text.startswith("---\n"):
    fail("SKILL.md has no YAML frontmatter")
frontmatter = text.split("---", 2)[1]
if "name: low-latency-quant-systems" not in frontmatter:
    fail("frontmatter name does not match directory")
if "not for generic refactoring" not in frontmatter.lower():
    fail("description lacks a negative activation boundary")

links = re.findall(r"\]\((references/[^)#]+\.md)\)", text)
if not links:
    fail("parent has no routed reference links")
missing = [link for link in links if not (SKILL / link).is_file()]
if missing:
    fail(f"unresolved parent links: {missing}")

nested = [path for path in REFERENCES.rglob("SKILL.md")]
if nested:
    fail(f"nested discoverable skills found: {nested}")

found = {path.name for path in REFERENCES.glob("*.md")}
if not TECHNICAL <= found:
    fail(f"technical modules missing: {sorted(TECHNICAL - found)}")

for name in sorted(TECHNICAL):
    module = (REFERENCES / name).read_text(encoding="utf-8")
    if "loading boundary" not in module.lower():
        fail(f"{name} lacks an explicit loading boundary")

cases = json.loads(CASES.read_text(encoding="utf-8"))
if len(cases) < 10:
    fail("behavior suite is too small")
if not any(case["activate"] for case in cases):
    fail("no positive activation cases")
if not any(not case["activate"] for case in cases):
    fail("no negative activation cases")

all_module_ids = {name.removesuffix(".md") for name in TECHNICAL}
for case in cases:
    routes = list(case.get("phases", [])) + list(case.get("conditional_routes", {}).values())
    for route in routes:
        unknown = set(route) - all_module_ids
        if unknown:
            fail(f"{case['id']} routes to unknown modules: {sorted(unknown)}")
        if len(route) > 2:
            fail(f"{case['id']} exceeds the two-reference phase limit")
    if not case["activate"] and case.get("phases"):
        fail(f"{case['id']} assigns modules despite non-activation")

required_case_ids = {
    "measurement_isolation",
    "trading_measurement_composition",
    "concurrency_network_composition",
    "dual_skill_explicit",
    "safety_live_orders",
    "safety_credentials",
    "safety_purchase",
    "safety_infrastructure",
    "delegation_parallel",
}
case_ids = {case["id"] for case in cases}
if not required_case_ids <= case_ids:
    fail(f"required coverage missing: {sorted(required_case_ids - case_ids)}")

dependencies = {
    "measurement-contract": [],
    "trading-correctness": [],
    "cpu-memory-compiler": [],
    "numerical-kernels": ["cpu-memory-compiler"],
    "concurrency-realtime": [],
    "networking-time": ["system-architecture"],
    "system-architecture": [],
}
visiting: set[str] = set()
visited: set[str] = set()


def visit(node: str) -> None:
    if node in visiting:
        fail(f"dependency cycle reaches {node}")
    if node in visited:
        return
    visiting.add(node)
    for target in dependencies[node]:
        if target not in dependencies:
            fail(f"unknown dependency target {target}")
        visit(target)
    visiting.remove(node)
    visited.add(node)


for module_id in dependencies:
    visit(module_id)

mit_text = MIT_PARENT.read_text(encoding="utf-8")
mit_frontmatter = mit_text.split("---", 2)[1]
if "mit-6172-performance-engineering" not in frontmatter:
    fail("low-latency parent does not name the MIT skill boundary")
if "low-latency-quant-systems" not in mit_frontmatter:
    fail("MIT parent does not name the trading-system skill boundary")

print(
    "PASS: one parent, all links resolve, no nested skills, "
    f"{len(TECHNICAL)} technical modules, {len(cases)} authored evaluation cases, "
    "two-reference limit, acyclic dependencies, and mutual discovery boundary"
)
