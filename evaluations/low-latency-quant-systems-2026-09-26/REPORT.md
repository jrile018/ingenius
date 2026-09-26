# Low-latency quantitative systems: research-to-skill report

Date: 2026-09-26

## Outcome

The research produced one usable Codex parent skill: [`low-latency-quant-systems`](../../skills/low-latency-quant-systems/). It is designed for end-to-end performance work on market data, execution, pricing, risk, and quantitative-research systems. It preserves trading, numerical, temporal, concurrency, and operational correctness while localizing and testing a performance mechanism.

The source hierarchy was not copied into the runtime hierarchy. Twenty institutional courses or courseware collections and eleven primary implementation, protocol, or research references were synthesized into seven decision-owning modules.

## Evidence collected

The dated [research corpus](../../research/low-latency-quant-systems-2026-09-26/) covers:

- CPU, compiler, and numerical methods from ETH Zürich, UT Austin, Cornell, KIT, Berkeley, and Illinois;
- parallel systems and accelerators from Stanford, CMU, Berkeley, Illinois, and EPFL;
- networking and fabrics from Stanford plus official Linux and DPDK documentation;
- trading systems and market microstructure from Chicago, Oxford, Stanford, and NYU;
- target-specific evidence from LLVM MCA, uops.info, Intel, AMD, and Arm;
- wire-level state machines from Nasdaq ITCH and OUCH;
- execution and event-time research from Cartea–Jaimungal and Kearns–Nevmyvaka.

Each dossier separates source observation, transfer to a trading-system skill, caveats, and direct source links. Public availability is not treated as an open redistribution license.

## Architecture

The final shape is one discoverable parent, seven technical references, and four maintenance/conditional references. There are no nested `SKILL.md` files.

```text
parent SKILL.md
    ├── measurement contract (advanced experiment design only)
    ├── trading correctness
    ├── CPU / memory / compiler
    ├── numerical kernels
    ├── concurrency / real time
    ├── networking / time
    └── system architecture / placement
```

The parent owns the ordinary baseline, acceptance, authorization boundary, and final synthesis. A normal phase loads at most two technical references. Wider work is sequenced or delegated into bounded phases. `mit-6172-performance-engineering` now owns non-trading performance and explicit 6.172 study; this skill owns trading-system performance. Both activate together only on an explicit request for both lenses.

## Graphify and ICM result

Graphify mapped the corrected 32-document research corpus into 175 nodes, 193 directed edges, and 12 named communities. The integrity check found no missing endpoints, dangling edges, self-loops, exact duplicates, or directed/undirected edge collapse. The strongest hubs and cross-source connections support the selected module seams, especially:

- network experiments ↔ timestamp boundaries;
- offered load ↔ tail latency and goodput;
- deterministic replay ↔ execution realism;
- fills and inventory ↔ accounting reconciliation;
- numerical contracts ↔ target-specific implementation.

The [graph report](graphify-out/GRAPH_REPORT.md), [interactive graph](graphify-out/graph.html), and [ICM audit](graphify-out/ICM_AUDIT.md) are retained as maintenance evidence. Graphify and ICM are not runtime prerequisites.

Graphify's query benchmark estimated a 43.2× reduction relative to loading its full graph-derived corpus for three generic queries. That is a graph-retrieval proxy, not a model-billing or skill-runtime claim. Extraction telemetry is incomplete: one of two host-agent chunks reported 6,842 input and 14,530 output tokens; the other exposed zero fields, which means unavailable—not free.

## Validation

- Standard skill-package validation passes for this skill and the adjusted MIT 6.172 skill.
- The custom verifier checks one parent, resolved links, no nested skills, seven modules, 20 authored cases, a two-reference phase cap, acyclic declared dependencies, required safety/composition coverage, and reciprocal discovery boundaries.
- A local-link audit resolved all checked Markdown links in the affected repository scope.
- The source-grounding council found no blocker and confirmed that mutable/vendor/protocol claims are scoped.
- The ICM reviewer initially failed the tree, then passed the corrected ownership, route-depth, DAG, maintenance, and discovery-boundary checks.
- The [live trial](LIVE_TRIAL.md) observed correct skill selection on eight held-out prompts, safe refusal boundaries on four operational prompts, and clean single-agent versus split-worker evidence plans.

The live delegation comparison did not show a proven accuracy or token advantage. It supports the chosen rule: use one agent by default and add workers only for independent evidence records or a real verified handoff.

## Context shape

The parent contains 726 words. Parent plus one technical module contains 987–1,107 words, versus 4,660 words for the parent and every reference. These are structural word counts, not exact tokens or bills. Loading every module would be worse than progressive disclosure; the design helps only when routing remains selective.

## What remains unproven

- No target trading codebase or hardware was benchmarked in this research-to-skill run.
- No native production-frequency skill-discovery telemetry was available.
- No exact multi-agent token or billing telemetry was exposed.
- Course content does not replace current exchange, regulator, broker, vendor, or installed-version documentation.
- A real implementation evaluation still needs sanitized code/data, correctness oracles, representative load, pinned hardware/toolchain, timestamp boundaries, and comparable before/after distributions.

Within those limits, the architecture is a good idea: one parent plus conditional subskill references gives clear ownership and focused context. Treating every source as a discoverable skill or every module as a permanent subagent would add overlap and coordination without evidence of benefit.
