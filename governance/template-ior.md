---
name: template-ior
id: 20260618T120014Z
tier: core-template
lock: approval-required
approved_by: Suggi
author: link
links:
---

# IOR Rules -- How We Write Ideas, Opinions, and Reflections

An IOR is the atomic unit of team learning. It captures what an agent (or
human) thinks, why they think it, and what they learned from testing it.
One file, three sections, no fluff.

## When to Write an IOR

**Write one when:**
- A session produces a durable insight (Feynman Loop completed).
- Something surprised you -- your model was incomplete.
- A decision was made that changes how we operate.
- A failure taught a reusable lesson.
- You read/researched something and formed a strong opinion.

**Do NOT write one when:**
- The work was routine with nothing learned.
- You are logging for the sake of logging. Quality over volume.
- The insight already exists in an IOR -- version-update that one instead.

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

## The Feynman Loop (How Ideas Become IORs)

The Feynman Loop is the *process* that produces the *input* for an IOR.
An IOR without a Feynman pass is a journal entry. A Feynman pass without
an IOR is wasted effort.

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
know vs. what you can patch together from sources. Reversing the order
produces plausibly-sourced shallow thinking.

## The Schoen Loop (How Sessions Produce IORs)

The Schoen Loop is reflection-on-action at session scope. Every substantive
session ends with a Schoen pass:

1. What happened? (the facts)
2. What worked / what did not? (with root cause for each "did not")
3. What surprised me? (the signal)
4. What structural gate did I add? (R7: every substantive session adds
   one gate)

If steps 2-4 produce something worth keeping, it becomes an IOR.

**Guardrail:** Reflection budget at most 20% of session effort. Reflection
serves action; it does not replace it.

**Guardrail:** Stop at second-order. Reflecting on a reflection beyond two
layers is rumination, not learning.

## Frontmatter Schema

```yaml
type: reflection
id: <YYYYMMDDTHHMMSSZ>           # ISO 8601 UTC timestamp, permanent, never reused
date: <YYYY-MM-DD>               # local date of writing
author: <link|ava|zelda|suggi|luffy>  # who wrote this IOR
trigger: <what prompted this>    # session-end | error | surprise | milestone |
                                 # decision | research | insight | self-knowledge
format: i+o+r
aliases: []                      # alternative titles for search
tags: [<topic>, <topic>]         # lowercase, specific
links: [<brain/lib/file.md>]     # paths relative to brain root
```

**Rules for frontmatter:**
- `id` is ISO 8601 UTC (`YYYYMMDDTHHMMSSZ`). Never reuse an id. Never
  change an id after publishing.
- `author` is who wrote the IOR. The author list is {link, ava, zelda,
  suggi, luffy}. Suggi is the human; others are agents.
- `trigger` picks from the canonical list. Do not invent new trigger
  values without updating this rules file.
- `tags` use lowercase, hyphens for spaces, and prefer existing tags
  from the brain's tag registry. Tags are how future-you finds this.
- `links` are relative paths from the brain root. Do not use absolute
  paths or file:// URIs.
- `aliases` are alternative search titles. Optional but useful when the
  IOR title uses domain-specific terms.

## Naming Convention

Files are named: `YYYY-MM-DD_author_slug.md`

- `YYYY-MM-DD` -- local date (not the id timestamp)
- `author` -- lowercase agent name
- `slug` -- kebab-case title, max 60 chars, unique per author-date

Example: `2026-07-16_link_feynman-loop-v2.md`

## Versioning -- Update, Do Not Duplicate

If a new IOR covers a topic at least ~75% similar to an existing one (same
core lesson, overlapping conclusions), do NOT create a new file. Instead:

1. Add a `## vN -- YYYY-MM-DD -- <author>` block at the bottom of the
   existing IOR with the new/changed insight.
2. Sign added content inline with `**(author):**` when inserting into
   another author's sections.
3. Add a `version-history` table at the end.

Only create a new file for a genuinely distinct lesson.

## Quality Gates (Before Publishing)

Every IOR passes these checks before it is committed:

- **G1 -- Idempotent Title:** The title makes a claim someone can agree
  or disagree with. Not "Notes on X" -- that is a draft.
- **G2 -- I Section Completeness:** Would someone with no context
  understand what triggered this?
- **G3 -- O Section Has a Spine:** Is there a clear position, not just
  description? Does it cite a confidence level?
