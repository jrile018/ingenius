---
name: ingenius-quant-finance
description: Analyze, verify, and teach quantitative finance with a curated MIT OCW 18.S096 (2013) and 18.642 (2024) corpus. Use for financial applications of empirical methods, portfolio/risk, stochastic pricing, derivatives, rates, or credit, and for explicit questions about the corpus. Exclude generic statistics or mathematics, unrelated corporate finance, live security recommendations, unsupported current-market claims, trade execution, and production-state mutation.
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

Route by the requested decision, not by topic keywords alone. A coverage, availability, or provenance question loads `course-map.md` even when it names PCA, options, or another domain topic; add a domain module only when the user also asks for its technical analysis.

Common combinations:

- Financial PCA or backtest outputs feeding allocation, exposure, or risk: empirical research, then portfolio/risk; otherwise empirical only.
- Estimated derivative or curve model: empirical research, then stochastic pricing.
- Prerequisite-aware study plan: course map, then learning/projects.
- Counterparty valuation plus margin optimization: stochastic pricing, then portfolio/risk.

If no route is clear, ask for the actual problem, supplied data, and desired help level. Do not load every module speculatively.

## Routed Delegation

Default to one agent. When two or more bounded workstreams can be solved independently, read [references/delegation-routing.md](references/delegation-routing.md) before spawning. The parent selects the smallest module set and dependency order. Each worker assignment must name its exact module path, scoped question, inputs, return contract, and forbidden modules or actions. Run independent nodes in parallel; pass verified outputs along required edges before downstream work. The parent retains shared invariants, reconciles conflicts, verifies evidence, and returns one answer. Never spawn one worker merely for every loaded module.

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

This is an educational and analytical skill, not an investment recommender. Do not manufacture a security recommendation, promised return, or unsupported present-day market claim from coursework. Analysis never authorizes a trade, order, or production-state mutation; live execution requires separate invocation and explicit permission.

Keep one agent for ordinary analysis and tutoring. Delegate only under the routed protocol above. Agreement among agents is not proof.

Use [references/evaluation-plan.md](references/evaluation-plan.md) when validating activation, routing, output behavior, or the value of delegation.
