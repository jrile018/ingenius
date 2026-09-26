# MIT OpenCourseWare roadmap for Ingenius

Research date: 2026-09-26

## Bottom line

For the intended outcome—optimizing codebases, understanding hedge-fund strategies and workflows, building fund research/trading infrastructure, and doing quantitative research—the best MIT OpenCourseWare set is not a generic CS or mathematics degree. It is a production-engineering spine joined to an empirical-finance spine.

The target-specific core is:

1. 6.0001 programming
2. 6.005 software construction
3. 6.006 algorithms
4. 6.033 computer-system engineering
5. 6.172 performance engineering
6. 6.830 database systems
7. 18.06SC linear algebra
8. 18.600 probability
9. 18.650 statistics
10. 15.053 optimization
11. 15.097 prediction, machine learning, and statistics
12. 14.384 time-series analysis
13. 15.401 finance theory
14. 15.433 investments and hedge-fund/proprietary-trading foundations
15. 15.450 analytics of finance
16. 15.481x adaptive markets and hedge-fund behavior
17. 18.642 integrated quantitative finance and systematic-trading applications

Calculus and discrete mathematics remain prerequisites when missing, but they are preparation rather than the destination. After the core, add operating systems, distributed systems, security, compiler engineering, advanced econometrics, or financial-system design only for the role being built.

## How courses were selected

Only official MIT OpenCourseWare course pages were treated as decisive sources. A course was retained when it supplied at least one of the following:

- a prerequisite used by several later courses;
- a central quantitative-finance capability;
- a strong implementation or research skill needed to turn theory into reliable software;
- unusually complete self-study material; or
- a specialist topic not adequately covered by a course already selected.

Material ratings are practical corpus ratings, not judgments of academic quality:

- **A** — unusually complete for self-study, normally including several of video, notes, exercises, solutions, exams, or projects;
- **B** — strong written course package, but less complete or less accessible than an A course;
- **C** — useful specialist or historical supplement whose examples, software, or market context require more updating.

## Computer science

