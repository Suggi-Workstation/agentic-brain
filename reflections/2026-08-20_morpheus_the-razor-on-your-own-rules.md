---
name: the-razor-on-your-own-rules
id: 20260820T052619Z
tier: reflection
trigger: insight
author: Morpheus
tags: [governance, contract-procedure-separation, rules, audit, razor]
links:
  - reflections/2026-08-19_morpheus_isolation-is-the-default.md
  - research/proposals/per-agent-workspace-search.md
---

# The Razor on Your Own Rules -- Standards Hide Procedures in Plain Sight

## I -- Idea

A governance standard you have read dozens of times can still hide
procedural violations in plain sight, and the only way to find them is
to apply a single razor to every item, one by one, with the question
spoken aloud: does this state a standard (WHAT must be true), or does
it embed a trigger, schedule, or step-sequence (WHEN + HOW) that
belongs in a skill?

I had read my own R1-R22 rules many times. I wrote most of them. I
believed they were clean. Then Suggi asked me to check them all
against the contract-procedure separation principle -- the same
principle I had just used to rewrite R15 -- and I found three rules
that violated it. Not new rules I had not examined; rules I had
read, cited, and enforced for weeks without noticing the violations.
R13 was the worst: a five-step git procedure ("Pull before edit.
Commit before destructive change. Never force-push. Resolve by
reading. Push only verified.") masquerading as a standard. R12
embedded a method ("Manually test...") in what should have been a
prohibition. R4 was a telegram-style checklist that read as procedure
shorthand. Each one had survived because it was SHORT -- the
procedural content was compressed enough to look like a standard at
a glance.

The context: this session continued the governance work from
2026-08-19. I had proposed R22 (Isolation by Default) and Suggi
approved it. He then asked me to align Neo's R1-R21 with mine (seven
rules were missing their Born-from clauses). Then he asked me to
rewrite R15 so it does not force a session-end revision -- the
session-end procedure lives in the skill, not the contract. That
rewrite was the razor: "At session-end, audit..." is a WHEN + HOW
instruction living in the WHAT layer. Once I saw it in R15, Suggi
asked the natural next question: do the other rules have the same
problem? I checked all 22, one by one, and found three more. The
process was mechanical: read each rule, ask "does this state what
must be true, or does it tell me when and how to do something?", and
classify. Three failed. The rest passed. But the three that failed
had been there for weeks, read and cited without triggering the
razor -- because nobody had asked the question over the full set.

What I knew before this audit: the contract-procedure separation
principle (AGENTS.md = lean contract, skills = procedures). I had
even cited it from Mnemosyne memory when rewriting R15. What I knew
after: the principle is easy to cite and hard to apply consistently.
The gap between citing a standard and living it is exactly the gap
the razor exposes. And that gap is not a one-time discovery -- it is
a recurring drift. Procedures accumulate in contracts because they
are convenient to write there. The razor is the tool that finds them,
but only if it is applied deliberately and exhaustively, not just to
the rule that triggered the question.

## O -- Opinion

Confidence: high (90%).

Every rule set should be audited with the contract-procedure razor
periodically, not just when a specific violation is caught. The
evidence is this session: I had the principle in memory, I had just
applied it to R15, and I still missed R4/R12/R13 until Suggi asked
me to check all of them. If the razor is not applied deliberately and
exhaustively, procedural content accumulates in the contract
unnoticed -- compressed shortcuts that look like standards because
they are short, but that embed the wrong layer's content.

The deeper opinion: the razor is not "is this rule good?" but "is
this rule in the right layer?" A rule can be correct in substance and
wrong in placement. R13's five steps are all true and all important --
but they belong in the git workflow skills, not in the contract. The
contract should say what is protected (git history, force-push
forbidden, verified work only) and point at the skills for the
operational sequence. This is not a cosmetic distinction: when the
procedure changes (new git workflow, new tooling), the contract
should not need updating. If it does, the procedure was in the wrong
layer.

A second opinion, on the Mnemosyne fix: Neo's provider key was
missing from birth, and nobody noticed for three days. His preflight
skill passed because built-in alone is sufficient -- but his AGENTS.md
describes Mnemosyne as the primary durable memory. The preflight
correctly flagged the contradiction, which is the design working. But
the birth skill should have verified `memory.provider` at provisioning
time. This is the same class as the v1.2 birth-template governance
drift: the template was incomplete, and every birth propagates the
gap until the birth skill encodes the check. I state this at medium
confidence (75%) because I have one data point -- but it is the
second birth-related gap I have found, and both had the same root
cause: the birth template was copy-pasted without verifying that
every config layer was populated. The pattern is clear even with two
data points.

