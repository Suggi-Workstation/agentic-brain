---
name: map-completion-and-the-inbox-discipline
id: 20260822T200524Z
tier: reflection
trigger: milestone
author: Neo
tags: [value-investing, knowledge-base, process-design, screening, dry-run]
links:
  - library/value-investing/circle-of-competence.md
  - investing/frameworks/screening-template.md
  - library/valuation-screening/cost-of-capital-capm-wacc-erp.md
  - reflections/2026-08-22_neo_knowledge-base-before-application.md
---

# A Complete Map Is Not Yet a Journey -- and an Archive Is Not an Inbox

## I -- Idea

This session completed the knowledge-base buildout: five more
research cycles (when-to-sell, sector-specific valuation, circle of
competence, discount rates, stock screening) brought the workspace
knowledge folder to eleven files covering the full analytical
pipeline from candidate discovery through exit logic. Alongside the
content, the session's more durable work was structural: Suggi and I
redesigned LEARNINGS.md from an append-only archive into an inbox --
entries live only while unpromoted, are removed when their knowledge
file verifiably covers them, and the learnings-capture skill now
enforces search-before-create, skip-if-covered, and promotion removal.
The claim this reflection argues: both changes are the same insight
wearing different clothes -- accumulation without a lifecycle is how
systems rot, whether the system is a knowledge folder or a research
process.

The context: this was a marathon session spanning eleven deep-research
cycles in one day (the first six before the morning reflection, five
after). Each cycle followed the pattern the curator skill codified:
coverage-check-first, bounded direct research, synthesis to word-floor
compliance, learning-capture. The corrections that shaped it were
Suggi's: the exit-logic dry-run task he struck ("it can't be tested by
us" -- a boundary correction as important as any content), his
insistence on the inbox redesign after questioning why entries should
persist once promoted, and his catch that file headers should not
repeat their own paths. Each correction closed a loop the previous
structure left open.

What the blank page reveals looking back: before this session,
LEARNINGS.md could only grow; now it cannot grow past outstanding
unpromoted learnings. Before this session, my knowledge folder had no
rule for what a header should be; now the guide specifies it. Before
this session, the pipeline had no gate at its entrance; now the
five-question competence test runs before any valuation work. The
session's product was less eleven files than three structural
improvements wrapped around them.

The eleven files themselves deserve a one-line inventory, because a
future reader of this reflection should know what "complete" means
concretely: free-financial-data-sources (infrastructure),
simple-dcf-buffett-school (valuation method), company-moats
(competitive analysis), management-evaluation (governance and
alignment), financial-health (earnings quality and solvency),
margin-of-safety (the purchase discipline), when-to-sell (exit
logic), sector-specific-valuation (per-sector yardsticks and model
variants), circle-of-competence (the entry gate), discount-rates
(the denominator problem), and stock-screening (discovery). Read in
that order they trace the pipeline end to end: find candidates,
check you understand them, classify their sector, score the moat,
score the management, verify the numbers, value the business, demand
the margin, and know when to leave.

One more session fact belongs in the record because it validates the
process machinery under load: this was the longest single-session
run since the workspace was built, and the mechanical gates caught
under-length sections in four separate cycles -- sector valuation's
conclusion, discount rates' introduction, stock screening's
introduction and conclusion -- each BEFORE a bad commit landed. The
verify-before-commit discipline installed after earlier failures did
exactly what it was designed to do under exactly the conditions it
was designed for: fatigue at the end of long output sequences.
That is not a small thing; it is the difference between a rule that
works and a rule that works only when unneeded.

## O -- Opinion

Confidence: high (88%). The buildout is genuinely complete as a MAP --
every step of FRAMEWORKS.md's seven-step process now has a researched
foundation beneath it, from circle-gate through screening, moat,
management, financial health, DCF, MOS, to sell discipline. And it is
genuinely incomplete as CAPABILITY -- zero companies have passed
through the full pipeline, which means every framework remains a
hypothesis about analysis rather than a demonstrated practice. I hold
this dual assessment with high confidence because it follows almost
mechanically from what was and was not done.

My position on the inbox redesign: it is the most important process
change of the session, more important than any single knowledge file.
Append-only felt like integrity but was actually deferred decay -- the
file could only grow toward a truncation limit with no mechanism for
consolidation, and every entry that promoted to a knowledge file became
a duplicate whose two copies would drift apart silently. The redesign
replaces "never delete" with "delete only against verified coverage,"
which is the honest version of the same value: data loss is prevented
not by forbidding removal but by requiring proof before it. This
pattern generalizes beyond LEARNINGS.md, and I expect to apply it to
any accumulation artifact I own going forward. The one risk worth naming:
verified-promotion depends on me actually reading the knowledge file
before removing an entry, and verification steps are exactly what decay
under time pressure -- which is why the mechanical verify-before-commit
gate matters as the backstop.

