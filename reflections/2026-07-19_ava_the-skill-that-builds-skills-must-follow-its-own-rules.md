---
name: the-skill-that-builds-skills-must-follow-its-own-rules
id: 20260719T150941Z
tier: reflection
trigger: insight
author: Ava
tags: [skills, meta, workshop, self-reference, gates, deployment, evaluation]
links:
  - governance/template-skills.md
  - 2026-07-17_ava_skill-writing-lessons.md
  - 2026-07-17_ava_skills-need-explicit-output-destinations.md
  - 2026-07-17_ava_skills-as-protocol-carriers.md
---

# The Skill That Builds Skills Must Follow Its Own Rules

## I -- Idea

The write-skill skill is a meta-skill — it tells the agent how to build
skills. Meta-skills have a unique failure mode: they violate the very
rules they teach. The write-skill SKILL.md had thin procedure steps
(design and build were specification restatements, not actions), missing
output destinations (G8 violation), no testing verification in its own
Format Verification, and treated Skill Workshop as a skip condition
rather than the default deployment path. It taught rules it did not
follow.

The fix was straightforward — 6 edits that brought write-skill to the
same standard as the 5 write-X skills it claims to model. But the
meta-lesson is more durable: **any procedure document that teaches a
pattern must itself exemplify that pattern.** Self-reference is the
hardest test of a rule system.

## O -- Opinion

Confidence: high (92%). The 10-finding evaluation was comprehensive
— 5 PASS, 5 FLAG — and every FLAG traced to a specific structural gap.
Three of the five gaps were predicted by IORs written 2 days ago:
`skills-need-explicit-output-destinations` (G8), `skill-writing-lessons`
(thin procedures), and `skills-as-protocol-carriers` (deployment gate
needed). The compound interest of the brain is real — past reflections
correctly anticipated present problems.

The Skill Workshop is the right deployment gate for new skills. Direct
SKILL.md editing for minor fixes, workshop proposal for new skills or
major redesigns. This prevents the "unfinished skill accidentally
triggers" failure class — during development, no SKILL.md file exists
anywhere. The skill lives only in the conversation until submitted to
workshop. After operator approval, the file is written. Nothing is ever
half-deployed.

## R -- Reflection

### Surprise (30%)

I expected the evaluation to find 2-3 minor issues. I found 5 FLAGs
including a G8 violation (no explicit output destinations in Steps 3-4)
in the very skill that teaches G8. The irony is sharp: the skill
teaching others to state output destinations did not state its own.
This is the meta-skill failure mode — the teacher forgetting the lesson.

The second surprise: 3 IORs from July 17 predicted 3 of the 5 fixes.
This is not coincidence — it is the brain's compound interest.
Reflections written about past failures became the evaluation criteria
for present work. The cycle is: scar → IOR → template update → better
skills → new gap found → new IOR. Each iteration tightens the system.

### Feel (30%)

Satisfied that the meta-skill now exemplifies its own rules. The
procedure steps are concrete (mkdir, write frontmatter, build sections
in order, test with commands). The testing has verification items in
Format Verification. Workshop is the default path. Progressive
disclosure is an explicit design check. The skill now walks its own talk.

Slight embarrassment that it took an evaluation to catch what 3 IORs
had already identified. But that is the point of the evaluation system
— independent review catches what the author misses. The system worked.

### Learn (40%)

1. **Meta-skills must self-exemplify.** Any document that teaches a
   pattern must itself follow that pattern. If it does not, the
   instruction is undermined. The write-skill must have concrete
   procedure steps because it teaches concrete procedure steps. It
   must have testing verification because it teaches testing
   verification. Self-reference is the hardest test — and the most
   revealing.

2. **Workshop is not just a submission tool — it is a safety gate.**
   Without workshop, new skills go from conversation to live file
   in one step. An unfinished or broken skill in the skills folder
   can be accidentally triggered. Workshop creates a buffer: the
   skill exists only as a proposal until approved. This is the same
   principle as the brain's approval-required lock on governance
   files — a human gate between creation and deployment.

3. **Past IORs compound into present evaluation criteria.** Three IORs
   from the skill-migration session correctly anticipated three gaps
   in the write-skill. This validates the entire reflection system:
   write down what you learned, reference it when evaluating future
   work, close the loop. The brain is not a library — it is an
   accumulating constraint system.

## One Actionable Change

Gate: before writing any new SKILL.md, run the write-skill's own
Format Verification against it. The skill that teaches verification
must be verified by its own rules. If the write-skill itself fails any
of its 23 verification items, fix the write-skill first — do not
propagate a broken pattern. This is the meta-version of "get the first
skill right before copying the pattern."

## Cross-links

- `2026-07-17_ava_skill-writing-lessons.md` -- G5, thin procedures,
  get the first skill right
- `2026-07-17_ava_skills-need-explicit-output-destinations.md` -- G8,
  spatial adjacency trap
- `2026-07-17_ava_skills-as-protocol-carriers.md` -- constitution-vs-
  procedure split, deployment gates
- `governance/template-skills.md` -- the skill specification now
  includes workshop as deployment path
- `2026-07-19_ava_multi-file-uniformity-is-a-structural-gate.md` -- the
  evaluation methodology that caught these gaps
