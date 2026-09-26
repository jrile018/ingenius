# SkillOpt run history

All runs targeted `skills/ingenius-quant-finance/SKILL.md`. No run auto-adopted a change.

| Run | Purpose | Result | Decision |
|---|---|---|---|
| Deterministic mock smoke | Verify the original harness control flow | 0.983891 → 0.983891; no edits | Smoke evidence only |
| First sandboxed Codex attempt | Exercise the original 11-case suite | 0 → 0 after the Codex state database was read-only | Execution failure; excluded from skill evidence |
| First successful Codex proposal | Explore changes with the original suite | 0.99625 → 1.0; 57,858 tokens; three skill edits proposed | Council rejected: no no-regression gate and two portfolio-solver details leaked into the parent |
| Stricter boundary run | Test activation/routing/permission surrogates with no-regression | 0.99375 → 0.99375; sealed test hard 1.0 / soft 0.975; 22,941 tokens | No candidate staged |
| Interrupted frozen-run attempt | Begin final evidence run | Interrupted after the live skill was deliberately compacted during execution | Invalidated by concurrent editing; excluded |
| Final pinned frozen run | Evaluate the final revised parent with corrected splits and runner | 0.9875 → 0.9875; sealed test hard 1.0 / soft 0.9675; 23,994 tokens; zero errors | No candidate staged; final parent retained |

## Rejected first proposal

The initial optimizer suggested:

1. a general minimal-route rule;
2. Phase-I feasibility guidance for constrained optimization;
3. an IIS/minimal-conflict solver checklist.

Only the first was cross-domain, and it duplicated the existing “smallest set of modules” rule. The other two belong in `portfolio-risk.md`, not the parent. The council therefore rejected the whole proposal. This is why an optimizer score increase was not treated as sufficient evidence for adoption.

## Final run interpretation

The final run used an empty state directory, explicit `gpt-5.6-sol`, Microsoft SkillOpt commit `79124b37e9a6371e13b753f8bcd7adb1e493ade1`, Codex CLI `0.151.0-alpha.7.2`, a no-regression gate, disabled memory evolution, and disabled auto-adoption. The skill hash remained `ec3fcae8b97a9d3d3b3a16de2a3690d0182d7cebd754aeaf687af6e15013410f` before and after the run.

The correct conclusion is not that the score proves the skill optimal. It shows only that, on this root-injected authored surrogate suite, SkillOpt could not justify adding another rule to the revised parent and the sealed cases were answered successfully.
