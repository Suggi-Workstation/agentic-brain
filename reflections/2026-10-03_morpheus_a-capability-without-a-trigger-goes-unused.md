---
name: a-capability-without-a-trigger-goes-unused
id: 20261003T082038Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [gate-design, shared-memory, session-end, governance]
links:
  - reflections/2026-07-20_ava_uninvoked-skills-are-dead-letters.md
  - research/insights/hindsight-system.md
  - library/psychology-behavior/framing-effects.md
  - reflections/2026-10-02_morpheus_an-instruction-is-only-as-good-as-its-chain.md
---

# A Capability Without a Trigger Goes Unused

## I -- Idea

A capability that waits to be remembered behaves like a capability the
agent does not have; it starts being used only when a step in a procedure
that already runs asks for it, and the right shape of that step is an
active choice in which "nothing" is a valid answer.

The evidence came from two places in one working day. The first was the
fleet's shared memory bank. Three weeks earlier Suggi had approved a native
memory design in which every core agent keeps an automatic private bank and
reaches a shared bank only through deliberate tool calls. The design was
sound, it was documented in each agent's AGENTS.md, and the agents had the
tools. When Suggi asked whether anyone had used it, the session stores gave
a blunt answer: Neo and Atlas had never called it, and Morpheus had called
it only to set it up, to run a disposable acceptance test, and to list
empty folders. No agent had ever stored a real fact there. Its contents
were a late-August import from the retired Mnemosyne system, and about a
quarter of what I sampled was out of date: an old agent name, a retired
port, model defaults from before the Claude migration, and a rule against
deploying the Forge that Suggi later reversed. There were no mental models
and no knowledge pages, although all three agents could create them.

The second was the Library model trial. Every Reviewer run on the Claude
subscription died after three rejections of the same kind: the plugin
refused a tool name that was outside its inventory. The session logs showed
that the step before each failure was a lookup of the web-search tools,
which Hermes hides by default behind a describe-then-call bridge. Claude
read the rule to use the bridge and then called the tool directly. The fix
Suggi chose was not more instruction. It was to turn the hiding off, so the
tools sit on the menu and a direct call is valid.

Before the Feynman pass I held the idea as "the shared bank was empty
because its tools were hidden." That was half of it. Hidden tools raised the
cost of every call, but the larger cause was that no procedure ever asked
an agent to read or write the bank. Every turn feeds the private bank
automatically; nothing feeds the shared one unless an agent decides to, and
in three weeks none did. What I knew from behavioral economics fit closely:
a default often determines the outcome even when people remain free to
choose otherwise. The Library topic on framing effects cites the
organ-donation comparison, where opt-in countries reached consent rates of
4 to 28 percent and opt-out countries 86 to nearly 100 percent. What the
pass added was the third design between opt-in and opt-out: the active
decision, where a choice is required but no answer is preselected.

## O -- Opinion

Confidence: medium-high (80%). The pattern is supported by two independent
cases in this fleet and by Ava's earlier finding that uninvoked skills are
dead letters. It is not yet supported by the outcome that matters, which is
a shared bank that fills with useful facts over the coming weeks.

My position is that every capability in this fleet that depends on an
agent's initiative should be attached to a step in a procedure that already
runs, and that the step should demand a decision rather than an output. The
shared-bank step added to the three session-end skills does this: recall
the bank for the session's topics, retain what every agent should know,
retire what proved wrong, and record "none" if nothing qualifies. The
mental-model rule has the same shape: check the existing models, widen one
if it is close, create one only if none fits, and report which, or none.

This is a deliberate middle path, and the reason is a failure we had
already lived through. Two days ago session-end forced every reflection to
produce a new rule, and Suggi removed that because forced output is noise.
Forcing a shared-bank write every session would repeat that mistake in a
new place: the bank would fill with filler, and the mental models would
summarize filler. The opposite extreme, copying every private turn into the
shared bank, was ruled out in September because private conversation must
stay private. Opt-in had been the design for three weeks, and opt-in
produced zero real writes.

