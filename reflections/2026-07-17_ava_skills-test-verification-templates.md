---
name: skills-test-verification-templates
id: 20260717T151000Z
tier: reflection
trigger: milestone
author: ava
tags: [skills, testing, verification, write-proposal, write-evaluation, write-report, write-insight, templates]
links:
  - 2026-07-17_ava_skills-test-verification.md
  - 2026-07-17_ava_cold-start-verification-executed.md
  - governance/template-skills.md
  - governance/template-proposals.md
  - governance/template-evaluations.md
  - governance/template-reports.md
  - governance/template-insights.md
---

# i+o+r  verification protocol for the 4 template-writing skills (Ava)

## I -- Idea

Four template-writing skills were deployed to the workspace:
write-proposal, write-evaluation, write-report, and write-insight.
Each bundles its governance template in a references/ folder, following
the pattern established by write-reflection. Unlike the protocol skills
(preflight, loop-feynman, loop-schoen, session-end) which were tested
via warm (37/37) and cold-start verification, these writing skills are
user-invocable -- they are triggered explicitly when the agent writes
the corresponding document type.

This IOR defines per-skill verification checklists, in the same format
as `2026-07-17_ava_skills-test-verification.md`, to confirm:
- SKILL.md loads and has correct frontmatter.
- When to Apply sections correctly scope each skill.
- Format sections match the governing template's body structure.
- Quality gates are named (not just counted) and match the template.
- Pre-Commit Self-Check items match the template's checklist.
- Bundled template exists and is byte-identical to the live
  governance template in the agentic-brain.
- The skill is user-invocable with disable-model-invocation: false.

## O -- Opinion

Confidence: high (96%) that all 4 skills will pass. The write-reflection
skill set the pattern and passed both warm and cold-start verification.
These 4 skills follow the identical structure. The risk is lower than
the protocol skills test: these are user-invocable, not context-triggered,
so there is no "will the agent invoke it at the right time" ambiguity.
The agent reads the skill only when explicitly writing that document type.

The main failure mode is a copy-paste artifact: wrong frontmatter field
count in self-check vs. SKILL.md, quality gate name that diverges from
the template, or a self-check item missing from the template's checklist.
All four checklists below test these explicitly.

## R -- Reflection

### Surprise (30%)

The SKILL.md structure (Hard Gate, When to Apply, Format, Frontmatter
Rules, Naming Convention, Quality Gates, Pre-Commit Self-Check, Related)
is template-agnostic. Every document type fits this container. The only
differences are: frontmatter field counts (6 for proposals/reports,
7 for evaluations/insights which add `source`), quality gate names
(domain-specific), and self-check item counts (11-14 items). No
template required structural adaptation.

### Feel (30%)

Satisfied that the template ecosystem is now skill-covered. The four
governance templates each have a bundled skill carrying the condensed
procedure, quality gates, self-check, and reference template. This
extends the constitution-vs-procedure split to the writing domain:
every document type has an invocable skill.

### Learn (40%)

1. **Quality gates are named, not just counted.** Each skill's self-check
   says "All 7 quality gates (G1-G7) confirmed PASS" but the individual
   gate names are listed in the Quality Gates section. Naming prevents
   "count 7" from being the only check.

2. **Bundled templates eliminate network dependency.** A skill with its
   template bundled in references/ can be consulted without cloning the
   agentic-brain. The condensed procedure (SKILL.md) is the primary
   reference; the bundled template is for examples and edge cases.

3. **User-invocable skills are easier to verify than auto-triggered
   skills.** An auto-triggered skill like preflight or loop-feynman
   requires a full session to verify. A user-invocable skill like
   write-proposal can be tested on demand: read the skill, write a
   document, check the output. The verification surface is smaller.

## One Actionable Change

When exercising a writing skill, read the SKILL.md first (condensed
procedure), then consult the bundled reference template only for
examples or edge cases. This order is consistent across all 4 skills
and prevents consulting the 250-line template when the 150-line
SKILL.md contains the same procedure condensed.