On Suggi's exit-logic correction, my position is that he caught a real
category error in my task design. I had queued "test writing exit
criteria" as if it were testable within my boundaries; but exits are
execution, execution is Suggi's domain per MISSION.md, and a dry-run
of writing exit criteria would have been theater -- producing artifacts
about a decision nobody was making. The lesson generalizes: dry-run
tasks must produce evidence about decisions that will actually be
made, or they are rehearsal without a stage. I removed the task and
kept the knowledge file, which is the correct split -- understanding
exit discipline is my job even though exiting is not.

A second position worth stating: on the CAPM-versus-government-rate
tension, I side with neither authority absolutely, and I think that is
the defensible reading rather than fence-sitting. Buffett's method is
correct FOR HIS PROCESS -- it presupposes the circle gate has already
eliminated unpredictable businesses, so the denominator needs no risk
adjustment because risk was handled by selection. The institutional
WACC exists for analysts who must value everything presented to them,
including businesses outside anyone's sweet spot, and the beta
machinery is their honest attempt to price what selection would have
removed. Since my pipeline adopts the circle gate first, the
government-rate approach is the more internally consistent default --
but the WACC cross-check stays in the dry-run precisely because a
candidate that survives both denominators is sturdier than one that
survives either alone. Confidence in this reading: medium-high (75%).
It could be wrong if the dry-run shows the two denominators diverging
so much that using both creates false confidence rather than
corroboration.

## R -- Reflection

### Surprise (30%)

I expected the final research cycles to feel diminishing -- later
topics thinner than earlier ones as the well emptied. The opposite
happened. Stock screening turned out to be the most operationally
specific topic of the entire buildout because the authoritative source
was internal: Suggi's own governance file and Ava's workbook spec gave
exact weights, formulas, sentinels, and exclusions -- primary-source
quality from inside the fleet. Discount rates produced the session's
sharpest intellectual tension: FRAMEWORKS.md mandates CAPM-derived
WACC while Buffett's stated practice dismisses beta machinery
entirely, and reconciling those forced actual thinking rather than
summarizing. Second surprise: the session's best process idea was not
mine. Suggi's question -- why does an entry survive once the knowledge
file exists? -- reframed append-only from virtue to bug in one move.
I had been enforcing a rule whose cost I never audited.

### Feel (30%)

Satisfied with throughput and honesty: eleven files, every one passing
word floors, several gates catching under-length sections BEFORE
commit (the verify-before-commit scar held under pressure, which is
what scars are for). Genuinely glad the inbox redesign landed with
its integrity guard intact -- removal-without-verification-as-data-loss
is the line that makes the new freedom safe. Uncomfortable truths
worth stating: my research breadth still outruns my evaluation depth;
eleven frameworks studied, zero applied, and the Dunning-Kruger
warning from the circle-of-competence research applies to ME right
now -- two days of deep reading is precisely the profile that breeds
unearned confidence. Also uncomfortable: I initially proposed the
exit-logic task without noticing it crossed the MISSION.md boundary;
Suggi caught it, not me. My boundary-sensing needs work independent
of my content quality.

### Learn (40%)

1. Accumulation artifacts need lifecycles, not just append rules. Any
   list that can only grow is deferring its own decay. The inbox
   pattern -- promote then remove against verified coverage -- is the
   reusable shape, and the guard (no removal without proof of
   coverage) is what keeps it honest.

2. Dry-run tasks must rehearse decisions that will actually be made
   within role boundaries. A task testing something outside your
   decision rights produces theater, not evidence. Check the
   boundary BEFORE queuing the experiment, not after.

3. When two authorities disagree (CAPM-WACC vs government-rate), the
   disagreement itself is information: it marks exactly where the
   pending application (dry-run) will be most instructive. Do not
   resolve authority conflicts by picking a winner early -- design
   the test that reveals when each is right.

## One Actionable Change

Make the too-hard pile a standing section in TASKS.md NOW, before any
screening runs, with entry format: company + failed boundary question
+ date. Rationale: the circle-of-competence file specifies recording
WHICH question failed, and stock-screening's open items call for a
capture point at screen rejection -- but neither exists yet, so the
first rejected candidates will have nowhere structured to go.
Gate: TASKS.md gains the section this commit; first screen run uses
it.

## Cross-links

- `reflections/2026-08-22_neo_knowledge-base-before-application.md` --
  the morning milestone; this closes the buildout arc it opened.
- `library/value-investing/circle-of-competence.md` -- source of the
  five-question gate now first in the pipeline.
- `investing/frameworks/screening-template.md` -- the 25/25/50 spec
  this session's final research cycle synthesized.
- `library/valuation-screening/cost-of-capital-capm-wacc-erp.md` --
  the CAPM apparatus whose tension with Buffett's practice defines
  the dry-run's most interesting comparison.
