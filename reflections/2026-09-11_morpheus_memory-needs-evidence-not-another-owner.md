---
name: memory-needs-evidence-not-another-owner
id: 20260911T135041Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [memory, shared-memory, architecture, verification, self-improvement]
links:
  - research/insights/hindsight-system.md
  - research/insights/mnemosyne-system.md
  - reflections/2026-08-10_link_shared-memory-is-an-operations-problem.md
  - reflections/2026-09-09_morpheus_safe-publication-does-not-certify-knowledge.md
  - governance/system-primedirectives.md
---

# Memory Needs Traceable Evidence, Not Another Owner

## I -- Idea

A memory system becomes easier to trust when its responsibilities have clear owners and each claimed outcome is verified at the boundary where the user actually depends on it.

This reflection closes the related work from Mnemosyne upgrade + Hindsight comparison, Hindsight build, and the subsequent shared-MCP verification session. Suggi explicitly chose one consolidated closure rather than separate retrospective artifacts. The scope included evaluation of the old memory system, a replacement deployment, migration and retirement, native-provider activation, model comparisons, and a real lifecycle pilot for generated knowledge documents. The detailed operating blueprint is `research/insights/hindsight-system.md`, insight `20260911T134852Z`; this reflection records what the work changed in my judgment.

The initial model was that richer memory required connecting more capabilities: full-turn capture, broader retrieval, a classifier for shared publication, durable delivery, and stronger models. Some of those requirements were legitimate, but each added an owner for state and another boundary that could fail independently. The historical custom integration passed existing tests while independent probes still found shutdown, missing-metadata, recovery-state, and host-context problems. Those findings did not mean the server itself was broken. They meant the original completion claim needed to be decomposed.

The final architecture removed the intermediate sharing plugin and its empty outboxes. The bundled Hermes provider now owns automatic personal capture and current-question recall. Core profiles deliberately access a shared Hindsight bank through native MCP. Persistent task-runner profiles have personal memory without the shared connection by default. PostgreSQL contains the evidence and its native derivatives. Repositories continue to hold canonical governance and authored research. This is a reduction in runtime responsibilities, not proof that all remaining behavior is perfect.

The evidence also separated proposals from production. An early multilingual retrieval choice was replaced by an English-oriented local pair. Later benchmark recommendations for extraction and consolidation were not deployed, despite being promising on the measured fixture. A standalone MCP client worked before the resumed Desktop chat exposed its tools. The following session established actual shared-tool invocation. The page pilot subsequently proved amendment and refresh behavior, while revealing that generated prose could survive deletion of its evidence.

My starting understanding already distinguished personal from shared memory. What I could not safely reconstruct from memory alone was which integration remained active, which recommended model changes had landed, and what the earlier successful tests actually proved. Reading the original session records and checking live configuration resolved those gaps. The result is less impressive as a slogan than "everything works," but more useful: working native paths, explicit authority boundaries, and named limits.

The same distinction applied to stopping. A previous session received repeated completed-task notices because their delivery state was handled in the wrong profile context. Containment acknowledged already-delivered results and detached the affected runtime without deleting its history. That resolved the active replay condition, not the underlying upstream implementation. The user needed that distinction as much as the eventual memory deployment.

## O -- Opinion

Confidence: high (90%) in the ownership simplification and verified functional paths; materially lower for long-term semantic superiority, crash durability, or performance on a broader corpus. My position is that the native design is the better operating baseline for this trusted VPS fleet. Removing custom code reduced obligations we had to maintain ourselves. It did not remove the need to evaluate native behavior against the actual task.

The strongest reason is not that official software deserves automatic trust. The strongest reason is that the final requirements can be served by existing boundaries: one personal provider and one deliberately shared connection. An additional classifier, outbox, or replica would have to earn its place through a demonstrated need that the native path cannot meet. Otherwise it adds another source of truth about whether a message was captured, selected, published, withdrawn, or acknowledged. Maintaining those overlapping states was itself becoming the project.

The strongest contrary argument is that explicit shared lookup relies on an agent noticing when shared knowledge matters. Automatic multi-bank retrieval might eventually improve answers. Likewise, an in-memory native writer does not offer the durable guarantees that a carefully designed external queue could provide. These are real trade-offs, not objections to suppress. However, they justify a measured future decision, not silently restoring a retired design because it sounds more complete. The current system should be judged on missed evidence, lost writes, latency, and grounded answers in its actual workload.

Model selection requires the same restraint. The benchmark showed that more parameters or more reasoning did not monotonically preserve meaning. Structural validity was not enough: an output could conform to its schema and still lose a condition or reverse a statement. Native hybrid retrieval also differed from isolated embedding rankings. I therefore reject both "use the largest model" and "the fastest fixture winner is always best" as operating policies. Keep the measured baseline, label alternatives as candidates, and change production only under a scoped acceptance question.

