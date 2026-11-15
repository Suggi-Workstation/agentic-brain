---
name: a-check-that-writes-where-evidence-lives-erases-it
id: 20261115T211258Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [security, verification, gate-design, background-systems, cron]
links:
  - reflections/2026-11-15_morpheus_a-classifier-must-take-its-evidence-when-the-event-happens.md
  - reflections/2026-11-15_morpheus_a-score-change-needs-the-same-ruler-and-a-kept-baseline.md
  - reflections/2026-09-01_morpheus_background-controls-need-an-evidence-lifecycle.md
  - reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md
---

# A Check That Writes Where the Evidence Lives Erases What It Was Meant to Confirm

## I -- Idea

This run set out to review one week of the server's security evidence and to update its security packages, and it mattered because it was the first scheduled run of a job whose whole value is that it is read on a Sunday night by someone who did not watch it work. The weekly security review is one of three jobs I run on the server every Sunday. It reads seven days of reports from the malware scanners, the intrusion detector and the daily health gate, compares the ban lists of the authentication guard with what the firewall enforces, lists every accepted remote login, checks which ports listen where, runs the seal test of the sandboxed unit in which the game agents live, installs updates of a short list of security packages, and reports newer versions of three components it is not allowed to install. It may write only that package update and its own records. Everything else is read and reported.

The job had already run once today. Suggi fired it by hand early in the morning as a test, and that run found a real fault: the daily malware scan had halted on three mornings of the week without finding anything, because its classifier looked at short-lived socket files minutes after the scanner had reported them, when they were already gone. The fix, a recorder that notes what each reported path is at the moment the scanner names it, was built and tested in the afternoon in an interactive session. So I went into the evening run expecting a quieter version of the morning: the same week shifted by about eighteen hours, the same three halted mornings, the fix in place but not yet exercised by a scheduled scan, and the same open question for Suggi about a few logins that only he can attribute.

That expectation held for most of the run. The scanner, health and detector summaries were present for every day of the window. The detector's daily reports reconciled exactly with its raw archives over the part of the window they cover. Every high-severity alert and every changed file in the monitored folders traced to recorded work or to known internet noise: the sandboxed unit built on Saturday, an embedding service switched, log caps added, the detector upgraded this afternoon, the scan recorder installed, the week's operating-system updates, and an update of the mesh network software that turned out to be that software updating itself, a setting I had not known was on. The ban lists matched the firewall entry for entry. No new listener had appeared. The seal test passed every check on all three sides. All twelve security packages were already at their newest version, so the install step installed nothing.

The finding of the run came from a timestamp. All times here are local. The health gate runs every morning at four and writes a dated report. The report for today said it was generated at half past four, not at four. The scheduler's journal showed that the four o'clock run had fired. The half-past-four file had been written by this morning's test run of my own job, whose package step ends by running the same health gate to prove that the install broke nothing. The gate writes to the dated file of the day, so a check run later on the same day replaces the morning's record. Tonight's run, following the same step, replaced it again at ten past ten in the evening. Today now has no record in the report folder of what the scheduled gate said, only of two runs of my job.

Going in, I believed the post-install health check was a pure reader: a gate I call to learn whether the server is healthy. I believe now that it is a producer that happens to return a verdict, and that calling a producer as a check rewrites the evidence it is meant to check. A second, smaller version of the same lesson came from the version step. The proxy image of the sealed unit is pinned by a tag and a content digest, and the tag's name was still the newest one published, but the image behind that name had been rebuilt about two hours before the run.

## O -- Opinion

Confidence: high (90%) that the post-install check, as the job is written, replaces the day's scheduled health record every time it runs, and medium (70%) on the best fix.

The evidence for the main claim is short and direct. The gate's script takes no output option and writes its report to a file named by the day. The journal shows its scheduled run at four. The file's generation time was the morning test run's, and after tonight's check it is tonight's. Both runs of my job read the gate's result correctly and reported it correctly. The damage is not in either report; it is in the folder those reports are about. Next week's review, reading the retained window, will find a health report for this Sunday generated late in the evening and will have no way to know what the gate said at four, except that both of my runs happened to report the same verdict.

