# Four-course skill evaluation

Evaluation date: 2026-09-26

## Scope

This evaluation checked the four new course skills and their relationship to `ingenius-quant-finance`:

- `mit-6172-performance-engineering`
- `mit-15481x-adaptive-markets`
- `mit-15450-analytics-of-finance`
- `mit-18642-quant-finance`

It separates structural validation, graph architecture checks, ICM navigation, and an independent behavioral forward test. None is described as a native probabilistic skill-discovery benchmark.

## Structural validation

Codex `quick_validate.py` passed for all four specialists and the updated Ingenius parent. Each package contains:

- one valid `SKILL.md`;
- one directly linked `references/course-guide.md`; and
- one `agents/openai.yaml` whose default prompt names the skill.

## Graph and walk checks

The directed isolated Graphify build produced 52 nodes, 58 edges, one hyperedge, and six communities. Integrity checks reported no missing or dangling endpoints, self-loops, or directed collapsed edges. Worker token usage was not exposed by the host collaboration API, so Graphify's zero token placeholder is not a cost measurement.

The ICM-informed cold walk passed: from the parent, a new agent can reach the specialist catalog and selected course entrypoint in two additional reads. Each specialist reaches its conditional course guide in one read.

Full architecture evidence is in [`research/course-skill-network-2026-09-26.md`](../../research/course-skill-network-2026-09-26.md).

## Independent forward test

The evaluator inspected only the five skill packages, not the research or architecture conclusions.

| Case | Observed route | Result |
|---|---|---|
| Allocation-bound C++ event-driven backtester | 6.172 only | Pass: established workload and finance correctness oracles before allocation/lifetime changes and repeated measurement |
| Crowded market-neutral strategy decay plus test design | Initially 15.481x then 15.450 | Partial: mechanism analysis was strong, but lightweight test design did not yet justify the second skill |
| GARCH estimation feeding Monte Carlo option pricing | 15.450 only | Pass: preserved physical/pricing measures, uncertainty, diagnostics, and handoff assumptions |
| 18.642 PCA/time-series/portfolio/volatility learning plan | 18.642 only | Pass: prerequisite-aware sequence and point-in-time capstone |
| Yield-curve PCA exposure and portfolio risk | Ingenius empirical then portfolio/risk | Pass: no course specialist activated merely from topic overlap |
| Unavailable Ross Garon systematic-trading lecture | 18.642 provenance only | Pass: refused reconstruction and offered clearly labeled alternatives |

### Observed strengths

- 6.172 adds finance-specific temporal, numerical, and replay invariants to performance work.
- 15.481x produces mechanisms, competitors, capacity, feedback, alternative explanations, and falsifiers rather than a post-hoc crowding label.
- 15.450 makes the empirical-to-pricing artifact and physical-to-pricing-measure boundary explicit.
- 18.642 combines prerequisite-aware tutoring with conservative source handling.
- The parent keeps an ordinary PCA portfolio request in the empirical-to-portfolio route.

### Revision from the trace

The parent catalog and Adaptive Markets skill were revised:

- 15.481x now owns mechanism mapping and high-level falsifiable test design.
- 15.450 joins only for an execution-ready econometric specification, dependence-valid inference, estimation, code, or implementation.

This is the only material revision supported by the independent trace. The affected routing cases and cold walk were updated.

## Remaining uncertainty

- Automatic discovery was not sampled repeatedly in the native selector.
- The forward test used one independent agent and authored cases rather than a randomized with-skill/without-skill experiment.
- No course assignment was reproduced end to end.
- No production code, market data, trade, or external system was mutated.

