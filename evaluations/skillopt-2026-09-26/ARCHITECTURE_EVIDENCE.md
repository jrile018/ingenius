# Architecture evidence carried into the Ingenius review

This is the repository-local record of the earlier `trade-ngin` comparison that informed the Ingenius skill-tree decision. It is evidence about a matched experiment, not a universal rule.

## Compared shapes

The control compared one monolithic skill, one routed parent with conditional references, four coarse sibling skills, and six matched-granularity sibling skills over the same six payloads and 11 equally weighted cases. Counts used `tiktoken` `o200k_base` over discovery metadata and activated skill/reference file contents. They excluded user prompts, runtime wrappers, repository reads, model output, latency, and billing.

| Architecture | Catalog tokens | Mean activated tokens | Narrow mean | Cross-domain mean | Blind behavior |
|---|---:|---:|---:|---:|---:|
| Monolith | 95 | 3,588 | 3,588 | 3,588 | 11/11 |
| Routed parent + references | **95** | 1,605 | 1,478 | **2,348** | 10/11 as written |
| Coarse siblings | 310 | 2,053 | not reported | not reported | 11/11 |
| Matched siblings | 432 | **1,504** | **1,210** | 2,689 | 11/11 |

Workload sensitivity favored matched siblings only for the narrow-heavy mix (1,391.6 versus 1,492.5 tokens). The routed parent won the balanced mix (1,597.3 versus 1,648.3) and cross-heavy mix (1,814.8 versus 2,017.9). The modeled 44% cross-domain crossover is specific to those cases and weights.

## Ingenius implication

The pre-review Ingenius package measured:

- 99 discovery tokens;
- 933 parent tokens;
- 548–724 tokens for one ordinary user-facing reference;
- 1,580–1,756 tokens for discovery + parent + one ordinary domain;
- 5,769 tokens for discovery + every package file.

This supports keeping a thin parent with conditional references because the modules share evidence, finance, verification, and permission rules and several useful workflows cross module boundaries. It does **not** prove the current tree optimal against a purpose-built Ingenius sibling design.

## Decision rule retained

- Use references for conditional modules under one discoverable goal with shared invariants and regular cross-domain composition.
- Promote a module to a sibling skill only when it has an independently requested goal, distinct inputs/outputs, a separate safety or tool boundary, and a non-overlapping evaluation set.
- Do not use nested `SKILL.md` files as hidden sub-skills.
- Do not use subagents as documentation storage. Use them only for independent runtime work with an explicit synthesis rule.

The full control artifacts remain outside this repository at the time of this review. This file records only the decision-relevant measurements so the Ingenius repository remains the system of record for its own architecture decision.
