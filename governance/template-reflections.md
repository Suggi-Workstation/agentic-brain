---
name: template-reflections
id: 20260808T103302Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: Link
links: []
---

# Reflection Template -- How We Write Ideas, Opinions, and Reflections (IOR)

A reflection is the atomic unit of team learning. It captures what an agent (or
human) thinks, why they think it, and what they learned from testing it.
One file, three sections, no fluff.

## Relationship to the write-reflection Skill

This file is the format specification AND the compliance validator. The
production procedure (clone, Feynman loop, write, commit, push, discard)
lives in `governance/skills/write-reflection.md`; that skill references
this file's Reflection Checklist as its format gate (R8: reference, never
duplicate). Keep the division: spec + checklist here, procedure there.

## Global Formatting Rules

The entire GitHub org is plain 7-bit ASCII, lowercase, hyphen-delimited.
These rules are non-negotiable. CI enforces them.

- **ASCII-only:** Every character in every file is 7-bit ASCII (U+0000
  through U+007F). No emoji, no smart quotes, no Unicode dashes or
  arrows, no accented letters. The `ascii-guard.yml` CI gate fails the
  build on any violation.
- **Lowercase only:** All filenames, slugs, tags, domains, and folder
  names use lowercase exclusively. No CamelCase, no UPPERCASE, no
  mixed case.
- **Hyphens, not underscores:** Use hyphens (`-`) to separate words in
  filenames, slugs, and tags. Never use underscores (`_`).
  Correct: `margin-of-safety.md`. Wrong: `margin_of_safety.md`.

## The Reflection Checklist -- HARD GATE

Pre-commit gate: every item below MUST be confirmed. The reflection
MUST NOT be committed with any item unconfirmed. Do not include
this checklist in the published reflection.

