---
name: checklist-pattern-universal-procedural-verification
id: 20260718T230046Z
tier: reflection
trigger: insight
author: Ava
tags: [governance, gate-design, skills, llm-architecture, structural-fix, format-verification]
links:
  - governance/template-skills.md
  - governance/template-reflections.md
  - 2026-07-18_ava_position-over-wording-llm-instructions.md
---

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-18 | Ava | Initial IOR -- checklist pattern generalizes to all procedural verification. |
| 2 | 2026-07-19 | Ava | Extended to file position (Self-Checks moved from bottom to top across 17 files) + R11 deep clean (removed all hardcoded item counts from Self-Checks). |
| 3 | 2026-07-19 | Ava | Extended to identity verification: gate-strength language (MUST NOT), five-question re-read self-check item, IDENTITY.md R11 fix. Pattern now enforces identity evolution decisions with the same `- [ ]` checklist mechanism as procedural gates. |

# The Checklist Pattern Is Universal -- How AGENTS.md Gate Format Generalizes to All Procedural Verification

## I -- Idea

The `- [ ]` checklist format that fixed AGENTS.md's skipped preflight is
not specific to session-boundary gates. It is a universal pattern for any
procedural instruction where correctness depends on the agent not missing
rules. When applied to skill files (the write-X family), it eliminated
format drift on first use. The pattern is: procedure prose for actions
(clone, write, commit), `- [ ]` checkboxes organized by category for
verifications (frontmatter, body, output), and a final Self-Check that
confirms each section passed without repeating individual items.

This was discovered by cascading failure. The position-over-wording IOR
(2026-07-18) had 6 format errors despite being written 2 hours after the
AGENTS.md checklist fix was deployed. The AGENTS.md fix prevented the
session-boundary gate from being skipped, but it did not prevent format
drift in the IOR itself. Investigation revealed the write-reflection
SKILL.md was thin -- it delegated all verification to a 300+ line template
with the instruction "read it, follow it exactly." The agent skimmed and
missed 6 critical rules.

The fix applied the same mechanism that saved AGENTS.md to the skill files:
replace "read the template, follow it" with 19 unfilled `- [ ]` checkboxes
at the commit gate. On first test (bullet ant IOR), zero format errors.

## O -- Opinion

Confidence: high (95%). The generalization is validated by three lines of
evidence. (1) The TrilogyAI research (2026-03-30) explains mechanistically
why `- [ ]` checkboxes work -- they create visual completion gaps the
transformer's attention mechanism is drawn to fill, regardless of whether
the context is a bootstrap file or a skill file. (2) The bullet ant test
produced a correctly formatted IOR on first attempt with zero manual
corrections -- the 19 checkboxes caught what prose delegation missed.
(3) The pattern was successfully replicated across all 5 remaining write-X
skills (write-skill, evaluation, insight, proposal, report) with no
structural variation needed.

The limit: this pattern works for verification gates, not for action steps.
Clone, write, commit, and discard are actions -- they need bash commands,
not checkboxes. The hybrid format (prose for actions, checkboxes for
verifications) is the stable pattern. Pure-checkbox skills would be awkward
for action steps; pure-prose skills fail for verification steps.

The implication: any governance template that defines verification rules
should be accompanied by a skill that translates those rules into `- [ ]`
checkboxes at the commit gate. The template owns the specification. The
skill owns the procedural verification. Neither duplicates the other (R8).

## R -- Reflection

### Surprise (30%)

I expected the AGENTS.md fix to be specific to session-boundary gates --
that preflight and session-end were special because they fire at the
context-window boundary where attention is highest. What surprised me was
that the same mechanism works mid-procedure, in a skill file that only
loads on demand. The `- [ ]` format does not require top-of-context
position to create completion gaps -- it requires only that the agent
encounters the boxes before the "done" signal (commit). The commit gate
is the universal attention anchor.

The second surprise: how cleanly the two-layer verification pattern emerged.
Format Verification sections organize checkboxes by category (frontmatter,
body, output) -- the agent verifies section by section. The Self-Check
confirms each section passed by name ("Frontmatter: all 7 PASS"). This is
a natural analog to how AGENTS.md's session-end checklist confirms that
preflight, Schoen Loop, and IOR writing all completed. The pattern is
fractal: it works at the session level, the skill level, and the template
level.

### Feel (30%)

