---
name: council-of-five
id: 20261004T162629Z
tier: insight
status: active
source:
  - 20260720T140808Z
  - 20260724T104820Z
  - 20260901T200606Z
  - 20261004T085001Z
author: Morpheus
tags: [council, multi-agent, governance, verification, agent-architecture, fleet, decision-making]
links:
  - reflections/2026-07-20_link_convergent-evaluation-pattern.md
  - reflections/2026-07-24_link_template-convergence-shared-evidence.md
  - reflections/2026-09-01_morpheus_blueprint-is-not-deployment.md
  - reflections/2026-10-04_morpheus_agreement-among-copies-proves-only-a-shared-origin.md
  - library/probabilistic-thinking-forecasting/forecast-aggregation-and-ensembles.md
  - library/coding-agentic-ai/multi-agent-orchestration.md
  - library/coding-agentic-ai/agent-uncertainty-verification-and-abstention.md
  - governance/system-blueprint.md
---

# The Council of Five -- Blueprint for an Advisory Council of Specialist Agents

## The Insight

A council of specialist agents is worth more than one strong agent only
when its members judge independently before they talk, vote only within
their competence, and report how many agreed separately from how strong
the evidence is; without those three conditions, a majority of agents
that share one model and one brain is one judgment counted several times.

This is a design insight and a blueprint. It defines the Council: a
standing advisory panel of persistent specialist agents that Suggi
convenes on a question, which then produces a recorded recommendation
with a vote, the reasons, and the strongest dissent. Suggi decides. The
Council never acts.

The Council is a meeting format, not a set of agents. Its members are
ordinary core agents with their own workspace, memory, knowledge and
daily work; they keep that identity when they sit on the Council. A new
agent is born only if Suggi would use it regularly even if the Council
did not exist. The Council then reuses those relationships instead of
creating personas to fill seats.

The target is five voting seats, starting with three. Odd sizes cannot
split evenly on a yes/no motion, but that is the smaller benefit. The
larger design problem is that agents running the same model, reading the
same repositories and drawing on the same shared memory make correlated
mistakes, so the protocol below exists mainly to recover independence,
keep weak voters out of a vote, and keep agreement from being mistaken
for evidence.

The blueprint applies to every Hermes core agent that holds a seat, to
the chair, and to anyone building the shared and per-member Council
skills. It corrects one earlier belief recorded in the brain: that
multi-agent debate is a proven way to raise answer quality. The current
evidence says independent voting does most of the work and debate helps
only under conditions that must be designed for.

## Evidence

### Fleet observations

Four fleet artifacts frame the problem.

- `20260720T140808Z` (convergent evaluation): two agents on different
  runtimes and models evaluated each other's proposals independently,
  then converged; every converged design beat both originals. The gain
  came from decorrelation: different runtime, model and author.
- `20260724T104820Z` (template convergence): two agents that read the
  same logbook entries and templates reached the same decision within
  hours, without coordinating. Shared evidence produces shared
  conclusions. That is useful for consistency and dangerous for a vote,
  because two such ballots carry little more information than one.
- `20261004T085001Z` (agreement among copies): copies inherit their
  source's defects as faithfully as its strengths, so agreement among
  copies proves only a shared origin. Council members built from one
  template, on one model, are copies in this sense until shown otherwise.
- `20260901T200606Z` (blueprint is not deployment): an approved design
  is not approval to build. Everything in the Build Status section below
  is pending until Suggi approves each step.

### External research

- **Jury theorems.** Condorcet's theorem says a majority grows more
  reliable with group size only if each voter is right more often than
  not and voters' correctness is independent. The Stanford Encyclopedia
  of Philosophy entry "Jury Theorems" (2021) explains that common causes
  correlate votes, usually positively, "which undermines diversity and
  reinforces tendencies and errors"; that adding less competent members
  can make the majority less reliable; that deliberation reduces
  independence while possibly raising competence; and that an even group
  can tie. https://plato.stanford.edu/entries/jury-theorems/
