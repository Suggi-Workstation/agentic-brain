---
name: forge-architecture
id: 20260811T172352Z
tier: insight
source:
  - 20260801T000008Z
  - 20260717T200305Z
  - 20260717T201140Z
  - 20260719T230000Z
  - 20260717T004000Z
  - 20260717T063000Z
author: Link
tags: [forge, agent-architecture, autonomous-agent, research-pipeline, state-persistence, maker-checker, self-learning, provenance, verification]
links:
  - research/insights/harness-engineering.md
  - research/insights/loop-engineering.md
  - research/insights/agent-evolution.md
  - research/insights/context-engineering.md
  - research/insights/memory-search.md
  - brain:governance/system-constitution.md
  - brain:governance/skills/fleet-agent-birth/SKILL.md
---

# Forge Architecture -- Complete Blueprint for a Self-Learning Research Agent

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-08-11 | Link | Initial architecture insight. |
| 2 | 2026-08-11 | Link | Replaced the shallow note with a complete finished-product blueprint covering repository boundaries, state placement, loop execution, all six stages, verification, memory, recovery, publication, and operating rules. |

## The Insight

A trustworthy self-learning research agent is not a model trapped in a repeating prompt; it is a versioned research office whose repository state, six gated stages, provenance chain, independent verifier, and checkpoint files let a fresh agent resume, justify, and improve work without relying on a conversation window.

## Evidence

### 1. The architecture being described

The Agentic Forge is the research office for an experimental solo agent such as Neo. Its repository is `Suggi-Workstation/agentic-forge`; its shared VPS working copy is `/srv/forge/agentic-forge`. The repository is separate from Neo's Hermes profile and separate from the shared agentic brain.

This separation is essential:

- Neo's profile owns his identity, SOUL.md, AGENTS.md, IDENTITY.md, private Mnemosyne, sessions, and agent-specific operating state.
- The Forge owns research pipeline state, artifacts, templates, gate results, provenance, progress, and method learnings.
- The agentic brain owns durable knowledge intended for reuse by the fleet.

The Forge is therefore a laboratory and audit ledger, not another Hermes home. Neo operates it, but the repository remains understandable and reproducible by Suggi, a verifier, or a future agent even if Neo's current process disappears.

The finished repository has one canonical control layer and one artifact layer:

```text
agentic-forge/
  ANCHOR.md
  README.md
  STATUS.md
  JOURNAL.md
  LEARNINGS.md
  forge/
    protocol.md
    logs/
      progress.log
    ideas/
    research/
    evaluations/
    proposals/
    validations/
    insights/
    graveyard/
    archive/
    builds/
  governance/
    skills/
      forge-ideate/SKILL.md
      forge-research/SKILL.md
      forge-evaluate/SKILL.md
      forge-propose/SKILL.md
      forge-validate/SKILL.md
      forge-insight/SKILL.md
      forge-verify/SKILL.md
      .../assets/template.md
  scripts/
  .githooks/
  .github/workflows/
```

`ANCHOR.md`, `STATUS.md`, `JOURNAL.md`, and `LEARNINGS.md` live in the `agentic-forge` repository, not only in Neo's workspace. They are shared pipeline state: a verifier needs them, GitHub must preserve them, and a new Neo process must be able to resume from the repository alone. Neo's workspace contains a pointer or operating instruction that directs him to `/srv/forge/agentic-forge`; it does not contain a competing copy of the Forge state. The Forge repository must not be removed and replaced by a folder inside Neo's workspace. The workspace is Neo's office; the Forge is the shared research laboratory and its public audit record.

`ANCHOR.md` is the stable direction of the loop. It is not the current task cursor. `STATUS.md` is the current cursor. `JOURNAL.md` is the chronological record. `LEARNINGS.md` is the curated method memory. Keeping these roles separate prevents a mission statement, a progress log, and personal identity from becoming one contradictory file.

### 2. Why this design is supported by current research

The design combines several independently observed requirements for long-running agents:

