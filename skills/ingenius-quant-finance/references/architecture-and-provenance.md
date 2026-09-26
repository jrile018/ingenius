# Architecture and Provenance

Load this file only when auditing, maintaining, or extending the skill tree.

## Selected architecture

This package is one discoverable parent skill, five conditional domain modules, and two maintenance references (`architecture-and-provenance.md` and `evaluation-plan.md`). It has exactly one `SKILL.md`; none of these references is a nested skill.

Why this shape:

- One monolithic file would load unrelated empirical, portfolio, pricing, and tutoring detail on every request.
- Separate discoverable skills would create overlapping activation boundaries because the modules share the same course corpus, assumptions, safety boundary, and verification contract.
- One subagent per topic would confuse stored knowledge with runtime execution and add synthesis cost without independent workstreams.

Promote a module to a separate skill only after realistic requests show a distinct standalone goal, inputs/outputs, success criteria, and non-overlapping evaluation set.

## Parent-to-module network

```text
SKILL.md (activation, shared workflow, invariants)
|-- course-map.md -------- provenance, prerequisites, coverage boundaries
|-- empirical-research.md - estimation, diagnostics, time-respecting evaluation
|-- portfolio-risk.md ----- exposure, objectives, constraints, robustness
|-- stochastic-pricing.md - measures, replication, dynamics, valuation
|-- learning-projects.md -- tutoring, sequencing, assignments, transfer
|-- architecture-and-provenance.md - maintenance-only structure audit
`-- evaluation-plan.md ---- validation-only test contract
```

Material cross-links:

- Empirical research → portfolio/risk when estimated factors, means, covariance, or backtests feed an allocation.
- Empirical research → stochastic pricing when volatility, curve, or model parameters are estimated.
- Course map → learning/projects when prerequisites or source availability determine a study plan.
- Stochastic pricing → portfolio/risk when valuation exposures feed margin, counterparty, or hedge optimization.

These links are directional routing dependencies, not instructions to load both modules every time.

## Graphify result

Graphify analyzed the five source Markdown files: 52 nodes, 67 edges, and 6 communities. The health check found no missing/dangling endpoints, self-loops, or collapsed edges. The principal communities were quantitative foundations, stochastic-pricing applications, learning/projects, modern portfolio applications, course scope/evidence, and risk-neutral pricing.

The material edges that influenced the design were:

- the quantitative dependency chain from linear algebra/probability through empirical and stochastic methods;
- the bridge from Brownian motion/Itō/SDEs to risk-neutral pricing;
- the 2013-to-2024 continuity in volatility, portfolio management, and Black–Scholes;
- evidence/availability boundaries as a cross-cutting concern;
- empirical assignments and case studies as a learning layer rather than a lecture-per-module hierarchy.

Graph community labels were treated as evidence, not copied mechanically into modules. The graph's generic token-reduction benchmark could not match its sample questions to this domain and remains unvalidated.

## ICM review

The package uses the ICM knowledge-bundle pattern within Codex skill constraints:

- `SKILL.md` is the small catalog.
- `references/` is the stable knowledge shelf.
- Each domain module has one job, explicit load/do-not-load conditions, inputs, and an output invariant. Maintenance references are routed by their audit or validation purpose instead.
- Shared activation, safety, and interpretation rules are canonical in the parent. Domain modules contain only the operational checks needed to apply those rules to a task.
- The cold walk reaches any operational module from the parent in one additional read.

The source snapshot, Graphify artifacts, earlier baseline, and final skill are separated at the repository level so evidence, analysis, comparison, and product do not blur together.

## Maintenance protocol

1. Change the source corpus only in `source-material/`; preserve source dates and licensing.
2. Run Graphify on the exact source corpus when material is added or relationships change. Record graph health, new/removed material edges, and ambiguities.
3. Use ICM Architect to review module ownership, one-home-per-fact, routing depth, and the cold walk.
4. Update the smallest affected module and its routing/evaluation cases.
5. Run structural validation and held-out activation, routing, and output tests.
6. Re-run subagent ablation only if a new task creates genuinely independent workstreams.

Do not run Graphify or ICM during ordinary finance questions. Their role is skill-tree construction and maintenance; the compiled routing table handles normal navigation.