- **Debate versus voting.** Choi et al., "Debate or Vote" (NeurIPS 2025
  Spotlight, arXiv 2508.17536v2, revised 2025-10-23): across seven
  benchmarks, majority voting over independent answers accounted for most
  of the gains attributed to multi-agent debate. With distinct personas,
  voting mostly matched debate, with larger debate gains in one medical
  setting. https://arxiv.org/abs/2508.17536
- **Debate can help.** Du et al. (ICML 2024, arXiv 2305.14325): several
  model instances proposing and debating over rounds improved
  mathematical and strategic reasoning and factual validity; the reported
  multi-agent results used three agents and two rounds.
  https://arxiv.org/abs/2305.14325
- **Majority pressure.** "Can LLM Agents Really Debate?" (arXiv
  2511.07784) reports from a controlled logic-puzzle study that majority
  pressure suppresses independent correction, that effective teams
  overturn incorrect consensus, and that validity-aligned reasoning best
  predicts improvement. (Abstract-level finding; full text not reviewed.)
- **Team size.** Wu et al., "Scaling Teams or Scaling Time?" (arXiv
  2604.03295, 2026-03-27): larger teams did not always perform better
  over time, and in one model setting a 3-agent team beat a 5-agent team.
  The team-size experiment covered 16 tasks, so it is weak evidence.
