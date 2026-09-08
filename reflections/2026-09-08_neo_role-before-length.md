---
name: role-before-length
id: 20260908T154338Z
tier: reflection
trigger: session-end
author: Neo
tags: [frameworks, verification, separation-of-concerns]
links:
  - reflections/2026-08-19_neo_templates-vs-frameworks-separation.md
  - research/insights/rules-need-gates.md
  - investing-hub:frameworks/simple-moat.md
  - investing-hub:frameworks/simple-dcf.md
---

# Simplicity Requires Separating Document Roles, Not Removing Analysis

## I -- Idea

A useful investing documentation system separates the purpose of an analysis from its executable procedure and makes the required result visible before adding explanatory detail.

The session began with reusable investment analysis tools and moved through several corrections before settling on a different structure. Suggi wanted simple, self-contained procedures, not a library of elaborate rules. I initially treated additional research and numerous safeguards as sufficient evidence of quality. The user repeatedly clarified that the final artifact needed a narrow purpose and a small result. For the general DCF, the calculation needed to accept a selected metric, use the requested discount convention and produce separate scenario values. Research background, source lists and references to an uploaded workbook were not part of that procedure's intended interface.

The next correction showed that shortness was not the entire requirement. Initial moat and management procedures were too skeletal. The replacement needed useful questions about competitive forces, stewardship, financial resilience and industry-specific measures. The resulting Investing Hub files therefore became fuller procedural blueprints, with evidence requirements and compact output tables, while the sector document remained a selection guide rather than a verdict. This was not a request to remove difficult analytical questions. It was a request to prevent those questions from producing an unbounded essay or competing instruction system.

A later audit exposed duplication in the core guidebook. FRAMEWORKS.md still contained an older discount-rate construction, numerical scoring thresholds and a description of the bear scenario as a floor. Updating the links alone did not make those rules consistent with the replacement procedures. I identified that distinction rather than silently rewriting a locked core file beyond the link-edit authorization. Suggi then explicitly authorized the guidebook rewrite. The core file became descriptive, the detailed calculations remained in Investing Hub, and a short boundaries section was restored without resurrecting the old formulas.

My blank-page understanding before the closing review was that the failure concerned excessive complexity and slow execution. The unresolved questions were whether the replacement also needed less analytical coverage, whether a built framework counted as a completed company test, and whether earlier template separation remained the right architecture. Reviewing the actual artifacts, task board and previous reflection clarified those distinctions. Analytical coverage could increase while output remained constrained. Structural and arithmetic verification did not establish real-company usability. Separate files were useful only where their responsibilities differed, not merely because separate filenames appeared orderly.

The earlier reflection on templates and frameworks recorded a design that split methods from output specifications. The present design keeps the executable procedure and its output together, while separating the high-level guide from both. That is the specific architectural change being recorded, not a claim that every documentation system should collapse its templates or that every earlier analytical observation was wrong.

## O -- Opinion

Confidence: high (90%). The role separation is supported by explicit user corrections, the reviewed files and observed contradictions; its effect on future research speed still needs a real-company test.

My position is that an artifact should be evaluated against its job before it is evaluated against its length. A core guidebook explains the investment sequence, the questions worth asking and the limits of the agent's role. It does not need a second copy of the scoring bands or valuation formulas. A procedural framework must be specific enough to execute, including how to handle uncertainty and what the completed result looks like. A research note preserves evidence, reasoning and limitations. Treating those as interchangeable creates either bloated procedures or empty guidance.

The strongest evidence is the direction of the user's corrections. He rejected unnecessary explanation, then rejected procedures that were too thin, then requested descriptive prose in the core guidebook. These requests are compatible once artifact roles are separated. They only appear contradictory if simple is interpreted as a universal word limit or if every file is expected to explain the entire investment philosophy. I should have recognized that earlier instead of responding to each correction as an isolated formatting change.

There are important qualifications. A compact output cannot justify concealing a material assumption, an integrity concern or an imminent financing shortfall. Nor does a fixed discount convention make every business equally risky. The new procedures retain the distinction between evidence and judgment, and between economic results and accounting proxies. Their compact tables are reporting constraints, not exemptions from analysis. The moat framework, for example, can ask about each protective mechanism and each competitive force without producing a long corporate biography. The management framework can expose an integrity problem without pretending that an arithmetic average resolves it.

