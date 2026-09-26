# ETH Zürich — How to Write Fast Numerical Code

## Scope and public material

The Spring 2026 edition of course 263-0007 is the strongest single source in this corpus for connecting algorithms, implementations, microarchitecture, and measured runtime. Its public page provides lecture slides and recordings, profiling material, homework information, prior exams and solutions, and project/report guidance. Some submission infrastructure remains behind Moodle.

## What it contributes

The sequence covers arithmetic cost, operational intensity, instruction-level parallelism, Intel microarchitecture, compiler limits, benchmarking, SIMD/AVX, automatic vectorization, caches and blocking, roofline analysis, BLAS, sparse matrix-vector products, FFTW, and SPIRAL. Its project pattern is especially reusable: begin with correct tested C/C++, count relevant work, measure, profile, optimize hot spots, and explain the result with plots and machine behavior.

## Transfer to trading systems

A pricing, calibration, feature, book-aggregation, or risk kernel should not be called faster because its source looks vectorized. The skill should require a reproducible baseline, an identified hot region, an explicit cost model, generated-code or counter evidence where relevant, and an end-to-end check on the actual event or batch workload. Operational intensity and roofline reasoning help distinguish arithmetic limits from data movement before an engineer reaches for intrinsics or threads.

## Limits

This is a master-level numerical-performance course, not a trading-systems course. It assumes C and matrix algebra. The current course prohibits AI assistance on assessed work; the research uses public methodology and must not be used to solve active graded assignments. No broad open-content license was identified, so this repository links and paraphrases rather than copying course artifacts.

## Sources

- [Course overview](https://acl.inf.ethz.ch/teaching/fastcode/)
- [Spring 2026 course](https://acl.inf.ethz.ch/teaching/fastcode/2026/)