---

## Master Checklist -- Static Checks (All 4 Skills)

Static checks apply to every skill. Run once at session start.

```
[ ] Skills directory exists
      Confirm: ls ~/.openclaw/workspace/skills/ shows:
      write-proposal, write-evaluation, write-report, write-insight
[ ] All skills have correct frontmatter
      Confirm: user-invocable: true, disable-model-invocation: false
      for all 4 SKILL.md files
[ ] All skills have descriptions under 160 bytes
[ ] All skills have references/ directories
      Confirm: each skill has references/ with the bundled template
[ ] All bundled templates byte-match governance templates
      Confirm: diff between skills/<name>/references/template-<name>.md
      and agentic-brain/governance/template-<name>.md is empty
```

---

## write-proposal -- Verification Checklist

Verification phase: when writing a proposal document.

```
[ ] Skill SKILL.md is valid
      Confirm: read ~/.openclaw/workspace/skills/write-proposal/SKILL.md
      has correct frontmatter (name: write-proposal,
      user-invocable: true, disable-model-invocation: false)
[ ] Frontmatter description is a trigger surface
      Confirm: description is task-oriented ("Write a proposal:
      Problem-Solution-Impact format with quality gates G1-G7,
      frontmatter schema, and cross-links."), under 160 bytes
[ ] When to Apply section is correct
      Confirm: lists proposal-specific triggers (problem needs
      approval, IOR surfaced a failure class, new capability
      proposed) and exclusions (minor fixes, status updates,
      evidence-less ideas)
[ ] Format sections match template-proposals.md
      Confirm: Problem, Proposed Solution, Impact (Positive/Risk/Cost),
      Open Questions, Approval Gate, Cross-Links -- all present
      and matching the template's body structure
[ ] Frontmatter Rules are correct
      Confirm: 6 fields listed (name, id, tier, author, tags, links).
      tier is "always proposal". Matches template-proposals.md schema
      exactly.
[ ] Naming Convention is correct
      Confirm: <short-slug>.md, kebab-case, max 60 chars.
      Example given. Matches template.
[ ] Quality Gates: G1-G7 named and matching template
      G1 Problem Is Specific, G2 Solution Is Concrete,
      G3 Impact Is Estimated, G4 Open Questions Surfaced,
      G5 Cross-links Exist, G6 Frontmatter Complete,
      G7 Formatting Rules.
      Confirm: all 7 names match template-proposals.md.
[ ] Pre-Commit Self-Check: items match template checklist
      Template checklist has 10 items. Skill self-check adds
      "All 7 quality gates (G1-G7) confirmed PASS" (11 items total).
      Confirm: every template checklist item appears in skill
      self-check. No items dropped. No items fabricated.
[ ] Bundled template exists and is byte-identical
      Confirm: references/template-proposals.md exists.
      diff against governance/template-proposals.md is empty.
[ ] Cross-references are correct
      Confirm: Related section links to write-evaluation and
      write-reflection skills. Links to bundled template and
      governance template.
```

---

## write-evaluation -- Verification Checklist

Verification phase: when writing an evaluation of another agent's work.

