# Ingenius Quant Finance

`ingenius` turns a researched MIT OpenCourseWare corpus into a source-grounded Codex skill for quantitative-finance analysis, verification, tutoring, and study planning.

The finished skill is [`skills/ingenius-quant-finance`](skills/ingenius-quant-finance/). It draws on public material from MIT OCW 18.S096 (Fall 2013) and its updated successor, 18.642 (Fall 2024). It is an independent research and learning tool, not an MIT product or an investment-recommendation system.

## Repository layout

```text
ingenius/
├── source-material/mit-ocw-research/   recovered research snapshot
│   └── graphify-out/                   portable knowledge graph and report
├── research/                            source-selection and architecture reports
│   └── courses/                         four course-specific deep-research briefs
├── research-baseline/                  earlier test skill for comparison
├── evaluations/skillopt-2026-09-26/    SkillOpt, council, token, and sandbox evidence
├── evaluations/delegation-routing-2026-09-26/ live routing experiment and verifier
├── skills/ingenius-quant-finance/      cross-course parent skill
├── skills/mit-6172-performance-engineering/
├── skills/mit-15481x-adaptive-markets/
├── skills/mit-15450-analytics-of-finance/
└── skills/mit-18642-quant-finance/      four course-specific skills
```

Each course package contains one `SKILL.md`, one conditionally loaded course guide, and Codex interface metadata. The course packages are siblings selected through the Ingenius parent catalog; they are not nested `SKILL.md` files.

```text
skills/<course-skill>/
    ├── SKILL.md                        parent router and shared invariants
    ├── agents/openai.yaml              Codex interface metadata
    └── references/course-guide.md      conditional course detail and tests
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

## Why this architecture was chosen

The original question was whether a deeply researched course should become one large skill, many subskills, or a parent skill that routes temporary specialist agents. We compared those designs and selected the last one, with an important constraint: the subskills are conditional reference modules, while subagents are optional runtime workers.

| Design considered | Result | Reason |
|---|---|---|
| One large `SKILL.md` | Rejected | Every request would load unrelated empirical, portfolio, pricing, provenance, and tutoring instructions. |
| Several independently discoverable finance skills | Rejected for this corpus | Their activation boundaries overlap, so similar questions could select inconsistent skills or duplicate shared rules. |
| One permanent agent per topic | Rejected | It adds agent context, coordination, and synthesis cost even when the question needs only one coherent argument. |
| One parent plus conditional reference modules | Selected | Activation and shared invariants have one owner, while each request loads only the relevant domain guidance. |
| Optional subagents over the selected modules | Selected conditionally | They help when work products are genuinely independent or when a verified upstream artifact must be handed to a downstream specialist. |

The resulting distinction is:

- A **parent skill** decides whether Ingenius applies, selects modules, controls dependencies, and owns the final answer.
- A **subskill module** is stored domain guidance in `references/`; it is not independently activated.
- A **subagent** is a temporary worker created only for a bounded work product and assigned an exact module contract.

### Earlier architecture evaluation

The earlier evaluation supported the selected design:

- A pinned Microsoft SkillOpt surrogate scored `0.9875`; a proposed rewrite also scored `0.9875`, so the optimizer correctly rejected unnecessary change.
- The sealed four-case evaluation scored hard `1.0` and soft `0.9675`, with no backend or parse failures.
- Independent architecture, behavioral, and packaging reviewers favored one discoverable parent with progressive disclosure and warned against overlapping activation, indiscriminate delegation, and treating agent agreement as proof.
- The parent and module layout reduced the files that an ordinary request needs to read compared with a monolithic skill. This is a structural context comparison, not a claim about exact billed model tokens.
- Subagents were judged worthwhile only when error isolation, parallel wall-clock work, or a real dependency handoff justifies their extra context and synthesis cost.

The conclusion was therefore not “more agents are always better.” It was: use one agent by default, use modules to keep context focused, and add agents only when the task graph provides a concrete reason.

## How parent-to-subagent routing works

The main agent activates the parent once, then the parent performs both module routing and worker routing:

1. Select the smallest domain modules that own the requested decisions.
2. Keep a short or tightly coupled request with one agent.
3. For independent workstreams, spawn bounded workers in parallel and give each worker the exact reference it must read.
4. For a real dependency, run the upstream worker first and pass its verified artifact to the downstream worker.
5. The parent checks assumptions and evidence across workers, then returns one synthesis.

```text
user request
    ↓
parent SKILL.md
    ├─ empirical worker ──validated estimate──> portfolio worker
    ├─ pricing worker ─────────────────────────┐
    └─ course/source worker ───────────────────┤
                                               ↓
                                      parent synthesis
