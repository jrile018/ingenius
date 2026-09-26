# Graph Report - low-latency-skill-graph.J6lxIZ  (2026-09-26)

## Corpus Check
- Corpus is ~6,316 words - fits in a single context window. You may not need a graph.

## Summary
- 175 nodes · 193 edges · 12 communities
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 34 edges (avg confidence: 0.85)
- Token cost: 6,842 input · 14,530 output

## Community Hubs (Navigation)
- Correctness and Measurement
- Network Paths and DPDK
- Replay and Execution Research
- Microarchitectural Tooling
- Nasdaq Protocol State
- Dense Linear Algebra
- Compiler and Roofline
- x86 Target Optimization
- Hardware Placement
- Arm SIMD
- Networking Replication
- Market Regime Models

## God Nodes (most connected - your core abstractions)
1. `Low-Latency Quantitative Systems Research` - 17 edges
2. `Stanford MS&E 448 — Big Financial Data for Algorithmic Trading` - 10 edges
3. `Linux Networking, Queue Placement, and Timestamping` - 9 edges
4. `Stanford CS244 — Advanced Topics in Networking` - 8 edges
5. `DPDK Poll-Mode Networking` - 8 edges
6. `uops.info Instruction Measurements` - 8 edges
7. `UT Austin — ALAFF` - 7 edges
8. `LAFF-On Programming for High Performance` - 7 edges
9. `Cartea–Jaimungal Asset-Price Models for Algorithmic and High-Frequency Trading` - 7 edges
10. `Stanford CS349F — Fabric Architectures for AI Systems` - 6 edges

## Surprising Connections (you probably didn't know these)
- `Network-Latency Experiment Specification` --semantically_similar_to--> `Network Timestamp Boundaries`  [INFERRED] [semantically similar]
  courses/stanford-cs244.md → implementation/linux-networking.md
- `Joint Tail-Latency and Goodput Evaluation` --semantically_similar_to--> `Burst and Tail-Latency Testing`  [INFERRED] [semantically similar]
  courses/stanford-cs349f.md → implementation/linux-networking.md
- `Deterministic Full-Depth Replay Benchmark` --semantically_similar_to--> `Deterministic Order-Book Replay`  [INFERRED] [semantically similar]
  courses/stanford-msande448.md → implementation/kearns-nevmyvaka.md
- `Inventory, Fill, and P&L Reconciliation` --semantically_similar_to--> `Event-by-Event Trading-Ledger Reconciliation`  [INFERRED] [semantically similar]
  implementation/cartea-jaimungal.md → courses/stanford-msande448.md
- `Low-Latency Quantitative Systems Research` --references--> `UC Berkeley CS267 — Applications of Parallel Computers`  [EXTRACTED]
  README.md → courses/berkeley-cs267.md

## Hyperedges (group relationships)
- **Performance Evidence Loop** — readme_defensible_optimization_workflow, courses_eth_fast_numerical_code_profile_optimize_explain, courses_berkeley_cs267_scaling_analysis, courses_stanford_cs149_scaling_diagnosis [INFERRED 0.85]
- **Correctness Before Performance** — readme_measurement_contract, courses_cornell_cs6210_numerical_acceptance_gates, courses_kit_nla4hpc_numerical_kernel_contract, courses_oxford_market_microstructure_trading_simulator_invariants [INFERRED 0.95]
- **Architecture and Placement Decisions** — courses_epfl_math454_architecture_selection, courses_illinois_ece408_cpu_gpu_placement, courses_nyu_ull_architectures_system_placement_choices [INFERRED 0.85]
- **Measurement-Preserving Optimization** — courses_ut_austin_alaff_numerical_correctness_acceptance_gates, courses_ut_austin_laff_performance_reference_implementation_and_correctness_oracle, implementation_amd_optimization_deployment_cpu_validation, implementation_arm_simd_scalar_oracle_and_tail_correctness, implementation_llvm_mca_wall_clock_and_counter_corroboration, implementation_uops_info_application_workload_and_counter_validation [INFERRED 0.85]
- **End-to-End Network Tail-Latency Control** — courses_stanford_cs244_network_latency_experiment_specification, courses_stanford_cs349f_joint_tail_latency_and_goodput_evaluation, implementation_dpdk_queue_core_and_numa_ownership, implementation_dpdk_timestamp_burst_and_recovery_boundaries, implementation_linux_networking_network_timestamp_boundaries, implementation_linux_networking_network_benchmark_configuration_record, implementation_linux_networking_burst_and_tail_latency_testing [INFERRED 0.85]
- **Market Event and Order-State Correctness** — courses_stanford_msande448_event_by_event_trading_ledger_reconciliation, courses_stanford_msande448_deterministic_full_depth_replay_benchmark, implementation_cartea_jaimungal_inventory_fill_and_pnl_reconciliation, implementation_kearns_nevmyvaka_deterministic_order_book_replay, implementation_nasdaq_itch_itch_order_lifecycle_state_machine, implementation_nasdaq_itch_partial_execution_and_replace_invariants, implementation_nasdaq_ouch_ouch_order_state_machine, implementation_nasdaq_ouch_retransmission_and_mirrored_session_recovery [INFERRED 0.85]

## Communities (12 total, 0 thin omitted)

### Community 0 - "Correctness and Measurement"
Cohesion: 0.08
Nodes (28): End-to-End Trading-Path Measurement, Trading-System Domain Skeleton, University of Chicago FINM 32700 — Low Latency Trading Systems, Event-Level Stochastic Models, Realistic Event Streams, University of Chicago FINM 37602 — Mathematical Market Microstructure, CMU 15-418/15-618 — Parallel Computer Architecture and Programming, Concurrency Validation Gates (+20 more)

