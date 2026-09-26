# UC Berkeley CS267 — Applications of Parallel Computers

## Scope and public material

The Spring 2025 course publishes its syllabus, four detailed homework sequences, and project guidance. Public work spans cache-aware DGEMM, shared and distributed particle simulation, MPI, UPC++, distributed hash tables, genome assembly, and distributed preconditioned conjugate gradient.

## What it contributes

CS267 makes scaling analysis an explicit deliverable. Homework asks for achieved FLOPS and percent of peak, successful and failed optimizations, strong and weak scaling, and decomposition of elapsed time into computation, synchronization, and communication. Projects require a hypothesis, prior work, empirical method, anticipated obstacles, and implementation-backed performance evidence.

## Transfer to trading systems

Roofline-style bounds can prevent wasted effort by revealing compute, memory, or communication ceilings. Distributed research or risk systems should report strong and weak scaling and efficiency, not speedup alone. Deterministic correctness must survive rank-count changes. Time should be attributed to useful work, synchronization, communication, and I/O before the architecture is altered.

## Limits

Recordings and some project documents require a Berkeley account. Perlmutter-specific scripts and absolute targets are not portable; the experimental method is. The course emphasizes HPC workloads, so direct application to latency-critical trading needs an end-to-end latency contract rather than aggregate FLOPS alone.

## Sources

- [Spring 2025 home](https://sites.google.com/lbl.gov/cs267-spr2025/home)
- [HW1: matrix multiplication](https://sites.google.com/lbl.gov/cs267-spr2025/hw-1)
- [HW2.2: MPI particle simulation](https://sites.google.com/lbl.gov/cs267-spr2025/hw-2-2)
- [HW4: distributed PCG](https://sites.google.com/lbl.gov/cs267-spr2025/hw-4)
