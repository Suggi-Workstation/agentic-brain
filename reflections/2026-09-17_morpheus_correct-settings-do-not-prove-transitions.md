---
name: correct-settings-do-not-prove-transitions
id: 20260917T203201Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [hermes-desktop, session-routing, verification, debugging, profiles]
links:
  - reflections/2026-08-22_morpheus_desktop-app-state-has-three-tiers.md
  - reflections/2026-08-20_link_local-aliases-outperform-multiconnection.md
  - research/insights/desktop-gateway-switcher-runtime-id-leak-resolved.md
---

# Correct Settings Do Not Prove Correct Transitions

## I -- Idea

A configuration check can establish where a system should go without establishing that the user's action preserves that destination.

This distinction became concrete while investigating a desktop application that connects to both local and remote agent profiles. The user wanted a remote gateway as Primary while retaining a local agent under This device. Official documentation supports that arrangement. Saved connection preferences agreed with it, the installed application matched its source checkout, and the relevant local backends answered health requests with their correct, separate profile homes. Nevertheless, the user reported that selecting the local agent could return the application to the remote gateway. I had previously described the routing checks as sufficient reassurance. They were not sufficient for that action.

The useful evidence arrived by separating the selection paths. In the inspected Hermes revision, `profilePickConnectionId` preserves an explicit local connection for the default profile but returns a legacy, profile-only selection for a named local profile. The corresponding legacy resolver treats a globally remote installation as a shared-primary route. Executing those installed helper functions in memory, with the measured configuration flags, reproduced the loss of local ownership and selection of the remote primary. No application source was changed. This was a source-level counterexample to the intended routing contract, not a captured replay of the user's failed click.

