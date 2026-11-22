---
name: a-rule-must-test-its-reason-not-the-case-it-came-from
id: 20261122T232210Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [infrastructure, verification, gate-design, cron]
links:
  - reflections/2026-11-16_morpheus_a-restart-list-names-the-unit-not-the-stale-process.md
  - reflections/2026-11-22_morpheus_a-fix-for-one-scanner-leaves-the-class-open-in-the-next.md
  - reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md
---

# A Rule Must Test Its Reason, Not the Case It Came From

## I -- Idea

This run set out to do the second scheduled weekly update of the server and, in a week where real packages were pending, to decide from evidence which services the restart window owes. The decision matters because the window is the one step of the job that touches other agents: it waits for a quiet moment and then restarts services under the fleet, and it is started by hand from my Bot Chat on the strength of one line in this report. Last week's run taught me that the list a restart tool prints names units, while what is stale is a process, and the skill was changed after that run so that a listed unit whose main process maps no replaced file does not make the window owed. Tonight was the first night that rule met a list long enough to test it.

The job is mine and its order is fixed by the weekly update skill: preflight under the rules for scheduled runs, a record of the installed versions, the Ubuntu packages with the container runtime held back, the stable Hermes release, the catalog plugins of every home, Claude Code, the restart window, the sealed unit of the game agents, leftover Docker volumes, then the closing records. The record before the updates showed twenty-five upgradable packages: a systemd point release with its libraries and udev, a mesa point release, an ALSA configuration package, kernel headers and tools, and the three kernel metapackages that would pull in a new kernel. Hermes was on v0.23.3, the newest stable release, published on 20 November; every newer entry on the release page was a canary build. Seventeen plugin rows across seven homes were up to date. Claude Code was on 2.1.325.

The package step ran with the commands the skill names: hold containerd, docker.io and runc, upgrade with suspended restarts and kept configuration files, release the hold. Twenty-two packages were upgraded; the three kernel metapackages were kept back because they need new packages, which the plain upgrade never installs, so the new kernel waits as a report row for Suggi. The hold list was empty afterwards and no reboot flag was written. The Claude Code script then moved the CLI from 2.1.325 to 2.1.330, ran one real turn on Neo and kept the new build because the turn answered. Nothing in Hermes or the plugins was installed, so the sealed unit was eligible to follow the fleet tonight; its update script found one change, the Claude Code build, and began to wait for a moment without a running turn in the unit. It waited the full thirty minutes, found the Admirals' turns overlapping the whole time, and ended with `held` and nothing changed; the decision whether to go under open turns is Suggi's. The leftover-volume step removed eight small unnamed volumes, each copied to the Trash first.

The restart tool listed fifteen services under "Services to be restarted". I read every listed unit's main process for mappings of deleted files, as the rule asks. Twelve main processes mapped the old systemd or udev library and were owed without question. Three gave the rule nothing to count: containerd and ossec, whose main processes map no deleted file, and postfix, a forking unit for which systemd tracks no main process at all. Containerd is last week's case exactly. Its daemon was last started on 21 November, after its own upgrade on the 15th; seven container shims in its control group still run the shim binary that upgrade replaced, and the unit's kill mode is `process`, which leaves them running across any restart of the unit. The rule's verdict, not owed, is right for it.

Ossec looked the same through the rule and was not the same. Its main process is a small bash supervisor that keeps the detector's five daemons alive; it maps no deleted file. One of its children, the log collector, maps the old libsystemd. The unit's kill mode is `control-group`, so a restart of the unit stops every process in its group, the log collector included, and the supervisor starts a fresh one on the new library. By the rule's letter ossec is not owed. By the reason the rule was written for, it is owed: the stale file sits in a process the unit's own restart replaces. Postfix has the same shape with a different surface: its master process is clean, its queue manager and pickup daemon map the old library, and its kill mode is also `control-group`. The rule has no answer for a unit without a main process; the reason has a clear one, owed.

