# Oxford — Market Microstructure and Algorithmic Trading

## Scope and public material

The 2025–26 public synopsis covers electronic markets, order types, limit-order books, price impact, Almgren–Chriss execution, predictive signals, transient impact, limit-order execution, market making, informed flow, and reinforcement learning. Earlier pages add dark pools and participation strategies. An Oxford-hosted 2019 handout gives detailed mathematical treatment of execution and impact models.

## What it contributes

The material turns trading correctness into explicit state and constraints. A liquidation problem has initial inventory and a required terminal condition; execution includes instantaneous, permanent, or transient impact; and the handout studies decay-kernel sensitivity and manipulative or predatory dynamics.

## Transfer to trading systems

A simulator should conserve inventory and volume, distinguish passive-fill uncertainty from aggressive execution, include fees and impact, and test terminal inventory policies. Model optimization should test decay-kernel sensitivity, no-dynamic-arbitrage, and round-trip sanity where those assumptions apply. Faster execution simulation is invalid if it permits impossible fills or removes the economics that drive the strategy.

## Limits

The 2019 handout overlaps with the course but is not labeled as the current lecture pack. Current full materials are not public, so the skill should cite the public synopsis and handout separately. Public accessibility does not establish an open redistribution license.

## Sources

- [2025–26 course synopsis](https://courses.maths.ox.ac.uk/course/info.php?id=6483)
- [Public reading list](https://courses.maths.ox.ac.uk/mod/page/view.php?id=49306)
- [Oxford-hosted 2019 handout](https://www.maths.ox.ac.uk/system/files/attachments/NUS19_JO_handout.pdf)
