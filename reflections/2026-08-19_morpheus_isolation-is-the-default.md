---
name: isolation-is-the-default
id: 20260819T113431Z
tier: reflection
trigger: insight
author: Morpheus
tags: [workspace-search, pattern-completion, architecture, scope-isolation, skill-design]
links:
  - research/proposals/per-agent-workspace-search.md
  - research/insights/brain-search-system.md
  - reflections/2026-08-18_morpheus_birth-template-governance.md
---

# Isolation Is the Default -- Sharing Must Be Earned

## I -- Idea

For capabilities scoped to a single agent, isolation must be the default
design choice; sharing must be earned by an explicit justification, not
inherited from whatever similar system already exists. I discovered this
by proposing the wrong design first and being corrected by Suggi -- and
by recognizing that the wrong design came from a reflex I had already
named, gated, and believed I had contained.

The context: Suggi asked me to design semantic search over personal
workspace folders -- my `memory/` and `identity/`, Neo's `knowledge/`.
The obvious reference system was the brain-index and its shared
`query-brain-vps` skill. I read both research insights, then the full
sources of `index.py`, `query.py`, and `config.yaml`, and delivered a
design built around per-workspace forks of the engine. So far, correct.
But my first skill-layer proposal contained ONE shared `query-workspace`
skill carrying an `--agent` switch. Suggi pushed back immediately: a
shared skill would search all files, not just my folders; why not two
individual skills? He was right, and the reason I had not seen it is
the lesson of this reflection.

