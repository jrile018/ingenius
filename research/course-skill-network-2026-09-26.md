# Four-course skill network: architecture and validation

Research date: 2026-09-26

## Architecture decision

The four courses become **separate discoverable skills** under the existing Ingenius catalog, not four supporting files inside one course skill and not four permanent agents.

Each course passes the separate-skill test because it has a distinct user-facing goal and independently testable output:

| Skill | Owned goal | Primary success contract | Principal near miss |
|---|---|---|---|
| `mit-6172-performance-engineering` | Improve measured software performance without breaking semantics | Reproducible baseline, bottleneck evidence, justified change, correctness, comparable measurement | Generic refactoring or system design without a performance workload |
| `mit-15481x-adaptive-markets` | Explain adaptive market and hedge-fund mechanisms | Actor/feedback map, competing hypotheses, falsifiers, evidence gaps | Pricing, optimization, or a request for a trade |
| `mit-15450-analytics-of-finance` | Integrate advanced quantitative methods | Model contract, estimation/derivation, uncertainty, dependent handoff, verification | Introductory finance or a single broad survey question |
| `mit-18642-quant-finance` | Teach and apply the public 18.642 bridge corpus | Prerequisite-aware guidance, mathematical translation, verified result, source status | Advanced work better owned by 15.450 or unavailable-lecture reconstruction |

The existing `ingenius-quant-finance` skill remains the cross-course parent for ordinary quantitative-finance analysis. Its `course-specialist-routing.md` catalog selects the specialist only when a course is explicit, its distinct success contract is needed, or a multi-course dependency is real.

## Rejected alternatives

- **One monolithic four-course skill:** rejected because code performance, adaptive-market interpretation, advanced integrated quant methods, and broad course tutoring have different triggers and outputs.
- **One module per lecture:** rejected because lecture order is evidence organization, not a runtime capability boundary.
- **Four permanent specialist agents:** rejected because most requests need one specialist; agent contexts add cost without changing the stored knowledge boundary.
- **Replace the Ingenius parent:** rejected because its empirical, portfolio/risk, and stochastic-pricing modules already own general cross-course analysis.

## Graphify source-evidence audit

Graphify ran in directed mode on an isolated copy containing the four research briefs and twelve skill package files. The persisted repository was not used as Graphify's working directory.

| Check | Result |
|---|---|
| Corpus | 16 files, approximately 8,565 words |
| Extracted graph | 52 nodes, 58 directed edges, 1 hyperedge |
| Communities | 6 |
| Edge confidence | 93% extracted, 7% inferred, 0% ambiguous |
| Integrity | 0 missing endpoints, 0 dangling endpoints, 0 self-loops, 0 directed collapsed edges |
| Runtime token accounting | Host collaboration API did not expose worker token usage; Graphify's placeholder remained zero and is not treated as a measured cost |

The six communities were:

1. 18.642 learning and empirical routing;
2. performance engineering;
3. 15.450 advanced quantitative methods;
4. skill interfaces and routers;
5. Adaptive Markets theory; and
6. the Adaptive Markets skill workflow.

Material graph findings:

- 15.450 no-arbitrage pricing overlaps with 18.642 stochastic pricing.
- 15.450's empirical handoff overlaps with 18.642's information-set preservation.
- 15.450's model contract overlaps with 18.642's request routing.
- 6.172 correctness/performance verification maps cleanly into its portable performance-change record.
- Each course research brief connects to one `SKILL.md`, one course guide, and one UI interface.

Those similarity edges identify overlap; they do not establish routing. The derived tree resolves ownership from user goals and output contracts.

Graphify also reported that the corpus fits in one context window. The graph is therefore useful as an architecture audit, but ordinary runtime requests should use the smaller catalog and should not rebuild or query the graph.

## Derived architecture map

