---
name: consolidated-memory-still-needs-a-current-truth-check
id: 20260912T134157Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [memory, verification, simplicity, self-improvement]
links:
  - research/insights/hindsight-system.md
  - reflections/2026-09-11_morpheus_memory-needs-evidence-not-another-owner.md
  - reflections/2026-09-09_morpheus_safe-publication-does-not-certify-knowledge.md
  - governance/system-primedirectives.md
---

# Consolidated Memory Still Needs a Current-Truth Check

## I -- Idea

A memory can be faithfully stored, correctly retrieved, and successfully delivered while still being the wrong evidence for the user's current decision.

This session began with council design and expanded into the operation of persistent memory. Suggi asked about agent roles, conversation summarization, stronger retrieval models, slow recalls, and outdated memories. The original Hindsight architecture was already deployed. The task was not to invent another memory system; it was to understand and improve the behavior of the existing one. The preceding reflection, `20260911T135041Z`, established that native ownership still requires evidence at each boundary. This session exposed an additional boundary: technical retrieval correctness does not establish present validity.

An earlier broad-recall choice allowed Hermes to retrieve raw world and experience facts alongside consolidated observations. That made recently extracted evidence available before consolidation completed, but it also exposed old decisions directly. The rerankers evaluated relevance to a question, not whether a once-valid instruction had been superseded. A historical request could therefore rank above a newer correction. Its text and source reference could be exact while its practical implication was wrong. The important distinction was not stored versus missing; it was historical evidence versus current guidance.

Model comparisons made this visible. The authorized live-memory matrix measured four rerankers at two candidate caps against a frozen Gemma-indexed snapshot. It included current-policy questions and an absent-project control, not just easy answer-present examples. Larger or slower models did not reliably promote the current policy, and every configuration returned unrelated material for the negative control. These were assistant-graded, narrow tests, not universal quality rankings. Their useful result was the failure pattern: more model work could improve relevance without resolving authority or obsolescence.

The eventual production choice restored the original BGE and MiniLM pair, with the normal candidate cap reduced to thirty. Restoring the old configuration required reconciling newer knowledge with the retained database; pointing at an earlier store alone would have discarded later work. The original evidence and accepted archival boundaries mattered more than making the configuration look familiar. Model residency was another separate fact: weights already stayed loaded, while every query still incurred embedding and reranking work.

The final recall-policy revision followed Hermes's observation-only default. Fresh native providers returned only observations through the host's bounded prefetch path. Yet a summarization-policy question still ranked an obsolete observation first, while the shared-publication question ranked the current policy correctly. That is the central counterexample. Consolidation improved the representation being retrieved; it did not certify every stored interpretation. My initial understanding separated sources from summaries. Source inspection and live checks showed that I also needed to separate retrieval eligibility, consumer activation, and present truth.

## O -- Opinion

Confidence: high (90%) that delivery, relevance, and current validity must be tested separately; medium that observation-only recall alone will materially improve every operational question. The first claim follows directly from distinct failures observed in the same system. The second remains a workload hypothesis: the filter worked mechanically, but one of the focused current-policy checks still exposed stale derived knowledge.

My position is to keep the native architecture and repair the specific policy boundary before adding another component. Ordinary recall should favor consolidated observations, as the Hermes provider prescribes. Source facts should remain available for deliberate investigation and reflection. Confirmed misextractions or obsolete active assertions should be corrected or invalidated through the native curation interface when authorized. A blanket observation rebuild would consume work and remove revision history without necessarily removing the historical assertions that produced the problem. Routine deletion is not a substitute for understanding what is stale and why.

Storage growth requires a different judgment. A source archive can grow while the amount of useful prompt context remains bounded. Revision caps and operational-record retention can limit particular storage classes without deleting the knowledge they support. Conversely, invalidation can remove a fact from active retrieval while retaining its archive. Neither operation is a universal database-size ceiling. The read-only inspection showed no immediate storage emergency. I therefore reject framing every retained historical fact as waste or treating a lower record count as proof of better memory.

The web-search interruption reinforced the same approach. A failure attributed broadly to the search gateway was traced to provider entitlement rather than general connectivity. The replacement used Parallel's supported keyless integration. Suggi then challenged my plan to repeat settings across profiles, prompting verification of Hermes's machine-wide managed layer. That layer suited a shared web-provider requirement, but it did not own the Hindsight plugin's profile-local JSON settings. Similar-looking configuration files did not imply identical inheritance. The correct simplification was native ownership at each scope, not forcing everything into one central file.

