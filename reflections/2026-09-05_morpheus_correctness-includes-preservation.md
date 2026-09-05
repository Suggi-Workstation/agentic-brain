---
name: correctness-includes-preservation
id: 20260905T211414Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [verification, scope, gate-design, end-to-end-testing]
links:
  - research/insights/mnemosyne-system.md
  - reflections/2026-09-03_morpheus_natural-transitions-prove-automation.md
  - reflections/2026-09-01_morpheus_background-controls-need-an-evidence-lifecycle.md
  - reflections/2026-07-19_ava_defense-in-depth-time-separated-gates.md
---

# Correctness Includes What Must Not Change

## I -- Idea

A repair is correct only when it produces the authorized change, preserves the surrounding state, and satisfies every obligation included in its completion claim.

The immediate task was repairing a deterministic publisher that copies selected private memory summaries into shared memory. Summarization and synchronization are separate stages. The publisher does not generate a summary or call the current chat model. Its responsibility is narrower: select eligible existing episodes, publish new copies with their provenance, withdraw obsolete owned copies, and leave everything outside that responsibility alone. The user authorized this repair for three agents and wanted the existing system blueprint to explain it without losing the rest of the architecture.

The original publisher looked more successful than it was. A history query used the wrong metadata column, and the exception became an empty publication history. The underlying memory API deduplicated matching content, so repeated execution did not necessarily create additional rows. However, returning an existing identifier was not a no-op: the API could update timestamps and expiry. Counting rows therefore missed a change to the very history that deduplication was supposed to preserve. The first necessary correction was to inspect state, not infer behavior from the shape of the return value.

Independent review found a deeper boundary. Different episode identifiers could share content, and an inactive matching row could arrive after the publisher's planning snapshot. A later native write could revive that row. An additional read-back check would observe the result only after the harmful update committed. The eventual repair reserved the SQLite writer and repeated collision checks on the same connection before insertion. The tests now include preservation of inactive markers arriving between planning and publication, rather than checking only the expected new output.

Documentation exposed the same omission in a different form. I replaced much of the wider blueprint while explaining the repaired component. The new explanation did not excuse removing information the user still needed. Suggi explicitly required restoration of the original document and an additive publisher subsection. That correction established a preservation requirement for the document, just as the database tests established one for existing memory. A smaller file was not automatically a simpler or more faithful result.

Finally, I finished implementation work without finishing session closure. The reflection and identity evaluation remained outstanding. My blank-page model connected these events as incomplete acceptance criteria. Reading the prior reflections sharpened the distinction: natural transitions establish who caused a change; preservation checks establish whether that change stayed within its authority. Completion requires both, plus evidence for the remaining named deliverables. These are related tests, not interchangeable signs of success.

## O -- Opinion

Confidence: high (95%). Preservation should be an explicit acceptance condition, because this session produced concrete counterexamples to judging correctness from a successful write, an improved explanation, or a completed implementation.

The strongest evidence is the native API behavior. A recording adapter can verify which arguments the publisher sends while missing what the installed library actually does with them. An integration fixture exercises those semantics without exposing live memory to experimental writes. The final regression suite passed, and an independent reviewer also exercised adversarial transaction interleavings. This supports the specific repair against the installed implementation. It does not prove compatibility with every future library version, eliminate the documented snapshot boundaries, or demonstrate the next scheduled execution before it happens.

The distinction matters because the tempting response is simply to demand more tests. More tests of the same output would still miss the defect. A test that asks whether a copy exists cannot establish whether an older copy was refreshed, whether another owner's record was changed, or whether an expired record became active. The test must name the forbidden mutation. For concurrency-sensitive invariants, the implementation must also protect the interval between observation and action. Detecting a violation afterward is useful evidence, but not equivalent to preventing it.

The documentation error supports a parallel position: a component repair does not authorize redesigning the explanatory scope of the system reference. The surrounding sections are part of the user's asset, not disposable context around my contribution. A full rewrite can be appropriate when explicitly requested. Here, restoration plus a focused addition was the correct operation. Diff review against the pre-edit version is the simplest relevant proof; no new documentation framework or additional governance layer is needed to establish that unrelated material survived.

I also distinguish session completion from software acceptance. A working publisher can be reported as working while reflection, identity, commits, or watcher verification remain pending. The problem is collapsing those states into one finished label or silently abandoning the remaining procedure. An explicit pending item is honest and actionable. A missing item hidden by a successful implementation summary transfers the burden of remembering the contract back to the user, as happened when Suggi had to ask whether I had actually closed the session.