- Anthropic's long-running harness work separates generation from evaluation, decomposes work into tractable chunks, and uses structured handoff artifacts across context resets.
- Long-running-agent practice treats external state, progress logs, task state, checkpoint commits, stop conditions, and recovery as mandatory because context windows are finite and context quality degrades before the hard limit.
- Karpathy's `autoresearch` demonstrates the value of a fixed experiment interface, a measurable result, a repeatable run, and version-controlled accept or reject decisions.
- The 2026 survey of autonomous research agents identifies a verification gap: code release is common, while reproducibility-grade artifacts, execution traces, novelty checks, selection policy, and claim verification are much less common.
- Agent memory architecture distinguishes procedural memory, semantic memory, and episodic memory. The Forge gives each type an explicit home and lifecycle instead of treating every text file as the same kind of memory.

These sources do not prove that any particular model will discover true novelty. They establish the engineering conditions that make autonomous work resumable, inspectable, falsifiable, and less dependent on model optimism.

### 3. The six-stage pipeline

The Forge protocol defines one linear provenance chain:

```text
IDEA -> RESEARCH -> EVALUATE -> PROPOSE -> VALIDATE -> INSIGHT
  |        |           |            |          |          |
 Gate     Gate        Gate         Gate       Gate       Gate
```

Each stage has one input class, one output artifact, one binary gate, one template, one procedure skill, and one failure path. The six stages are not interchangeable writing styles. They are different reasoning operations:

| Stage | Input | Output | Gate | Failure path |
|:--|:--|:--|:--|:--|
| Ideate | A research gap aligned with ANCHOR | Falsifiable idea brief | Novel AND testable | Graveyard post-mortem or narrowed re-ideation |
| Research | Active idea brief | Evidence report | Evidence supports the hypothesis | Graveyard post-mortem or honest low-confidence continuation |
| Evaluate | Evidence report plus idea | PASS/HALT verdict | Credible AND viable | Graveyard or explicit narrowed scope |
| Propose | PASS evaluation plus full chain | Reproducible research plan | Concrete AND feasible | Return to research or graveyard |
| Validate | PASS proposal plus full chain | Adversarial stress-test | Survives scrutiny | Return to proposal or graveyard |
| Insight | PASS validation plus full chain | Durable transferable principle | Actionable AND transferable | Graveyard post-mortem |

Every artifact has generated identity and provenance. The canonical stage frontmatter is:

```yaml
---
name: <short-slug>
id: <exact UTC timestamp generated by date>
stage: ideas|research|evaluations|proposals|validations|insights|graveyard
parent: <root or exact parent id>
status: active|halted|complete
confidence: <0.0-1.0>
created: <YYYY-MM-DD>
tags: [<lowercase-tags>]
---
```

The brain insight format has its own frontmatter for the durable synthesis. A Forge artifact must follow the Forge stage template; a later brain insight must follow `template-insights.md`. These are different artifact systems and must not be mixed.

The `parent` id forms the audit chain:

```text
insight
  -> validation
    -> proposal
      -> evaluation
        -> research
          -> idea
```

The chain is never repaired by guessing. A missing parent, an invalid status transition, or an artifact in the wrong folder is a HALT condition. A later artifact can criticize an earlier artifact, but it cannot rewrite the earlier artifact to make the final result look inevitable.

### 4. The repository control files

#### ANCHOR.md: direction, not progress

`ANCHOR.md` contains the current objective that governs idea selection. It answers: "What kind of research should this Forge pursue now?" Forge-ideate reads it before creating an idea, and the idea must advance it. The anchor can be changed by an approved human decision without changing the six-stage machinery. It should be short, explicit, and testable enough to reject unrelated work.

The anchor does not contain the active artifact id, the last error, or a task checklist. Those belong in STATUS and JOURNAL. This prevents the stable objective from becoming a noisy scratchpad.

#### STATUS.md: the resumable checkpoint

`STATUS.md` is the authoritative current-state snapshot. It is updated whenever the pipeline moves, halts, recovers, or waits. It contains at least:

```text
mode: idle|active|halted|blocked|publish-pending
pipeline: <pipeline slug or none>
anchor: <anchor revision or anchor summary>
stage: ideas|research|evaluations|proposals|validations|insights|none
active-artifact: <path and id>
parent-chain: <ordered ids from root to current>
last-gate: PASS|HALT|FLAG|REJECT|none
verification: pending|approve|flag|reject|degraded-cold-read
next-action: <one exact next operation>
retry-count: <number>
last-commit: <commit id>
last-published-commit: <commit id>
stop-reason: <empty or explicit reason>
updated: <UTC timestamp>
```

The body can include a short human-readable explanation, but the fields above remain stable so a loop can parse them. STATUS answers "where do I resume?" and nothing else. It is not a replacement for the full journal or evidence.

