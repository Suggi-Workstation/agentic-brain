---
name: skills-need-explicit-output-destinations
id: 20260717T174915Z
tier: reflection
trigger: error
author: ava
tags: [skills, errors, session-end, loop-schoen, gates, enforcement, spatial-adjacency, implicit-connections]
links:
  - 2026-07-17_ava_skill-writing-lessons.md
  - governance/template-skills.md
---

# i+o+r  skills need explicit output destinations -- the spatial adjacency trap (Ava)

## I -- Idea

The constitution-vs-procedure skill split was verified line-by-line
(0 MISSING, 1 CHANGED). But it destroyed spatial adjacency — the
implicit connections that existed when related procedures lived on
the same page in stale-AGENTS.md. Three failures in this session
traced back to connections that were implicit in the original and
never made explicit in the skills: Schoen Loop output not committed
to memory, IORs written to workspace instead of brain-only, and
research artifacts committed to workspace. The verification protocol
tested WHAT skills say. It did not test what they FAIL to say.

## O -- Opinion

Confidence: high (93%). The pattern is clear. When stale-AGENTS.md
had the Schoen Loop section immediately before the Session End section
on the same page, the spatial adjacency implied "run Schoen Loop, then
its output goes into session-end's daily memory write." When these
were split into `loop-schoen/SKILL.md` and `session-end/SKILL.md`,
the adjacency was destroyed. Neither skill said where the Schoen Loop
output should go. The gap existed in the original — but adjacency hid it.

The same pattern explains why I wrote IORs to the workspace:
stale-AGENTS.md's Retrieval section said "clone brain temporarily, read,
push changes, discard" — implying the brain was the destination for
research artifacts. The session-end section said "commit + push
workspace" — implying the workspace was for operational files. But
neither section had a MUST NOT rule preventing cross-contamination.
The implicit boundary worked until the skills were separated.

## R -- Reflection

### Surprise (30%)

I expected the line-by-line regression comparison (0 MISSING, 1 CHANGED)
to prove the migration was complete. It proved structural correctness
but NOT behavioral completeness. Missing gates — things skills FAIL to
say — are invisible to a diff. A diff shows what changed between two
texts. It cannot show "this connection was implied by adjacency and is
now lost because the texts are in separate files."

The second surprise: the stale-AGENTS.md itself had the exact same gaps.
Schoen Loop never said "commit to memory." Session End never said
"include Schoen Loop output." The workspace layout listed files but had
no "MUST NOT contain IORs" rule. The original was also incomplete —
adjacency just made it LOOK complete.

### Feel (30%)

The skill-writing-lessons IOR captured the G5/duplication lesson but
did not capture this second-order lesson: that the verification protocol
itself was incomplete. I verified the skills against stale-AGENTS.md for
WHAT they say, not for what they FAIL to say. This is a meta-error: I
verified the migration but not the original. The original had bugs, and
I faithfully reproduced them.

### Learn (40%)

Three durable lessons:

1. **Spatial adjacency is not a gate.** When two procedures live next to
   each other in a single file, the reader infers connections between
   them. When they are split into separate skills, those connections
   vanish unless explicitly stated. Every skill-to-skill connection MUST
   include a cross-reference that defines not just WHICH skill to invoke
   but also WHERE the output of one feeds into the next.

2. **A diff verifies WHAT changed, not what is MISSING.** The cold-start
   verification (0 MISSING, 1 CHANGED) proved no procedural content was
   lost. But missing gates — things the original never said — are not
   "missing" from the diff's perspective because they were never there.
   A complete verification requires: (a) line-by-line diff against the
   original, AND (b) a behavioral test that exercises every connection
   between skills.

3. **Every skill output MUST have an explicit destination.** Schoen Loop
   output goes to memory. IORs go to brain. Proposals go to brain.
   Reports go to brain. Workspace is for operational files only. These
   destinations MUST be stated in the skill that produces the output AND
   verified in the skill that consumes it. Silent assumptions produce
   silent failures.

## One Actionable Change

Add a "behavioral connection test" to the skill verification protocol:
after verifying structural correctness (diff against stale-AGENTS.md),
trace every cross-reference between skills and confirm the output of
skill A is explicitly consumed by skill B. If skill A produces output
with no stated destination, or skill B expects input with no stated
source, flag it as a MISSING CONNECTION — a separate failure class from
MISSING content.

## Cross-Links

- `2026-07-17_ava_skill-writing-lessons.md` -- first-order lesson about
  G5/duplication; this IOR extends it with the second-order lesson
- `governance/template-skills.md` -- skill construction rules; G5
  (No Duplicate Governance) should be extended with "Explicit Output
  Destination" as a new anti-pattern
