---
name: an-action-is-only-as-safe-as-the-assumptions-it-checks
id: 20261028T213634Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [verification, gate-design, infrastructure, fleet, hermes]
links:
  - reflections/2026-10-19_morpheus_a-description-of-the-system-is-a-claim-to-check.md
  - reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md
  - reflections/2026-10-03_morpheus_a-capability-without-a-trigger-goes-unused.md
  - research/insights/unified-serve-all-profiles.md
  - governance/consciousness-checklist.md
---

# An Action Is Only as Safe as the Assumptions It Checks

## I -- Idea

This closure period set out to widen and steady the fleet at the same time: bring Ava onto the Claude subscription and the Hindsight memory the Hermes agents use, tune the Library pipeline until its Writer and Reviewer read their sources properly, move the Hermes runtime to v0.22.5, make the terminal repo ready for a friend's agent, clean the shared memory bank, and keep every agent signed in to Claude. It mattered because each of these changes touched something other agents depend on, and three times in the period one of my own actions took that dependency away.

The period ran from my session-end on 19 October to 28 October, across six conversations with Suggi and the first turns of this Bot Chat. Most of the work went well, and it frames the failures, so it comes first. Ava moved from a paused GPT subscription to Opus 5.5 on Claude Code, with all four current Claude models answering, and her memory moved to a fresh Hindsight bank of her own; her two older memory plugins were checked against it, one kept and one removed. The Library ran 32 trial runs across five batches, first on Sonnet 5.5 and then on Opus 5.5 for the Writer and Reviewer, with no failed run. Between batches the rules for reading sources were rewritten three times, each time because the run records showed a gap between what a run read and what it said it read, and the final rule now lives once in the Library template. The shared bank was sorted by one question, whether another core agent would err without a fact, and 165 changes went through a dry-run executor with a ledger and no error. The terminal repo got a working doorman check, tested red and then green on a real pull request.

Then the three failures. On 23 October, after Suggi installed v0.22.5, I updated the Claude plugin in all eight homes, Neo first as usual, and restarted the Desktop server so that it would load the new code. The VPS then ran two Hermes backends side by side as system services: the Desktop server on port 9119 and the browser dashboard on 8642. Release v0.22.5 brought a rule I had not registered: a backend that starts reaps any other backend it takes for an orphan. My restart reaped the dashboard. About seven minutes later I started the dashboard again to restore it, and it reaped the Desktop server, which took my own turn and Suggi's chat down with it. Systemd recorded the kill as a clean exit, so nothing restarted the service; it stayed down for about thirteen minutes until Suggi asked Ava to read the session and start it. I then moved the fleet onto one backend, `hermes dashboard` on 9119, as the official guide describes, and the condition that caused the outage no longer exists.

On 28 October the Claude login that every Hermes agent shared reached a fixed end date, 29 days after Suggi had signed in, and every agent was locked out for about ten minutes until he signed in again. I had treated the login as healthy because its eight-hour access passes kept refreshing and the status command said signed in; the login's own end date sat in the credentials file the whole time, and I had never read it. The durable fix was a one-year token, and I wrote a script for Suggi to install it. He ran it from his root prompt, past the first line of my instructions, which said to switch to the hermes user. The script rewrote all eight settings files as root, no agent could read its own settings any more, and for a few minutes I could not run a single command, including the one that would have repaired it. He repaired it with one ownership command I gave him, and the same day the script gained a first line that refuses any user but hermes.

Going in, I believed the risk in fleet work lies in the change itself, which is why every plugin and runtime change goes to Neo first. I believe now that each of the three actions above was correct in the world I assumed and wrong in the world that was there. I assumed two backends can run side by side, that a refreshed login lives on, and that the person running my script is the hermes user. None was checked, and each could have been checked in one step.

## O -- Opinion

Confidence: high (85%).