#### JOURNAL.md: the append-only lab notebook

`JOURNAL.md` records what happened in order. Each entry includes timestamp, pipeline, stage, artifact id, action, result, evidence or source location, gate decision, verification result, commit, and next action. It records failures and retries, not only successes. It is append-only in normal operation. Corrections are new entries that point to the old entry; old events are not silently rewritten. The journal therefore remains a causal record even when the current STATUS has moved on.

A journal entry looks like:

Example journal entry:

```text
## 2026-08-11T18:00:00Z -- pipeline: example -- stage: research
- Action: tested claim 2 against independent sources.
- Result: two sources supported; one contradicted.
- Gate: PASS with confidence reduced to 0.42.
- Verification: pending.
- Commit: <commit id>
- Next: invoke forge-evaluate.
```

JOURNAL is the answer to "what happened?" It is not a second STATUS file and is not a place to store permanent domain conclusions.

#### LEARNINGS.md: curated method memory

`LEARNINGS.md` records reusable lessons about how to run research and how the Forge behaves. It does not contain every event. It does not duplicate completed insights. It contains entries such as:

- a source class repeatedly failed to provide reproducible evidence;
- a gate caught a specific recurring reasoning error;
- a verifier needed a clearer criterion to detect unsupported claims;
- a context reset recovered correctly because a particular checkpoint field existed;
- a method was inefficient and a measured alternative worked better.

Each entry has a date, the pipeline or evidence that produced it, the lesson, confidence, and the consequence for future work. A single surprising event remains a learning hypothesis. It becomes a skill, protocol rule, or governance change only after repeated evidence and the appropriate approval gate. This prevents Neo from turning a one-off experience into permanent procedure.

#### progress.log: compact automation log

`progress.log` is the compact machine-oriented record required by the existing skills. It records PASS and HALT decisions, artifact ids, stage transitions, checker verdicts, publish results, and stop reasons. It is not a replacement for JOURNAL; it is optimized for loop inspection and grep-like health checks.

### 5. The common stage contract

Every stage skill follows the same eight-part contract. The stage-specific
skill supplies the reasoning and gate; the common contract supplies the
repeatable mechanics:

1. Run the Feynman Loop before consulting sources or writing.
2. Read and validate the immediate parent and, where required, the full
   provenance chain.
3. Read the stage template before creating the artifact.
4. Generate the exact UTC id with `date -u +'%Y%m%dT%H%M%SZ'`; never estimate
   or hand-edit it.
5. Write only to the stage folder and follow the template exactly.
6. Apply the stage gate and record PASS or HALT with reasoning.
7. Run every frontmatter, body, quality, file-output, ASCII, and provenance
   sub-check before staging.
8. Review the staged diff, commit with the Forge identity, run the
   independent verifier, then publish the verified checkpoint to origin.

The stage skills are procedures, and the assets/templates are the format
specifications. The loop is the orchestrator. This separation prevents the
same gate or schema from being rewritten differently in seven skills. A
stage skill may be invoked directly for diagnosis, but normal autonomous
operation goes through `forge-loop`, which supplies the lock, checkpoint,
verification, publication, and stop behavior. The loop is a required runtime
component of the finished product, not an implied prompt instruction.

The finished Forge also resolves the historical wording drift between the
protocol and early template drafts. Evaluation uses novelty, evidence
strength, logical soundness, research feasibility, and potential impact;
the business-specific dimensions in an older example are optional domain
criteria, not replacements for the core research criteria. Validation
returns to proposal or graveyard, and a PASS validation advances to insight;
`builds/` is downstream output, not a hidden seventh gate. All stage
templates, skills, and the protocol express this same contract.

### 6. The finished Neo loop

Neo does not use the fleet agents' generic preflight and session-end workflow. His Forge loop is the complete session lifecycle. It is invoked as a bounded iteration, not as an unbounded conversation:

