---
name: multi-file-uniformity-is-a-structural-gate
id: 20260719T140018Z
tier: reflection
trigger: insight
author: Ava
tags: [uniformity, verification, drift, gates, skills, templates]
links:
  - governance/template-skills.md
  - research/insights/rules-need-gates.md
---

# Multi-File Uniformity Is a Structural Verification Gate

## I -- Idea

When N files are supposed to follow the same pattern (Self-Check
structure, Format Verification sections, commit format, gate
references), uniformity itself becomes the verification mechanism.
A single-file review catches content errors. A cross-file diff
catches structural drift that single-file review is blind to. The
audit of 5 write-X skills and 5 templates proved this: 20 errors
were found that a single-skill review would have missed, because
each skill individually looked "close enough."

The trigger was Suggi asking for a uniformity audit. The result
revealed copy-paste errors (wrong Quality Gates content copied from
report into reflection), numbering collisions (reflection items
15-18 appeared in two different sections), and wording drift
("IOR" vs "reflection" in commit messages). None of these were
visible when reading only one skill file at a time.

## O -- Opinion

Confidence: high (90%). I just performed the audit and fixed all 20
errors. The mechanism is straightforward: diff any two write-X skills
and deviations light up. This is not theoretical -- it is battle-tested
in this session.

Uniformity-as-gate is a specific case of R8 (Reference, Never Duplicate)
and R9 (Cross-Reference Propagation). When N files share a pattern,
the pattern IS the reference. Drift IS the violation. The gate is
structural because it fires on comparison, not on memory.

The cost of non-uniformity is invisible decay. One skill drifts by one
wording change. Next session, another skill drifts differently. After
10 sessions, 5 files share a name but not a structure. The agent
reading each skill spends tokens reconciling the differences. The fix
cost is 20x the prevention cost -- exactly what happened here.

## R -- Reflection

### Surprise (30%)

I expected the audit to find 3-5 minor wording issues. I did not
expect 20 errors including wrong Quality Gates content (report's G1
"Evaluated" copied into reflection's Quality Gates section) and
numbering collisions (four items in write-reflection appeared in two
sections with different meanings). The magnitude gap -- 5x what I
predicted -- confirms that single-file review is systematically blind
to cross-file drift.

### Feel (30%)

Satisfied that the fix was clean and complete. The edit-then-verify
cycle produced 10 files pushed to 2 repos without introducing new
errors. The one rollback (B1 match text) was detected and fixed
immediately. Slightly embarrassed that the memory overwrite happened
on daily memory -- restored from git, but the scar is fresh.

### Learn (40%)

1. Cross-file uniformity is not cosmetic. It is a verification
   mechanism. When N files share an identical skeleton, drift is
   self-evident. When they don't, drift is invisible until an audit.

2. The fractal pattern (checklist + Self-Check) works at every layer:
   session-wide (AGENTS.md preflight), skill-level (Format Verification),
   and template-level (pre-commit checklists). Suggi deploying the
   meta-gate checkbox to AGENTS.md independently confirms the pattern
   has transferred -- it is no longer just my design vocabulary.

3. The "if push fails, pull first" handler is reactive, not proactive.
   A pre-push pull would prevent the failure class entirely. R13
   should be strengthened: pull before push, not pull if push fails.

## One Actionable Change

Add a proactive pre-push pull to the commit step in all 5 write-X skills
and the session-end skill. Current: "git push origin main" followed by
"If the push fails, pull first, resolve, then push." Changed to:
"git pull --ff-only origin main" BEFORE "git push origin main," with
the reactive fallback retained as defense-in-depth. This prevents the
R13 violation class observed this session (concurrent edits causing
push rejection).

## Cross-links

- `2026-07-19_ava_checklist-verification-generalizes.md` -- prior IOR
  on the checklist-as-verification-primitive pattern
- `governance/template-skills.md` -- the Format Verification pattern
  that enabled the uniformity audit
- `research/insights/rules-need-gates.md` -- R8 and R9 as scar tissue
  from drift failures
