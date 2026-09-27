# Ingenius Quant Finance

`ingenius` turns advanced university coursework and primary technical sources into source-grounded, testable Codex skills for quantitative research, trading, data platforms, performance, optimization, and investment-firm systems.

The original [`skills/ingenius-quant-finance`](skills/ingenius-quant-finance/) skill draws on public MIT OCW material and advanced empirical electives. [`skills/low-latency-quant-systems`](skills/low-latency-quant-systems/) combines cross-institution courses with primary systems sources. Six newer sibling skills own advanced portfolio theory, rigorous mathematical finance, market microstructure/execution, robust optimization, reliable quantitative data systems, and investment-firm operating architecture. These are independent engineering and learning tools, not institutional products, legal opinions, or investment-recommendation systems.

## When to use this architecture

**Use a routed parent skill when several tightly connected components form one workflow—not merely because a project contains multiple repositories.** The components may live in one repository or many. What matters is that they share invariants, regularly compose, or pass verified outputs from one stage to another.

```text
point-in-time market data
    → quantitative research
        → portfolio and risk
            → backtest or paper execution
                → accounting and monitoring
```

This architecture fits when one user goal crosses several of those stages, the parent must enforce common rules, and the final answer needs one coordinated synthesis. The parent selects the smallest relevant reference modules; it creates subagents only for independent workstreams or a real artifact handoff.

Use separate sibling skills instead when capabilities have independently requested goals, clean activation boundaries, different permissions or lifecycles, and mostly narrow requests. In short:

> Use a parent when the parts form one workflow. Use sibling skills when the parts merely coexist.

The current experiment supports this as a workload-dependent decision, not a universal superiority claim. For its modeled cases, the routed design used fewer static context tokens when cross-domain requests exceeded roughly 44%; matched sibling skills were cheaper below that point. The threshold is specific to those files, routes, and request weights.

## Repository layout

```text
ingenius/
├── source-material/mit-ocw-research/   recovered research snapshot
│   └── graphify-out/                   portable knowledge graph and report
├── research/                            source-selection and architecture reports
│   └── courses/                         four course-specific deep-research briefs
│   └── low-latency-quant-systems-2026-09-26/  20 courses + 11 primary references
│   └── advanced-electives-2026-09-26/   five advanced capability dossiers
│   └── portfolio-mathematical-finance-2026-09-26/  advanced course synthesis
├── research-baseline/                  earlier test skill for comparison
├── evaluations/skillopt-2026-09-26/    SkillOpt, council, token, and sandbox evidence
├── evaluations/delegation-routing-2026-09-26/ live routing experiment and verifier
├── evaluations/low-latency-quant-systems-2026-09-26/ design, graph, and checks
├── evaluations/advanced-elective-skills-2026-09-26/ architecture and checks
├── evaluations/portfolio-mathematical-finance-skills-2026-09-26/ routing checks
├── skills/ingenius-quant-finance/      cross-course parent skill
├── skills/low-latency-quant-systems/   end-to-end trading performance skill
├── skills/advanced-portfolio-theory/   advanced allocation decisions
├── skills/rigorous-mathematical-finance/ proof-level finance derivations
├── skills/market-microstructure-execution/
├── skills/robust-quant-optimization/
├── skills/reliable-quant-data-systems/
├── skills/investment-firm-systems/
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

## Advanced elective expansion

The [advanced-elective research set](research/advanced-electives-2026-09-26/) adds graduate or upper-level material from MIT, Stanford, Oxford, Chicago, NYU, and CMU. Courses were selected for capabilities the user repeatedly needs, not for completeness or prestige.

| Skill or extension | Representative advanced courses | What it owns |
|---|---|---|
| Existing `ingenius-quant-finance` empirical module | MIT 14.384, MIT 14.387, Stanford MS&E 448 | Persistent time series, structural breaks, causal-design boundaries, and realistic market-data validation |
| [`market-microstructure-execution`](skills/market-microstructure-execution/) | Oxford Market Microstructure, Chicago FINM 37601/37602, Stanford MS&E 448, NYU MATH-GA 2763 | Order-book mechanics, transaction costs, impact, execution schedules, fills, and market making |
| [`robust-quant-optimization`](skills/robust-quant-optimization/) | Stanford EE364A/B, MIT 15.093J | Formulation, convexity, duality/KKT, solver verification, sensitivity, and robust/stochastic decisions |
| [`reliable-quant-data-systems`](skills/reliable-quant-data-systems/) | MIT 6.5840, CMU 15-445/645 and 15-721, Stanford CS244B | Point-in-time lineage, schemas, transactions, idempotency, replication, consistency, and recovery |
| [`investment-firm-systems`](skills/investment-firm-systems/) | NYU Operating Hedge Funds, NYU FRE-GY 7841, MIT 15.S08 and 15.997 | Front/middle/back-office mapping, service providers, trade lifecycle, reconciliation, controls, and resilience |

These are sibling skills because each can be requested independently and returns a different artifact. Inside each skill, the parent `SKILL.md` routes to small reference modules—the sub-skill architecture—without creating nested discoverable skills. Cross-skill work is staged only through a concrete artifact:

```text
point-in-time data → empirical estimate → robust decision → execution policy
reconciled positions/cash → operating control and exception evidence
measured execution bottleneck → low-latency systems investigation
```

The [design brief and 16 authored cases](evaluations/advanced-elective-skills-2026-09-26/) document activation, negative boundaries, safety behavior, and acyclic handoffs. Graphify detected six Markdown research documents and 1,433 words and reported that the corpus fits one context window, so it did not need a graph. With no Gemini key or semantic-extraction agents used, the handoff map is explicitly a manually derived ICM architecture map, not a claimed semantic graph. ICM's cold walk confirmed that direct requests select one sibling and one or two modules, while ambiguous terms such as “optimize execution” route by the requested output rather than by keywords.

## Advanced portfolio theory and mathematical finance

The [advanced portfolio and mathematical-finance research set](research/portfolio-mathematical-finance-2026-09-26/) adds a deeper graduate/elective spine from MIT, ETH Zürich, NYU, Chicago, Columbia, and Oxford. It produces two sibling skills because their success criteria differ:

| Skill | Use it when the requested output is | Representative coverage |
|---|---|---|
| [`advanced-portfolio-theory`](skills/advanced-portfolio-theory/) | A defensible allocation or policy under uncertain estimates, constraints, costs, and multiple periods | Mean-variance extensions, utility/equilibrium, factors, Bayesian and Black–Litterman construction, shrinkage, robustness, risk budgeting, dynamic allocation, and out-of-sample validation |
| [`rigorous-mathematical-finance`](skills/rigorous-mathematical-finance/) | A proof or derivation with explicit stochastic objects and theorem conditions | Filtered probability, martingales and stopping, FTAP, semimartingales, Itō/Girsanov, numeraires, replication/PDE, stochastic control, optimal stopping, duality, and incomplete markets |

Routine portfolio arithmetic, VaR/ES, and Black–Scholes calculations remain with `ingenius-quant-finance`. Generic solver formulation and certification remain with `robust-quant-optimization`. Explicit MIT 15.450 or MIT 18.642 study stays with those course skills. This avoids making “advanced” synonymous with loading every mathematical module.

The main handoffs are typed and directional:

```text
point-in-time estimate + uncertainty
    → advanced portfolio construction

