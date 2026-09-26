# Low-latency quantitative systems research

Research date: 2026-09-26

This corpus asks one practical question: how should a Codex skill help an engineer make a quantitative trading system faster without weakening its market, numerical, or concurrency semantics?

The answer is synthesized from 20 institutional courses or courseware collections and 11 primary implementation, protocol, or research references. Course pages are evidence libraries, not the skill hierarchy. The resulting skill is organized around decisions an engineer must make: establish the measurement contract, preserve trading correctness, select sound numerical methods, diagnose CPU/compiler behavior, control concurrency, measure networking and time, and choose system placement or offload.

## Evidence groups

| Group | Sources | Primary contribution |
|---|---|---|
| CPU and numerical code | ETH Fast Numerical Code; UT Austin LAFF-On PfHP and ALAFF; Cornell CS6210 and CS6120; KIT NLA4HPC | Measurement loop, data movement, stable numerical methods, compiler legality, test-and-benchmark harnesses |
| Parallel and systems | Stanford CS149; CMU 15-418/618; Berkeley CS267; Illinois CS420, ECE408, and CS598PA; EPFL MATH-454 | SIMD, multicore scaling, false sharing, roofline reasoning, CPU/GPU placement, communication-minimal algorithms |
| Networking and fabrics | Stanford CS244 and CS349F | Reproducible networking experiments, queues, congestion, NIC/host boundaries, tail latency near saturation |
| Trading workloads | Chicago FINM 32700 and 37602; Oxford Market Microstructure; Stanford MS&E 448; NYU ULL | Exchange/order lifecycle, event-time models, execution realism, market data, venue latency, FPGA/kernel/network design |
| Implementation references | uops.info; LLVM MCA; Intel, AMD, and Arm documentation; Linux networking; DPDK; Nasdaq ITCH and OUCH | Target-specific instruction evidence, static pipeline hypotheses, timestamping, queue/core placement, poll-mode networking, wire-level state machines |
| Primary market research | Cartea–Jaimungal; Kearns–Nevmyvaka | Event-time state, inventory and fill invariants, implementation shortfall, censored venue liquidity |

## Source-strength policy

A public lecture sequence with assignments supports procedures and evaluation methods. A catalog-only course supports a capability taxonomy, not detailed implementation rules. Vendor manuals and analysis tools support target-specific hypotheses, never universal performance claims. Student reports supply realistic failure modes but are not elevated to peer-reviewed evidence.

## Synthesis

Across the sources, the defensible workflow is:

1. Define semantic, numerical, temporal, and risk invariants.
2. Measure an end-to-end baseline with a representative event stream and pinned machine/toolchain.
3. Localize the limiting layer before selecting a transformation.
4. Change one attributable mechanism and inspect both code generation and runtime evidence.
5. Re-run correctness gates before comparable latency/throughput measurements.
6. Accept the change only when the relevant latency distribution or capacity objective improves on the deployment target.

The detailed research is split into [`courses/`](courses/) and [`implementation/`](implementation/). The research-to-skill design and architecture decisions are recorded in [`evaluations/low-latency-quant-systems-2026-09-26/`](../../evaluations/low-latency-quant-systems-2026-09-26/) so source observations remain distinguishable from derived instructions.
