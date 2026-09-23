---
name: refresh-must-preserve-the-cache-owner
id: 20260923T062902Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [verification, debugging, profiles, hermes-desktop]
links:
  - reflections/2026-09-17_morpheus_correct-settings-do-not-prove-transitions.md
  - reflections/2026-09-18_morpheus_preservation-must-name-the-writer.md
---

# A Forced Refresh Must Invalidate the State It Actually Reads

## I -- Idea

A forced refresh is trustworthy only when invalidation, retrieval, and presentation preserve the identity of the same logical object.

The triggering case was a desktop application displaying separate client and backend update indicators. The client showed pending commits while the backend displayed no corresponding count. The user knew that both installations needed updates and had already clicked the backend indicator repeatedly. The same behavior appeared on another computer connected to the shared backend. This was a precise failed operation, not a general request to explain how update checks work. Nevertheless, my first explanation emphasized an older profile-switch bug and the application's daily refresh interval. Those facts were relevant background, but they did not explain why the user's explicit refresh failed.

The subsequent investigation separated the source checkout, running service, displayed version, and update-check result. The source comparison established that updates really existed. Reading a current version label did not establish that the update-count cache was current, because the two values traveled through different paths. The backend's forced-check handler supplied the sharper explanation: it entered the selected profile's context to remove that profile's cache, then left the context before invoking the update checker. The reader could therefore use an untouched cache belonging to the process's default home. The cache selected for deletion was not necessarily the cache supplying the answer.

An isolated execution of the installed handler reproduced that identity mismatch while blocking filesystem mutation. The observed default cache contained a zero-update result from an earlier check. This supported the source-level diagnosis and the possibility that both clients would receive the same stale answer. It did not capture the authenticated response inside the user's running desktop application. That evidence boundary mattered: a causal witness in the handler is stronger than an age-based guess, but it is still not a complete observation of the original click, network request, and rendered result.

A second correction concerned upstream awareness. Searches initially found no dedicated report of the precise regression. Reading the introducing pull request's inline review revealed that a contributor had already described the same scope error before merge. The distinction between an issue, an ordinary discussion comment, and an inline review changed the answer from apparently unreported to reported but not demonstrated fixed. No amount of confidence in a narrow search could substitute for checking the surface where the evidence actually lived.

My blank-page understanding already separated healthy settings from working transitions. Reading the prior transition and writer-aware preservation reflections sharpened the missing invariant: a maintenance operation can preserve its selected profile long enough to perform one step correctly, then lose it before the next step consumes state. The relevant object is not merely the request or the cache file. It is the owner-qualified invalidation-and-read pair across the entire operation.

## O -- Opinion

Confidence: high (90%). The investigated source and bounded reproduction support an owner-preserving refresh gate. Confidence is lower for attributing every instance of the user's missing indicator to that one handler without the original authenticated client trace.

My position is that a failed explicit refresh deserves precedence over a generic caching explanation. The user had already supplied the discriminating observation: the action that previously refreshed the count no longer did so. Recommending the same action as an untried remedy failed to incorporate that evidence. It also shifted work back to the user without changing the hypothesis. A better response begins by recording the operation that failed and identifying which part of its contract a new observation could actually test. This does not require assuming that every reported detail is a proven mechanism; it requires treating the report as the test case rather than replacing it with a more familiar complaint.

The cache-scope mismatch demonstrates why a successful substep cannot certify a transaction. Deleting a file can succeed under the intended profile while the following read succeeds under another profile. Both steps can return ordinary results, leaving no obvious exception. A boolean named force does not repair this separation. The useful comparison is between the effective home, resource path, cache key, and account or connection identity at invalidation and at retrieval. Where work moves into a thread or exits a context manager, the comparison must follow that transition rather than stop at the presence of a scoping helper.

This extends the earlier reflection on correct settings and incorrect transitions rather than superseding it. That reflection showed a picker losing the connection identifier before backend resolution. Here, the selected owner survived one meaningful operation and was lost before another. The writer-aware preservation reflection contributes a complementary constraint: diagnostics must not clear production caches or rewrite live credentials simply to manufacture a clean comparison. A read-only witness can disprove an assumed invariant while preserving the user's working state. Repair still requires separate authorization and an acceptance check through the affected surface.

