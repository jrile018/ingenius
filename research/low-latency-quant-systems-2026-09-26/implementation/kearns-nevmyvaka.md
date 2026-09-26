# Kearns–Nevmyvaka — machine learning for market microstructure and HFT

## Evidence

The UPenn-hosted 2013 chapter covers reinforcement-learning execution, order-book prediction, smart-order routing with censored observations, event-level adds/executions/cancellations, partial fills, hidden liquidity, streaming data, chronological train/test methodology, and implementation shortfall.

## Skill use

Agency-execution workloads with a specified target quantity and horizon need hard volume/time constraints, causal features, no-overfill assertions, explicit terminal completion, and implementation-shortfall evaluation. Book replay should be deterministic over adds, cancellations, partial fills, and executions while acknowledging hidden-liquidity limits. Smart-order-routing estimates should handle right-censoring rather than treat submitted size as observed available liquidity.

## Limits

The chapter is historical and calls several feature ideas provisional. Some experiments use idealized midpoint execution, which the authors warn can overstate profitability. No code or dataset was linked from the chapter or identified in this review. Public accessibility does not establish an open redistribution license.

## Source

- [UPenn-hosted chapter](https://www.cis.upenn.edu/~mkearns/papers/KearnsNevmyvakaHFTRiskBooks.pdf)