### Community 1 - "Network Paths and DPDK"
Cohesion: 0.09
Nodes (26): Network-Latency Experiment Specification, Coupled Fabric Control, Deterministic Ultra-Low Latency Near Saturation, Edge–Network Coordination Contract, Joint Tail-Latency and Goodput Evaluation, Official Stanford Bulletin Entry, Stanford CS349F — Fabric Architectures for AI Systems, Stanford Spring Course Schedule (+18 more)

### Community 2 - "Replay and Execution Research"
Cohesion: 0.12
Nodes (18): Attainable Fill Constraint, Chronological Transaction-Cost-Aware Validation, MS&E 448 Course Home, MS&E 448 Course Information, Deterministic Full-Depth Replay Benchmark, Event-Level Market-Data Workloads, 2020 HFT Final Report, 2021 Project Proposals (+10 more)

### Community 3 - "Microarchitectural Tooling"
Cohesion: 0.12
Nodes (17): Independent Replication Process, Deployment CPU Validation, LLVM Machine Code Analyzer, Official llvm-mca Command Guide, Resource Pressure and Dependency Chains, Scheduling-Model Scope Limit, Static Processor-Pipeline Analysis, Wall-Clock and Counter Corroboration (+9 more)

### Community 4 - "Nasdaq Protocol State"
Cohesion: 0.15
Nodes (16): Event-by-Event Trading-Ledger Reconciliation, Inventory, Fill, and P&L Reconciliation, Displayed-Book and Statistics Separation, ITCH Order-Lifecycle State Machine, Nasdaq TotalView-ITCH 5.0 Market-Data Protocol, Nasdaq TotalView-ITCH 5.0 Specification, Partial-Execution and Replace Invariants, Protocol-Revision-Pinned Feed Fixtures (+8 more)

### Community 5 - "Dense Linear Algebra"
Cohesion: 0.14
Nodes (15): ALAFF Front Matter, Conditioning and Finite Precision, Data-Movement Cost Model, Numerical-Correctness Acceptance Gates, Optimizing Matrix Multiplication, Simple Computer Model, Structure-Aware Optimization, UT Austin — ALAFF (+7 more)

### Community 6 - "Compiler and Roofline"
Cohesion: 0.17
Nodes (12): Roofline-Style Bounds, Scaling Analysis, UC Berkeley CS267 — Applications of Parallel Computers, Compiler IR and Assembly, Compiler Transformation Proof Obligation, Cornell CS6120 — Advanced Compilers, ETH Zürich — How to Write Fast Numerical Code, Operational Intensity and Roofline Analysis (+4 more)

### Community 7 - "x86 Target Optimization"
Cohesion: 0.18
Nodes (12): Staged Kernel Transformations, AMD Architecture and Optimization Documentation, AMD Developer Documentation, AOCC Target Selection, Generation-Specific Optimization, Runtime Feature Selection, Zen 5 Software Optimization Guide, Intel Architecture and Optimization Documentation (+4 more)

### Community 8 - "Hardware Placement"
Cohesion: 0.22
Nodes (9): Architecture Selection, EPFL MATH-454 — Parallel and High-Performance Computing, Workload Classification, CPU/GPU Placement, Illinois ECE408/CS483 — Applied Parallel Programming, Offload Amortization, Infrastructure Return Analysis, NYU SPS — Ultra-Low-Latency Architectures for Electronic Trading (+1 more)

### Community 9 - "Arm SIMD"
Cohesion: 0.22
Nodes (9): Arm Performance Studio, Arm SIMD and CPU Optimization Material, Arm SIMD Optimization Portal, Generated Assembly Inspection, Neon, SVE, SVE2, and SME, Scalar Oracle and Tail Correctness, Vector-Length Model, Emitted Instruction Inspection (+1 more)

### Community 10 - "Networking Replication"
Cohesion: 0.29
Nodes (7): Failed Replication as Evidence, Midterm Report Assignment, Project Proposal Assignment, Replication Framing Assignment, Research Reading Critique Framework, Spring 2025 Course and Schedule, Stanford CS244 — Advanced Topics in Networking

### Community 11 - "Market Regime Models"
Cohesion: 0.33
Nodes (6): Calibration Version and Regime Drift, Cartea–Jaimungal Asset-Price Models for Algorithmic and High-Frequency Trading, Hidden-Regime Quoting, Open-Access 2013 Paper, UCL Repository Record, Zero-Price-Revision Trades

## Knowledge Gaps
- **56 isolated node(s):** `Research Reading Critique Framework`, `Spring 2025 Course and Schedule`, `Replication Framing Assignment`, `Project Proposal Assignment`, `Midterm Report Assignment` (+51 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 76 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `Research Reading Critique Framework`, `Spring 2025 Course and Schedule`, `Replication Framing Assignment` to the rest of the system?**
  _56 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Correctness and Measurement` be split into smaller, more focused modules?**
  _Cohesion score 0.082010582010582 - nodes in this community are weakly interconnected._
- **Should `Network Paths and DPDK` be split into smaller, more focused modules?**
  _Cohesion score 0.08615384615384615 - nodes in this community are weakly interconnected._
- **Should `Replay and Execution Research` be split into smaller, more focused modules?**
  _Cohesion score 0.11764705882352941 - nodes in this community are weakly interconnected._
- **Should `Microarchitectural Tooling` be split into smaller, more focused modules?**
  _Cohesion score 0.125 - nodes in this community are weakly interconnected._
- **Should `Dense Linear Algebra` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._