# University of Chicago FINM 37602 — Mathematical Market Microstructure

## Scope and public material

The current course page describes a five-week course on mathematical models for ultra-low-latency market behavior and risk. It combines lectures, workshops, real data, R implementations, and simulated real-time trading projects.

## What it contributes

The course studies event-level stochastic models including ordered-probit and decomposition time series, Poisson, Cox, Ammeter, Hawkes, and related processes. Its value to the skill is the reminder that the workload is endogenous to market microstructure: event arrival, clustering, regime behavior, and feedback shape both computation and validation.

## Transfer to trading systems

Benchmark streams should preserve realistic burstiness, event-type mix, and temporal dependence rather than replay uniformly spaced synthetic messages. Models used in a hot path need causal features, point-in-time state, and calibration-drift checks. A performance optimization must not silently change event-time semantics or estimation results.

## Limits

Only the public description was inspected; the linked syllabus is externally hosted. The course establishes model families and workload realism, not a universal choice of process or production trading rule.

## Sources

- [FINM 37602 course page](https://finmath.uchicago.edu/curriculum/electives/finm-37602/)
