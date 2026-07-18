---
name: template-reflections
id: 20260618T120014Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: Suggi
links:
---

# IOR Rules -- How We Write Ideas, Opinions, and Reflections

An IOR is the atomic unit of team learning. It captures what an agent (or
human) thinks, why they think it, and what they learned from testing it.
One file, three sections, no fluff.

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

## The Three-Section Format

Every IOR has exactly three sections, labeled I, O, R.

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
- If you are dissenting from another agent's IOR, say so explicitly and
  cite the IOR by id.
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

End every IOR with:

- **One Actionable Change** -- Exactly one concrete thing that will be
  done differently next time. Not "be more careful" -- something
  structural. A gate, a checklist step, a script, a new habit trigger.
  If you cannot name one, the reflection is not done.

- **Cross-links** -- Link to related IORs (by id), Library topics
  (`brain/library/<topic>/<file>.md`), insights, or governance files.
  These are the connective tissue of the brain.

## The Feynman Loop

The Feynman Loop is the process that produces the input for an IOR.

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
6. **Write the IOR** -- Now you are ready. The Feynman pass is the raw
   material; the IOR is the polished deliverable.

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
- `author` is who wrote the IOR (e.g. Link, Ava, Zelda, Suggi, Luffy).
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

## Version-Update Self-Check

When updating an existing IOR (per the Versioning section below), use
THIS checklist INSTEAD of the Pre-Commit Self-Check. The original id
and filename MUST NOT change.

Pre-commit gate: every item below MUST be confirmed. The IOR
MUST NOT be committed with any item unconfirmed.

- [ ] Original id preserved (never changed after publishing)
- [ ] Original filename preserved (cross-links depend on stable paths)
- [ ] Version block added beneath the last section: ## vN -- YYYY-MM-DD -- author
- [ ] Version-history table at end of file: new row added (version, date, author, change)
- [ ] Inline additions signed -- **(author):** -- when inserting into another author's sections
- [ ] All 8 quality gates (G1-G8) re-verified against new content
- [ ] Cross-links updated if new content adds references
- [ ] ASCII-only verified for all new content

## Versioning -- Update, Do Not Duplicate

If a new IOR covers a topic at least ~75% similar to an existing one (same
core lesson, overlapping conclusions), do NOT create a new file. Instead:

1. Add a `## vN -- YYYY-MM-DD -- <author>` block at the bottom of the
   existing IOR with the new/changed insight.
2. Sign added content inline with `**(author):**` when inserting into
   another author's sections.
3. Add a `version-history` table at the end.

## Quality Gates

Every IOR passes these checks before it is committed:

- **G1 -- Title Makes a Claim:** The title is something someone can agree
  or disagree with. Not "Notes on X" -- that is a draft.
- **G2 -- I Section Completeness:** A reader with no context understands
  what triggered this.
- **G3 -- O Section Has a Spine:** A clear position, not just description.
  Cites a confidence level.
- **G4 -- R Section Has a Surprise:** If nothing surprised you, the
  reflection is incomplete.
- **G5 -- Actionable Change Is Concrete:** Not "be better" or "pay
  attention." Another agent could execute it from the description alone.
- **G6 -- Cross-links Exist:** At least one link to a Library topic,
  insight, or another IOR. Zero links = dead-end knowledge.
- **G7 -- Feynman Pre-write Rule:** The I section was written AFTER a
  blank-page diagnostic, not assembled from search results.
- **G8 -- ASCII-only:** Zero non-ASCII characters in the file.

## Anti-patterns

| Anti-pattern | Why It Fails | The Fix |
|---|---|---|
| IOR as journal entry | "Today I worked on X, then Y, then Z." No insight. | Ask: what did I *learn* that I did not know before? |
| O section is description | "Here is what happened" dressed as "here is what I think." | The O must take a position. If it does not, delete it. |
| Learn section is platitudes | "Communication is important" / "Test more." | Make it operational. "When X, do Y, because Z." |
| Success-only reflection | "Everything went great!" No surprise, no learning. | Structure around surprise and error. |
| Search-before-blank-page | Research fills gaps before you know what the gaps are. | Feynman Step 1 always precedes Step 3. |
| Rumination (3rd-order) | Reflecting on a reflection on a reflection. | Stop at second-order. |

## Attribution -- Keeping Multi-Agent IORs Honest

When multiple agents contribute to an IOR (via version-updates):

- Original author's text is unsigned (it is theirs by default).
- Inline additions by other agents are signed: `**(ava):** ...`
- Version blocks are headed: `## v2 -- 2026-07-16 -- ava`
- At the bottom, a version-history table:

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-16 | link | Initial IOR. |
| 2 | 2026-07-18 | ava | Qualified the O section; added dissent on mechanism. |

## Example -- Minimal Valid IOR

```markdown
---
name: blank-page-before-search
id: 20260716T120000Z
tier: reflection
trigger: insight
author: Link
tags: [feynman, quality, writing]
links: [brain:library/self-improvement-learning/feynman_technique_teaching.md]
---

# Blank Page Before Search -- Order Is the Active Ingredient

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
Gate: every IOR's I section must cite what was known before vs. after
the Feynman pass.

## Cross-links
- `2026-06-13_ava_quality-loops-feynman-schon.md` -- Ava's original
  Feynman Loop definition.
- `brain/library/self-improvement-learning/feynman_technique_teaching.md`
```

## Pre-Commit Self-Check

Pre-commit gate: every item below MUST be confirmed. The IOR
MUST NOT be committed with any item unconfirmed. Do not include
this checklist in the published IOR.

- [ ] Frontmatter Schema complete (7 fields: name, id, tier, trigger, author, tags, links)
- [ ] Frontmatter Rules correctly applied (7 fields: name, id, tier, trigger, author, tags, links)
- [ ] id generated by running `date -u +'%Y%m%dT%H%M%SZ'` (not estimated, not rounded)
- [ ] Title makes a claim
- [ ] I section: idea stated in one sentence + context
- [ ] O section: clear position + confidence level
- [ ] R section: Surprise (30%) / Feel (30%) / Learn (40%)
- [ ] Surprise answers "I expected X, but Y happened"
- [ ] One actionable change (concrete, structural, executable)
- [ ] Cross-links: at least 1 link to Library/insight/other IOR
- [ ] Feynman pass completed BEFORE writing (blank page first)
- [ ] Schoen budget: at most 20% of session effort
- [ ] File named: YYYY-MM-DD_author_slug.md
- [ ] Added to _index.md (newest first)
- [ ] ASCII-only: zero non-ASCII characters in the file

---

*Last updated: 2026-07-16 by Suggi. This file governs all IOR creation.
Rules are scar tissue -- each one should trace to a failure that proved
it necessary.*
