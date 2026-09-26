# MIT OCW finance mathematics: assignments and case studies

Research date: September 25, 2026. This guide describes the public course work; it is not a solution manual. The two editions assign different work. Mathematical comments and suggested extensions below are original explanatory synthesis.

## How assessment changed

The 2013 syllabus assigns 75% of the grade to homework and 25% to a final paper, with no exams. Its public assignment index contains nine sets; the ninth PDF explicitly says it need not be turned in. [2013 syllabus](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/pages/syllabus/), [assignment index](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/pages/assignments/).

The 2024 syllabus assigns 40% to homework, 20% to group presentations, 10% to participation, and 30% to the final paper. There are five problem sets, a group lecture-note project, and an individual final paper instead of a final exam. [2024 syllabus](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/pages/syllabus/).

## The nine 2013 problem sets

| Set | Mathematical work and learning purpose | Source |
|---|---|---|
| 1: Linear Algebra | Rank, invertibility, determinants, eigenvectors, Gram–Schmidt, SVD, positive semidefinite matrices, and least squares. The extension problems connect matrix decomposition directly to regression. | [PDF](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/79abc7077a91900369bbb9823211bba1_MIT18_S096F13_pset1.pdf) |
| 2: Probability Theory and Stochastic Process | Exponential and Poisson distributions, moment-generating functions, memorylessness, Markov chains and stationary laws, lognormal moments, exponential families, and a critique of time diversification. | [PDF](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/86e64fb3acfdb8aab38af462aaac1ece_MIT18_S096F13_pset2.pdf) |
| 3: Regression Analysis | Projection/hat matrices, observation leverage, invariance under reparameterization, QR methods, and tests of regression restrictions. The goal is to understand the geometry and sampling theory behind software output. | [PDF](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/61d868106b4de23e5c59c04512954a8b_MIT18_S096F13_pset3.pdf) |
| 4: Time Series Analysis | AR(2) moments and autocorrelations, Yule–Walker equations, lag polynomials and difference equations, oscillatory behavior, MA(1) identifiability/invertibility, and ARMA(1,1). | [PDF](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/64b58a3283830d9448e769a201824bfb_MIT18_S096F13_pset4.pdf) |
| 5: Volatility Modeling | Drift and volatility estimation from diffusion data, sampling frequency, estimator distributions and consistency, and uncertainty intervals for variance. This makes estimation error an explicit part of modeling. | [PDF](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/2dcc893d045ba13d2904efb2bb5f22cf_MIT18_S096F13_pset5.pdf) |
| 6: Time Series II and Portfolio Theory | Moments and lagged covariance of a vector autoregression, relationships between AR and moving-average representations, two-asset portfolio variance, and minimum-variance allocation under stated constraints. | [PDF](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/9c3945082887de1e03b79092d8f06010_MIT18_S096F13_pset6.pdf) |
| 7: Factor Modeling | Derive PCA for two variables, interpret it as an orthogonal change of coordinates, analyze eigenvector uniqueness, and study principal components of Treasury yields. | [PDF](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/501ab6f76c47c8f8a3be8d0a73cc670d_MIT18_S096F13_pset7.pdf) |
| 8: Stochastic Calculus | Identify martingales and adapted processes, compute conditional Brownian moments, apply Itô's formula, compare probability measures, use Itô isometry, and derive integration by parts for deterministic integrands. | [PDF](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/20348102bc927284425e6d505495eb30_MIT18_S096F13_pset8.pdf) |
| 9: Stochastic Differential Equations | Verify candidate SDE solutions with Itô's rule, including the explicit solution of the Vasicek interest-rate process. The sheet states that submission is unnecessary. | [PDF](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/c02bf5203e965227082b82fa1e59afa9_MIT18_S096F13_pset9.pdf) |

## The five 2024 problem sets

**Set 1: matrix dynamics and Markov chains.** Students derive Fibonacci growth through eigenvalues and diagonalization, study convergence of matrix powers, and analyze a two-state chain describing buy/sell order transitions. It connects abstract spectral theory with long-run probabilities. The reference to Fibonacci ratios in technical analysis is context for an exercise, not an empirical demonstration of trading profitability. [Set 1 PDF](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/mit18_642_f24_pset1.pdf).