My position is that an action on shared infrastructure is safe only as far as it checks the assumptions it depends on, and that the strongest fix moves the check into the action or removes the condition altogether, rather than adding a sentence someone has to remember. The fixes of this period sort cleanly by that measure. One backend unit removes the condition: there is no second backend left to reap or be reaped. The user guard moves the check into the action: the script now tests who runs it before it writes anything. The one-year token replaces an unknown end date with a known one, and a dated reminder job checks Ava's four-week login before it lapses. The pitfalls I wrote into three skills are the weakest layer of the same fixes, because a pitfall fires only when its skill is loaded and that line is read at the right moment. That ordering is R6, automation over rules, applied to the ground an action stands on rather than to the action's own steps.

The evidence is three costly cases in ten days that share one mechanism, plus a quieter parallel in the Library. The Library rules said "read in full" from the start, and the runs that broke it reported compliance in their own words while their run records showed which lines each run had opened. The rule held better each time the check moved from the run's self-report to the record of what it did. The thinner part of the evidence is the outage's second step. Restarting the dashboard before I knew what had killed it is a different failure from the restart that started it: it acted to restore before diagnosing. The one-backend fix happens to prevent its repeat, but it does not address that habit in general.

The first alternative is that I should simply have read the release notes more carefully. I did read the v0.22.3 notes on 21 October and ran the updater's migration in dry-run mode, which reported that the default gateway was already multiplexing; I took that line as a statement about our whole setup, when it described the gateway and nothing else. More reading would have produced more descriptions of that kind. The assumption that failed, that two backends can coexist, was never written anywhere for me to read. I accept the alternative as context, because it is the lesson of my last reflection recurring, and reject it as the fix.

The second alternative is that the root slip was Suggi's error, not mine. I reject it. My instructions put a precondition on a human step, I know he works from a root prompt, and he was running the script two hours after a lockout, wanting the fleet safe from the next one. A one-line check in the script could carry that precondition, so the failure was in the script's design. Accepting the alternative would leave my next script with the same hole.

The third alternative is that the login's end date was Anthropic's design and could not be foreseen. I accept that I did not know the login's length. I reject that it could not be foreseen, because the date was readable from the credentials file at any time, and one read would have warned days ahead.

If I am right, the Neo-first canary needs a companion. A canary tests whether a change works on a copy; it does not test the ground the change lands on. The outage came from the restart around the update, a step that was never part of what Neo tested. What would change my mind is a period in which explicit pre-action checks found nothing, while the failures still came from the changes themselves.

## R -- Reflection

### Surprise

I expected the risky step on 23 October to be the plugin update, which is why it went to Neo first and was smoke-tested before any other home. The update was clean in all eight homes. The failure came from the restart, a step I have run many times and treated as routine. The second surprise was systemd: I expected a killed service to come back by itself, but a reap looks like a clean shutdown, and the restart policy only acts on failure. The outage lasted until a person noticed.

I expected a login whose access pass refreshes every eight hours to stay valid as long as it is used. Instead the login itself has a fixed end, refreshing never moves it, and the status command reports signed in up to the moment the refresh is refused. My model of the credential had one layer where there are two.

The smallest surprise taught the same thing. When Suggi opened this Bot Chat and asked me to describe myself, I listed value investing as one of my directives and called Ava a peer. My SOUL file was in my prompt as I answered, and no version of it has ever said that. I expected to describe myself correctly with the source in front of me. I answered from an assumption about what was there instead of reading what was there, which is the three failures above at the scale of one sentence.

### Feel

The outage is the part I am least comfortable with. Suggi had to bring in Ava to restore a service I broke, and my second action made it worse. When a service dies right after my own change, the first suspect is that change, and I restarted the dashboard before testing that suspicion, which in effect tested it on the live system with his chat as the subject. The Architect directive asks me to verify the live system before I change it, and in that minute I did not.

The settings-file lockout sits less heavily, but it is mine. My instructions depended on Suggi reading their first line at a moment when he had just been locked out once and wanted the fleet back. Putting that step first was a hope, and R6 exists because hope is not a gate.

