---
name: skills-test-verification-templates
id: 20260717T150500Z
tier: reflection
trigger: milestone
author: ava
tags: [skills, testing, verification, write-proposal, write-evaluation, write-report, write-insight, write-library, templates]
links:
  - 2026-07-17_ava_skills-test-verification.md
  - 2026-07-17_ava_cold-start-verification-executed.md
  - governance/template-skills.md
  - governance/template-proposals.md
  - governance/template-evaluations.md
  - governance/template-reports.md
  - governance/template-insights.md
  - governance/template-library.md
---

# i+o+r  verification protocol for the 5 template-writing skills (Ava)

## I -- Idea

Five template-writing skills have been deployed to the workspace:
write-proposal, write-evaluation, write-report, write-insight, and
write-library. Each bundles its template in a references/ folder,
analogous to write-reflection. Unlike the protocol skills (preflight,
loop-feynman, loop-schoen, session-end) which were tested via warm
(37/37) and cold-start verification, these writing skills are
user-invocable -- they are triggered explicitly when an agent writes
the corresponding document type. They need their own integration test
to confirm: the SKILL.md loads, the bundled template is accessible,
the quality gates match the live template, and all pre-commit
self-check items are present.

This IOR defines the verification protocol and test checklist for all
5 skills. Write-library was deployed in an earlier session;
write-proposal, write-evaluation, write-report, and write-insight
were deployed in this session.

## O -- Opinion

Confidence: high (95%) that all 5 skills will pass. The write-reflection
skill set the pattern that all 5 follow. The risk is lower than the
protocol skills test because these are simpler -- each maps one template
to one document type, with no session-phase dependency or gate-trigger
ambiguity. The only failure mode is a copy-paste error in the SKILL.md
(quality gate count mismatch, wrong frontmatter field count, missing
self-check item).

The write-library skill has already been exercised (the subagent-workspace-
routing proposal used template-proposals.md, which was confirmed to match
the live template). The other four have not been exercised yet. A future
session should exercise one of each document type to confirm end-to-end.

## R -- Reflection

### Surprise (30%)

The pattern established by write-reflection (SKILL.md + bundled template
in references/) scales cleanly. All 5 skills follow the same structure:
Hard Gate, When to Apply, Format (condensed from template), Frontmatter
Rules, Naming Convention, Quality Gates, Pre-Commit Self-Check, Related.
No template required unique structural treatment -- the differences are
in content (different sections, different gate counts) but the SKILL.md
structure is invariant.

The one structural difference across templates is the frontmatter field
count: proposals need 6 fields, evaluations need 7 (includes `source`),
reports need 6, insights need 7 (includes `source`), library topics
need 7 (includes `domain`). The self-check items reflect these counts
correctly in each SKILL.md -- verified during construction.

### Feel (30%)

Satisfied that the template ecosystem is now fully skill-covered. The
six governance templates (template-reflections, template-library,
template-proposals, template-evaluations, template-reports,
template-insights) now have six corresponding skills (write-reflection,
write-library, write-proposal, write-evaluation, write-report,
write-insight). The seventh template (template-skills) governs skill
construction itself and does not need a write-skill skill -- it is
consumed by skill-builder.

The progression from "governance templates are documents I must
remember to read" to "each template is bundled in a skill that
self-documents the procedure" is the constitution-vs-procedure split
extended to the writing domain. Every document type now has an
invocable skill that carries the condensed procedure, the quality
gates, and the bundled reference template.

### Learn (40%)

1. **Bundled templates create self-contained skills.** A skill that
   bundles its governing template in references/ does not need a
   brain clone to consult the format. This removes the network/fetch
   dependency during writing sessions -- the skill and its reference
   travel together.

2. **The SKILL.md structure is template-agnostic.** The same structure
   (Hard Gate, When to Apply, Format, Frontmatter Rules, Naming
   Convention, Quality Gates, Pre-Commit Self-Check, Related) works
   for every document type. The content changes; the container does
   not. This means future templates can be skilled with minimal
   design work.

3. **Quality gate counts differ across templates, and that is correct.**
   Proposals have 7 gates (G1-G7). Evaluations have 7 (G1-G7).
   Reports have 7 (G1-G7). Insights have 7 (G1-G7). Library topics
   have 7 (G1-G7). But the gates test different things -- an
   evaluation's G1 (Different Agent) is fundamentally different from
   a report's G1 (Independently Evaluated). The gates are named, not
   numbered, in the self-checks. Good: naming gates prevents
   "count 7" from becoming the only check.

## One Actionable Change

