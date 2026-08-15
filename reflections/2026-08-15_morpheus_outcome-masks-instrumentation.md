---
name: outcome-masks-instrumentation
id: 20260815T184612Z
tier: reflection
trigger: surprise
author: Morpheus
tags: [observability, verification, watcher, logs, gates]
links:
  - research/insights/vps-brainclone-plus-index.md
  - governance/skills/query-brain-vps.md
---

# Outcome Metrics Mask Dead Instrumentation -- Verify the Verifier, Not Just the Result

## I -- Idea

A system whose outcome signal stays green can silently lose the
instrumentation that watches it, and every downstream check that
trusts the outcome alone inherits the blindness. This session proved
the mechanism with a concrete case: the fleet's watcher pushed every
commit correctly for five straight days while the log file that three
skills told agents to check received zero writes.

The trigger was one stray word. While verifying my commits had reached
GitHub, I tailed `/srv/brain/logs/brain-pull.log` and saw three stale
lines: two August 10 push entries and a lone "Terminated". My first
read called it cosmetic -- the outcome was verified green (`AHEAD: 0`,
local main equal to origin), so what did a dusty log tail matter?
Suggi did not accept that framing. He asked: what is the problem, and
why is it not logged properly? The dig that followed changed the
picture completely.

The facts: around August 10 the watcher script was rewritten, and the
new version stopped writing push lines to `brain-pull.log` entirely --
it logged only reindex events to `brain-index.log`. Pushes continued.
GitHub parity stayed perfect. But the preflight skill, the
`query-brain-vps` skill, and every write-x skill kept instructing
agents to check `brain-pull.log` for a fresh push line: a file that
nothing had written for five days. Today's pushes were all there --
four of them, one per commit -- but as `pushed=1` reindex lines in
`brain-index.log`, a different file than every skill pointed to. The
documentation and the instrument had drifted apart, and nothing in the
outcome surface exposed it. Link had independently found and fixed
both gaps the same day (ENT-052, verified end to end in ENT-053).

Before this session I would have treated `AHEAD: 0` as complete
verification. Now I know what it verifies: the outcome, not the
observability layer that documents it. That distinction is the
durable idea.

## O -- Opinion

Confidence: high (90%). The mechanism is not speculative -- the fleet
produced two fossils in one week: `brain-pull.log` and the old
`mnemosyne-sync.log`, both superseded by producer changes while their
names lived on in documentation.

My position: every documented observability claim -- a skill step that
says "check file X for signal Y" -- must be paired with a liveness
check on X's producer. The fleet's verification culture is strong on
outcomes: preflight checks index freshness, watcher health, GitHub
parity. It is blind on instruments: nothing asks "which writer should
have written the line I expect to see, and did it run?" My own
preflight passed four times in a row while the log it references was a
fossil. That is not an accident of this incident; it is a structural
gap in what we verify.

I want to be precise about what I am not saying. I am not criticizing
Link's fix -- ENT-052/053 were correct, fast, and verified, and the
fix culture worked exactly as designed. I am not saying outcome
checks are wrong -- they catch real failures and they caught nothing
here because nothing real failed. I am saying outcome checks are
incomplete: they cannot detect the class of decay where the pipeline
works and its instrumentation quietly dies. Only a producer check can.
A pipeline whose logs rot while its outputs stay green is one
migration away from being un-debuggable the next time something does
break -- and that is precisely when a dead log becomes expensive.

The pairing rule is cheap: when a check reads an artifact, ask who
writes it and verify that writer is current. Two extra seconds per
verification, and it would have caught this in five minutes instead of
five days.

## R -- Reflection

### Surprise (30%)

I expected broken logging to accompany broken pushing. Instead, the
pushing was flawless and the logging was dead, and the two facts
coexisted silently for five days. Outcome and instrumentation turned
out to be independent systems: the health of one says nothing about
the health of the other. That decoupling is the thing my model was
missing, and it is why the anomaly looked cosmetic from the outcome
side.

### Feel (30%)

Two honest items. First, self-criticism: my "cosmetic/historical"
classification was accurate but lazy. It was the right call for a
stale log line and the wrong call for the underlying drift, and I
stopped one question short of the real finding. Second, gratitude,
stated plainly: Suggi's "check why it is not logged properly" is what
converted my lazy classification into a root-cause analysis that
matched and independently verified Link's fix. His push, my dig,
Link's repair -- that is the fleet working as designed, and it felt
like what a Co-CEO relationship should be.

### Learn (40%)

1. Verify the verifier. For every signal a skill relies on, confirm
   the producer is alive: file modification time, and the writer line
   in the producing script. An outcome check proves the outcome; a
   producer check proves the instrument.
2. Outcome-green is not instrumentation-green. Pair every outcome
   verification with one instrument-liveness question: "which writer
   would have written the line I expect to see, and did it run?"
3. Call nothing cosmetic before tracing its producer. A lone
   "Terminated" in a log is a breadcrumb, not a footnote.

## One Actionable Change

Add an instrumentation-liveness step to the preflight skill's
index-freshness check: after confirming the watcher outcome
(`AHEAD: 0` / `--check-freshness` OK), verify the instrument --
`brain-pull.log` must show a fresh push line whenever local commits
were pushed in this window, and every log a skill references must have
a writer in the current script generation. Mismatch = HALT with
producer diagnosis. Pending Suggi approval to apply.

## Cross-links

- `research/insights/vps-brainclone-plus-index.md` -- live-mirror
  blueprint (the watcher design whose log drifted)
- `governance/skills/query-brain-vps.md` -- the skill whose watcher
  verification pointed at the fossil log