```

For example, a volatility forecast used in option pricing routes first to an empirical worker. Only after that worker returns a validated forecast and information set does a pricing worker use it. By contrast, an unrelated course-source audit and derivative derivation can run at the same time. The full worker contract is in [`delegation-routing.md`](skills/ingenius-quant-finance/references/delegation-routing.md).

### Live routing experiment result

The live experiment passed both core routing behaviors:

- **Parallel:** a course-coverage worker received only `course-map.md`, while an independent Black–Scholes worker received only `stochastic-pricing.md`.
- **Staged:** an empirical worker returned `CORRECTED_PCA_SPEC`; only then was the portfolio worker created and given that exact artifact.

The first parallel run exposed an over-routing bug: the word “PCA” caused the coverage worker to receive the empirical module too. The parent was changed to route by the decision being made, not by keywords, and a fresh run passed. The full evidence, including limitations and the unrun single-agent control, is in the [delegation-routing experiment report](evaluations/delegation-routing-2026-09-26/REPORT.md).

The staged trial also confirmed that topical similarity is not enough to create a dependency. A dependency exists only when a downstream decision consumes an upstream result. Graphify helps reveal related concepts in the research corpus, but the runtime graph uses explicit input/output handoffs rather than inferred similarity edges.

The live evidence is deliberately bounded: these were small behavioral trials, not production-frequency measurements. Exact model-token or billing usage was not exposed, and the planned single-module no-spawn control could not start after the collaboration thread limit was reached. It remains a structurally validated case rather than a claimed live pass.

## MIT OCW expansion roadmap

The [CS, mathematics, and quantitative-finance course roadmap](research/mit-ocw-course-roadmap-2026-09-26.md) is optimized for four outcomes: faster and more reliable codebases, empirical quant research, trading and portfolio development, and production systems for investment firms. It combines software construction, algorithms, systems, databases, and performance engineering with statistics, econometrics, optimization, investments, adaptive markets, and integrated quantitative finance.

The roadmap is not a claim that MIT OCW alone teaches how to operate a hedge fund. It explicitly identifies missing operational areas—prime brokerage, fund administration, current regulation, market-data governance, OMS/EMS and exchange connectivity, production microstructure, and compliance—that require current regulator, exchange, broker, and vendor sources. Courses remain traceable evidence sources, while the skill tree is organized around capabilities instead of creating one overlapping subskill per course.

The parent is deliberately not a general statistics or mathematics skill. Overlapping prerequisites activate it only when they are applied to quantitative finance or when the user explicitly asks about the curated MIT corpus. Analysis never authorizes trade execution or production-state mutation.

## Four course deep dives and skills

Four high-value courses now have separate source-backed research briefs and separately installable skills:

| Course | Deep research | Skill | Owns |
|---|---|---|---|
| MIT 6.172 | [Performance Engineering of Software Systems](research/courses/mit-6-172-performance-engineering.md) | [`mit-6172-performance-engineering`](skills/mit-6172-performance-engineering/) | Profiling, benchmarks, bottleneck diagnosis, safe optimization, and before/after verification |
| MIT 15.481x | [Adaptive Markets](research/courses/mit-15-481x-adaptive-markets.md) | [`mit-15481x-adaptive-markets`](skills/mit-15481x-adaptive-markets/) | Market adaptation, hedge-fund ecology, crowding, liquidity/leverage feedback, crises, and ethics |
| MIT 15.450 | [Analytics of Finance](research/courses/mit-15-450-analytics-of-finance.md) | [`mit-15450-analytics-of-finance`](skills/mit-15450-analytics-of-finance/) | Advanced workflows integrating econometrics, stochastic pricing, Monte Carlo, volatility, and dynamic choice |
| MIT 18.642 | [Topics in Mathematics with Applications in Finance](research/courses/mit-18-642-quantitative-finance.md) | [`mit-18642-quant-finance`](skills/mit-18642-quant-finance/) | Course-guided learning and broad mathematics-to-finance translation |

The [course-skill network report](research/course-skill-network-2026-09-26.md) records the research-to-skill briefs, Graphify audit, derived route/dependency map, and ICM-informed cold walk. Graphify found the main overlap between 15.450 and 18.642: both cover empirical information sets and stochastic pricing. The catalog resolves this by goal—18.642 owns broad course learning, while 15.450 owns advanced integrated multi-method work.

The parent routes multi-course work by artifact rather than asking four agents to answer the same question. For example:

```text
15.481x adaptive hypothesis
    → 15.450 empirical specification and uncertainty
        → 6.172 measured implementation optimization
