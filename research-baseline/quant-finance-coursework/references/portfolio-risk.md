# Portfolio, Risk, and Calibration

## Module Contract

- **Purpose:** Analyze allocation, covariance, factor exposure, risk measures, constraints, and calibration stability.
- **Load when:** The task asks how exposures combine, how an objective is optimized, or how risk/model inputs affect a decision.
- **Do not load when:** The question is only about a derivative's replication or stochastic transformation.
- **Output invariant:** Separate the mathematical optimum from uncertainty in inputs and operational constraints.

## Portfolio Workflow

1. Define assets, horizon, numeraire, return convention, objective, and feasible constraints.
2. State estimated mean vector, covariance or factor model, and the observation period used to estimate them.
3. Write the objective and constraints before solving. For fixed weights, expected return and variance take the forms `w' mu` and `w' Sigma w`.
4. Check covariance symmetry and positive semidefiniteness, constraint feasibility, units, and exposure totals.
5. Stress the inputs, not only the optimizer: change means, correlations, volatility, lookback windows, position caps, and transaction-cost assumptions.
6. Report concentration, factor exposures, turnover, leverage, liquidity, and sensitivity alongside the objective value.

## Risk Measures

Define the loss variable, horizon, confidence level, and aggregation convention. Value at risk is a quantile threshold; expected shortfall summarizes the tail beyond a threshold. Neither replaces scenario analysis, model-risk review, or stress testing. Compare variance-covariance, historical, and simulation methods only after stating their different assumptions.

## Calibration and Inverse Problems

Exact benchmark repricing does not guarantee stable parameters, valuations, or hedges. Diagnose conditioning and small singular values. When regularization is justified, identify the penalty, scaling, and tuning rule, then show the tradeoff between fit and stability. Do not describe smoothness or sparsity as information directly observed from market quotes.

## Factor and Counterparty Applications

Distinguish common-factor covariance from specific risk and statistical factors from economic interpretations. In counterparty or margin optimization, include netting, collateral, discrete trade constraints, fairness, feasibility, and rounding effects; an elegant continuous solution may not be operationally valid.

## Verification

Check limiting correlations, constraint residuals, scenario P&L, perturbation sensitivity, and alternative estimation windows. For a two-asset example, test correlation `-1`, `0`, and `1` to expose sign or covariance errors. Make clear when a result depends on historical estimates remaining stable.
