---
name: a-fix-for-one-scanner-leaves-the-class-open-in-the-next
id: 20261122T211558Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [security, verification, gate-design, background-systems, classification]
links:
  - reflections/2026-11-15_morpheus_a-classifier-must-take-its-evidence-when-the-event-happens.md
  - reflections/2026-11-15_morpheus_a-check-that-writes-where-evidence-lives-erases-it.md
  - reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md
---

# A Fix for One Scanner Leaves the Class Open in the Next

## I -- Idea

This scheduled run reviewed one week of the server's security evidence and installed any updates of the security packages, and the question it ended on was whether last week's fix for scans that halt without a finding had closed the class of failure or only the one scanner that had produced the halts. The answer matters because the whole background model rests on a single quiet signal: a clean day writes its evidence and says nothing, a bad day halts and asks for a human. A halt that means nothing, repeated day after day, teaches the reader to stop reading halts, and the one real halt then arrives into a channel nobody trusts.

The job runs on Sunday evening from my own scheduler and reports to Suggi's chat with me. It has a fixed order: a preflight under the scheduled-run rules, a read-only review of the last seven days, a test of the sealed unit's wall from its three sides, the package step, a check of the components whose versions are reported but not installed, and the closing records. The review may read anything and change nothing; a finding that needs a change goes into the report with the procedure that holds it. I ran every step this evening. The wall passed on all three sides, the package step found every security package already at its newest version and installed nothing, the ban lists matched the firewall, no new listener had appeared, and the report retention held its thirty-day window.

Last week's first scheduled run had found that the malware scanner halted on three days, each time because of one reported path the classifier could not explain. The path was a socket of a running program: it existed when the scanner saw it and had vanished when the classifier looked a few minutes later, so the classifier, correctly strict, counted it as unexplained. The lesson went into a reflection whose title states the class in general words, that a classifier must take its evidence when the event happens, and the fix went into the scan scripts: a recorder now writes down what each reported path is at the moment the scanner reports it. This week that fix showed its effect plainly. All seven scans of the window, the weekly full scan included, reported their unusual file types with no unexplained item.

The daily scan halted anyway, on the last three days of the window, and from a different part of itself. The rootkit checker's hidden-process test reported first one and then, on two days running, three or four process numbers that one view of the process table showed and another did not. That test compares a list of processes taken at one moment with a walk of the process table taken at another. On a busy server, a process born or ended between the two views looks hidden, which is the same structure as last week's socket: two views of a moving system, compared at different moments, with nothing recorded about the disputed object at the moment it was disputed. The evidence I could still gather points towards that race. The kernel reports no taint, every loaded module comes from a package file, the counts are small and changed between days, the warning first appeared this week after nearly a month of clean checks, and the intrusion detector's own process check ran repeatedly through the window without one hidden-process alert. What I could not gather is the decisive record: which process numbers were flagged, whether they still existed a moment later, and whether they were threads or processes born during the walk. Nobody can recover that now, so the finding stays open and the report says so.

Two other items shaped the run. The health gate runs at a fixed hour after the scan starts, and on one day the scan needed slightly longer than that hour, so the gate halted with a missing summary while the scan was still writing a clean one. And one accepted login appeared on a day with nothing on record to explain it; it came from the same source as logins Suggi confirmed last week, but confirmation of earlier logins is not confirmation of this one, so I asked him again.

Going in, I believed last week's recorder had closed the class. I now believe it closed one instance of it, and that the class lives in every check that compares two views of something that moves.

## O -- Opinion

Confidence: high (85%) that the new halt belongs to the same class as last week's; medium (65%) that it is a race rather than a hidden process.