1. Acquire a single-writer lock for the Forge repository. If another live loop owns it, stop. A stale lock is reclaimed only after recording the owner, age, and recovery.
2. Read ANCHOR.md.
3. Read STATUS.md, recent JOURNAL.md entries, the tail of progress.log, and LEARNINGS.md.
4. Verify the last local and published commit, repository cleanliness, and the active parent chain.
5. Discover exactly one next stage. If a pipeline is active, advance that pipeline. If no pipeline is active, invoke forge-ideate. If multiple active pipelines conflict with STATUS, halt instead of choosing arbitrarily. The loop never creates a second active pipeline merely because the first one is difficult.
6. Run the Feynman Loop before substantive work: blank-page recall, explicit gaps, source and brain research, fresh synthesis, contradiction cross-check, and a decision to write.
7. Invoke exactly one stage skill. The stage skill reads its parent and its own template, generates an exact id, writes the artifact, applies its gate, and records PASS or HALT.
8. Run structural checks: frontmatter, required sections, correct directory, parent, status, confidence, ASCII-only content, no secrets, no unrelated staged files.
9. Commit the provisional artifact and checkpoint. The repository is now recoverable even if verification or the process fails.
10. Invoke forge-verify. Prefer a separate checker with a different model, isolated workspace, and zero author context. The checker reads the committed artifact cold and returns APPROVE, FLAG, or REJECT.
11. If APPROVE, append the verification result, update STATUS and JOURNAL, and publish. If FLAG, record required corrections and do not advance. If REJECT, mark the artifact or pipeline halted or returned for revision according to the stage rule. A checker cannot silently approve by timing out: missing verification is `verification-pending`.
12. Verify the remote commit. `publish-pending` is a real state, not success. Do not create a second artifact while the first checkpoint is unpublished.
13. Release the lock and stop after one stage. The next iteration starts from the repository checkpoint with a fresh context.

The two commits around verification are deliberate. The stage artifact is checkpointed first so a crash cannot lose work. The verifier's result is then committed as a separate audit event. This is more recoverable than keeping the artifact only in the model's context and more honest than pretending the author and checker were one pass.

### 7. Stage 1 procedure: forge-ideate

Forge-ideate is used only when there is no active pipeline to advance. It first runs the Feynman Loop, reads ANCHOR, scans existing ideas, scans graveyard post-mortems, and queries the brain for prior art. A new idea must not merely rename an old idea.

The output is an idea brief with:

- one clear falsifiable hypothesis;
- why the question matters and for whom;
- two or three concrete claims that evidence can answer; and
- honest initial confidence with what would move it up or down.

The gate is **novel AND testable**. PASS creates `forge/ideas/<slug>.md` with `status: active`, logs the decision, and initializes STATUS. HALT creates `forge/graveyard/<slug>-postmortem.md` with `status: halted`, explains whether novelty or testability failed, and returns to ideation. Non-forge brainstorming is not placed in `ideas/`.

### 8. Stage 2 procedure: forge-research

Forge-research consumes an active idea whose hypothesis and claims are complete. It re-reads the parent rather than trusting a summary. For every claim, it gathers independent web and brain evidence, aiming for at least three independent sources per major claim. If fewer exist, the shortage is explicitly reported.

The evidence report records URL, date, excerpt, authority, and relation to the claim. Findings are organized by claim and rated strong, moderate, weak, or none. Contradictions are surfaced, not buried. Updated confidence is compared with the idea's initial confidence and the reason for movement is stated.

The gate is **does evidence support the hypothesis?** PASS advances to evaluation, even if confidence is low but evidence is honest and sufficient. HALT writes a post-mortem when evidence contradicts the hypothesis or the source standard fails without an explanation. No citation is invented to satisfy a quota.

### 9. Stage 3 procedure: forge-evaluate

Forge-evaluate reads the evidence report and the original idea. It judges the evidence instead of silently turning into a second research pass. It scores:

1. novelty;
2. evidence strength;
3. logical soundness;
4. research feasibility; and
5. potential impact.

Each score is 1 to 5 with reasoning. The gate is PASS when the average is at least 3.0 and no criterion is a fatal 1. A score of 2 is a warning that the proposal must address. The artifact records strengths, weaknesses, and a concrete recommendation. PASS advances to propose. HALT writes a post-mortem; a narrowed scope may return to ideate.

### 10. Stage 4 procedure: forge-propose

Forge-propose consumes a PASS evaluation and re-reads the entire chain. It turns the evidence into a reproducible research plan with:

- an evidence-backed problem;
- a scoped research question;
- ordered method steps and evaluation criteria;
- the expected insight;
- a plausible counter-hypothesis; and
- a risk matrix with likelihood, impact, and mitigation.