verified state dynamics + value equation + conditions + candidate control
    → implementable dynamic-allocation assessment

portfolio objective + variables + constraints + units + uncertainty model
    → robust solver formulation and certification
```

Graphify inspected the three-document research corpus, counted about 1,555 words, and returned `needs_graph: false`; under its small-corpus rule, no semantic graph was fabricated. ICM's cold walk kept one discoverable parent per outcome, four conditionally loaded reference modules per skill, and an acyclic route map. The [design brief, 16 authored cases, and deterministic verifier](evaluations/portfolio-mathematical-finance-skills-2026-09-26/) check direct, indirect, negative, handoff, and safety boundaries. These checks validate structure and authored routing expectations, not investment performance or live model activation rates.

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

## Cross-institution low-latency trading systems skill

The [low-latency research corpus](research/low-latency-quant-systems-2026-09-26/) expands beyond MIT to 20 institutional courses or courseware collections and 11 primary implementation, protocol, or research references. It was selected around a practical target: optimize the code architecture and mathematics inside a trading system without breaking market, numerical, concurrency, timing, or recovery semantics.

The research includes performance and numerical computing from ETH Zürich, UT Austin, Stanford, CMU, UC Berkeley, Cornell, Illinois, EPFL, and KIT; networking from Stanford; and trading systems or microstructure from Chicago, Oxford, Stanford, and NYU. It adds primary material from Linux, DPDK, LLVM, uops.info, Intel, AMD, Arm, Nasdaq ITCH/OUCH, and market-microstructure research. Each source has its own dated dossier with contribution, limits, and direct links.

### How it works

[`low-latency-quant-systems/SKILL.md`](skills/low-latency-quant-systems/SKILL.md) is the only discoverable parent. It first establishes trading correctness and a comparable measurement contract, then routes to the smallest modules that own the measured decision:

| Module | Owns |
|---|---|
| `measurement-contract.md` | Workload, clocks, baseline, distributions, comparability, and acceptance |
| `trading-correctness.md` | Feed, book, order, fill, replay, accounting, point-in-time, and protocol invariants |
| `cpu-memory-compiler.md` | Generated code, cache/TLB, data layout, SIMD, compiler, and instruction evidence |
| `numerical-kernels.md` | Algorithm, conditioning, tolerances, data movement, and CPU/GPU kernel decisions |
| `concurrency-realtime.md` | Ownership, queues, atomics, locks, affinity, NUMA, backpressure, and jitter |
| `networking-time.md` | NIC-to-application path, timestamps, Linux queues, busy polling, AF_XDP, and DPDK |
| `system-architecture.md` | Critical-path budgets and CPU/GPU/FPGA or kernel/user-space placement |

The core order is: preserve semantics, establish a baseline, localize the mechanism, make the smallest attributable change, rerun correctness gates, and compare end to end. A static pipeline estimate or a faster microbenchmark can explain a hypothesis; neither is accepted as proof of a faster trading path.

### Why the parent/sub-skill architecture fits

The “sub-skills” are conditional reference modules, not nested `SKILL.md` files. This gives activation and shared safety rules one owner while keeping unrelated material out of ordinary requests. The parent is 726 words; the parent plus one technical module is 987–1,107 words, compared with 4,660 words for every skill and reference file. Those are structural word counts, not billed-token measurements.

Temporary subagents are optional. The parent keeps tightly coupled diagnosis in one agent. It assigns one bounded module contract per worker only when workstreams are genuinely independent or a downstream specialist consumes a verified upstream artifact. Graphify is used during authoring to check relationships in the evidence corpus, and ICM principles keep the runtime catalog shallow and acyclic; neither is a runtime prerequisite.

The refreshed Graphify audit contains 175 nodes, 193 directed edges, and 12 named communities, with no dangling, missing, self-loop, or collapsed edges. Its cross-source links support the selected seams: network experiments with timestamp boundaries, offered load with tail latency/goodput, deterministic replay with execution realism, and fills/inventory with accounting. See the [graph report](evaluations/low-latency-quant-systems-2026-09-26/graphify-out/GRAPH_REPORT.md) and [interactive graph](evaluations/low-latency-quant-systems-2026-09-26/graphify-out/graph.html).

The [design brief](evaluations/low-latency-quant-systems-2026-09-26/DESIGN_BRIEF.md), [evaluation cases](evaluations/low-latency-quant-systems-2026-09-26/cases.json), and [deterministic verifier](evaluations/low-latency-quant-systems-2026-09-26/verify_skill_tree.py) preserve the architecture decision and its tests. The source and maintenance map lives in [`source-map.md`](skills/low-latency-quant-systems/references/source-map.md) and [`architecture-and-provenance.md`](skills/low-latency-quant-systems/references/architecture-and-provenance.md).

Example invocation:

```text
Use $low-latency-quant-systems to reduce p99 feed-to-book latency without changing replayed book state.
```

## Applied Trade Ngin review

The seven-skill [Trade Ngin synopsis](research/trade-ngin-multi-skill-synopsis-2026-09-26.md) applies Graphify, ICM Architect, the low-latency systems parent, the Ingenius finance parent, and the MIT 15.450, 15.481x, and 18.642 course skills to `AlgoGators/trade-ngin` at commit `08b15c0`.

Its plain-language result is that Trade Ngin is a strong daily research, backtest, and paper-accounting engine, but not yet a broker-connected live or low-latency execution stack. The immediate priorities are the repeatedly failing live watchdog, explicit fail-open/fail-closed behavior, separate gating and reporting risk measures, covariance validation, a shared daily-cycle artifact pipeline, reproducible research-promotion gates, and end-to-end data-path measurement. Existing evidence shows database work in seconds while stored mathematical kernels run in microseconds or less, so materialized adjustment factors and pipeline observability should precede CPU instruction tuning.

The review records exact source links, the code-graph result, current CI/watchdog evidence, local verification limits, and a staged implementation plan. It did not modify the Trade Ngin repository.

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

Install a skill by linking or copying its directory into your Codex skills directory. The skills built here are intended to be linked at:

```text
~/.agents/skills/<skill-name>
```

Example invocation:

```text
Use $ingenius-quant-finance to audit my rolling PCA backtest and the portfolio constraints built on top of it.
Use $market-microstructure-execution to compare an impact-aware schedule with capped participation.
Use $robust-quant-optimization to verify this constrained optimizer and stress its estimated inputs.
Use $reliable-quant-data-systems to design point-in-time market-data lineage and crash recovery.
Use $investment-firm-systems to map this trade lifecycle, reconciliations, owners, and failure controls.
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
- The advanced-elective verifier passes four sibling skills, 12 conditional modules, 16 authored routing/boundary cases, source dossiers, and acyclic typed handoffs; live model-behavior tests remain separate from these structural checks.

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
