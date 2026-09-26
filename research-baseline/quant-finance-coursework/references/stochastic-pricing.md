# Stochastic Processes and Pricing

## Module Contract

- **Purpose:** Review stochastic-process reasoning, Itô/SDE derivations, replication, derivatives, rates, commodities, and credit models.
- **Load when:** The request involves path dynamics, a pricing measure, hedging, a PDE, simulation, or a contingent payoff.
- **Do not load when:** The task is solely an empirical forecast or portfolio allocation from estimated returns.
- **Output invariant:** Identify the probability measure, model assumptions, payoff, hedge or valuation principle, and verification route.

## Reasoning Sequence

1. Define the state variables, filtration or information set, horizon, payoff, and tradable instruments.
2. State dynamics and parameter assumptions. Do not infer differentiability from path continuity; Brownian motion has nonzero quadratic variation.
3. Apply conditional expectation, martingale, optional-stopping, Itô, or change-of-measure results only after checking their conditions.
4. Distinguish the physical measure used for outcomes or forecasts from the pricing measure used for no-arbitrage valuation.
5. Derive the value through replication, a pricing expectation, a PDE, a tree, or Monte Carlo, and explain why the chosen route applies.
6. Verify through an alternative representation or terminal-state check.

## Core Distinctions

- A discounted physical expected payoff is not generally an arbitrage-free price.
- In a one-period complete model, verify that pricing probabilities lie in `[0,1]` and that the replicating portfolio matches every state.
- In geometric Brownian motion, applying Itô's formula to `log(S)` produces the `-sigma^2/2` drift correction.
- A Black-Scholes-style PDE requires its market and dynamics assumptions; the physical stock drift disappears through replication.
- Simulation requires increments with the correct distribution and square-root time scaling. Separate discretization error from Monte Carlo sampling error.
- Strike derivatives of option prices concern pricing distributions under appropriate regularity and measure conventions, not automatic physical forecasts.

## Rates, Commodities, and Credit

For rates, distinguish discounting, projection/index curves, forwards, and sensitivities; fitting today's curve does not determine future physical evolution or volatility. For HJM-style models, no-arbitrage links drift to volatility under the pricing measure.

For commodities and operational options, state storage, capacity, injection/withdrawal, fuel, non-storability, and market-completeness assumptions. Do not import equity replication arguments when the asset cannot be stored or traded as assumed.

For credit and counterparty exposure, state default timing, recovery, collateral, netting, wrong-way risk, discounting, and the sign convention for valuation adjustments. Exact replication in simplified zero-recovery or single-risk models may fail after adding recovery, diffusion, or another risk source.

## Verification

Check units, terminal and boundary conditions, martingale or self-financing properties, state-by-state replication, limiting cases, and consistency between analytical, tree, PDE, and simulation results where more than one method is available.
