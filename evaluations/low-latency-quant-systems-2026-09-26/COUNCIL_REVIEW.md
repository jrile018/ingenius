# Agentic council review

Date: 2026-09-26

Three independent roles reviewed the package: source grounding, behavior/packaging, and ICM architecture. They were asked to report failures rather than reach consensus.

## Findings and corrections

| Reviewer | Initial result | Material finding | Correction | Final status |
|---|---|---|---|---|
| Source grounding | Pass | Traceability is module-level; AF_XDP has no dedicated dossier; some placement rules are derived heuristics | Kept claims narrow, version-pinned where available, and explicitly hypothesis-only | Pass with non-blocking traceability improvements |
| ICM architecture | Fail | Some cases loaded three references; global gates had several homes; MIT 6.172 overlapped at discovery; ICM evidence was not durable | Parent owns ordinary gates; phases cap at two references; both skills name their mutual boundary; DAG and ICM audit added | Pass |
| Behavior and packaging | Fail | Authored cases assumed bottlenecks; structural verifier was mislabeled as behavioral; coverage and live evidence were missing | Split initial and conditional routes; expanded to 20 cases; added safety/composition/dual-skill cases; ran live blind routing, safety, and delegation trials | Pass after two final premature routes were corrected |

## Accepted non-blockers

- The source map groups evidence by module rather than attaching a citation to every sentence. Future audits can improve rule-level traceability.
- AF_XDP is currently a routing keyword, not the basis of a concrete implementation claim. Add an official AF_XDP dossier before expanding its guidance.
- Catalog-level CPU/GPU/FPGA material is used only to generate candidates; target measurements decide.
- Graphify community cohesion is intentionally low in broad evidence families; runtime modules are narrower than corpus communities.
- The live delegation trial establishes isolation and safety, not lower token use or higher accuracy.

## Decision rule

The final behavior reviewer confirmed that the corrected cases no longer preselect unsupported bottlenecks, the live trials are reported as observed but bounded evidence, and the deterministic verifier passes. The council's final result is **pass with the non-blocking traceability improvements above**.
