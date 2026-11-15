---
name: a-score-change-needs-the-same-ruler-and-a-kept-baseline
id: 20261115T053324Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [gold-queries, evaluation, verification, information-retrieval, brain-index]
links:
  - research/insights/gold-query-maintenance-procedure.md
  - reflections/2026-11-08_morpheus_last-weeks-knowledge-is-a-claim-about-this-week.md
  - reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md
  - reflections/2026-11-15_morpheus_a-classifier-must-take-its-evidence-when-the-event-happens.md
---

# A Score Change Needs the Same Ruler and a Kept Baseline

## I -- Idea

This run set out to repair the drifted gold question sets of the server's six search indexes and then score every index, because a benchmark that no longer matches its files measures nothing, and a score that is never compared with the week before cannot show that search has become worse.

The six indexes serve the fleet's three shared repositories, the knowledge base, the research forge and the investing hub, and the private workspaces of the three core agents, Neo, Cassandra and myself. Each index has a gold set: questions written by independent writers who read one whole file and ask what it holds, each paired with the files that answer it. Scoring sends every question through the search and records where the right file lands: first place, the first five, the first twenty, and the mean reciprocal rank that summarises all of it. The job is new and weekly. Suggi fired this first run by hand as a test, before its first scheduled slot. A tool does the mechanical work: it plans which questions drifted because their files changed and which new files need a question, writes a brief for each batch of writers, checks their answers, applies them, runs the scoring, lists the misses and adds files to a question's relevance set. My part was to run the steps in their order, dispatch the writers, read every question once, commit each gold file alone, and judge each miss by reading what ranked above the gold file.

The repair went as designed. The plan found drift in five sets: thirteen rewrites and three new questions in the knowledge base, one new question in the forge, three rewrites and three new questions in the investing hub, two new questions in my workspace and one rewrite in Neo's; Cassandra's set had none. Five writers produced twenty-six questions, and the independent check passed all of them with no warning. Each changed set validated, and each commit held its gold file alone. Scoring took seventy-nine and a half minutes, forty-eight of them for the knowledge base. The knowledge base and my workspace rose slightly, Neo's and Cassandra's sets scored exactly as before, the forge fell from a mean reciprocal rank of 0.7236 to 0.6842, and the investing hub from 0.9512 to 0.9151.

The forge fall was the moment the run changed character. Fifty of its fifty-one questions were unchanged, and the skill asks for a fall on an unchanged question set to be named with the questions that moved. When I went to list them I found that the tool keeps only three summary numbers of the previous run, and that the evaluator writes its per-question results over the old file. For the forge and the knowledge base, the previous rows were already gone. The investing hub and the three workspaces had not run yet, so I copied their previous files into the work folder and compared afterwards, question by question. Then I looked at dates. The forge's previous results had been written on the afternoon of 14 November, about three hours before the commits that changed the embedding model and switched on the reranker in all six search configurations. The investing hub's previous file lacked two fields that the current evaluator always writes, so it came from a different state of the evaluator. For those two repositories, last week's number had been taken with a different ruler.

The misses step then judged twelve questions whose file was not in the first five. Four relevance sets grew by five files: two archived skills that answer questions about earlier formats, a skill and an insight that restate a tool's README, and the forge protocol, which answers a question about final-review verdicts as fully as the template does. Eight were real retrieval misses.

Going in, I believed the before-and-after line of each set was the run's main result. Now I believe it is like for like for the three workspace sets, uncertain for the knowledge base, whose previous run finished seconds before its configuration commit, and mixed for the forge and the investing hub, where it adds two causes that nothing the run kept can separate.

## O -- Opinion

Confidence: high (85%). A change in a benchmark score is evidence about the system only when two conditions hold. Both runs must have used the same instrument, and the earlier run's per-question record must still exist when the comparison is made. Without the first, the difference adds a pipeline change to whatever drift happened in the questions and the corpus. Without the second, a fall can be reported but not explained, because nobody can say which questions moved. The tool, as built, secures neither condition by itself.

Most of the run deserves to be trusted, and I want to say why before criticising the comparison. The repair touched only questions whose files had changed; the writers saw neither search results nor the existing questions; the check is mechanical and found nothing to reject; the commits were scoped and are on the remote. The three workspace sets give the strongest evidence of the day. Their previous runs came after the pipeline change, and across all three, not one unchanged question moved by a single rank. That is what a stable instrument shows when nothing but the questions changed, and it makes the workspace numbers trustworthy in both directions.

The investing hub shows what the opposite case looks like. Of its thirty-eight questions with unchanged text, five moved; one fell from first place to sixteenth, and another lost half of its relevance set from the first twenty. Read naively, that is a regression of the investing index. But the previous file predates the configuration change and was written by a different evaluator state, so at least part of the movement belongs to the new model and the reranker, and I cannot split the parts. I reject reporting the change as a decline of the index. I also reject dismissing it: the question that now ranks sixteenth is a real miss today whatever caused it, because the framework that defines the thresholds for a wide moat is outranked by fifteen files, fourteen of them company files that apply those thresholds.

I weighed three ways forward. The first is to recreate the old pipeline and score both versions. I reject it: this run may not rebuild an index or touch a configuration, and a rebuild with the old model would cost the index's owner more than the comparison is worth. The second is to treat this week's results as the new baseline and let next week's run compare like with like. I accept it as the honest reading of this week, but it only works if next week's run still has this week's per-question record, which today it will not. The third is already half built: the evaluator can compare a run with an earlier results file question by question and report the difference of the mean reciprocal rank with a confidence interval. The weekly tool does not use it, because it does not keep the file. The fix I suggest therefore costs little: copy the previous results before scoring, compare with them when the pipeline matches, and print a plain mismatch line when it does not.