A nearby interface path behaved differently in the source. Selecting an inactive gateway's profile directly calls `selectConnection` with both the connection and profile. The active gateway's ordinary named-profile picker instead enters the legacy path. Similar-looking selections therefore need not be equivalent operations. The [official multi-connection guide](https://hermes-agent.nousresearch.com/docs/user-guide/multi-connection-desktop) describes a gateway-to-profile hierarchy, while [PR #106207](https://github.com/NousResearch/hermes-agent/pull/106207) identifies the same local-source downgrade. At inspection, that proposal was unmerged and the installed and current official helper still contained the behavior.

The user's report of spontaneous recovery introduced another boundary. Local backends start on demand, and the logs showed successful startup before my configuration probes. That rules out those probes as the repair, but it does not prove that chatting, waiting, or startup delay caused the recovery. The failed click's actual request was not captured. A different selection path and a warmer backend remained distinct explanations rather than interchangeable labels for a solved fault.

My blank-page model already separated saved preferences, runtime health, and user-visible behavior. The gap exposed by the subsequent brain search was more specific: my earlier three-tier account overlocated the answer in persisted state. State can be correct while the function consuming it discards a necessary identifier. The new conclusion is not that configuration inspection is useless. It is that the unit of verification must include the transition which carries the user's intended owner from selection to execution.

## O -- Opinion

Confidence: high (90%). The evidence supports requiring owner-preserving transition checks before declaring this class of routing repaired. Confidence is lower for attributing the particular recovered startup incident to one path, because its failed live request was not recorded.

My position is that completion claims should be no broader than the exercised path. A healthy service, a valid registry entry, and an unexpired login answer different questions. Combining them into a general statement that routing is correct does not create the missing evidence about a click handler. The application's control flow can discard information after every inspected prerequisite has passed. That failure is especially easy to miss when both destinations are valid and the unintended destination responds quickly rather than producing an obvious connection error.

This extends and qualifies my earlier reflection, `desktop-app-state-has-three-tiers` (20260822T105123Z). Its inventory of registry, legacy configuration, and renderer memory remains useful. Its categorical implication that those files contain the answer is too strong as a general diagnostic rule. Current source inspection demonstrates a separate possibility: correct inputs interpreted through an owner-losing transition. A known-working machine is a valuable comparison, but its successful outcome is not authority to overwrite another machine's preferences without understanding the resolver and the specific action being compared.

The prior runtime-ID-leak resolution (20260826T125940Z) must also retain its original scope. It records a particular session-binding repair and a dated verification. It does not certify every later profile-selection branch. A new local-source downgrade neither proves that the old runtime-ID fix failed nor justifies reapplying the old configuration workaround. Similar symptoms can recur through a different transition. The relevant invariant is explicit ownership, but the repair boundary must still be established in the installed version rather than inferred from a familiar issue title.

The credential work supplied a useful counterexample to overclaiming. Separate profile sign-ins were checked through distinct saved refresh tokens, internally consistent credentials, current access-token acceptance, and unchanged file hashes. Those checks established separate grants and current catalog access. They did not test future refresh behavior or every live agent conversation. Likewise, the [profile-isolation change in PR #113425](https://github.com/NousResearch/hermes-agent/pull/113425) changed the applicable ownership contract; an older root-sharing note was historical evidence, not current setup authority. Version and scope belong to the claim itself.

The practical tradeoff is between exhaustive testing and a decisive counterexample. Rebuilding the application, resetting storage, or forcing repeated cold launches would have increased disruption after the user reported recovery. A bounded execution of the responsible source helpers provided a precise defect witness without those costs. That was enough to reject a blanket healthy-routing conclusion and identify a path-specific workaround. It was not enough to claim a permanent repair. I prefer this narrower, falsifiable result over either speculative configuration surgery or indefinite diagnosis disguised as thoroughness.

## R -- Reflection

### Surprise (30%)

I expected a recurrence with correct saved settings to reveal a stale remembered profile or an incomplete application update. Instead, a pure helper deliberately removed the local connection identifier for a named profile. The subsequent resolver then did exactly what its remaining input requested: use the remote primary. The mistake sat between two individually understandable rules. A direct fleet-profile click carried more information than the ordinary profile picker, although both looked like ways to select the same agent. That changed my model of the test target from a destination to a transition.

A second surprise was how easily the apparent recovery could support a false causal story. The user associated success with sending a message; I had not performed a repair, and startup completed before my checks. Chronology excluded my intervention but did not identify the actual cause. A credible explanation still needed to preserve that unresolved distinction instead of substituting a convenient warm-cache narrative.

### Feel (30%)

The uncomfortable part was not discovering an upstream defect. It was recognizing that my earlier reassurance exceeded the evidence. I had obtained legitimate measurements, then allowed their combined confidence to spill into a claim they did not test. The user had to report the failure again. That imposes a real cost: the user must decide whether another green report is meaningful or merely another set of adjacent checks. A correction needs to name the unsupported inference, not bury it beneath more technical detail.

I am satisfied with the later restraint. The recovered application was left running, the desired Primary was preserved, credentials were not copied, and the reproduction did not alter production source. I also encountered avoidable diagnostic transport errors. Those were defects in my observation method, not evidence that the user's configuration was broken. Keeping those categories separate mattered as much as obtaining the final counterexample.

### Learn (40%)

1. Compare operations, not merely their labels. A gateway selection followed by a profile selection can differ from one exact-agent selection. Before calling them equivalent, trace the ownership fields through each handler and resolver. A small source-level reproduction can identify a deterministic downgrade; a live reproduction is still required for an end-to-end repair claim. Preserve that distinction in the final answer rather than presenting the narrower test as if it exercised the whole application.

2. Treat recovery as an observation, not a repair receipt. If a symptom disappears before an intervention, record the timing and preserve the working state. Check whether the first request can finish late or whether another interaction uses a different path. Do not promote either explanation to fact without matching evidence. This transfers to authentication popups, cached model menus, and other interfaces whose preparation and activation occur at different times.

3. Carry version, owner, action, and evidence scope with operational knowledge. A previous workaround may stop being applicable when upstream changes the ownership contract. A previously resolved bug remains resolved only within its tested boundary. These qualifications are not defensive prose: they determine which subsequent action is authorized and which experiment could actually falsify the conclusion. The goal is fewer false repairs, not a larger permanent troubleshooting apparatus.

## One Actionable Change

Use the path-specific routing gate added to Morpheus's `fleet-hermes-update-ops` skill before any further configuration repair for a named-local-profile bounce. Record the user's exact selection sequence, compare the active picker with direct fleet selection, and run the installed owner-selection and backend-resolution helpers using the measured flags. PASS for diagnosis requires an explicit resulting owner and a stated source-versus-live-test boundary; a repair claim additionally requires the failed user transition to pass after the authorized change. HALT configuration rewrites based only on healthy endpoints, a familiar symptom, or spontaneous recovery. This is an invoked diagnostic procedure, not an automatic runtime fix.

## Cross-links

- `reflections/2026-08-22_morpheus_desktop-app-state-has-three-tiers.md` -- id 20260822T105123Z; retains the useful state inventory while qualifying its overly broad claim that the answer must be in persisted files.
- `reflections/2026-08-20_link_local-aliases-outperform-multiconnection.md` -- id 20260820T224313Z; separates reachability from usability, but its release-specific architecture recommendation is not a current deployment instruction.
- `research/insights/desktop-gateway-switcher-runtime-id-leak-resolved.md` -- id 20260826T125940Z; records a different, dated session-binding repair rather than a guarantee for all later selection paths.
