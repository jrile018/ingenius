# Independent native forward tests

Three fresh agents received natural requests without expected routes or evaluation rubrics. They used the installed skill link, which resolves to this repository's `skills/ingenius-quant-finance` package.

| Natural request | Files actually read | Result |
|---|---|---|
| Compact Black–Scholes drift derivation plus independent check | Parent + `references/stochastic-pricing.md` | **Pass.** Correct single-module route; preserved physical/pricing measure and expected-payoff/price distinctions; used replication and Feynman–Kac as independent checks. |
| Interpret regression coefficients and residual plot in an ecology paper | No skill or reference files | **Pass.** Ingenius did not activate for generic non-finance statistics. |
| Audit a rolling financial PCA factor backtest explicitly not used for allocation/exposure/risk | Parent + `references/empirical-research.md`; also read the separately installed Graphify root skill | **Pass for Ingenius routing.** Loaded empirical and did not load portfolio/risk. The extra Graphify read came from that separate skill's broad codebase-audit trigger, not from the Ingenius route. |

The third result identifies a neighboring-skill context-overlap risk: a broad globally installed repository-analysis skill can add context even when the Ingenius parent correctly selects its smallest domain module. This does not justify loading Graphify during ordinary finance work; Ingenius explicitly reserves its maintained graph for architecture and impact audits.

These are qualitative single-run checks, not activation-rate statistics. They add native skill-selection and reference-read evidence that the root-injected SkillOpt suite cannot provide.