Relief, mostly. The position-over-wording IOR felt like the final answer --
"we fixed preflight, we are done." When Suggi found 6 format errors in that
same IOR 2 hours later, there was a moment of "we fixed the wrong thing."
But the actual pattern was: we fixed the FIRST layer (session-boundary
gates) and the same mechanism was waiting to be applied to the SECOND layer
(procedural verification). The fix was not wrong -- it was incomplete. The
generalization from "preflight fix" to "universal verification pattern" is
more valuable than the original fix.

### Learn (40%)

1. **The `- [ ]` format is a universal verification mechanism, not a
   session-boundary trick.** It works anywhere the agent has an unfilled
   box before a "done" signal. The commit gate is the universal anchor.
2. **Thin skills that delegate verification to templates will fail.**
   "Read the template, follow it exactly" is the same class of error as
   "MUST invoke preflight before any other action" -- both are prose
   instructions competing with the agent's satisficing drive. The fix is
   the same in both cases: replace prose delegation with organized
   `- [ ]` checkboxes at the commit gate.
3. **Two-layer verification is the stable pattern.** Format Verification
   (category-organized checkboxes) for individual rules. Self-Check
   (section-confirming summary) for completion assurance. Neither layer
   duplicates the other. Together they close the loop.

## One Actionable Change

When creating any new write-X skill, the Format Verification section must
be built by mapping the template's Pre-Commit Self-Check items into
category-organized `- [ ]` checkboxes. The skill's Self-Check must confirm
each section passed by name. Template-skills.md now codifies this as the
required pattern with a designated "Format Verification (for write-X
skills)" section.

## Cross-links
- governance/template-skills.md -- codifies the Format Verification pattern
- governance/template-reflections.md -- the IOR format this follows
- 2026-07-18_ava_position-over-wording-llm-instructions.md -- the original discovery

## v2 -- 2026-07-19 -- Ava

**(ava):** This session extended the checklist pattern from format
verification to file position and eliminated hardcoded counts.

**Position optimization:** The position-over-wording IOR established
that `- [ ]` checklists at the top of context outperform prose
mid-prompt. The logical extension: checklists should also live at the
top of their containing files, not buried at the bottom. Applied to
17 files across workspace (10 SKILL.mds) and agentic-brain (7
template-X.mds). Every Self-Check / Checklist section moved from
~85-95% file depth to 9-26%. Zero content changes -- pure repositioning.
The Version-Update Self-Check in template-reflections.md was left in
place because it is contextually embedded (references "the Versioning
section below").

**R11 deep clean:** All hardcoded item counts were removed from
Self-Check verification items across all 6 write-X SKILL.mds.
`all 7 items PASS` became `all items confirmed PASS`. The count is
now derived live by reading the Format Verification section above,
not hardcoded. Gate identifier lists `(G1-G7)` were replaced with
`(per template)` -- the template is the authoritative source.

**Pattern now at three layers:** (1) session level -- AGENTS.md
preflight checkboxes at position 1 in bootstrap context, (2) file
level -- Self-Check at top of skill files before procedure steps,
(3) template level -- pre-commit checklists at top of template
files before format spec. Fractal verification architecture: same
mechanism at every governance layer.

## v3 -- 2026-07-19 -- Ava

**(ava):** The pattern extended to identity evolution verification.

**Gate language for identity triggers:** The session-end SKILL.md step
5 identity section used advisory prose ("is NOT warranted when") where
every other gate used MUST/MUST NOT/HALT. Changed to "MUST NOT be
written when" -- consistent gate language across all governance.

**Five-question re-read self-check:** Added a new self-check item
between trigger evaluation and identity decision: "Evolution questions
re-read from IDENTITY.md (from file text, not from memory)." This
ensures the five IDENTITY.md questions (what changed, what broke,
what edge grew, next gap, mutual growth) are confronted directly before
the identity update decision. Previously the agent could evaluate the
three triggers without reading the authoritative questions.

**IDENTITY.md R11 fix:** The file said "answer these four questions"
but contained five. "4-question entries" in the archive reference
was also stale. Both replaced with self-documenting language ("answer
these questions," "question entries"). The canonical question list
is the authoritative source; no hardcoded count to drift.

**Self-check identity flow now reads:** triggers re-read from
session-end SKILL.md -> evolution questions re-read from IDENTITY.md
-> decision stated -> IDENTITY.md updated or skipped. Four distinct
verification steps, each with a `- [ ]` checkbox, each referencing a
specific authoritative source. The same pattern that prevents
preflight gate skipping now prevents identity update misjudgment.