| Priority | Course | Best use in Ingenius | Material |
|---|---|---|---|
| Core | [6.0001 Introduction to Computer Science and Programming in Python (Fall 2016)](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/) | Python and computational problem-solving foundation | A |
| Core | [6.0002 Introduction to Computational Thinking and Data Science (Fall 2016)](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/) | Optimization, simulation, stochastic thinking, experimental data, and introductory modeling | A |
| Core | [6.042J Mathematics for Computer Science (Spring 2015)](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) | Proofs, graphs, counting, discrete structures, and discrete probability | A |
| Core | [6.006 Introduction to Algorithms (Spring 2020)](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) | Data structures, algorithm design, complexity, and implementation discipline | A |
| Advanced theory | [6.046J Design and Analysis of Algorithms (Spring 2015)](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/) | Randomization, dynamic programming, network flow, approximation, and rigorous performance analysis | A |
| Software quality | [6.005 Software Construction (Spring 2016)](https://ocw.mit.edu/courses/6-005-software-construction-spring-2016/) | Testing, specifications, invariants, abstraction, concurrency, and maintainable research code | A |
| Core ML | [6.036 Introduction to Machine Learning (Fall 2020)](https://ocw.mit.edu/courses/6-036-introduction-to-machine-learning-fall-2020/) | Modeling, generalization, supervised learning, temporal sequences, and evaluation foundations | A |
| Advanced ML | [18.409 Algorithmic Aspects of Machine Learning (Spring 2015)](https://ocw.mit.edu/courses/18-409-algorithmic-aspects-of-machine-learning-spring-2015/) | Rigorous algorithmic ML after algorithms, probability, and linear algebra | B |
| Systems | [6.033 Computer System Engineering (Spring 2018)](https://ocw.mit.edu/courses/6-033-computer-system-engineering-spring-2018/) | Reliability, concurrency, fault tolerance, networks, security, and system design | B |
| Distributed systems | [6.824 Distributed Computer Systems Engineering (Spring 2006)](https://ocw.mit.edu/courses/6-824-distributed-computer-systems-engineering-spring-2006/) | Replicated services, distributed storage, network systems, security, and fault tolerance | C |
| Performance | [6.172 Performance Engineering of Software Systems (Fall 2018)](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/) | Profiling, caching, parallelism, measurement, and low-latency implementation | A |
| Data systems | [6.830 Database Systems (Fall 2010)](https://ocw.mit.edu/courses/6-830-database-systems-fall-2010/) | Data models, query processing, transactions, recovery, and research-data infrastructure | B |
| Operating systems | [6.828 Operating System Engineering (Fall 2012)](https://ocw.mit.edu/courses/6-828-operating-system-engineering-fall-2012/) | Virtual memory, threads, kernels, IPC, coordination, and software/hardware interactions | B |
| Systems security | [6.858 Computer Systems Security (Fall 2014)](https://ocw.mit.edu/courses/6-858-computer-systems-security-fall-2014/) | Threat models, OS and network security, information flow, secure implementation, and adversarial review | A |
| Compiler specialization | [6.035 Computer Language Engineering (Spring 2010)](https://ocw.mit.edu/courses/6-035-computer-language-engineering-spring-2010/) | Compilers, program analysis, optimization, and understanding generated machine behavior | B |
| Optional computation | [18.S191 Introduction to Computational Thinking (Fall 2022)](https://ocw.mit.edu/courses/18-s191-introduction-to-computational-thinking-fall-2022/) | Julia, numerical experiments, and integrated mathematical computation | A |

### CS selection result

For the revised goal, 6.005, 6.006, 6.033, 6.172, and 6.830 are no longer peripheral: together they teach how to make research code correct, scalable, measurable, and operable. Add 6.824 for distributed services, 6.828 for low-level latency and resource behavior, 6.858 for security-sensitive fund infrastructure, and 6.035 only when compiler or low-level optimization knowledge will actually be used.

## Mathematics

| Priority | Course | Best use in Ingenius | Material |
|---|---|---|---|
| Core | [18.01SC Single Variable Calculus (Fall 2010)](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) | Differentiation, integration, approximation, series, and optimization basics | A |
| Core | [18.02SC Multivariable Calculus (Fall 2010)](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/) | Gradients, multiple integration, vector calculus, and multivariate optimization foundations | A |
| Pricing branch | [18.03SC Differential Equations (Fall 2011)](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/) | ODEs, linear systems, transforms, and preparation for continuous-time models | A |
| Core | [18.06SC Linear Algebra (Fall 2011)](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) | Projections, eigenvectors, least squares, covariance methods, and factor models | A |
| Core probability | [18.600 Probability and Random Variables (Fall 2019)](https://ocw.mit.edu/courses/18-600-probability-and-random-variables-fall-2019/) | Probability, random variables, limit results, martingales, risk-neutral probability, and a Black–Scholes bridge | A |
| Alternative probability | [6.041SC Probabilistic Systems Analysis and Applied Probability (Fall 2013)](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) | A more engineering-oriented, exceptionally complete probability course | A |
| Core statistics | [18.650 Statistics for Applications (Fall 2016)](https://ocw.mit.edu/courses/18-650-statistics-for-applications-fall-2016/) | Estimation, hypothesis testing, regression, Bayesian methods, PCA, and generalized linear models | A |
| Applied statistics | [15.075J Statistical Thinking and Data Analysis (Fall 2011)](https://ocw.mit.edu/courses/15-075j-statistical-thinking-and-data-analysis-fall-2011/) | Sampling, inference, regression, nonparametrics, and applied programming exercises | B |
| Applied linear algebra | [18.065 Matrix Methods in Data Analysis, Signal Processing, and Machine Learning (Spring 2018)](https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/) | SVD, low-rank methods, optimization, and matrix-based data analysis | A |
| Predictive modeling | [15.097 Prediction: Machine Learning and Statistics (Spring 2012)](https://ocw.mit.edu/courses/15-097-prediction-machine-learning-and-statistics-spring-2012/) | Generalization, statistical learning, kernels, Bayesian analysis, and project-based prediction | B |
| Advanced empirical methods | [14.387 Applied Econometrics: Mostly Harmless Big Data (Fall 2014)](https://ocw.mit.edu/courses/14-387-applied-econometrics-mostly-harmless-big-data-fall-2014/) | Regression design, matching, IV, differences, high-dimensional covariates, and causal-research discipline | B |
| Numerical methods | [18.330 Introduction to Numerical Analysis (Spring 2012)](https://ocw.mit.edu/courses/18-330-introduction-to-numerical-analysis-spring-2012/) | Root finding, approximation, integration, differential equations, and numerical linear algebra | B |
| Intro optimization | [15.053 Optimization Methods in Management Science (Spring 2013)](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/) | Accessible linear, integer, network, and decision optimization | B |
| Advanced optimization | [15.093J Optimization Methods (Fall 2009)](https://ocw.mit.edu/courses/15-093j-optimization-methods-fall-2009/) | Graduate linear, nonlinear, discrete, network, dynamic, and control optimization | B |
| Stochastic processes | [18.445 Introduction to Stochastic Processes (Spring 2015)](https://ocw.mit.edu/courses/18-445-introduction-to-stochastic-processes-spring-2015/) | Markov chains and processes before advanced pricing or probability theory | B |
| Rigorous analysis | [18.100B Real Analysis (Spring 2025)](https://ocw.mit.edu/courses/18-100b-real-analysis-spring-2025/) | Proof maturity, convergence, continuity, integration, and rigorous mathematical foundations | A |
| Measure theory | [18.125 Measure and Integration (Fall 2003)](https://ocw.mit.edu/courses/18-125-measure-and-integration-fall-2003/) | Specialist preparation for measure-theoretic probability and stochastic calculus | B |
| Graduate probability | [18.175 Theory of Probability (Spring 2014)](https://ocw.mit.edu/courses/18-175-theory-of-probability-spring-2014/) | Brownian motion, martingales, conditioning, Lévy processes, and asymptotic probability | B |
| Empirical branch | [14.384 Time Series Analysis (Fall 2013)](https://ocw.mit.edu/courses/14-384-time-series-analysis-fall-2013/) | Stationary and nonstationary series, VARs, frequency methods, persistence, and structural breaks | B |

### Math selection result

Do not require real analysis, measure theory, or graduate probability for every quant-finance task. They form a theory branch for rigorous stochastic modeling. For most empirical work, calculus, linear algebra, undergraduate probability, statistics, numerical methods, and optimization have much higher immediate value.

18.600 and 6.041SC overlap. Use 18.600 when the destination is mathematical finance because its public notes explicitly bridge into martingales, risk-neutral probability, and Black–Scholes. Use 6.041SC when the destination is engineering probability or when an especially complete independent-study package is more important.

## Quantitative finance

| Priority | Course | Best use in Ingenius | Material |
|---|---|---|---|
| Finance foundation | [15.401 Finance Theory I (Fall 2008)](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/) | Valuation, fixed income, equities, forwards, futures, options, portfolio theory, CAPM/APT, and market efficiency | A |
| Primary integrated quant course | [18.642 Topics in Mathematics with Applications in Finance (Fall 2024)](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/) | Current primary survey: bond math, regression, rates, PCA, portfolio construction, volatility, stochastic calculus, Black–Scholes, ML, and SDEs | A |
| Complementary predecessor | [18.S096 Topics in Mathematics with Applications in Finance (Fall 2013)](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/) | Additional factor, time-series, portfolio, rates, commodity, credit, and case-study material | A |
| Advanced integrated quant | [15.450 Analytics of Finance (Fall 2010)](https://ocw.mit.edu/courses/15-450-analytics-of-finance-fall-2010/) | Financial econometrics, dynamic optimization, Monte Carlo, Itô calculus, derivatives, and portfolio choice | B |
| Investments branch | [15.433 Investments (Spring 2003)](https://ocw.mit.edu/courses/15-433-investments-spring-2003/) | Portfolio theory, empirical returns, fixed income, derivatives, credit, risk management, and active management | C |
| Hedge-fund and market behavior | [15.481x Adaptive Markets: Financial Market Dynamics and Human Behavior (Fall 2022)](https://ocw.mit.edu/courses/15-481x-adaptive-markets-financial-market-dynamics-and-human-behavior-fall-2022/) | Market efficiency limits, changing regimes, behavioral foundations, hedge-fund ecology, crises, and ethics | A |
| Trading and financial technology | [15.S08 FinTech: Shaping the Financial World (Spring 2020)](https://ocw.mit.edu/courses/15-s08-fintech-shaping-the-financial-world-spring-2020/) | AI in finance, APIs, payments, trading and capital markets, and financial-platform context | A |
| Financial-system design | [14.129 Blockchain and the Design of Financial Systems (Spring 2025)](https://ocw.mit.edu/courses/14-129-blockchain-and-the-design-of-financial-systems-spring-2025/) | Financial infrastructure, distributed ledgers, market mechanisms, regulation, and economics/CS system design | A |
| Empirical research branch | [14.384 Time Series Analysis (Fall 2013)](https://ocw.mit.edu/courses/14-384-time-series-analysis-fall-2013/) | Graduate time-series methods and model-diagnostic discipline | B |

### Quant-finance selection result

Use 18.642 as the primary integrated course and 18.S096 as a complementary historical source, not as two independent authorities to be loaded in full every time. Their shared topics should be deduplicated by concept, while unique cases and explanations remain traceable to their original offering.

15.401 supplies the finance vocabulary and no-arbitrage/valuation foundation that mathematics-only courses assume. 15.450 is the strongest advanced bridge across econometrics, stochastic calculus, optimization, simulation, and implementation, but it assumes prior finance, programming, calculus, probability, and statistics.

15.433 is valuable because its public materials explicitly cover active portfolio management, hedge funds and proprietary trading, risk management, commodities, fixed income, credit, and derivatives. Its 2003 examples are historical, so use its stable concepts while verifying market conventions and operations against current sources.

15.481x is the strongest public MIT course in this set for understanding why hedge-fund strategies emerge, adapt, crowd, and sometimes fail. It is not an operations manual. 15.S08 and 14.129 add financial-platform and market-infrastructure context, while 6.033/6.830/6.824/6.858 supply the engineering needed to build dependable systems.

## Recommended learning and skill-building routes

### Targeted foundation

```text
math prerequisites → 18.06SC → 18.600 → 18.650 → 15.053
                                               ├→ 15.097 → 14.384
6.0001 → 6.006 → 6.005 → 6.033 → 6.830       │
                                               └→ 15.401 → 15.433/15.481x → 18.642/15.450
```

### Empirical quant branch

```text
foundation → 18.650 → 18.065 → 15.097 → 14.384 → 15.450
                                     └→ 14.387 for causal/empirical design
```

Use this for backtesting, regression, factor models, PCA, volatility, time series, validation, and ML. Research code should simultaneously follow the 6.005/6.830 reproducibility and data-system path.

### Stochastic pricing branch

```text
foundation → 18.03SC → 18.445 → 18.642 → 15.450
                         └→ 18.100B → 18.125 → 18.175  (rigorous theory route)
```

Use the rigorous route only when the task actually needs measure-theoretic probability, Brownian motion, martingales, or proof-level foundations.

### Portfolio and risk branch

```text
foundation → 15.053/15.093J → 15.401 → 18.642 → 15.433 or 15.450
```

Use 15.433 for breadth across asset classes and investment practice; use 15.450 for more mathematical optimization and econometrics.

### Quant developer branch

```text
6.0001 → 6.006 → 6.005 → 6.033 → 6.830 → 6.172
                                  ├→ 6.824 distributed services
                                  ├→ 6.828 operating systems
                                  ├→ 6.858 systems security
                                  └→ 6.035 compiler specialization
```

This route is about building reliable and performant systems. It should stay separate from the mathematical-pricing path unless a task genuinely combines both.

### Hedge-fund research and trading branch

```text
15.401 → 15.433 → 15.481x
   ├→ 18.642 → systematic strategies, portfolios, risk, and trading applications
   ├→ 15.450 → econometrics, optimization, simulation, and proprietary trading
   └→ 15.S08/14.129 → trading platforms and financial-system context
```

This branch teaches strategy families, instruments, portfolio construction, empirical evaluation, and changing market behavior. The publicly listed 18.642 systematic-trading guest lecture is unavailable to OCW learners, so its title cannot be treated as a complete algorithmic-trading module.

### Fund research-platform branch

```text
6.005 → 6.033 → 6.830 → 6.172
                    ├→ 6.824 for distributed jobs and services
                    ├→ 6.858 for secrets, authorization, and adversarial security
                    └→ 6.828/6.035 for latency-sensitive specialization
```

The project target should be a reproducible pipeline: dated data ingestion, point-in-time feature generation, experiment tracking, time-ordered evaluation, portfolio/risk constraints, paper-trading simulation, monitoring, and deterministic replay.

## What MIT OCW does not fully cover

The selected courses are strong for theory, research, and systems foundations, but they do not form a complete handbook for launching or operating a hedge fund. Important gaps include:

- prime brokerage, custody, fund administration, NAV/accounting, audit, tax, and investor reporting;
- current adviser, commodity, derivatives, short-sale, market-data, and exchange regulation;
- production OMS/EMS design, exchange protocols, venue routing, transaction-cost analysis, and live market microstructure;
- corporate data licensing, entitlements, symbol/security-master maintenance, and point-in-time vendor corrections;
- operational risk, disaster recovery, model governance, surveillance, compliance, and change-management controls.

Those topics require fresh regulator, exchange, broker, vendor, and practitioner sources. Dated OCW slides must not be treated as current legal or operational authority.

## Implications for the Ingenius skill tree

The courses should remain evidence sources, not become one subskill per course. Course-shaped subskills would overlap heavily: PCA appears in linear algebra, statistics, machine learning, time series, and both finance offerings; optimization appears in algorithms, operations research, portfolios, and stochastic control.

A scalable parent-to-module architecture is instead:

```text
Ingenius parent
├── provenance and course map
├── mathematical foundations
├── computation and algorithms
├── empirical research and machine learning
├── optimization, portfolio, and risk
├── stochastic processes and pricing
├── quant software, data, and performance
└── learning projects and curriculum planning
```

The parent should route by the decision or artifact being produced, not by course number or a keyword. A worker estimating a volatility model needs empirical-research guidance; a worker consuming that validated forecast to price an option needs stochastic-pricing guidance. They may cite several courses, but the runtime modules follow capabilities and dependencies.

## Courses deliberately not promoted to the main set

- Duplicate editions were omitted when one OCW edition had a clearer or more complete self-study package.
- Broad AI courses were not promoted because 6.036 and 18.409 cover the ML capabilities most relevant to quantitative research with less unrelated material.
- Distributed systems is retained as a specialist production course, not a general quantitative-finance prerequisite; its older public package should be supplemented with current implementation practices when used.
- MIT subjects mentioned inside a syllabus were not included unless a usable official OCW course page was verified. For example, 15.437 Options and Futures Markets is recommended by 15.450, but a substantive public OCW package was not found in this pass.
- A course's age is not automatically disqualifying for stable mathematics. It is a reason to label market examples, software, regulations, and empirical claims as historical.

## Confidence and limitations

Confidence is high that the courses above form the most useful MIT OCW dependency network for a quant-finance-centered Ingenius expansion. “All relevant courses” cannot be made literal without becoming an unbounded catalog, so this report defines relevance operationally and records the selection boundary.

This pass verified course identity, topic fit, and publicly visible learning-resource types. It did not download and grade every individual lecture, assignment, or solution. Before adding a course to the installed skill, the next research stage should inventory its files, record unavailable resources, deduplicate concepts against the current 18.S096/18.642 corpus, and run source-grounded evaluation cases.
