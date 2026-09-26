# Stanford CS149 — Parallel Computing

## Scope and public material

The Fall 2024 course publishes its schedule, slides, course information, and assignment repositories. The assignments cover CPU performance analysis, multicore task scheduling, CUDA rendering, DNN accelerator work, and optional graph processing.

## What it contributes

CS149 treats performance as a hardware–software interaction. Topics include multicore execution, SIMD/ISPC, work distribution, scheduling, locality, communication, contention, CUDA, parallel primitives, specialization, cache coherence, false sharing, synchronization, relaxed consistency, and transactional memory. Assignment 1 requires speedup curves, per-thread timing, load-balance analysis, SIMD utilization, and explicit handling of work sizes that are not divisible by the vector width.

## Transfer to trading systems

The skill should establish a correct serial baseline and record hardware, compiler, thread count, vector width, workload, and timing method. Poor scaling should be diagnosed as decomposition, locality, contention, imbalance, bandwidth, or utilization before threads are added. SIMD tail cases and divergent lanes need explicit correctness tests. Multicore speedup, SIMD speedup, and a memory-bandwidth ceiling are different claims and should be reported separately.

## Limits

Recordings require Canvas access. The Fall 2024 schedule links a lecture index labeled Fall 2022. Assignment repositories are mutable—the current `asst1` default branch contains newer text—so reproducible evaluation must pin a commit.

## Sources

- [Fall 2024 schedule](https://gfxcourses.stanford.edu/cs149/fall24)
- [Course information](https://gfxcourses.stanford.edu/cs149/fall24/courseinfo)
- [Assignment 1 repository](https://github.com/stanford-cs149/asst1)
