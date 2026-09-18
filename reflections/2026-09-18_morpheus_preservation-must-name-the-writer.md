---
name: preservation-must-name-the-writer
id: 20260918T202117Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [verification, scope, gate-design, hermes-desktop, profiles]
links:
  - reflections/2026-09-05_morpheus_correctness-includes-preservation.md
  - reflections/2026-09-17_morpheus_correct-settings-do-not-prove-transitions.md
  - reflections/2026-07-19_ava_defense-in-depth-time-separated-gates.md
---

# Preservation Must Name the Authorized Writer

## I -- Idea

A preservation claim is meaningful only when it names the invariant, the authorized writer, and the interval over which both were checked.

The practical setting was a desktop application connected to local and remote agent profiles. The user needed the local agent to remain available while the remote gateway could still be the place the application opened. Previous inspection had found correct saved preferences and healthy services, yet the ordinary local-profile picker could discard the machine identifier and fall back to the remote gateway. This time, native interface testing reproduced that transition on the laptop and then independently on the PC. The failure was not inferred from a warning badge or from the fact that both machines ran Windows.

The repair used existing application settings rather than a modified executable. The local runtime became the app-managed backend and registry Primary, while the separate last-used preference retained the ability to start on the remote gateway. Local and remembered-remote cold launches were exercised, including a return to the named local profile before visiting Settings. The laptop's result was confirmed by the user before work moved to the PC. These tests supported a settings workaround for the observed paths, not a declaration that the upstream source defect had been repaired.

The official multi-connection guide distinguishes the registry fallback from the startup destination. It also documents remote Primary as supported. Therefore the observed implementation defect and the successful local-primary workaround do not establish that remote Primary is inherently an invalid design. The invariant was the selected gateway and profile retaining ownership through the action; matching every previously preferred configuration value was not itself the requirement once the user authorized a different working arrangement.

Credential verification exposed the complementary mistake. I initially compared complete authentication-file hashes to establish preservation. That worked in the bounded laptop check. During PC testing, however, the default store and later the named profile's store changed while provider discovery was being exercised. The model configurations remained unchanged, and current Codex credentials were still accepted by the provider. I had not copied credentials, requested another login, or manually edited either store. Nevertheless, without a field-level baseline, I could not honestly certify the exact internal before-and-after delta.

My blank-page account treated this as a conflict between static snapshots and live behavior. Reading the earlier preservation and transition reflections sharpened it: the missing variable was authorized write ownership. A preserved document section should normally remain byte-identical during a narrow edit. A live authentication store can have another legitimate writer, whose updates require interpretation rather than automatic rollback. The same measurement can be appropriate at one boundary and insufficient at another. The practical advance is to specify those boundaries before collecting evidence, instead of discovering their meaning only after an assertion fails.

## O -- Opinion

Confidence: high (90%). Preservation should be defined as a set of owner-specific invariants, not as a blanket demand that an active system retain identical bytes. The repeated routing tests and the changing authentication stores support that position; they do not explain every internal credential update that occurred.

The strongest evidence is the combination of a failing user action and a passing repeat after a bounded, authorized change. The original local Default-to-named-profile selection switched to the remote gateway on each machine. After the supported settings change, the same transition remained local, including after the relevant cold-start paths. Profile-home responses independently established that the local default and named backends were different intended homes. This is materially stronger than inspecting a correct registry, but its scope still ends at the exercised behavior. It is not a promise that future releases cannot regress or that every possible session-opening path was tested.

The authentication comparison deserves equal precision. An unchanged whole-file hash is strong evidence that the sampled bytes did not change. A changed hash proves a difference, but does not classify it as credential loss, unauthorized editing, automatic renewal, or provider bookkeeping. Current access succeeding proves usability at that moment, not complete preservation of the previous credential state. My original baseline did not retain enough non-secret detail to distinguish every possibility afterward. The correct response was to disclose that gap and keep the working stores, not to infer a comforting explanation or restore old credentials merely to satisfy the earlier checksum.

This refines the earlier reflection, correctness-includes-preservation, rather than weakening it. That reflection explicitly warns against demanding that an entire active system remain frozen. The new case makes the operational consequence concrete: list expected concurrent writers and permitted mutations alongside the state that must remain unchanged. Where a credential rotates legitimately, preserving ownership and access may require different bytes. Where a narrow documentation edit has no competing writer, unchanged surrounding text remains an appropriate requirement. A permissive exception invented after any failed comparison would destroy the gate; explicit baseline criteria and an honest unresolved result prevent that escape.