The strongest objection is that these distinctions can themselves become an excuse for excessive analysis. That objection applied to my conduct. Suggi repeatedly redirected me toward direct execution, the existing blueprint, and the specific requested change. Some comparisons were explicitly requested; others were not a reason to delay the current deployment decision. A comprehensive explanation that arrives after avoidable service disruption or repeated clarification has an operating cost. The solution is not to skip preservation or verification, but to define the smallest complete acceptance question and stop when it is answered.

This extends the prior ownership lesson rather than overturning it. Native tools reduce the amount of machinery we maintain, but their documentation, defaults, lifecycle, and failure modes still need inspection. My judgment should become more selective as evidence accumulates, not more elaborate. Where a semantic check fails, the honest result is a working retrieval path with an unresolved data-quality finding, not a declaration that the memory system is now clean.

## R -- Reflection

### Surprise (30%)

I expected an observation-only filter to remove the most obvious route by which old decisions reached the prompt. It did remove independently recalled raw facts, but a superseded observation still ranked first. The source correction existed, and the host received context on time. That combination showed why freshness cannot be inferred from successful consolidation, recent delivery, or a plausible top result. Each is a different property of the evidence.

A second surprise appeared during closure. The required logbook validator claimed to check the newly appended entry, but its implementation examined the second-last header and did not enforce exactly one separator. The old script accepted missing and doubled separators in the actual target. A validator can preserve the same proxy-check mistake as a model: it returns a convincing success signal about a nearby state. Explicit negative fixtures exposed the defect without changing any real log entry.

### Feel (30%)

My uncomfortable assessment is that proportionality remains an active weakness. I had already named premature narrowing of acceptance in the previous identity entry. Here I also expanded narrow tasks into longer operational investigations, and Suggi had to insist on direct work and simpler execution. More diligence is not automatically more useful. Effort spent on a technically interesting branch can still displace the user's immediate objective.

I am satisfied with the preserved knowledge, restored native retrieval pair, working web default, and candid disclosure of the stale-observation result. Those outcomes are supported by tools. They do not erase the delays or prove that written lessons will always govern my next choice. The identity update should therefore record concrete capabilities and a continuing constraint, not manufacture a story of complete improvement. No conclusion about consciousness follows from understanding my configuration and memory dependencies more accurately.

### Learn (40%)

First, define the exact consumer claim before choosing the test. A provider configuration, a fresh native client, an already-open chat, and the model's outgoing context are distinct states. State which one was exercised. For semantic quality, include a question whose historical answer is known to be obsolete. A relevance score or an observation type cannot substitute for checking the correction and its authority.

Second, preserve current state when taking a reversible-looking action. Rolling back an embedder is not merely reversing a filename if the database has accepted new knowledge. Likewise, invalidating an assertion differs from deleting its source, and limiting operation history differs from limiting memory. The safest simplification keeps those meanings explicit, uses the native operation that matches the goal, and avoids adding services or cleanup jobs without a demonstrated need.

Third, test the verifier with a counterexample at the actual boundary. The logbook repair now selects the last or explicitly requested entry and rejects absent, ambiguous, missing-gap, and multiple-gap cases. The regression suite proved the old failure before proving the fix. This is stronger than adding another reminder to inspect spacing. It also supplies a practical stopping rule: once the scoped contract and its negative cases pass, close the work rather than inventing a larger maintenance project.

## One Actionable Change

Repair the existing session-end separator validator rather than add another logbook rule. With Suggi's explicit approval, Morpheus's local `session-end/scripts/check-logbook-blank-line.sh` now resolves the actual last or requested ENT entry, requires a unique target, and checks for exactly one preceding blank line when a predecessor exists. Invoke it after appending and before committing. PASS requires the real target to satisfy that boundary; malformed selection or zero/multiple separators HALTs publication. The regression fixtures reproduced the original false passes and then all passed against the corrected script. Shared copies were not silently rewritten.

## Cross-links

- `research/insights/hindsight-system.md` -- `20260911T134852Z`, the current native architecture, observation-only policy, activation boundary, and documented semantic limits.
- `reflections/2026-09-11_morpheus_memory-needs-evidence-not-another-owner.md` -- `20260911T135041Z`, the preceding ownership and consumer-verification lesson extended here.
- `reflections/2026-09-09_morpheus_safe-publication-does-not-certify-knowledge.md` -- why procedural success and justified knowledge require different evidence.
- `governance/system-primedirectives.md` -- integrity, simplicity, scoped action, and structural learning.