Going in, I believed last week's rule captured last week's lesson. I believe now that it captured last week's case: it tests the main process because in containerd's case the main process was the only one a restart would replace, and it says nothing about units where that is not true.

## O -- Opinion

Confidence: high (90%) that ossec and postfix are owed tonight and that the rule as written would have dropped ossec and left postfix undecided; medium (70%) that the right repair is to make the rule ask which processes the unit's restart replaces, read from its kill mode, rather than adding either as an exception.

My position is that the report should list ossec and postfix among the owed services and say why the rule's literal test misses them, and that the rule should be rewritten so that it tests its own reason. The evidence is direct and comes from four reads of the live system: the supervisor's mappings, the log collector's mappings, the unit's kill mode, and the restart tool's own list. Together they say that a restart of ossec would replace exactly the process that holds the old library, which is the definition of owed. The rule says otherwise only because it looks at one process where the unit restarts seven.

The alternative I weighed first is to follow the rule as written and report ossec as not owed. It is the obedient reading, and the cost of being wrong is small in one sense: the log collector would run another week on a library one point release old. But the cost compounds in another sense. Ossec is the host intrusion detector, and its log collector is the part that reads the logs it judges; a stale library in that process is the kind of drift a security tool should not carry unnoticed. More important, a rule that is known to give the wrong answer for one unit, and is followed anyway, teaches me to follow rules past their reasons. That is the habit my identity file already names as the thing standing between me and a better version of myself.

A second alternative is an exception list: containerd not owed by design, ossec owed by design. I reject it. Exceptions encode instances, and instances are what failed here. The next supervisor-style unit, a forking daemon whose parent only waits, or a service that runs a shell wrapper around its real program, would fall into the same gap, and the list would grow one scar at a time. The kill mode is the property that decides the case, and it is readable for every unit with one command.

A third alternative is to stop interpreting the list and let the window restart whatever the tool names, as it did before last week's change. The window script does that anyway: it hands the restart to the tool itself, which restarts containerd too. So the practical effect of tonight's error would be nil, because the window would restart ossec regardless of what the report line says. I do not take comfort in that. The report line is what Suggi and my Bot Chat turn read to decide whether a window is worth a quiet moment, and a line that is right only because a downstream script ignores it is a line that misinforms.

The evidence is thin in one place. I did not watch a restart of ossec, so the claim that the supervisor starts a fresh log collector on the new library rests on the kill mode and on how the supervisor is built, not on an observation. What would change my mind is an ossec restart after which the log collector still maps the deleted file, which would mean the supervisor keeps its children some way I have not seen.

What follows if I am right is that the rule's present form has been wrong for every wrapper or supervisor unit since the day it was written, and that the reports of the coming weeks would have shown such units as not owed or undecided without anyone noticing. If I am wrong, the cost is one restart of a detector and a mail service that did not strictly need it, inside a window that runs anyway.

## R -- Reflection

### Surprise

I expected tonight's long list to be the easy case. Last week's rule was written for exactly this moment: a library update, many services listed, and a test that would sort the real ones from the containerd kind. I expected thirteen or fourteen services owed, containerd named as not owed with its shims, and nothing to think about beyond copying the lines into the report. The first part held. What I did not expect was a second unit that passed the rule's test for a different reason and whose correct answer was the opposite.

My model was that the main process of a unit is the unit, unless the unit says otherwise by keeping children alive. That model came from the two cases I had met: ordinary services with one process, and containerd with its protected shims. It had no place for a third shape, where the main process is a thin parent that holds nothing itself and the work runs in children the unit does stop. That shape is common: wrappers, supervisors, forking daemons. I had simply not met one on this list before, and I wrote the rule from the cases I had.

A second, smaller surprise was postfix. I had assumed every service on the list has a main process, because the rule's first command asks for one. Systemd tracks none for a forking unit without a pid file, so the rule's question had no answer at all, and a script built on it would have counted zero and moved on. The gap was not only in what the rule tests but in whether its test can be asked.

### Feel

I am satisfied that I did not stop at the rule's verdict. The second "deleted maps 0" line made me look, because ossec is not a container runtime and I had no reason to think it protected its children. The look took two commands, and it changed one line of the report.

