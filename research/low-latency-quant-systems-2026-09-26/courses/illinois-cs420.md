# Illinois CS420/CSE402/ECE492 — Parallel Programming

## Scope and public material

Illinois publishes an official course description, learning goals, and topic list, with historical public lecture links. The course covers CPU pipelines, dependencies, caches, locality, compiler optimization, vector instructions, coherence, false sharing, OpenMP, MPI, GPU programming, I/O, and parallel patterns.

## What it contributes

CS420 is a useful architecture survey because it links compiler/vectorization, cache behavior, multicore correctness, and distributed communication in one performance curriculum. It explicitly includes cost models, debugging, and evaluation rather than parallelism as an end in itself.

## Transfer to trading systems

The skill should separate instruction, cache, shared-memory, distributed-memory, and I/O bottlenecks. It should test false sharing and data placement before changing synchronization and should match a programming model to the workload's communication pattern. Generic parallelism is not automatically a latency win.

## Limits

The official page was last substantively updated in 2019 and some lecture resources use gated or historical systems. More current Stanford, CMU, and Berkeley materials should be preferred for implementation detail.

## Sources

- [Official CS420 description](https://siebelschool.illinois.edu/academics/courses/cs420-120178)
- [Historical public lecture sequence](https://courses.grainger.illinois.edu/cs420/fa2012/lectures.html)
