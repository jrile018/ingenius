# Advanced elective skill expansion: design brief

Date: 2026-09-26

## Goal

Add advanced, reusable capabilities that match the user's recurring quantitative-development work without creating one skill per course or duplicating the existing finance/performance tree.

## Architecture decision

Four capabilities have independent activation and output contracts, so they are sibling skills:

| Skill | Input contract | Output contract | Main negative boundary |
|---|---|---|---|
| `market-microstructure-execution` | venue/instrument state, order objective, benchmark, data | mechanics, cost model or execution policy plus validation | no live orders; implementation latency belongs elsewhere |
| `robust-quant-optimization` | variables, objective, constraints, units, uncertainty | formulation, method, certificate/residuals, sensitivity | no investment advice or unsupported global-optimality claim |
| `reliable-quant-data-systems` | producers/consumers, time axes, invariants, failures | temporal/data contract, recovery design, tests | no destructive migration or hot-path tuning by default |
| `investment-firm-systems` | entity/strategy scope, actors, providers, workflows | operating map, controls, exception/recovery plan | no legal/compliance sign-off or live operations |

Each uses a shallow parent-plus-references layout. The reference modules are conditional sub-skills, not nested `SKILL.md` files. This preserves one activation boundary per user goal and keeps normal requests from loading unrelated courses.

This matches [OpenAI's skill-building guidance](https://developers.openai.com/plugins/build/skills): keep each skill focused on a recognizable user goal, split workflows when triggers/inputs/success criteria differ, keep `SKILL.md` concise, and load supporting references conditionally.

MIT 14.384, MIT 14.387, and Stanford MS&E 448 strengthen the existing `ingenius-quant-finance` empirical module. A fifth empirical skill was rejected because its triggers and output would overlap the existing parent.

## Derived route and handoff map

```text
ingenius-quant-finance / empirical-research
    ├─ signal + uncertainty ─→ robust-quant-optimization
    └─ signal + timestamps ─→ market-microstructure-execution

reliable-quant-data-systems
    ├─ point-in-time dataset ─→ ingenius-quant-finance
    └─ reconciled positions/cash ─→ investment-firm-systems

market-microstructure-execution
    └─ measured implementation target ─→ low-latency-quant-systems
```

These are typed optional handoffs. Topic overlap alone never creates a dependency or a reason to spawn an agent.

## ICM cold walk

ICM form: saved Codex skills; no separate workspace form requested.

1. A direct request such as “verify the KKT residuals” activates one sibling and one module.
2. A cross-domain request begins with the artifact owner, then passes only a verified artifact downstream.
3. Each parent states global invariants and authority limits; modules own only decision-specific procedures.
4. There are no recursive discovery paths or nested `SKILL.md` files.
5. A fresh reader can decide the owner from the requested output, not course names or keywords.

Cold-walk ambiguities and resolutions:

- “Optimize execution” means `market-microstructure-execution` when optimizing the schedule/cost decision; `low-latency-quant-systems` when reducing measured software latency. Use both only if both artifacts are requested.
- “Optimize a portfolio” stays with `ingenius-quant-finance` for financial interpretation and adds `robust-quant-optimization` only when formulation/certification is a separate deliverable.
- “Build a trading database” activates `reliable-quant-data-systems`; it does not activate the low-latency skill unless a measured hot path is in scope.
- “Make the fund compliant” is rejected as a compliance conclusion; `investment-firm-systems` can map workflows and controls while requiring current authority and qualified review.

## Graphify status

The research corpus was organized as Markdown evidence and checked with Graphify's local detection stage. It found six documents and 1,433 words and returned `needs_graph: false` because the corpus fits a single context window. No Gemini key was available, and this turn did not authorize semantic-extraction subagents, so no semantic graph is claimed. The route graph above is a disclosed, manually derived architecture map from explicit contracts and course scope—not Graphify-backed semantic evidence.

## Evaluation design

The deterministic suite checks frontmatter, discoverable-skill boundaries, reference resolution, negative activation language, source presence, sibling cross-routes, case coverage, and acyclic handoffs. Authored cases cover positive, negative, ambiguous, cross-skill, and safety behavior. They are structural expectations, not claims of model-behavior accuracy until live forward tests are run.
