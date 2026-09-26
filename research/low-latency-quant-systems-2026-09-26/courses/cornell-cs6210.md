# Cornell CS6210 — Matrix Computations

## Scope and public material

The Fall 2025 course publishes lecture notes and slides, assignments with Julia files, exam-review resources, and repository source. It covers stable and efficient methods for linear systems, least squares, eigenproblems, sparse and iterative methods, and sensitivity analysis.

## What it contributes

CS6210 ties algorithmic cost to representation and data movement. It covers floating-point error, conditioning, Cholesky/LU/QR, rank deficiency, regularization, sparse direct methods, SVD, stationary and Krylov iterations, conjugate gradients, GMRES, and preconditioning. Its notes explicitly distinguish arithmetic/storage cost from data movement and motivate blocked BLAS-3 formulations.

## Transfer to trading systems

Runtime claims for calibration, regression, covariance, optimization, and risk kernels should be paired with residuals, error or convergence diagnostics, condition sensitivity, and structural assumptions. A blocked, sparse, iterative, or approximate method is justified only when its error contract and workload match the trading application.

## Limits

Course collaboration systems are restricted. The repository README permits reuse of code and TeX materials, but no formal license file was identified during review, so this corpus paraphrases and links. The course does not supply market-specific numerical tolerances.

## Sources

- [Fall 2025 home](https://www.cs.cornell.edu/courses/cs6210/2025fa/)
- [Schedule](https://www.cs.cornell.edu/courses/cs6210/2025fa/schedule.html)
- [Matrix representation and memory](https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-09-03.html)
- [Floating-point error](https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-09-10.html)