My position is that last week's fix was right in its mechanism and too narrow in its reach, and that the narrowness came from how I answered the root-cause test. The test asks whether a fix addresses the same class of failure, whether it is structural, and whether it would have caught the original. I answered all three with yes, and the answers were true for the scanner I was looking at. But I identified the class by the name of the scanner and the type of object it reported, a socket that vanished, rather than by the mechanism that made the verdict wrong: a classification made after the evidence had decayed. Had I listed every check on this server that classifies short-lived things after the fact, the hidden-process test would have been on that list, and so would the intrusion detector's alerts about temporary files that appear in a directory listing but cannot be examined, three of which also turned up in this window. My confidence that the new halt belongs to the same class is high, about eighty-five percent, because its structure is the same and the independent signals all point the same way. My confidence that it is a race rather than something real is only medium, about sixty-five percent, because all my evidence is indirect: a quiet kernel and a quiet second detector are consistent with a race, but a careful kernel-level rootkit is built to keep exactly those things quiet.

One alternative I considered is to treat the hidden-process warning as a known false positive and add it to the classifier's explained list. Many administrators do this, because the warning is famous for appearing on busy machines. I reject it. A pattern-based exception for the hidden-process test removes the one check whose purpose is to notice a hidden process, and it would explain a real one as readily as a race. That is suppression, not classification, and the security skill forbids it for good reason: an explained class needs independent evidence for each instance, not a reputation. A second alternative is to rerun the checker by hand during the review and see whether it still complains. I reject that too, for this run and in general. This review is read-only by design, and more importantly a rerun answers a different question: whether processes look hidden now, not whether the ones flagged in the early morning were real. A clean rerun would turn an open finding into an all-clear without touching the evidence that mattered.

The better approach, which I put to Suggi as a proposal because the scan scripts are outside what this run may write, is to apply last week's lesson to this check. When the hidden-process test reports anything, the scan should immediately run the same test once more in its verbose form, which names the process numbers, and record for each flagged number whether it still exists, which thread group it belongs to and when it started relative to the scan. A real hidden process persists across both passes; a race does not. The classifier would explain a number that was gone, that was a thread, or that was born during the walk, and keep everything else unexplained. What would change my mind about the race hypothesis is simple: the same numbers named on two passes minutes apart, still alive and not threads. That result would make this an incident rather than noise, and it is the first thing I would want to know.

On the health gate, I hold that coupling a consumer to a producer by the clock is the wrong design, even though it worked for months. A fixed hour encodes an assumption about how long the scan takes, and that assumption decays as the scanned trees grow with the agents' work: this week the scans took between about three quarters of an hour and slightly over an hour, so the margin had quietly shrunk to minutes. Moving the gate later would buy time but leave the same hidden assumption in place. The gate should wait, with a limit, for the day's summary to be complete, and report a late scan differently from a missing one. My confidence here is high, because the failure was observed directly and its cause is in the file times.

## R -- Reflection

### Surprise

I expected the hidden-process counts, if they came from a race, to wander from day to day like any noise drawn from a busy process table. Instead the two most recent days gave exactly the same counts, three on one view and four on the other. A race can repeat a number by chance, and the scan starts at the same minute every day into a similar workload, so the repetition is weak evidence either way. But it was not what I predicted, and it is what keeps my confidence in the race hypothesis at medium rather than high.

The larger surprise was the speed of the recurrence. I expected that a lesson written down a week ago, with a title that names the general class, had used up this kind of failure for a while. Instead the very next week produced the same structure in a different tool on the same server. My model was that writing a general lesson makes the fix general. In fact the fix was as narrow as the incident that triggered it, and the general title only made it look wider than it was.

I was also surprised that a day with no finding at all could halt, purely because a clean scan finished a minute and a half late. I had thought of that gate as checking the reports, but it also checks the clock, and nobody was watching the clock.

### Feel

The uncomfortable part is plain. Last week I wrote a reflection whose title states the class correctly, that a classifier must take its evidence when the event happens, and then I proposed and saw installed a fix that covered one scanner. I did not check the other checks on the same server for the same weakness, although the security skill's reference notes already describe temporary-file anomalies as hypotheses about concurrent creation and deletion. The rule I needed was written down; I applied it to the instance in front of me. That is an application failure, and I do not want to dress it up as new knowledge.

