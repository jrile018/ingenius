# Advanced Portfolio Theory Dossier

## Capability target

Design and evaluate allocations when expected returns and covariances are estimated, constraints and costs bind, investment opportunities change, and a mathematically optimal solution may be empirically unstable.

## Selected sources

### NYU Courant — Active Portfolio Management

Official catalog: <https://math-finance.cims.nyu.edu/?pg=2>

The course explicitly advances beyond mean-variance construction into robust optimization, dynamic programming, Bayesian choice, return and covariance estimation, predictability, and related econometric issues. It provides the cleanest source-level justification for joining portfolio decisions with estimation uncertainty while keeping generic solver theory separate.

### University of Chicago — FINM 36700 Portfolio Theory and Risk Management II

Official page: <https://finmath.uchicago.edu/curriculum/required-courses/finm-36700/>

The course connects mean-variance analysis with factor models, attribution, risk and pricing, tail risk, long-run returns, forecasting, allocation beyond mean-variance, cross-asset carry, and implementation. Its real-data and case orientation supports a skill that must test assumptions and implementation rather than stop at a closed-form optimum.

### Columbia — MS in Financial Engineering curriculum

Official curriculum: <https://ieor.columbia.edu/msfe-curriculum>

The curriculum combines asset allocation and quantitative risk with stochastic models, continuous-time models, Monte Carlo, computational finance, and stochastic control. It supports the boundary between an allocation skill and a theorem/control skill while showing how the two compose.

### Oxford — MSc in Mathematical and Computational Finance

Official course list: <https://courses.maths.ox.ac.uk/mod/book/view.php?chapterid=816&id=65619>

The 2025–26 list includes stochastic control, quantitative risk, computational finance, volatility modeling, asset pricing, and market microstructure. It supplies advanced breadth and makes clear that implementation and risk sit alongside—but are not identical to—continuous-time theory.

### MIT OpenCourseWare — 15.433 Investments

Official lecture notes: <https://ocw.mit.edu/courses/15-433-investments-spring-2003/pages/lecture-notes/>

This historical graduate course provides open material on portfolio theory, CAPM/APT, cross-sectional evidence, active management, risk, and hedge funds. It is useful as an accessible foundation but must not be presented as current market practice.

### MIT OpenCourseWare — 15.450 Analytics of Finance

Official syllabus: <https://ocw.mit.edu/courses/15-450-analytics-of-finance-fall-2010/pages/syllabus/>

The existing MIT 15.450 skill already owns explicit course work integrating estimation, volatility, Monte Carlo, dynamic programming, asset allocation, and Merton. The new portfolio skill therefore owns the reusable allocation decision, not the course identity.

## Derived modules

1. Static and equilibrium: mean-variance geometry, utility, factors, equilibrium restrictions, and attribution.
2. Estimation and construction: shrinkage, Bayesian views, Black–Litterman, robust construction, constraints, turnover, and costs.
3. Dynamic allocation: multi-period state, liabilities, consumption, Bellman/HJB reasoning, and policy evaluation.
4. Validation and sources: point-in-time testing, baselines, stress, attribution, multiplicity, and curriculum provenance.

## Boundaries

- Routine covariance, VaR/ES, or allocation questions remain in `ingenius-quant-finance`.
- Solver formulation and certification belong to `robust-quant-optimization` when they are the requested product.
- Transaction-cost mechanisms and execution schedules belong to `market-microstructure-execution`.
- Proof-level stochastic control belongs to `rigorous-mathematical-finance`; this skill consumes its verified output to judge implementability.

## Failure modes the skill must prevent

- optimizing noisy expected returns as if known;
- leaking future universe or estimates into a backtest;
- comparing gross optimized performance with a net baseline;
- using a factor regression as causal proof;
- hiding leverage, financing, liquidity, and turnover;
- interpreting an in-sample efficient frontier as realized efficiency;
- adding dynamics without a state variable or without a meaningful intertemporal effect.