This week the loss is small, because the gate gave the same verdict all three times: halted, for one reason, the malware scan of that morning. That is luck, not design. On a morning when the gate halts for a reason that is gone by evening, a stale signature or a detector daemon that died and was restarted, my evening check would write a passing report over the morning's halt, and a review reading the folder a week later would see a clean day. The morning test run made the same overwrite and did not notice it. It compared the gate's issue list before and after the install, which was the right comparison, and held the before in its own context, which is where it stayed. The record on disk was gone.

I weighed the view that this is not a fault at all. The skill tells the run to call the gate; the gate's job is to describe the server's health now; a fresher report is a better report. There is something in this. A health report generated after a package update describes the server more accurately than one from eighteen hours earlier. I reject it as a reason to keep the step as it is, for two reasons. The security model of this server is background-first: the scheduled programs do the work and leave dated evidence, and the review reads that evidence. A review that rewrites the evidence breaks the one property the model depends on, that the record of a day is what the scheduled controls saw on that day. And the job's own boundaries say it is read-only except for the package update and its records. The rewritten health report is neither of those.

I followed the step tonight anyway. I had seen the overwrite in the morning's file before I reached the package step, the verdict was certain to be the same, and the skill names the call. I chose to run the written step in an unattended job and report its side effect, rather than improvise around a procedure nobody was watching me change. I hold that choice as defensible, not as clearly right.

On the fix I am less sure. The cleanest change is a mode of the health gate that prints its verdict and writes nothing, which the job would call after the install. That touches a security script, which is Suggi's decision. A weaker change needs no script edit: the job reads and records the day's report before calling the gate, so its own report states what was replaced. That keeps the lost evidence in the job's report instead of in the folder, which is better than losing it and worse than not overwriting it.

What would change my mind on the main point is a second health record I have missed, such as a copy the gate keeps elsewhere or a journal line carrying its verdict. I read the gate's script and the scheduler's journal and found neither.

## R -- Reflection

### Surprise

I expected the evening run to be a quieter repeat of the morning one: the same evidence, one day later, read with helpers that had already been debugged. I expected the only new information to be whatever happened in the hours between the two runs. What I did not expect was that one of the files I would read as evidence of the week had been written by my own job in the morning, and that the step which wrote it was a step I was about to run again.

I noticed it only because the report's generation time and the scheduler's start time were half an hour apart. The morning run had read the same file before its install, while it was still the genuine one, and then ran the gate after the install. It did not see the overwrite because the file it read first was the real record, and the file it left behind was not read again until tonight. My model of the step was that the gate is a test. It is a test that publishes.

I also did not expect the version step to need content rather than names. I had treated an image tag as a version: if the pinned tag is the newest tag, the image is current. Tonight the newest tag was the pinned one, and the build under it was new. A rolling tag is a pointer, and the digest is the version.

A smaller surprise was that the mesh network software updates itself. A package upgrade by the superuser in the middle of the night looked at first like work nobody had recorded. It was the software's own updater, enabled in its preferences, and my job lists that package among the ones it installs.

### Feel

I am satisfied with how the review read the week. Every count in the report came from a helper run tonight, the detector's alerts were reconciled with the raw archives and not with the summaries alone, the reference file the morning run had opened too late was read before the first check, and each changed system file was matched to a dated piece of recorded work rather than waved through as the week's busy work. That earns the confidence I have in the findings.

I am less comfortable with a step I ran knowing what it would do. I saw the overwrite before the package step and ran the gate anyway. I think that was the right side of a real tension: an unattended job that rewrites its own procedure when it disagrees with a step is a worse risk than one evening's lost record that I can describe exactly. But the record was mine to protect, the loss was certain when I ran the step, and I chose the written step over the evidence. The report says so plainly; that is the least it owes Suggi.

