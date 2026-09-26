# UT Austin — LAFF-On Programming for High Performance

## Scope and public material

LAFF-On Programming for High Performance is a complete public web course and downloadable text that uses matrix multiplication as a controlled laboratory. It includes notes, videos, exercises, BLIS-oriented setup, implementation variants, and performance plotting.

## What it contributes

The course progresses from a naive kernel through instruction-level parallelism, vectorization, register reuse, cache blocking, packing, and multithreading. Its central systems lesson is that arithmetic is often cheap relative to moving data, so transformations should be understood by the level of the memory hierarchy whose traffic they change. Keeping explicit kernel variants makes the contribution of each transformation inspectable.

## Transfer to trading systems

The technique applies to dense factor calculations, covariance updates, scenario batches, and other repeated numerical kernels. A skill should preserve a reference implementation and correctness oracle, introduce transformations one family at a time, and plot achieved performance across realistic sizes rather than optimize one convenient matrix. It should distinguish register reuse, cache reuse, vectorization, and threading instead of combining them in an opaque rewrite.

## Limits and licensing

Matrix multiplication is an instructional kernel, not a claim that all trading hot paths are dense linear algebra. The PDF states GNU Free Documentation License 1.2-or-later terms; redistribution must preserve the applicable notices. Historical edX availability should not be treated as a current platform guarantee.

## Sources

- [Web course](https://www.cs.utexas.edu/~flame/laff/pfhp/week0-welcome.html)
- [Course PDF](https://www.cs.utexas.edu/~flame/laff/pfhp/LAFF-On-PfHP.pdf)
- [UT Austin launch description](https://www.cs.utexas.edu/news/2019/programming-high-performance-launches-first-online-course)
