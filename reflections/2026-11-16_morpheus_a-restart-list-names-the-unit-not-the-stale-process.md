---
name: a-restart-list-names-the-unit-not-the-stale-process
id: 20261115T230745Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [infrastructure, verification, gate-design, cron]
links:
  - reflections/2026-11-15_morpheus_a-job-is-tested-only-from-the-process-that-runs-it.md
  - reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md
  - reflections/2026-10-28_morpheus_an-action-is-only-as-safe-as-the-assumptions-it-checks.md
---

# A Restart List Names the Unit, Not the Stale Process

## I -- Idea

This run set out to do the weekly update of the server on its schedule for the first time and, in a week where almost nothing was pending, to decide from evidence whether the restart window was owed. That decision matters more than its size suggests. The window is the one step of the job that interrupts other agents: it waits for a quiet moment, then restarts services under the fleet, and since this morning it is started by hand from my Bot Chat on the strength of one line in this report. A wrong "owed" spends a restart and a turn of attention for nothing; a wrong "not needed" leaves a service on old code that nobody looks at again.

The job is mine. Its skill names a fixed order: preflight, a record of the installed versions, the Ubuntu packages with the container runtime held back, the stable Hermes release, the catalog plugins, Claude Code, the restart window, the sealed unit of the game agents, leftover Docker volumes, then the closing records. The same skill says when the window is owed: when Hermes code or a plugin was installed, or when the tool `needrestart` names a service under its heading "Services to be restarted". The job was fired once by hand this morning as a test. That test installed twenty-eight packages and found that a scheduled run cannot start the window at all, because Hermes refuses inside the gateway any command whose script could restart the gateway. The skill was changed the same morning: the job reports the window as owed and names the services, and the Bot Chat turn that receives the report starts it.

Tonight the record showed nothing to install. After a fresh package list, no package was upgradable. Hermes was on the newest stable release, and every newer entry on the release page was a canary build. Seventeen plugin rows across seven homes were up to date. The Claude Code script answered that its build was current and changed nothing. I still ran the package step with the commands the skill names, the hold, the upgrade and the release of the hold, and it printed zero packages and an empty hold list. No reboot was pending.

Then `needrestart` named exactly one service to be restarted: `containerd.service`. By the letter of the skill, that makes the window owed. I did not write that line yet, because the package history said containerd itself had been upgraded at 14:14 local time that afternoon, and the unit's own start time was two seconds later. A daemon that restarted after its upgrade should not be running old code. So I looked at the processes in the unit's control group instead of at the unit. The containerd daemon maps no deleted file. Twelve other processes in the same group do: one `containerd-shim-runc-v2` per container started before the upgrade, from the host's boot on 14 November to the front container's restart early this morning, each still running the binary that the upgrade replaced on disk. The unit's kill mode is `process`, which means a restart stops the daemon and deliberately leaves the shims alone. That is the design: containers keep running while containerd restarts under them. It also means the window would restart a daemon that is already the new build and leave all twelve shims, and with them the listing, exactly where they are.

The rest of the run was short. The sealed unit's update script planned nothing to change and ended at once with `ok (nothing to update)`. Before I started it I read its plan, because my Bot Chat had left an installer for the unit's lead agent waiting inside the unit for a quiet moment, and I wanted to know whether two waiting programs could take the same moment; the script ends before any waiting when nothing differs, so they could not. The leftover-volume step removed nothing. The rows reported but not installed matched the morning's, except that containerd was no longer pending and available memory had fallen from ten to five gigabytes.

Going in, I believed that a service on the restart list is a service whose restart fixes the listing. I believe now that the list names the unit that owns a stale process, and that whether a restart of the unit fixes it depends on which process it is.

## O -- Opinion

Confidence: high (85%) that a window started for containerd tonight would change nothing that matters and that the listing would still be there next Sunday; medium (65%) that the right remedy is a change to how the job reads the listing, not to the window itself.

My position is that the report should carry the window as the skill's rule defines it, owed for `containerd.service`, and say in the same line that a restart would not clear it and why, so that the Bot Chat turn can decline it on evidence. The evidence for the main claim is direct and comes from three reads of the live system: the daemon's own process has no deleted mapping and started after the upgrade; the twelve shims run a binary marked deleted; the unit is configured to leave its children alive when it restarts. Together these say that the listing is caused by processes the remedy is built not to touch.

The obvious alternative is to follow the rule and let the window run. It is not dangerous. Docker only wants containerd rather than being bound to it, so a containerd restart does not restart Docker, and the shims keep the containers alive. But a restart with no effect is not free either. It interrupts container management for a moment, it costs a quiet moment in a fleet where quiet moments are scarce, and above all it fails to clear the line, so every following Sunday reports the same owed window until the containers restart for some other reason. A report that cries owed every week teaches its reader to skip that line, and the week it is real it will be skipped too.

A second alternative is to restart the containers themselves, which would replace the shims. I reject it for this job. The containers are the sealed unit, the memory servers and their databases; restarting them is a much larger act than the window, with its own owners and its own checks, and a host reboot, which is Suggi's, replaces every shim at once. A third alternative is to tell `needrestart` to ignore containerd. That is a configuration change the job may not make, and it would also hide the case where the daemon itself is stale, which is the one the listing exists for.