**Set 2: probability, payoffs, and covariance.** Students analyze a biased random walk using moment-generating functions and the central limit theorem; compute lognormal moments and expected call payoffs; and relate portfolio variance to positive semidefinite covariance matrices and a special positive-matrix PCA case. A payoff expectation under an assumed real-world distribution does not, by itself, establish a no-arbitrage option price. [Set 2 PDF](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/mit18_642_f24_pset2.pdf).

**Set 3: Stein's lemma and financial factor structure.** It develops the Gaussian covariance identity, extends it to a stochastic-volatility mixture using a size-biased variance distribution, includes asset-price stochastic processes, and compares covariance-based and correlation-based PCA of Treasury yield changes. This shows why changing the probability weighting or scaling of variables changes interpretation. [Set 3 PDF](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/mit18_642_f24_pset3.pdf).

**Set 4: Brownian motion, estimation, and time series.** The work covers conditional moments, Brownian scaling, maximum-likelihood drift/volatility estimation under equal and unequal observation intervals, fixed-horizon consistency, AR(2), Yule–Walker relations, and ARMA(1,1). This set is particularly useful for connecting continuous-time models with sampled data. [Set 4 PDF](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/mit18_642_f24_pset4.pdf).

**Set 5: jumps and empirical volatility.** Students verify Brownian and Poisson processes as examples of Lévy processes, simulate trajectories, read Parkinson's high–low range estimator paper, and compare supplied S&P 500 and ARKK volatility case studies. An optional extension adapts the R Markdown analysis to another symbol. Its forecasting material includes naive baselines, residual diagnostics, and ARIMA/seasonal ARIMA. [Set 5 PDF](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/mit18_642_f24_pset5.pdf).

The assignment page also supplies a Treasury PCA reading, sample R code, and the volatility case-study R Markdown archive. These are useful starting points for reproducing the mathematics with data. [2024 problem-set resources](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/pages/problem-sets/).

## Six substantial 2013 case studies

These are separate teaching resources, not merely illustrations embedded in slides. The public case-study page links R files and data for some cases, together with portfolio simulation and allocation plots. [Case-study resource index](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/pages/case-studies/).

| Case | Actual investigation | What to extract from it |
|---|---|---|
| [1: Asset pricing](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/0bdbe269aa9dfcdc38aa22cb1536e359_MIT18_S096F13_CaseStudy1.pdf) | Fit a CAPM-style regression to excess stock returns; inspect residuals and influential observations; add macroeconomic factors. | Separate factor exposure from intercept, and inspect the assumptions supporting standard errors. |
| [2: Currency regimes](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/f8c5c85ab8873fb4ef4b0bfcc6aec835_MIT18_S096F13_CaseStudy2.pdf) | Examine Chinese-yuan exchange-rate regimes, change the currency base to Swiss francs, and fit currency-return regressions. | Quotation conventions and structural changes can change the meaning of a regression. |
| [3: Treasury yields](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/080e2e5b442051fae5099cf224f58c0f_MIT18_S096F13_CaseStudy3.pdf) | Compare daily, weekly, and monthly ten-year yields; use ACF/PACF, augmented Dickey–Fuller tests, differencing, AR(2), and AIC selection. | Frequency, stationarity, and model order must be evaluated together. |
| [4: FX volatility](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/809b321c4ffe634b3db0e8c59c4049df_MIT18_S096F13_CaseStudy4.pdf) | Compare geometric Brownian motion with Gaussian ARCH/GARCH and GARCH using Student-t innovations; examine dependence in squared returns. | Weak predictability of return direction can coexist with predictable conditional variance. |
| [5: Macroeconomic VAR](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/e633bd2bf13b7d0b9d8067f6b00db398_MIT18_S096F13_CaseStudy5.pdf) | Assemble macroeconomic series, fit vector autoregressions in levels and differences, and inspect impulse responses. | Joint time-series dynamics are richer than separate univariate forecasts; interpreting shocks requires care. |
| [6: Portfolio theory](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/f9775f1179d20bc788a0d1a623107a7b_MIT18_S096F13_CaseStudy6.pdf) | Simulate two-asset portfolios across correlations; compare US sector ETF allocations in 2003–2006 and 2009–2013 under 15% and 30% position caps. | Correlation, estimation period, and feasible allocation constraints shape the opportunity set. |

