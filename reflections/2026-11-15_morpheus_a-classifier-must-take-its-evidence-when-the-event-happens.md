---
name: a-classifier-must-take-its-evidence-when-the-event-happens
id: 20261115T033910Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [security, verification, gate-design, background-systems, classification]
links:
  - reflections/2026-09-01_morpheus_background-controls-need-an-evidence-lifecycle.md
  - reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md
---

# A Classifier Must Take Its Evidence When the Event Happens

## I -- Idea

This run set out to read one week of a server's background security evidence, install the pending updates of its security packages and report what the record showed, because a control that runs quietly is only worth trusting if somebody reads its record from time to time.

It was the first run of a new weekly job, started by hand as a test before its first scheduled slot. I manage the server the fleet lives on, and this job is the one recurring agent review that our background-only security model allows: the scanners, the intrusion detection and the ban service do their work through ordinary scheduled programs, stay silent on clean days, and keep a bounded window of reports that a person or an agent can read when asked. The run is read-only except for one step, the update of a fixed set of security packages. Its order is fixed in a skill: startup checks, the review of the retained week, the isolation test of a sealed container unit, the package step with checks before and after, a comparison of three components that are updated by hand against their newest releases, and then the closing work that produces this text.

I went in believing that a quiet week would end in the word clean. Every piece of the evidence chain had been built weeks earlier: scanner summaries that separate explained conditions from unexplained findings, a daily health verdict that reads those summaries, and a retention rule. The review confirmed most of that. A report existed for every day. The services and their workers were alive. The lists of banned sources matched what the firewall enforced, entry for entry. Nothing in the report folder was older than the retention window. The sealed unit passed its isolation test on all three sides. The intrusion-detection summaries matched the raw alert archives exactly when I counted both for the same period.

The daily health verdict, however, had been HALT on several mornings of the week, without one infected file on any of them. Each halt carried the same single line; the newest also carried two warnings from the rootkit checker about an account created the day before, which our own records explain. The malware scanner cannot read special files, the endpoints that running programs open to talk to each other, and it reports each one as an unsupported type. A small classifier then confirms for each reported path that it really is a special file and counts those as explained. That confirmation runs after the whole scan has finished, minutes later, and some of these endpoints live for seconds. One that existed when the scanner passed and was gone when the classifier looked could not be confirmed, was counted as unexplained, and one unexplained line halts the gate. For the most recent morning I could name the path, because I looked within the hour and exactly one reported path no longer existed. For the earlier mornings the record no longer allowed that: more paths had disappeared since, and the logs showed only which paths had appeared on that day alone.

Three smaller things happened around that finding. To list what the automatic updater had installed during the week, I wrote a parser over the package manager's history and labelled a transaction as the updater's when the updater's name appeared in its command line. The install command of this very run named the updater's package among the packages to upgrade, so my parser counted my own transaction as the updater's. I saw it because the script printed its rows beside the total, and one row carried the minute of my own command. Second, the procedure asks for the health gate to pass after the package step. It could not pass: it reads the day's scan verdict, which had been HALT since before I started. Third, I opened the detailed reference behind the review procedure only during the closing work, while searching for an existing rule about disappearing paths. It held that rule, written for the reviewer, and two checks I had not yet run. I ran both; neither changed a finding.

What I believe now is narrower than what I believed going in. The week's evidence showed nothing that recorded work does not explain, apart from items that only the server's owner can recognise. The verdict is still not clean, because one of the gates that produces the verdict was halting on its own timing.

## O -- Opinion

Confidence: high (88%). A classification is a claim about a moment, and its evidence has to be taken at that moment. A classifier that looks later and files everything it can no longer confirm under the alarm class is safe in direction and wrong in design.

The existing classifier got the hard part right, and I want to say so before criticising it. It does not trust names. It asks the operating system what each reported path is, it keeps every raw line, and it halts on anything it cannot explain. That is the discipline I argued for in `reflections/2026-09-01_morpheus_background-controls-need-an-evidence-lifecycle.md`: expected conditions may be classified, but only on independent evidence, and unexplained findings must never be normalized away. The flaw is in time, not in logic. The scanner observes a path at one moment; the classifier asks about it at another. For durable objects the two moments give the same answer. For objects that live for seconds they do not, and the classifier has no way to tell a vanished harmless endpoint from anything else that vanished.

I reject three ways out. The first is to exclude the folders where such endpoints live from the scan. That removes the false alarm and also removes every ordinary file in those folders from the scan, which trades a noisy gate for a blind spot. The second is to classify by name, treating anything that looks like an endpoint as one. A name is chosen by whoever creates the file; a classifier that accepts names is suppression with extra steps. The third is to leave the gate as it is and let the weekly reviewer explain each halt. This run shows what that costs. The explanation was only fully available for the newest day. For the older days I could establish the kind of object and not the object, because the evidence that would have named it had decayed in the meantime. A reviewer who explains the same halt every week also learns to expect it, and a gate whose HALT is expected has stopped being a gate. That is the alert-fatigue failure from the opposite side: not too many messages, but one message that has lost its meaning.

The design I hold instead keeps the strict rule and moves the evidence. The scan itself should record, at scan time, which paths under the scanned trees are special files. The classifier then accepts a reported path as explained when that record shows it was a special file while the scanner ran, and keeps halting on everything else, including a regular file the scanner could not read. Nothing is relaxed. The claim "this was a special file when it was reported" finally rests on an observation from the moment it is about.

My own parser made the same class of error in miniature. I decided who ran a transaction from a word in its command line, a proxy, when the record held a field that says which program was invoked. What saved the report was not care. It was that the script printed the rows the total was built from. `reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md` says a check is evidence only if it would fail in the likely world where the claim is false. A bare total could not have failed here: eleven looks as plausible as ten. A list of rows could, because one row was visibly mine.

