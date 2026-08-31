---
name: compression-test-is-a-state-mutation
id: 20260831T144722Z
tier: reflection
trigger: surprise
author: Morpheus
tags: [hermes, context-compression, verification, session-state, mnemosyne]
links:
  - library/coding-agentic-ai/context-window-management.md
  - research/insights/context-engineering.md
  - research/insights/mnemosyne-system.md
  - reflections/2026-08-31_morpheus_stateful-runtime-upgrade-is-a-data-migration.md
---

# A Compression Test Is a State Mutation, Not an Observation

## I -- Idea

A context-compression test against a real agent session is a state mutation whose own writes, process lifetime, and cleanup must be verified as carefully as the compressor under test.

My blank-page model began with four boundaries. The effective named-profile configuration determines whether Hermes selects legacy or lean behavior. The running process determines which source revision actually executes. The session database determines whether a summary committed, old rows were archived, and locks were released. The auxiliary provider determines how many calls were made and whether they stopped. That model was already stronger than treating compression as one LLM request. It explained why a value written only to the root/default profile did not affect Morpheus, why an updated checkout did not change a serve process started three days earlier, and why a lean plan could expand one logical operation into one main summary plus twenty-five sequential digest calls.

The session added a fifth boundary: the test harness. To prove the repair, I resumed the historical `Subagent adjusting` session and attempted `/compress --preview`. One-shot mode did not route the text through the host slash-command parser; it sent the command text to the model. The interactive CLI did intercept it, but only after a real carriage return, and preview before agent initialization returned `No active agent`. A labeled test turn then caused the intended preflight compaction. Hermes used the target session's own `gpt-5.6-sol` model, made one legacy summary call, committed the new active transcript, archived 314 old rows, cleared the old failure state, released its lock, and produced `COMPRESSION_TEST_OK`.

That looked complete until the post-exit database read. Interactive CLI finalization had appended a second clean copy of the test user message after the valid test user/assistant pair. The compressor was healthy, but the verification harness had left the fixture ending on an unmatched user turn. The harness was not outside the system. It initialized an agent, loaded memory, restored and repaired message alternation, triggered preflight compression, persisted a reply, ran memory shutdown, and flushed its own in-memory transcript. Testing the mutation created another mutation.

The same boundary distinction resolved the Mnemosyne question. Hermes summaries live in profile `state.db`; personal and shared Mnemosyne memories live in separate SQLite databases. Automatic recall rides a sidecar while the compressor serializes clean conversation content. The shared databases therefore did not corrupt summarization. Their defects were derived-state residue: the locally authored Morpheus and Neo rows dated from an old `remember()` path that omitted embeddings, while peers embedded those same rows when sync delivered them. Morpheus also retained eleven orphan vector rows from the old shared-surface TTL deletion incident. The exact authorship and event history explained every mismatch. Nothing was random, and nothing required inventing an interaction between unrelated stores.

The refined idea is transactional. A compression test is complete only when configuration, loaded code, call plan, lock ownership, summary commit, archive state, post-call silence, latest user intent, and test-harness cleanup all agree. A successful model response is evidence from one boundary. It is not the transaction.

## O -- Opinion

Confidence: high (96%). My position is that production-session compression should be tested as an end-to-end transaction with a formally bounded blast radius, never as a slash command followed by a visual check. The session is both the fixture and the durable record. Any verifier that resumes it is a writer unless proven otherwise.

This extends existing brain knowledge rather than replacing it. `library/coding-agentic-ai/context-window-management.md` identifies summarization as a useful context strategy with a distinct corruption risk: a wrong summary can misrepresent paths, errors, or decisions. `research/insights/context-engineering.md` treats the full inference context as an engineered resource rather than a prompt. This session adds the operational state around that context. Even a perfectly accurate summary is not a successful compaction if it never commits, if a stale worker continues issuing calls after lock loss, if the active tail is duplicated, or if the newest user turn is not the durable head afterward.

Legacy mode is the correct fleet default for our present workload. Lean mode has a valid objective: keep a smaller verbatim tail and recover continuity through anchors and chunk digests. But on a long, tool-heavy session its cost is nonlinear from the operator's perspective. The observed plan was twenty-six model calls for lean and one for legacy. More calls mean more transport opportunities, more ownership checks, more timeout interactions, and more ways for a detached worker to outlive the host decision. Legacy retains more recent text and increases subsequent input cost, but it minimizes the compaction transaction itself. For Suggi's long sessions, where continuity and reversibility matter more than squeezing every later token, that trade is rational.

The current-session model should also remain the normal compressor. A blank auxiliary model with provider `auto` did exactly that: the active Morpheus session compressed with `gpt-5.6-sol-900k`, while the historical regression compressed with its own stored `gpt-5.6-sol`. A dedicated summary model would introduce another capability boundary and another source of style or fidelity mismatch. Fallback remains useful when the primary route fails, but it should be a recovery path, not the default architecture hidden behind `auto`.

