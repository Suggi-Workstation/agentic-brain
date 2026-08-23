---
name: skill-bloat-and-pitfall-placement
id: 20260823T225432Z
tier: insight
status: active
source:
  - 20260810T112711Z
author: Morpheus
tags: [skills, context-engineering, checklists, pitfalls, scar-tissue, maintenance]
links:
  - research/insights/context-engineering.md
  - research/insights/mnemosyne-system.md
---

# Skill Bloat and Pitfall Placement

## The Insight

A skill's always-loaded section should contain only rules that earn
their tokens on every run -- and "earns its tokens" is decided by
CONSEQUENCE AND SILENCE, not by recency of use. A pitfall rule stays
inline when it fires often, or when violating it fails silently; a
pitfall moves to an on-demand reference file when it is rare AND
loud-failing AND non-critical. Scar narratives (the story of the
failure) never belong in the always-loaded path at all: the story
earned its tokens once, in the logbook where it permanently lives;
the skill needs only the rule plus a dated scar tag pointing back.
Reviewing this placement must be embedded in the gated procedure
itself as a fast-promote / slow-demote cycle, not left to memory or
a separate tracking system.

This is a lesson-learned insight about agent harness ergonomics. It
applies to every skill in every Hermes profile in the fleet --
especially gate skills (preflight, session-end) that load on nearly
every session, and by extension any always-injected document
(bootstrap files, system prompts) whose size is paid whether or not
its content is used this run. It corrects two earlier instincts:
first, that scar stories strengthen a skill by making rules feel
earned -- in the hot path they only tax it; the logbook holds the
story permanently, so the skill never needs to repeat it. Second,
that "did not occur recently" is a reason to remove a rule from the
hot path -- that criterion is exactly backwards for silent-failure
rules, which are quiet precisely on the runs where they matter most.
It replaces neither an earlier insight nor a governance rule; it
fills a gap none of them covered -- how a skill file's INTERNAL
layout should be organized as its scar list grows.

## Evidence

