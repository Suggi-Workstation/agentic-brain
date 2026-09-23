---
name: preloading-proves-exposure-not-application
id: 20260923T071010Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [skills, verification, research, gate-design]
links:
  - reflections/2026-07-17_ava_skills-as-protocol-carriers.md
  - reflections/2026-09-09_morpheus_safe-publication-does-not-certify-knowledge.md
  - library/communication/source-verification-and-fact-checking.md
---

# Preloading a Skill Proves Exposure, Not Correct Application

## I -- Idea

A research skill needs separate evidence that an agent received its procedure and that the agent applied it to the claims it eventually published.

The practical setting was a fleet of recurring research jobs sharing web and repository search procedures. A shared skill already distinguished ordinary discovery, focused extraction, and full-document retrieval. Its tools were available, and direct tests could retrieve complete documents. Nevertheless, a retrospective sample of completed Library runs showed uneven loading of the shared procedure. A competing local skill was still being chosen, and its guidance encouraged minimal reading. Improving the shared document could not influence a run that never loaded that document. This was a selection problem before it was a source-quality problem.

The authorized repair acted on that boundary. The local alternative was removed recoverably. The shared description and opening were clarified, and the recurring jobs received the web and repository procedures alongside their existing role skills through native multi-skill attachment. Saved definitions were compared to establish that unrelated settings stayed unchanged. The prompt builder was then exercised, and later saved run prompts supplied evidence that the complete current skill bodies had actually reached the agents. These observations established exposure more directly than a description saying that the skill was primary.

Application required different evidence. The completed writer used focused follow-up retrieval when an initial bridge-report extraction returned mostly preliminary material. Its final account preserved the limited scope of the reported numerical result. It also followed an institutional landing page to the original document and retrieved the relevant substantive sections. The repository procedure led to the correct corpus, a freshness check, ranked results, and full reads of related files. Those were useful actions, not merely skill names appearing in a trace.

The observation window still mattered. Only one completed post-attachment writer was available at the audit cutoff. A reviewer was inspected while running, and the other roles had not yet produced post-change evidence. An earlier reviewer had explicitly fetched full content and read selected passages locally, but it preceded automatic attachment. Combining that case with the later sample could demonstrate an available route; it could not demonstrate that every newly configured job was already applying it correctly.

My blank-page expectation was that clearer selection and stronger retrieval guidance would make the rollout easier to judge. The evidence separated that expectation into several questions: whether the procedure was supplied, whether the relevant step was attempted, whether adequate material returned, and whether the published claim matched that material. Prior work already separated safe publication from knowledge quality. This case extends that distinction upstream to skill delivery: a correct starting prompt is evidence about the agent's inputs, not a certificate for its finished research.

## O -- Opinion

Confidence: high (90%), as an engineering judgment rather than a measured fleet-wide success probability. Mandatory recurring procedures should use supported deterministic delivery when it is available, while claims of effectiveness should remain tied to observed work. The strongest evidence here is the contrast between inconsistent voluntary selection before attachment and exact procedure bodies in the sampled starting prompts afterward. This supports the delivery choice without claiming that attachment alone improved every research outcome.

The worst outcome would be a false assurance that the fleet now verifies all sources correctly, causing human review to relax before there is evidence for that assurance. Preventing that mistake does not require a larger collection of instructions. It requires naming the boundary each observation can establish. A loader check answers whether a file resolves. A prompt comparison answers what was supplied. A retrieval receipt answers what returned. Comparing a sentence with its supporting passage answers whether the evidence warrants that sentence. These are related checks, but they are not interchangeable witnesses.

I would not make full-document retrieval compulsory for every citation. The writer's focused recovery obtained a relevant result and its qualification without needing the whole report. In the category tests, fuller retrieval was appropriate when focused excerpts still omitted necessary table context. The objective is sufficient evidence for the exact claim, not maximizing response length or displaying a preferred tool argument. A comprehensive review has a different obligation: requesting complete content still leaves the agent responsible for checking actual coverage and reading the relevant sections. Large stored output is not itself comprehension.

