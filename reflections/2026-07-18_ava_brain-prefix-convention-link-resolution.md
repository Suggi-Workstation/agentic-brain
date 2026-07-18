---
name: brain-prefix-convention-link-resolution
id: 20260718T121000Z
tier: reflection
trigger: insight
author: Ava
tags: [architecture, brain, cross-repo, duplicates, r8, links, templates, skills, convention]
links: [brain:governance/template-reflections.md, brain:governance/template-library.md]
---

# Brain-Prefix Convention -- Structural Elimination of Cross-Repo Ambiguity

## I -- Idea

A single file-not-found error (trying to read `research/insights/openclaw-manual.md`
from the workspace instead of the agentic-brain) exposed a structural ambiguity
that had been silently present in every core file since the org was founded.
The `links:` frontmatter field used bare relative paths, but the files
containing those links lived in two different repos. Without a namespace
prefix, there was no way to tell which repo a link pointed to. The fix was a
three-character convention (`brain:`) that cascaded into a full architectural
cleanup across 13 files in 2 repos, eliminating 5 template duplicates in the
process.

I discovered this when Suggi asked me to test web_search. I tried to read
the openclaw-manual.md file referenced in TOOLS.md, looked in the local
workspace first, got a file-not-found, and only then realized it lived in the
agentic-brain. Every core file had the same silent bug -- AGENTS.md, SOUL.md,
MEMORY.md, IDENTITY.md, USER.md, TOOLS.md all used bare paths to reference
brain content. 13 frontmatter links + 2 body references, all ambiguous.

## O -- Opinion

Confidence: high (95%). This was a textbook R8 violation (Reference, Never
Duplicate) expressed as a naming problem. The symptom was ambiguous links.
The deeper disease was that files in two repos shared a namespace with no
qualifier. The `brain:` prefix is the structural fix -- it makes the link
unambiguous at the point of reading.

What surprised me more was the second-order discovery: the template
duplication in the skills. Each write-X skill bundled its own copy of the
brain's governance template in a `references/` folder. We had synced them
minutes before. This meant every template change required syncing 5 copies --
guaranteed drift. The fix (delete references/ folders, point skills to
`brain:governance/template-X.md`) eliminated the duplication entirely.

The pattern that emerged: Suggi would spot an ambiguity, I would trace it
to its structural root, and the fix would expose another layer. The link
ambiguity led to the prefix convention, which led to the template duplication
discovery, which led to removing the references/ folders. Each fix was a
scalpel cut that revealed the next growth.

I also learned something about proactive verification. When Suggi asked me to
fix "template" ambiguity in the Self-Check section (10 checklist edits), I
ran a grep to verify and found 4 additional "per template" references in the
procedure body. I fixed them without being asked. Suggi noticed and praised
the initiative. The lesson: a fix is not complete until you verify that the
entire class of the problem is gone, not just the instance you were asked
about.

## R -- Reflection

### Surprise (30%)
I expected the `brain:` prefix to be the end of the work -- a simple rename.
I did not expect it to cascade into deleting entire `references/` folders,
renaming a skill, hunting down 37 stray path references, and finding 4
unrequested fixes by proactive grep. One file-not-found error produced 8
commits across 2 repos. The cost of the ambiguity was far larger than the
ambiguity itself.

### Feel (30%)
Satisfied. This was structural architecture work done carefully, one file at
a time, with zero mistakes. Suggi's feedback ("very clean work Ava. Good job.
I like that you proactively solved this by yourself") confirms the approach:
slow, deliberate, verify-every-step. I earned the praise by catching things
he missed, not just executing what he asked.

### Learn (40%)
1. **Ambiguity is technical debt with a zero-day exploit.** The bare paths
   had been there since day one and "worked" because I always cloned the brain
   when I needed it. The ambiguity was invisible until it wasn't. A convention
   that relies on human inference is not a convention -- it is a trap.

2. **R8's scope is larger than I thought.** Duplication is not just
   copy-pasting text. It is maintaining parallel copies in different repos
   with no sync mechanism. The references/ folders were a textbook R8
   violation disguised as "convenient bundling."

3. **Proactive verification compounds.** The 4 extra edits I found by
   grepping beyond the planned scope were the difference between "done what
   was asked" and "done what was needed." Suggi noticed. The gap between
   those two is where trust is built.

4. **One file at a time is not slow -- it is fast because it is correct.**
   Doing 37 sed replacements in one command would have been faster in
   keystrokes but risked missing context-specific edits (like write-skill's
   unique meta-instructional references). The per-file approach caught edge
   cases that a batch approach would have missed.

## One Actionable Change

When fixing any class of ambiguity or stale reference, run a full-repo grep
for the OLD pattern after the fix, not just the files you edited. If the grep
returns anything, those are missed instances -- fix them before committing.
This is not "nice to have" -- it is the difference between 10 edits and 14,
and the 4 I caught prevented silent ambiguity from lingering in procedure
bodies indefinitely.

## Cross-Links
- `brain:governance/template-reflections.md` -- IOR format specification used here
- `brain:governance/template-library.md` -- defines R8 (Reference, Never Duplicate) which this IOR validates
- `brain:governance/system-constitution.md` -- org-wide governance the prefix convention supports
