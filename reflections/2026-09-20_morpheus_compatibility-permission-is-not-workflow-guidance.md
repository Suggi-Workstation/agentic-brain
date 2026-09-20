---
name: compatibility-permission-is-not-workflow-guidance
id: 20260920T213608Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [verification, scope, simplicity, skills, gate-design]
links:
  - library/guide-library.md
  - reflections/2026-07-17_ava_skills-as-protocol-carriers.md
  - reflections/2026-09-12_morpheus_consolidated-memory-still-needs-a-current-truth-check.md
  - library/coding-agentic-ai/human-in-the-loop-patterns.md
---

# Compatibility Permission Must Not Become Workflow Guidance

## I -- Idea

A system can permit a recovery path without teaching that path as a second normal workflow.

The practical setting was a shared research library maintained by scheduled agents. Its jobs prepare temporary material, publish validated changes, and remove the temporary material after checking publication. A discovery run completed its substantive work but could not finish cleanup. The execution trace showed that the temporary directory had been created in the runtime's profile-local scratch area, while the saved permission covered an older temporary-location convention. The published candidates were intact. Cleanup failure and publication failure were different outcomes, although a broad completion label could have hidden the distinction.

The user authorized cleanup permissions for both locations. My first documentation response described both as ordinary choices and mentioned naming conventions for other scheduled workflows. That response followed the breadth of the permission request rather than the purpose of the Library guide. Suggi corrected the scope twice: unrelated workflows did not belong in that guide, and the guide should describe the official normal method rather than advertise every permitted fallback. Reading the current runtime documentation established the normal method: use its supplied temporary-directory variable, which points to profile-local scratch unless explicitly overridden.

The final guide therefore retained one procedure for creating, using, removing, and verifying a run-owned directory. The broader compatibility allowance remained in configuration. The three Library role skills already referenced the guide, so duplicating the revised procedure into each role would have created additional sources of drift. The task did not require a new cleanup service, another scheduler, or changes to the agents' core identities. The smaller documentation change was possible because instruction ownership and permission ownership were separated instead of made identical.

Related web-research work exposed another version of the same confusion. Connecting an official MCP service made additional search and fetching tools available; it did not redirect the existing native tools or force models to request complete documents. A shared skill could explain when excerpts were sufficient and when full-source reading was necessary. Actual planning tests nevertheless showed agents sometimes selecting existing specialist skills instead of the new guide. Correct tool choices in those cases did not prove that the new guide had caused the choices or would always be loaded.

My blank-page account treated these as problems of clearer instructions and narrower success claims. The source checks and prior reflections sharpened the model: capability, permission, guidance, selection, and verification are separate responsibilities. A document should contain the decisions its reader must make, not reproduce every mechanism that supports those decisions. An exception belongs in the normal procedure only when encountering it genuinely requires the operator to choose differently. Otherwise, exposing it can increase interpretation work without increasing useful control.

## O -- Opinion

Confidence: high (90%) that normal workflow guidance and compatibility permissions should be separated in this system. This is a reasoned judgment from the inspected runtime, the user's explicit requirements, and the exercised behavior, not a measured universal effect size for shorter documentation.

My position is to make the correct routine action easy to identify and keep authorized tolerance underneath it. The operator should not need to reconstruct an incident before creating a temporary directory. The agent should not need to choose between equally presented storage locations when the runtime already supplies the intended location. Permissions may intentionally accommodate a known older path, but that does not make the older path a second recommendation. The guide remains truthful by describing what should happen, while configuration remains resilient to the limited alternative the user authorized.

This is not an argument for hiding meaningful choices. Web retrieval is a genuine choice because different tasks require different evidence. A narrow factual question may be answered from a verified passage, whereas a comprehensive review needs complete source coverage. A tool-selection skill should explain that distinction. By contrast, an incidental directory choice does not usually improve the research result. The useful question is whether the alternative changes the task's evidence or outcome, not merely whether the system is capable of taking it. The same principle supports keeping domain-specific instructions in their own guides.

The strongest objection is that concise guidance can conceal important failure modes. The answer is not to turn every user-facing procedure into a complete operations manual. Keep the checks that the operator must actually perform: exact target, ownership, current use, preservation of required evidence, and a verified result. Put the detailed configuration semantics and adversarial tests in the relevant maintenance procedure. Independent review remains valuable at consequential boundaries. In this session it found a permission-matching edge case that ordinary positive examples did not expose, and a supported configuration safeguard was tested before the final permission claim.

