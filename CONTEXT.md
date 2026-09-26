# Ingenius knowledge-to-skill workspace

One job: preserve the MIT OCW research corpus and turn it into a source-grounded, testable Codex skill.

## Layers

- `source-material/mit-ocw-research/` — exact files recovered from Git commit `4cd5ee0`, plus their Graphify sidecar.
- `research-baseline/quant-finance-coursework/` — the earlier test skill, retained only for regression comparison.
- `skills/ingenius-quant-finance/` — the current product and sole install target.

## Maintenance flow

1. Preserve or update evidence in `source-material/` with dates and licensing intact.
2. Rebuild/query the source graph when relationships materially change.
3. Review the parent/module boundaries using `references/architecture-and-provenance.md` in the final skill.
4. Edit the smallest affected module.
5. Run structural, routing, and held-out behavior tests before installation.

## Human check

Before adopting a skill revision, verify that source claims remain attributable, routing reaches the smallest useful module set, and the skill does not present historical coursework as current investment guidance.
