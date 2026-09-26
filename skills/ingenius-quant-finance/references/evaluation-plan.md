# Evaluation Plan

Evaluate activation, routing, output behavior, and delegation separately. Use held-out tasks not copied or closely paraphrased from the source corpus.

## Activation cases

| Request | Expected behavior |
|---|---|
| “Review my rolling GARCH forecast using the MIT finance-course framework.” | Activate; empirical only |
| “Why does physical drift vanish from this option-pricing PDE?” | Activate; stochastic pricing only |
| “Stress this constrained minimum-variance portfolio.” | Activate; portfolio/risk only |
| “Build a prerequisite-aware path through the two OCW offerings.” | Activate; course map + learning/projects |
| “Evaluate a PCA yield-curve backtest and resulting butterfly portfolio.” | Activate; empirical + portfolio/risk |
| “What stock should I buy today?” | Do not behave as an investment recommender; current research would be a separate task |
| “Summarize this corporate-finance filing.” | Do not activate |
| “Implement generic matrix multiplication.” | Do not activate |

Include indirect, incomplete, near-miss, and boundary-negative phrasings in the test set.

## Routing cases

- Empirical only: diagnose a nonstationary AR fit.
- Portfolio only: inspect infeasible allocation constraints.
- Pricing only: verify a one-period replicating portfolio.
- Learning only: diagnose confusion between covariance and correlation.
- Course map only: identify whether a named session has public technical material.
- Multi-module: test a PCA portfolio backtest or estimated-volatility option model.
- Parent only: explain the skill's scope.
- Ambiguous: “Help with my finance problem” should request the problem and desired help level rather than load all modules.

Record required and forbidden modules. Repeated all-module loading is a routing failure even if the final answer is correct.

## Output checks

Blind-grade skill-assisted and ordinary baselines on:

- mathematical correctness;
- explicit, appropriate assumptions;
- correct empirical-versus-pricing distinctions;
- information-set integrity and absence of look-ahead;
- verification quality;
- source fidelity and handling of unavailable material;
- tutoring diagnosis and transfer quality;
- unsupported current-market, causal, or profitability claims;
- tokens, latency, and unnecessary module loading.

Hard failures include calling a pricing measure a physical forecast, accepting invalid replication, using future data in a live backtest, inventing unavailable lecture content, or presenting coursework as personalized investment advice.

## Structural checks

- Exactly one `SKILL.md` exists in the package.
- Every parent route resolves to a file.
- Every operational module is reachable from the parent in one read.
- Cross-links do not create a mandatory loading cycle.
- Shared invariants have one canonical home.
- `agents/openai.yaml` names `$ingenius-quant-finance` in its default prompt.

## Subagent ablation

Default to one agent. For a complex proof, model comparison, or provenance audit, compare one-agent work with an independent solver/checker or source-review arrangement. Keep delegation only when it reduces serious errors or wall-clock time enough to justify token, latency, and synthesis costs. Agent agreement alone is not verification.