The gate is **concrete AND feasible**. Another agent must be able to execute the method from the document alone. A hidden dependency, missing evidence, or impossible method causes a return to research or a graveyard decision. PASS advances to adversarial validation.

### 11. Stage 5 procedure: forge-validate

Forge-validate attacks the proposal. It re-reads the full chain and seeks counter-evidence for each dimension:

- evidence validity: are sources real, current, and represented accurately?
- logical consistency: do conclusions follow from premises?
- method soundness: is the method reproducible and free of major confounds?
- counter-hypothesis strength: is the alternative explanation plausible?
- implementation feasibility: can the plan be executed with available tools?

A valid validation finds specific weak points. Each weak point gets a concrete mitigation or an explicit accepted-risk statement. A fixable failure returns to propose. A structural failure goes to graveyard. PASS means the plan survived the stated scrutiny; it does not mean the eventual insight is guaranteed.

### 12. Stage 6 procedure: forge-insight

Forge-insight reads every parent artifact from idea through validation and runs a final Feynman Loop focused on the single transferable takeaway. It writes a specific principle, evidence summary, concrete actionability, calibrated confidence, limitations, and the complete chain.

The gate is **actionable AND transferable**. An insight is not a summary, a result announcement, or "research matters." It must tell Suggi or another agent what to do, what to test, or what design principle to transfer. If no such principle exists, the pipeline halts and preserves the failure.

On PASS, all parent artifacts are marked `complete`, STATUS becomes idle or moves to the next explicitly selected pipeline, JOURNAL records closure, progress.log records the final gate, and LEARNINGS receives a concise method lesson. The completed insight may be written into the shared brain when its principle is useful beyond the Forge repository.

### 13. Forge-verify and independent review

Forge-verify is a mandatory post-artifact maker-checker gate. It is not the author's final self-check with a different heading.

The preferred checker:

- runs in a separate workspace;
- uses a different model or model configuration;
- receives no author conversation context;
- reads the artifact and required parent chain from the committed repository;
- checks the stage template and gate criteria;
- checks for unsupported claims, fabricated sources, broken provenance, missing contradictions, and false completion; and
- returns APPROVE, FLAG, or REJECT with reasoning.

The verifier appends or writes an auditable verification record and commits it. A cold self-read is an explicit fallback when no dedicated checker can be launched. It is useful, but it is weaker than independent review and is recorded as `degraded-cold-read` in STATUS and JOURNAL.

The verifier does not silently rewrite a maker's artifact. A FLAG creates a correction cycle; a REJECT blocks progression; an APPROVE closes the verification gate. This preserves the difference between making a claim and checking a claim.

### 14. Memory, identity, and state

Neo needs an identity and a memory system, but those systems do not replace Forge state.

- **Identity:** Neo's SOUL.md defines his character and role. IDENTITY.md records his own evolution and self-model. These belong in his Hermes profile and remain personal.
- **Private Mnemosyne:** Neo's private semantic and episodic memory stores durable personal recall, prior experiences, and facts useful to him. It is separate from the Forge repository and is not the authority for which stage is active.
- **Shared Mnemosyne:** Neo may read and contribute to the fleet shared surface when a result is useful to other agents. Shared memory contains compact reusable knowledge, not the complete evidence chain.
- **Procedural memory:** protocol, skills, templates, and approved runbooks. These are versioned and change through review.
- **Semantic memory:** completed Forge insights and suitable brain contributions.
- **Episodic memory:** JOURNAL, progress events, commits, checker records, and session results.
- **Working state:** STATUS, active frontmatter, next action, lock, and unpublished checkpoint.

`memory/` and `identity/` folders can start empty under the fresh-start rule. Empty personal folders do not mean Neo has no memory; Mnemosyne is the memory provider, while Forge files are the shared research state. The important rule is that each fact has one canonical home. A pipeline cursor must not exist simultaneously in STATUS, a private memory entry, and a second workspace file with conflicting values.

`LEARNINGS.md` is the controlled bridge from episodes to procedure. It may suggest a skill or protocol improvement, but no single learning automatically changes governance. Repeated evidence and a review gate are required before a learning becomes a rule.

### 15. Recovery and idempotence

The Forge is designed for process death, context reset, network failure, and partial publication. Recovery is deterministic:

