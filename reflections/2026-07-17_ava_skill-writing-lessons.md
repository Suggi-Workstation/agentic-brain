---
name: skill-writing-lessons
id: 20260717T153800Z
tier: reflection
trigger: error
author: ava
tags: [skills, skill-writing, errors, governance, duplication, r8, g5, template-skills, learning]
links:
  - governance/template-skills.md
  - 2026-07-17_ava_skills-test-verification.md
  - 2026-07-17_ava_skills-test-verification-templates.md
---

# i+o+r  what I learned about building OpenClaw skills (Ava)

## I -- Idea

Writing skills correctly requires understanding one rule above all others:
the SKILL.md carries procedure (what to do step by step); the bundled
reference template carries specification (format, schema, gates,
checklist). Duplicating the specification into the procedure is an R8
violation that bloats the skill, creates drift risk, and violates
G5 (No Duplicate Governance) from template-skills.md. I made this
mistake across 5 skills before Suggi corrected me.

## O -- Opinion

Confidence: high (95%). The pattern is now clear because I have seen
both the wrong way and the right way. The wrong way: my first write-
reflection skill (165 lines) inlined all 8 quality gates, the full
I/O/R format, frontmatter rules, and self-check items -- all content
that already lived in `references/template-reflections.md`. The right
way: 96 lines. "Read `{baseDir}/references/template-reflections.md`.
Follow it exactly." The skill shrunk by 42% and became strictly
procedural.

The same mistake propagated to the other 4 writing skills
(write-proposal, write-evaluation, write-report, write-insight)
because I templated the wrong pattern. This is a compound failure:
copying a broken pattern produces N broken copies. The fix required
rewriting all 5 skills, which cost extra session time that could have
been avoided by getting the first one right.

## R -- Reflection

### Surprise (30%)

I expected writing skills to be straightforward -- read the governance
template, write a condensed version, bundle both. What surprised me
was that the condensed version IS the problem. Condensing a template
into a skill body is still duplication; it is just shorter duplication.
The correct skill body does not condense the template at all. It
references it.

The second surprise: `{baseDir}` is the correct convention, not `~`.
I initially questioned whether `{baseDir}` worked correctly, but the
OpenClaw docs (`creating-skills.md`) explicitly define it: "the agent
resolves `{baseDir}` against the skill's own directory." This is
portable -- the skill can move to a different location and still find
its references. A hardcoded `~` path would break on different machines.

The third surprise: the output path `/tmp/brain-ior/reflections/` vs
`brain-ior/reflections/` matters. A relative path leaves ambiguity
about the working directory. An absolute path in the clone directory
(which the skill explicitly creates at `/tmp/brain-ior`) is unambiguous.
Small path errors in skills create silent failures that are hard to
debug because the skill appears to work but writes to the wrong
location.

### Feel (30%)

Frustrated that I made a systematic error across 5 skills. The
template-skills.md governance file was right there -- I had read it,
I had consulted it for the protocol skills (preflight, loop-feynman,
etc.), but I did not apply its G5 rule to the writing skills. The
anti-pattern "Skill duplicates template" lists exactly what I did:
"Skill contains checklist items from template-reflections.md. R8
violation. Reference the template. Skill is procedure, template is
format."

The fix was quick -- rewriting 5 skills took under 10 minutes each once
the correct pattern was established -- but the fact that I needed the
fix at all means I was applying a different standard to writing skills
than to protocol skills. The protocol skills (preflight, loop-feynman,
etc.) do not duplicate governance because they carry their own
procedures. The writing skills should carry procedure too -- but I
treated them as "condensed templates" instead of "procedural guides
to using a template."

### Learn (40%)

Four durable lessons:

1. **The procedure-specification split is universal.** Every skill
   follows the same model: SKILL.md = procedure (steps to follow);
   references/template-*.md = specification (format, schema, gates,
   checklist). This applies to writing skills, protocol skills, tool
   skills -- every skill. If a SKILL.md contains a format definition,
   a quality gate list, or a self-check that also exists in a
   references/ file, it is duplication. Delete it and reference the
   file instead.

2. **Get the first skill right before copying the pattern.** My
   write-reflection skill was the template for the other 4 writing
   skills. Because it was wrong, all 4 copies were wrong. The fix
   multiplied by N. If I had validated the first skill against
   template-skills.md G5 before writing the others, I would have
   caught the error after 1 skill, not 5. Structural gate: after
   writing any new skill, run the template-skills.md checklist
   (12 items) before writing the next one. Never batch-create skills
   from an unvalidated template.

3. **`{baseDir}` for internal references, absolute paths for clone
   outputs, MUST/MUST NOT for self-checks.** Three small conventions
   that each caused a correction: `{baseDir}/references/` not `~/`,
   `/tmp/brain-ior/reflections/` not `brain-ior/reflections/`, and
   "MUST NOT be committed with any item unconfirmed" not "Before
   ending the session, confirm." Small conventions, big difference
   in correctness.

4. **The description is the skill's trigger surface.** The description
   field is not a summary -- it is what the model matches against the
   current task to decide whether to invoke the skill. A good
   description embeds trigger keywords (IOR, reflection, evaluation,
   proposal, report, insight) and names the format (Idea-Opinion-
   Reflection, Source-Criteria-Findings-Verdict, etc.). The When to
   Invoke section can list additional keywords, but the description
   is the primary trigger surface.

## One Actionable Change

Add a gate to the skill-building workflow: after writing any new
SKILL.md, run the template-skills.md 12-item Pre-Commit Self-Check
BEFORE committing. Add a step to the skill-builder skill that
explicitly checks G5 (No Duplicate Governance): confirm every format
definition, quality gate list, and self-check item in the SKILL.md
does NOT duplicate content from a bundled references/ file. If it
does, delete the duplication and add a `{baseDir}` reference instead.

## Cross-Links

- `governance/template-skills.md` -- skill construction rules; the G5
  anti-pattern that caught this error
- `2026-07-17_ava_skills-test-verification.md` -- protocol skills test
  (the correct pattern I should have followed)
- `2026-07-17_ava_skills-test-verification-templates.md` -- template
  skills test (the skills this reflection is about)
