# Robust quantitative optimization electives

## Capability target

Translate financial or systems decisions into mathematically explicit programs, choose methods from problem structure, verify numerical certificates, and test whether uncertain inputs make the apparent optimum unstable.

## Selected sources

- [Stanford EE364A Convex Optimization I](https://see.stanford.edu/Course/EE364A): public lectures, transcripts, assignments, and solutions covering convex sets/functions, LP/QP/SDP, optimality, duality, estimation, numerical linear algebra, and interior-point methods.
- [Stanford EE364B Convex Optimization II](https://see.stanford.edu/Course/EE364B): advanced methods including subgradient and cutting-plane methods, decomposition, structure exploitation, relaxations, branch-and-bound, robust optimization, and a substantial project.
- [MIT 15.093J Optimization Methods](https://ocw.mit.edu/courses/15-093j-optimization-methods-fall-2009/): graduate linear, network, discrete, nonlinear, and dynamic optimization plus optimal control.
- [Boyd and Vandenberghe, Convex Optimization](https://stanford.edu/~boyd/cvxbook/): authoritative companion reference; linked rather than copied.

## Synthesis and boundary

The reusable workflow is problem record → convexity/structure classification → solver and tolerance choice → independent residual/certificate checks → perturbation and baseline comparison. It is a separate skill because users can request formulation, infeasibility analysis, KKT verification, or robust optimization independently of finance theory.

The skill does not own investment advice, the empirical validity of financial inputs, or low-level kernel performance. Those hand off respectively to the finance, empirical, or performance skills.

