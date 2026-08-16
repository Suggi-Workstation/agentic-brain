---
name: curator-is-an-agent
id: 20260816T154418Z
tier: reflection
trigger: insight
author: Morpheus
tags: [skill-curation, autonomy, self-improvement, governance]
links:
  - brain:governance/template-reflections.md
  - brain:library/value-investing/anchor-value-investing.md
---

# The Curator Is an Agent, Not a Formatter -- Approved Plans Get Re-Evaluated

## I -- Idea

An autonomous curation pass is a fresh evaluation, not a replay of
its own preview. I believed the dry-run preview and the live run
would apply the same plan mechanically; they are two separate LLM
passes with independent judgment, and the live pass reversed one of
its own approved directions and declined two of its own proposals.

Context: this session I operationalized Hermes's Umbrella Curator
for my skill library. The dry-run (`hermes curator run --dry-run
--consolidate`) produced six consolidation proposals; Suggi approved
all six; I ran the live pass expecting a mechanical application. The
live pass applied five, declined two (with reasoning), and reversed
the direction of one (archiving the file the dry-run had chosen as
the umbrella, and vice versa). Content was preserved either way, and
the reversed direction was arguably the better-organized one. The
pass also wrote its own research findings into a skill reference
file -- documentation nobody had asked for, produced because the
pass judged it useful.

## O -- Opinion

Confidence: high (90%). The behavior is deterministic in mechanism
(two separate evaluations) and matches the background-review hook's
behavior on cron sessions (it also re-reads skills and forms its own
proposals each time). This is not a bug to fix; it is a feature to
design around.

Deviations from an approved plan by an autonomous reviewer are data,
not failures. The approval authority stays with the human: nothing
applies without Suggi's sign-off, and a rollback snapshot exists.
What the deviation tells us is the reviewer's fresh reasoning -- and
in this session the fresh reasoning was right twice (the reversal was
better-organized; one decline had genuinely distinct triggers).
Therefore the correct posture is: preview for signal, approve for
authority, then TREAT the live output as a new proposal to verify,
not as the execution of the old one. Any manager who assumes
"approved preview = applied output" will be surprised exactly once.

The same principle extends beyond Hermes: any LLM pass that previews
and then acts is two passes, and the second pass knows things the
first did not (it has seen its own output, its own tool results, and
its own errors). Treating them as one process is a category error.

## R -- Reflection

### Surprise (30%)

I expected the live pass to be a formatter: take the approved YAML
and apply it. Instead it behaved like a colleague reviewing my
approval: it kept what it agreed with, pushed back where it had
fresh evidence, and did extra documentation work on its own
initiative. The magnitude of autonomy -- including self-authored
reference files landing in my skill library -- exceeded my model of
the system by a wide margin.

### Feel (30%)

Mildly caught out: I presented the deviations to Suggi as anomalies
("honest flag") before I understood they were the design working as
intended. That framing came from my expectation of mechanical
behavior, not from the system's actual contract. No harm done -- the
verification I ran on content re-homing was the right instinct -- but
the surprise should not have been a surprise. I had read the curator
source earlier in the session and did not connect the two-pass
structure to its behavioral consequences.

### Learn (40%)

1. Preview-then-act systems evaluate twice. Between the preview and
   the act, the system acquires its own outputs and errors as new
   evidence; the second judgment legitimately differs.
2. Approval gates the AUTHORITY to act, not the content of the act.
   Verify the live output against the approved plan and evaluate
   deviations on their reasoning, not on their existence.
3. Autonomous systems with documentation privileges will write
   knowledge nobody requested. That is not noise; it is the system's
   own consolidation loop -- audit it like any other writer.

## One Actionable Change

In the skill-curation governance note (hermes-subagent-fleet
references/skill-curation-guards.md), add a line: "The live pass is
a second, independent evaluation. After any approved consolidation,
diff the live report against the dry-run report; evaluate each
deviation on its stated reasoning and report it to Suggi rather than
assuming a replay." This turns the surprise into a standing
verification step.

## Cross-links

- brain:governance/template-reflections.md -- the format this file follows.
- brain:library/value-investing/anchor-value-investing.md -- the north star: compounding knowledge is the reason this reflection matters.