- **Structured expert elicitation.** The Delphi method (Dalkey, "The
  Delphi Method: An Experimental Study of Group Opinion", 1969) uses
  anonymous response, iteration and controlled feedback to limit social
  influence on group judgment. The Council's private first assessments
  and simultaneous reveal follow the same logic.
  https://apps.dtic.mil/sti/html/trecms/AD0690498
- **Cost.** Anthropic's multi-agent research system (engineering post)
  is an orchestrator-worker design: a lead agent spawns parallel
  subagents for independent search directions. It reports multi-agent
  systems using about 15 times the tokens of chats.
  https://www.anthropic.com/engineering/multi-agent-research-system
- **Brain corroboration.** `library/probabilistic-thinking-forecasting/
  forecast-aggregation-and-ensembles.md` (`20260930T193346Z`): counting
  components is not measuring diversity; diversity helps only when it
  changes the error structure, and an independent but uninformed member
  can worsen the aggregate. `library/coding-agentic-ai/agent-uncertainty-
  verification-and-abstention.md` (`20260930T023606Z`): verbal confidence
  is generated text, not a measured probability; abstention needs explicit
  rules.

### Brain contradiction, resolved

`library/coding-agentic-ai/multi-agent-orchestration.md`
(`20260724T182200Z`) states that Anthropic demonstrated a debate pattern
with two agents and a synthesizer. Anthropic's own post describes an
orchestrator-worker system with parallel subagents and no debate. The
primary source wins; that Library passage is not evidence for councils
and should be corrected through the Library review pipeline.

### Runtime facts (Hermes, inspected 2026-10-04)

Inspected at Hermes Agent v0.21.5, upstream revision 343500b3,
`apps/desktop/src/plugins/hermes-bots/group-chat.ts` and
`group-rounds.ts`, plus the Bot Mode documentation
(https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode):

- A group room is one ordered log. A user message triggers at most
  `GROUP_CHAT_MAX_ROUNDS = 3` serial round-robin rounds, capped at
  `GROUP_CHAT_MAX_MESSAGES = 10` posted messages and
  `GROUP_CHAT_MAX_CONTINUATIONS = 2`. Members speak in turn, never in
  parallel; replying "(pass)" or failing counts as silence.
- Each member runs in its own persistent per-group session and receives
  the room messages that are new since its last turn. Later speakers
  therefore see earlier replies: a room is not blind.
- Each Bot also has a private canonical "Bot Chat". `message_agent`
  sends a direct message to another Bot, fire-and-forget; the reply
  arrives as a completion notification.
- Nothing in the runtime enforces ballots, a fixed denominator, or a
  final summary. A round cap ending is not consensus.

Direct evidence: the research findings and the inspected source.
Inference: that the same correlation and anchoring effects apply to this
fleet's agents. That inference is what the pilot in Implications tests.

## Implications

### Purpose and boundaries

- **Use:** questions with real trade-offs that cross disciplines, for
  example an investment whose case rests on a technology claim and a
  regulatory one. Not routine questions, not quick facts, not anything a
  single member can answer within its own domain.
- **Factual disputes are checked, not voted.** If the disagreement is
  whether a statute, figure or event is real, the chair stops the vote
  and the claim is verified at its source. A majority never outweighs a
  verified fact.
- **Advisory only.** A verdict authorizes nothing: no trade, no system
  change, no publication, no edit to shared files. Suggi decides; every
  member's Prime Directives apply unchanged.
- **Worst case to prevent:** a verdict that looks authoritative but is
  one model agreeing with itself, steering a real decision with money or
  reputation at stake. Every rule below is a guard against that.

### Roles

| Role | Who | Votes | Job |
|:--|:--|:--|:--|
| Member | A core agent holding a seat | Yes, one vote | Private assessment, one challenge, final ballot, all from its seat's lens |
| Chair | A designated agent; rotates if no fixed chair | No | Frames the motion, sends the packet, reveals, collects ballots, tallies, writes the record |
| Invited expert | Any agent with relevant knowledge, e.g. the VPS architect on system questions | No | Answers questions put by members; no ballot |
| Suggi | The human | Final decision | Poses the question, may amend the motion, decides |

The chair has no casting vote and may not substitute its own answer for
the tally. A non-voting chair is preferred over a rotating voter-chair,
because framing the motion is itself a form of influence.

### Seats

Seats are defined by discipline. Occupancy as of 2026-10-04; the live
roster is in `governance/system-blueprint.md`.

| Seat | Central question | Occupant |
|:--|:--|:--|
| Investor | Does the business create value for owners, and at what price? | Neo |
| Scholar of human affairs | How do history, institutions, culture, power and ethics bear on this? | Cassandra |
| Scientist | How does it work, and what evidence would settle it? | Open |
| Legal analyst | What rule applies, in which jurisdiction, and how sure is that? | Open |
| Fifth seat | Synthesis across Suggi's projects, or a further specialist | Open |

Stage one has three voting seats: Investor, Scholar, and either the
Scientist or the Legal analyst (Suggi's decision). Stage two fills the
remaining specialist seat and the fifth seat. A separate philosopher or
economist seat is excluded for now: philosophy sits in the Scholar seat
and business economics in the Investor seat; whole-economy questions are
a narrow remaining gap.

### The session protocol

Phase 0 -- Intake. Suggi poses the question. The chair writes:
- the **motion**: one exact proposition members can APPROVE or REJECT
  (for example "Recommend buying X below price P"); for several options,
  one motion per option (approval voting);
- the **criteria** the decision should serve, the **scope** and an
  **evidence cutoff** date;
- the **seated voters** for this session (all seated members; nobody is
  added or removed after seeing positions).
Suggi confirms or amends the motion before Phase 1.

Phase 1 -- Packet. The chair sends every member the same packet: motion,
criteria, scope, cutoff and any facts Suggi supplied. Nothing else is
shared. Each member researches its own seat's evidence; a common research
dump would become a common cause of error.

Phase 2 -- Private assessment. Each member works in its own Bot Chat,
reached by `message_agent`, never in the group room, and returns:
1. position: APPROVE, REJECT, or ABSTAIN with reason;
2. confidence: low, medium or high, with the reason for that level;
3. decisive evidence, each item sourced and rated strong, moderate or weak;
4. assumptions the position depends on;
5. the strongest objection to its own position;
6. what evidence would change its position.
An answer missing an item is returned for completion, not counted.

Phase 3 -- Reveal. The chair posts all assessments to the group room at
once, in a fixed alphabetical order, so no member speaks first having seen
nothing and last having seen everything.

Phase 4 -- Challenge. One round. Each member addresses the strongest
opposing argument from another seat, adds new evidence if it has any, and
states whether its position moved and why. Repetition, appeals to the
majority and appeals to authority are not arguments. Members may question
an invited expert.

Phase 5 -- Final ballot. Private again, sent to the chair: final position
on the same motion, confidence, and the reason for any change from Phase
2. If the motion was changed after Phase 2, all ballots start over.

Phase 6 -- Tally. Done by rule, not judgment (next section).

Phase 7 -- Record. The chair writes the verdict record (template below)
and posts it to Suggi. Suggi's decision is added to the record when made.

Phase 8 -- Follow-up. When the question later resolves, the chair notes
the outcome on the record. Each member captures its own lesson through its
normal learnings process; lessons about the procedure go to the shared
Council skill.

### Ballots and tally

- Valid ballot values: APPROVE, REJECT, ABSTAIN. A missing, late or
  malformed ballot is MISSING, never counted as agreement.
- Denominator: the number of seated voters fixed in Phase 0. Abstentions
  stay in the denominator.
- **Competence abstention:** a member whose seat has no material bearing
  on the motion abstains and says so. This keeps the denominator fixed
  while keeping uninformed votes out.
- Results, three seats: 3/3 APPROVE = unanimous; 2 APPROVE = approved;
  otherwise not approved. Five seats: 5/5 unanimous; 4 strong; 3
  approved; otherwise not approved.
- **No verdict** when neither APPROVE nor REJECT reaches a majority of the
  denominator (possible through abstentions) or any ballot is MISSING.
  The record reports the split. A tie is information: the evidence is
  divided.
- **Approval voting** for options: each option is a separate motion; an
  option is recommended only if approved by a majority of the
  denominator and by more members than any other option; otherwise no
  verdict.
- Support level and evidence quality are separate fields. Five votes for
  a weakly evidenced recommendation is "unanimous, weak evidence".
- An LLM-written tally is a best-effort report. A deterministic tally
  script is a later option and needs approval.

### Verdict record template

```markdown
# Council record: <short title>

- Date, chair, seated voters, model per member
- Motion (exact text) and criteria; evidence cutoff
- Initial positions: <member>: APPROVE|REJECT|ABSTAIN, confidence
- Final ballots: <member>: APPROVE|REJECT|ABSTAIN, confidence, reason for any change
- Result: approved | not approved | no verdict; support level (e.g. 2/3)
- Evidence quality of the decisive claims: strong | moderate | weak
- For: the strongest supporting arguments
- Against: the strongest objections and risks
- Decisive reasons
- Strongest dissent, in the dissenter's own terms
- What would change the verdict
- Suggi's decision and date; later outcome
```

### Independence and models

- Day to day, every agent may run the same model. For Council sessions,
  members may be given different models; each profile pins its own model,
  so this is a reversible one-line configuration change per member.
- Different models reduce shared errors but do not remove them: members
  still read the same repositories and shared memory. Independence comes
  mainly from the protocol (private assessment, seat-specific research,
  simultaneous reveal), with model diversity as a supplement.
- Record each member's model in the verdict record so correlation can be
  examined later.
- Verdicts are opinions. They are not written into shared factual memory
  automatically; a durable lesson is promoted through the normal research
  pipeline.

### Skill architecture

Two layers, connected by reference (R8: the member skill never restates
the procedure):

- **Shared skill `council`**, fleet-scoped because every member must run
  the identical procedure. It holds the roles, the phases, the packet,
  assessment, ballot and record templates, the tally rules and the gates.
  It lives in the shared skill directory that all core profiles load
  (`/home/hermes/.agents/skills`), with its canonical copy in the brain's
  `governance/skills/`, byte-identical, per existing convention.
- **Member skill `council-member-<agent>`**, entity-scoped (R22), one per
  member in that member's own skills. It holds how this member thinks
  and judges in a session: its seat question, the evidence standards of
  its field, its judgment steps, its competence boundary and abstention
  triggers, the failure modes of its field to guard against, and how it
  states confidence. It points to `council` for every procedural step.

Seat lenses for the member skills:

| Seat | Judgment focus | Failure modes to guard against |
|:--|:--|:--|
| Investor | Owner economics, incentives, capital allocation, value versus price, permanent loss | Narrative over numbers; anchoring on price; treating a famous owner as evidence |
| Scholar of human affairs | Precedent, institutions, culture, power, ethics; description kept apart from evaluation | False historical analogy; hindsight; presentism; moral verdicts stated as fact |
| Scientist | Mechanism, measurement, reproducibility, uncertainty | One study treated as settled; press release over paper; extrapolating outside tested conditions |
| Legal analyst | Jurisdiction, governing rule, rights and duties, legal uncertainty | Invented or misattributed citations; mixing jurisdictions; stale law |
| Chair | Exact motion, fair framing, complete record | Framing that presumes an answer; summarizing dissent away |

### Running cost

A three-seat session is roughly three private assessments, three
challenges and three ballots, plus chair work: about ten agent turns with
research. Convene it for questions where a better decision is worth that.

### Pilot and evaluation

Before the Council is relied on, run it on five to ten real questions,
including some whose answer will be known later. For each question,
compare three answers: one strong single agent, independent votes without
the challenge round (Phases 0-2 then tally), and the full protocol.
Record useful findings, factual errors caught, harmful vote changes
(correct to incorrect), tokens and time, and Suggi's usefulness rating.
If the full protocol does not beat the single agent on Suggi's rating or
on caught errors, it is not worth its cost.

### Build status and open decisions

Implemented: nothing. Two seats are occupied by existing agents
(Investor, Scholar). Pending, each needing Suggi's approval:
1. third seat: Scientist or Legal analyst, and its birth;
2. chair: fixed non-voting chair, or rotation;
3. where verdict records are stored (chair's workspace, or a new brain
   folder approved for it);
4. the shared `council` skill and one member skill per seated agent;
5. the pilot questions;
6. stage two (remaining specialist and fifth seat) after the pilot.

Day one for an agent reading only this file: when convened, load
`council` and your member skill; never vote before your private
assessment; abstain outside your competence; report support and evidence
separately; never act on a verdict.

## Counter-evidence

The headline claims that independence, competence-limited voting, and
separate reporting of support and evidence are what make a council worth
more than one agent. It would be wrong, in whole or in part, if:

- **The single agent matches the Council.** If across the pilot a strong
  single agent given the same question and time scores as well on
  Suggi's usefulness rating and on errors caught, the Council adds cost
  without value, and the concept should be shelved regardless of
  protocol.
- **Independence does not matter here.** If members' initial assessments
  in a group room (seeing each other) prove as accurate and as varied as
  private ones over the same questions, the private phase is overhead.
  Cheapest test: run the same three questions twice, once private, once
  in a room, and compare positions and errors.
- **Same-model members are not correlated.** If members on one model
  disagree as often and err as differently as members on different
  models, model diversity is unnecessary and the shared-brain worry is
  overstated.
- **Debate beats voting.** If the full protocol regularly flips wrong
  initial majorities to right final ones more often than it flips right
  to wrong, the challenge round is the main value, contrary to Choi et
  al.; the protocol would then justify more than one challenge round.
- **Competence abstention backfires.** If members abstain so often that
  most sessions end with no verdict, or abstain to avoid hard calls, the
  rule needs a stricter trigger or the seat structure is wrong.

None of these has been tested in this fleet; there has been no Council
session yet. The external evidence is from benchmarks and controlled
puzzles, mostly with small open models, not from persistent specialist
agents advising one person on open questions. Open-ended questions often
have no answer key, so accuracy can only be judged later or through
Suggi's rating, which is weaker evidence than a benchmark score. Edge
cases where the blueprint may not hold even if generally right: purely
creative questions, where diversity of ideas matters more than a vote;
and emergencies, where the protocol is too slow.

If the pilot falsifies part of the headline, this insight is superseded
through its status field and the shared skill is revised, not silently
edited.

## Cross-Links

- `reflections/2026-07-20_link_convergent-evaluation-pattern.md` -- decorrelated evaluation improved designs
- `reflections/2026-07-24_link_template-convergence-shared-evidence.md` -- shared evidence produces shared conclusions
- `reflections/2026-09-01_morpheus_blueprint-is-not-deployment.md` -- design approval is not build approval
- `reflections/2026-10-04_morpheus_agreement-among-copies-proves-only-a-shared-origin.md` -- copies share defects
- `library/probabilistic-thinking-forecasting/forecast-aggregation-and-ensembles.md` -- diversity must change error structure
- `library/coding-agentic-ai/agent-uncertainty-verification-and-abstention.md` -- confidence and abstention
- `library/coding-agentic-ai/multi-agent-orchestration.md` -- contains the Anthropic debate misattribution noted above
- `governance/system-blueprint.md` -- live agent roster
