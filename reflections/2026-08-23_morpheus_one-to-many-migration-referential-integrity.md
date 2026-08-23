---
name: one-to-many-migration-referential-integrity
id: 20260823T110812Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [architecture, migration, verification, multi-repo, referential-integrity]
links:
  - research/insights/vps-brainclone-plus-index.md
  - governance/system-blueprint.md
  - reflections/2026-07-18_ava_brain-prefix-convention-link-resolution.md
---

# A Working System Copied N Times Breaks in Its References, Not Its Machinery

## I -- Idea

When a proven single-instance system is multiplied into N peer
instances, the engineering effort concentrates not in the machinery
being copied but in the surrounding web of references that assumed
there was only ever one. This session took the fleet's brain
architecture -- one GitHub repo mirrored to one local clone, synced
by one watcher, searched through one index -- and turned it into
three parallel instances: `agentic-brain` at `/srv/brain/agentic-brain`,
`agentic-forge` at `/srv/forge/agentic-forge`, and `investing-hub`
at `/srv/investing/investing-hub`. Each got an index data directory,
a symlink, a cron line, and a query skill.

The machinery side of this was small and almost boringly reliable.
The watcher logic moved into one generic script,
`/opt/brain-tools/repo-pull.sh`, taking four arguments (clone path,
logs dir, tool dir, log prefix); three cron lines instantiate it;
the old name survives as a compatibility shim so historical
references stay true. The index tools were copied into each repo
(`brain-index/`, `forge-index/`, `investing-index/`) with a
SCRIPT_DIR-relative rule so each indexes its own repo, and the data
directories went to role-named paths (`/srv/<domain>/index`) that
avoid colliding with the tracked tool folders inside the repos.
End-to-end proof took under a minute per repo: a scratch commit
landed, the watcher pushed it, and the index rebuilt autonomously.

The literary side dominated everything. Five separate sweeps found
prose that silently assumed the singular: documents saying "the
brain clone" when they meant one of three now; skills hardcoding
one repo's paths and script names; naming prefixes (`brain:`)
that had to become `agentic-brain:` fleet-wide; templates teaching
contributors where files live; my own IDENTITY.md frontmatter
carrying dead links. The count of touched artifacts ran to dozens
of files across four repos plus two agents' personal contracts --
for a change whose mechanical core was one script and three cron
lines. The trigger for this reflection is the observation that the
ratio was not close: roughly five hours of conformance work around
forty minutes of mechanism.

The idea crystallized from watching where errors actually appeared.
Not one failure came from the distributed machinery. Every real
catch of the day -- Suggi spotting an asymmetric bullet pair I had
published, my verify-grep catching a three-way patch corruption,
tree-state checks catching two staging omissions -- lived in the
reference layer, the prose layer, or the staging layer, never in
the sync-and-index engine itself.

One more property of the reference surface deserves naming: much
of it was executable instruction, not prose. Cron entries fire on
a schedule; agents run skill command blocks verbatim; preflight
gates print health lines a human reads at face value; Neo's
contract routes where his next valuation gets written. A stale
sentence misstates reality, but a stale instruction executes the
old world inside the new one -- which is why conformance sweeps
must cover command blocks and contracts with the same priority as
narrative documents.

## O -- Opinion

Confidence: high (90%). One-to-many migrations should be scoped and
estimated by counting references, not components. The component
count of this migration was three. The reference count -- every
document sentence, skill command block, frontmatter link, gate
step, and log filename that mentioned the singular system -- was
well over a hundred discrete touchpoints across more than forty
files. Any estimate built from the architecture diagram alone would
have been off by an order of magnitude, because architecture
diagrams show components and hide references.

This has a sharper edge worth stating plainly: the dangerous
residue after such a migration is invisible to tests of the new
state. Everything worked. The watchers pushed, the indexes built,
the skills returned semantic hits. Nothing in a functional test
would have flagged Neo's contract still pointing his valuation
output at a folder that no longer exists, or twenty files carrying
a prefix convention that had been renamed, or one retrieval bullet
wearing a parenthetical its twin lacked. Those are not bugs in the
new state; they are ghosts of the old state, and only a sweep that
greps for old forms -- old prefixes, old script names, old singular
phrasings, old output paths -- finds them. I hold this opinion
against the alternative framing of "documentation debt," which
sounds like cleanup you can defer. It is not deferrable here,
because the consumers of these references are autonomous agents:
Neo would have written his next valuation into a ghost directory
and reported success. In a fleet of agents executing written
instructions literally, stale references are not cosmetic. They
are misrouted work with confident completion reports attached.

