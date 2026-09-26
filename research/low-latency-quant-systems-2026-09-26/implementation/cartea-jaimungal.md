# Cartea–Jaimungal — asset-price models for algorithmic and high-frequency trading

## Evidence

The UCL repository hosts the full open-access 2013 paper. It models trade intensity, duration, zero and non-zero price revisions, hidden regimes, limit-order fills, rebates, inventory, and regime-dependent quoting. The paper exposes formulas, calibration tables, HMM details, and simulated strategies.

## Skill use

For duration-, event-time-, or regime-dependent models, replay and simulation should preserve the required transaction/calendar-time representations, retain zero-price-revision trades when the model uses them, and validate probability and generator-matrix constraints. Inventory must reconcile from fills, terminal inventory policy must be explicit, and fees/rebates belong in P&L. Calibration version and regime drift should be tracked before parameters are reused.

## Limits

The empirical samples are historical, fill-decay parameters were assumed in parts of the work, and the strategy assumes a sufficiently small trader. The source grounds invariants and workload structure, not current profitability or market behavior. The UCL copy is CC BY 3.0; attribution and any third-party-material limits still apply.

## Sources

- [UCL repository record](https://discovery.ucl.ac.uk/id/eprint/1467031/)
- [Open-access paper](https://discovery.ucl.ac.uk/id/eprint/1467031/1/1350486x%252E2013%252E771515.pdf)