One judgment in the misses step will look wrong to some readers. I added two archived, superseded skills to the relevance sets of questions about the earlier evaluation and proposal formats. A fair objection is that an agent should never act on an archive. I hold that the benchmark measures whether search finds the file that answers the question asked, and for a question about the old format the archived skill answers it. Whether archives should be indexed at all is a separate design question, and it belongs to Suggi.

My evidence is thinnest for the forge. Its previous file is gone, the file date is my only evidence, and I cannot tell whether that afternoon run used a configuration that was already changed but not yet committed. If a record shows that it did, the forge fall is real drift and needs its own investigation.

## R -- Reflection

### Surprise

I expected the previous run to be a fixed reference, like the zero of a balance that was tared once and left alone. Instead the reference had moved underneath it. The retrieval pipeline changed on the same day as the previous runs: after the forge and investing runs, seconds after the knowledge base run, and before the three workspace runs. Six numbers printed side by side looked like one kind of comparison and were three kinds. I also expected a tool that prints "last run" to keep what it compares against. It keeps three summary numbers, and the record that could explain them is overwritten by the very run that is compared with it.

Two smaller surprises came from the misses. Archived skills competed with live templates and sometimes answered just as well, so the archive is a real part of the corpus the search sees. And a question written in this very run, for the README of the knowledge base's search tool, missed the first twenty entirely, while a skill and an insight that list the same scripts with their jobs took the first two places. I had not expected redundancy inside the corpus to defeat a question that was written to be specific.

### Feel

I am satisfied with three things. I did not report the forge fall as a decline of the index; it goes into the report as the finding the skill asks for, with the reason its moved questions cannot be listed. When I saw the overwrite I saved the four previous files that still existed instead of noting the gap for later, and that is why the investing movement can be shown question by question. And every number in my records comes from the tool's output or from the comparison script that printed its rows.

Two things are uncomfortable. I noticed the overwrite only after the forge set had run, about fifty minutes into scoring, and I read the scoring function only while I was waiting for it. Had I read it before starting, I could have saved all six previous records. I had assumed that a tool which prints the last run's numbers keeps the last run, which is exactly the kind of assumption my reflection of 8 November warned about: a claim learned in another week, used without one fresh look. The second is smaller. My first check of the gold files for non-ASCII characters printed a failure for all five files while showing no offending line, because the pipeline returned the exit status of its last command. I caught the contradiction because I read the output rather than the label, and I replaced the check with counts.

### Learn

Every comparison has three parts: two measurements, and the claim that nothing but the thing of interest changed between them. The third part is rarely written down, and it is the part that fails. In a search benchmark at least four things can change between two runs: the questions, the corpus, the retrieval pipeline and the evaluator itself. When more than one has changed, the difference of the scores is the sum of their effects, and it cannot be taken apart afterwards unless the per-question record of both runs survives. Two rules follow. Before computing a difference, write down what changed between the two measurements, and if more than the subject of interest changed, label the difference as mixed instead of interpreting it. And keep the earlier per-item record until the comparison has been made, because a summary cannot be decomposed.

The rule is old outside this server. A chemist does not compare yields across a change of balance without recalibrating, and an investor does not compare margins across a restatement without restating the earlier year. In both cases the instrument, or the accounting, is part of the measurement. What this run adds is the second half: the baseline has to be kept by whoever overwrites it, because the overwrite happens as a side effect of the very run that needs it. It is the same lesson as the classifier finding from earlier today in a different place: evidence that exists only until the next event must be captured before that event.

The rule has a boundary. When the per-item record is expensive to keep, or the instrument is known to be fixed, a summary comparison is enough, and keeping everything only adds cost. Here the record is at most about a hundred kilobytes per set each week, and the instrument had changed the day before, so neither excuse applies.

## Key Learning and Improvement

The major learning is that a score difference is evidence about a system only when the earlier measurement was taken with the same instrument and its per-item record is still there when the comparison is made. This run had the instrument problem for two of its six sets and the record problem for two, and the overlap was the forge, whose fall can be neither attributed nor explained.

The improvement I would make is in the weekly tool's scoring step, and I offer it to Suggi as a suggestion because this run may write only gold files and its own records. Before the evaluator runs for a set, the tool would copy that set's previous results file into the run's work folder. After the run, it would compare the two files: when the pipeline fields recorded in both files agree, it would run the evaluator's existing question-by-question comparison against the copy and print the questions with unchanged text whose rank moved; when the fields are missing or differ, it would print one line saying that the pipeline changed since the last run and the comparison is not like for like. The cost is perhaps a dozen lines and a few hundred kilobytes of scratch per week. It would have named the forge questions that moved and labelled two of this week's six comparisons before anyone read them as a decline. I would know it works when the tool's own throwaway test shows the mismatch line for a run whose reranker field differs, and the list of moved questions for a run whose pipeline is unchanged.

## Cross-links

- `research/insights/gold-query-maintenance-procedure.md`
  -- why relevance sets grow with the corpus and how to read a falling score; this run adds the instrument as a cause.
- `reflections/2026-11-08_morpheus_last-weeks-knowledge-is-a-claim-about-this-week.md`
  -- knowledge has a date; last week's score is last week's claim, taken with last week's instrument.
- `reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md`
  -- a check is evidence only if it could fail; applied here to a comparison that could not be decomposed and to my own ASCII check.
- `reflections/2026-11-15_morpheus_a-classifier-must-take-its-evidence-when-the-event-happens.md`
  -- evidence must be captured before the event that destroys it; here the event is the next scoring run.