| Node | Type | Owner | Trigger or load condition | Incoming dependency | Outgoing route | Canonical evidence | Test |
|---|---|---|---|---|---|---|---|
| Ingenius catalog | Parent skill | `ingenius-quant-finance` | General quant work or explicit multi-course request | User request | Smallest general module or course specialist | Parent `SKILL.md` and specialist catalog | Parent-only, single-specialist, overlap, and no-match routes |
| Performance specialist | Separate skill | `mit-6172-performance-engineering` | Concrete measurement/optimization contract or explicit 6.172 request | Optional validated quantitative implementation | Course guide; no further course route | 6.172 research brief | Allocation bottleneck must not route to vectorization by keyword |
| Adaptive-market specialist | Separate skill | `mit-15481x-adaptive-markets` | Adaptive mechanism, hedge-fund ecology, crowding, liquidity/leverage, or explicit course request | Market claim or event | 15.450 only when empirical validation is requested | 15.481x research brief | Residual return must not be declared skill automatically |
| Advanced quant specialist | Separate skill | `mit-15450-analytics-of-finance` | Explicit 15.450 or advanced multi-method workflow | Optional hypothesis from 15.481x | 6.172 only for a measured implementation bottleneck | 15.450 research brief | Estimated inputs must carry uncertainty downstream |
| Broad course specialist | Separate skill | `mit-18642-quant-finance` | Explicit course learning, problem, project, or broad translation | Learner goal or supplied work | 15.450 when advanced integrated depth is required | 18.642 research brief | Unavailable Lecture 22 content must not be invented |
| Course guide | Supporting module | Each specialist | Technical detail, provenance, tutoring, or evaluation is needed after activation | Its specialist `SKILL.md` | None | Official MIT course pages plus its research brief | Cold agent reaches it from the entrypoint in one read |

The material dependency overlay is acyclic:

```text
15.481x hypothesis and high-level test design
    → 15.450 execution-ready empirical artifact
        → 6.172 implementation optimization
18.642 broad project → 15.450 advanced derivation → 6.172 measured optimization
```

These are conditional runtime handoffs, not mandatory loading edges.

## ICM-informed navigability review

Form: **N/A — saved skills are the correct rung.** No full ICM workspace was created.

| ICM check | Result |
|---|---|
| Small stable catalog | Pass: the existing parent links one focused specialist catalog |
| One job per shelf | Pass: each course package owns one user-facing job; each course guide stores conditional detail |
| One home per fact | Pass with portability exception: full evidence lives in the research brief; each independently installable bundle repeats only the stable operational invariant and source links it needs |
| Explicit links | Pass: every `SKILL.md` names when to load its guide; the parent names when to read the specialist catalog |
| Context loading | Pass: ordinary use loads one entrypoint and at most one guide; other course packages stay out of context |
| Human edit surface | Pass: research evidence, skill contract, and course guide are separate Markdown files |

### Cold walk

A cold agent can navigate each tested request within the parent plus at most two reads:

- “Use 6.172 to optimize this backtest” → parent → specialist catalog → 6.172 `SKILL.md`.
- “Use Adaptive Markets and identify falsifying evidence” → parent → specialist catalog → 15.481x only.
- “Turn that mechanism into an execution-ready econometric test” → parent → specialist catalog → staged 15.481x-to-15.450 handoff.
- “Teach me 18.642 PCA” → parent → specialist catalog → 18.642 `SKILL.md`.
- “Estimate volatility and use it in Monte Carlo pricing” → parent → specialist catalog → 15.450 `SKILL.md`.
- “Explain PCA portfolio exposure” → parent empirical module then portfolio/risk; no course skill is loaded merely from the keyword.

The walk passes. No routing file carries the detailed course payload.

An independent forward test exercised six mixed requests. Five routes were unambiguous. The initial wording could over-route a lightweight Adaptive Markets test-design request into 15.450; the catalog was revised so 15.481x owns high-level test design and 15.450 joins only for execution-ready econometrics, inference, estimation, or implementation.

## Remaining limitations

- Structural validation and the cold walk do not measure probabilistic automatic activation in the live Codex selector.
- Output cases are authored tests, not a randomized with-skill/without-skill study.
- Course offerings are historical sources; current software, market, regulatory, and operational claims still require fresh evidence.
- The four skills were built from verified public inventories and selected pages, not a line-by-line ingestion of every video, slide, problem, and solution.