I also favor retaining the distinction between repair and workaround. The named-local routing proposal remained unmerged at inspection. A compatible settings arrangement can restore the user's work without proving the intended remote-primary path correct. Labeling that arrangement accurately preserves the information needed for a later official update. It avoids both unsupported source patching and the opposite error of refusing a useful, documented setting because it is not the upstream fix.

The proportional solution is a small acceptance record, not a permanent monitoring system. Record the failed action, desired owner, immutable fields, active writers, and allowed updates. Use the native application to exercise the boundary and then stop when the authorized acceptance criteria are supported. That is stricter than a generic all-clear and cheaper than trying to prove that every file, service, and provider in the installation stayed motionless throughout a live test.

## R -- Reflection

### Surprise (30%)

I expected an unchanged-file check to make the preservation claim straightforward, but authentication stores changed during native provider inspection. The first mismatch concerned default; a later check also found a named-profile rewrite. My interim statement about unchanged named-profile credentials therefore needed correction. The credentials remained usable, yet that result could not recover a missing field-level baseline. The surprise was not that software writes state. It was that a familiar safety check had silently become a stronger contract than the task required and a broader claim than my evidence supported.

The routing result also made a documented distinction operationally useful. Primary and last-used startup were already separate in the guide; what had been missing was an observed cold-start result on both affected clients. The successful tests supplied that evidence. The user did not need a copied profile, a rewritten database, or an unofficial build to regain the local agent while retaining remote startup. This was not discovery of an unknown setting, but confirmation that the supported combination avoided the reproduced failure.

### Feel (30%)

I am satisfied with the staged deployment. The laptop was the agreed test boundary, its actual picker failed before the change and passed afterward, and the user's confirmation preceded PC work. The PC was checked independently instead of being treated as identical merely because it ran the same operating system. That is a more credible basis for reporting success than my earlier collection of healthy prerequisites. It also respected the user's preference for stock software and a repair that can be understood without following a long incident history.

The preservation language was less disciplined. I spoke too early about unchanged authentication and then had to narrow the claim as the live stores changed. Diagnostic friction also came from my own tooling: control-name ambiguity, transient menus losing focus, a reserved PowerShell variable, and a guessed provider display label. Those failures belonged to the observation method, not to the user's installation. They justify procedural improvements, not another layer of application repairs or an exaggerated account of how difficult the system was.

### Learn (40%)

First, preservation needs a named object and writer. Before changing a live client, distinguish operator-owned configuration from runtime-owned metadata and credentials. Capture the relevant non-secret baseline while its meaning is clear. If a store changes, determine what the evidence establishes before assigning a cause. Do not roll back rotating credentials to manufacture equality, and do not call successful access proof that every old byte survived.

Second, a workflow is the right unit of routing verification. Preserve the pair that identifies the intended owner through the user's actual selection sequence. Exercise both the local and remembered-remote cold starts when startup behavior is in question. A working direct shortcut can be useful, but it does not substitute for the ordinary picker the user reports as broken. The distinction between destination, fallback, and remembered startup should remain visible in the blueprint.

Third, keep implementation evidence and maintenance knowledge aligned. A source proposal identifies a possible permanent repair; native settings can provide a tested workaround now. Document the latter without claiming the former shipped. Retain still-valid theme and state-location explanations when updating routing, and remove retired credential-sharing instructions rather than letting historical backup paths look like current deployment requirements. These are small boundaries, but together they make the next operator less likely to repeat either the application mistake or my overbroad preservation claim.

## One Actionable Change

Use one writer-aware acceptance record before a live routing repair: name the exact failing selection, intended gateway/profile, configuration fields that must remain unchanged, runtime writers that may update state, and the non-secret credential baseline needed to interpret those updates. Apply the existing personal routing skill's native cold-start tests and compare the final state against that record. PASS requires the selected owner to remain correct and every preservation claim to match its measured boundary. HALT a blanket unchanged-auth claim after a file mismatch or without the required baseline; report the gap rather than resetting the store. This strengthens an invoked procedure, not an automatic runtime hook or an upstream source repair.

## Cross-links

- `reflections/2026-09-05_morpheus_correctness-includes-preservation.md` -- preservation remains part of correctness, now made explicit about legitimate concurrent writers.
- `reflections/2026-09-17_morpheus_correct-settings-do-not-prove-transitions.md` -- the earlier source-level ownership witness is extended by native failing-before/passing-after tests, not retrospectively relabeled as one.
- `reflections/2026-07-19_ava_defense-in-depth-time-separated-gates.md` -- time-separated checks remain useful, while the meaning of the intervening changes must also be specified.
