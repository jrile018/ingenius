# Design Brief: Advanced Portfolio and Mathematical Finance Skills

Date: 2026-09-26

## Decision

Add two independently discoverable sibling skills below the broad Ingenius finance catalog:

- `advanced-portfolio-theory` for estimation-aware static and dynamic allocation decisions;
- `rigorous-mathematical-finance` for proof-level stochastic-finance derivations.

Do not create a new umbrella skill, nested `SKILL.md` files, or one skill per university course. The existing `ingenius-quant-finance` parent remains the broad entry point and routes to these specialists only when the requested output crosses their advanced activation boundaries.

## Trigger contract

The portfolio specialist activates when success means a defensible allocation, policy, or validation package under uncertain estimates, constraints, costs, or multiple periods. The mathematical-finance specialist activates when success means a proof or derivation with explicit filtered-probability, no-arbitrage, measure-change, control, or stopping conditions.

Routine portfolio arithmetic and routine Black–Scholes usage remain with the broad parent. Generic solver work remains with `robust-quant-optimization`. Explicit MIT 15.450 or MIT 18.642 learning remains with those course skills.

## Module architecture

Each specialist has one discoverable `SKILL.md` and four conditional references. Modules are stored guidance, not permanent agents and not nested skills. An ordinary phase loads no more than two references.

```text
advanced-portfolio-theory
  ├─ static-and-equilibrium
  ├─ estimation-and-construction
  ├─ dynamic-allocation
  └─ validation-and-sources

rigorous-mathematical-finance
  ├─ probability-martingales-ftap
  ├─ stochastic-calculus-pricing
  ├─ control-stopping-incomplete-markets
  └─ validation-and-sources
```

## Typed handoffs

```text
ingenius empirical estimate
  -- point-in-time estimate + uncertainty + information set --> advanced portfolio

rigorous mathematical finance
  -- verified dynamics + value equation + conditions + candidate control --> advanced portfolio

advanced portfolio
  -- objective + variables + constraints + units + uncertainty model --> robust optimization
```

No skill is invoked merely because it shares vocabulary with another. A downstream stage runs only when it consumes the named upstream artifact.

## Graphify and ICM result

Graphify's detector found three research documents and about 1,555 words and returned `needs_graph: false`. Following its small-corpus rule, no semantic graph was fabricated. The architecture map is therefore a manually derived, source-backed route map.

The ICM cold walk used the user's requested output as the entry point:

- “construct” or “validate allocation” reaches the portfolio sibling and one or two modules;
- “prove” or “derive under no-arbitrage/measure/control assumptions” reaches the mathematical-finance sibling;
- routine calculations stay at the broad parent;
- solver certification, execution mechanics, empirical estimation, and performance tuning exit through explicit sibling boundaries.

Each terminal reference answers one kind of decision; the parent files preserve invariants and handoffs. No ordinary route requires backtracking through another sibling, and the declared handoff graph is acyclic.

## Evaluation plan

The authored suite covers direct, indirect, incomplete, negative, handoff, and safety cases. Deterministic checks verify frontmatter, negative boundaries, exact reference routes, no nested skills, loading boundaries, parent adjacency, bounded module sets, and an acyclic handoff graph. This is structural and authored-case evidence, not a live activation benchmark or proof of real-world portfolio performance.