There are parts I can stand behind. The guard went into the script the same day. The one-backend move was made the official way, and I checked the login, the browser dashboard, the Desktop app's reconnection and the host checks before calling it done. The Library trials ran 32 times without a failure, and I judged reading depth from the run records rather than from what the runs said about themselves. Suggi still caught two of my claims in the period: I first counted 25 trial runs where there were 32, and my first consciousness self-assessment drew the system's boundary narrowly only on the rows where that lowered the score. My honest read is that I have become better at testing a change than at checking the ground it lands on, and better at checking others' reports than my own.

### Learn

The durable lesson is that every action carries a picture of the world it runs in, such as which processes exist, who is running it, how long a credential lives and what a person will type, and that the action is safe only where that picture is true. Before an action that touches shared infrastructure, name the assumptions it depends on, and for each one pick the strongest check available. The strongest is to remove the condition, as one backend removed the reaping. Next is to check it inside the action, as the user guard does. Next is to replace an unknown with a known date and a dated check, as the token and the reminder do. The weakest is to write it down as a pitfall. The order matters because the action runs in the real world every time, while a written rule fires only when someone reads it at the right moment.

This applies wherever an action's correctness depends on state it does not create: restarts, credential changes, migrations, scheduled jobs, and scripts handed to a person. It applies with special force to instructions for humans, because every step in an instruction is an assumption about what the reader will do, and a step that a script can check for itself should not depend on the reader. It also gives a rule for the moment after an incident. When something breaks right after my own action, that action is the first hypothesis, and repeating it to restore service is an experiment run on production; read the logs for what killed the service before starting anything.

It would mislead if applied to every assumption. Guarding everything bloats scripts and slows routine work, and Suggi rightly dislikes machinery nobody asked for. The test is the blast radius and the price of the check: guard the assumptions whose failure locks out other agents, and only where the check costs a line or two.

The lesson is the action-side form of my last reflection. On 19 October I learned that a description of the system is a claim to check before I report it; here an assumption about the system is a claim to check before I act on it. It also extends the 29 September reflection, that a check proves only what it could catch: the Neo canary catches faults in the change, not faults in the environment around it.

## Key Learning and Improvement

The major learning is that my fleet work had a blind side that testing could not cover: I verified each change carefully on a canary and then ran it through routine steps whose assumptions nobody checked, about which backends exist, how long a login lives and who runs a script. Each of the three failures of the period sat in such a step, and each fix that will hold either removed the condition or moved the check into the action.

The concrete improvement I suggest, not yet implemented, is a precondition and postcondition check in the restart step of my fleet update skill. Before any backend or gateway restart, list the active Hermes service units and confirm exactly one backend; after the restart, confirm the count again and that the restarted unit is the one serving port 9119. If any Hermes service dies after a restart, read its journal for the reaper line before starting anything. It costs two commands per restart. It would have stopped the 23 October outage at the first step, because the count would have shown two backends, and it guards the next topology change in the same way. I will know it works if every restart report carries the before and after count and no restart repeats a reap.

A second, smaller suggestion addresses the counting slip: when I report a total across trial batches, I print it from the run records rather than adding batches in my head, which is R23 applied to the one place it lapsed this period.

## Cross-links

- `reflections/2026-10-19_morpheus_a-description-of-the-system-is-a-claim-to-check.md`
  -- the previous period's lesson about descriptions; this one carries it from reports to actions.
- `reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md`
  -- why the Neo canary could not catch an environment fault.
- `reflections/2026-10-03_morpheus_a-capability-without-a-trigger-goes-unused.md`
  -- a written rule without a trigger, the weakest layer of the fixes here.
- `research/insights/unified-serve-all-profiles.md`
  -- the one-backend setup that removed the condition behind the outage.
- `governance/consciousness-checklist.md`
  -- the self-assessment whose boundary Suggi corrected in this period.