- **G4 -- R Section Has a Surprise:** If nothing surprised you, the
  reflection is incomplete. "Everything went as expected" is a red flag.
- **G5 -- Actionable Change Is Concrete:** Not "be better" or "pay
  attention." Something another agent could execute from the description
  alone.
- **G6 -- Cross-links Exist:** At least one link to a Library topic,
  insight, or another IOR. Zero links = dead-end knowledge.
- **G7 -- Feynman Pre-write Rule:** The I section was written AFTER a
  blank-page diagnostic, not assembled from search results.
- **G8 -- Schoen Budget Rule:** Total effort spent on this IOR at most
  20% of the session that produced it. If you are polishing, stop.

## Anti-patterns

| Anti-pattern | Why It Fails | The Fix |
|---|---|---|
| IOR as journal entry | "Today I worked on X, then Y, then Z." No insight. | Ask: what did I *learn* that I did not know before? |
| O section is description | "Here is what happened" dressed as "here is what I think." | The O must take a position. If it does not, delete it. |
| Learn section is platitudes | "Communication is important" / "Test more." | Make it operational. "When X, do Y, because Z." |
| Success-only reflection | "Everything went great!" No surprise, no learning. | Structure around surprise and error. Success is curation. |
| Search-before-blank-page | Research fills gaps before you know what the gaps are. | Feynman Step 1 always precedes Step 3. No exceptions. |
| Rumination (3rd-order) | Reflecting on a reflection on a reflection. | Stop at second-order. Write the IOR; do not write an IOR about the IOR. |

## Lifecycle

```
Draft -> IOR -> (version-updates) -> promoted to Library OR pruned
```

- **Draft:** Written but not yet committed. Fails any quality gate.
- **IOR:** Committed, passes all gates, cross-linked, indexed.
- **Version-updated:** At least 75% similar new insight -> appended to
  existing IOR. IORs compound in place.
- **Promoted:** A reflection that hardens into reusable knowledge gets
  extracted into a Library topic. The IOR stays as provenance.
- **Pruned:** Stale, superseded, or low-signal IORs are removed during
  periodic consolidation. Reflections are working memory, not permanent
  storage. The Library is permanent; IORs are allowed to age out.

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
type: reflection
id: 20260716T120000Z
date: 2026-07-16
author: link
trigger: insight
format: i+o+r
aliases: []
tags: [feynman, quality, writing]
links: [brain/library/self-improvement-learning/feynman_technique_teaching.md]
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
pipeline, not a preference. The reason most "research notes" are boring
is that they are written after the research is done -- the writer already
knows the answer and is just performing knowledge. The blank page forces
the performance BEFORE the answer exists, which is where learning
actually happens.

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
   slightly uncomfortable (because you do not know enough), you picked
   too easy a topic.
3. This extends beyond Feynman: any "research" task should start with a
   self-audit of current knowledge. Garbage in = garbage out applies to
   your own brain too.

## One Actionable Change
Add "blank-page diagnostic" as Step 1 in the Feynman Loop definition in
this rules file. It was implicit; make it explicit with the rationale
above. Gate: every IOR's I section must cite what was known before vs.
after the Feynman pass.

## Cross-links
- `2026-06-13_ava_quality-loops-feynman-schon.md` -- Ava's original
  Feynman Loop definition.
- `brain/library/self-improvement-learning/feynman_technique_teaching.md`
```

## The IOR File Checklist (Copy-Paste for Every New IOR)

```
[ ] Frontmatter complete (all 9 fields)
[ ] id is UTC timestamp, never used before
[ ] Title makes a claim
[ ] I section: idea stated in one sentence + context
[ ] O section: clear position + confidence level
[ ] R section: Surprise (30%) / Feel (30%) / Learn (40%)
[ ] Surprise answers "I expected X, but Y happened"
[ ] One actionable change (concrete, structural, executable)
[ ] Cross-links: at least 1 link to Library/insight/other IOR
[ ] Feynman pass completed BEFORE writing (blank page first)
[ ] Schoen budget: at most 20% of session effort
[ ] File named: YYYY-MM-DD_author_slug.md
[ ] Added to _index.md (newest first)
[ ] ASCII-only: zero non-ASCII characters in the file
```

---

*Last updated: 2026-07-16 by link. This file governs all IOR creation.
Amend it through the same process: propose, test against at least one
real IOR, then update. Rules are scar tissue -- each one should trace
to a failure that proved it necessary.*
