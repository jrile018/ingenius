# ICM architecture audit

Audit date: 2026-09-26

This is the durable result of the ICM-informed review applied after Graphify mapped the research corpus. ICM was used as an authoring check, not added as a runtime dependency.

| Check | Initial result | Correction | Final result |
|---|---|---|---|
| One discoverable catalog | One parent and reference modules | None | Pass |
| One home for shared facts | Baseline, acceptance, and safety were repeated | Made `SKILL.md` canonical; modules add only domain checks | Pass |
| Cold walk | Four cases loaded three references after the parent | Parent now owns the ordinary baseline; normal phases load at most two modules | Pass |
| Acyclic shelves | Numerical→CPU and network→architecture were the only staged edges | Added deterministic DAG validation | Pass |
| Maintenance/runtime boundary | Graphify and ICM were authoring-only | Preserved explicitly | Pass |
| Competing catalogs | MIT 6.172 and trading performance overlapped at discovery | Added mutual exclusions to both frontmatter descriptions | Pass |
| Delegation | Conditional, bounded worker contracts | Preserved; no worker-per-module rule | Pass |

The cold-start rule is now:

```text
SKILL.md
    → zero, one, or two decision-owning references for the current phase
    → sequential phase or bounded subagent only when a third independent decision is real
```

The audit does not prove behavior under every prompt. It is backed by 20 authored activation/routing cases, deterministic link/package checks, live routing and safety trials, and independent council review. Native skill-discovery and real-system latency tests remain separate empirical obligations.
