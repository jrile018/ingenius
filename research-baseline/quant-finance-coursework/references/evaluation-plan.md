# Evaluation Plan

Evaluate activation, module routing, and output quality separately. Use held-out problems that are not copied or closely paraphrased from the source repository.

## Activation Cases

| Request | Expected |
|---|---|
| "Use the MIT finance course framework to review my GARCH analysis." | Activate; empirical module |
| "Why does the physical stock drift disappear from this option-pricing PDE?" | Activate; stochastic-pricing module |
| "Build a prerequisite-aware study plan for these two OCW offerings." | Activate; source map and study module |
| "Compare constrained minimum variance with equal weights and stress the inputs." | Activate; portfolio-risk module |
| "What is today's best stock to buy?" | Do not use the skill as an investment recommender |
| "Summarize an unrelated corporate-finance filing." | Do not activate |
| "Implement a generic matrix multiplication library." | Do not activate |

## Routing Cases

- Empirical only: diagnose a nonstationary AR fit.
- Portfolio only: inspect an infeasible constrained allocation.
- Stochastic only: verify a one-period replicating portfolio.
- Study only: diagnose confusion between covariance and correlation.
- Multi-module: evaluate a PCA portfolio backtest, requiring empirical and portfolio modules.
- Parent only: explain what the skill can and cannot do.
- Ambiguous: "Help with my finance problem" should request the problem and desired help level before loading every reference.

Record required and forbidden unnecessary modules. Repeatedly loading all modules is a routing failure even if the final answer is correct.

## Output Tests

Compare the same task with and without the skill. Blind-grade:

- Mathematical correctness.
- Explicit and appropriate assumptions.
- Correct distinction between empirical and pricing claims.
- Verification quality.
- Course-source fidelity and correct handling of unavailable material.
- Tutoring diagnosis and transfer quality when applicable.
- Unsupported current-market or profitability claims.
- Tokens, latency, and unnecessary reference loading.

Hard failures include calling a pricing measure a physical forecast, declaring an invalid replication correct, using future information in an alleged live backtest, inventing unavailable lecture content, or presenting coursework as personalized investment advice.

## Subagent Ablation

Default to one agent. For a complex proof, model comparison, or source audit, compare a single-agent run with an independent solver/checker arrangement. Keep delegation only if it materially reduces serious errors or improves wall-clock time enough to justify extra tokens and synthesis risk. Agent agreement alone is not verification.
