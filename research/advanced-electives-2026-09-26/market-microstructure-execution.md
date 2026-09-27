# Market microstructure and execution electives

## Capability target

Analyze how electronic markets form prices and liquidity, turn an order objective into an execution policy, and validate cost, fill, impact, or market-making claims without confusing model output with executable evidence.

## Selected sources

- [Oxford, Market Microstructure and Algorithmic Trading (2025–26)](https://courses.maths.ox.ac.uk/course/info.php?id=6483): current advanced course covering limit-order books, order types, price impact, Almgren–Chriss, predictive signals, transient impact, limit orders, Avellaneda–Stoikov market making, and the benefits and limits of reinforcement learning.
- [Stanford MS&E 448](https://web.stanford.edu/class/msande448/info.html): historically dated project course using raw quotes, orders, and transactions for execution, market making, and intraday modeling; some materials are access-restricted.
- [Chicago FINM 37601 Mathematical Market Microstructure](https://finmath.uchicago.edu/curriculum/degree-concentrations/trading/finm-37601/): advanced mathematical/practitioner market-microstructure lens.
- [Chicago FINM 37602](https://finmath.uchicago.edu/curriculum/electives/finm-37602/): stochastic event models and high-frequency empirical behavior.
- [NYU Mathematics in Finance course catalog](https://math-finance.cims.nyu.edu/?pg=2): advanced course coverage for transaction costs, liquidity, price formation, limit-order books, auctions, and empirical analysis.

## Synthesis and boundary

The reusable workflow is market-state contract → benchmark and cost decomposition → mechanism/model → point-in-time calibration → simple baseline → chronological and regime stress. This is distinct from `low-latency-quant-systems`, which owns implementation latency and throughput, and from `ingenius-quant-finance`, which owns broad empirical and portfolio analysis.

The skill must not place orders, infer current venue rules from a syllabus, promise alpha, or treat a simulated fill as executable without queue and latency assumptions.

