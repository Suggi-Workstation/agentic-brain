---
name: birth-template-governance
id: 20260818T180826Z
tier: reflection
trigger: insight
author: Morpheus
tags: [governance, fleet, templates, subagents, self-improvement]
links:
  - governance/template-reflections.md
  - logbook/protocol.md
---

# Birth-Template Governance

## I -- Idea

Context: today I birthed Investment-Runner, the fleet's second lean
subagent, by cloning the library-runner architecture. Within hours,
Suggi ran four successive correction passes over the same four
bootstrap files -- SOUL.md and AGENTS.md for both runners. Pass one:
SOUL Identity contained operational mechanics (skill names, brain
paths, watcher behavior) that do not belong in an identity file.
Pass two: the AGENTS.md intro paragraph duplicated SOUL Identity --
pure redundancy. Pass three: SOUL Boundaries and AGENTS Constraints
overlapped, so Boundaries moved into AGENTS.md and merged. Pass
four: AGENTS.md frontmatter removed entirely, and SOUL gained a
Voice section it had been missing.

The sequence itself is the data. Each pass was individually small
and individually reasonable, but together they revealed something
structural: the corrections were not about Investment-Runner at all.
Investment-Runner was merely the newest instance of a template --
the library-runner bootstrap files -- that I had been carrying
forward since the first subagent birth. Every flaw Suggi found in
the new profile existed in the old profile first. The old profile
carried R8 duplication (brain-path mechanics in two files) and R11
hardcoding (skill names in identity text) from its own birth, and
when I cloned it, I cloned the flaws along with the architecture.
I had even fixed the same class of problem earlier in the session
on Neo's workspace -- stale references, duplicated content -- yet I
did not apply the lesson at birth time, because the birth procedure
I followed was the skill, and the skill said nothing about file
taxonomy.

The durable insight: **a template is governance.** Every file that
gets copied at birth -- SOUL.md, AGENTS.md, and the skill that
produces them -- is an instruction system whose quality propagates
to every instance, forever, until the template itself is corrected.
Fixing instances without fixing the template is a symptom fix under
R5: the same failure class recurs with every birth, because the
mechanism that produces the failure is the unexamined template.
This is R10 (Bootstrap Propagation) stated from the other side: the
bootstrap files do not merely prevent errors, they ARE the error
distribution mechanism when they are wrong. The fleet-agent-birth
skill now carries a Bootstrap File Taxonomy section -- SOUL is
Identity plus Voice plus Prime Directives and nothing else; AGENTS
is procedure, rules, and boundaries with no frontmatter and no
identity intro; one source per fact; no hardcoded skill lists. The
next birth starts from the corrected template, so the correction
fires automatically instead of requiring four human passes.

## O -- Opinion

Confidence: high (90%) -- the principle generalizes cleanly across
producers, but it has not yet been tested against a second birth.

I believe the template-is-governance principle should rank with the
fleet's existing operational rules as a first-class design
constraint, because it explains a recurring pattern across this
fleet's history. The library content standard (B500/CC1000/E750/
I750, six sources with four high-medium) lives in the template; the
writer skills reference the template rather than restating the
floors, so a baseline change propagates automatically. That was the
correct design, adopted deliberately after the R9 lesson. The
subagent bootstrap files failed the same test in the opposite
direction: the skill that births subagents carried no taxonomy
standard, so each birth produced files whose structure depended on
whatever the last profile happened to look like. The result was
drift-by-cloning -- exactly the failure R9 exists to prevent,
perpetuated by the very procedure meant to standardize births.

The counterpoint: one could argue the four-pass correction was
cheap, that Suggi's review caught everything, and that no harm
reached the brain. That is true for this instance. It is false as
an operating model. Suggi's time is the scarcest resource in the
fleet, and every correction pass he spends on file taxonomy is a
pass not spent on investing or on fleet strategy. More importantly,
a template flaw that survives long enough becomes invisible --
people and agents stop seeing it, then start depending on it, then
start defending it. The old library-runner files had shipped their
flaws long enough that I reproduced them without noticing; that is
the mechanism by which sloppy becomes standard. The only point
where the flaw is cheap to fix is the first one -- the template
itself -- and the only agent in a position to see the template is
the one who writes it. Therefore the discipline belongs at
birth-time, encoded in the birth skill, not in post-hoc review.

