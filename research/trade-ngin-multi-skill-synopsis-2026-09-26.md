# Trade Ngin applied multi-skill synopsis

Date: 2026-09-26

Repository: [`AlgoGators/trade-ngin`](https://github.com/AlgoGators/trade-ngin)

Reviewed commit: [`08b15c0`](https://github.com/AlgoGators/trade-ngin/tree/08b15c00e61b3e5c9d84cf28e708a3710bf08729)

## Plain-language conclusion

Trade Ngin is a serious **daily research, backtest, and paper-accounting engine** with unusually explicit data and accounting contracts. It is not yet a real broker-connected live-execution system or a low-latency trading stack. The best next work is to restore operational observability, make risk and failure behavior unambiguous, extract the daily cycle from very large application entry points, and measure the full database-to-result path. CPU instruction tuning is not the present bottleneck.

That conclusion is stronger than the earlier synopsis because seven complementary skills were applied to the current repository:

| Skill lens | What it added |
|---|---|
| Graphify | Located the real dependency hubs and found no import cycles. |
| ICM Architect | Exposed the missing system map and documentation drift; produced a shallow navigation design. |
| Low-latency quant systems | Distinguished measured daily-pipeline costs from speculative CPU work and checked execution/replay boundaries. |
| Ingenius quant finance | Checked point-in-time, covariance, portfolio-risk, cost, and research-promotion invariants. |
| MIT 15.450 | Added econometric validation, conditioning, uncertainty, and multi-method consistency checks. |
| MIT 15.481x | Checked regime, crowding, liquidity, capacity, and adaptive-market claims. |
| MIT 18.642 | Checked the mathematics-to-implementation seam, especially covariance and risk semantics. |

## What is already strong

1. **Data-source contracts are explicit.** The repository says to use raw prices plus per-bar corporate-action fields and compute adjustment internally, rather than trust stale vendor-adjusted columns ([source-of-truth contract](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/docs/DATA_SOURCES_OF_TRUTH.md#L12-L50)).
2. **Atomic accounting writes are treated as correctness, not style.** `DbTransaction` explains why position adjustment and corporate-action deduplication must commit together and rolls back incomplete units ([transaction contract](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/include/trade_ngin/data/postgres_database.hpp#L39-L88)).
3. **Backtest timing is deliberately modeled.** Signals use prior bars, fills use the intended pricing boundary, and current bars update valuation afterward ([beginning-of-day path](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/src/backtest/backtest_coordinator.cpp#L381-L490)).
4. **The current execution boundary is honestly documented.** The live-path `ExecutionManager` explicitly says it synthesizes paper fills and has no broker routing or partial-fill handling ([execution boundary](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/include/trade_ngin/live/execution_manager.hpp#L14-L31)).
5. **There is substantial regression coverage and a benchmark harness.** The current reviewed commit passed the repository's main [CI/CD run](https://github.com/AlgoGators/trade-ngin/actions/runs/33984177190). The benchmark suite uses fixed input generation, warm-ups, medians, p95, and an optimization barrier.

## Findings by priority

### P0 — restore operational confidence

The latest public scheduled [Live Trading Watchdog run](https://github.com/AlgoGators/trade-ngin/actions/runs/36176903193) failed at “Check that live trading is writing,” and the listed daily watchdog runs from September 14–25 also failed. Checkout, environment setup, self-test, and dependency installation succeeded in the latest run; the public metadata does **not** establish whether the cause is stale results, database/secrets access, or an engine failure.

Treat this as a production-observability incident before optimizing internals:

1. Make the watchdog emit a machine-readable reason code, last successful run ID, expected-versus-observed timestamp, and the checked data destination.
2. Separate “the workflow ran,” “the strategy completed,” “results were persisted,” and “results passed reconciliation.”
3. Page or block promotion on stale/invalid paper results rather than allowing a green main build to imply operational health.

### P1 — define failure policy and make risk fail safely

Several paths warn and continue with plausible output:

- Missing market data returns a default `RiskResult` whose recommended scale is `1.0` ([risk default](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/src/risk/risk_manager.cpp#L25-L42)).
- A strategy `on_data` error is logged, but the manager still reads its targets and proceeds ([strategy continuation](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/src/portfolio/portfolio_manager.cpp#L197-L245)).
- Optimization and risk failures can continue without those controls.
- A failed backtest day can append the prior equity value, creating a plausible flat segment instead of marking the run invalid ([backtest continuation](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/src/backtest/backtest_coordinator.cpp#L283-L306)).

Define one policy table by mode and stage. A paper/live risk or required-data failure should fail closed or produce an explicitly invalid run. A research backtest may continue for diagnostics, but its result must carry invalid intervals and must not pass promotion gates.

### P1 — separate the two meanings of portfolio risk

`RiskResult::portfolio_var` first contains a gating volatility based on dollar-notional weights, then is overwritten by a reporting volatility based on weights without contract multipliers. The source carefully documents that these can diverge ([reporting form](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/src/risk/risk_manager.cpp#L144-L180), [gating form](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/src/risk/risk_manager.cpp#L253-L313)), but one field still represents two different quantities during one calculation.

Replace it with typed, separately named outputs such as `gating_volatility` and `reported_volatility`. Record their units, annualization, weighting rule, covariance as-of time, and downstream consumers. Never overwrite a decision input with a reporting metric.

### P1 — validate covariance before using it

The optimizer checks matrix shape but does not establish finiteness, symmetry, positive semidefiniteness, or conditioning. Negative quadratic forms are clamped to zero before the square root ([optimizer calculation](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/src/optimization/dynamic_optimizer.cpp#L107-L114)), which can turn an invalid covariance into apparently zero risk.

Add a single covariance-validation boundary:

- finite values and matching labels;
- symmetry within a declared tolerance;
- eigenvalue/PSD and conditioning checks;
- documented shrinkage or nearest-PSD repair when allowed;
- perturbation tests and an explicit reject/fallback policy.

There is also a recorded mixed-empty-series crash in `calculate_covariance_matrix` ([test note](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/tests/portfolio/test_portfolio_manager_internals.cpp#L181-L189)). Production currently filters short histories before its normal optimizer call, but the function itself remains unsafe and should reject or align empty inputs.

### P1 — fix the dead excess-slippage branch

`VolumeSlippageModel` clamps `volume_ratio` to its maximum and then checks whether that clamped value exceeds the maximum, making the extra-impact path unreachable ([implementation](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/src/backtest/slippage_model.cpp#L29-L44)). A regression test explicitly records the current dead behavior ([test](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/tests/backtest/test_slippage_model.cpp#L120-L132)). Preserve the raw ratio for the excess calculation and clamp only the base-impact component.

### P1 — extract one shared daily-cycle architecture

The application entry points carry too much orchestration: `live_equity_mean_reversion.cpp` is 6,266 lines, while two portfolio live runners are about 3,300 lines each. Graph analysis also identified `PostgresDatabase`, `PortfolioManager`, and `BacktestCoordinator` as the meaningful coupling hubs. Shared types such as `Result` and `Bar` have high degree but are not architectural defects by themselves.

Use a decision-artifact pipeline:

```text
PointInTimeSnapshot
  → StrategyDecision (signals, targets, model/version, information time)
  → PortfolioDecision (optimizer, risk, fallback policy)
  → OrderIntent
  → ExecutionBoundary
       ├─ BacktestSimulator
       ├─ PaperExecutionSimulator
       └─ future BrokerAdapter
  → LedgerTransition
  → validated persistence/reporting effects
```

Backtest and paper modes should share the same decision artifacts while supplying different clocks and execution adapters. Each stage returns an artifact, validation status, provenance, and run ID. Rename user-facing “live” behavior to “paper” until a broker adapter, order-state machine, and reconciliation boundary exist.

### P2 — add a formal research-promotion gate

The code and documentation search found no systematic walk-forward, out-of-sample, holdout, bootstrap, multiple-testing, ablation, capacity, or crowding framework. That does not prove individual researchers never perform those checks; it means the repository does not make them a reproducible promotion contract.

Add a versioned model card or research artifact containing:

- observation time, universe as-of rule, data revision, and exclusions;
- chronological train/validation/test or walk-forward design;
- naive and economic baselines;
- parameter-selection scope and multiple-testing control;
- estimated costs, liquidity/capacity stress, and regime sensitivity;
- residual/stability diagnostics and uncertainty intervals;
- reproducible configuration, code commit, and acceptance decision.

The documented `sp500_membership` table is already available for survivorship-correct universes but is not wired into the engine ([available dataset](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/docs/DATA_SOURCES_OF_TRUTH.md#L57-L62)). That is a high-value first integration.

### P2 — finish or demote regime detection

`RegimeDetector` populates trend, mean-reversion, volatility, and Hurst features, but leaves volatility-of-volatility, correlation, liquidity, and stress at defaults before using those fields in its regime tree ([feature population](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/src/strategy/regime_detector.cpp#L73-L83), [decision tree](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/src/strategy/regime_detector.cpp#L325-L379)). Repository search found it instantiated in tests, not a production runner.

Treat it as an experimental component. Either remove it from production-facing architecture claims or complete the features and validate incremental value with chronological tests, ablations, transition stability, cost, liquidity, and capacity stress.

## Performance conclusion

The measured priority is the data path, not arithmetic micro-optimization.

- Documented database work fell from 14,301 ms to 800 ms for per-bar corporate actions and from 14,144 ms to 1,865 ms for delisting dates after indexing ([measurements](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/docs/DATA_SOURCES_OF_TRUTH.md#L191-L197)).
- The adjustment query still costs about 25 seconds because of a `WindowAgg`; the repository itself recommends materializing adjustment factors ([known cost](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/docs/DATA_SOURCES_OF_TRUTH.md#L199-L205)).
- Stored microbenchmark medians range from 757 ns to 223,927 ns. Those numbers are many orders below the database path and were captured on unspecified hardware, so they are baselines, not cross-machine performance claims.
- Benchmarks are not run by the current GitHub workflows, and the named `BarConversion` benchmark currently copies bars rather than measuring a real conversion ([workload](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/benchmarks/benchmark_main.cpp#L272-L279)).

Recommended order:

1. timestamp every daily-cycle stage and record query duration, row count, symbols, and dataset window;
2. materialize and incrementally maintain adjustment factors;
3. add a representative end-to-end replay benchmark;
4. add a comparable, pinned-hardware performance lane;
5. optimize CPU kernels only after profiles show they constrain the service-level objective.

A fresh local configure could not run because GTest is unconditionally required and `tests/` is always added, even with `BUILD_TESTING=OFF` ([CMake configuration](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/CMakeLists.txt#L53-L63), [test inclusion](https://github.com/AlgoGators/trade-ngin/blob/08b15c00e61b3e5c9d84cf28e708a3710bf08729/CMakeLists.txt#L213-L223)). This is a build-ergonomics finding, not evidence that the tests fail. Gate GTest and `add_subdirectory(tests)` behind `BUILD_TESTING` so benchmark-only and production builds remain possible.

## ICM navigation recommendation

Add a shallow, maintained map rather than another long narrative document:

```text
map/
├── README.md                  entry point and reading order
├── system.md                  boundaries and component ownership
├── objects.md                 bars, positions, decisions, orders, fills, ledger
├── invariants.md              time, price, accounting, risk, and data rules
├── effects.md                 database, files, email, alerts, and external calls
├── operational-status.md      CI, watchdog, known degraded paths
└── processes/
    ├── backtest.md
    └── daily-paper-cycle.md
```

The map should link to code and be checked for stale symbols in CI. Existing module READMEs contain constructor and coordinator examples that no longer match current interfaces, some docs link to absent filenames, and two corporate-action documents disagree on a same-date ticker-alias count. Keep implementation and executable contract tests authoritative; make the map an index to those sources, not a second specification.

## Graphify result and limits

The isolated code-only graph contained 8,996 nodes, 15,824 directed edges, and 488 communities. It found no import cycles. The most decision-relevant hubs were `PostgresDatabase` (degree 120), `PortfolioManager` (72), and `BacktestCoordinator` (68). It also produced 2,284 isolated code nodes, so the graph is useful for orientation and coupling hypotheses, not a complete semantic call graph.

No hosted semantic model credential was available for the Graphify documentation pass. Documentation was therefore inspected directly, and Graphify's code graph was kept in an isolated temporary directory rather than written into Trade Ngin. The repository itself was not modified.

## Verification boundary

| Check | Result |
|---|---|
| Reviewed local commit versus remote `main` | Both resolved to `08b15c0` during the review. |
| Trade Ngin working tree | Clean; no files changed. |
| Current main CI | Passed in the linked run. |
| Scheduled live watchdog | Repeated public failures; precise root cause not proven. |
| Local configure/tests | Not run because the environment lacked required GTest and CMake requires it unconditionally. |
| Benchmark comparator | Baseline self-comparison passed; no fresh timing run was claimed. |
| Graph | Static code graph plus direct documentation review; no hosted semantic pass. |

## Recommended implementation sequence

1. **Operational:** diagnose the watchdog outcome failure and add explicit stage/reconciliation status.
2. **Safety:** define fail-open/fail-closed policy; split gating and reporting risk fields.
3. **Correctness:** validate covariance; handle empty series; repair the slippage excess path.
4. **Architecture:** extract one deterministic daily-cycle pipeline and call the existing behavior paper trading.
5. **Research:** add point-in-time universe construction and a reproducible promotion artifact.
6. **Performance:** instrument end to end, materialize adjustment factors, and integrate representative benchmarks into CI.
7. **Clarity:** add the ICM map and automatically check documentation links and code symbols.
8. **Optionality:** complete and validate the regime detector, or clearly mark it experimental.

If true intraday or low-latency trading becomes a goal, build it as a separate measured hot path with sequence IDs, bounded queues and backpressure, event timestamps, an order-state machine, deterministic replay, and no synchronous PostgreSQL dependency on the critical path. Do not infer that requirement from the present daily engine or retrofit CPU-specific optimizations before an end-to-end profile justifies them.