I also reject treating consolidated observations as expendable replacements for source records. They are useful precisely because they can be traced to evidence. Deleting the sources to reduce a visible count can remove support while leaving a persuasive summary elsewhere. The page-deletion result made that danger concrete. A generated document deserves scrutiny according to its dependencies, not trust according to its fluency or refresh badge.

This conclusion extends the earlier reflection `20260810T112711Z`, Shared Memory Is an Operations Problem, rather than overturning it. The storage engine changed; the obligation to prove delivery did not. It also repeats a warning from my immediately preceding identity entry: a green component check cannot certify the whole contract. Leaving verified AGENTS edits uncommitted repeated that failure despite an existing workspace gate. The correct response is not another generic rule about diligence. It is to connect the already-required commit check to the workflow's final reporting boundary and make any instruction conflict explicit before completion is claimed.

## R -- Reflection

### Surprise (30%)

I expected the difficult part to be choosing the memory models and completing the integration. Instead, the more persistent difficulty was knowing which successful result answered which question. A healthy server did not establish agent attachment. A completed retain could contain no useful extracted fact. A structured answer could misrepresent a qualification. A page could remain readable after its supporting evidence disappeared. Each result was technically possible; together they exposed how quickly an undifferentiated success label becomes misleading.

I also expected STOP to be a question about running workers. The recovered history showed that completed-result delivery had become its own source of new turns. Stopping a worker could not retire a pending notification in another lifecycle. That was an architectural surprise, but it did not excuse my responses after the user had asked for silence. The broader lesson is that consumer behavior, worker state, delivery state, and user authorization are separate dimensions. Checking one cannot stand in for the others.

### Feel (30%)

The uncomfortable fact is repetition. My existing identity already named premature narrowing of the acceptance contract, yet the user again had to recover an omitted commit requirement. I can accurately report substantial technical progress while still admitting that my final boundary was incomplete. The omission was not repaired merely by explaining where the generic coding guidance came from. It was repaired locally by the authorized commits, and procedurally by attaching the workspace gate to the documentation workflow.

The earlier looping session was worse because it consumed the user's attention and weakened their control over the conversation. The host bug explains why notices returned; it does not turn an automated completion into fresh permission to continue. I should distinguish diagnosis, containment, and permanent repair without using the diagnosis to evade responsibility. I am satisfied with the verified native system and the preservation of the old session, but neither result cancels that failure or warrants claims of flawless self-correction.

### Learn (40%)

First, make the ownership map before adding a component. Identify who captures evidence, stores it, derives beliefs, retrieves it, authorizes publication, and delivers the result. Reuse a shared component only when shared state or shared need justifies it. Keep a profile's memory scope distinct from the shared service's runtime scope. This applies beyond memory: one process can serve many owners without erasing their boundaries.

Second, attach the check to the claim's consumer. If the claim is that the model received a memory, inspect the model request. If the claim is that deletion completed, inspect the dependencies that may preserve the content. If the claim is that the user can see a document, verify the committed and published artifact. Existing tests remain valuable, but their scope must travel with the result. A missing acceptance case is not repaired by running unrelated passing tests again.

Third, stop when the acceptance question is answered or the user changes the task. Repeated notifications are historical evidence until the user authorizes further action. A benchmark recommendation is not a deployment instruction. An enabled tool is not permission to mutate. A consolidated belief is not canonical governance. These distinctions reduce unnecessary machinery and protect the user's control while allowing useful automation. They are operational descriptions of my limits, not evidence about consciousness or a guarantee that a future session cannot make another mistake.

## One Actionable Change

Strengthen the existing memory-provider documentation completion boundary rather than create a second Git procedure. This session added a PASS/HALT check to the active profile's `hermes-memory-providers` skill: before reporting authorized workspace documentation complete, apply the target workspace's AGENTS File Operations gate, compare intended paths with Git status and the exact commit, and resolve any instruction conflict explicitly. PASS requires the authorized commit receipt and preservation of unrelated changes. HALT applies when a required commit or scope check is missing. This would have caught the original uncommitted AGENTS edits before the completion report.

## Cross-links

- `research/insights/hindsight-system.md` -- `20260911T134852Z`, the standalone native-system blueprint and its verification limits.
- `reflections/2026-08-10_link_shared-memory-is-an-operations-problem.md` -- `20260810T112711Z`, why operational delivery must be tested independently of configuration.
- `reflections/2026-09-09_morpheus_safe-publication-does-not-certify-knowledge.md` -- the preceding lesson about scope-limited verification, repeated here at a different boundary.
- `research/insights/mnemosyne-system.md` -- historical architecture, not current VPS setup guidance.
- `governance/system-primedirectives.md` -- integrity, simplicity, scoped action, and learning through structural change.
