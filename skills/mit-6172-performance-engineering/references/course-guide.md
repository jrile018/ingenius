# 6.172 course-grounded guide

Read this reference for technical routing, quantitative-system applications, tutoring, provenance, and skill evaluation.

## Cross-layer diagnosis

| Observed evidence | Primary hypothesis family | Useful checks |
|---|---|---|
| Work grows too quickly with input size | Algorithm or data structure | Complexity, redundant work, batching, problem reformulation |
| Hot loop is compute-bound | Instructions and vectorization | Generated code, dependencies, branches, SIMD utilization |
| High cache misses or bandwidth saturation | Memory hierarchy | Layout, traversal order, working set, blocking, copying |
| Allocation dominates | Allocation and lifetime | Counts, size classes, ownership, pooling, locality |
| Throughput stalls with more workers | Parallel overhead | Work/span, contention, granularity, false sharing, imbalance |
| Tail latency tracks external waits | I/O or services | Queues, batching, serialization, backpressure, concurrency limits |
| Results vary with harness order | Measurement artifact | Warm-up, CPU state, caches, background work, sampling method |

Use this table to form hypotheses, not to choose a fix by keyword. Confirm the mechanism with a measurement that could disprove it.

## Performance record

For every accepted change, preserve:

- commit or patch identity;
- correctness command and outcome;
- workload and input provenance;
- compiler/runtime version and flags;
- machine and concurrency configuration;
- baseline and candidate distributions;
- profiler or counter evidence;
- effect size and uncertainty;
- introduced complexity and rollback trigger.

## Quantitative-system checks

When optimizing a backtester, simulator, optimizer, risk engine, or market-data component, also verify:

- timestamp and event-order preservation;
- point-in-time data and corporate-action semantics;
- deterministic replay where promised;
- numerical tolerances and aggregation order;
- random seed and scenario comparability;
- unchanged transaction-cost and constraint logic.

## Tutoring path

The public Fall 2018 course progresses through profiling, local transformations, architecture/vectorization, multicore work/span, compiler limits, timing, storage allocation, caches, nondeterminism, synchronization, runtime systems, autotuning, and integrated tuning. Diagnose prerequisites in C, algorithms, computer architecture, and software construction before prescribing a project.

Some public assignments lack code or depend on historical Cilk/AWS/Git environments. Adapt the learning objective to a current local toolchain rather than invent missing files or pretending the original environment is reproducible.

## Source boundaries

- [Course home](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/)
- [Syllabus](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/pages/syllabus/)
- [Calendar](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/pages/calendar/)
- [Assignments](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/pages/assignments/)
- [Projects](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/pages/projects/)
- Full research brief in the Ingenius repository: `research/courses/mit-6-172-performance-engineering.md`

## Behavioral evaluation

| Request | Expected behavior |
|---|---|
| “Profile this backtester and improve its hot path.” | Activate; establish correctness, workload, baseline, profile, and verified change |
| “Design a benchmark before parallelizing this simulation.” | Activate; define representative inputs, metrics, noise controls, and correctness oracle |
| “The profiler says allocations dominate; vectorize it.” | Activate but challenge the mechanism mismatch |
| “Rename these functions.” | Do not activate |
| “Explain Black–Scholes.” | Do not activate |

Output tests:

1. Reject a faster candidate that fails equivalence tests or races.
2. Distinguish microbenchmark improvement from end-to-end effect.
3. Disclose a flat or noisy result.
4. Preserve finance-specific temporal and numerical invariants.
5. Avoid inventing unavailable course assets.

