# Advanced Portfolio and Mathematical Finance Research

Date: 2026-09-26

## Question

Which advanced university courses best deepen Ingenius in portfolio theory and mathematical finance without duplicating its broad finance parent, its MIT course skills, or its generic optimization specialist?

## Answer

The evidence supports two capability skills rather than a course-per-skill expansion:

1. **Advanced portfolio theory** owns the decision from estimated inputs to a constrained, cost-aware, validated static or dynamic allocation.
2. **Rigorous mathematical finance** owns proof-level work from filtered probability and no-arbitrage through stochastic calculus, pricing, control, stopping, and incomplete markets.

The first produces an allocation research package. The second produces a derivation or proof with conditions. Those observable outputs are different enough to justify separate activation. Individual courses remain evidence and study routes; they are not copied into overlapping skills.

## Selection rules

Sources had to be official university course pages, official open-course material, or instructor-hosted university notes; graduate or advanced elective material received priority. A source was selected only when it added a capability used in portfolio research, pricing, hedging, control, or mathematical verification. Historical pages are labeled as historical curriculum rather than current practice.

MIT 15.401 was not promoted because it is a broad foundation. MIT 15.450 and 18.642 were not duplicated because they already have course-specific skills. Computational performance, market microstructure, empirical forecasting, and generic optimization remain separate siblings.

## Claim ledger

| Claim | Evidence | Confidence | Consequence |
|---|---|---:|---|
| Advanced portfolio study extends beyond one-period mean-variance into robust, Bayesian, dynamic, econometric, and implementation questions. | NYU Active Portfolio Management; Chicago FINM 36700; Columbia MSFE; Oxford MCF | High | Create a decision-focused portfolio specialist. |
| Proof-level mathematical finance needs filtered probability, martingales, stochastic integration, measure changes, no-arbitrage, and control. | MIT 15.070J; ETH Mathematical Finance; NYU; Columbia; Oxford | High | Create a theorem-focused mathematical-finance specialist. |
| Portfolio construction and rigorous derivation overlap at dynamic allocation but do not have the same success criterion. | NYU active portfolio; ETH notes; Columbia stochastic control/asset allocation | High | Use a typed handoff, not one merged skill. |
| A course list alone cannot validate an investment process or theorem. | Evidence-type limitation | High | Separate curriculum provenance from proof and empirical validation. |
| A deeper hierarchy would improve activation. | No supporting evidence found | Low/unsupported | Keep a shallow sibling catalog with conditional reference modules. |

## Architecture map

```text
ingenius-quant-finance
    ├── routine portfolio/risk and empirical estimates
    ├── routine stochastic pricing
    ├── advanced-portfolio-theory
    │      ├── static/equilibrium
    │      ├── estimation/construction
    │      ├── dynamic allocation
    │      └── validation/sources
    └── rigorous-mathematical-finance
           ├── probability/martingales/FTAP
           ├── stochastic calculus/pricing
           ├── control/stopping/incomplete markets
           └── validation/sources
```

Cross-skill edges are typed artifacts, not topic similarity:

- empirical parent → portfolio specialist: point-in-time estimate, uncertainty, and information set;
- mathematical-finance specialist → portfolio specialist: verified state dynamics, value equation, conditions, and candidate control;
- portfolio specialist → robust optimization: fully specified objective, variables, constraints, units, and uncertainty model.

This keeps the runtime graph shallow and acyclic for an ordinary request. A single request activates one skill; a cross-domain request runs stages only when the downstream result consumes an upstream artifact.

## Dossiers

- [Advanced portfolio theory](advanced-portfolio-theory.md)
- [Rigorous mathematical finance](rigorous-mathematical-finance.md)