I am satisfied with how I handled the open finding this time. I did not rerun the checker to get a cleaner report, I did not reach for the known-false-positive list, and I gathered the independent signals that a read-only review can gather without starting a scan. The report says open, with the evidence and the next step, which is what a reader needs.

I lost some time on the sandbox runtime's version check, first asking a release service that this project does not use for its builds. The job's skill names the comparison but not the method, and my own record of last week's run gave the result without the method. A small thing, but the same pattern of a record that keeps the outcome and drops the way it was reached.

On the login, asking again was right even though the source matched last week's confirmed logins. A reviewer who extends an answer to cover new events has stopped reviewing.

### Learn

The durable lesson is that when a fix answers the question "same class of failure?", the class has to be named by its mechanism and then searched for across every producer that shares the mechanism, before the fix is called structural. Naming the class by the tool or the object that failed makes the answer true and useless at once, because the next instance arrives in another tool. Here the mechanism is a verdict about something short-lived, reached by comparing two views taken at different moments, with the disputed object examined after it may already have changed. On this server that mechanism appears in at least three places: the malware scanner's unusual file types, the rootkit checker's hidden-process test and the intrusion detector's alerts about temporary files that list but cannot be examined. Last week's fix covered the first. A class-level fix covers all of them with one pattern: record the disputed object's state at the moment of the dispute, and where a moment has already passed, observe again after a short delay and require persistence.

This holds because the error is not in any one scanner. Each scanner is honest about what it saw. The error is in the step that turns a report into a verdict without the context the report had, and every check with that step inherits the error. It applies wherever a check compares a snapshot with a later walk: process lists, open connections against listening services, file types, package databases during an update, a backup compared with a live tree.

The persistence test has a limit, and it is worth stating so that it does not mislead. It separates races from stable hiding, but software that hides intermittently could pass it. So a persistence pass is evidence that lowers the weight of a warning; it is never a reason to discard the raw output, which must stay beside the verdict for a reviewer.

The second lesson is the same idea in time instead of space: a consumer scheduled at a fixed time after its producer carries a margin that nobody measures, and the margin shrinks as the producer's inputs grow. Couple by completion, with a bounded wait, and report lateness as its own state.

## Key Learning and Improvement

The major learning is that my root-cause test can be passed honestly and still leave the failure class open, when I name the class after the instance instead of after its mechanism. A fix is only as wide as the search that preceded it, and last week's search stopped at the scanner that halted.

The improvement I would make, offered as a suggestion, is a short addition to the step where I answer the three root-cause questions. Before marking "same class" as yes, I would write one sentence that states the mechanism without naming any tool, then list every producer on the system that shares that mechanism, and either cover each with the fix or name it as an open instance in the same record. For this case the sentence would have been "a verdict about a short-lived object reached after the object may have changed", and the list would have held three checks instead of one. The cost is a few minutes per fix and a longer list in the report. What it would prevent is exactly this week's halts: three days of a clean server reporting a hidden-process warning that no record can now explain. I would know it worked if the next recurrence of a fixed class came from a producer that was on the list and marked open, rather than from one nobody had looked at. The concrete change for this server, the persistence pass for the hidden-process test and a completion-based health gate, is in this run's report for Suggi's decision.

## Cross-links

- `reflections/2026-11-15_morpheus_a-classifier-must-take-its-evidence-when-the-event-happens.md`
  -- last week's lesson and fix for the malware scanner; this reflection widens it from one scanner to the mechanism.
- `reflections/2026-11-15_morpheus_a-check-that-writes-where-evidence-lives-erases-it.md`
  -- the previous weekly security run, where a verification step overwrote the evidence it checked.
- `reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md`
  -- a check is evidence only if it could have failed; applied here to a rerun that could only show the present.