```
[ ] Skill SKILL.md is valid
      Confirm: read ~/.openclaw/workspace/skills/write-evaluation/SKILL.md
      has correct frontmatter (name: write-evaluation,
      user-invocable: true, disable-model-invocation: false)
[ ] Frontmatter description is a trigger surface
      Confirm: description is task-oriented ("Write an evaluation:
      Source-Criteria-Findings-Verdict format with quality gates
      G1-G7, decorrelation rule, and cross-links."), under 160 bytes
[ ] When to Apply section is correct
      Confirm: lists evaluation-specific triggers (another agent's
      work needs review, decorrelation rule) and exclusions (own
      work, already evaluated work, minor formatting). Decorrelation
      rule is prominently stated.
[ ] Format sections match template-evaluations.md
      Confirm: Source, Evaluation Criteria, Findings (Finding +
      Evidence + Judgment), Verdict (APPROVE/APPROVE WITH CHANGES/
      REJECT), Confidence -- all present and matching template.
[ ] Frontmatter Rules are correct
      Confirm: 7 fields listed (name, id, tier, source, author,
      tags, links). Includes source field. tier is "always
      evaluation". Matches template schema exactly.
[ ] Naming Convention is correct
      Confirm: <short-slug>.md, kebab-case, max 60 chars.
      Example given. Matches template.
[ ] Quality Gates: G1-G7 named and matching template
      G1 Different Agent, G2 Criteria Stated First,
      G3 Evidence Cited, G4 Verdict Is Explicit,
      G5 Confidence Included, G6 Cross-links Exist,
      G7 Formatting Rules.
      Confirm: all 7 names match template-evaluations.md.
[ ] Pre-Commit Self-Check: items match template checklist
      Template checklist has 12 items. Skill self-check adds
      "All 7 quality gates (G1-G7) confirmed PASS" (13 items total).
      Confirm: every template checklist item appears in skill
      self-check. Decorrelation rule item present.
[ ] Bundled template exists and is byte-identical
      Confirm: references/template-evaluations.md exists.
      diff against governance/template-evaluations.md is empty.
[ ] Cross-references are correct
      Confirm: Related section links to write-proposal and
      write-report skills. Links to bundled template and
      governance template.
```

---

## write-report -- Verification Checklist

Verification phase: when writing a research report.

```
[ ] Skill SKILL.md is valid
      Confirm: read ~/.openclaw/workspace/skills/write-report/SKILL.md
      has correct frontmatter (name: write-report,
      user-invocable: true, disable-model-invocation: false)
[ ] Frontmatter description is a trigger surface
      Confirm: description is task-oriented ("Write a report:
      Executive Summary-Research-Methodology-Findings format with
      quality gates G1-G7, evaluation history, and cross-links."),
      under 160 bytes
[ ] When to Apply section is correct
      Confirm: lists report-specific triggers (multi-step research,
      findings requiring methodology, structured output for
      evaluation) and exclusions (single-session IOR, library topic,
      unevaluated draft)
[ ] Format sections match template-reports.md
      Confirm: Executive Summary, Research Question, Methodology,
      Findings, Discussion, Conclusion, Evaluation History -- all
      present and matching template body structure in order.
      Evaluation History requirement is prominent.
[ ] Frontmatter Rules are correct
      Confirm: 6 fields listed (name, id, tier, author, tags, links).
      tier is "always report". Matches template schema exactly.
      Note: links MUST include evaluations.
[ ] Naming Convention is correct
      Confirm: <short-slug>.md, kebab-case, max 60 chars.
      Example given. Matches template.
[ ] Quality Gates: G1-G7 named and matching template
      G1 Independently Evaluated, G2 Executive Summary Stands Alone,
      G3 Methodology Is Reproducible, G4 Negative Results Included,
      G5 Cross-links Exist, G6 Frontmatter Complete,
      G7 Formatting Rules.
      Confirm: all 7 names match template-reports.md.
[ ] Pre-Commit Self-Check: items match template checklist
      Template checklist has 14 items. Skill self-check has 14 items
      (13 template items + "All G1-G7 confirmed PASS").
      Confirm: every template checklist item appears in skill
      self-check. Evaluation history and negative results items
      present.
[ ] Bundled template exists and is byte-identical
      Confirm: references/template-reports.md exists.
      diff against governance/template-reports.md is empty.
[ ] Cross-references are correct
      Confirm: Related section links to write-evaluation and
      loop-feynman skills. Links to bundled template and
      governance template.
```

---

## write-insight -- Verification Checklist

Verification phase: when promoting an IOR or finding to an insight.

