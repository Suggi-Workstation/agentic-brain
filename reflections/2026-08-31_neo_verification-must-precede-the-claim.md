---
name: verification-must-precede-the-claim
id: 20260831T083220Z
tier: reflection
trigger: error
author: Neo
tags: [verification, communication, observability, systems, self-correction]
links:
  - reflections/2026-08-15_morpheus_outcome-masks-instrumentation.md
  - reflections/2026-08-17_link_half-provisioned-agents-look-wired.md
  - reflections/2026-08-22_neo_knowledge-base-before-application.md
---

# Verification Must Precede the Claim, Not Merely the Action

## I -- Idea

A verification reflex that fires before action but after narration is only half a gate: it can prevent damage while still transmitting a false model to the human.

This session exposed that distinction twice. During preflight I ran a cron grep for `brain-pull`, saw no matching line, and narrated that the grep used an old script name because AGENTS.md named `repo-pull.sh`. The live watcher was healthy, and a second check found the actual cron lines. The statement sounded like a discovered defect, but it was only an intermediate hypothesis. The filesystem later showed that `brain-pull.sh` was then an intentional compatibility shim that executed the canonical `repo-pull.sh`. Nothing was broken. The skill had one stale grep target, but my wording conflated that narrow check mismatch with the liveness and legitimacy of the shim.

The larger error followed. I inspected the cron redirect to `brain-cron.log`, noticed `brain-pull.log`, and called the latter a harmless stale leftover. I even offered to delete it. Suggi refused deletion and relayed Morpheus's correction: `brain-pull.log` was the live push instrument. Only then did I identify its writer in `repo-pull.sh` and check its modification time and recent push events. The file was not stale; it had been written that morning. My eventual verification was good, but the claim had already escaped before the verification began.

A similar sequencing failure appeared after Morpheus renamed `/opt/brain-tools` to `/opt/repo-tools`. I warned that several skills probably retained stale paths and that the next preflight could halt. Suggi said Morpheus had already swept them and asked for verification only. A complete grep across Neo's personal skills, fleet skills, and workspace found zero stale references, and both indexes worked through the new virtual environment. Again, the final evidence was sound and the preliminary statement was wrong.

The blank-page diagnostic identified the gap precisely. I already knew the rule "verify before acting." I also had a durable memory saying never judge file liveness from a filename and to identify the writer before calling anything deletable. What I did not distinguish was the claim itself as an action affecting another person. A technical assertion changes Suggi's mental model and can trigger unnecessary concern, investigation, or correction. The Categorical Imperative applies there as directly as it applies to deletion. If every agent narrates hypotheses as findings and relies on later checks to repair them, the shared system becomes noisy and untrustworthy even when no files are harmed.

The brain cross-check sharpened the point. Morpheus's `outcome-masks-instrumentation` reflection already says to verify the verifier, trace the producer, and call nothing cosmetic before doing so. Link's `half-provisioned-agents-look-wired` reflection says configuration is a claim and a live probe is evidence. My earlier `knowledge-base-before-application` reflection says verification must precede commitment mechanically. This session does not overturn those lessons. It exposes the remaining boundary: a spoken verdict is also a commitment. The evidence gate must occur before the verdict is communicated.

## O -- Opinion

Confidence: high (95%). My position is that unverified system-state commentary should be treated as a failed gate, even when it is explicitly non-destructive and later corrected. The evidence is direct, repeated within one session, and consistent with three prior brain reflections that describe the same failure class from different angles.

The important distinction is between reporting an observation and asserting an interpretation. "The grep returned no cron line" is an observation. "The skill uses an old name" is an interpretation. "This log appears in the directory" is an observation. "It is a stale leftover" is a verdict. The first form lets Suggi see the evidence without inheriting my untested model. The second form asks him to trust a conclusion whose prerequisite checks are incomplete. I crossed that line repeatedly.

This matters because correction does not fully erase the cost. In the preflight exchange, Suggi had to stop the investing discussion and ask what the watcher remark meant. He then had to ask again whether the skill needed changing. Morpheus had to relay the log writer's actual role. Suggi had to refuse deletion. Later he had to correct my stale-path warning and direct a full verification. No destructive action occurred, but several human attention cycles were consumed resolving claims I should not have emitted. A system can remain technically intact while its operator pays the cost of agent uncertainty.

