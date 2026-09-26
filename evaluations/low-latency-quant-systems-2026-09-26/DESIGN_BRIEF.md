# Design brief: low-latency quantitative systems

Date: 2026-09-26

## Repeatable job

Help an engineer diagnose, change, and verify an end-to-end quantitative trading workload whose objective is latency, jitter, throughput under load, or time/resource cost. Preserve trading semantics, numerical acceptance, concurrency correctness, temporal meaning, and operational safety while doing so.

## Inputs and outputs

Inputs may include code, profiles, benchmark output, hardware and toolchain details, event replays, numerical specifications, protocol revisions, topology, and operational constraints.

The output is an evidence record: scoped objective, invariants, baseline, localized mechanism, smallest candidate change, comparable correctness and performance results, resource/operability cost, uncertainty, and rollback condition. When the target cannot be run, the output is an executable measurement plan rather than an invented speedup.

## Activation boundary

Activate for trading, market-data, execution, pricing, risk, or quantitative-research systems with a concrete systems-performance objective. Do not activate for generic refactoring, conceptual finance, strategy profitability, or unrelated code optimization. Explicit MIT 6.172 study and generic software-performance work belong to `mit-6172-performance-engineering`.

## Evidence base

The research snapshot contains 20 public institutional courses/courseware collections and 11 primary implementation, protocol, or research references. It combines measurement and compiler methods, numerical and parallel algorithms, networking/time, trading-system architecture, market microstructure, primary market research, Linux/DPDK guidance, processor/compiler evidence, and Nasdaq ITCH/OUCH protocol semantics.

## Architecture decision

Use one discoverable parent with seven conditionally loaded technical modules:

1. measurement contract;
2. trading correctness;
3. CPU/memory/compiler;
4. numerical kernels;
5. concurrency/real-time behavior;
6. networking/time;
7. system architecture/placement.

Keep delegation, provenance, architecture, and evaluation as maintenance or conditional references. Do not create nested discoverable subskills or permanent specialist agents. The parent owns activation, shared invariants, safety, and synthesis. Temporary subagents receive a bounded module contract only when independent work or a real artifact dependency justifies them.

## Hard gates

- No speedup claim without a comparable reproducible baseline.
- No optimization accepted before applicable semantic and numerical oracles pass.
- No static instruction or pipeline estimate presented as end-to-end proof.
- No venue semantics inferred from generic coursework when a pinned protocol is required.
- No live trading, deployment, infrastructure mutation, exchange connection, or purchase without separate explicit authorization.
- No exact token-saving claim without exposed comparable runtime usage.

## Success criteria

The skill activates on held-out end-to-end trading-performance tasks, declines near misses, routes to the smallest decision-owning module set, preserves dependency order, and reports evidence and uncertainty without turning source examples into current deployment facts.