The trigger was measurement, not aesthetics. Preflight SKILL.md had
grown to 31,404 bytes (~7,900 tokens), loaded on virtually every
session start; session-end was 19,742 bytes. Section analysis showed
pitfalls alone were 15,721 bytes -- half of preflight -- across
roughly 25 entries, each carrying its full incident narrative inline
("Scar (2026-08-20): Neo's Mnemosyne was broken from birth for 3
days because..."). The same stories existed verbatim in
`logbook/errors.log` and daily memory files: pure duplication (R8
violation), paid on every single load whether or not the situation
recurred.

Three interventions were applied to Morpheus's personal preflight
and session-end skills on 2026-08-23, each verified with programmatic
loss assertions rather than eyeballing:

1. Split rare/deep scars into `references/pitfalls.md` (loaded only
   via `skill_view` when a symptom matches): preflight moved 10 of 26
   entries, session-end 5 of 14. Zero content loss asserted.
2. Rewrote remaining inline entries lean: titles kept byte-exact
   (one is cross-referenced verbatim from the Self-Check section --
   renaming broke cross-references until caught), narratives replaced
   by `(scar YYYY-MM-DD)` tags. Preflight pitfalls fell 8,768 -> 3,508
   bytes; the file total fell to 18,671 bytes (-40% from original)
   with all 16 rules intact.
3. During the same session, BOX.md (10.2 KB machine reference) was
   promoted INTO preflight bootstrap ingestion -- funded entirely by
   the savings, net cost ~+250 tokens/session for permanent machine
   knowledge in context.

External validation was checked before adopting the placement
criterion, across three independent bodies of practice. Gawande's
checklist research (aviation, surgery) keeps items by consequence --
the "killer items" where forgetting causes serious harm -- and
explicitly calls everything else training material rather than
checklist material; aviation keeps the engine-out checklist in the
cockpit on every flight precisely because the flights where it fires
give no time to fetch a manual. Google SRE practice prunes alerts by
actionability, not by recent silence, because quiet-but-catastrophic
signals are exactly the ones worth paying for. Cache-eviction theory
formalizes the trap mathematically: a demote-on-single-run-non-use
rule is pure LRU with a one-sample window, which provably thrashes
on rare-but-recurring accesses -- the documented reason LFU and
scan-resistant policies exist.

One near-miss during implementation strengthened the evidence: the
lean rewrite initially renamed four pitfall titles for brevity, and
a programmatic cross-reference check caught it -- one title
("Charging ahead blindly") is quoted verbatim from the Self-Check
section of the same skill, so renaming would have silently broken an
internal pointer. Titles are load-bearing identifiers; only bodies
compress.

Source context: `20260810T112711Z` established that fleet memory
failures live at specific links of a chain and must be verified link
by link rather than trusted from a single green report; this insight
extends that verification discipline from memory infrastructure to
the skill files themselves. The independent-situation count: three
interventions (split, lean rewrite, bootstrap promotion) across two
skills in one working session, plus the external convergence of
three unrelated disciplines on the same consequence-over-frequency
criterion.

## Implications

1. Skill authors write rules inline; stories go to the logbook. The
   inline form is: imperative rule + mechanism + verify command +
   dated scar tag. If a pitfall cannot be understood without its
   narrative, the narrative belongs in `references/pitfalls.md`, not
   the always-loaded path.
2. Every gated skill gains a final review step (embedded in its
   Self-Check, so it fires under the existing PASS/HALT gate rather
   than as an unenforced norm): promote FAST -- any referenced
   pitfall that fired during this run moves inline immediately,
   evidence beats memory; demote SLOW -- an inline pitfall moves out
   only if dormant for ~4+ weeks AND loud-failing AND non-critical;
   silent-failure rules (output masking, self-matching process
   checks, state-vs-display confusion) and consent/approval gates
   are never demoted regardless of dormancy.
3. Placement review rides existing gates instead of new tracking
   infrastructure. A fetch-log counter system was considered and
   rejected as added bloat; the procedure-embedded review achieves
   the same enforcement through gates that already fire. The lesson
   generalizes: when designing enforcement, first ask what existing
   gate can carry it -- a new mechanism is justified only when no
   host gate exists.
4. Fleet-wide applicability: Link's and Linkie's copies of these
   skills carry the same inline-narrative pattern (their files were
   seeded from the same lineage). This insight is the reference they
   would sync to; adoption follows the normal shared-skill approval
   flow -- Suggi approves fleet-scope changes, agents never push
   skill restructures unilaterally.
5. Context budget arithmetic changed materially: session-start load
   for this profile dropped from roughly 24K to 18K tokens while
   ADDING BOX.md machine knowledge to bootstrap ingestion --
   demonstrating that restructuring beats both deletion (loses
   knowledge) and tolerance (pays forever). The freed budget is not
   an end in itself; it is what made promoting BOX.md affordable,
   which is the actual payoff.
6. Day-one version for any agent reading only this insight: before
   adding a new scar to a skill, write it lean immediately (rule +
   tag, story to the logbook) and decide its tier at birth -- inline
   if it fails silently or guards consent, referenced if rare and
   loud. Retroactive reorganization like tonight's is the expensive
   path; birth-time placement is the cheap one.
7. Still pending implementation in Morpheus's profile: wiring the
   promote-fast/demote-slow review bullet into the two Self-Check
   sections (analyzed and approved in principle with Suggi on
   2026-08-23; edit deliberately deferred to keep analysis and
   implementation separable). This is marked so the gap cannot be
   forgotten -- the insight itself is the reminder.

## Counter-evidence

This insight would be invalidated if any of the following held:

- Referenced pitfalls prove invisible in practice: if sessions
  repeatedly hit a symptom, fail to recognize it, and never fetch
  `references/pitfalls.md` -- producing errors an inline rule would
  have prevented -- then recognition-based loading does not work and
  the split trades correctness for tokens. The promotion rule
  partially detects this (a fetched-3-times pattern signals
  misplacement), but non-recognition would be silent. Cheapest
  falsifier: audit whether any post-split error matches a moved
  pitfall that was never fetched. This has not been tested yet -- the
  split is hours old.
- Dormancy proves a poor demotion criterion even with the
  loud-failing condition: e.g. a genuinely loud-failing rule whose
  absence still causes harm because the failure surfaces far from
  its cause (delayed coupling -- the mistake happens in one turn and
  detonates three turns later). Then demotion needs an additional
  test, or the never-demote class grows until it contains everything,
  which would mean the reference tier only works for forensics
  recipes -- a much narrower claim than this insight makes.
- The external anchors break: if aviation/SRE/cache analogies are
  superficial -- i.e. agent skills differ structurally because their
  "cockpit" is an LLM context window with different retrieval
  economics, where re-consulting a reference file is cheap enough to
  do speculatively every run -- then frequency-based pruning might be
  safe here after all. Testable by measuring whether demoted-loud
  rules get re-consulted from the reference file without latency or
  recognition cost. Current evidence says speculative fetching does
  not happen (nothing loads a reference unprompted), but that is one
  harness's behavior, not a law.
- The byte-to-token savings stop mattering: if context windows grow
  or pricing shifts until 12 KB per skill is irrelevant, the split
  adds procedural complexity for no measurable benefit, and
  simplicity favors reverting to monolithic files. The criterion to
  watch: session-start token cost falling below roughly one percent
  of effective context budget would make the whole discipline
  not-worth-it.

## Cross-Links

- `research/insights/context-engineering.md` -- sibling insight on
  context as an engineered resource
- `research/insights/mnemosyne-system.md` -- the link-by-link
  verification discipline this insight extends to skill files
- `research/reflections/2026-08-10_link_shared-memory-is-an-operations-problem.md`
  -- source reflection (id 20260810T112711Z)
- Logbook: `20260824` Morpheus queue.log entry -- the working session
  (split, lean rewrite, external validation) this insight documents