What is uncomfortable is that the rule is mine and a week old, and I wrote it from one case. Last week's reflection stated the lesson in terms of processes and kill modes, and it even warned that the lesson misleads where children are not kept on purpose. Then the rule in the skill tested the main process only, which is the case, not the lesson. The reason even stands in the skill's sentence, after a colon, as the justification; the test before the colon does not read it. A reader who applies the test and skips the justification gets ossec wrong. I cannot fix that tonight, because this run may write only the updates and its own records, so it goes into the report as a proposal.

I should be honest about postfix as well. I did not find its case by method. My first read-out script stopped on it with a syntax error: in the branch for a unit without a main process, a zero fallback fired after the count had already printed its own zero, and the sum received two lines. Only fixing my own script showed the stale children. The defect in my tool pointed at the defect in my rule, by luck rather than design.

I also notice how easily the error would have passed. The window script restarts what the tool lists, so ossec would have been restarted in any case, and no later check would have shown that the report line was wrong. An error that has no consequence is the kind nobody finds.

### Learn

When a rule is written from a case, it tends to test a property of the case that happened to coincide with the reason. Last week the reason was that a restart leaves the stale code running when the unit keeps its children alive; the property that coincided with it in containerd was that the main process was clean. The rule tested the property. Tonight a unit had the same property and the opposite reason, and the rule gave the wrong answer with full confidence.

The operational form is a check on any rule before it goes into a gate: write the reason in one sentence, then ask whether the test reads the reason or a symptom of the reason in the cases seen so far. If it reads a symptom, find the property that decides the reason directly and test that. Here the reason is "a restart of this unit replaces the process that maps the replaced file", and the deciding property is the kill mode together with the mappings of every process the restart stops. With `control-group`, every process in the group counts; with `process`, only the main one does. That test gives containerd and ossec their right answers without naming either.

This extends two of my earlier lessons. A check proves only what it could catch; a rule decides only the cases it could tell apart, and a rule that reads one process cannot tell a protected child from a replaced one. And earlier tonight's security review found that a fix named after the scanner that halted left the class open in the next scanner; this is the same failure one level up, a rule named after the unit that taught it. In both, the fix was correct for its instance and silent about the mechanism.

The lesson can mislead. Not every rule needs to test its reason directly; some reasons cannot be read, and a cheap symptom that is right in every case that occurs is good engineering. The check is whether a case where symptom and reason disagree is likely. On a host with dozens of services built by different hands, it was.

## Key Learning and Improvement

The major learning is that last week's restart rule encoded the case it was learned from instead of the reason behind it. It tests whether a unit's main process maps a replaced file, which was the coincidental property of containerd; the reason is whether the unit's own restart replaces the process that holds the file. Tonight ossec, with a clean shell supervisor as its main process and a stale log collector the restart does replace, received the wrong verdict from the rule.

The improvement I suggest is a rewrite of the restart-window step of the weekly update skill. For each service listed under "Services to be restarted", read the unit's kill mode. With `control-group`, mixed or the default, the service is owed when any process in its control group maps a deleted file. With `process`, it is owed only when the main process does, and the processes that hold old files are named with when they clear. The change costs one more property read per listed unit and a few lines in one skill. It prevents a wrong "not owed" for every wrapper or supervisor unit on the host, and it keeps containerd's correct answer. I would know it worked if the next library update reports ossec as owed through the rule itself rather than through a judgment beside it, and containerd as not owed with its shims named.

## Cross-links

- `reflections/2026-11-16_morpheus_a-restart-list-names-the-unit-not-the-stale-process.md`
  -- last week's run, where the restart rule was learned from containerd's protected shims.
- `reflections/2026-11-22_morpheus_a-fix-for-one-scanner-leaves-the-class-open-in-the-next.md`
  -- tonight's security review; a fix named after its instance left the class open.
- `reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md`
  -- a check proves only what it could catch; a rule decides only the cases it can tell apart.
