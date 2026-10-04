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
production procedure (Feynman loop, read template, write, commit)
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

- [ ] Frontmatter: every Frontmatter Schema field present (name, id, tier, trigger, author, tags, links)  (PASS / HALT)
- [ ] name: lowercase kebab-case, matches filename slug  (PASS / HALT)
- [ ] id: exact output from `date -u +'%Y%m%dT%H%M%SZ'` exec call, pasted directly; does not end in 000000Z (human-rounded = reject); never manually typed  (PASS / HALT)
- [ ] tier: "reflection"  (PASS / HALT)
- [ ] trigger: one of {session-end, error, surprise, milestone, decision, research, insight, self-knowledge}  (PASS / HALT)
- [ ] author: capitalized (e.g. Ava, Link, Researcher-1, Investor)  (PASS / HALT)
- [ ] tags: lowercase, hyphen-delimited, prefer existing brain tags  (PASS / HALT)
- [ ] links: relative paths from repo root; `repo:` prefix only for cross-repo references, omit for same-repo  (PASS / HALT)
- [ ] Section headers: `#` = title only, `##` = I/O/R and the closing sections, `###` = sub-sections within R  (PASS / HALT)
- [ ] Title makes a claim: something someone can agree or disagree with. Not "Notes on X" -- that is a draft  (PASS / HALT)
- [ ] I section: the purpose of the session, topic or theme stated in one sentence + context; reader with no context understands what triggered this  (PASS / HALT)
- [ ] O section: clear position + confidence level: high 85%+ / medium 60-85% / low below 60%, with why; at least one alternative view or approach weighed  (PASS / HALT)
- [ ] R section: Surprise (30%) / Feel (30%) / Learn (40%)  (PASS / HALT)
- [ ] Body word counts: I >= 600 words, O >= 600 words, R >= 600 words, Key Learning and Improvement >= 200 words  (PASS / HALT)
- [ ] Prose: every section except Cross-links is paragraphs; no bullet or numbered lists  (PASS / HALT)
- [ ] Surprise answers "I expected X, but Y happened"; if nothing surprised you, the reflection is incomplete  (PASS / HALT)
- [ ] Key Learning and Improvement: the major learning in brief + one concrete improvement, offered as a suggestion; it need not be implemented. Not "be better" or "pay attention"  (PASS / HALT)
- [ ] Feynman pass completed BEFORE writing: blank page first  (PASS / HALT)
- [ ] References: at least 1 internal Library/insight/reflection cross-link with a short description; no IDs repeated beside paths or external website links  (PASS / HALT)
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
links: [<path/to/file.md>]     # paths relative to repo root. Cross-repo references use the `repo:` prefix; omit for same-repo links.
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
- `links` are paths relative to the repo root. Cross-repo references use the `repo:` prefix -- the token before `:` is
the exact GitHub repo name (see the Cross-Repo Link Convention in
`governance/system-blueprint.md`). Same-repo links carry no prefix. Do not use
  absolute paths or file:// URIs.

Example: `2026-07-16_link_feynman-loop-v2.md`

## Naming Convention

Files are named: `YYYY-MM-DD_author_slug.md`

- `YYYY-MM-DD` -- local date of ORIGINAL publication. Stable identifier;
  MUST NOT change when the file is updated.
- `author` -- lowercase agent name
- `slug` -- kebab-case title, max 60 chars, unique per author-date

## Body Structure

Every reflection has three core sections, I, O and R, followed by Key
Learning and Improvement and Cross-links. Header hierarchy: `#` = title
only, `##` = these section headings, `###` = sub-sections within R.

Minimum words: I >= 600, O >= 600, R >= 600 (Surprise, Feel and Learn
together), Key Learning and Improvement >= 200. Every section except
Cross-links is continuous prose: paragraphs, no bullet or numbered lists.
Depth comes from connecting causes, judgments and lessons; lists cut
those connections.

The helper questions under each section are prompts, not a form. Answer
those that apply, in your own order, in prose. They exist to take the
writing deeper, not to fill the word count.

### I -- Idea
*What was the idea: the purpose of the session, topic or theme?*

- Open with one sentence that states what the work set out to do or to
  understand, and why it mattered.
- Then give the context a reader with none needs: what triggered the
  work, what you were working on, your role, what you did, and what
  happened.
- Keep it factual. This is the "what" and "why" -- not the judgment yet.
- State what you knew before the Feynman Loop's blank page and what you
  know now.
- Helper questions: What problem, question or goal started this, and who
  raised it? What did success look like at the start, and which
  constraints applied? What was already known, decided or assumed? What
  were the main steps, and what did each produce? Who or what else
  shaped the work: Suggi, other agents, tools, sources? Did the purpose
  shift along the way, and why?
- **Anti-pattern:** starting with the conclusion before establishing the
  context. The reader needs to see the *before* picture.

### O -- Opinion
*What do you think about it? Take a position.*

- State your position clearly. No hedging, no "it depends" without
  specifying what it depends on.
- Judge the work: what worked, what did not, and why.
- Weigh at least one alternative view or approach, and say why you
  accept or reject it.
- If you are dissenting from another agent's reflection, say so explicitly and
  reference the reflection by repository path.
- Include your confidence level: high (85%+), medium (60-85%), or low
  (below 60%) -- and why. State what evidence would change your mind.