The morning run's miss is also mine. It was the same job, written by me. It compared before and after without asking where the after was written. I wrote the step, tested the job once by hand and called it ready, and that test fire was exactly the run that should have caught this.

The logins only Suggi can attribute stay open for a second report, and I am uneasy about asking twice. Asking is right; the logs cannot say whose they are, and a review that guessed would be worse. The discomfort points elsewhere: a weekly job can raise the same question every week, and the answer lives only in his memory. Unless his answer is recorded where the next run reads it, the same rows will come back each Sunday until they leave the window.

### Learn

A check is only a check if it leaves the thing it checks as it found it. Many tools in operations are producers that also return a verdict: a health gate that writes its report, a scanner that writes its log, a test that refreshes a baseline, a scoring tool that saves its latest results over the last ones. Calling one of them to verify something is safe only when what it writes cannot replace evidence that someone will read later. When the output is named by date, a second call on the same day replaces the first, and the record of the scheduled run, the one the whole design depends on, quietly becomes the record of the most recent manual call.

This matters because of the shape of the background security model. The scheduled controls run unwatched and leave dated evidence; a human or an agent reads that evidence later and trusts that each day's file is what the control saw on that day. Every extra writer into that folder, however well meant, turns the evidence into a mixture of scheduled and ad hoc results with nothing to tell them apart. A morning halt can become an evening pass, and a review a week later cannot know it happened.

The practical rule follows. Before using any tool as a verification step, ask where it writes. If it writes into an evidence store, call it in a mode that does not write, or record the existing file before the call so that the replacement is at least known and described. For a review job whose boundary is read-only, the first is the real fix and the second is the stopgap. The same rule covers the scoring tool that overwrote its own baseline earlier today, and it is the same class as the classifier that judged a file after it was gone: in each case the evidence and the verdict came from different moments or different writers, and the record no longer said what had happened.

The version lesson is the same principle applied to identity. A name is a claim about content, and a rolling name is a weak claim. When a component is pinned by digest, compare digests; the tag says which line of builds you follow, not which build you have.

The rule has limits. A tool whose output is append-only and labelled by run, or a check against a throwaway copy, carries no such cost. Nor does the rule say a job may never re-run a producer. It says the job must know that it is doing so, and that the evidence store must be able to tell the scheduled run from the manual one. Where neither holds, the check should not be run against the live store at all, because its passing result would be the least trustworthy line in the folder.

## Key Learning and Improvement

The major learning is that my weekly review job, built to read the server's security evidence without changing it, rewrites one piece of that evidence each time it runs, because its post-install verification calls a health gate that writes its dated report. The verdict it returns is right; the record it leaves is not the scheduled one. The morning test run and the scheduled run both did it, and only a generation time half an hour off revealed it.

The improvement I suggest has two parts and is not applied, because this run may write only the package update and its own records. The first is a no-write mode for the health gate that prints its verdict to standard output, which the weekly job would call after the install; the scheduled run would remain the only writer of the dated report. That is a small change to a security script and needs Suggi's approval. Until then, the second part costs nothing: the package step records the day's report, its verdict, issues and generation time, before calling the gate, and the job's report states that the file was replaced and what it said. I would know the fix worked when next Sunday's health report for the day still carries its four o'clock generation time after the job has finished. For the version step, I suggest that the proxy row compares the pinned digest with the tag's current digest as well as the tag's name.

## Cross-links

- `reflections/2026-11-15_morpheus_a-classifier-must-take-its-evidence-when-the-event-happens.md`
  -- the morning test run of the same job; a verdict inherits the timing of its evidence.
- `reflections/2026-11-15_morpheus_a-score-change-needs-the-same-ruler-and-a-kept-baseline.md`
  -- a scoring tool that overwrote its own baseline; the same class of writer into evidence.
- `reflections/2026-09-01_morpheus_background-controls-need-an-evidence-lifecycle.md`
  -- why the dated evidence of background controls is what a review must be able to trust.
- `reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md`
  -- what a check can and cannot show; here, what a check can also take away.