```

That chain runs only when each downstream stage consumes the upstream result. Independent course/source and implementation audits may run in parallel; ordinary one-course requests stay with one agent.

## External learning-memory research

The [external-memory research report](research/agent-learnings-external-memory-2026-09-26.md) evaluates the proposal to keep an `AGENT_LEARNINGS.md` that records mistakes and is read before future work.

The conclusion is **useful with controls, unsafe as a raw diary**:

- A small, versioned file of externally verified, reusable lessons is a sensible pilot.
- Unverified observations belong in quarantine, not in active instructions.
- Every active lesson needs a scope, evidence, exceptions, a regression test, and a review or expiry date.
- Duplicate, contradicted, and stale lessons must be merged, superseded, or removed.
- Once the collection grows, the agent should load a short index and retrieve only relevant records rather than read the entire history.
- Markdown plus Git is sufficient at the current scale. Hindsight scored 6/20 on the adoption rubric, so the report recommends revisiting a memory service only when multi-agent, multi-user, temporal, provenance, or retrieval pressure materially outgrows files.

The report distinguishes external memory from retraining, reviews controlled academic evidence and production patterns, specifies security boundaries, and defines a four-arm experiment: no memory, raw append-only Markdown, curated Markdown, and curated retrieval. The experiment measures repeated errors, transfer, false-memory harm, staleness, token cost, and latency.

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
- Live parent-to-subagent trials passed independent parallel routing and a staged empirical-to-portfolio artifact handoff after correcting one observed over-routing defect.
- A pinned Microsoft SkillOpt surrogate run rejected further edits at 0.9875 → 0.9875; its sealed four-case test scored hard 1.0 and soft 0.9675 with no backend or parse failures.

See [the evaluation report](evaluations/skillopt-2026-09-26/REPORT.md) for the run history, council findings, method limits, architecture comparison, and sandbox candidates. The SkillOpt cases are reviewed authored surrogates, not mined production usage or native skill-discovery measurements.

## Architecture token-use experiment

This experiment compared four ways to package the same six `trade-ngin` knowledge domains across 11 equally weighted request cases. It was used as a controlled architecture test for Ingenius; it was not a benchmark of investment performance or model intelligence.

Token counts use `tiktoken` with `o200k_base` over discovery metadata and the skill/reference files that each case would load. They exclude the user prompt, runtime wrappers, repository reads, model output, latency, and billed API accounting.

### Architecture comparison

| Architecture | Catalog tokens on every request | Mean activated case | Narrow focused mean | Cross-domain mean | Worst activated case | Blind behavior result |
|---|---:|---:|---:|---:|---:|---:|
| One monolithic `SKILL.md` | 95 | 3,588 | 3,588 | 3,588 | 3,588 | 11/11 |
| Routed parent + conditional references | **95** | 1,605 | 1,478 | **2,348** | **2,792** | 10/11 as originally written |
| Four coarse sibling skills | 310 | 2,053 | Not separately reported | Not separately reported | 4,399 | 11/11 |
| Six matched-granularity sibling skills | 432 | **1,504** | **1,210** | 2,689 | 3,434 | 11/11 |

The matched sibling design used 6.3% fewer tokens than the routed design in the equally weighted average because most cases were narrow. The routed design still used 55.3% fewer tokens than the monolith and had the lowest catalog cost and cross-domain worst case. Its one behavioral miss was an under-routed live/backtest parity case; the routing rule was corrected to include strategy/statistics and portfolio/risk when those stages can cause the divergence.

### Workload sensitivity

| Modeled request mix | Routed parent | Matched siblings | Lower estimate |
|---|---:|---:|---|
| Narrow-heavy | 1,492.5 | **1,391.6** | Matched siblings |
| Balanced | **1,597.3** | 1,648.3 | Routed parent |
| Cross-domain-heavy | **1,814.8** | 2,017.9 | Routed parent |

For these cases and weights, the estimated crossover occurs when cross-domain requests exceed about 44.0% of focused-plus-cross requests. That number is experiment-specific, not a general constant.

The boundary cases also favored the routed parent:

- Unrelated request that should activate nothing: 95 tokens for routed references versus 432 for matched siblings.
- Parent-only live-operation safety question: 1,008 tokens for routed references versus 1,195 for matched siblings.
- Loading every routed reference at once: 3,821 tokens, which is 233 more than the 3,588-token monolith. Progressive disclosure helps only when most requests load a subset.

### Ingenius package measurements

| Ingenius context component | Estimated tokens |
|---|---:|
| Discovery metadata | 99 |
| Parent `SKILL.md` | 933 |
| One ordinary domain reference | 548–724 |
| Discovery + parent + one ordinary domain | **1,580–1,756** |
| Discovery + every package file | 5,769 |

An ordinary routed Ingenius request therefore loads about 69.6–72.6% less skill context than loading the entire catalog-inclusive package. This supports the current parent-plus-references architecture, but it does not prove that architecture universally optimal. A sibling should be promoted only when real request data shows a distinct user goal, non-overlapping activation, its own inputs and outputs, and mostly narrow traffic.

### Live-agent and Graphify telemetry limits

The live delegation trials verified parallel routing and a staged empirical-to-portfolio handoff, but the collaboration interface did not expose exact worker token or billing usage. Likewise, Graphify token fields remained `0` when host-agent semantic extraction lacked token telemetry. Those zeroes mean **unavailable measurement**, not zero computational cost. The static measurements above are therefore suitable for comparing skill-file context, not for claiming exact runtime savings from subagents.

The decision-relevant evidence is preserved in [ARCHITECTURE_EVIDENCE.md](evaluations/skillopt-2026-09-26/ARCHITECTURE_EVIDENCE.md), while the broader optimization and behavioral results are in [REPORT.md](evaluations/skillopt-2026-09-26/REPORT.md) and the [delegation-routing report](evaluations/delegation-routing-2026-09-26/REPORT.md).
