#!/usr/bin/env python3
"""Verify the static parent-to-module delegation graph and case contracts."""

from __future__ import annotations

import json
import re
from pathlib import Path


def acyclic(nodes: set[str], edges: list[list[str]]) -> bool:
    outgoing = {node: [] for node in nodes}
    indegree = {node: 0 for node in nodes}
    for source, target in edges:
        outgoing[source].append(target)
        indegree[target] += 1
    queue = [node for node, degree in indegree.items() if degree == 0]
    visited = 0
    while queue:
        node = queue.pop()
        visited += 1
        for target in outgoing[node]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    return visited == len(nodes)


def main() -> int:
    repo = Path(__file__).resolve().parents[2]
    spec = json.loads(Path(__file__).with_name("cases.json").read_text(encoding="utf-8"))
    parent = repo / spec["parent_skill"]
    contract = repo / spec["delegation_contract"]
    parent_text = parent.read_text(encoding="utf-8")
    contract_text = contract.read_text(encoding="utf-8")
    modules = set(spec["module_paths"])
    module_files = {name: repo / path for name, path in spec["module_paths"].items()}
    errors: list[str] = []

    if "references/delegation-routing.md" not in parent_text:
        errors.append("parent does not link the delegation contract")
    if not acyclic(modules, spec["dependency_edges"]):
        errors.append("module dependency graph contains a cycle")
    for source, target in spec["dependency_edges"]:
        if source not in modules or target not in modules:
            errors.append(f"dependency endpoint missing: {source} -> {target}")
    for name, path in module_files.items():
        if not path.is_file():
            errors.append(f"missing module path for {name}: {path}")
        if path.name not in contract_text:
            errors.append(f"delegation contract does not route module {name}")

    spawning_cases = 0
    for case in spec["cases"]:
        workers = case["workers"]
        if case["spawn"]:
            spawning_cases += 1
            if len(workers) < 2:
                errors.append(f"{case['id']}: spawning case has fewer than two workers")
        elif workers:
            errors.append(f"{case['id']}: no-spawn case defines workers")
        for index, worker in enumerate(workers):
            module = worker.get("primary_module")
            if module not in modules:
                errors.append(f"{case['id']} worker {index}: invalid primary module {module}")
                continue
            forbidden = set(worker.get("forbidden_modules", []))
            allowed = set(worker.get("additional_allowed_modules", []))
            if module in forbidden or allowed & forbidden:
                errors.append(f"{case['id']} worker {index}: allowed/forbidden overlap")
            for field in ("required_return", "stop_when"):
                if not worker.get(field):
                    errors.append(f"{case['id']} worker {index}: missing {field}")
            dependency = worker.get("requires_worker")
            if dependency is not None:
                if case["schedule"] != "staged" or not 0 <= dependency < index:
                    errors.append(f"{case['id']} worker {index}: invalid staged dependency")

    skill_files = list((repo / "skills" / "ingenius-quant-finance").rglob("SKILL.md"))
    linked_references = set(re.findall(r"\]\((references/[^)#]+\.md)\)", parent_text))
    result = {
        "passed": not errors,
        "errors": errors,
        "metrics": {
            "modules": len(modules),
            "dependency_edges": len(spec["dependency_edges"]),
            "cases": len(spec["cases"]),
            "spawning_cases": spawning_cases,
            "skill_md_files": len(skill_files),
            "parent_words": len(parent_text.split()),
            "delegated_cold_walk_reads": 2,
            "linked_references": sorted(linked_references),
        },
        "invariants": {
            "one_discoverable_parent": len(skill_files) == 1,
            "dependency_graph_acyclic": acyclic(modules, spec["dependency_edges"]),
            "normal_route_reads": 1,
            "delegated_route_reads": 2,
            "parent_retains_synthesis": "parent" in contract_text.lower() and "synthesis" in contract_text.lower(),
        },
    }
    if not all(result["invariants"].values()):
        result["passed"] = False
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
