# Parent-to-Subagent Routing Experiment

Date: 2026-09-26

## Result in plain English

The architecture works for the two behaviors that matter most:

1. Independent work is routed to different specialist modules and can run in parallel.
2. Dependent work is run in order, with a named artifact passed from the upstream worker to the downstream worker.

The first trial also found a real bug: a source-coverage worker was given the empirical module merely because the request contained the word “PCA.” The routing rule was changed from topic-keyword matching to decision ownership. A fresh rerun then assigned only `course-map.md` to the coverage worker and only `stochastic-pricing.md` to the pricing worker.

This is a good architecture when subagents have genuinely separate or dependent work products. It is a bad default for every question because spawning workers adds context, output, and synthesis cost. The parent therefore defaults to one agent and delegates only when the benefit is explicit.

## What was built

There is one discoverable parent:

```text
skills/ingenius-quant-finance/SKILL.md
```

The parent routes workers to supporting reference modules:

```text
course-map.md
empirical-research.md
portfolio-risk.md
stochastic-pricing.md
learning-projects.md
```

These references are subskill modules, not additional discoverable `SKILL.md` files. This avoids overlapping activation while still giving each worker a narrow operating contract.

The runtime rules live in [`delegation-routing.md`](../../skills/ingenius-quant-finance/references/delegation-routing.md). Every worker receives an exact module path, inputs, one bounded decision, a return contract, forbidden scope, and a stopping condition. The parent always retains final synthesis.

## Experiment 1: independent work in parallel

Request:

> Verify which public MIT materials cover financial PCA, and independently derive why physical drift disappears from the Black–Scholes PDE.

### First run: useful failure

The parent correctly created two parallel workers and synthesized their answers, but the coverage worker received both `course-map.md` and `empirical-research.md`. Only the course map was needed. The router had followed the noun “PCA” instead of the worker's actual decision, which was source coverage.

Correction:

> Choose the worker's primary module by the decision it owns, not by nouns in the prompt.

### Fresh rerun: pass

```text
parent
├── coverage worker -> course-map.md
└── pricing worker  -> stochastic-pricing.md
     (parallel)
          ↓
    parent synthesis
```

Observed result:

- Both workers ran concurrently.
- The coverage worker read `course-map.md`, not the empirical module.
- The pricing worker read `stochastic-pricing.md`.
- Each worker stayed within its allowed task.
- The parent reconciled the results and produced one answer.

## Experiment 2: dependent work in stages

Request:

> Audit a rolling PCA factor design, then assess a constrained portfolio that consumes the corrected factors.

Observed schedule:

```text
empirical worker
    ↓ returns CORRECTED_PCA_SPEC
portfolio worker
    ↓ consumes CORRECTED_PCA_SPEC verbatim
parent synthesis
```

This passed the important dependency test: the portfolio worker was not spawned while the PCA worker was still running. It appeared only after the parent received and checked the upstream artifact. The portfolio worker read only `portfolio-risk.md` as its domain module and explicitly confirmed that it did not modify the artifact.

## Structural checks

The automated verifier checks the contract rather than answer wording. It confirmed:

- one discoverable `SKILL.md`;
- five domain modules and four directed dependency edges;
- an acyclic runtime graph;
- exact worker fields for every spawning case;
- resolvable parent-to-reference links;
- parent ownership of synthesis;
- a 716-word parent, below the 750-word guardrail; and
- a two-reference delegated cold path: delegation contract, then assigned module.

Run it with:

```bash
python3 evaluations/delegation-routing-2026-09-26/verify_delegation_contract.py
```

The authored cases are in [`cases.json`](cases.json), and the machine-readable observed results are in [`RESULTS.json`](RESULTS.json).

## What this proves—and what it does not

The experiment supports these claims:

- The parent can route independent workers to different modules.
- It can stage a true dependency and pass an explicit artifact downstream.
- A narrow routing defect can be exposed by a live trial and corrected without splitting the package into competing skills.

It does not prove:

- that every future prompt will route perfectly;
- that subagents always improve answer quality;
- that this architecture saves tokens; exact model-token usage was not exposed; or
- that the narrow single-module no-spawn control passed live. That run could not start after the collaboration thread limit was reached, so it remains a specified structural case rather than claimed behavioral evidence.

A separate post-edit council turn was attempted but could not start under the same thread limit. The fresh parallel and staged coordinators plus their four specialist workers are the live behavioral evidence; the deterministic validators are the final file-level evidence. Earlier architecture, behavior, and packaging council reviews remain in the [SkillOpt evaluation report](../skillopt-2026-09-26/REPORT.md), but they are not presented as reviews of this later routing patch.

## Recommendation

Keep this design:

- one parent skill for activation and shared invariants;
- subskill reference modules for domain-specific reasoning;
- optional subagents as a runtime overlay;
- parallel execution only for independent products;
- staged execution for real dependencies; and
- final verification and synthesis in the parent.

Do not create a permanent agent for every module. That would increase token use and coordination failure modes without adding independent reasoning value.