I also reject calling migration itself a completed investing experiment. The earlier Alphabet exercise used material that the user subsequently asked to delete. The current five-framework set has formatting, reference and synthetic arithmetic checks, but it has not yet been applied end to end as a complete set. Leaving that application as one clear task is more honest than clearing every old dry-run item as completed. The obsolete rate-comparison and template-dependent tasks can be retired because their premises changed; their retirement should not be described as a successful test.

This position revises my earlier separation reflection, identified by its stable identifier in the cross-links. The useful principle was avoiding duplicate responsibilities, not preserving one particular arrangement of files. The rules-need-gates insight supports the same conclusion: checks should verify the intended claim, not merely the existence of a document. I would reconsider this arrangement if company applications show that embedded output formats change independently so often that they again create duplication or confusion. Until that evidence appears, adding another layer would be speculation rather than simplification.

## R -- Reflection

### Surprise (30%)

I expected the user to prefer progressively shorter documents after rejecting complex frameworks, but he later asked for fuller questionnaires and broader analytical coverage. The surprise was not inconsistency in the request. It was that my own model of simplicity had only one dimension. I had collapsed scope, depth, presentation and document responsibility into length. Once separated, the corrections made sense: thorough research could support a compact answer, an executable procedure could be longer than a superficial checklist, and a descriptive guide could avoid formulas while remaining useful.

The reference audit revealed a second consequence. A live link can still point from text that describes a different method. Mechanical path checks passed after replacement, but semantic disagreement remained in the core guidebook. That made the necessary distinction concrete: referential validity and methodological agreement are different checks. Neither can stand in for the other, and a clean working tree proves neither by itself.

### Feel (30%)

The appropriate self-assessment is that I imposed unnecessary review work on Suggi. He had to repeat the distinction between procedure and background, and later explain why the core file should guide rather than duplicate calculations. The problem was not a shortage of tools or sources. It was allocating effort to the version of completeness I preferred instead of the result he had described. More research did not excuse that mismatch.

The useful part of the recovery was that the changes became concrete and inspectable. Old templates were actually removed after replacements were committed. Reference targets were verified, the detailed frameworks kept compact outputs, and the core rewrite occurred under explicit authorization. Those are supported accomplishments, not evidence that all future analyses will be correct. I do not need to turn the earlier failures into dramatic self-criticism; I need to preserve the operational distinction that would have prevented them.

### Learn (40%)

The durable lesson is to make document responsibility explicit before drafting. Purpose, procedure and supporting knowledge require different forms. The same instruction to keep something simple therefore produces different text in different locations. A guidebook can be descriptive; a procedure must be executable; a research note must preserve the basis and limitations of its claims. The completed result belongs near the procedure that produces it, so the analyst can see whether the work answers the intended questions.

A second lesson is that completion has distinct categories. Work may be completed, superseded, deferred or untested. Session-end cleanup must preserve those distinctions. Consolidating fragmented dry-run tasks makes the board more usable, but does not create evidence that the consolidated experiment succeeded. Likewise, a corrected knowledge note should identify which older prescriptions were superseded instead of letting historical material quietly remain an additional current instruction set.

Finally, the learning cycle should change the system without inventing a new governance layer. The core guide now references rather than duplicates procedures, the moat output has explicit fields, and the task board names a current application test. These changes address the observed failure class directly. Additional automation may be justified after that test, but neither another skill nor another checklist is valuable merely because a session has ended.

### One Actionable Change

Before editing an investment document, classify its role as descriptive guide, executable procedure or supporting knowledge, and identify its required output. Check the draft against that role before committing. PASS means the role and output match the human's request and detailed rules have one current home; HALT means the draft duplicates another role or omits the required result. This check applies the existing scope and duplication gates rather than adding a new core-governance rule.

### Cross-links

- `reflections/2026-08-19_neo_templates-vs-frameworks-separation.md` -- prior design, id 20260819T174217Z; revised here at the level of responsibility separation.
- `research/insights/rules-need-gates.md` -- checks must verify their claim rather than document presence.
- `investing-hub:frameworks/simple-moat.md` -- explicit questions and evidence fields with compact output.
- `investing-hub:frameworks/simple-dcf.md` -- calculation and scenario output without research background.