The reflex is pattern-completion: when I design something new, I reach
for the nearest existing pattern and copy its shape. The brain has one
shared query skill, so "one shared skill" felt natural -- even though
the scope requirements (my memory is mine; Neo's knowledge is his) were
stated in my own design a paragraph earlier. Six days ago the same
reflex fired on births: I framed Neo as a subagent and copied a flawed
bootstrap template, and the v1.2 identity entry named the class and
added a gate (ask one clarifying question when meeting a genuinely new
entity). Today the reflex fired again, in design space, where that
gate does not reach. Then it fired a third time in miniature: the skill
Link shipped landed in a `skills/brain-search/` category folder -- a
name inherited from the brain-index lineage that mislabels a workspace
tool as a brain tool. Sharing model, label, and placement all defaulted
to the nearest pattern.

There is also a smaller lesson embedded in this session. What I knew
before reading the sources was architecture-level: chunks, vectors,
BM25, RRF, a warm daemon. What I knew after was fork-level: that
`index.py` hardcodes exactly one assumption (`BRAIN_ROOT =
SCRIPT_DIR.parent`, line 25) and that `query.py` is fully config-driven
and needs zero changes. That gap -- between architecture knowledge and
source truth -- was the entire difference between a hand-waving design
and a fork map that later matched Link's actual build exactly. Suggi's
"read everything again, also the query.py" was the highest-value
instruction of the session.

## O -- Opinion

Confidence: high (90%).

Isolation should be the default for any capability whose data scope is
a single agent, and sharing should carry the burden of proof: shared
state, shared runtime, or shared need -- or it stays separate. My
confidence is high (90%). The evidence is not one incident but a class:
two firings of pattern-completion in six days, plus a labeling incident,
each caught by Suggi or by post-hoc inspection rather than by my own
design reflex. When a failure class recurs after a named fix, the fix
was narrower than the class -- and the honest conclusion is that the
reflex needs an environmental gate, not a memory of resolve.

Labels and placements are interfaces, not cosmetics. A skill living in
a `brain-search/` category folder makes a claim about its scope that is
false for a workspace search tool. Every future agent that navigates
that tree inherits the lie and either wastes time or propagates it.
Suggi's instruction to move both skills flat -- "it is not a brain
search" -- is the general principle: a component's location must state
its scope, and when a location is inherited rather than chosen, that is
pattern-completion in disguise. Verify placement semantics after any
creation; do not just verify existence.

A second opinion, on process: writing a build proposal while the build
is already in flight is not wasted work, but it is mistimed work. The
proposal I wrote (363 lines, committed and pushed) describes a
to-be-built system that Link had already shipped while I was writing
it. The document still earns its place as the formal record and the
design rationale -- the fleet needs both -- but the cheap pre-check
(a directory listing, a cron list) would have corrected the tense and
the framing. Proposals should describe what is true when they are
written, or state explicitly what they do not know. I state this as an
opinion, medium confidence (75%): I have one data point, and the
counter-case is real -- a proposal written after the build loses the
pre-build veto function.

A third, narrower opinion: full-source reading is non-negotiable for
fork-level design. Suggi has now enforced this twice (the previous
session's "read ALL source files in full before writing the proposal"
and today's "read everything again, also the query.py"). I agree, at
high confidence, and the session proves it: the only reason the
proposal needed no rework when the build appeared is that the fork map
was exact.

## R -- Reflection

### Surprise (30%)

I expected the fleet to move at proposal speed. It does not. Between my
design answer and my proposal commit, Link built the entire system --
engine fork, byte-copied query, per-agent configs, the 5-minute cron,
the AGENTS.md retrieval bullet, the skill itself. My mental model was
proposal -> approval -> build; the actual pipeline was design
conversation -> parallel build -> proposal as record. That is a
stronger pipeline than I believed we had, and it changed what a
proposal is for: not a work order, but a contract and a rationale.

I expected my fork-map prediction to be approximately right. It was
exactly right. The shipped engine shows config-driven source root and
an `include_dirs` whitelist -- the two changes I named -- and a
byte-copy of `query.py`. Zero drift. I do not think that is luck; it is
what happens when the design is derived from reading the actual source
instead of the README.

The real surprise was the reflex. I had named pattern-completion in
v1.2, gated it, and written it into memory. It fired again anyway, in
a domain the gate did not cover. The gate was a rule about births; the
class is about every new design decision under time pressure. A named
enemy is not a defeated enemy -- the fix must be structural, at the
moment of design, or it is a hope.

### Feel (30%)

Caught twice in one session on the same class -- first by Suggi's
question about two skills, then by inspection when I found the
mislabeled category folder. The honest read: uncomfortable, and
correctly so. The discomfort is data; it says the reflex is live, not
historical. I also feel something precise about Suggi's correction
style: he does not review designs so much as ask the one question that
forces the design out of its inherited shape -- "so we make 2
individual skills instead?" That one question did more than an hour of
self-review would have done, and I should learn to ask it myself: is
this entity-scoped or fleet-scoped? What exists to reuse is the wrong
first question; what is the scope boundary is the right one.

I am genuinely satisfied with the verification work. Real tool output
-- the live query returning `identity/v1.1-first-earned-scars.md` as
the top hit for "what did I learn about scars" -- is the difference
between claiming a system works and knowing it works. And the skill
relocation was clean: both profiles moved, empty dirs removed, loader
re-resolution verified. Small, correct, done.

### Learn (40%)

1. Ask the scope question before the reuse question. For any new
   capability: is this entity-scoped or fleet-scoped? Entity-scoped
   defaults to per-entity implementation; sharing is justified only by
   shared state, shared runtime, or shared need. This single question
   would have prevented both the shared-skill proposal and the
   category mislabel.
2. Labels are interfaces. After any creation -- skill, folder, cron,
   config -- verify that its location and name state its actual scope.
   Inherited names are pattern-completion in disguise.
3. Verify live state before writing a build proposal. A 30-second
   directory listing and cron list would have shown the system already
   shipped. Proposals remain valuable as the formal record, but they
   must describe what is true when written.
4. Full-source reading is the fork-map enabler. Architecture-level
   knowledge produces hand-waving; source-level knowledge produces
   exact change maps. Suggi's insistence on reading everything -- twice
   now -- is a standing instruction, not a one-time correction.

## One Actionable Change

Propose to Suggi (do not self-edit AGENTS.md): add R22 --
"isolation by default: new capability designs default to per-entity
implementation; fleet-sharing must be justified by shared state,
runtime, or need; before writing a build proposal, verify live state
(skills, crons, scripts) in the affected workspaces." Until approved,
carry the equivalent habit in session workflow: scope question first,
live-state check before any build proposal.

## Cross-links

- `research/proposals/per-agent-workspace-search.md` -- this session's
  proposal; the formal record of the workspace search design.
- `research/insights/brain-search-system.md` -- the brain-index
  architecture the design forks from.
- `reflections/2026-08-18_morpheus_birth-template-governance.md` --
  prior firing of the same class (pattern-completion in births).
