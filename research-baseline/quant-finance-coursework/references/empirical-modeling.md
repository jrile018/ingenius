# Empirical Modeling

## Module Contract

- **Purpose:** Design or review regression, time-series, volatility, factor, PCA, and empirical-finance analyses.
- **Load when:** The request uses observed data, estimated relationships, forecasts, or latent factors.
- **Do not load when:** The task is a purely arbitrage-based pricing derivation with no empirical estimation.
- **Output invariant:** State the information set, transformations, assumptions, diagnostics, and out-of-sample check.

## Workflow

1. Define the response, predictors, timestamps, sampling frequency, and information available at each decision time.
2. Inspect units, missingness, transformations, corporate-action handling, and selection or survivorship effects.
3. Separate descriptive fit, forecasting, and causal claims. A fitted relationship does not establish causation.
4. Check stationarity and dependence before interpreting standard errors or forecasts. Distinguish levels, returns, differences, and cointegrating combinations.
5. Fit a simple baseline before a richer model. Reserve regularization or latent factors for an identified dimensionality or stability problem.
6. Diagnose residual dependence, heteroskedasticity, influential observations, distributional misspecification, and parameter instability.
7. Evaluate using only prior information. Report uncertainty and compare out-of-sample performance with the baseline.

## Model-Specific Checks

### Regression

For `y = X beta + error`, state rank and error assumptions. Prefer QR or SVD over explicitly forming an inverse in numerical work. Distinguish Gauss-Markov conditions from the stronger normality assumptions used for exact finite-sample inference. Use GLS or robust methods only when their covariance or loss assumptions are justified.

### Time series

For ARMA/ARIMA or VAR work, state lag order, root/stability conditions, differencing, innovation assumptions, and selection criterion. A predictive lag relationship is not causal identification. Filtering uses data available through the current time; smoothing uses later observations and cannot represent a real-time decision.

### Volatility

Keep realized/historical estimates, conditional forecasts, and option-implied quantities separate. For GARCH-type models, check positivity, persistence, standardized residuals, and squared-residual dependence. Square-root-of-time scaling needs dependence assumptions.

### Factors and PCA

State whether PCA uses covariance or correlation, whether variables were demeaned or scaled, the estimation window, and out-of-sample stability. A high-variance direction is not automatically an economic factor or a profitable strategy. Record how portfolio weights, financing, transaction costs, and lookback changes affect any strategy interpretation.

## Verification

Use time-ordered splits or rolling evaluation, naive forecast baselines, residual plots/tests, parameter-sensitivity checks, and reproducible transformations. Treat course-reported empirical findings as teaching examples unless independently reproduced on dated data.
