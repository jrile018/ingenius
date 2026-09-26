# Agentic council review

Three independent review roles examined the skill architecture, SkillOpt method, and sandbox research. Each reviewed twice: first to find defects, then after correction.

## Final verdicts

| Reviewer | Final verdict | Scope |
|---|---|---|
| Routing and architecture | **Pass** | Activation description, minimal routing, parent/reference ownership, execution boundary, and subagent policy |
| Evaluation method | **Pass for proposal evidence only** | SkillOpt configuration, state isolation, provenance, no-regression gate, and result interpretation |
| Sandbox research | **Pass** | Accuracy and framing of the official-GitHub sandbox comparison |

## Corrections caused by the council

### Skill behavior

- Narrowed discovery so generic regression, PCA, stochastic calculus, or other prerequisite overlap does not activate the skill without a finance application or explicit corpus request.
- Changed the broad “PCA portfolio or backtest” shortcut: PCA/backtest work stays empirical unless its outputs feed allocation, exposures, or risk.
- Added a categorical boundary: analysis does not authorize a trade, order, or production-state mutation.
- Kept live security recommendations outside the skill even when current evidence exists; current evidence may inform a valid analytical task, not turn the skill into an investment recommender.

### Evaluation design

- Replaced direct train-to-holdout semantic duplicates.
- Labeled every case as a reviewed authored surrogate and explained SkillOpt's `origin: real` compatibility vocabulary.
- Pinned gate mode, mixed metric, no-regression, model, edit budget, mining, dream/recall, fan-out, memory evolution, seed, and auto-adoption.
- Required a fresh explicit state directory and added before/after hashes to detect concurrent mutation.
- Added cache, error, parse, test-score, toolchain, and effective-configuration evidence.
- Added a baseline-relative word-growth guard and staged-candidate support to the structural verifier.

### Sandbox research

- Reframed every option as a research candidate rather than an installed solution.
- Added Microsandbox beta/platform prerequisites, E2B adapter experimental status, and Agent Sandbox policy scope.
- Replaced categorical absence claims with reviewed-source wording.
- Added a mandatory live Codex/SkillOpt spike before adopting any sandbox backend.

## Preserved architecture

The council supported one discoverable parent with ordinary Markdown references. There is exactly one `SKILL.md`; each domain reference owns one conditional decision set and is reachable in one read. Shared evidence, finance, verification, and permission rules remain in the parent.

“Sub-skill” is therefore implemented as a **supporting module**, not a nested skill. A capability becomes a separate sibling skill only when it has its own user goal, activation boundary, inputs/outputs, safety or tool boundary, and independent evaluation set. Subagents remain temporary runtime workers for independent tasks; they are not storage nodes and are not spawned merely to read modules.

## Remaining limits

- SkillOpt injects the root text into prompts. Three independent forward tests add native selection/read evidence, but they remain single runs rather than activation-rate estimates.
- One same-model run is not an estimate of production accuracy or variance.
- The task distribution is authored and balanced for coverage, not sampled from real usage.
- Static token counts estimate file context, not billing.
- Raw provider transcripts remain local because they contain complete prompts and model outputs; the repository tracks the reviewed tasks, runner, hashes, curated metrics, and decisions instead.