- Ground the opinion in evidence: what you observed, tested, or read.
- Keep external website citations in supporting research, not the reflection.
- If the opinion is speculative, label it as such.
- Helper questions: Was the approach right for the purpose, and what
  would a better one have looked like? What was the root cause of each
  thing that did not work? How strong is the evidence for your position,
  and where is it thin? Where do you agree or disagree with Suggi,
  another agent, or a prior reflection or Library topic? What follows if
  you are right, and what if you are wrong?
- **Anti-pattern:** "both sides" fence-sitting that avoids taking a
  position. An opinion without a position is just more context.

### R -- Reflection
*What did you learn, and what changes because of it?*

Three sub-sections, each written as paragraphs, weighted 30 / 30 / 40:

- **Surprise (30%)** -- What did NOT match your expectation? Surprise is
  the signal that your mental model was incomplete. If nothing surprised
  you, you either were not paying attention or the insight is too shallow.
  Answer: "I expected X, but Y happened", then explain why your model was
  wrong or incomplete. Helper questions: What did you predict at the
  start that turned out wrong? What was harder or easier than expected?
  What did a tool, source, person or agent reveal that you had not
  anticipated? Which assumption failed, and where did it come from?

- **Feel (30%)** -- Candid self-assessment. Not emotion for its own sake;
  the honest read on how it went and how you judge your own conduct
  during the work, including what was uncomfortable or wrong. Stoic, not
  dramatic. If you messed up, say so. If you are proud of something, say
  that too -- but earn it. Helper questions: What are you satisfied with,
  and does the evidence earn it? What was uncomfortable, and what does
  the discomfort point to? Where did you hesitate, cut a corner or claim
  more than you had verified? How would Suggi or a peer judge your
  conduct, and would they be right?

- **Learn (40%)** -- The durable lesson, developed in prose: what the
  lesson is, why it holds, and where it applies and where it does not,
  written so a future agent (or future you) can apply it without this
  context. The test: if someone reads this in 6 months with zero
  context, can they act on it? Helper questions: What general principle
  does this case show? What causes make it true? Where else, in the
  system or in other domains, does it apply? Where would it mislead?
  Does it confirm, extend or contradict an earlier lesson, reflection or
  Library topic?

### Key Learning and Improvement
*What is the major learning, and what can be improved?*

At least 200 words of prose. Name the major learning in brief, without
repeating Learn, then one concrete improvement the author would make next
time, offered as a suggestion. It need not be a new rule or gate, and it
need not be implemented. Not "be more careful" -- name the specific
change. Helper questions: At which step would you act differently, and
how? What would the change cost, and what would it prevent? How would you
know it worked?

### Cross-links
Reference related reflections, Library topics, insights, or governance
files by repository path with a short description. Keep permanent IDs in
frontmatter, not repeated beside the paths.

## The Feynman Loop

The Feynman Loop produces the raw material for a reflection. Its procedure
and self-check live in the shared `loop-feynman` skill (canonical:
`governance/skills/loop-feynman.md`).

## Anti-patterns

| Anti-pattern | Why It Fails | The Fix |
|---|---|---|
| Reflection as journal entry | "Today I worked on X, then Y, then Z." No insight. | Ask: what did I *learn* that I did not know before? |
| O section is description | "Here is what happened" dressed as "here is what I think." | The O must take a position. If it does not, delete it. |
| Learn section is platitudes | "Communication is important" / "Test more." | Make it operational. "When X, do Y, because Z." |
| Success-only reflection | "Everything went great!" No surprise, no learning. | Structure around surprise and error. |
| Search-before-blank-page | Research fills gaps before you know what the gaps are. | Feynman Step 1 always precedes Step 3. |
| Rumination (3rd-order) | Reflecting on a reflection on a reflection. | Stop at second-order. |
| Bullet-point reflection | Lists cut the links between cause, judgment and lesson; the result reads as notes. | Write every section except Cross-links as paragraphs. |
| Padding to the word count | Repetition and filler reach the minimum without adding thought. | Use the helper questions to go deeper: causes, alternatives, limits. |

## Example -- Minimal Structure

Shows the layout and voice only; each section is shorter than the word
minimums.

```markdown
---
name: blank-page-before-search
id: 20260716T120000Z
tier: reflection
trigger: insight
author: Link
tags: [feynman, quality, writing]
links:
  - library/education-learning/feynman-technique-and-learning-heuristics.md
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
Blank-page-first is a structural gate, not a style choice: the order
itself produces the understanding, so it must be enforced by the Feynman
Loop definition rather than left to preference. Comfort is a warning
sign; if the blank-page pass does not feel slightly uncomfortable, the
topic was too easy to teach anything. The lesson extends beyond Feynman:
any research task should start with a self-audit of current knowledge.

## Key Learning and Improvement
The order of the Feynman Loop is the active ingredient. Next time I would
write the blank-page diagnostic before opening any source, and in the I
section state what I knew before the pass and what I knew after it.

## Cross-links
- `library/education-learning/feynman-technique-and-learning-heuristics.md`
  -- Library topic on the Feynman Technique.
- `governance/skills/loop-feynman.md` -- the Feynman Loop procedure.
```

---

*Last updated: 2026-10-04 by Morpheus, approved by Suggi. Rules are scar tissue -- each one should trace to a failure that proved it necessary.*
