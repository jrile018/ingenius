# Ingenius knowledge-to-skill workspace

One job: preserve attributable quantitative-finance and performance-engineering research, then turn it into source-grounded, testable Codex skills.

## Layers

- `source-material/mit-ocw-research/` — exact files recovered from Git commit `4cd5ee0`, plus their Graphify sidecar.
- `research/low-latency-quant-systems-2026-09-26/` — dated cross-institution course, implementation, protocol, and research dossiers.
- `research-baseline/quant-finance-coursework/` — the earlier test skill, retained only for regression comparison.
- `skills/ingenius-quant-finance/` — cross-course quantitative-finance parent skill.
- `skills/low-latency-quant-systems/` — end-to-end trading-system performance parent skill.
- `evaluations/low-latency-quant-systems-2026-09-26/` — its design brief, graph, cases, verifier, and report.

## Maintenance flow

1. Preserve or update evidence in `source-material/` with dates and licensing intact.
2. Rebuild/query the source graph when relationships materially change.
3. Review the affected parent/module boundaries using its `references/architecture-and-provenance.md`.
4. Edit the smallest affected module.
5. Run structural, routing, and held-out behavior tests before installation.

## Human check

Before adopting a skill revision, verify that source claims remain attributable, routing reaches the smallest useful module set, and the skill does not present historical coursework as current investment guidance.