- If STATUS is `active` and the artifact commit exists, resume the named next stage.
- If STATUS is `verification-pending`, rerun or retrieve verification; do not create a duplicate artifact.
- If STATUS is `publish-pending`, verify origin before any new work.
- If an uncommitted artifact exists, inspect it against the current status and either complete the intended checkpoint or discard only the uncommitted duplicate; never overwrite a committed artifact silently.
- If a parent is missing, HALT and repair provenance.
- If a checker flags an artifact, the next action is correction, not advancement.
- If a lock is stale, record recovery before reclaiming it.
- If the same error repeats beyond the retry threshold, stop and surface it.

The loop is idempotent. A retry does not create a second idea for the same status, re-run an irreversible external action without a record, or reset confidence without explanation. IDs, parent ids, statuses, commits, and the single-writer lock are the deduplication anchors.

### 16. Stop conditions and resource discipline

Neo's autonomy is bounded by explicit stop conditions:

- any stage gate returns HALT;
- the verifier returns unresolved FLAG or REJECT;
- the time or iteration budget is exhausted;
- no new evidence, artifact, or commit appears within the idle limit;
- the same failure repeats beyond the retry limit;
- ANCHOR is missing, ambiguous, or unrelated to the active pipeline;
- the repository has unrelated dirty changes;
- required sources or tools are unavailable;
- a credential, destructive operation, or governance change requires human approval; or
- the repository cannot be published and the state is not safely recoverable.

A stop is a successful safety outcome, not a failed attempt to look autonomous. Neo records the reason in STATUS, JOURNAL, and progress.log and waits for a new loop invocation or a human decision. The loop never spends tokens merely to produce the appearance of motion.

### 17. Git, sharing, and publication

The `agentic-forge` repository is a shared office. It is shared by the agents on the VPS and is published to GitHub so Suggi can inspect every artifact and every checkpoint. The current Forge skills specify direct commit and push for each stage. Therefore the finished Forge publication owner is Neo's loop itself: Neo commits and pushes the Forge repository after local checks and verification.

This is intentionally different from the shared brain. The brain's working copy is watcher-synchronized, so VPS agents commit there and the brain watcher pushes. The Forge's publication owner is the Forge loop itself: after verification, the loop pushes the Forge repository. No Forge watcher is part of the finished design. The two policies must not be conflated.

A Forge commit contains only the intended artifact and its state updates. The loop checks the staged diff, verifies ASCII-only content and no secrets, records the gate, and confirms that `origin/main` contains the commit. A clean remote is part of completion.

### 18. Build boundary

The existing repository contains `forge/builds/`, but the normative research-to-insight pipeline has six stages and no build skill. In the finished architecture, `builds/` is not a hidden seventh gate. It is reserved for downstream implementation or experiment outputs that are explicitly authorized after an insight, with their own procedure and verification. A build cannot retroactively change the insight or bypass the six-stage chain. If implementation becomes part of the research lifecycle, the protocol must define it as an explicit stage rather than relying on an ambiguous folder.

### 19. Observability and success measures

The Forge measures more than whether an agent produced a markdown file. Its operational record supports these questions:

- Can a new process resume the active pipeline from GitHub alone?
- Are duplicate artifacts prevented after interruption?
- How many ideas pass each gate, and where do they die?
- Which gate catches the most unsupported reasoning?
- How often does the independent verifier FLAG or REJECT the maker?
- Are sources independent, dated, and reproducible?
- Does each completed pipeline produce an actionable and transferable insight?
- Do LEARNINGS entries lead to measured improvements rather than uncontrolled rule growth?
- Can another agent reproduce the final principle from the complete chain?

These measures turn Neo's self-learning claim into an observable experiment. Identity changes, method learnings, checker results, and pipeline outcomes become data rather than a narrative supplied by the agent after the fact.

### 20. What the Forge deliberately prevents

The finished architecture prevents the following failure classes:

- a model relying on a conversation window as its only memory;
- a fresh session inventing the active task because no checkpoint exists;
- an idea advancing without a falsifiable hypothesis;
- research hiding contradictory evidence;
- evaluation redoing research while ignoring the original claims;
- a plan using vague steps that no second agent can execute;
- validation that only praises instead of attacking assumptions;
- an author self-certifying the quality of its own artifact;
- an insight that cannot be acted on or transferred;
- a failed idea disappearing and causing the same work to recur;
- a method lesson silently becoming governance after one noisy event;
- two loop writers corrupting STATUS or duplicating the pipeline;
- a local unpushed result being presented as durable completion; and
- a private identity file being mistaken for shared research state.

