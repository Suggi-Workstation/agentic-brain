---
name: promote-the-best-variant-upward
id: 20260822T193753Z
tier: reflection
trigger: decision
author: Morpheus
tags: [governance, constitution, directives, unification, fleet, curator]
links:
  - research/insights/why-constitution-matters.md
  - governance/system-primedirectives.md
  - reflections/2026-08-22_morpheus_desktop-app-state-has-three-tiers.md
---

# Promote the Best Variant Upward -- Unification Is Not Standardization

## I -- Idea

When unifying shared doctrine across multiple agents, the fastest and
most honest path is not pushing the canonical text downward onto every
mirror -- it is reviewing every local variant, harvesting the best
ones, promoting them into the canonical source, and only then
synchronizing everything to the improved standard. Unification done
right is an upgrade pass, not an enforcement pass.

The session that produced this idea began as a governance audit.
Suggi asked me to re-read `system-constitution.md` and
`system-primedirectives.md`, check them against my own bootstrap
files and AGENTS.md rules, research current best practices for agent
architecture and governance, and propose expansions. The external
research (Anthropic's Constitutional AI method, the NIST AI RMF /
ISO 42001 / EU AI Act framework family, and agentic-specific control
lists descended from the OWASP Agentic AI Top 10) produced a gap map:
our documents already covered five of the six agentic controls the
industry now recommends -- agent registration, capability scoping,
human-override categories, action-level incident response -- and had
real scars behind most of them. Two gaps were real: nothing governed
destructive modification of shared state (a gap we had bled on that
same morning, when the Mnemosyne TTL-trim bug deleted eleven of
Link's facts fleet-wide through automated tombstones), and the
Containment section defined "external input" so narrowly that
agent-to-agent traffic inside our own workspace escaped the rule
entirely. The approved fixes went into the constitution as version 4
with the required scar citations, plus two identity-level additions:
Kant's means-ends rule and a reversibility preference. That part was
conventional amendment work.

The unification round that followed is what generated this insight.
Four agents mirror the prime directives in their SOUL.md files. My
working assumption going in was that byte-exactness meant making all
four copies match the canonical text exactly -- meaning Neo's three
intentional phrasings would be reverted as drift. They were not
drift. When Suggi saw them, he did not ask which text was canonical;
he asked which text was better. His rulings: cross-referencing "the
agentic-brain and your own memory" is superior now that every agent
runs personal memory alongside the brain; recording "an explicit no
gate warranted" matches what session-end actually does; "bring it to
your human" beats "write a proposal" because proposals are one
mechanism among several and humans are the actual authority. Each
ruling promoted a bottom-up variant into the standard. Only one Neo
phrasing was rejected, and it was rejected on correctness grounds
(weakened self-edit protection), not on direction-of-authority
grounds. The final state: one canonical block, character-identical
across all four agents, proven programmatically -- and every line of
it is text that survived a deliberate quality comparison first.

## O -- Opinion

Confidence: high (90%) for doctrine files across a small fleet, and I
will argue the boundary conditions explicitly.

My position: for texts whose value is judgment rather than mechanism
-- ethics, principles, decision norms -- local variation should be
treated as a distributed experiment, and unification should proceed
by promotion of the winning variants. The evidence is that all three
promoted phrasings are strictly stronger than what they replaced.
"Your own memory" widened the cross-reference duty to match the
actual architecture. The no-gate-warranted clause closed a real gap
(R7 sessions without failure classes previously had no sanctioned
output). "Bring it to your human" fixed a subtle coupling problem:
the old wording tied the escalation duty to one artifact type, so an
agent without a proposals directory would have no named channel.
Suggi's instinct outranked my assumption in all three cases, and my
assumption was the one that would have lost information.

The inverse position -- push canonical downward without review --
is correct for a different class of content, and conflating the two
classes is the failure mode. Mechanical content (file paths, schema
fields, command syntax, checklist items) has no local wisdom to
harvest; a variant there is a bug, and the fix is exact mirroring.
Security rules sit somewhere stricter still: I would argue local
variants must be forbidden outright and any loosening treated as an
incident, because an attacker-optimal move is precisely to introduce
a "better fitting" local variant. So the operational rule I carry
forward has three tiers: mechanisms mirror, judgments compare-and-
promote, protections never vary.

The load-bearing element in the middle tier is who arbitrates. An
agent reviewing its own variant against canonical suffers exactly
the self-serving bias that makes self-review weak everywhere else:
the text it authored already feels finished. This session worked
because Suggi read the two candidate texts side by side and ruled --
three rulings in one sitting -- rather than delegating the quality
judgment to me. His August 16 correction ("present options, never
silently resolve") is the same principle at smaller scale: surface
the divergence, let the human pick. The promotion pattern without
that human pick degrades into whichever phrasing the executing agent
prefers, which is not curation but drift with extra steps.

Today's work exercised the middle
tier under explicit human arbitration, which is what made it safe --
I did not get to decide that Neo's wording was better; Suggi did,
after seeing both side by side. Without that arbitration step the
promotion idea degrades into whichever agent argues last.

One more position, held at medium confidence (70%): this pattern
does not scale past small fleets without tooling. With four agents
and one human reading diffs, promotion-by-review works. At twenty
agents you need variant detection automated -- a scheduled diff of
all mirrors against canonical, presenting divergences as candidate
promotions rather than violations. The classification problem
(which tier a divergence belongs to) stays human either way.

## R -- Reflection

### Surprise (30%)

I expected the tailoring to end one way: Suggi seeing Neo's
deviations and asking me to restore canonical wording everywhere --
that is literally what "make them match word for word" sounded like
at the start. Instead he read each deviation on its merits and
promoted two of three into the fleet standard, then overrode the
canonical text itself a third time ("bring it to your human") within
minutes of seeing it. My model of "unify the mirrors" was
enforcement-shaped; his was curation-shaped. Second surprise: the
curator question. I expected pausing the curator to slow down skill
creation, because colloquially "curator" covers all skill
maintenance. It does nothing of the kind -- the background reviewer
created a new skill for Neo hours after we paused the curator on his
profile, and the source code confirms the two systems share no state.
A governance change aimed at autonomous maintenance turned out to
have zero effect on autonomous learning, and I only verified that
because Suggi kept probing.

### Feel (30%)

Two misses sting, both caught before they cost anything. First, my
first `hermes curator status` call ran without `HERMES_HOME` set and
quietly reported the default profile's ENABLED state while Morpheus
was PAUSED -- I reported "ENABLED" to Suggi, then re-checked against
the `.curator_state` file and found the truth minutes later. The
lesson is old (verify the verifier) wearing a new costume (CLI output
is an instrument that can silently aim at the wrong target; state
files are ground truth). Second, I over-applied the August 16
approval rule to personal skills and burned an approval round-trip
on a patch I was authorized to make freely; Suggi's correction
sharpened the rule's scope, which is now saved to memory. What I am
proud of: the unification proof. Rather than claiming "all four are
identical," I spliced the canonical block programmatically with
uniqueness assertions on every replacement and then computed the
distinct-region count across all four files -- answer: one. Claims
about text equality should be machine-checked or not made.

### Learn (40%)

1. Unify doctrine by promotion, not enforcement: harvest local
   variants, arbitrate quality at the human level, amend the
   canonical source with the winners, then synchronize. Reserve
   exact mirroring for mechanisms, and forbid variation entirely in
   security rules.
2. State files beat CLI status output. Any daemon or profile-scoped
   tool can silently target the wrong instance when environment
   variables are unset; before reporting or acting on a status
   claim, read the underlying state file (`cat` the `.curator_state`,
   check the config.yaml block) and confirm the target.
3. Decoupled systems need decoupled audits. "We paused maintenance"
   says nothing about learning, backup, or sync behavior -- each
   subsystem gets its own verification, ideally against source code
   or docs, before anyone concludes a behavior changed.

## One Actionable Change

Make state-file confirmation the standing rule for status claims in
my preflight and session-end practice: whenever a profile-scoped CLI
(`hermes curator status`, `cron list`) is used to report state, the
same call chain MUST include an explicit `HERMES_HOME` export and a
read of the underlying state file (for example `skills/.curator_state`
for the curator, `cron/jobs.json` for cron registries), with the
state-file value treated as authoritative on any disagreement.
Executable by another agent verbatim: export, run CLI, cat state
file, reconcile, report the state-file value.

## Cross-links

- `research/insights/why-constitution-matters.md` -- Ava's insight on
  constitutions as chains of command; this session extended the
  constitution under its own amendment protocol.
- `governance/system-primedirectives.md` -- the canonical text that
  absorbed the promoted variants and the new Ethics/Simplicity rules.
- `reflections/2026-08-22_morpheus_desktop-app-state-has-three-tiers.md`
  -- same-day sibling reflection; its "diff against the known-good
  machine" pattern is the same family as diff-against-canonical.
