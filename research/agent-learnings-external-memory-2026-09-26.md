# Does an `AGENT_LEARNINGS.md` improve an agent?

Research date: 2026-09-26

## Verdict

**Yes, a persistent learning file can help, but not safely in the literal form “append every mistake and read the whole file before every task.”** The evidence supports a small, curated, test-backed memory that records reusable corrections. It does not support treating every self-diagnosed mistake as a permanent instruction.

The recommended decision for Ingenius is:

- **Adopt the pattern as a controlled Markdown pilot.** Keep `AGENT_LEARNINGS.md` short, versioned, scoped, and limited to verified active lessons.
- **Do not use it as a chronological diary.** Put unverified observations in quarantine, merge duplicates, supersede obsolete rules, and archive history outside the always-loaded file.
- **Retrieve by task relevance once the collection grows.** Reading a small index is reasonable; reading an unlimited history is not.
- **Do not adopt Hindsight yet.** The current repository is small enough for Markdown, Git history, and regression tests. Reconsider a memory service when several agents, projects, or users need selective semantic and temporal retrieval over hundreds of records.

This is external memory scaffolding: it changes the context supplied at inference time. It does **not** retrain the model or update its weights.

## What the evidence actually shows

| Evidence | Tested mechanism | Result relevant to this proposal | Important limitation |
|---|---|---|---|
| [Reflexion](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html) | Evaluator-grounded verbal reflections kept in a small episodic buffer for retries | Strong gains on several interactive, reasoning, and coding benchmarks show that evaluated failure feedback can improve later attempts | Mostly same-problem retries with a bounded buffer, not a durable cross-project file; at least one programming result did not beat the cited GPT-4 baseline |
| [Self-Refine](https://proceedings.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html) | A model critiques and revises its own current output | About 20 percentage points average improvement across the paper's seven tasks supports iterative feedback | No cross-session persistence or evidence that a self-written long-term rule remains correct |
| [Voyager](https://arxiv.org/abs/2305.16291) | A persistent library of executable skills, environment feedback, automatic curriculum, and self-verification | Reusing verified procedural artifacts helped the agent acquire capabilities and transfer them to a new world | The memory was a library of tested code, not raw prose about every mistake; the headline result belongs to the composite system |
| [Generative Agents](https://arxiv.org/abs/2304.03442) | Retrieval from a natural-language memory stream plus higher-level reflection and planning | Ablations support the value of reflection and retrieval for believable longitudinal behavior | The outcome was perceived believability, not coding correctness or avoidance of repeated failures |
| [MemGPT](https://arxiv.org/abs/2310.08560) | LLM-managed working context plus archival storage and retrieval | Large improvements on deep-memory retrieval support tiered external memory | The experiment concerns fact recall, not learning procedural corrections from mistakes |
| [ExpeL](https://arxiv.org/abs/2308.10144) | Curated natural-language insights built from success/failure comparisons, plus retrieval of useful prior trajectories | This is the closest analogue: it improved HotPotQA from 28% to 39%, ALFWorld from 40% to 59%, and cross-task transfer from 63% to 70% in reported experiments | The system used add/edit/upvote/downvote curation and retrieval. Adding raw reflections reduced the reported HotPotQA result to 29%, far below the curated system's 39% |
| [LongMemEval](https://arxiv.org/abs/2410.10813) | Long-term conversational retrieval, temporal reasoning, updates, and abstention | Better indexing and time-aware retrieval improved recall and QA | Long histories still produced major degradation; memory quality depends on retrieval and reading policy |
| [MemoryAgentBench](https://arxiv.org/abs/2507.05257) | Retrieval, test-time learning, long-range understanding, and selective forgetting | Its broad evaluation makes clear that storage alone is not equivalent to learning or safe forgetting | A recent preprint, and not a direct test of Markdown mistake logs |
| [Xiong et al.](https://arxiv.org/abs/2505.16067) | Controlled addition and deletion of execution experiences | Selective addition plus deletion averaged a 10-point gain over naive memory growth; add-all policies could flatten or degrade | Structured execution records, not a Markdown file, but directly relevant to the danger of retaining everything |

The evidence therefore supports five conclusions:

1. External context can preserve useful information across attempts and sessions.
2. Failure-derived lessons can transfer when they are grounded in an objective outcome and generalized carefully.
3. Verification, selection, retrieval, deduplication, and forgetting are part of the learning mechanism, not optional housekeeping.
4. Executable tests and successful counterexamples are stronger memory than an agent's unsupported explanation of why it failed.
5. The exact `AGENT_LEARNINGS.md` proposal has not received a direct controlled test. It is a plausible implementation hypothesis, not an established scientific result.

## Why the naive version fails

### Self-diagnosis is not a reliable verifier

[Research on intrinsic self-correction](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html) found that models can make reasoning worse when asked to correct themselves without reliable external feedback. A broader [TACL survey](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes) reaches the same practical conclusion: self-correction is most dependable when an external signal identifies what is wrong.

A failed test, compiler error, numerical oracle, reviewed source, or explicit user correction may justify a candidate lesson. The model merely feeling uncertain does not.

### More context is not automatically better

[Lost in the Middle](https://doi.org/10.48550/arXiv.2307.03172) shows that models can use long context unevenly, especially when relevant information is buried. OpenAI's [agent memory guidance](https://developers.openai.com/api/docs/guides/agents/sandboxes) uses progressive disclosure: load a short memory summary first, search the larger memory only when needed, and open detailed rollout summaries selectively.

An unlimited always-read file adds token cost, hides relevant rules among irrelevant ones, and increases the chance that an obsolete instruction wins attention.

### Persistence amplifies both truth and error

A useful correction prevents recurrence. A false correction can repeatedly cause new failures. A broad rule learned from one repository can be harmful in another. A correct rule can become stale after a tool, dependency, or policy changes.

Production systems therefore add controls. GitHub Copilot Memory validates stored memories against the current branch and expires unused entries; its [official documentation](https://docs.github.com/en/copilot/concepts/agents/copilot-memory) also exposes review and deletion. Anthropic's [long-running agent harness](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) combines a progress file with Git history and executable tests. OpenAI's [harness engineering report](https://openai.com/index/harness-engineering/) recommends a short `AGENTS.md` as a map into a structured, versioned documentation system rather than one giant instruction file.

### A writable memory is a security boundary

Untrusted repository text, web pages, tool output, and retrieved documents must not be able to promote themselves into permanent instructions. The [OWASP AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) recommends sanitization, isolation, size and retention limits, integrity checks, and audits for memory. OpenAI's [agent safety guidance](https://developers.openai.com/api/docs/guides/agent-builder-safety) likewise treats untrusted text as data rather than privileged instructions.

## Recommended Ingenius design

Separate capture from promotion:

```text
AGENTS.md                         stable repository policy and memory workflow
AGENT_LEARNINGS.md                short index of active, verified lessons
memory/
├── candidates/                   quarantined proposed lessons
├── topics/                       detailed evidence loaded on demand
└── archive/                      superseded, expired, and rejected records
evaluations/memory/               regression cases and experiment results
```

`AGENT_LEARNINGS.md` should be a catalog, not the full evidence store. A task begins by reading its small active index. The agent then opens only the topic records relevant to the task. For a very small corpus, searching by explicit tags is enough; semantic retrieval should be added only when scale justifies it.

### Record schema

Each promoted lesson should answer when it applies, how it was verified, and when it must be reviewed:

```yaml
id: testing.redis-required
status: active
scope: tests/integration/**
trigger: running the repository integration suite
observed_failure: tests failed because no Redis service was available
root_cause: the suite depends on a local Redis instance
correction: start the repository-pinned Redis service before the suite
exceptions: unit tests and mocked integration tests do not require Redis
evidence: CI configuration plus reproduced failing and passing runs
confidence: verified
created_at: 2026-09-26
last_verified: 2026-09-26
review_after: 2026-12-26
supersedes: null
```

Avoid vague lessons such as “be more careful,” “always use Redis,” or “never trust the tests.” They do not provide a reproducible trigger, correction, or boundary.

### Promotion workflow

1. **Detect:** an external verifier establishes that an outcome is wrong.
2. **Quarantine:** write a candidate with evidence; do not make it an active instruction yet.
3. **Diagnose:** reproduce the failure and identify the root cause. Compare against a successful run when possible.
4. **Generalize narrowly:** state the applicability conditions, exception cases, and forbidden overgeneralization.
5. **Test:** add or identify a regression test that distinguishes the correction from the failed behavior.
6. **Promote:** a trusted reviewer or deterministic policy moves the record into the active index.
7. **Retrieve:** future tasks load active records that match the current scope; they do not ingest the full historical diary.
8. **Maintain:** merge duplicates, replace contradictions at their source, and expire or archive stale lessons.

Only the active layer may influence routine tasks automatically. Candidate and archived text remains untrusted evidence until explicitly inspected.

### Governance rules

- Never store secrets, credentials, private user data, raw confidential transcripts, or hidden evaluation answers.
- Isolate memory by repository, user, and environment. A local convention must not silently become a global rule.
- Record provenance and the exact validating artifact.
- Use Git review, named ownership, diffs, and rollback for promoted entries.
- Give deterministic permission and safety controls higher precedence than prose memory.
- Serialize compaction and use version checks for concurrent updates.
- Log which entries were read and whether they helped, were ignored, or caused harm.

## Controlled experiment

The architecture should earn adoption through an experiment, not through an agent council vote.

### Four arms

| Arm | Before a task | After a verified mistake |
|---|---|---|
| No persistent memory | Start fresh | Produce a postmortem, then discard it |
| Raw append-only Markdown | Read the complete chronological file | Append the unedited mistake and proposed correction |
| Curated structured Markdown | Read the complete active structured file | Validate, scope, deduplicate, merge, or supersede the record |
| Curated plus retrieval | Retrieve a fixed top-*k* set from the same structured corpus | Apply the same curation policy, then update the index |

Randomize persistent agent lineages, not individual turns, because a memory treatment creates carryover. First run a content-controlled phase in which every arm receives the same validated seed mistakes. Then run an end-to-end phase in which each arm uses its own real write policy.

Keep model version, prompt, tools, retry budget, initial repository snapshot, task order, verifier, and compute budget fixed. Keep each lineage's files, cache, memory, and credentials isolated. Do not store future task text, hidden tests, or complete solutions in memory.

### Probe set

For every seeded mistake, test:

1. an exact recurrence;
2. a differently worded instance with the same causal structure;
3. transfer to another repository or tool;
4. a near-miss where the old lesson is tempting but inapplicable;
5. an explicit exception to the rule;
6. a version or policy change that makes the rule stale; and
7. a delayed recurrence after many unrelated records accumulate.

### Measurements

The primary measure is the fraction of applicable probes that repeat the same root-cause error. Also record:

- first-attempt success by task and probe family;
- false-memory harm on near-misses and irrelevant tasks;
- obsolete-rule violations and time to recover after a rule changes;
- relevant-record retrieval precision and missed-memory rate;
- input tokens, output tokens, embedding/reranking cost, and curation cost;
- median and p95 wall-clock latency;
- memory size and performance as the log grows; and
- severity-weighted unsafe actions, tested only in disposable environments.

For the cleanest harm estimate, snapshot a lineage before a negative-control task and run a non-updating shadow replay with memory hidden. A memory-induced harm is a case where the enabled run fails, the shadow run passes, and the trace supports the memory as the cause.

Pre-register practical thresholds for worthwhile repeat-error reduction, allowed overall-performance regression, false-memory harm, stale-rule burden, latency, and cost. Adopt the least expensive arm that beats the no-memory control, transfers beyond exact repeats, remains noninferior overall, and stays inside every harm and cost boundary.

## Hindsight fit assessment

[Hindsight](https://github.com/vectorize-io/hindsight) provides retained memories, selective recall, reflection, provenance, observations, and higher-level mental models. Those capabilities become valuable when memory is large, longitudinal, shared, and difficult to manage as files.

For the current Ingenius use case, the fit score is **6/20: skip for now**.

| Rubric dimension | Score | Reason |
|---|---:|---|
| Durable continuity | 3/4 | Learning across agent sessions is a stated goal |
| Memory transformation | 3/4 | Mistakes must be converted into scoped, revised, evidence-backed lessons |
| Retrieval/context pressure | 1/3 | The useful corpus is currently small |
| Provenance/reasoning | 2/3 | Derived rules should link to failures and tests |
| Integration fit | 0/2 | The repository has no existing memory-service insertion point |
| Operational readiness | 0/2 | No database, embedding, queue, or memory-service operations are needed today |
| Governance value | 1/2 | Isolation, review, retention, and deletion help |
| Small editable list penalty | -2 | Markdown plus Git is presently sufficient |
| Low-volume penalty | -2 | Current scale does not justify another service |
| **Total** | **6/20** | **Use the simpler controlled file design first** |

Reconsider Hindsight or another searchable memory service when one or more of these triggers occur:

- hundreds of active records make file scanning inaccurate or expensive;
- several agents or users need isolated but selectively shared memory;
- temporal changes and contradictions require systematic reconciliation;
- provenance must be traced across summaries, observations, and source events; or
- measured retrieval failures remain high after the Markdown design is indexed and pruned.

At that point, pilot one isolated project bank. Measure retrieval precision, missed-memory rate, correction rate, provenance usefulness, latency, model/embedding/storage cost, and deletion behavior before migrating the source of truth.

## Final conclusion

The statement “an agent improves over time by recording and rereading mistakes” is directionally right but incomplete. The dependable loop is:

```text
verified failure
    → narrow causal lesson
    → regression test
    → reviewed promotion
    → relevant retrieval
    → measured reuse
    → correction, expiry, or deletion
```

That design can reduce repeated mistakes without retraining. A raw append-only diary has no comparable validation and creates predictable risks: self-reinforced error, stale rules, context bloat, cross-project leakage, and memory poisoning. Serious systems are likely to need some form of durable state when work spans sessions, but they do not all need one universal learning file, and one-shot agents may need no durable memory at all.