There is a tension in my own design that this run exposed. The script that installs the runtime packages by hand passes only when every container kept its start time. Keeping the containers running is exactly what leaves their shims on the old binary. So by construction every containerd update made the careful way produces this listing, and the job's rule turns it into an owed window. Two parts of one system, each correct, add up to a recurring false signal.

The evidence is thin in one place. I did not ask `needrestart` in verbose mode which process it attributes to the unit; I inferred the attribution from the control group's member list and their mappings. The inference is strong, because the daemon is the only member without a deleted mapping, but it is an inference. What would change my mind is a verbose listing that names the daemon itself, or a containerd restart after which the line disappears.

What follows if I am right is modest but real. The report line becomes a statement about processes rather than a forwarded verdict of a tool, and the Bot Chat turn that reads it can decline a restart without having to repeat my investigation. If I am wrong and the daemon is the stale part after all, the cost of declining is one more week on old code in a daemon that only manages containers, and the next run lists it again, so the error corrects itself at the price of a week.

## R -- Reflection

### Surprise

I expected an empty night. The morning's test run had installed twenty-eight packages a few hours earlier, so I expected the record to show nothing pending and, if the restart tool listed anything at all, a service whose own program was older than a library it uses. The first half held. The second did not: the tool named a unit whose daemon was the newest build on the machine, started two seconds after its own upgrade.

My model was that the unit on the list is the thing that is stale. That model came from the morning, when twelve services were listed after a library update and I read each as a service whose restart would replace the stale code. It is a good model for most services, which own one process or kill all of their children when they stop. It is wrong for a unit built to outlive its own restarts through children it never stops, and I had not met that case on this host.

A smaller surprise was the memory headroom. Available memory halved between the morning and the night, and the only package change in between was containerd's. I reported the figure and did not look for the cause, since a run of this job may only report it.

### Feel

I am satisfied that I asked why before I wrote "owed". The question took three commands and changed the meaning of the line. I want to be honest that it was not method alone that made me ask: the package history happened to be on the screen with a time two seconds before the unit's start, and the contradiction was hard to miss. On a different night, with the upgrade a week old, I might have written the line as the rule produces it.

What is uncomfortable is that the rule is mine. I wrote step 7 at the level of the unit, because that is the level at which the tool speaks and at which the window acts. I did not ask what the window can reach. This run may not change the skill, so the line goes into the report with an explanation, and the rule stays as it is until Suggi and I change it in an open session.

I also notice where I was lucky. I checked whether the sealed unit's update could collide with the installer waiting inside the unit only because the Bot Chat's recent turns, which I read for context at preflight, said the installer was there. The job's own steps would not have shown it. Nothing went wrong, and the safeguard was my reading, not the design.

### Learn

A restart list is a list of units, and what is stale is a process. Restarting a unit replaces only the processes that the unit's kill mode stops. For most units that is all of them, and the list can be read at face value. For units designed to keep children alive across their own restarts, the listing persists after any number of unit restarts, because the stale process is a child the unit protects. On this host the case is containerd and its container shims; the same shape exists wherever a supervisor hands off long-lived work that must survive it, as a login daemon leaves its open sessions running when it restarts.

The operational form is a question to ask before acting on any such list: which process maps the replaced file? If it is the unit's main process, restarting the unit fixes it. If only children kept by design hold it, the listing waits for those children to end on their own terms: a container restart, a logout, a reboot. Then it belongs in the report as a fact with its cause and its natural end, not as work owed.

This extends the lesson of 29 September, that a check proves only what it could catch, to the remedy side: a remedy fixes only what it can reach, and the reach of a restart is set by the unit's configuration, not by its name on a list. It also extends the morning's lesson that a job is tested only from the process that runs it. Both cases looked one level below the label a tool reports, at the process the label stands for, and both found that the label and the process differed.

The lesson can mislead where children are not kept on purpose. A unit whose kill mode stops its whole group does replace its children on restart, and there the face-value reading is right. The question is cheap either way, and it should be asked before the restart rather than after the listing reappears.

## Key Learning and Improvement

The major learning is that the job decided "owed" from the name of a unit, while the stale code lived in twelve processes that a restart of that unit is built to leave running. The rule was correct for every case I had seen and wrong for the first unit on this host that protects its children across restarts, and it would have produced the same false owed window every week after every careful containerd update.

The improvement I suggest is a change to step 7 of the weekly update skill. For each service listed under "Services to be restarted", the run reads whether the unit's main process maps a deleted file. If it does, the service counts toward the window as now. If it does not, the run names the processes that do, states that the window cannot clear them, and says when they will clear: when those containers restart, or at the next host reboot. Such a service then does not make the window owed. The change costs a few lines in one skill and one read per listed service. It prevents a weekly false alarm and the habit of skipping the line that a false alarm builds. I would know it worked if the next run after a containerd update reports the window as not needed with the shims named, and a run after a library update still reports the affected services as owed.

## Cross-links

- `reflections/2026-11-15_morpheus_a-job-is-tested-only-from-the-process-that-runs-it.md`
  -- the morning's test fire of the same job; a label above the process hid what the platform would allow.
- `reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md`
  -- a check proves only what it could catch; here the remedy fixes only what it can reach.
- `reflections/2026-10-28_morpheus_an-action-is-only-as-safe-as-the-assumptions-it-checks.md`
  -- an action rests on assumptions; the restart rested on the assumption that the unit was the stale part.
