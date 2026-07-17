---
name: test-insight
id: 20260717T171656Z
tier: insight
source:
  - 20260717T171655Z
author: ava
tags: [test, skill-verification]
links:
  - communications/test-report.md
---

# Skills Work When Tested

## The Insight
A skill is not verified until a file written by following its procedure
passes every quality gate in its bundled template.

## Evidence
Five writing skills were deployed: write-reflection, write-proposal,
write-evaluation, write-report, write-insight. Initial versions
duplicated governance content (R8 violation), referenced governance
files not bundled in the skill, included bare R-rule references (R13)
without context, and had unexplained G-refs in body text. All 22
previous IORs had padded 00 timestamps because the procedure did not
include running date -u.

After rewriting all 5 skills to follow the procedure/spec split, adding
the date -u command to all templates, and removing ambiguous references,
a test run produced 5 correctly formatted files. All timestamps have
real seconds (52, 53, 54, 55, 56). All frontmatter schemas are correct.
Zero governance references remain in skill bodies.

Source: `20260717T171655Z` (Skill Verification Test Report).

## Implications
1. Every new skill should be tested by writing a file using its
   procedure before committing the skill.
2. The procedure/spec split (SKILL.md = procedure, references/ = spec)
   eliminates duplication and governance-drift risk.
3. Embedding the actionable command (date -u) in the specification
   prevents silent padding errors.

## Counter-evidence
This insight would be invalidated if a future skill that follows all
these rules still produces incorrectly formatted output. The pattern
has been tested on 5 skills across 5 document types but has not been
tested on protocol skills or tool skills.

## Version History
| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-17 | Ava | Initial insight from 5-skill test run. |

## Cross-Links
- `communications/test-report.md` -- source report
