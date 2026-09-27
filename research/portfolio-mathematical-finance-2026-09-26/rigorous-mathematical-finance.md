# Rigorous Mathematical Finance Dossier

## Capability target

Derive and check advanced pricing, hedging, allocation, stopping, and incomplete-market results with explicit stochastic objects and theorem hypotheses.

## Selected sources

### MIT OpenCourseWare — 15.070J Advanced Stochastic Processes

Official course: <https://ocw.mit.edu/courses/15-070j-advanced-stochastic-processes-fall-2013/>

This graduate course supplies the mathematical substrate: measure-theoretic probability, filtrations, martingales and stopping, Brownian motion, stochastic integration, Itō calculus, and functional limits. It is not itself a finance course, so the skill applies these methods only when the requested output is mathematical finance.

### ETH Zürich — Mathematical Finance

Instructor page: <https://people.math.ethz.ch/~jteichma/index.php?content=teach_MF20>

The course links general process theory, the fundamental theorem of asset pricing, portfolio selection, semimartingales, and stochastic portfolio theory.

Instructor notes: <https://people.math.ethz.ch/~jteichma/lecturenotesMF20180108.pdf>

The notes provide a deep spine through semimartingales and stochastic integration, Girsanov–Meyer transformations, stochastic exponentials, no-free-lunch conditions, deflators, utility maximization, primal/dual methods, numeraires, and stochastic portfolio theory. This source most strongly justifies the theorem-level boundary.

### NYU Courant — Mathematics in Finance academics

Official academics page: <https://math-finance.cims.nyu.edu/academics/>

The stochastic-calculus and dynamic-asset-pricing sequence includes Brownian motion, Itō integration and formula, Girsanov, Feynman–Kac, martingale pricing, incomplete markets, change of numeraire, and rates. It supports a pricing module that checks measure and representation conditions instead of merely applying formulas.

### Columbia — MS in Financial Engineering curriculum

Official curriculum: <https://ieor.columbia.edu/msfe-curriculum>

The curriculum connects stochastic models, continuous-time models, Monte Carlo, stochastic control, advanced derivatives, and asset allocation. It supports typed handoffs between proofs, computation, and portfolio decisions.

### Oxford — MSc in Mathematical and Computational Finance

Official programme: <https://www.maths.ox.ac.uk/members/students/postgraduate-courses/msc-mathematical-and-computational-finance>

The programme combines SDEs and stochastic control with Monte Carlo, PDEs, optimization, derivatives, fixed income, and microstructure. Its breadth helps define what this skill excludes: numerical implementation, optimization, and microstructure remain adjacent specialisms unless the requested artifact is the mathematical derivation itself.

## Derived modules

1. Probability, martingales, and FTAP: filtration, stopping, equivalent measures, admissibility, arbitrage, completeness, and semimartingale structure.
2. Stochastic calculus and pricing: Itō calculus, SDEs, Girsanov, numeraire changes, replication, Feynman–Kac, PDEs, rates, and volatility.
3. Control, stopping, and incomplete markets: utility, Merton problems, Bellman/HJB, American claims, duality, and preference- or bound-based values.
4. Validation and sources: object, hypothesis, algebra, representation, limiting-case, and numerical checks.

## Boundaries

- A routine Black–Scholes calculation remains in `ingenius-quant-finance`.
- Explicit MIT 15.450 or 18.642 study remains with those course skills.
- A generic stochastic-process exercise with no finance application should not activate this skill.
- A calibrated trading or allocation decision routes to the empirical or portfolio skill after the mathematical result is verified.
- Numerical performance belongs to `low-latency-quant-systems` only after measurement shows it is the bottleneck.

## Failure modes the skill must prevent

- invoking a risk-neutral measure without a no-arbitrage and numeraire argument;
- treating a local martingale as a martingale without sufficient conditions;
- omitting admissibility and thereby permitting doubling strategies;
- claiming completeness from one replicated payoff;
- changing measure by editing only the drift;
- accepting a formal PDE solution without terminal, boundary, and verification conditions;
- treating a simulation or discretization as proof;
- selecting one incomplete-market price without stating the criterion.