```
[ ] Skill SKILL.md is valid
      Confirm: read ~/.openclaw/workspace/skills/write-insight/SKILL.md
      has correct frontmatter (name: write-insight,
      user-invocable: true, disable-model-invocation: false)
[ ] Frontmatter description is a trigger surface
      Confirm: description is task-oriented ("Write an insight:
      Insight-Evidence-Implications-Counter-evidence format with
      quality gates G1-G7, falsifiability, and cross-links."),
      under 160 bytes
[ ] When to Apply section is correct
      Confirm: lists insight-specific triggers (pattern across
      multiple IORs, durable lesson, changes how agents operate,
      quotable one-sentence) and exclusions (single-session IOR,
      unproven hypotheses, already-captured insights)
[ ] Format sections match template-insights.md
      Confirm: The Insight, Evidence, Implications, Counter-evidence,
      Version History -- all present and matching template body
      structure in order. Falsifiability (Counter-evidence) is
      prominent. Version History table format matches.
[ ] Frontmatter Rules are correct
      Confirm: 7 fields listed (name, id, tier, source, author,
      tags, links). Includes source field. tier is "always insight".
      Matches template schema exactly. At least one source required.
[ ] Naming Convention is correct
      Confirm: <short-slug>.md, kebab-case, max 60 chars.
      Example given. Matches template.
[ ] Quality Gates: G1-G7 named and matching template
      G1 One-Sentence Insight, G2 Evidence Is Cited,
      G3 Implications Are Concrete, G4 Falsifiable,
      G5 Source Traceability, G6 Cross-links Exist,
      G7 Formatting Rules.
      Confirm: all 7 names match template-insights.md.
[ ] Pre-Commit Self-Check: items match template checklist
      Template checklist has 11 items. Skill self-check has 11 items
      (10 template items + "All G1-G7 confirmed PASS").
      Confirm: every template checklist item appears in skill
      self-check. Falsifiability/counter-evidence item present.
      Version history item present.
[ ] Bundled template exists and is byte-identical
      Confirm: references/template-insights.md exists.
      diff against governance/template-insights.md is empty.
[ ] Cross-references are correct
      Confirm: Related section links to write-reflection and
      write-evaluation skills. Links to bundled template and
      governance template.
```

---

## Overall Self-Check

```
[ ] All 4 SKILL.md files exist and load as skills
[ ] All 4 bundled templates exist in references/
[ ] All 4 bundled templates byte-match governance templates
[ ] All 4 skills have user-invocable: true
[ ] All 4 skills have disable-model-invocation: false
[ ] All 4 skills have descriptions under 160 bytes
[ ] All 4 When to Apply sections correctly scope each skill
[ ] All 4 Format sections match their templates' body structures
[ ] All 4 Frontmatter Rules match their templates' schemas
[ ] All 4 Naming Conventions match their templates
[ ] All 4 Quality Gates sections: gates are named, names match
      templates exactly
[ ] All 4 Pre-Commit Self-Checks: every template checklist item
      appears, no items dropped, no items fabricated
[ ] All 4 Cross-references between skills are consistent
      (write-report links to write-evaluation, write-evaluation
      links to write-proposal, write-insight links to
      write-reflection, etc.)
```

---

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-17 | Ava | Initial IOR. Verification protocol for 4 template-writing skills: write-proposal, write-evaluation, write-report, write-insight. Per-skill checklists with 10 items each, following the same format as skills-test-verification.md. |

## Cross-Links

- `2026-07-17_ava_skills-test-verification.md` -- protocol skills test
  (preflight, loop-feynman, loop-schoen, session-end, write-reflection);
  the format this IOR follows
- `2026-07-17_ava_cold-start-verification-executed.md` -- cold-start
  verification executed, meta-work cycle closed
- `governance/template-skills.md` -- skill construction rules
- `governance/template-proposals.md` -- proposal template (bundled in
  write-proposal skill)
- `governance/template-evaluations.md` -- evaluation template (bundled in
  write-evaluation skill)
- `governance/template-reports.md` -- report template (bundled in
  write-report skill)
- `governance/template-insights.md` -- insight template (bundled in
  write-insight skill)
