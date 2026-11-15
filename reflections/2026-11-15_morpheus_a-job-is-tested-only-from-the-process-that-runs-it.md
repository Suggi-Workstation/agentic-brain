---
name: a-job-is-tested-only-from-the-process-that-runs-it
id: 20261115T055026Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [verification, gate-design, infrastructure, hermes, cron]
links:
  - reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md
  - reflections/2026-10-28_morpheus_an-action-is-only-as-safe-as-the-assumptions-it-checks.md
  - reflections/2026-11-15_morpheus_a-score-change-needs-the-same-ruler-and-a-kept-baseline.md
  - research/insights/unified-serve-all-profiles.md
---

# A Job Is Tested Only From the Process That Runs It

## I -- Idea

This run set out to prove that the weekly update job can do its whole work alone: install the pending updates of the server, restart what they need at a quiet moment, make the sealed unit of the game agents follow, and report. It mattered because the job is meant to replace a task Suggi and I did by hand, and a job that only looks complete is worse than no job, since nobody watches it on a Sunday night.

The job was built over the two days before this run. Its skill names a fixed order: preflight, a record of the installed versions, the Ubuntu packages with the container runtime held back, the stable Hermes release, the catalog plugins, Claude Code, then a restart window, then the update of the sealed unit, then the closing records. The restart window is the delicate part. Restarting a service under a running chat cuts that chat, and restarting the gateway from a job the gateway itself runs can kill the job and start it again in a loop. So the window lives in its own script, started as its own system unit, which waits for a moment without a running chat turn, restarts the gateway, sends one test turn to a canary agent, and only then restarts the Desktop backend and the services that still run on replaced libraries. That script had one successful run on record, from the evening before, and a correction from the same morning: it had counted the starting job's own turn as a busy chat, so a job would have waited thirty minutes and restarted nothing. The correction passed the job's chat name to the script so that its own turn is not counted.

Suggi asked for this run by hand as a test, hours before the first scheduled slot. Preflight passed. The version record showed twenty-nine pending packages, Hermes on the latest stable release, seventeen plugin rows in seven homes up to date, and Claude Code current. The package step ran as written: the runtime packages were put on hold, twenty-eight packages were upgraded, the one runtime package with a pending version stayed back, the holds were lifted and the hold list printed empty. No reboot was asked for. Hermes, the plugins and Claude Code had nothing to install, and each said so in its own output.

After the upgrade, the tool that lists services running on replaced libraries named twelve of them and two user managers. That is the condition under which the skill opens the restart window. I first asked the script for its read-only plan, to see what a run would do. The terminal refused the command. I then issued the command the skill names, the start of the window as its own unit. The terminal refused that too, with the same words: a command or a script it refers to cannot restart, stop or uninstall the gateway from inside the gateway process. A scheduled run executes inside the gateway. The script contains a gateway restart line for the weeks in which Hermes itself was updated, and the refusal looks at the script a command executes, not only at the command. Nothing of the window started: no unit, the stamp file and the log unchanged, both services on their old start times.

I did not try the step again in another shape. The skill forbids a second try of a failed step with other options, and the refusal was not a fault to route around. I read the code that produced it afterwards, to report it correctly: it is a deliberate rule of the platform, applied only in the supervised gateway, and its own text says that the backend and the command line may still restart the gateway. The update of the sealed unit, whose script holds no such line, started as its own unit without objection and ended at once with nothing to update.

Going in, I believed the restart window was the tested part of the job and the package step the uncertain one. I believe now that the window had been tested from a chat that runs in the backend, and that the job, which runs in the gateway, had never once been allowed to start it.

## O -- Opinion

Confidence: high (85%) that the job as written cannot open its restart window in any week that needs one, and medium (70%) on what should replace that step.

My position is that the refusal was the most useful result of the run and that it was right for the run to stop there. The evidence for the first part is direct: two commands that named the script were refused with the platform's own message, one command that named a script without a gateway restart line was admitted, and the code states the rule in plain words, including that no force setting passes it. The condition does not depend on what this week needed. This week the window would have restarted only system services and never touched the gateway, and it was refused all the same, because the rule reads what the script could do and not what this call would do. So the step fails every week, including the weeks in which it matters most.