The upstream search correction imposes the same discipline on knowledge. A negative conclusion must name its search boundary. No matching standalone issue is a supportable report after searching issues; nobody has reported this is a much broader statement. Inline reviews, linked replacement pull requests, and current code can reverse that conclusion. The appropriate improvement is a bounded expansion into those relevant surfaces, not an unlimited search of every discussion or a promise that a contributor's priority annotation means a maintainer has scheduled a fix.

I favor keeping these requirements in the invoked troubleshooting procedure. A private application patch, permanent monitor, or new shared service would not follow from this evidence alone. The smallest useful structural change is to require identity-matched cache checks and source-complete upstream review before diagnosis and recommendation. It prevents the original reporting errors without pretending to fix the upstream software or make every future investigation automatic.

## R -- Reflection

### Surprise (30%)

I expected clicking the backend label to distinguish a stale automatic check from a deeper fault, but the user had already performed that experiment. The surprising result was that force could still reuse stale data without the deletion step itself failing. The handler's context lifetime was sufficient for one operation and insufficient for the transaction. Two computers repeating the same symptom made shared-backend investigation more informative than separate client reinstallations, although their agreement alone did not prove the backend mechanism.

I also expected a precise issue search to establish whether the regression was known. Instead, the strongest matching report was an inline warning on the change that introduced it. The evidence was not absent; my search boundary excluded it. That was a useful counterexample to treating a successful retrieval tool call as a complete investigation. It changed both the technical explanation and the appropriate recommendation for upstream follow-up.

### Feel (30%)

The uncomfortable part was asking the user to repeat a step they were already emphasizing. My explanation had become organized around a plausible model of normal caching rather than around their failed action. That is not corrected by adding more jargon about intervals or refresh buttons. The correction is to state what the new evidence excludes, trace the next relevant boundary, and acknowledge which earlier claim was too broad.

I am satisfied with the later restraint. The diagnosis did not become permission to patch the application, clear authentication stores, reinstall clients, or restart a shared service. The handler witness and upstream review were enough to improve the answer. I also explicitly separated that source evidence from an authenticated desktop capture that I did not have. Those limits are useful engineering information, not an excuse to dilute a concrete finding into uncertainty about everything.

### Learn (40%)

First, preserve object identity across maintenance operations. When a request invalidates, reloads, migrates, or refreshes state, compare the effective owner and key at every consumer boundary. A successful deletion followed by a successful read can still violate the intended operation. This applies beyond caches to configuration reloads, tenant-scoped credentials, index generations, and account-specific model discovery. The comparison should be small and explicit enough to test without rewriting unrelated state.

Second, let the user's failed action narrow the experiment. A known issue with a similar label is only a candidate until its trigger and control flow match. Record whether the user has already tried the proposed discriminator. A repeated recommendation is not progress when it produces no new evidence. Prefer a bounded inspection of the shared path when independent clients fail against the same resource, while retaining client-specific alternatives until the evidence rules them out.

Third, make negative research conclusions conditional on the inspected surfaces. A closed original proposal can have shipped through a replacement, and a merged change can contain an unresolved inline warning. Read the relevant review and actual current implementation before claiming unreported or fixed. These checks improve the recommendation without granting authority to apply an unmerged patch or promising that upstream will act on a particular schedule.

## One Actionable Change

Apply the strengthened Client/backend update-badge mismatch and Upstream issue recency gates in Morpheus's fleet-hermes-update-ops skill before the next forced-refresh diagnosis. Record the exact failed action, compare invalidator and reader home/path/key through the worker boundary, and inspect the introducing change's inline reviews before a negative report claim. PASS requires matching resource identities or an explicit mismatch witness, plus a stated source-versus-live evidence boundary. HALT an explanation based only on cache age, a force flag, or an issue-title search. This is an invoked diagnostic gate, not an automatic runtime repair.

## Cross-links

- `reflections/2026-09-17_morpheus_correct-settings-do-not-prove-transitions.md` -- extends transition-level ownership checks to a multi-step invalidation and retrieval operation.
- `reflections/2026-09-18_morpheus_preservation-must-name-the-writer.md` -- keeps diagnostic preservation tied to the actual owner and writer instead of clearing live state to simplify the test.
