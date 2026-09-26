# Ingenius skill architecture and optimization report

## Verdict

The selected design is a good fit: one thin, discoverable quantitative-finance parent plus conditional reference modules. It is materially better than a monolith for ordinary requests and safer than treating course topics as nested skills or permanent agents.

The architecture is conditional, not dogma. Supporting modules should become separate sibling skills only when real usage demonstrates independently requested goals, clean discovery boundaries, distinct outputs or permissions, and mostly narrow traffic. The existing evidence does not justify that promotion.

## What changed

The final parent now:

- activates only for quantitative-finance applications or explicit questions about the MIT corpus;
- excludes generic statistics/mathematics, unrelated corporate finance, live security recommendations, unsupported current-market claims, execution, and production mutation;
- keeps PCA/backtest review empirical unless its outputs feed an allocation, exposure, or risk decision;
- states that analytical completion does not authorize trades, orders, or production-state changes.

The evaluation plan now includes generic-statistics and generic-stochastic-calculus negatives, a PCA empirical-only contrast, and a direct non-execution case.

## How the tree is architected

```text
SKILL.md
|-- course-map.md
|-- empirical-research.md
|-- portfolio-risk.md
|-- stochastic-pricing.md
|-- learning-projects.md
|-- architecture-and-provenance.md
`-- evaluation-plan.md
```

The parent owns discovery, shared workflow, cross-domain invariants, permission boundaries, and routing. Each supporting reference owns a conditional decision set. Cross-module order exists only when one output is a real input to another: empirical → portfolio, empirical → pricing, course map → learning, or pricing → portfolio.

Graphify supplied the source-evidence network; ICM Architect supplied the catalog/shelf, one-job, one-home-per-fact, explicit-link, and cold-walk review. Neither runs during ordinary finance questions. Their compiled result is the parent routing table and the maintenance protocol in `architecture-and-provenance.md`.

## Validation result

- Codex skill structural validator: pass.
- Exactly one `SKILL.md`: pass.
- Seven parent links resolve and all reference files are reachable: pass.
- Parent word count: 619, an increase of 29 words over the prior 590-word parent and within the 40-word revision guard.
- Final agentic council: pass for skill architecture; pass for SkillOpt proposal evidence with stated limits; pass for sandbox research.
- Final SkillOpt validation score: 0.9875 with no accepted change.
- Final sealed test: hard 1.0, soft 0.9675 across four cases.
- Backend/parse errors: zero; empty or non-finite results: zero; holdout leakage: false.
- Skill before/after hash: identical.
- Three native forward tests passed the intended Ingenius behavior: pricing loaded only stochastic pricing, generic ecology regression loaded no skill, and PCA-only backtest review loaded empirical without portfolio/risk.

See [FINAL_RUN.json](FINAL_RUN.json), [RUN_HISTORY.md](RUN_HISTORY.md), [COUNCIL_REVIEW.md](COUNCIL_REVIEW.md), and [FORWARD_TESTS.md](FORWARD_TESTS.md).

## Token evidence

The earlier matched `trade-ngin` control found:

- monolith: 3,588 mean activated tokens;
- routed parent: 1,605;
- matched siblings: 1,504;
- routed parent won balanced and cross-heavy workloads; siblings won the narrow-heavy mix;
- the experiment-specific crossover was about 44% cross-domain work.

For pre-review Ingenius, discovery + parent + one ordinary domain measured 1,580–1,756 tokens versus 5,769 for the full catalog-inclusive package, a 69.6–72.6% reduction. These are static `o200k_base` file-content estimates, not live billing. See [ARCHITECTURE_EVIDENCE.md](ARCHITECTURE_EVIDENCE.md).

## Sandbox research

Microsandbox is the leading local pilot candidate; E2B is the leading managed fallback; Vercel Sandbox is a strong managed alternative; Kubernetes Agent Sandbox plus gVisor is a future fleet option; just-bash is suitable only for tier-zero shell/fixture checks. No backend has been installed or validated. See [SANDBOX_OPTIONS.md](SANDBOX_OPTIONS.md) for official GitHub links, platform caveats, containment gates, and the proposed replay topology.

## Reproduce

Structural checks:

```bash
python3 evaluations/skillopt-2026-09-26/verify_skill_tree.py --baseline-git-ref HEAD --max-added-words 40
python3 /home/john-riley/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/ingenius-quant-finance
```

SkillOpt smoke or real run:

```bash
python3 evaluations/skillopt-2026-09-26/run_skillopt_cycle.py \
  --skillopt-root '/path/to/microsoft/SkillOpt' \
  --codex-path '/path/to/codex' \
  --state-home '/new/empty/state-directory' \
  --backend codex \
  --model gpt-5.6-sol
```

The runner refuses a non-empty state directory, disables auto-adoption, and records the effective configuration and limitations. Raw `.skillopt-sleep/` evidence is intentionally Git-ignored; commit the reviewed tasks, runner, curated result, hashes, and decisions instead.