## Writing, presenting, and the investment exercise

In 2013, final-paper suggestions include regime shifts, low-volatility investing, bubbles, the Black–Scholes/heat-equation connection, hybrid FX products, HJM versus short-rate models, and Ross recovery. These are offered as research directions; their appearance does not mean every topic received a full lecture. [2013 projects](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/pages/projects/).

The 2024 group project asks students to write an introductory lecture note for classmates. Individuals submit distinct contributions, receive feedback and peer review, and prepare a 15–20 minute presentation. Listed subjects include behavioral anomalies, property-price regression, machine learning for rates, alternative data, jump diffusion, utility and risk, Fourier methods, option pricing, implied volatility, time series, and delta hedging. These are student-project topics, not a guaranteed common curriculum for every participant. [Group-project instructions](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/pages/group-project/).

The individual final paper begins with a proposal specifying a topic, objective, and sources. Drafting includes reflection and peer feedback. The published topic list ranges from SABR/Heston and Black–Litterman to pairs trading, momentum, market volume, sports betting, and AI. A topic may extend group work, but the assessed contribution is individual. [Final-paper instructions](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/pages/final-paper/).

The 2024 investment assignment is ungraded. It allocates a hypothetical $10,000 to an eligible asset, tracks holdings and daily dollar/percentage P&L, allows one optional full-position switch, and evaluates the result over specified September–November 2024 dates. One requested statistic is $(G-L)/(G+L)$, with $G$ and $L$ the magnitudes of accumulated gains and losses. Treat this as an observation and reflection exercise; it is not a substitute for a diversified portfolio experiment or a risk-adjusted strategy evaluation. [Investment-game instructions](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/pages/investment-game/).

## A result worth deriving yourself: drift is harder to estimate than volatility

This is an original worked explanation of the fixed-horizon estimation question in 2024 Set 4, rather than a quotation from a solution key.

Write the log price as $X_t=X_0+at+\sigma W_t$, and sample increments $Y_i=X_{ih}-X_{(i-1)h}$ with $h=T/n$. The model gives independent $Y_i\sim N(ah,\sigma^2h)$.

The drift estimate is

$$\hat a=\frac{\sum_iY_i}{T}=\frac{X_T-X_0}{T},\qquad \operatorname{Var}(\hat a)=\frac{\sigma^2}{T}.$$

Increasing $n$ while keeping $T$ fixed adds no information to this estimator beyond the two endpoints. Increasing the elapsed history $T$ reduces its variance, if the same model parameters remain appropriate throughout.

By contrast, the realized quadratic variation $\sum_iY_i^2$ converges to $\sigma^2T$ as the mesh shrinks. Thus volatility can be consistently estimated over a fixed horizon in this ideal diffusion model. Real observed prices can also contain bid–ask and measurement effects, which this model does not describe.

The financial implication is precise: abundant high-frequency data do not automatically yield an accurate estimate of expected return. That matters whenever a portfolio optimizer treats estimated means as known inputs.

## Suggested independent projects

These are recommendations arising from the research, not additional MIT assignments.

1. **Factor and volatility report.** Reproduce the CAPM case study, then compare rolling regression estimates and Gaussian versus Student-t GARCH. Report uncertainty and residual diagnostics.
2. **Portfolio estimation experiment.** Compare equal weights, minimum variance, and constrained mean–variance allocations using only prior observations to estimate inputs. Record allocation changes and sensitivity to the lookback period.
3. **Three-way option valuation.** For the same European call, compare a binomial tree, a Monte Carlo estimate under a pricing measure, and the Black–Scholes formula. Explain discretization and sampling error separately.
4. **Yield-curve laboratory.** Bootstrap discount factors from a small internally consistent instrument set, perform PCA on yield changes, and examine hedge sensitivity to the first few components.
5. **Range-based volatility comparison.** Compare close-to-close and Parkinson estimates on the same data, with an explicit account of overnight moves and estimator assumptions.

For any empirical project, preserve the observation dates, input conventions, transformations, and exact information available when a decision would have been made. This is the bridge from a classroom calculation to a reproducible research result.
