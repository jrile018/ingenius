# Karlsruhe Institute of Technology — Numerical Linear Algebra for HPC

## Scope and public material

KIT course listings identify Numerical Linear Algebra for Scientific High Performance Computing. A public BSD-3-Clause exercise framework from the course provides CMake scaffolding, unit-test locations, benchmark locations, dense and sparse kernel exercises, OpenMP/CUDA work, and Ginkgo-based correctness checks.

## What it contributes

The framework deliberately separates implementation, tests, and benchmarks so students can focus on kernels without losing correctness infrastructure. Public descriptions of the exercise sequence cover dense BLAS, parallel matrix-vector products, task-based LU, compressed sparse row multiplication, and conjugate gradients.

## Transfer to trading systems

Every optimized numerical kernel should have a reference implementation, edge-case unit tests, and a benchmark harness with representative shapes. Build scaffolding and correctness checks should be reusable so optimization experiments do not repeatedly reconstruct infrastructure. GPU and CPU candidates should implement the same numerical contract.

## Limits and licensing

The inspected exercise framework is from Winter 2020 and is not a current complete course site. Its repository is BSD-3-Clause, but linked course documents may have different terms.

## Sources

- [KIT course listing](https://www.math.kit.edu/vvz/seite/vvz-w21/de)
- [Public exercise framework](https://github.com/pratikvn/nla4hpc-exercises-framework)