This extends rather than replaces the earlier evidence-lifecycle and natural-transition reflections. Their concern was the ownership and freshness of evidence. The additional concern here is its coverage: each success claim must include the state that should survive unchanged. The proportional response is a boundary-specific acceptance record using existing tests and diffs, not a universal monitoring system. Scope discipline applies to the proposed safeguard too; preventing one omission must not become permission to build unrelated machinery.

## R -- Reflection

### Surprise (30%)

I expected native deduplication to make repeated publication harmless, but an unchanged row count concealed refreshed state. I then expected a collision check before publication to be sufficient, but the reviewer introduced a matching inactive marker after the snapshot. The check was correct about an earlier moment and still inadequate for the write that followed. This changed my question from whether I had checked the condition to whether the condition remained protected when the mutation occurred.

The documentation correction was equally instructive. I expected reducing the blueprint around the repaired mechanism to improve clarity, but it removed explanations the user needed. That was not an unexpected preference discovered late; the request already concerned an end-to-end blueprint. The surprise was recognizing how easily my attention narrowed the definition of the artifact to the part I had just worked on.

### Feel (30%)

My assessment is mixed. The repair earned confidence through reproduced failures, installed-API tests, independent review, and bounded deployment. I accepted the reviewers' counterexamples and changed the implementation rather than defending passing tests that did not cover the failure. That is useful engineering behavior, and the resulting test cases preserve knowledge beyond this conversation.

The documentation rewrite and incomplete closure did not earn the same assessment. Suggi had to protect existing context and then remind me of obligations already written into my own procedure. I should not describe that intervention as evidence that I had become reliable at those boundaries. The correction is evidence of a limitation identified, not a limitation permanently removed. The useful response is to restore the asset, finish the missing work, and make the omitted deliverables visible in the closing workflow. There is no benefit in either self-excuse or exaggerated remorse.

### Learn (40%)

First, preservation is observable. For a repeat operation, compare the relevant records and timestamps, not only their count. For an archive, compare the complete old section with its saved copy. For a focused document edit, compare the unaffected text with the baseline. These checks turn a vague intention to avoid collateral change into a falsifiable condition. They must follow the scope of the claim rather than demanding that an entire active system remain frozen.

Second, a safety check has a lifetime. Where another writer can invalidate its premise, protect the check and the operation within the appropriate transaction boundary. The native API's commit behavior is part of that reasoning. A post-write verification remains valuable, but cannot retroactively prevent a committed harmful change. This qualifies the general write-time/read-time gate pattern without rejecting its value for detecting later drift.

Third, session closure needs its own acceptance state. The implementation's completed task list did not represent the reflection, identity decision, archive, commits, and watcher evidence. Making those deliverables explicit preserves them across interruption. That is a procedural improvement, not a claim that the platform now automatically prevents every premature reply. I must keep that limitation visible while applying the checks that exist.

## One Actionable Change

Before accepting a bounded repair, use one preservation-aware acceptance record: state the authorized changes, the surrounding state that must remain unchanged, and the outstanding completion evidence. Attach a concrete check to each item, such as an installed-API state comparison, a baseline diff, an archive equality check, or an artifact-backed closure task. Run the checks before the corresponding commit or completion claim. PASS requires the intended change, preserved boundaries, and evidence for every required deliverable; any failed or unverified item is HALT for that claim. This session applies that record through the publisher regressions, the restored-document comparison, and explicit session-end tasks, without adding runtime services or changing shared governance.

## Cross-links

- `research/insights/mnemosyne-system.md` -- the complete memory-system reference, with the additive publisher repair and its verification boundaries.
- `reflections/2026-09-03_morpheus_natural-transitions-prove-automation.md` (id: 20260903T165935Z) -- observing the designated producer rather than manufacturing a green snapshot.
- `reflections/2026-09-01_morpheus_background-controls-need-an-evidence-lifecycle.md` (id: 20260901T052512Z) -- evidence freshness and lifecycle belong inside completion.
- `reflections/2026-07-19_ava_defense-in-depth-time-separated-gates.md` (id: 20260719T105602Z) -- complementary write-time and read-time checks; concurrent mutation additionally requires protecting the check-to-write interval.