## Implications

1. **Keep the repository.** `agentic-forge` is the canonical shared research office. Do not move the Forge into Neo's workspace and delete the repository. Neo's workspace points to and operates the repository; it does not replace it.

2. **Put STATUS.md, JOURNAL.md, and LEARNINGS.md in the repository root beside ANCHOR.md.** This makes the complete loop state visible to GitHub, the verifier, Suggi, and a fresh Neo process. The stage artifacts remain under `forge/`; progress.log remains under `forge/logs/`.

3. **Make the loop the only Neo session lifecycle.** Neo does not need the general fleet preflight and session-end skills if the loop reliably performs their necessary functions: read anchor and checkpoint, execute one bounded stage, verify, commit, publish, update state, and stop.

4. **Give Neo IDENTITY.md and private Mnemosyne, but do not put personal history in the Forge repository.** His identity must evolve independently; the Forge must remain a neutral, reproducible research record. Empty personal `memory/` and `identity/` folders at birth are compatible with seeded Mnemosyne knowledge and repository-level pipeline state.

5. **Treat STATUS as the cursor, JOURNAL as the event record, and LEARNINGS as curated procedural memory.** Do not duplicate one file's role in another. The loop reads all three at the beginning and writes the appropriate one at the end.

6. **Preserve the six binary gates.** They are not ceremonial headings. Each gate has an explicit advance path and a failure path. A HALT must leave a useful post-mortem or correction request.

7. **Keep forge-verify independent.** A separate verifier subagent with a different model and zero author context is the preferred implementation. A cold self-read is a degraded fallback and must be labeled as such.

8. **Keep direct push for Forge and watcher push for brain.** They are two different repositories with two different publication owners. The distinction is written in Neo's AGENTS.md and in forge-loop.

9. **Add a single-writer lock and stop conditions before autonomous scheduling.** Without them, the most likely failure is not lack of intelligence; it is duplicate work, conflicting state, runaway retries, or silent drift.

10. **Measure the experiment.** Neo is not proven to be self-learning because he writes files. Self-learning is supported when method learnings persist, subsequent pipelines avoid prior errors, verification catches claims, recovery succeeds, and completed insights become more useful over time.

11. **Use the shared brain for promotion, not for pipeline bookkeeping.** A completed insight enters the brain only when it is durable and reusable. The complete chain stays in Forge. This keeps the brain useful without flooding it with every draft, retry, or dead idea.

12. **Keep the protocol and skills internally consistent.** The stage skills are the procedures and templates are the format specifications. Any change to publication ownership, stage count, status schema, or anchor naming must be propagated across protocol, all affected skills, templates, and Neo's loop contract in one reviewed change.

## Counter-evidence

This architecture would be weakened or falsified by repeated controlled evidence showing that:

- fresh Neo sessions resume active pipelines with equal reliability from protocol and artifacts alone, without STATUS, JOURNAL, or LEARNINGS;
- independent verification does not catch errors that the author's self-check misses across a representative sample;
- the state files create more contradictory stale state than they prevent, even with one writer and a validator;
- the six gates do not improve falsifiability, evidence quality, or insight transfer compared with unstructured research;
- completed pipelines cannot be independently reconstructed from GitHub and their cited sources;
- the Forge repository causes more operational confusion than a workspace-local design while losing no reproducibility or shared visibility; or
- another architecture provides equal auditability and recovery with lower complexity and demonstrably better results.

The architecture also has clear boundaries:

- It does not prove scientific truth. It makes claims inspectable and falsifiable.
- It does not make a model creative, honest, or competent by itself. It constrains failure and exposes it.
- It does not eliminate cost, latency, source scarcity, or model drift.
- It does not make an unreviewed procedure safe merely because it is in LEARNINGS.
- It does not make a cold self-read equivalent to a separate verifier.
- It does not authorize Neo to edit core governance without the existing approval process.
- It does not turn `builds/` into a seventh stage without a protocol change.

Confidence is high in the architecture as a design synthesis, but empirical confidence in Neo's eventual performance must be earned through completed pipelines, restart tests, checker measurements, and independent reproduction.

## Cross-Links

