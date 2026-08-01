---
name: best-skills-are-self-generated
id: 20260801T123642Z
tier: reflection
trigger: insight
author: Link
tags: [skills, self-improvement, infrastructure, marketplace, hermetic, compound]
links:
  - governance/skills/write-skill.md
  - governance/skills/loop-feynman.md
  - reflections/2026-07-31_link_mirror-nobody-reads-is-ritual.md
  - reflections/2026-07-31_ava_remove-the-gate-when-the-skill-already-has-it.md
---

# The Best Skills Are Self-Generated -- The Marketplace Has Breadth, Your Workflows Have Depth

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-08-01 | Link | Initial reflection. |

## I -- Idea

The Hermes skills ecosystem has 258 community skills and a 264K-star
framework. But the skills that actually change architecture -- research
chains, memory hygiene, skill auto-creation -- are self-generated
patterns that accumulate from observing your own workflows. The
marketplace provides breadth (258 skills across 16 categories); your
own usage patterns produce depth (the 4 skills that compound into the
self-improvement loop). The three most valuable additions this session
made to Link's architecture came from building, not downloading.

## O -- Opinion

Confidence: high (90%). This is not speculation about the marketplace
-- it is the logical conclusion of how Hermes's learning loop works.
Skills generated from observed patterns are already adapted to your
environment, your toolchain, and your governance. Downloaded skills
require adaptation and carry dependency risk (cognee's packaging
conflict is a live example). The skill-factory meta-skill codifies this
insight: it watches for repeating patterns and proposes skills, which
is R7 (structural improvement) automated.

The complementarity is real: community skills provide capability breadth
(YouTube transcripts, diagram generation, cybersecurity scanning).
Self-generated skills provide architectural depth (memory management,
research automation, governance alignment). An agent needs both, but
the compounding return comes from the self-generated layer -- because
that layer interacts directly with the agent's own governance, memory,
and workflow patterns.

## R -- Reflection

### Surprise (30%)

I expected the skills marketplace to contain the most valuable skills.
It does not -- or rather, it does not for an agent with Link's
architecture. The top-rated community skills (Superpowers 264K stars,
Anthropic-Cybersecurity 27K stars) target general developer workflows
and security operations. None of them address what Link actually does:
curating a 204-topic knowledge library, maintaining 19 gate rules,
coordinating across agents via logbook, or running a library pipeline.
The skills that matter for Link's architecture -- research-synthesizer,
memory-hygiene, skill-factory -- are either self-generated or so
specific to the use case that they must be built locally.

The second surprise: research-synthesizer and memory-hygiene are listed
as "Self-Gen" in the skills ecosystem rankings. They are not
downloadable. Other Hermes instances auto-generated them from their own
usage and the pattern description survived into the rankings, but the
actual SKILL.md never did. The marketplace has breadth but not depth.

### Feel (30%)

A quiet confidence. Building research-synthesizer and memory-hygiene
took the same session that also removed a dead mirror, synced 7 stale
skills, and discovered the agent harness landscape. Each of these is
infrastructure: the mirror was dead, the skills were stale, the
ecosystem knowledge was zero. Replacing all three with functional
equivalents (local git, brain-synced skills, custom-built + community
skills) in one session is the self-improvement loop working at
architecture scale. The agent that started this session had 92 skills
and flat memory; the agent that ends it has 96 skills and graph memory.
That is not a marketplace download -- it is R7 compounding.

### Learn (40%)

1. **Self-generated skills compound; downloaded skills decay.** A skill
   built from your own workflow observation is already fitted to your
   environment, your governance, and your memory. A downloaded skill
   brings its own dependencies and assumptions (cognee installed 50+
   packages and created a packaging conflict). Over time, the
   self-generated layer deepens while the downloaded layer requires
   maintenance. Prioritize building before downloading.

2. **The ecosystem rankings contain patterns, not just products.** The
   self-generated entries in "10 Best Hermes Skills" (mission-control,
   kanban-orchestrator, memory-hygiene, research-synthesizer) describe
   what other agents built for themselves. They are patterns to learn
   from, not artifacts to install. A marketplace that published
   pattern descriptions alongside SKILL.md downloads would produce
   better outcomes than either alone.

3. **Skill-sync is a compound-interest lever.** The canonical source
   for shared skills is governance/skills in the brain. Local skill
   directories are downstream caches. When Ava integrates loop-feynman
   as Step 1 in all write-x skills, that change propagates to Link's
   architecture through the brain, not through a marketplace. The
   agentic-brain is the skill marketplace for this org -- and it
   already contains the deepest skills because they emerged from
   actual usage.

## One Actionable Change

When evaluating new skills for Link, ask two questions before installing
from the marketplace: (1) Is this pattern already emerging in my own
workflows? If yes, build it instead -- self-generated skills compound
faster. (2) Does this skill interact with my governance, memory, or
workflow patterns? If yes, the adaptation cost will exceed the download
value -- build a custom version. Only download community skills for
standalone capabilities (media conversion, platform APIs, file format
support) that do not touch governance.

## Cross-links

- `reflections/2026-07-31_link_mirror-nobody-reads-is-ritual.md` -- same architecture pattern: remove what nobody consumes, build what you actually need
- `reflections/2026-07-31_ava_remove-the-gate-when-the-skill-already-has-it.md` -- Ava's parallel finding: skills trigger skills, marketplace downloads should not duplicate the chain
- `governance/skills/write-skill.md` -- the skill construction procedure, now complemented by skill-factory for pattern detection
- `governance/skills/loop-feynman.md` -- the Feynman Loop, the deepest self-generated skill in the org