When exercising a writing skill, the agent should read the SKILL.md
first, NOT the bundled reference template first. The SKILL.md is the
condensed procedure; the reference template is for detailed rules and
examples. The write-reflection skill already says "For detailed rules
and examples, consult the template." This pattern is consistent across
all 5 new skills. The actionable change: add a "Read Order" note to
the AGENTS.md IOR Writing section clarifying that the SKILL.md is read
first, and the reference template is read only for example consultation
or edge cases not covered in the condensed procedure.

---

## Master Static Verification Checklist

Run these checks for each of the 5 skills. All items must PASS before
the skills are considered verified.

```
[ ] Skills directory exists: skills/<name>/SKILL.md
[ ] References directory exists: skills/<name>/references/
[ ] Bundled template exists: skills/<name>/references/template-<name>.md
[ ] Template file is identical to agentic-brain/governance/template-<name>.md
      (byte-for-byte, or with only expected versioning differences)
[ ] Skill visible in session (listed in available_skills)
[ ] user-invocable: true
[ ] disable-model-invocation: false
[ ] Description is under 160 bytes
```

---

## write-proposal -- Static Checks

```
[ ] SKILL.md frontmatter: name=write-proposal, user-invocable=true
[ ] When to Apply: lists proposal-specific triggers and exclusions
[ ] Format sections: Problem, Proposed Solution, Impact, Open Questions, Approval Gate
      All match template-proposals.md body structure
[ ] Frontmatter Rules: 6 fields (name, id, tier, author, tags, links)
      Matches template-proposals.md schema
[ ] Naming Convention: <short-slug>.md, kebab-case
      Matches template-proposals.md convention
[ ] Quality Gates: G1-G7 present
      G1 Problem Is Specific, G2 Solution Is Concrete, G3 Impact Is Estimated,
      G4 Open Questions Surfaced, G5 Cross-links Exist, G6 Frontmatter Complete,
      G7 Formatting Rules -- all match template-proposals.md
[ ] Pre-Commit Self-Check: 11 items
      Frontmatter (2), id, problem, solution, impact, open questions,
      approval gate, cross-links, filename, ASCII, all G1-G7
[ ] Bundled template: references/template-proposals.md exists
[ ] Bundled template content: byte-identical to governance/template-proposals.md
```

---

## write-evaluation -- Static Checks

```
[ ] SKILL.md frontmatter: name=write-evaluation, user-invocable=true
[ ] When to Apply: lists evaluation-specific triggers (decorrelation rule)
[ ] Format sections: Source, Evaluation Criteria, Findings, Verdict, Confidence
      All match template-evaluations.md body structure
[ ] Frontmatter Rules: 7 fields (name, id, tier, source, author, tags, links)
      Matches template-evaluations.md schema (includes source field)
[ ] Naming Convention: <short-slug>.md, kebab-case
      Matches template-evaluations.md convention
[ ] Quality Gates: G1-G7 present
      G1 Different Agent, G2 Criteria Stated First, G3 Evidence Cited,
      G4 Verdict Is Explicit, G5 Confidence Included, G6 Cross-links Exist,
      G7 Formatting Rules -- all match template-evaluations.md
[ ] Pre-Commit Self-Check: 13 items
      Frontmatter (2), id, source+scope, criteria-before-findings,
      findings-backed, verdict-explicit, changes-concrete, confidence,
      cross-links, decorrelation, filename, ASCII, all G1-G7
[ ] Bundled template: references/template-evaluations.md exists
[ ] Bundled template content: byte-identical to governance/template-evaluations.md
```

---

## write-report -- Static Checks

```
[ ] SKILL.md frontmatter: name=write-report, user-invocable=true
[ ] When to Apply: lists report-specific triggers (multi-step, evaluated)
[ ] Format sections: Executive Summary, Research Question, Methodology,
      Findings, Discussion, Conclusion, Evaluation History
      All match template-reports.md body structure
[ ] Frontmatter Rules: 6 fields (name, id, tier, author, tags, links)
      Matches template-reports.md schema
[ ] Naming Convention: <short-slug>.md, kebab-case
      Matches template-reports.md convention
[ ] Quality Gates: G1-G7 present
      G1 Independently Evaluated, G2 Executive Summary Stands Alone,
      G3 Methodology Is Reproducible, G4 Negative Results Included,
      G5 Cross-links Exist, G6 Frontmatter Complete, G7 Formatting Rules
      -- all match template-reports.md
[ ] Pre-Commit Self-Check: 14 items
      Frontmatter (2), id, exec-summary, research-question, methodology,
      findings, negative-results, discussion, conclusion, eval-history,
      cross-links, filename, ASCII, all G1-G7
[ ] Bundled template: references/template-reports.md exists
[ ] Bundled template content: byte-identical to governance/template-reports.md
```

---

## write-insight -- Static Checks