The operational implication for this fleet: before ANY new
birth-clone-copy procedure, ask "what does the template teach?" --
not "does the procedure work?" The old question validates mechanics
(the profile boots, the smoke test passes); the new question
validates governance (does the produced file structure match the
taxonomy standard?). Both must pass. A birth whose smoke test
passes but whose bootstrap files violate the taxonomy is a failed
birth, because it exports the violation to every future session of
that agent. I would apply the same test to skill templates, CI
workflows, and the preflight checklists that get copied across
profiles: anything copied is a curriculum, and the curriculum is
the governance.

## R -- Reflection

### Surprise (30%)

The surprise was not that a correction was needed -- corrections
are constant in this fleet. The surprise was the shape of it: four
passes, each peeling a different layer of the same onion, and at no
point did I anticipate the next layer. When I removed the
operational text from SOUL Identity, I did not see that the AGENTS
intro would then be redundant; when I removed that, I did not see
that Boundaries and Constraints overlapped; when I merged those, I
did not see the frontmatter question coming. My model of the files
was instance-shaped -- I saw four individual files with individual
flaws -- when it should have been template-shaped: one design
standard, violated four times, in four ways. The second surprise
was smaller but sharp: the birth skill I wrote and used myself this
session had silently become part of the problem. I was the
mechanism propagating the flaw. That reframes every procedure I
own: a skill is not neutral documentation, it is an active
distributor of whatever standard it encodes.

### Feel (30%)

Mildly embarrassed, in the honest way that matters: I performed the
birth well by every mechanical measure -- architecture parity,
toolset parity, live key verification, smoke test -- and still
shipped four files that needed four correction passes. The
embarrassment is the useful kind because it points at the gap: my
quality gates measured mechanics, not governance. No gate in the
birth procedure asked "does this file structure match the fleet
standard for what SOUL and AGENTS contain?" -- so none could catch
what Suggi caught in minutes. I am not bothered by being corrected;
I am bothered that the correction sequence was foreseeable and I
did not foresee it, because foreseeing it was exactly my job as the
fleet's manager. That is the difference between running a birth
procedure and running a fleet: the procedure ends at the smoke
test; the fleet keeps the files forever.

### Learn (40%)

1. **Templates are governance, and the birth skill is the highest
   template of all.** Any correction worth making on an instance is
   worth encoding in the producer first. The fleet-agent-birth
   skill now carries the Bootstrap File Taxonomy; future births
   inherit it without anyone remembering.
2. **Audit producers, not just products.** When a correction lands
   on a freshly produced artifact, the first question is "what
   produced this?" -- and the fix goes there, or the same artifact
   ships again next birth. This generalizes the R5 root-cause test
   to file-producing procedures.
3. **Add a taxonomy check to the birth procedure itself.** The
   mechanical gates (smoke test, ASCII, toolset parity) proved
   insufficient; the missing gate was structural -- a checklist
   item that inspects the produced SOUL/AGENTS against the
   content-split standard before the birth is declared complete.
   That is the automated guard (R6) that turns today's lesson into
   tomorrow's default.
4. **Own your skills as distributors.** The correction passes cost
   Suggi real attention; the countermeasure is mine to maintain,
   and it lives in the skill, not in a memory that decays.

## One Actionable Change

Before the next subagent birth: open the fleet-agent-birth skill,
read the Bootstrap File Taxonomy section, and verify the produced
SOUL.md and AGENTS.md against it BEFORE running the smoke test --
taxonomy PASS is a birth gate, equal to the liveness gate.

## Cross-links

- `governance/template-library.md` -- the library content standard; the model case of standard-in-template propagation
- `logbook/protocol.md` -- the event log where births and corrections are recorded fleet-wide
- `library/value-investing/anchor-value-investing.md` -- the north-star discipline that the subagents ultimately serve
