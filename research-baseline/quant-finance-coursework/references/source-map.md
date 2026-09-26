# Course Source Map

## Module Contract

- **Purpose:** Ground course coverage, prerequisites, sequencing, and provenance.
- **Load when:** The request depends on what MIT 18.S096/18.642 taught, how topics connect, or what public material is available.
- **Do not load when:** A self-contained mathematical calculation needs no course-specific claim.
- **Output invariant:** Identify the supporting source or label the statement as synthesis, extension, or unknown.

## Provenance

This skill was derived from the `jrile018/ingenius` research snapshot at commit [`4cd5ee0`](https://github.com/jrile018/ingenius/tree/4cd5ee039532aa8c1a4a42707a822a5be692e01a). The snapshot synthesizes public MIT OCW materials for:

- [18.S096, Fall 2013](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/)
- [18.642, Fall 2024](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/)

Use the snapshot as a research guide, not as a substitute for the linked MIT materials. It distinguishes published teaching material, student-selected project subjects, and the research author's explanatory extensions.

## Prerequisites

Expected foundations include multivariable calculus, differential equations, probability and statistics, and linear algebra. Working readiness means being able to manipulate matrices, interpret eigenvectors, integrate densities, compute conditional expectations, solve elementary differential equations, and read regression output. Prior finance knowledge is helpful but not required by the course descriptions.

## Capability Map

| Foundation | Downstream capability |
|---|---|
| Linear algebra | Regression, PCA, factor models, portfolio covariance, calibration |
| Probability and conditional expectation | Markov processes, martingales, statistical inference, pricing measures |
| Regression and time-series diagnostics | Factor analysis, volatility forecasting, empirical portfolio research |
| Brownian motion and quadratic variation | Itô calculus and stochastic differential equations |
| Itô calculus and SDEs | Replication, PDE methods, Monte Carlo, risk-neutral pricing |
| Portfolio and factor models | Allocation, risk, constraints, counterparty and practical applications |

The map is conceptual rather than the literal lecture order. Practitioner applications can precede all of their mathematical machinery.

## Evidence Status

- The 2013 offering supplies broad statistics, time-series, portfolio/factor, stochastic-calculus, commodities, rates, credit, and counterparty material.
- The 2024 successor refreshes empirical work and includes visible material on PCA applications, rates practice, margin optimization, biomedical financing, event markets, volatility, and machine-learning examples.
- Some specialist 2013 topics have no dedicated 2024 session; absence of a titled session does not prove total absence.
- The public 2013 materials lack substantive accessible content for the Matrix Primer and FX-execution lectures.
- The public 2024 package withholds several guest/student sessions or supplies only descriptions. Do not reconstruct their technical content.
- Student-project titles establish topic interest, not a complete instructor-taught module.

## Source Files in the Snapshot

- [`README.md`](https://github.com/jrile018/ingenius/blob/4cd5ee039532aa8c1a4a42707a822a5be692e01a/README.md): synthesis, dependency map, equations, distinctions, and study route.
- [`research-2013-lectures-01-13.md`](https://github.com/jrile018/ingenius/blob/4cd5ee039532aa8c1a4a42707a822a5be692e01a/research-2013-lectures-01-13.md): foundations through commodities.
- [`research-2013-lectures-14-26.md`](https://github.com/jrile018/ingenius/blob/4cd5ee039532aa8c1a4a42707a822a5be692e01a/research-2013-lectures-14-26.md): portfolio/factor work through counterparty risk.
- [`research-2024-update.md`](https://github.com/jrile018/ingenius/blob/4cd5ee039532aa8c1a4a42707a822a5be692e01a/research-2024-update.md): successor lecture map, additions, and availability limits.
- [`assignments-and-case-studies.md`](https://github.com/jrile018/ingenius/blob/4cd5ee039532aa8c1a4a42707a822a5be692e01a/assignments-and-case-studies.md): problem-set coverage, case studies, and project ideas without solutions.

The repository snapshot is MIT-licensed by its author. Linked MIT OCW content has its own terms; preserve attribution and review applicable licensing before redistributing substantial adaptations.