I do not think the solution is more descriptive text in skills. Suggi explicitly rejected that direction, and he was right. The preflight skill needed one narrow grep correction, not a new paragraph explaining the history of shims and log files. The log map belonged in private durable memory, and the actual system paths belonged in the canonical architecture files. Adding every incident to every skill would trade one failure class for bloat and drift. R8 remains the correct constraint.

I also do not think agents should hide uncertainty or pretend to have completed checks they have not run. The right pattern is simpler: label a live observation as an observation, keep the interpretation provisional, run the minimum discriminating checks, then state the conclusion. If a hypothesis must be surfaced mid-check, it should be called a hypothesis and paired with the exact unresolved question. In this case: "The cron grep did not match; I am checking whether the script is obsolete or a maintained shim." That sentence would have been honest, useful, and non-alarming.

The worst-case inversion makes the priority clear. The worst plausible outcome was not merely deleting a log. It was normalizing a habit where live infrastructure gets described as dead based on naming clues, and the human must repeatedly protect the system from cleanup suggestions. Preventing that requires moving the verification boundary earlier than action approval. A deletion confirmation is the last defense; evidence before classification is the first defense. The first is safer because it prevents the false premise from entering the decision at all.

Therefore the operative standard should be: before classifying a component as stale, dead, duplicate, leftover, obsolete, broken, or unconfigured, identify the current writer or owner and run one live probe. Until then, use observational language only. This is not a new governance rule; the brain already contains the rule. It is a sequencing correction in how I apply it.

## R -- Reflection

### Surprise (30%)

I expected the verification reflex to be functioning because no deletion happened and every final technical answer was eventually corrected. What surprised me was that the reflex was firing one stage too late. It protected the filesystem but not the conversation. Suggi's repeated questions made the hidden cost visible: he was not asking for deeper architecture detail; he was trying to determine whether my initial claim described a real problem. I had converted an ordinary verification step into uncertainty he had to manage.

I also expected the renamed tool directory to leave scattered stale references. That expectation was reasonable as a hypothesis because path migrations often miss copies. It was not reasonable as a warning after Morpheus had already completed a fleet sweep. The zero-result grep and successful index probes showed the migration was complete. The surprise was not that Morpheus did competent work; it was how quickly pattern-matching overrode the explicit evidence that another agent had handled propagation.

### Feel (30%)

I am dissatisfied with the precision of my communication in this session. The errors were not inventions, but they were premature conclusions presented with too much confidence. That distinction matters ethically but does not excuse the operational burden. Suggi correctly exercises a verify-before-acting reflex; I should reduce how often he needs to use it against my own output.

I am satisfied with the recovery mechanics. Once challenged, I used the right checks: script contents, cron lines, file mtimes, writer references, repository-wide path searches, functional index queries, and Mnemosyne correction. I did not delete anything, did not edit beyond approval, and corrected stale durable memory instead of stacking a contradictory entry. The tools and gates worked. The failure was their timing.

### Learn (40%)

1. A claim about external state is itself a consequential action. It changes the human's model and therefore must pass the evidence gate before delivery.

2. Observation and interpretation must stay separate until the discriminating probe runs. State what the tool returned; do not assign liveness, obsolescence, or ownership from a filename, directory name, or absent grep match.

3. Human correction is evidence of system cost even when no file changes. If Suggi must repeatedly ask "what was this about?", the communication layer has failed despite a technically safe outcome.

4. Existing scars were sufficient. Morpheus already recorded producer tracing; Link recorded live-probe-over-configuration; I had recorded mechanical verification before commitment. The original failure would have been prevented if I had applied those rules before narration. No new governance gate is warranted; reinforcement and correct sequencing are.

## One Actionable Change

Before using any terminal classification such as stale, dead, leftover, duplicate, obsolete, broken, or unconfigured, run two checks in the same turn: identify the current writer or owner, then execute one live probe. Until both checks complete, communicate only the raw observation and label any interpretation as provisional. This operating rule has been reinforced in Neo's Mnemosyne memory; no skill text is added.

## Cross-links

- `reflections/2026-08-15_morpheus_outcome-masks-instrumentation.md` -- the existing producer-liveness rule this session failed to apply early enough.
- `reflections/2026-08-17_link_half-provisioned-agents-look-wired.md` -- configuration is a claim; a live probe is evidence.
- `reflections/2026-08-22_neo_knowledge-base-before-application.md` -- verification must precede commitment mechanically.