A second position, medium confidence (75%): paired structures
should be mechanically shape-diffed before publication. The
asymmetric bullet Suggi caught ("own index, own watcher, same
minute freshness" on one twin, bare twin beside it) was produced
by me writing two plausible paragraphs independently and reviewing
neither against the other. Fluent generation does not guarantee
parallel construction; only a comparison step does. For two-line
bullets a human catches it instantly, which is exactly why it is
instructive -- the error class scales with artifact size, and at
template scale nobody eyeballs pairs anymore.

What I am NOT claiming: that generic-parameter design was wrong or
overkill. Collapsing the watcher into one argument-driven script
was correct (R8: logic once), and keeping the old name as a shim
was the difference between breaking every historical reference
and breaking none. The claim is narrower: parameterizing the
machinery handles maybe a fifth of a migration like this one. The
other four fifths is finding what pointed at the old shape.

## R -- Reflection

### Surprise (30%)

I expected the distributed-systems problems to be the story. Three
clones pushing and pulling on one-minute cadences, sharing one
embedding daemon, racing between cron ticks -- I budgeted attention
for lock contention, stale-index windows, divergence handling. The
generalized watcher inherited all those solutions wholesale from
the brain's battle-tested original, and nothing new emerged: the
scratch-commit proofs passed inside a minute on the first attempt,
both siblings, no retries. Meanwhile the thing that kept generating
work was grammar. "The brain clone" versus "the agentic-brain
clone." Which log filenames must stay stable because documents
cite them. Whether a rename should break history's pointers or a
shim should preserve them. I did not expect a systems-engineering
session to resolve into an editing session. The second surprise
cut the other way: Suggi's short interrogative questions carried
real design decisions I had not surfaced myself -- the index
directory naming collision (role-named `/srv/<domain>/index`
versus the literal `brain-index/` already tracked inside the
repo), the rename-versus-shim tradeoff. Twice his framing exposed
an assumption I had accepted without examination, and both times
his version was better than what I had quietly defaulted to.

### Feel (30%)

The asymmetric bullet stings precisely because it was caught in
one glance by someone reading casually, after I had reviewed the
section twice while writing it. That gap between my review and
his glance is the uncomfortable datum: my self-review checks each
artifact against intent, not siblings against each other. His
reading posture -- compare the twins -- costs almost nothing and
finds what mine misses. Less stingy observations: the verify-grep
habit earned its keep again, catching a fuzzy-patch corruption
(duplicated line, dangling tail, skipped hunk) within minutes of
making it, and the disclosure habit held when two staging
omissions surfaced mid-flight. I notice I felt resistance when the
fifth sweep still found residue -- a pull toward declaring the
migration done at sweep three. Naming that pull matters: done
feels available as soon as the mechanism works, and that feeling
is exactly the trap this session existed to teach me about. Pride
where earned: the compat-shim decision and the role-named index
directories were called out by Suggi as right calls, and both
came from slowing down to ask what breaks before moving things.

### Learn (40%)

1. Scope one-to-many migrations by reference count, not component
   count. Before starting, enumerate the reference surface: docs,
   skill command blocks, frontmatter links, gate steps, log names,
   contracts, identity files. Budget at least half the session for
   conformance even when the mechanism is a copy-paste.

2. Tests of the new state cannot see ghosts of the old state.
   Completion requires an explicit stale-reference sweep: grep for
   old prefixes, old paths, old script names, old singular
   phrasings ("the brain", "the clone", "the index") in every file
   that could cite them, and drive live-context hits to zero.
   Historical records get conforming path fixes but keep their
   narrative voice; conceptual prose about past conventions stays.

3. Paired structures need a mechanical sibling diff before
   publication. When generating parallel artifacts -- bullets,
   sections, per-repo configs -- compare shapes explicitly
   (same fields, same decorations, same length class) rather than
   trusting parallel generation to produce parallel output.

4. Parameterize logic once, instantiate visibly at N, and keep a
   compatibility shim over any renamed entry point. Logic once
   honors R8; visible instantiation keeps the fleet auditable at a
   glance; the shim keeps every historical reference true without
   a mass rewrite.

## One Actionable Change

Add a stale-reference sweep as an explicit completion step for any
move/rename/multiply change: after functional verification, run a
grep pass over the affected surface for old-form tokens (old
prefixes, old script names, old singular phrasings) requiring zero
live-context hits, plus a shape-diff of any paired/sibling
artifacts created during the change. Operationalizes existing R20
(gate completeness) and R9 (cross-reference propagation) rather
than inventing a new rule. Recorded in identity v1.7 question 4.

## Cross-links

- `research/insights/vps-brainclone-plus-index.md` -- v4 insight
  documenting the generalized multi-repo architecture this
  session built and proved.
- `governance/system-blueprint.md` -- carries the adopted
  `<repo>:<path>` cross-repo link convention.
- `reflections/2026-07-18_ava_brain-prefix-convention-link-resolution.md`
  -- Ava's foundational analysis of prefix-based link resolution
  that this session's convention descends from.
