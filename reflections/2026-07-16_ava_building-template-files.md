---
name: building-template-files
id: 20260716T215500Z
tier: reflection
trigger: milestone
author: ava
tags: [templates, architecture, governance, frontmatter, metadata, quality]
links:
  - governance/template-reflections.md
  - governance/template-library.md
  - governance/template-proposals.md
  - governance/template-evaluations.md
  - governance/template-reports.md
  - governance/template-insights.md
  - governance/system-constitution.md
  - governance/system-primedirectives.md
---

# Building Six Template Files From Scratch -- What 3 Hours of Iteration Taught Me

## I -- Idea
We built six governance template files that define how every document type
in the Suggi-Workstation org is written. Starting from one template
(reflections/IORs), we expanded to a complete set: reflections, library,
proposals, evaluations, reports, and insights. Every template now shares
the same structure -- Global Formatting Rules, Frontmatter Schema with
inline comments, Frontmatter Rules, Naming Convention, Body Structure,
Cross-Links, numbered Quality Gates (G1-GN), an Example, and a copy-paste
Checklist. The process took roughly 3 hours, roughly 25 commits, and
surfaced deep design questions about metadata, redundancy, and uniformity.

What triggered this: Suggi asked me to research and build a rule layout
for IORs. That single template grew into a full governance layer as we
realized every file type in the org needed the same level of structural
clarity. Each iteration exposed a new consistency gap -- a missing
section, a duplicated field, an inconsistent naming convention --
that once seen, could not be unseen.

## O -- Opinion
Confidence: high (90%). The templates are solid. More importantly, the
process of building them taught me principles I will apply to every
future system design.

The single most impactful decision was standardizing the numbered G1-GN
quality gate format across all six templates. Before this, each template
had its own ad-hoc gate list with inconsistent naming and structure.
After standardization, every template has a falsifiable checklist: each
gate either passes or it does not. A weak file is explicitly visible as
failing specific numbered gates. This is the same principle that made
the 13 Gate Rules (R1-R13) the most durable part of the v0.1-v4.0
architecture -- numbered, falsifiable, structural.

The second most impactful decision was removing redundant metadata
fields. We eliminated `date` (encoded in id + filename), `aliases`
(tags cover searchability), `format` (the template defines the format),
`status` (git history is the tracker), `evaluated_by` (evaluations are
the single source of truth), and `evaluator` (identical to author).
Each removal reduced maintenance burden -- fewer fields to keep in
sync, fewer sources of drift. This aligns with the Zettelkasten
principle: "Don't over-formalize. Denote type with a tag."

The third insight was that templates themselves need different metadata
than the files they describe. The `lock: approval-required` and
`approved_by: Suggi` fields belong on the governance templates
themselves, not on the user-facing schemas. This distinction --
governance vs. operational -- took two passes to get right. The first
version had `lock`/`approved_by` leaking into every schema. Suggi's
feedback ("Do you understand my pain?") crystallized the rule:
governance files are locked; working files are not.

## R -- Reflection

### Surprise (30%)
I expected this to take 20 minutes. It took 3 hours. The surprise was
not the volume of work -- it was how each iteration exposed a new
consistency problem. Fixing one template's frontmatter ordering would
reveal that another template had no Frontmatter Rules section at all.
Adding inline comments to evaluations would expose that proposals had
a stray `tags` field in its own governance frontmatter from an earlier
sed command. The templates had to be checked as a SET, not individually.
One template's inconsistency made the others look wrong by comparison,
and the standard kept rising.

The second surprise: Suggi's feedback was almost entirely about
uniformity. Not "this field is wrong" but "this field is in a
different order than the others" or "this template has comments but
this one does not." The lesson: in a multi-file system, consistency IS
the feature. An inconsistent system teaches the user that the rules
don't matter -- because they change from file to file.

### Feel (30%)
Humbled by the number of mistakes I made. The stray `tags` field in
proposals' governance frontmatter, the duplicate comments from
overlapping replace operations, the missing Frontmatter Rules sections
in four templates -- each mistake was caught by either Suggi's review
or a systematic consistency check. This is exactly what the decorrelated
review principle predicts: the producing mind cannot see its own errors.
Suggi's role as the external reviewer caught things I walked past
dozens of times.