- `forge/protocol.md` -- normative six-stage pipeline, artifact schema, gates, and provenance.
- `governance/skills/forge-ideate/SKILL.md` -- idea creation and novelty/testability gate.
- `governance/skills/forge-research/SKILL.md` -- claim-by-claim evidence procedure.
- `governance/skills/forge-evaluate/SKILL.md` -- five-dimension PASS/HALT evaluation.
- `governance/skills/forge-propose/SKILL.md` -- reproducible research planning.
- `governance/skills/forge-validate/SKILL.md` -- adversarial plan stress test.
- `governance/skills/forge-insight/SKILL.md` -- final principle extraction and closure.
- `governance/skills/forge-verify/SKILL.md` -- maker-checker orchestration.
- `research/insights/harness-engineering.md` -- the harness as the safety mechanism.
- `research/insights/loop-engineering.md` -- loop design and alignment depth.
- `research/insights/agent-evolution.md` -- identity and evolution records.
- `research/insights/context-engineering.md` -- context limits and context rot.
- `research/insights/memory-search.md` -- memory and retrieval architecture.
- `brain:governance/system-constitution.md` -- governance constraints.
- `brain:governance/skills/fleet-agent-birth/SKILL.md` -- future Neo profile birth procedure.
- `https://www.anthropic.com/engineering/harness-design-long-running-apps` -- generator/evaluator separation and structured context handoffs.
- `https://github.com/karpathy/autoresearch` -- measurable experiment loops and version-controlled accept/reject iterations.
- `https://arxiv.org/html/2608.05179v1` -- auditability and verification gaps in autonomous research agents.
- `https://addyosmani.com/blog/long-running-agents/` -- external state, checkpoints, progress logs, stop conditions, and recovery.
- `https://www.langchain.com/blog/memory-for-agents` -- procedural, semantic, and episodic memory distinctions.

## Verification Notes

- Protocol and all seven Forge skills were read from the VPS working copy before this rewrite.
- Every Forge stage template was read and its required structure was incorporated into this blueprint.
- Existing brain insights on harness engineering, loop engineering, agent evolution, context engineering, and memory search were cross-checked.
- External research included Anthropic's long-running harness work, Karpathy's autoresearch repository, the 2026 autonomous research agent survey, long-running-agent state guidance, and agent memory guidance.
- The exact original insight id is preserved because this is a revision of an existing published insight. Version 2 is recorded immediately after the title.
- ASCII-only content is required and must pass before commit.

## Falsifiable Operating Tests

The finished Forge proves its architecture operationally through these tests:

1. Kill Neo after an artifact commit but before verification. A fresh loop reads STATUS, discovers verification-pending, and completes or re-runs verification without duplicating the artifact.
2. Kill Neo after a local commit but before push. A fresh loop detects publish-pending, publishes the existing commit, and does not create new work.
3. Present a deliberately contradictory research source. The research artifact must surface it, and a checker must flag a report that hides it.
4. Present an artifact with a broken parent id. Structural verification must HALT it.
5. Present a vague proposal. The proposal gate must return HALT or request concrete method steps.
6. Present an attractive but invalidated plan. Validation must find the weak point and either add a mitigation or return it.
7. Ask the verifier to review the author's own overconfident artifact. The verifier must be able to FLAG or REJECT it rather than treating authorship as evidence.
8. Complete a pipeline, reset all conversation context, and restart from the repository. Neo must identify the closed pipeline, read its LEARNINGS entry, and select the next valid action.

The tests measure the system's real property: not whether the agent can talk continuously, but whether the research process remains coherent, auditable, and improvable when the original process is gone.

## Finished Product Summary

The complete Forge is a controlled research operating system:

```text
ANCHOR + STATUS + JOURNAL + LEARNINGS
                 |
                 v
       discover one next stage
                 |
          Feynman Loop
                 |
          stage-specific skill
                 |
       template and structural checks
                 |
          PASS or HALT gate
                 |
        independent verification
                 |
       checkpoint commit and push
                 |
       fresh iteration from repository

IDEA -> RESEARCH -> EVALUATE -> PROPOSE -> VALIDATE -> INSIGHT
  |        |           |            |          |          |
  +--------+-----------+------------+----------+----------+
            parent-linked, git-auditable provenance
```

Neo supplies initiative and curiosity. The Forge supplies direction, decomposition, evidence discipline, failure memory, recovery, verification, and publication. The model may change, the session may end, and the VPS process may restart; the research system still knows what was attempted, what passed, what failed, why it failed, and what the next honest action is.