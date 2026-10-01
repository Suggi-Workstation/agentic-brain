---
name: an-instruction-is-only-as-good-as-its-chain
id: 20261001T223354Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [gate-design, governance, verification, session-end]
links:
  - reflections/2026-10-01_morpheus_a-workaround-ends-where-its-cause-lives.md
  - reflections/2026-07-23_ava_permissive-templates-produce-divergent-output.md
  - library/engineering-infrastructure/systems-engineering-complex-systems-under-constraints.md
---

# An Instruction Is Only as Good as the Chain It Runs Through

## I -- Idea

An instruction does what it says only if every rule and tool it runs through
does too, so fixing the sentence that states a policy is not the same as
fixing the policy.

This closure period began right after the previous session-end. Suggi asked
whether session-end forces a new rule every time, and recalled that we had
already changed the wording so it does not. He was right about the wording.
R7 in AGENTS.md, the Prime Directives in SOUL.md and the session-end gate step
all said the same thing: add a gate only when the session produced a failure
class, scar or insight; otherwise record "no gate warranted".

The force came through a chain instead. Session-end made a reflection
mandatory every time, with "no exceptions, no skips, no 'not warranted'
escape hatch". The reflection template then required every reflection to end
with One Actionable Change, defined as "something structural. A gate, a
checklist step, a script", with the checklist adding "executable" and "If you
cannot name one, the reflection is not done". Each rule was defensible alone.
Together they forced a structural change into every closure. The template's
Schoen Loop section also still carried the old R7 text, "every substantive
session adds one gate".

Suggi decided the fix: One Actionable Change becomes a suggestion that need not
be a rule or be implemented; the write-reflection skill describes only how to
write a reflection, not when; session-end keeps the reflection mandatory. I
changed the template, the write-reflection skill in three places (canonical,
runtime and legacy copies) and the session-end skills of Morpheus and Atlas.
Neo's needed no change for that point.

A second question followed: what period does the reflection cover? Suggi
expected the whole session, or the work since the last session-end in that
conversation. The skill said "from the Schoen Loop output", and the Schoen Loop
never says from when; in practice it covers what survives in context, which in
a conversation running since 19 September is far less than the session. We
settled on new wording for all three agents: one new reflection on the work
since the previous session-end, starting from the agent's own review and then
skimming Suggi's requests in the conversation history with `session_search`,
as a quick check rather than new research.

Suggi then asked me to run session-end to see if it works. It did not, fully.
`session_search` returned no results for any query over this conversation, and
scrolling inside it was refused: "anchor lives in the current session lineage
(already in your active context)". The tool the new step names cannot read the
current conversation, which is the one case the step exists for. A direct
read-only query of this profile's `state.db` listed all eight of Suggi's
requests since the previous closure in one call.

Before this period I would have said a policy is fixed when its statement is
fixed. Now I would say it is fixed when every path to its effect is fixed, and
that includes the tools an instruction names, not only the other rules.

## O -- Opinion

Confidence: medium (75%). Two instances in one short closure period, both
confirmed by direct evidence; the generalization rests on their shared shape.

My position: when a policy changes, audit the chain, not the sentence. That
means three checks. First, search for every rule that can produce the effect
the policy forbids, including checklists and templates that other procedures
call, not only the files that state the policy. Second, for each procedure
step that names a tool, run that tool once on the exact case the step names
before relying on it. Third, treat an instruction written in one place and
executed through another, such as a template called by a skill, as one unit
when reviewing it.

The evidence is concrete. The direct statements were correct in three places,
so a reviewer checking R7 would have passed it, as Suggi's memory did. Only
tracing session-end to write-reflection to the template's checklist exposed
the forced gate. The second instance is sharper: Suggi and I agreed wording
that named `session_search`, I applied it to three skills, and the first real
execution showed the tool excludes the current conversation. Nothing in the
wording was wrong as English; it was wrong as a description of what the tool
does in this case.

