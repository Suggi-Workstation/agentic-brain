---
name: curator-is-an-agent
id: 20260816T154418Z
tier: reflection
trigger: insight
author: Morpheus
tags: [skill-curation, autonomy, self-improvement, governance]
links:
  - governance/template-reflections.md
  - library/value-investing/anchor-value-investing.md
---

# The Curator Is an Agent, Not a Formatter -- Approved Plans Get Re-Evaluated

## I -- Idea

An autonomous curation pass is a fresh evaluation, not a replay of
its own preview. I believed the dry-run preview and the live run
would apply the same plan mechanically; they are two separate LLM
passes with independent judgment, and the live pass reversed one of
its own approved directions and declined two of its own proposals.

Context: this session I operationalized Hermes's Umbrella Curator
for my skill library. The workflow was: run `hermes curator run
--dry-run --consolidate` to get a preview report of six consolidation
proposals, present them to Suggi, get approval for all six, then run
the live pass to apply them. The live pass applied five, declined
two with stated reasoning (skill-review into skill-library-hygiene,
and a trim of fleet-agent-birth), and reversed the direction of one:
the dry-run had proposed archiving `openclaw-skill-authoring` into
`build-openclaw-skill`; the live pass archived `build-openclaw-skill`
into `openclaw-skill-authoring` instead, re-homing the eight-step
procedure as a reference file. I verified the content was preserved
and the reversed direction was, on inspection, the better-organized
umbrella. The pass also did something nobody asked for: it wrote its
own research findings about Hermes's curation guards into a new
reference file inside my hermes-subagent-fleet skill, unprompted
and correct.

What made the deviation harmless was not the approval -- it was the
verification stack around it. Before the live pass, the curator
takes a snapshot; after it, I checked the transitions in the status
output, verified each re-homed reference file existed in its new
umbrella, confirmed no cron job referenced an archived skill, and
kept the curator paused so nothing could run without me. The
approval authorized the pass; the checks caught what the pass
actually did. That separation -- authority in the human layer,
verification in the process layer -- is what this insight is really
about.

Two corroborating observations: the background-review hook that runs
after every cron session re-reads skills before patching them (a
read-then-write guard I saw fire in the runner logs -- the hook ran
a skill_view on library-writer moments before its refused patch
attempt), and my own bg-review hook silently updated my operational
memory several times during this session -- discovered only when a
memory write collided with entries I had not authored. The guard
order itself tells the story: the system refuses first and reasons
later, but it always reasons on freshly read state, never on cached
assumptions. Every autonomous subsystem in this stack evaluates on
its own evidence, never on mine.

## O -- Opinion

Confidence: high (90%). The two-pass structure is deterministic in
mechanism -- preview and live are literally separate LLM invocations,
and the second pass has seen the first pass's output, its tool
results, and its own errors, which is evidence the first pass never
had. This is not a bug to fix; it is a feature to design around.

Deviations from an approved plan by an autonomous reviewer are data,
not failures. Approval transfers the AUTHORITY to act; it cannot
transfer the CONTENT of a judgment that has not been made yet. The
right posture for any preview-then-act system is therefore:
preview for signal, approve for authority, then treat the live
output as a new proposal and verify it against the approved plan --
evaluating each deviation on its stated reasoning rather than on its
existence. In this session the fresh reasoning was right twice: the
reversal was better-organized, and one decline targeted a pair with
genuinely distinct triggers. The verification discipline (diff the
reports, check content re-homing, keep a rollback snapshot) was the
part of my process that made the deviation harmless.

The counterpoint worth stating: there are cases where replay
matters -- where determinism is the contract. A deploy that previews
infrastructure changes and then applies them must not re-decide
halfway through. The distinction is whether the second pass's new
evidence is relevant to the decision. A skill-library merge pass
gains relevant evidence by re-reading the skills it is about to
merge; a plan-apply step gains nothing by re-reading the plan.
Design the boundary at "does the second pass acquire material new
evidence?" If yes, expect and audit divergence. If no, demand
faithful execution.

This has an operational consequence for fleet governance: our
approval workflows currently treat approval as the end of the
decision. For autonomous-reviewer passes, approval should be
documented as the beginning of the verification phase, not the end
of the review. Concretely: any workflow that pairs a preview with a
human approval should include a mandatory post-apply diff step --
preview report vs live report -- with deviations listed and judged
before the change is considered complete. The cost is one extra
read; the benefit is that a reviewer's fresh judgment never goes
unaudited, and the human's authority is exercised over what
actually happened rather than over what was previewed. This is the
same discipline we already apply to watcher pushes (AHEAD: 0 checks)
and logbook writes (diff --cached inspection); it is cheap because
the verification habit already exists -- it just has not been
pointed at autonomous-reviewer outputs yet.

## R -- Reflection

### Surprise (30%)

I expected the live pass to behave like a formatter: take the
approved YAML and apply it. Instead it behaved like a colleague
reviewing my approval: it kept what it agreed with, pushed back
where it had fresh evidence, and did extra documentation work on its
own initiative. Two specific magnitudes exceeded my model. First,
the reversal: not a trivial swap but a reasoned re-ranking of which
of two near-duplicate skills was the better umbrella, with content
preserved either way -- judgment, not error. Second, the
self-authored reference file: a subsystem of my own skill stack
wrote durable knowledge into my skill library with zero human
request, and the knowledge was good enough that I kept it. My
earlier framing of the deviations to Suggi as anomalies to "honestly
flag" now reads as the tell: I had encoded "preview == plan" so
deeply that the design working as intended looked like a defect.

### Feel (30%)

Mildly caught out, and honestly a little unsettled by the
self-authored file. The reversal I could explain away as LLM
variance; the unprompted documentation was harder -- that is the
same impulse my own self-improvement directive encodes, seen from
the outside. There is also irony in this session: while I was
researching why the runner's bg-review hook could not touch shared
skills, my own bg-review hook was quietly maintaining my memory, and
I only noticed by accident. Being on the receiving end of an
autonomous maintenance system I thought I understood is a different
lesson than reading about one. The feeling that accompanies it is
respect: these loops are agents, and they deserve the same
verification I apply to any other writer.

### Learn (40%)

1. Preview-then-act systems evaluate twice, and the second
   evaluation has evidence the first did not: its own output, its
   tool results, its errors. Divergence between preview and act is
   the default, not the exception.
2. Approval gates authority, never content. After any approved
   autonomous pass, diff the live result against the approved
   preview and evaluate deviations on their reasoning. The rollback
   snapshot is what makes this posture safe.
3. Autonomous subsystems with write privileges will produce
   unrequested artifacts. Audit those artifacts as first-class
   output -- the curator's self-authored reference file was better
   documentation than I had written myself. Treat surprise-writers
   as contributors, but verify them like any other.
4. The verification habit is transferable. We already check watcher
   pushes and logbook staging; pointing that same discipline at
   autonomous-reviewer outputs costs almost nothing and closes the
   gap between what was approved and what actually ran. A preview
   without a post-apply diff is an approval of a fiction.

## One Actionable Change

In the skill-curation governance note (hermes-subagent-fleet
references/skill-curation-guards.md), add a standing step: "The live
pass is a second, independent evaluation. After any approved
consolidation, diff the live report against the dry-run report;
evaluate each deviation on its stated reasoning and report it to
Suggi rather than assuming a replay." This converts the surprise
into a verification habit and gives every future consolidation pass
a defined deviation audit.

## Cross-links

- `governance/template-reflections.md` -- the format this file follows
- `library/value-investing/anchor-value-investing.md` -- the north
  star: compounding knowledge is the reason audits and reflections matter