The post-install gate deserves the same scrutiny. Requiring an absolute PASS after a change assumes the baseline was PASS. When it was not, the honest question is a difference: which issues exist now that did not exist before the change. I had the gate's output from before the install and compared the two lists; they were identical. An absolute requirement would have turned an old fault into a false accusation against the update, or into pressure to make the gate green before reporting.

My evidence is strong for the newest day and thinner for the older ones, where I rely on the pattern that the paths seen on a halting day alone were all endpoints of the same kind. If a scan-time record later shows a halting line whose path was a regular file, the timing explanation is incomplete and this opinion needs revising.

## R -- Reflection

### Surprise

I expected a first run over a quiet week to end in a clean verdict, and it ended in one that asks for attention. The surprise was not a finding about an intruder. It was that a control I had helped build and described as finished could halt repeatedly without a single real finding, and that nothing in its own output said why. The summary line reads the same whether one unexplained item is a threat or a path that no longer exists.

I also expected knowledge written down for one stage to protect the neighbouring stage. The reference behind the review procedure already says that a temporary endpoint can disappear before review and that an absent path proves nothing about the earlier moment. That sentence was written for the reader of old reports. The producer of the reports has the identical problem at a smaller time scale, minutes instead of days, and there it does not produce a note in a review; it produces a HALT. I had not carried the lesson across, because I had filed it under reviewing rather than under what it is, a statement about evidence and time.

The third surprise was how ordinary my own error looked. The updater's name in a command line seemed a perfectly reasonable sign of the updater. It took a row showing my own command to make the proxy visible as a proxy.

### Feel

I am satisfied with how the counts in this run were made. Every number came from command output, the scripts printed groups and never a source address, the comparison of ban lists and firewall entries was a set comparison rather than a glance at two totals, and the summaries were checked against the raw archives. I am also satisfied that I did not call the week clean and did not soften the failing check. The procedure says a failing check leads the report, and it will.

Two things are uncomfortable. I read the detailed reference late. The skill pointed to it at the end of the section I was working from, and I started from the numbered steps above that pointer. The two checks it added changed nothing this time, which is luck, not method; had one of them mattered, I would have found out only because the closing search for an existing rule led me to the file. And the first result of my parser was wrong in a direction that flattered nothing and hurt nothing, a count of eleven where ten was true, which is exactly the kind of error that survives because nobody has a reason to doubt it. I caught it from the rows. If I had printed only the total, it would be in the report.

I am uneasy, though not ashamed, about the older halting days. I can say what kind of object caused them and cannot name it, and I have said so rather than rounding the explanation up.

### Learn

A classification is a statement about a moment, so the evidence for it must come from that moment. When a verifier runs later than the observation it verifies, everything short-lived turns into "cannot confirm", and a strict gate turns "cannot confirm" into an alarm. The strictness is correct and should stay. The delay is the defect. The fix for this class is always the same shape: record the property at observation time, next to the observation, and let the later step read the record instead of asking the world again. This holds for scanners, for log parsers that look up a process that has since exited, for audits that check a file a job has since rewritten, and for my own reports when I describe a state I did not capture when I saw it.

The lesson has a boundary. For durable objects, a later look is as good as an earlier one, and capturing more at observation time only adds cost. The test is whether the object can change or vanish between the observation and the check within the normal operation of the system. If it can, the check needs a record from the earlier moment.

An alarm that the gate's own mechanics produce is a debt that grows. Each occurrence costs a reviewer a reconstruction, the reconstruction gets worse as the evidence ages, and the readers of the gate learn that HALT can mean nothing. Explaining such an alarm once is review. Explaining it every week is maintenance of a defect, and the right response is to repair the mechanism while the strict rule stays untouched.

Two working habits follow from the smaller events. A total should travel with the rows it was built from, because a wrong total and a right one look alike and a wrong row does not. And a check after a change should be read as a difference against the state before the change whenever that state was not green; the question is what the change added, not whether the world is perfect.

This extends the lesson of 2026-09-01, which named honest classification as one of four properties of a background control, by adding time to it: honest classification includes when the evidence was taken. It applies the lesson of 2026-09-29 to my own script: the row list was the check that could have caught the error, and the total was not.

## Key Learning and Improvement

The major learning is that a verdict inherits the timing of its evidence. The scan gate was strict, independent and well tested, and it still halted without a finding because it asked about short-lived objects minutes after they were seen. Strictness without evidence from the right moment produces alarms that mean nothing, and repeated alarms that mean nothing wear down the one signal the whole background model depends on.

The improvement I would make is in the scan scripts, and I offer it as a suggestion for the server's owner because changing a security classifier is his decision and lies outside what this run may write. Immediately before and after the scanner runs, the script would write a list of every path under the scanned trees that is not a regular file, with its type, and keep that list beside the raw scan log under the same retention. The classifier would count a reported unsupported path as explained when either list shows it as a special file, and would keep counting everything else as unexplained. The cost is one extra walk over the scanned trees per run and a small file per day. It would prevent the false halts and leave the strict rule in place. I would know it worked if, over the following weeks, days without a real finding show zero unexplained items, while a test fixture, a regular file the scanner cannot read, still halts the gate.

## Cross-links

- `reflections/2026-09-01_morpheus_background-controls-need-an-evidence-lifecycle.md`
  -- the four properties of a background control; this reflection adds the time of the evidence to honest classification.
- `reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md`
  -- a check is evidence only if it could have failed; applied here to a total printed without its rows.
