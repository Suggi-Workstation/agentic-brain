---
name: pitfall-placement-twin-review
id: 20260823T231718Z
tier: proposal
status: open
author: Morpheus
tags: [skills, pitfalls, gates, context-engineering, maintenance]
links:
  - research/insights/skill-bloat-and-pitfall-placement.md
  - governance/template-proposals.md
---

# Pitfall Placement Twin Review (preflight <-> session-end)

## Problem

Morpheus's two gate skills now use a two-tier pitfall layout: rules
that fire often or fail silently stay inline in SKILL.md; rare,
loud-failing, deep-recovery scars live in `references/pitfalls.md`
and load only on symptom match. The restructure (2026-08-23) cut
preflight from 31,404 to 18,671 bytes with zero rule loss and is
documented in `research/insights/skill-bloat-and-pitfall-placement.md`.
But the placement itself currently has no enforcement loop: the
promotion rule written into both files ("fetched 3 runs in a row ->
promote back inline or root-cause-fix") is a norm wearing a gate's
clothes -- nothing counts fetches across sessions, each session
starts with fresh context, so the trigger cannot actually fire. This
is precisely the R6 failure class ("a gate that fires by itself beats
a rule that must be remembered"): unenforced, the reference tier will
silently drift, with mispromoted content paid every run and misplaced
inline content invisible until it bites.

The obvious fix -- make session-end audit all pitfalls of all skills
used in the session -- fails on two grounds. First, memory: after
context compaction in a long session, neither the agent nor any
checklist can reliably reconstruct which skills ran or what their
internals contain, violating the fleet's own principle that gates
verify from disk evidence, not recall. Second, evidence quality:
demotion requires longitudinal data (weeks of non-occurrence plus a
loud-failure property plus non-criticality); a single run provides
none of it. Any workable mechanism must be scoped to what each gate
can actually see, when it can see it.

## Proposed Solution

A twin-review division of labor across the existing pair, embedded
entirely in gates that already fire -- no new files, counters, or
infrastructure. Design iterations already worked through with Suggi
in working session 2026-08-23: (v1) a fetch-log counter file --
rejected as added bloat; (v2) Suggi's final-procedure-step design
with symmetric parts A/B -- part A survives verbatim as
promote-on-evidence, part B was corrected because demote-on-single-
run-non-use is pure LRU thrashing against silent-failure rules;
(v3, this proposal) asymmetric split: each half lives where its
evidence naturally exists.

Edit set A -- `profiles/morpheus/skills/github/preflight/SKILL.md`
(personal skill, no approval needed beyond this proposal):

1. New step "8. Pitfall Promotion Check" before Emit Read-Proof:
   if this run fetched `references/pitfalls.md` or hit a problem a
   referenced pitfall describes, move that entry verbatim into
   `## Pitfalls` (title byte-exact -- titles are cross-referenced
   identifiers), delete it from the reference file, note the move in
   the read-proof. Nothing fired = do nothing. Demotion explicitly
   forbidden here: single-run absence is not evidence.
2. Matching Self-Check line (R14): "[ ] Pitfall placement reviewed:
   anything eligible promoted in step 8; zero demotions performed
   (PASS / HALT)".
3. Reconcile the PROMOTION RULE pointer text in `## Pitfalls`
   (currently says fetched-3-runs; would conflict): gated-run
   evidence promotes immediately; 3 consecutive out-of-gate fetches
   promote or root-cause-fix.
4. Renumber Emit Read-Proof to step 9 and sweep stale "step 8"
   cross-references (R9).

Edit set B -- `.../session-end/SKILL.md`, one clause:

Extend the existing Gate-Rules self-check item (R15 stale-rule
audit) from "rules audited for staleness" to "rules AND inline
pitfalls audited for staleness". Scope strictly limited to the two
owned skills (session-end + preflight) -- never all skills used in
the session. Dormancy judged from disk, not memory: search the
trailing ~4 weeks of `memory/*.md` and `logbook/errors.log` for the
pitfall's symptom class; zero hits AND loud-failing AND non-critical
=> flag as demotion candidate. The flag produces a reviewed edit (a
visible diff), never an automatic mid-gate shuffle. Silent-failure
rules and consent/approval gates are permanently exempt regardless
of dormancy.

Generalization rule to add to the insight afterward: any skill
adopting the reference tier must declare where its promotion and
demotion live -- own gate where one exists, Suggi's monthly manual
review pass where none does. There is no central pitfall auditor by
design.

## Impact

Benefit: closes the last unenforced norm left by the 2026-08-23
restructure. Today the placement rule is aspiration; after these
edits, misplacement self-corrects within one gated cycle (promotion
fires on in-run evidence) or surfaces as a reviewed diff at session
end (demotion flags through R15's existing audit). This also closes
a honesty gap between documents and reality: the linked insight
currently describes promote-fast/demote-slow as if it existed;
implementing this proposal makes the artifact true. Who acts
differently: Morpheus, at every gated run -- preflight gains a
concrete step-8 decision instead of an ambient intention, and
session-end's staleness audit gains a greppable evidence procedure
instead of relying on recall. Suggi experiences no new burden;
demotions arrive as visible diffs inside work he already reviews,
and the monthly manual pass is untouched. The pair also becomes a
copyable template for any future skill adopting the reference tier.

Risk assessment: main risk is churn -- rules oscillating between
tiers on noisy evidence, which would make both files unstable and
the history hard to follow. Mitigated three ways: promotion requires
positive in-run evidence (not vibes), demotion requires the
triple-lock plus a greppable dormancy window, and demotion is
flagged-then-reviewed rather than automatic. Second risk: scope
creep into auditing every skill touched during a session --
explicitly designed out; the audit surface is fixed at two owned
files regardless of session length or compaction. Residual risk: a
referenced pitfall whose symptom recurs but is never recognized is
neither fetched nor promoted -- undetectable by this mechanism;
accepted consciously and documented as the primary falsifier in the
linked insight. Second residual: the R15 extension adds one judgment
call (interpreting symptom-class grep hits) to an existing audit;
bounded by the two-file scope.

Cost estimate: implementation under one hour -- five small edits, a
renumber sweep with stale-reference grep, one dry-run of preflight.
Ongoing cost ~70 tokens per gated run (both skills combined) and
roughly five minutes per month of dormancy greps -- negligible
against the ~3,300 tokens/run the restructure already banked, so the
pair remains net-negative context cost even in the worst month.

## Open Questions

1. Is the 4-week dormancy window right? Too short risks evicting a
   genuinely rare-but-live rule; too long leaves bloat in place and
   weakens the whole argument for the reference tier. Alternative
   anchors: a calendar quarter, or "N gated runs" instead of
   wall-clock weeks (runs are more honest -- preflight does not fire
   every day). Default proposed: 4 weeks, revisited at first
   quarterly review once real demotion data exists.
2. Should the read-proof line gain a fixed placement field (e.g.
   `placement: clean` / `placement: +1 inline`)? That would make
   promotion history greppable without any new file and give the
   dormancy greps a cleaner signal. Cost: adds format surface to
   every future read-proof and one more thing to keep consistent.
   Default proposed: no for now -- note moves in prose only until
   move volume justifies a field.
3. Fleet adoption path: Link's and Linkie's seeded skill copies
   carry the same drift exposure and the same unenforced promotion
   text. Adopt via normal shared-skill sync after this pair proves
   itself here, or leave their copies untouched until they ask?
   Default proposed: prove locally for one clean month, then propose
   fleet sync with the evidence attached -- never push skill
   restructures unilaterally across machines.
4. Should other personal skills that grow past ~20 KB adopt the same
   tier + twin pattern automatically? A hard size trigger is simple
   but mechanical; case-by-case keeps judgment in the loop but
   relies on noticing. Default proposed: case by case, relying on
   the insight's birth-time-placement rule to make new scars cheap
   from day one so large-scale reorganizations stay rare.
5. Should session-end's demotion flag require your explicit nod per
   move, or is surfacing it inside an already-reviewed diff enough?
   Stricter costs you attention on what should be routine; looser
   trusts the triple-lock. Default proposed: diff-surfaced, no extra
   nod -- reversible either way since git history tracks both tiers.

## Approval Gate

If approved, I will execute in this order: (1) apply edit set A to
preflight -- new step 8 (Pitfall Promotion Check), matching
Self-Check line, PROMOTION RULE pointer reconciliation, and the
step-9 renumber with a stale-reference sweep; (2) apply edit set B
to session-end -- the single R15 clause extension adding inline
pitfalls to the staleness audit, scoped to the two owned skills,
with the disk-evidence dormancy check (trailing ~4 weeks of
`memory/*.md` + `errors.log`, symptom-class grep) and the permanent
exemptions for silent-failure and consent rules written into the
clause itself so future sessions cannot reinterpret it looser;
(3) verify: ASCII scan on both files, a full dry-run of preflight
against the new shape proving the step order still flows, and grep
confirmation that no stale "fetched 3 runs" or old step-number
references survive; (4) append the generalization rule to the linked
insight ("any skill adopting the reference tier must declare where
promotion and demotion live") and mark this proposal `implemented`
in the same commit, citing both skill paths as the landed evidence;
(5) record the outcome in the logbook queue per protocol.

Skills live outside any git repository, so there are no commits for
the edits themselves -- verification is grep output plus the dry-run,
and the brain-side insight/proposal updates are the tracked artifacts.
No workspace files change. If you want tuning instead of a clean yes
-- different dormancy window, stricter demotion approval, or
promoting only edit set A first -- the two edit sets are independent:
A lands promotion enforcement alone and is safe without B; B can
follow later once you have watched a month of promotion behavior.
Silence beyond your normal review rhythm I will treat as no
objection to the defaults stated in Open Questions, but no edit
happens until you say go.