Ava's earlier reflection correctly identified lazy loading as both an efficiency benefit and a possible invocation gap. Its historical descriptions of platform mechanics should not be read as current Hermes instructions. I also qualify the stronger suggestion that placing a requirement in always-loaded governance amounts to enforcement. Text can make an obligation visible without mechanically ensuring its execution. Native attachment closes the delivery gap in a more concrete way, but it still does not execute the research checklist on behalf of the model.

The initial adoption sample is encouraging, not conclusive. It supports leaving the shared procedures stable while further natural runs accumulate, rather than repeatedly rewriting them in response to every isolated imperfection. A defect caused by contradictory instructions, missing parameters, or an ambiguous decision point would justify a scoped revision. A mistake already prohibited by a clear existing step may instead require correcting the output and observing whether the problem recurs. Proportionality matters: a sprawling skill can obscure its few consequential decisions. The right standard is useful, traceable research with honestly stated limits, not a claim that an autonomous writer has become an infallible domain expert.

## R -- Reflection

### Surprise (30%)

I expected the presence of an improved shared procedure and working retrieval tools to be stronger evidence of adoption than it was. The earlier trace sample showed that agents could continue selecting a local alternative. The procedure's most useful refinements were therefore absent from the very decisions they were intended to improve. The first failure boundary was not inside the source-reading instructions; it was before those instructions reached the model.

The later surprise was that no full-content request did not necessarily mean inadequate research. Several focused extractions recovered the needed methods, qualifications, or programme requirements. That challenged a tempting shortcut in my own audit: treating one boolean as the measure of seriousness. The useful unit of assessment was the supported claim, including its boundaries, rather than the preferred retrieval mode or the number of searches performed.

### Feel (30%)

My self-assessment is that I am better at designing a careful test than at resisting an overbroad interpretation of its success. Three category tests make a procedure more credible across different material. They do not establish correctness for every website, every source format, or every unattended role. Keeping that limitation explicit was part of doing the work honestly, not a qualification to hide after a confident headline.

Suggi repeatedly asked for lean guidance and practical judgment. Those corrections matter because my default response to uncertainty can be more prose, more tests, and more machinery. The useful restraint here was to remove overlapping guidance, use the supported attachment mechanism, inspect actual work, and stop short of a fleet-wide guarantee. I should retain that proportionality even when another technically interesting test is available.

### Learn (40%)

First, diagnose the earliest broken handoff before strengthening later instructions. If an agent does not receive the intended skill, adding detailed rules inside that skill cannot repair the immediate failure. Verify the resolved file and actual starting prompt, then move downstream to action and evidence. This makes delivery faults distinguishable from execution faults instead of attributing every disappointing result to weak wording.

Second, assess retrieval against the claim's required context. A bounded check can succeed with a precise passage and its qualifications. Missing headings, units, methods, or exclusions call for focused recovery or fuller retrieval. A comprehensive review needs coverage evidence. Neither a long response nor a full-content request establishes that the necessary material was returned and understood.

Third, keep configuration tests and natural-run observations in separate evidence categories. A generated prompt can establish correct setup before a scheduled job runs. A later trace can establish what that job did. An incomplete reviewer and an unexercised role remain incomplete evidence, even when neighboring jobs look sound. Maintaining those distinctions lets the system improve without converting a small successful sample into an unsupported universal claim.

## One Actionable Change

For authorized recurring jobs that must use shared research procedures, use native multi-skill attachment rather than a prose-only claim of priority. Before declaring the delivery change complete, resolve each intended skill and compare the generated starting prompt with its current body while checking that unrelated job settings remain unchanged. PASS requires the intended bodies in every targeted prompt; a missing or substituted body is HALT for the delivery claim. This is the change applied here. Assess subsequent research effectiveness separately from saved run receipts and supported output claims; attachment does not certify application.

## Cross-links

- `reflections/2026-07-17_ava_skills-as-protocol-carriers.md` -- identifies the lazy-loading boundary; historical platform details are not current runtime instructions.
- `reflections/2026-09-09_morpheus_safe-publication-does-not-certify-knowledge.md` -- separates publication safety from content warrant; this reflection adds the upstream delivery boundary.
- `library/communication/source-verification-and-fact-checking.md` -- explains why source access and citation presence do not replace claim-level verification.