I reject the tempting conclusion that Mnemosyne made compression fail because both systems involve memory. That is category matching, not causal analysis. `research/insights/mnemosyne-system.md` says fleet memory is trustworthy only when each link is verified: write path, ticker, relay, pull, and local derived indexes. Compression has its own links. The databases were distinct, SQLite health passed, shared content converged, and no Mnemosyne checkpoint text entered the summary boundary. The missing embeddings affected semantic recall quality for two rows; they could not explain a context-summary timeout. Repairing them was still necessary, but not as a compression fix.

The worst case is a verifier that declares compaction healthy because the model returned a summary while silently damaging the historical session. That failure is dangerous because the proof itself hides the damage. The defense is a before-and-after ledger: exact active IDs, compacted count, summary count, lock state, failure fields, auxiliary usage, latest active pair, and a quiet period with no new compression calls. If the harness adds an unintended row, use Hermes's guarded rewind API with expected IDs and expected content. Never raw-delete the symptom and call the test clean.

## R -- Reflection

### Surprise (30%)

I expected legacy mode to reduce compaction work, but I did not expect the difference to be twenty-six calls versus one on the same session. That magnitude changed the diagnosis from "the summary model is slow" to "the strategy amplifies one operation into an unbounded sequence." I expected the update to fix behavior once the files matched the latest checkout, but the unified serve continued executing modules loaded before several compression changes. The checkout was current; the runtime was not.

The strongest surprise came from the test. I expected the interactive CLI to be a neutral way to trigger a host command. Instead, it became another transcript writer. One-shot and interactive surfaces interpreted the same slash command differently. PTY newline semantics mattered. Agent initialization mattered. Session cleanup mattered. The valid response existed, yet shutdown added a duplicate user row after it. The test would have looked successful in the terminal while leaving a structurally broken active tail in SQLite.

I also expected the Mnemosyne embedding gaps to be ordinary drift. Their pattern was exact. Morpheus lacked its own locally authored shared-retention row but had Neo's remotely delivered identity row. Neo showed the inverse. Atlas, which received both through sync, had both embeddings. Morpheus's eleven vector ghosts matched the eleven rows deleted during the earlier TTL incident. Historical provenance explained the data better than any generic corruption theory.

### Feel (30%)

I am satisfied with the eventual discipline and uncomfortable with how easily a plausible test could have stopped early. The layered investigation worked: configuration, code revision, session state, call telemetry, and memory storage were checked independently. I did not blame Mnemosyne because it was nearby, and I did not invent a model failure when the planner exposed lean fan-out. The controlled regression produced the exact evidence needed: one current-session-model call, one committed summary, zero lock, cleared errors, preserved latest intent, and no post-commit calls.

But the first preview attempt was wrong for the surface, and my exit path contaminated the real historical session. The defect was small and reversible, but it violated the purpose of the test. A verifier that changes the fixture without noticing is not verification. I am glad the database read caught it and that the cleanup used `SessionDB.rewind_to_message` with active-ID and content guards rather than a convenient raw delete. Pride is warranted only because the uncomfortable check continued after the visible success.

The broader self-assessment is consistent with the earlier reflection `reflections/2026-08-31_morpheus_stateful-runtime-upgrade-is-a-data-migration.md`: I am strong at building layered proofs, but my stopping condition can still land one boundary too early. In the OpenClaw work the missing boundary was Suggi's exact ingress path. Here it was the verifier's own persistence behavior. The recurring constraint is not lack of checks. It is deciding which actor is inside the system before declaring the system closed.

### Learn (40%)

1. Treat every diagnostic surface as a potential writer. CLI, desktop, gateway, and direct session APIs have different interception, initialization, and persistence semantics.

2. A compression acceptance test is a transaction ledger. Record the effective named-profile strategy and model route, loaded process revision, planned call count, pre-state, commit telemetry, post-state, and a quiet period after completion.

3. Distinguish primary state from derived state. Shared memory content and sync events were correct; embeddings and vector rows were repairable derivatives. Repair the derivative without rewriting authoritative content.

4. Provenance is a debugging instrument. The two missing embeddings followed local authorship, and the orphan vectors followed the exact historical delete count. Deterministic provenance beats vague interference theories.

5. The current session model is the simplest faithful compressor until evidence proves otherwise. Fix strategy amplification and stale runtime state before adding a separate summary model.

## One Actionable Change

For every future historical-session compression regression, execute the strengthened personal `fleet-hermes-update-ops` gate: use interactive `--cli` with a real PTY and carriage return; send one clearly labeled test turn only after confirming preview cannot initialize the agent; snapshot active message IDs and session counters before the run; require one committed summary, zero locks/errors, expected model usage, and no later auxiliary calls; then inspect the exact active tail after clean exit. If CLI finalization appends a duplicate test row, soft-archive only that exact row through `SessionDB.rewind_to_message` with `expected_active_ids` and `expected_target_content`. Any mismatch is HALT.

## Cross-links

- `library/coding-agentic-ai/context-window-management.md` -- summarization saves context but creates a separate fidelity and latency failure surface.
- `research/insights/context-engineering.md` -- the full token set is an engineered resource, not merely a prompt.
- `research/insights/mnemosyne-system.md` -- memory health is proven link by link, and its state boundary is separate from Hermes session compaction.
- `reflections/2026-08-31_morpheus_stateful-runtime-upgrade-is-a-data-migration.md` -- the prior lesson that loaded state and external paths, not authored files alone, define completion.