A third opinion, narrower: the contract-procedure separation audit
should be a periodic practice, not a one-time event. Procedures
accumulate in contracts because writing them there is convenient --
you have the rule open, you add the steps, it looks complete. Six
months later nobody remembers those steps belong in a skill. The
razor applied periodically (every few sessions, or whenever a rule is
modified) catches the drift before it compounds. R15 was the trigger
this time; next time it could be a new rule that someone writes with
embedded procedure without realizing it. The audit is cheap (read 22
rules, classify each) and the payoff is high (three violations found
this round). The cost of not auditing is governance drift -- the same
failure class R15 itself warns about, applied to the rule system's
own structure.

## R -- Reflection

### Surprise (30%)

I expected the R15 rewrite to be the only contract-procedure
violation. It was not -- it was the tip. Three more rules had the
same problem, and they had been there for weeks. The surprise is not
that they existed; it is that I had read them so many times without
seeing the violation. R13 in particular is a five-step procedure
written as a single paragraph. It is SHORT, so it passes the eye as a
standard. But "Pull before edit. Commit before destructive change."
is a sequence -- it tells you what to do and in what order. That is a
procedure, not a standard.

The Mnemosyne finding surprised me differently. I expected Neo's
setup to match mine -- we are on the same VPS, same plugin, same .env
vars. The difference was one config key that was never set at birth.
Three days of memories went to the wrong DB. The surprise: how
invisible a missing config key is when everything else looks correct.
The plugin registered 40 tools. The log showed "registered." Only
`hermes memory status` revealed the provider was not wired. The
signal was there, but it required the right command to surface it.

### Feel (30%)

Honest read: I should have caught R4/R12/R13 earlier. I wrote the
contract-procedure separation principle into my own memory. I cite
it. And I still had three procedural rules in my contract. The
discomfort is not that Suggi caught it -- it is that the razor was
available to me the whole time and I did not apply it exhaustively.
Applying it to R15 was reactive (one rule, caught by a specific
question). Applying it to all 22 was proactive, and it found three
more. The lesson: a razor applied to one item is a fix; a razor
applied to the full set is an audit. Audits find what fixes cannot.

On the Mnemosyne fix: I feel good about the diagnosis. I traced the
exact root cause (one missing config key), verified it against my own
working setup, applied the fix, restarted the service, and confirmed
across nine layers. That is the methodical verification the
preflight scar (2026-08-01) demands. No guessing, no assumption.

### Learn (40%)

1. Apply the contract-procedure razor to the full rule set
   periodically, not just to the rule that triggered the question.
   A razor applied to one item is a fix; applied to the full set it
   is an audit. Audits find what single fixes miss. R15 was the
   trigger; R4/R12/R13 were the harvest.

2. A rule can be correct in substance and wrong in placement. The
   test: would this rule need updating if the procedure changed? If
   yes, the procedure is in the contract, not the standard. Move it
   to a skill and leave the standard.

3. A missing config key is invisible when everything else looks
   correct. The only reliable signal is the right verification
   command (`hermes memory status`, not the agent.log registration
   line). The birth skill should verify provider configuration at
   provisioning time -- not after three days of silent failure.

4. Short rules are the most dangerous hiding place for procedural
   content. A five-step procedure compressed into one paragraph looks
   like a standard at a glance. The razor does not care about length
   -- it cares about content. Apply it to the short rules especially.

## One Actionable Change

Add a step to the session-end Gate Rules Self-Check: "Apply the
contract-procedure razor to any rule modified this session: does it
state a standard (WHAT) or embed a trigger/schedule/step-sequence
(WHEN+HOW)? Procedural content belongs in skills." This makes the
audit periodic and targeted -- it checks the rules that were touched,
not the full set every time. The full-set audit stays as a periodic
deep dive (R15 audit). Until the Self-Check is updated, carry the
habit: after editing any rule, run the razor on it before committing.

## Cross-links

- `reflections/2026-08-19_morpheus_isolation-is-the-default.md` --
  the prior session's reflection on the same governance work; R22
  was proposed there and formalized this session.
- `research/proposals/per-agent-workspace-search.md` -- the proposal
  that triggered the design work leading to R22.