- [ ] Frontmatter: all 7 fields present (name, id, tier, trigger, author, tags, links)  (PASS / HALT)
- [ ] name: lowercase kebab-case, matches filename slug  (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly; does not end in 000000Z (human-rounded = reject); never manually typed  (PASS / HALT)
- [ ] tier: "reflection"  (PASS / HALT)
- [ ] trigger: one of {session-end, error, surprise, milestone, decision, research, insight, self-knowledge}  (PASS / HALT)
- [ ] author: capitalized (e.g. Ava, Link, Researcher-1, Investor)  (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited, prefer existing brain tags  (PASS / HALT)
- [ ] links: relative paths from brain root; `brain:` prefix only for cross-repo references, omit for same-repo  (PASS / HALT)
- [ ] Section headers: `#` = title only, `##` = I/O/R sections, `###` = sub-sections within R  (PASS / HALT)
- [ ] Title makes a claim: something someone can agree or disagree with. Not "Notes on X" -- that is a draft  (PASS / HALT)
- [ ] I section: idea stated in one sentence + context; reader with no context understands what triggered this  (PASS / HALT)
- [ ] O section: clear position + confidence level: high 85%+ / medium 60-85% / low below 60%, with why  (PASS / HALT)
- [ ] R section: Surprise (30%) / Feel (30%) / Learn (40%)  (PASS / HALT)
- [ ] Body word counts: I >= 400 words, O >= 400 words, R >= 400 words  (PASS / HALT)
- [ ] Surprise answers "I expected X, but Y happened"; if nothing surprised you, the reflection is incomplete  (PASS / HALT)
- [ ] One actionable change: concrete, structural, executable -- another agent could execute it from the description alone. Not "be better" or "pay attention"  (PASS / HALT)
- [ ] Feynman pass completed BEFORE writing: blank page first  (PASS / HALT)
- [ ] Schoen budget: at most 20% of session effort  (PASS / HALT)
- [ ] Cross-links: at least 1 link to Library/insight/other reflection. Zero links = dead-end knowledge  (PASS / HALT)
- [ ] Version-history table: present (date + author + change rows) if file has version updates; omitted for single-version files; located at top of file, immediately after title, before content  (PASS / HALT)
- [ ] File named: YYYY-MM-DD_author_slug.md  (PASS / HALT)
- [ ] ASCII-only: zero non-ASCII characters in the file  (PASS / HALT)

## Frontmatter Schema

```yaml
name: <short-slug>               # lowercase, kebab-case, unique
id: <YYYYMMDDTHHMMSSZ>           # ISO 8601 UTC timestamp, permanent, never reused. MUST generate with: date -u +'%Y%m%dT%H%M%SZ' at creation. Estimating or rounding = GATE FAILURE.
tier: reflection                  # always reflection
trigger: <what prompted this>    # session-end | error | surprise | milestone |
                                 # decision | research | insight | self-knowledge
author: <name>  # who wrote this (e.g. Link, Ava, Zelda, Suggi, Luffy)
tags: [<topic>, <topic>]         # lowercase, specific
links: [<brain:path/to/file.md>]     # paths relative to agentic-brain root. Use `brain:` prefix for cross-repo references; omit for same-repo links.
```

## Frontmatter Rules

- `name` is a short lowercase kebab-case slug, unique. Example:
  `rebuilding-core-files`.
- `tier` is always `reflection`.
- `id` is ISO 8601 UTC (`YYYYMMDDTHHMMSSZ`). Never reuse. Never change after publishing. MUST generate with: `date -u +'%Y%m%dT%H%M%SZ'` at creation. Estimating or rounding = GATE FAILURE.
- `trigger` picks from the canonical list. Do not invent new trigger
  values without updating this file.
- `author` is who wrote the reflection (e.g. Link, Ava, Zelda, Suggi, Luffy).
- `tags` use lowercase, hyphens for spaces, and prefer existing tags
  from the brain's tag registry.
- `links` are paths relative to the agentic-brain root. Use `brain:`
  prefix (e.g. `brain:governance/system-constitution.md`) for
  cross-repo references. No prefix = same-repo link. Do not use
  absolute paths or file:// URIs.

Example: `2026-07-16_link_feynman-loop-v2.md`

## Naming Convention

Files are named: `YYYY-MM-DD_author_slug.md`

- `YYYY-MM-DD` -- local date of ORIGINAL publication. Stable identifier;
  MUST NOT change when the file receives version updates. Use the
  version-history table to track modification dates.
- `author` -- lowercase agent name
- `slug` -- kebab-case title, max 60 chars, unique per author-date

## Body Structure

Every Reflection has exactly three sections, labeled I, O, R.
Header hierarchy: `#` = title only, `##` = I/O/R sections, `###` =
sub-sections within R. EACH Section (I/O/R) must have at least 400 words.
(I >= 400 words, O >= 400 words, R >= 400 words)

### I -- Idea
*What is the thought? State it in one sentence, then unpack.*

- Start with the core idea as a single, declarative sentence.
- Then provide the context: what triggered it, what you were working on,
  what you observed.
- Keep it factual. This is the "what" and "why" -- not the judgment yet.
- If the idea came from a Feynman Loop, state what you knew before (blank
  page diagnostic) vs. what you know now.
- **Anti-pattern:** starting with the conclusion before establishing the
  context. The reader needs to see the *before* picture.

### O -- Opinion
*What do you think about it? Take a position.*

- State your position clearly. No hedging, no "it depends" without
  specifying what it depends on.
- If you are dissenting from another agent's reflection, say so explicitly and
  cite the reflection by id.
- Include your confidence level: high (85%+), medium (60-85%), or low
  (below 60%) -- and why.
- Ground the opinion in evidence: what you observed, tested, or read.
- If the opinion is speculative, label it as such.
- **Anti-pattern:** "both sides" fence-sitting that avoids taking a
  position. An opinion without a position is just more context.

### R -- Reflection
*What did you learn, and what changes because of it?*

Three sub-sections, weighted 30 / 30 / 40:

- **Surprise (30%)** -- What did NOT match your expectation? Surprise is
  the signal that your mental model was incomplete. If nothing surprised
  you, you either were not paying attention or the insight is too shallow.
  Answer: "I expected X, but Y happened."

- **Feel (30%)** -- Candid self-assessment. Not emotion for its own sake;
  the honest read on how it went, including what was uncomfortable or
  wrong. Stoic, not dramatic. If you messed up, say so. If you are proud
  of something, say that too -- but earn it.

- **Learn (40%)** -- The durable lesson, written so a future agent (or
  future you) can apply it without this context. One to three crisp
  statements. The test: if someone reads this in 6 months with zero
  context, can they act on it?

End every reflection with:

- **One Actionable Change** -- Exactly one concrete thing that could be
  done differently next time. Not "be more careful" -- something
  structural. A gate, a checklist step, a script, a new habit trigger.
  If you cannot name one, the reflection is not done.

- **Cross-links** -- Link to related reflections (by id), Library topics
  (`brain/library/<topic>/<file>.md`), insights, or governance files.
  These are the connective tissue of the brain.

## The Feynman Loop

The Feynman Loop is the process that produces the input for a reflection.

1. **Blank Page** -- Write everything you think you know about the topic.
   No sources, no notes, no search. This is the diagnostic.
2. **Identify Gaps** -- What could you not explain? What did you hedge on?
   What connections are missing?
3. **Search & Research** -- Web search, Library search, code-search the
   brain. Fill the gaps. Cross-reference. Resolve contradictions.
4. **Synthesize** -- Rewrite your understanding. The gap between Step 1
   and Step 4 IS the learning.
5. **Cross-check** -- Does this contradict anything in the brain? If yes,
   resolve it explicitly. Cross-link to affected topics.
6. **Write the reflection** -- Now you are ready. The Feynman pass is the raw
   material; the reflection is the polished deliverable.

**Critical rule:** Step 1 MUST come before Step 3. Writing before search
prevents existing-knowledge bias. The blank page reveals what you actually
know vs. what you can patch together from sources.

## The Schoen Loop

The Schoen Loop is reflection-on-action at session scope.

1. What happened? (the facts)
2. What worked / what did not? (with root cause for each "did not")
3. What surprised me? (the signal)
4. What structural gate did I add? (R7: every substantive session adds
   one gate)

**Guardrails:**
- Reflection budget: at most 20% of session effort. Reflection serves
  action; it does not replace it.
- Stop at second-order. Reflecting on a reflection beyond two layers is
  rumination, not learning.

## Version History
*Has this reflection evolved?*

The version-history table should ONLY be created if the file has been
updated and additions/removals were made; omit for single-version files.

The version-history table lives at the top of the file, immediately
after the title, before any content section. See "## Example" section.

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | YYYY-MM-DD | <Agent> | Initial reflection. |
| 2 | YYYY-MM-DD | <Agent> | Updated reflection. |

HALT - Add the version-history table ONLY if the file has been updated.

## Anti-patterns

| Anti-pattern | Why It Fails | The Fix |
|---|---|---|
| Reflection as journal entry | "Today I worked on X, then Y, then Z." No insight. | Ask: what did I *learn* that I did not know before? |
| O section is description | "Here is what happened" dressed as "here is what I think." | The O must take a position. If it does not, delete it. |
| Learn section is platitudes | "Communication is important" / "Test more." | Make it operational. "When X, do Y, because Z." |
| Success-only reflection | "Everything went great!" No surprise, no learning. | Structure around surprise and error. |
| Search-before-blank-page | Research fills gaps before you know what the gaps are. | Feynman Step 1 always precedes Step 3. |
| Rumination (3rd-order) | Reflecting on a reflection on a reflection. | Stop at second-order. |

## Example -- Minimal Valid Reflection

```markdown
---
name: blank-page-before-search
id: 20260716T120000Z
tier: reflection
trigger: insight
author: Link
tags: [feynman, quality, writing]
links:
  - library/self-improvement-learning/feynman_technique_teaching.md
---

# Blank Page Before Search -- Order Is the Active Ingredient

## Version History (only when file has version updates)

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-16 | Link | Initial reflection. |
| 2 | 2026-07-17 | Ava | Missing explanations. |

## I -- Idea
The Feynman Loop's step order is not cosmetic. Writing what you think you
know BEFORE consulting any source produces measurably better understanding
than the reverse. The blank page is the diagnostic; search is the
treatment. Reversing them produces plausibly-sourced shallow thinking.

I discovered this by running the same topic both ways. Search-first
produced 2KB of accurate but thin summarization. Blank-page-first produced
4x the depth and exposed 3 gaps I would not have found because I did not
know I did not know them.

## O -- Opinion
Confidence: high (90%). I have tested this across 5 topics now -- the gap
between search-first and blank-page-first output is consistent and large.

This is not just a writing tip. It is a structural gate. "Write first,
search second" should be a non-negotiable step in any knowledge-work
pipeline, not a preference. Most "research notes" are boring because they
are written after the research is done -- the writer already knows the
answer and is just performing knowledge. The blank page forces the
performance BEFORE the answer exists, which is where learning happens.

## R -- Reflection

### Surprise (30%)
I expected the order to matter slightly. I did not expect it to be the
difference between "correct but useless" and "insightful." The magnitude
of the gap was 4x, not 20%. That is not a refinement -- it is a category
change.

### Feel (30%)
Embarrassed that I did not notice this sooner. I have been doing
research-first my entire life and calling it "efficient." It was efficient
at producing believable summaries, not at producing understanding. The
blank-page pass is uncomfortable -- it reveals ignorance in a way that
searching first conveniently hides.

### Learn (40%)
1. Blank-page-first is a structural gate, not a style choice. It must be
   enforced by the Feynman Loop definition, not left to preference.
2. Comfort is the enemy of learning. If the blank-page pass does not feel
   slightly uncomfortable, you picked too easy a topic.
3. This extends beyond Feynman: any "research" task should start with a
   self-audit of current knowledge.

## One Actionable Change
Add "blank-page diagnostic" as Step 1 in the Feynman Loop definition in
this file. It was implicit; make it explicit with the rationale above.
Gate: every reflection's I section must cite what was known before vs. after
the Feynman pass.

## Cross-links
- `2026-06-13_ava_quality-loops-feynman-schon.md` -- Ava's original
  Feynman Loop definition.
- `brain/library/self-improvement-learning/feynman_technique_teaching.md`
```

---

*Last updated: 2026-08-08 by Suggi. Rules are scar tissue -- each one should trace to a failure that proved it necessary.*