```
[ ] SKILL.md frontmatter: name=write-insight, user-invocable=true
[ ] When to Apply: lists insight-specific triggers (patterns, promoted)
[ ] Format sections: The Insight, Evidence, Implications, Counter-evidence,
      Version History
      All match template-insights.md body structure
[ ] Frontmatter Rules: 7 fields (name, id, tier, source, author, tags, links)
      Matches template-insights.md schema (includes source field)
[ ] Naming Convention: <short-slug>.md, kebab-case
      Matches template-insights.md convention
[ ] Quality Gates: G1-G7 present
      G1 One-Sentence Insight, G2 Evidence Is Cited, G3 Implications Are
      Concrete, G4 Falsifiable, G5 Source Traceability, G6 Cross-links Exist,
      G7 Formatting Rules -- all match template-insights.md
[ ] Pre-Commit Self-Check: 11 items
      Frontmatter (2), id, one-sentence, evidence, implications,
      counter-evidence, version-history, cross-links, filename, ASCII,
      all G1-G7
[ ] Bundled template: references/template-insights.md exists
[ ] Bundled template content: byte-identical to governance/template-insights.md
```

---

## write-library -- Static Checks

```
[ ] SKILL.md frontmatter: name=write-library, user-invocable=true
[ ] When to Apply: lists library-specific triggers and exclusions
[ ] Format sections: Hypothesis, Body (Analytical + Narrative), Conclusion,
      Cross-Links
      All match template-library.md body structure
[ ] Frontmatter Rules: 7 fields (name, id, tier, domain, author, tags, links)
      Matches template-library.md schema (includes domain field)
[ ] Naming Convention: <domain>/<slug>.md
      Matches template-library.md convention
[ ] Quality Gates: G1-G7 present
      G1 Atomic, G2 Feynman Test, G3 Hypothesis Makes a Claim, G4 Sourced,
      G5 Cross-links Exist, G6 Frontmatter Complete, G7 Formatting Rules
      -- all match template-library.md
[ ] Pre-Commit Self-Check: 14 items
      Frontmatter (2), id, domain-match, tags-type, hypothesis-claim,
      analytical-element, narrative-section, conclusion, cross-links,
      sources, feynman-test, filename, ASCII, all G1-G7
[ ] Bundled template: references/template-library.md exists
[ ] Bundled template content: byte-identical to governance/template-library.md
```

---

## Dynamic Verification (Future Session)

In a future session, exercise each skill by writing one document of each
type. Confirm:

```
[ ] write-proposal: agent writes a minimal proposal, G1-G7 all pass
[ ] write-evaluation: agent evaluates another agent's work, decorrelation
      rule satisfied, G1-G7 all pass
[ ] write-report: agent writes a report, includes evaluation history,
      G1-G7 all pass
[ ] write-insight: agent promotes an IOR to an insight, includes
      counter-evidence, G1-G7 all pass
[ ] write-library: agent writes a library topic, includes analytical
      section, G1-G7 all pass
```

Dynamic verification is lower priority than the protocol skills'
cold-start test because these are user-invocable -- the agent explicitly
reads the skill when the user says "write a proposal" or "evaluate this."
The trigger is explicit, not contextual like preflight or loop-feynman.

---

## Template Content Verification (Static)

Verify each bundled template is byte-identical to the live governance
template in the agentic-brain. Run from workspace root:

```bash
for skill in write-proposal write-evaluation write-report write-insight write-library; do
  tmpl=$(echo $skill | sed 's/write-/template-/')
  if diff <(tr -d '\r' skills/$skill/references/$tmpl.md) \
          <(tr -d '\r' /tmp/brain-check/governance/$tmpl.md) > /dev/null 2>&1; then
    echo "MATCH: $skill"
  else
    echo "MISMATCH: $skill"
  fi
done
```

---

## Overall Self-Check

```
[ ] All 5 SKILL.md files exist and load as skills
[ ] All 5 bundled templates exist in references/
[ ] All 5 bundled templates byte-match governance templates
[ ] All 5 skills have user-invocable: true
[ ] All 5 skills have disable-model-invocation: false
[ ] All 5 skills have descriptions under 160 bytes
[ ] All 5 self-checks match their template checklists
[ ] Quality gate names (not just counts) match templates
[ ] Frontmatter field counts match template schemas
[ ] Cross-references between skills are consistent (write-report links
      to write-evaluation, write-evaluation links to write-proposal, etc.)
```

---

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-17 | Ava | Initial IOR. Verification protocol for 5 template-writing skills: write-proposal, write-evaluation, write-report, write-insight, write-library. Static checks defined for each skill. Dynamic verification deferred to future session. |

## Cross-Links

- `2026-07-17_ava_skills-test-verification.md` -- protocol skills test
  (preflight, loop-feynman, loop-schoen, session-end, write-reflection)
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
- `governance/template-library.md` -- library template (bundled in
  write-library skill)