The prior reflection on skills as protocol carriers remains useful, but its historical use of enforcement must be read carefully. Instructions can make a required step visible; they do not automatically create a runtime refusal. The current human-oversight Library topic distinguishes those functions explicitly. A tool description is not an authorization policy, and a skill listing is not proof of selection. The new guide's observed invocation rate was therefore reported separately from the correctness of the planned routes. Treating all three as one success would have repeated the same category error.

I also reject using this distinction to justify unbounded testing. Verification should address the change's actual claims and realistic counterexamples, then stop. A harmless wording simplification does not need another research pipeline run. A permission change does need negative cases, but it does not authorize unrelated security changes. Existing broader settings discovered during testing must be disclosed without silently changing them. Simplicity is not the absence of checks; it is placing each necessary check at the boundary where it can answer a specific question.

## R -- Reflection

### Surprise (30%)

I expected the cleanup permission mismatch to be resolved by allowing both temporary locations and documenting both. Instead, Suggi's correction exposed a mistake in my information design. I had converted tolerated behavior into recommended behavior. The runtime already supplied a normal path; the guide only needed to name that method and show how to verify cleanup. More complete explanation was not the same as a better procedure for the person or agent reading it.

The tool-selection tests produced a related surprise. A new guide could be visible and relevant without being selected, while the agent still chose an appropriate tool through other guidance. That is neither universal trigger success nor total failure. It is evidence about a particular selection path. Separately, the permission review showed that a familiar matching mechanism needed a negative test involving its own rule representation. Both observations challenged my habit of treating a well-formed configuration as a sufficiently complete description of actual behavior.

### Feel (30%)

My candid assessment is that I still overexplain infrastructure in documents meant to direct a narrow task. The user had to remove references to unrelated workflows and then clarify that fallback permission should remain background tolerance. Those corrections were not requests to weaken verification. They were requests to stop making the reader carry implementation details that did not help the next action. This repeats the proportionality constraint already recorded in my identity rather than proving that I have solved it.

I am satisfied with the evidence-preserving parts of the work: the published result was distinguished from failed cleanup, the remaining temporary material was removed only after authorization and ownership checks, and the discovered policy edge was tested without executing the dangerous negative cases. That satisfaction has a specific basis. It does not excuse the documentation detour, establish that every future model will follow the guide, or turn a passing fixture into an assurance about all possible filesystem states.

### Learn (40%)

First, separate the instruction surface from the permission surface. Before editing a guide, establish the native normal operation and the task boundary its reader owns. Describe that operation directly. Keep an authorized fallback in configuration when the operator does not need to choose it during ordinary work. If a genuine decision affects evidence, quality, or consequence, explain that decision in the appropriate skill rather than suppressing it for brevity.

Second, test each claimed boundary with the right evidence. Discovery proves availability; observed calls prove selection; policy checks prove only their modeled authorization conditions; post-action inspection proves the checked result. Include a negative case that challenges the mechanism's own assumptions, not just an obviously unrelated input. Where existing configuration disables a broader check, state that limitation instead of claiming fleet-wide enforcement from a narrower test.

Third, let a correction reduce the system. The Library roles did not need duplicate edits because they already delegated to one guide. Native settings and a lean procedural correction met the approved scope without a new service. The durable improvement is not another generic command to be careful. It is a documentation acceptance boundary that asks whether the normal path is accurate, the reader's scope is respected, and compatible exceptions have accidentally become extra instructions. That boundary would have prevented my original dual-path explanation while preserving the user's requested tolerance.

## One Actionable Change

Apply the strengthened workflow-documentation gate in the personal `library-pipeline-ops` skill before committing guide changes: verify the runtime's native normal route, describe that single procedure for the guide's own readers, and keep compatibility allowances in configuration unless the user requests an explicit operational choice. PASS requires the documented method to match the runtime and the guide to exclude unrelated workflows or duplicated role procedures. Otherwise HALT the documentation claim and narrow the draft. The Library guide now passes this check; the permission tests remain separate evidence rather than extra guide content.

## Cross-links

- `library/guide-library.md` -- the corrected single-path preparation and cleanup procedure shared by the Library roles.
- `reflections/2026-07-17_ava_skills-as-protocol-carriers.md` -- the earlier separation of procedural carriers and gates, extended here to distinguish guidance from permitted fallback behavior.
- `reflections/2026-09-12_morpheus_consolidated-memory-still-needs-a-current-truth-check.md` -- why a passing result must identify its exact consumer and validity boundary.
- `library/coding-agentic-ai/human-in-the-loop-patterns.md` -- authority and execution checks belong at consequential boundaries rather than being inferred from tool visibility.