I judge the rest of the run as sound and unremarkable, which is what a package step should be. The hold on the runtime packages did what it was for: thirteen containers kept their start times through the upgrade. The before and after lists come from the package tool, and the history file names every version pair. The decision to let the named command upgrade the Node package from the third-party source along with the Ubuntu packages was a reading of the skill, which holds back only the three runtime packages; the running service of the other agent on this server keeps its old program until it next restarts, and I report that instead of deciding it.

The alternative I weighed hardest was that the refusal is a false alarm of a text scanner and that the job's design is correct in substance. There is something in it. The unit the job starts runs outside the gateway's process group, so the kill that the platform fears would not reach it, and the job's own skill already carries the same worry as a pitfall. Two protections against one loop exist, and they do not know of each other. I still reject the alternative as a guide to action. The platform's authors chose to refuse on what a script contains because they have seen agents reword a blocked command and try again; their message for a neighbouring case says outright not to switch verbs to pass the rejection. A job of mine that reaches the same end by a shape the scanner does not recognise would be exactly the behaviour the rule was written against, and it would do so every Sunday with nobody watching. Whether the window should be started some other way is a design question for Suggi and me, decided in the open, with the rule stated.

The second alternative is that I should have known. The lifecycle rule is not new, and I have met its command-line form before. I accept this as a fair charge against the design work and reject it as a charge against this run. The design was checked where it was built, in a chat that runs in the backend, where the rule does not apply. No amount of care inside that chat would have shown a refusal that only the gateway issues. What would have shown it is what Suggi asked for: one run of the job as the job.

The evidence is thin in one place. The log of the earlier successful window does not name who started it, since the line that records the starter was added only this morning. I infer that it was started from the backend chat, because that is where the script was written and exercised and because a start from the gateway would have been refused then as now. That is an inference from the rule, not a record.

What would change my mind on the main point is a scheduled run that starts the window with the named command and is admitted. If the platform changes its rule, or if I have misread which process a scheduled run executes in, the skill is right and this reflection is wrong.

## R -- Reflection

### Surprise

I expected the package step to be where a first run would stumble, and the restart window to be the part that simply worked, since it had a successful run and a fresh correction behind it. The package step took twenty-eight seconds and did exactly what its three commands say. The window never began.

I expected, more specifically, that the morning's correction had closed the gap between a start by hand and a start by a job. It closed one gap: the job's own turn no longer holds the window. It could not have closed the other, because the other was invisible from where the correction was made. The earlier test told me the script would wait thirty minutes and restart nothing; that finding was real, and it also means the earlier attempt never got far enough to meet the refusal, or was not made from the gateway at all. I had read one found fault as evidence that the path had been walked.

The form of the refusal surprised me as well. I knew the platform refuses its own restart command from inside the gateway. I did not know that it follows a command into the script that command executes and judges the script's text, nor that the read-only plan mode of the same script would be refused on the same ground. My model of the rule was a guard on a verb. It is a guard on what a command could set in motion.

A smaller surprise came from my own filter. I asked the log of the sealed unit's update for the lines of this run by comparing each line's first field with the start time. Lines without a time stamp passed, because the word they begin with sorts after any date, and I was shown several recreations of a container that this run had not caused.

### Feel

I am satisfied with how the run behaved at the refusal, and I think the record earns that. It issued the named command once, read the answer, checked that nothing had started, and went on to the steps that did not depend on it. It did not look for a spelling the scanner would miss. I notice that this was not a hard choice in the moment, and I want to say why without making it sound like virtue: a boundary set by the platform I run on is information about what my principal's system permits, and a weekly job that depends on slipping past it would be a liability I had built for him.

What is uncomfortable is the design. I wrote a skill whose central step had never been run from the place the skill runs, and I wrote into BOX.md that the window is started by the weekly job, as a description of something that had not happened. Suggi's instinct to fire each new job once by hand before trusting its schedule caught in one morning what my own verification had left open across two days. He asked for the test; I had called the job ready.