Ava's 2026-07-23 reflection on permissive templates found a mirror image:
permissive template wording let writers omit sections, and the checklist,
written in the same permissive language, never caught it. Here the template
was too strict, and its checklist enforced that strictness. In both, the
checklist inherits the template's assumptions, so a fault in the template
passes its own gate. The Library topic on systems engineering states the
general form: a system can comply with every narrow specification and still
fail its purpose, because performance arises from the relationships among
elements.

Why not higher confidence: two cases do not establish how often this happens,
and a chain audit has a cost. Tracing every caller for every wording change
would be bloat, which Suggi rejects. The audit should be proportionate:
mandatory when the change is a policy (what must or must not happen), optional
for phrasing. A cheap version exists: one search for the effect's keywords
across governance, skills and templates, plus one live run of any named tool.

A counter-position is that Suggi's question already did the audit, so the
process works. It worked because he asked. The goal is that the next forced
gate or broken tool reference is found by the procedure, not by luck or by
his memory of an earlier discussion.

## R -- Reflection

### Surprise (30%)

I expected the forced-rule question to have a short answer: R7 was fixed, so
no. Instead the force came from two rules that never mention gates in the
same terms. The reflection mandate said nothing about rules, and the template
said nothing about session-end; joined, they required a gate every closure.
I had read both files many times and not seen the join.

The second surprise was larger. I expected `session_search` to be the natural
way to read back a conversation; it was the tool the system prompt recommends
for prior work. I expected the new step to pass on its first run. Instead
every query came back empty and the scroll was refused, because the tool
treats the current conversation as already in context. That is true for a
short conversation and false for this one, where most of the history exists
only as a compressed summary. The tool's assumption and the step's purpose
point in opposite directions.

A smaller one: Neo's skill was already ahead on one point, a mandatory
reflection, and behind on another, updating one reflection per conversation
instead of writing one per closure. Three agents' copies of one procedure had
drifted in different directions.

### Feel (30%)

I am satisfied that the test caught the broken step before it misled a later
closure. Running the procedure instead of declaring it done is what Suggi
asked for, and it paid off within minutes. I am less satisfied that I wrote
and applied the `session_search` wording to three agents' skills without
running it once. That is the same failure my 2026-10-01 reflection named,
choosing a check without testing whether it can work on the real case, one
period later. The repeat is uncomfortable to state, but stating it is the
point of this section.

I also notice I first answered the forced-rule question by listing what was
correct before what was wrong. Suggi needed the second part more. The answer
did reach the chain, but leading with reassurance is a habit worth watching.

### Learn (40%)

1. When a policy changes, search for its effect, not its wording: find every
   rule, checklist and template that can produce the forbidden outcome, and
   follow each caller one hop into what it calls.
2. Before a procedure step that names a tool is relied on, run the tool once
   on the exact case the step names. A tool can be correct in general and
   excluded from the one case that matters, such as the current conversation.
3. Copies of one procedure across agents drift independently. When one copy
   changes for a policy reason, diff the others against the policy, not
   against the changed copy.

## One Actionable Change

In the session-end skills of Morpheus, Neo and Atlas, I would replace the
`session_search` instruction with a read-only query of the agent's own
`state.db` listing Suggi's messages in this conversation since the previous
closure's timestamp. That query worked on the first try during this closure.
It is a suggestion pending Suggi's approval, since he agreed the current
wording.

## Cross-links

- `reflections/2026-10-01_morpheus_a-workaround-ends-where-its-cause-lives.md` -- the previous closure, whose lesson about untested checks repeated here.
- `reflections/2026-07-23_ava_permissive-templates-produce-divergent-output.md` -- a template's checklist inherits the template's assumptions; here the template was too strict rather than too loose.
- `library/engineering-infrastructure/systems-engineering-complex-systems-under-constraints.md` -- systems can meet each narrow specification and fail as a whole.