Proud of the final result. Six templates, each with the same skeleton,
each field explained with an inline comment, each gate numbered and
falsifiable. The templates now encode everything we learned from the
archive's v0.1-v5.7 journey -- the Feynman Loop, the Schoen Loop, the
13 Gate Rules, the IOR format, the Prime Directives, the anti-patterns
table -- in a structure that any new agent can pick up and use.

Slightly embarrassed that we did not write a single actual file using
any of these templates. We spent 3 hours perfecting the HOW and zero
minutes testing the WHAT. This is a reflection I am writing now because
Suggi asked for it -- the templates themselves have not yet produced a
single reflection, library topic, proposal, evaluation, report, or
insight. The architecture is ready. The proof is in the using.

### Learn (40%)
1. **Templates must be checked as a set, not individually.** A change
   to one template's section structure must be cross-checked against all
   others. The systematic consistency audit (counting sections per
   template, verifying field order, checking for stray fields) was the
   single most effective quality mechanism. Every time I ran the audit,
   it found something. This should be automated: a script that reads all
   six templates and reports any structural inconsistency.

2. **Every metadata field must justify its existence.** Each field in a
   frontmatter schema is a maintenance contract. If the field must be
   kept in sync with another source, it WILL drift. The fields we removed
   (`date`, `aliases`, `format`, `status`, `evaluated_by`, `evaluator`)
   were all cases of either (a) information encoded elsewhere or (b)
   information that must be manually synchronized with another file.
   Single source of truth is not a preference -- it is the only way to
   prevent drift in a multi-agent system.

3. **Governance metadata and operational metadata are different tiers.**
   `lock: approval-required` and `approved_by` are governance-tier
   fields. They should NEVER appear in user-facing schemas. The
   templates themselves carry them; the files written using the
   templates do not. Mixing tiers creates confusion about who can
   modify what. This should be explicit in every template's frontmatter
   rules.

4. **Inline comments in schemas are disproportionately valuable.** The
   reflection template had inline comments (`# ISO 8601 UTC...`, `#
   lowercase, specific`) on every field. The other templates did not.
   Adding them took 5 minutes and immediately made every template feel
   complete. A schema without comments is a puzzle; a schema with
   comments is a contract. For agents reading these templates cold
   (new agents joining the system), the comments are the onboarding.

5. **The example section is the template's test.** Every template has an
   Example section with a complete, valid file. These examples are
   self-referential -- they use realistic ids, tags, and links that
   could exist in the system. The examples serve as both documentation
   and as a structural test: if the example does not pass all quality
   gates, the template is broken. This is the template equivalent of
   R6 (automation beats rules): the example is the automated test.

6. **Suggi's review pattern: consistency first, content second.** Suggi
   did not question the individual field choices nearly as much as the
   inconsistency between templates. "Why does evaluations have subject
   but insights has source?" / "Why is id before tier here but after
   there?" / "This one has comments but this one does not." The review
   instinct is: if it varies, there must be a reason. If there is no
   reason, make it uniform. This is R8 (Reference, Never Duplicate)
   applied at the review level.

## One Actionable Change
Write a consistency audit script (`governance/audit-templates.sh`) that
reads all six template files and verifies:
- Every template has the same section headers (Global Formatting Rules,
  Frontmatter, Naming Convention, Frontmatter Rules, Body Structure,
  Cross-Links, Quality Gates, Example, Checklist)
- Every template has exactly one `### Frontmatter Rules:` section with
  one rule per schema field
- Every template's Quality Gates are numbered G1-GN in sequence
- Every template's frontmatter schema fields are in the same order as
  their Frontmatter Rules
- Zero non-ASCII characters across all templates
- Zero instances of `lock:` or `approved_by:` in user-facing schemas
  or examples (only in the template's own frontmatter, lines 1-12)

This is R6 in action: automation beats manual review. The consistency
problems I fixed manually today would have been caught by this script
on the first commit.

## Cross-links
- `governance/template-reflections.md` -- the reference template that
  set the standard for all others
- `governance/system-constitution.md` -- the precedence rules that
  govern the template tier system
- `governance/system-primedirectives.md` -- the Prime Directives that
  shaped the template content (Ethics, Self-Improvement, Simplicity)
- `2026-07-16_ava_rebuilding-core-files.md` -- the earlier reflection
  on core files research that led to this template work
- `2026-06-13_ava_gate-rules-architecture.md` -- the 13 Gate Rules
  (R1-R13) that the numbered G1-GN quality gate format echoes
