#!/usr/bin/env python3
"""Deterministic checks for the advanced portfolio and mathematical-finance skills."""

from __future__ import annotations

import json
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CASES = json.loads((HERE / "cases.json").read_text(encoding="utf-8"))

SKILLS = {
    "advanced-portfolio-theory": {
        "static-and-equilibrium",
        "estimation-and-construction",
        "dynamic-allocation",
        "validation-and-sources",
    },
    "rigorous-mathematical-finance": {
        "probability-martingales-ftap",
        "stochastic-calculus-pricing",
        "control-stopping-incomplete-markets",
        "validation-and-sources",
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
    if linked != modules:
        fail(f"{name}: expected {sorted(modules)}, got {sorted(linked)}")
    if list((root / "references").rglob("SKILL.md")):
        fail(f"{name}: nested discoverable skill found")
    for module in modules:
        path = root / "references" / f"{module}.md"
        if not path.is_file():
            fail(f"{name}: missing {module}.md")
        if "loading boundary" not in path.read_text(encoding="utf-8").lower():
            fail(f"{name}/{module}: missing loading boundary")

parent_text = (REPO / "skills/ingenius-quant-finance/SKILL.md").read_text(encoding="utf-8")
for name in SKILLS:
    if name not in parent_text:
        fail(f"broad parent does not route to {name}")

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
    "portfolio_black_litterman",
    "portfolio_dynamic_liability",
    "portfolio_basic_negative",
    "portfolio_solver_negative",
    "math_ftap",
    "math_numeraire",
    "math_american_stopping",
    "math_black_scholes_negative",
    "math_probability_negative",
    "handoff_empirical_portfolio",
    "handoff_math_portfolio",
    "handoff_portfolio_optimizer",
    "safety_live_orders",
}
case_ids = {case["id"] for case in CASES}
if not required <= case_ids:
    fail(f"missing required cases: {sorted(required - case_ids)}")

edges = {
    "ingenius-quant-finance": {"advanced-portfolio-theory", "rigorous-mathematical-finance"},
    "rigorous-mathematical-finance": {"advanced-portfolio-theory"},
    "advanced-portfolio-theory": {"robust-quant-optimization"},
    "robust-quant-optimization": set(),
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

research = REPO / "research/portfolio-mathematical-finance-2026-09-26"
for dossier in ["README.md", "advanced-portfolio-theory.md", "rigorous-mathematical-finance.md"]:
    if not (research / dossier).is_file():
        fail(f"missing research dossier {dossier}")

print(
    "PASS: 2 sibling skills, 8 conditional modules, no nested skills, "
    f"{len(CASES)} authored cases, negative boundaries, source dossiers, and acyclic handoffs"
)
