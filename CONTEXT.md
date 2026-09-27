# Ingenius knowledge-to-skill workspace

One job: preserve attributable quantitative-finance, trading, systems, and operating-model research, then turn it into source-grounded, testable Codex skills.

## Layers

- `source-material/mit-ocw-research/` — exact files recovered from Git commit `4cd5ee0`, plus their Graphify sidecar.
- `research/low-latency-quant-systems-2026-09-26/` — dated cross-institution course, implementation, protocol, and research dossiers.
- `research/advanced-electives-2026-09-26/` — advanced empirical, microstructure, optimization, data-systems, and investment-firm course dossiers.
- `research-baseline/quant-finance-coursework/` — the earlier test skill, retained only for regression comparison.
- `skills/ingenius-quant-finance/` — cross-course quantitative-finance parent skill.
- `skills/low-latency-quant-systems/` — end-to-end trading-system performance parent skill.
- `skills/market-microstructure-execution/` — market mechanics, transaction costs, execution, and market-making skill.
- `skills/robust-quant-optimization/` — formulation, solver verification, and uncertainty-aware optimization skill.
- `skills/reliable-quant-data-systems/` — temporal lineage, transactional correctness, distribution, and recovery skill.
- `skills/investment-firm-systems/` — fund operating-model, controls, and resilience skill.
- `evaluations/low-latency-quant-systems-2026-09-26/` — its design brief, graph, cases, verifier, and report.
- `evaluations/advanced-elective-skills-2026-09-26/` — sibling-skill design, ICM cold walk, authored cases, and deterministic verifier.

## Maintenance flow

1. Preserve or update evidence in `source-material/` with dates and licensing intact.
2. Rebuild/query the source graph when relationships materially change.
3. Review the affected parent/module boundaries using its `references/architecture-and-provenance.md`.
4. Edit the smallest affected module.
5. Run structural, routing, and held-out behavior tests before installation.

## Human check

Before adopting a skill revision, verify that source claims remain attributable, routing reaches the smallest useful module set, and the skill does not present historical coursework as current investment guidance.