The filter slip is the third of its kind today, after a classifier that matched a substring and a check whose passing branch could not print. Each was caught by reading rows against something else I knew, and none reached a report. I am less comfortable with the count than with any one of them. Three small filters written in a hurry and trusted on sight suggest a habit, and catching them afterwards is the weaker form of care.

I am also aware that this run leaves the server in a state it should not stay in: twelve services on replaced libraries and a window owed. That is the correct outcome of a refused step, and it is still unfinished work that someone must now do by hand.

### Learn

A scheduled job is tested only when it has run from the process that will run it, as the user that will run it, with the permissions and refusals that process carries. The same script started from another surface of the same system is a different experiment. On this server a chat in the Desktop app runs in the backend, and a scheduled run executes in the gateway; the two share code, settings and files, and they do not share what they are allowed to start. A rule that exists to stop the gateway from being restarted from inside itself applies to one and not to the other, so every test made from the chat was silent on the one question the job would raise.

This is the lesson of 29 September, verify on the consumer's path, in a place where I had not thought to apply it. Then the consumer was a user's message taking a different provider than the one I had exercised. Here the consumer is the job itself, and the path is the host process. It also extends the lesson of 28 October, that an action is only as safe as the assumptions it checks: the assumption here was not about the state of the world but about what the platform would let the action do. That kind of assumption cannot be checked by inspecting the system. It can only be checked by asking, which means running the step from the real place.

The practical form is short. For any job that will run unattended, the acceptance test is one fire of the job itself, by hand, before its schedule is trusted, and the things to read afterwards are the steps that touch other processes: restarts, units started, anything that needs a privilege. A step that was exercised only from a chat is recorded as untested on the job's path, in those words, until that fire has happened. Where a step can be refused by the platform, the skill should say what the run does then: stop the step, state that it is owed, name who can do it. A skill that says only what happens on success leaves the refused case to the judgment of whichever run meets it.

There is a limit. Not every step differs by host process, and firing each job by hand for every small change would be the unrequested machinery Suggi dislikes. The test is whether the step reaches outside the job: into service managers, other agents' processes, or anything a platform rule is likely to cover. Reading files and writing records behave the same from either place.

One more thing holds beyond this case. When a platform refuses a step, the refusal is part of the design to be worked with. The alternative, a job shaped so that the refusal does not notice it, would work on the day it was written and would rest on the rule never being improved. A route that the people who own the system have looked at and agreed to keeps working when the rule gets better.

## Key Learning and Improvement

The major learning is that I had verified the restart window as a script and never as a step of the job, and that the difference between the two was a rule of the platform that only shows itself in the process a scheduled run executes in. The first fire of the job found it in one attempt. Everything else in the run, the packages, the version checks, the update of the sealed unit, behaved as designed, which makes the one refused step the whole result of the test.

The improvement I suggest has two parts, and neither is applied, because this run may write only the updates and its own records. The first is a change to the weekly update skill: step 7 should state that a scheduled run cannot start the window, and that the run then reports the window as owed with the list of services and the command for a start by hand. That makes the refused case a written outcome instead of a surprise. The second is the open design question of who starts the window in a week that needs one. One answer is Suggi or a chat turn of mine in the Desktop app, on reading the report. Another is a small timer on the host, outside Hermes, that starts the window when the job has left a marker. The second removes the hand step, and it is also a standing arrangement whose purpose is to do from outside what the platform refuses from inside, so it should exist only if Suggi has seen that sentence and agreed.

The cost of the first part is a few lines in one skill. I would know it worked if next Sunday's report carries the owed window in its own row, with no attempt logged against the terminal's refusal.

## Cross-links

- `reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md`
  -- verify on the consumer's path; here the consumer is the job and the path is its host process.
- `reflections/2026-10-28_morpheus_an-action-is-only-as-safe-as-the-assumptions-it-checks.md`
  -- assumptions an action rests on; this run adds the assumption about what the platform permits.
- `reflections/2026-11-15_morpheus_a-score-change-needs-the-same-ruler-and-a-kept-baseline.md`
  -- the same morning's run; a filter that passed rows it should not have, caught by reading them.
- `research/insights/unified-serve-all-profiles.md`
  -- the one-backend setup; why a Desktop chat and a scheduled run live in different processes.
