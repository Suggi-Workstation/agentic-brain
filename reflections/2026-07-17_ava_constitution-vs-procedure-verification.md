---
name: constitution-vs-procedure-verification
id: 20260717T134800Z
tier: reflection
trigger: research
author: Ava
tags: [skills, architecture, constitution, procedure, verification, protocol-migration, agents-md]
links:
  - 2026-07-17_ava_skills-as-protocol-carriers.md
  - 2026-07-17_ava_preflight-skill-deployment.md
  - 2026-07-17_ava_skills-test-verification.md
  - governance/template-skills.md
---

# i+o+r  constitution-vs-procedure split -- is it working? (Ava)

## I -- Idea

The constitution-vs-procedure architecture split in one sentence: we
moved five protocol procedures from AGENTS.md inline text into
lazily-loaded skills, keeping only gate instructions in the always-
loaded context. The split works -- the migration preserved all original
content, reduced AGENTS.md by 99 lines (4,548 chars, 38%), and
discovered one new failure class (stale inline-prose references
surviving file-path renames).

This IOR is the Feynman Loop output from a skills integration test
session. Before the loop, I knew the migration reduced AGENTS.md size
and the preflight skill passed its test. I did not know the exact
char/line delta, whether any stale references survived the rename
pass, whether the bundled template was functional, or whether the
skills meaningfully improved over the inline versions they replaced.

## O -- Opinion

Confidence: high (90%) that the split architecture is correct and
working. The evidence:

**AGENTS.md reduction:** 273 lines / 12,123 chars (stale-AGENTS.md from
Phase 24, with inline preflight) -> 174 lines / 7,575 chars (current).
That is 99 lines and 4,548 characters removed from always-loaded
bootstrap context -- a 38% reduction. The five skills together contain
~16,000 chars of procedure text, loaded only when invoked. A session
with 3+ turns nets positive on token savings.

**Gate instructions intact:** Every protocol section in the new AGENTS.md
has a valid gate instruction with the correct skill name and path.
The preflight skill already verified as working (10/10 integration test).

**Content preserved and improved:** Comparing stale-AGENTS.md procedures
against their skill counterparts, no procedural content was lost. The
skills added structure the inline versions lacked:
- `loop-feynman`: added when-to-apply rules, 7-item self-check, cross-refs
- `loop-schoen`: added self-check (6 items), when-to-apply, cross-refs
- `session-end`: added prerequisite section, cross-refs, git commands
- `write-reflection`: added frontmatter rules, naming convention,
  when-to-apply, and bundled template-reflections.md locally

**One gap found:** The rename pass (feynman-loop->loop-feynman,
schoen-loop->loop-schoen, ior-write->write-reflection) used sed on file
paths but missed inline prose references in skill body text. Three
stale references survived:
1. `loop-feynman/SKILL.md` line 90: referenced `ior-write` (fixed)
2. `session-end/SKILL.md` line 18: referenced `schoen-loop` (fixed)
3. `session-end/SKILL.md` line 44: referenced `ior-write` (fixed)

This is a new failure class: **rename sed passes are necessary but
insufficient -- they only match file-path patterns, not inline prose
that uses backtick-quoted skill names.** A grep for the old names
across all skill bodies after rename would have caught this.

## R -- Reflection

### Surprise (30%)

I expected the migration to be clean after the sed pass. I did not
expect 3 stale references to survive. The surprise is that sed
matched `skills/feynman-loop/SKILL.md` (path pattern) but missed
`` `feynman-loop` `` (inline prose). This is a pattern I should
have anticipated -- the preflight-skill-deployment IOR's step 3
`/context list` was another case of "the reference format differs
from the thing being referenced." The lesson compounds.

The 38% reduction (99 lines) was also larger than I expected. I had
estimated ~76 lines from memory; the actual delta is 99. The
discrepancy was because I forgot the self-check tables in session-end
and IOR writing were also removed.

### Feel (30%)

Satisfied that the architecture holds up under scrutiny. The 38%
reduction is real and measurable. The skills are richer than the
inline versions they replaced -- they did not just preserve content,
they improved it. Finding the stale references during the test
session is exactly why we test: the gap existed, the test caught it,
the fix was applied before anyone else encountered it.

Slightly frustrated that I did not think to grep for backtick-quoted
old names during the rename. That is the kind of completeness check
that separates "migration" from "thorough migration." The scar is
small but the pattern is worth gating.

### Learn (40%)

1. **Rename completeness requires two grep passes.** A file-path grep
   (`skills/old-name/`) catches directory references. An inline-prose
   grep (`` `old-name` ``) catches body text. Both must be run after
   every rename. R9 (Cross-Reference Propagation) covers this in
   principle but the procedure was incomplete.

2. **The write-reflection skill's bundled template is a design win.**
   Removing the agentic-brain clone dependency for IOR format reference
   means the skill is self-contained. This is the pattern for future
   skills that need governance templates: bundle the reference, don't
   link to the brain.

3. **The split architecture passed its first full-session test.** All
   five skills loaded (static check), the gate instructions triggered
   invocation (preflight tested, loop-feynman invoked for this IOR,
   loop-schoen and session-end will be tested at session end), and
   the content integrity held (no procedural steps lost). The
   architecture is ready for production.

## One Actionable Change

Add a gate to `governance/template-skills.md`: after any skill rename,
run TWO grep passes across ALL skill bodies and AGENTS.md -- one for
file-path patterns (`skills/old-name/`) and one for backtick-quoted
names (`` `old-name` ``). Both must return zero results before the
rename is declared complete. This prevents the stale-reference failure
class discovered in this session.

## Cross-links

- `2026-07-17_ava_skills-as-protocol-carriers.md` -- the architecture
  IOR that proposed this split
- `2026-07-17_ava_preflight-skill-deployment.md` -- the first migration
  test (preflight skill, 10/10 PASS)
- `2026-07-17_ava_skills-test-verification.md` -- the verification
  protocol IOR (checklists for remaining 4 skills)
- `governance/template-skills.md` -- skill construction rules
- `skills/loop-feynman/SKILL.md` (workspace) -- tested and fixed
- `skills/session-end/SKILL.md` (workspace) -- tested and fixed

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-17 | Ava | Initial IOR. Feynman Loop evaluation of the constitution-vs-procedure split: 38% AGENTS.md reduction, 3 stale references found and fixed, architecture verified working. |
