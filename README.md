# Ingenius Quant Finance

`ingenius` turns a researched MIT OpenCourseWare corpus into a source-grounded Codex skill for quantitative-finance analysis, verification, tutoring, and study planning.

The finished skill is [`skills/ingenius-quant-finance`](skills/ingenius-quant-finance/). It draws on public material from MIT OCW 18.S096 (Fall 2013) and its updated successor, 18.642 (Fall 2024). It is an independent research and learning tool, not an MIT product or an investment-recommendation system.

## Repository layout

```text
ingenius/
├── source-material/mit-ocw-research/   recovered research snapshot
│   └── graphify-out/                   portable knowledge graph and report
├── research-baseline/                  earlier test skill for comparison
├── evaluations/skillopt-2026-09-26/    SkillOpt, council, token, and sandbox evidence
└── skills/ingenius-quant-finance/      validated installable skill
    ├── SKILL.md                        parent router and shared invariants
    ├── agents/openai.yaml              Codex interface metadata
    └── references/                     conditional domain modules
```

## How the skill works

The package has one discoverable parent `SKILL.md`. After activation, the parent classifies the request and loads only the smallest relevant module set:

- `course-map.md` — provenance, prerequisites, course coverage, and evidence boundaries
- `empirical-research.md` — regression, time series, volatility, factors, PCA, and ML evaluation
- `portfolio-risk.md` — allocation, risk measures, calibration, constraints, and counterparty optimization
- `stochastic-pricing.md` — stochastic processes, Itō calculus, derivatives, rates, commodities, and credit
- `learning-projects.md` — tutoring, study sequencing, assignments, and project design

For example, a PCA portfolio backtest routes first through empirical validation and then through portfolio/risk analysis. A question about why physical drift disappears from an option-pricing PDE loads only stochastic pricing.

Modules are references, not nested skills or permanent agents. Subagents are optional runtime workers reserved for genuinely independent workstreams, such as a solver/checker pair.

The parent is deliberately not a general statistics or mathematics skill. Overlapping prerequisites activate it only when they are applied to quantitative finance or when the user explicitly asks about the curated MIT corpus. Analysis never authorizes trade execution or production-state mutation.

## Architecture method

The architecture was produced with the `research-to-skill` workflow:

1. Recover and verify the source snapshot from commit `4cd5ee0`.
2. Extract reusable capabilities rather than copying the lecture hierarchy.
3. Use Graphify to identify the dependency spine and cross-document relationships.
4. Use ICM principles to make `SKILL.md` a small catalog and the references conditional knowledge shelves.
5. Package with the Codex skill format and test activation, routing, invariants, and installation.

The graph contains 52 nodes, 67 edges, and six communities. See the [graph report](source-material/mit-ocw-research/graphify-out/GRAPH_REPORT.md) or open the [interactive graph](source-material/mit-ocw-research/graphify-out/graph.html).

## Install and invoke

Install by linking or copying `skills/ingenius-quant-finance` into your Codex skills directory. In this workspace it is linked at:

```text
~/.agents/skills/ingenius-quant-finance
```

Example invocation:

```text
Use $ingenius-quant-finance to audit my rolling PCA backtest and the portfolio constraints built on top of it.
```

## Boundaries

The skill distinguishes physical and pricing measures, expected payoffs and arbitrage-free prices, filtering and smoothing, and historical, conditional, realized, and implied volatility. It preserves observation-time information sets and flags look-ahead, survivorship, and selection bias.

It does not promise returns, manufacture security recommendations, reconstruct unavailable course material, or present dated course examples as current market facts.

## Validation

- Source files byte-match Git commit `4cd5ee0`.
- Codex structural validation passes.
- The package contains exactly one `SKILL.md`.
- All parent-to-reference links resolve.
- Independent architecture, behavioral, and packaging reviews pass.
- Reviewed activation, routing, boundary, and native forward-test cases are tracked with their limitations.
- A pinned Microsoft SkillOpt surrogate run rejected further edits at 0.9875 → 0.9875; its sealed four-case test scored hard 1.0 and soft 0.9675 with no backend or parse failures.

See [the evaluation report](evaluations/skillopt-2026-09-26/REPORT.md) for the run history, council findings, method limits, architecture comparison, and sandbox candidates. The SkillOpt cases are reviewed authored surrogates, not mined production usage or native skill-discovery measurements.