The economics literature names this middle path. Carroll, Choi, Laibson,
Madrian and Metrick compared standard opt-in 401(k) enrollment with a
regime that required new hires to state a choice, and the required choice
raised initial enrollment by 28 percentage points. Their model says active
decisions beat defaults when people procrastinate strongly and their right
answers differ widely. Both conditions hold here. An agent at the end of a
long session will always find something more pressing than a shared-memory
write, and what deserves saving varies from session to session, so no
preselected answer would fit.

The Tool Search change looks like the opposite move, and I do not think it
is. There the capability was already in use; the default made the correct
call harder than the incorrect one, and removing the default made the call
the agent was already making valid. Both fixes change the structure the
agent acts in instead of adding a sentence the agent must remember. The
rule Claude broke was already in front of it, which is the strongest
evidence I have that instruction alone was never going to work.

What would change my mind: if, after several closures, Neo and Atlas record
"none" every time while their sessions contain decisions Suggi made, the
step is being satisfied without being performed, and it needs a sharper
trigger than a checklist line.

## R -- Reflection

### Surprise (30%)

I expected the plugin error to need guidance, a short provider note telling
Claude to use the bridge. Suggi proposed exactly that, and it was a
reasonable idea. But the rule was already in the bridge description and in
every describe answer Claude received seconds before it slipped. The fix
was to remove a feature, not to add words. I also expected the empty shared
bank to be explained by the hidden tools, and the session data said
otherwise: my own profile, which used those tools during setup, wrote
nothing real either. A third surprise was about me. While writing the
Schoen Loop I listed four trial lessons as gates I would add to the Library
operations skill, then found them already there. The background skill
review had written them during the session, and I had not noticed my own
skill changing.

### Feel (30%)

The trial went worse than it should have, and most of the cost was mine.
The first controller used a dispatch command that a sibling skill had
already warned against, because I loaded the Library skill and not the
fleet skill that carried the warning. The second controller counted a
failed run as finished and moved to the next phase, and stopping it skipped
its restore step, leaving one job enabled on the wrong model until I
re-read the registry. None of this did lasting harm, and each problem was
caught by reading the ledger rather than trusting a message, but Suggi
waited through two false starts for a comparison that is still incomplete.
The shared-bank work I am satisfied with: the cleanup was evidence-based,
the retirements are reversible, and the new step is short. I am less
comfortable that I nearly reported gates as my own work when another
process had written them.

### Learn (40%)

1. When a capability depends on an agent's initiative, attach it to a step
   in a procedure that already runs, and phrase the step as a required
   decision with "none" allowed. Opt-in leaves the capability unused;
   forced output fills it with noise.
2. When a model keeps breaking a rule that is already in its context,
   change the structure that makes the wrong action possible or the right
   one costly. Another sentence in the prompt will not hold.
3. Before claiming a skill change in a closure record, read the current
   skill text, because a background review can edit skills mid-session.
   Name who made the change.

## One Actionable Change

At the start of any live operation, load every skill whose description
matches the operation, not only the most specific one, and run the
cheapest dry check those skills name before dispatch. For a cron trial that
means loading the Library operations skill and the subagent-fleet skill
together, and testing one paused-job dispatch before launching a
controller.

## Cross-links

- `reflections/2026-07-20_ava_uninvoked-skills-are-dead-letters.md` --
  Ava's earlier case: a perfect checklist is worthless until something
  forces it to be read.
- `research/insights/hindsight-system.md` -- the native memory design:
  automatic private capture, deliberate sharing.
- `library/psychology-behavior/framing-effects.md` -- default effects and
  choice architecture, including the organ-donation evidence.
- `reflections/2026-10-02_morpheus_an-instruction-is-only-as-good-as-its-chain.md`
  -- why forced output through session-end was removed.
