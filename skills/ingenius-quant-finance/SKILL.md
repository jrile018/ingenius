---
name: ingenius-quant-finance
description: Analyze, verify, and teach quantitative-finance problems using a curated MIT OCW 18.S096 (2013) and 18.642 (2024) research corpus. Use for regression, time series, volatility, PCA, portfolio and risk analysis, stochastic processes, derivatives, rates, credit, or source-grounded study and project planning. Do not use for live investment recommendations, unsupported current-market claims, or unrelated corporate finance.
---

# Ingenius Quant Finance

Use the MIT OCW-derived corpus as a source-grounded reasoning framework. Optimize for correct assumptions, mathematical verification, and honest source boundaries—not for reproducing lecture order.

## Route the Request

Load the smallest set of modules that owns distinct decisions:

| Observable request | Load |
|---|---|
| Course coverage, prerequisites, 2013/2024 comparison, source status, or what material is publicly available | [references/course-map.md](references/course-map.md) |
| Regression, time series, stationarity, volatility, factors, PCA, ML evaluation, or empirical research design | [references/empirical-research.md](references/empirical-research.md) |
| Allocation, covariance, factor exposure, VaR/ES, constraints, calibration stability, margin, or counterparty optimization | [references/portfolio-risk.md](references/portfolio-risk.md) |
| Brownian motion, Itō calculus, SDEs, replication, options, rates, commodities, credit, or pricing measures | [references/stochastic-pricing.md](references/stochastic-pricing.md) |
| Tutoring, assignment strategy, study sequencing, misconception diagnosis, or project design | [references/learning-projects.md](references/learning-projects.md) |
| Auditing, extending, or restructuring this skill and its module tree | [references/architecture-and-provenance.md](references/architecture-and-provenance.md) |

Common combinations:

- PCA portfolio or backtest: empirical research, then portfolio/risk.
- Estimated derivative or curve model: empirical research, then stochastic pricing.
- Prerequisite-aware study plan: course map, then learning/projects.
- Counterparty valuation plus margin optimization: stochastic pricing, then portfolio/risk.

If no route is clear, ask for the actual problem, supplied data, and desired help level. Do not load every module speculatively.

## Shared Workflow

1. Identify the objective, supplied inputs, horizon, information set, requested depth, and whether the user wants a hint, review, derivation, implementation, or study plan.
2. State assumptions before applying a formula or model. Ask only when a missing fact would materially change the result; otherwise label a reasonable assumption.
3. Separate calculation from interpretation. A mathematically valid result is not automatically empirically adequate, causal, tradable, operationally feasible, or current.
4. Verify independently where practical using dimensions, limiting cases, covariance properties, state-by-state replication, residual diagnostics, time-ordered evaluation, simulation, or a second derivation.
5. Label claims as corpus-grounded, standard extension, fresh external fact, or unknown. Browse authoritative current sources when a time-sensitive claim actually matters.

## Invariants

- Keep physical probability and pricing measures distinct.
- Keep expected payoff and arbitrage-free price distinct.
- Keep historical, conditional, realized, and implied volatility distinct.
- Keep vector autoregression and value at risk distinct.
- Keep filtering and smoothing information sets distinct.
- Do not treat PCA directions as stable economic factors without evidence.
- Do not treat a precise optimization result as reliable when its estimated inputs are unstable.
- Preserve observation dates and contemporaneous information sets; flag look-ahead, survivorship, and selection bias.
- Do not invent content for unavailable lectures, recordings, or student presentations.
- Treat historical examples, lecturer claims, and course-reported results as dated teaching evidence unless independently refreshed.

## Boundary and Delegation

This is an educational and analytical skill, not an investment recommender. Do not manufacture a security recommendation, promised return, or unsupported present-day market claim from coursework.

Keep one agent for ordinary analysis and tutoring. Delegate only independent, bounded work such as a solver/checker pair, separate source audits, or independent empirical and derivation workstreams. Require an explicit synthesis rule and deterministic or source-based checks; agreement among agents is not proof. Never create one subagent merely to read each module.

Use [references/evaluation-plan.md](references/evaluation-plan.md) when validating activation, routing, output behavior, or the value of delegation.
