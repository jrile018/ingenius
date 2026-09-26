# UT Austin — ALAFF

## Scope and public material

ALAFF is a public, continuously maintained treatment of applied linear algebra. The January 2026 materials include HTML chapters, a PDF, videos, exercises, solutions, figures, and presentation source.

## What it contributes

ALAFF joins floating-point reasoning with practical algorithms for least squares, direct and iterative solvers, eigenproblems, and singular-value decompositions. Its performance chapters explain why data movement from memory to registers dominates many kernels and build multilevel blocking, packing, and vector-register reuse from that model. Its mathematical chapters supply the missing acceptance gates: residuals, conditioning, structural assumptions, and the consequences of finite precision.

## Transfer to trading systems

A faster solver is not acceptable if a portfolio optimizer changes feasibility, a calibration becomes unstable, or a risk decomposition loses required accuracy. The skill should pair runtime evidence with residual/error checks, conditioning awareness, convergence tests, and explicit tolerances. It should exploit symmetry, sparsity, or low rank only when the model actually guarantees that structure.

## Limits and licensing

The material teaches numerical computing broadly and does not define finance-specific tolerances or execution semantics. The site contains a GNU Free Documentation License appendix; users should follow the exact notice attached to the selected artifact rather than assume every linked asset has identical terms.

## Sources

- [ALAFF front matter](https://www.cs.utexas.edu/~flame/laff/alaff/frontmatter.html)
- [Simple computer model](https://www.cs.utexas.edu/~flame/laff/alaff/chapter12-simple-model.html)
- [Optimizing matrix multiplication](https://www.cs.utexas.edu/~flame/laff/alaff/chapter12-optimizing-MMM.html)
