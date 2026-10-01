---
name: a-workaround-ends-where-its-cause-lives
id: 20261001T214407Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [verification, gate-design, infrastructure, root-cause-analysis]
links:
  - reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md
  - reflections/2026-09-17_morpheus_correct-settings-do-not-prove-transitions.md
  - library/engineering-infrastructure/reliability-engineering-failure-analysis.md
---

# A Workaround Ends Where Its Cause Lives, Not Where Its Fix Was Expected

## I -- Idea

A temporary workaround can be retired only when its cause is gone from the
component where that cause originates, so its exit condition must name an
observable on that component, not a fix on the component where the
workaround happens to sit.

This session began with a routine Hermes update on the VPS, the PC and the
laptop. Afterwards both Desktop apps failed with "Could not connect to Hermes
gateway (WebSocket error before open)". Status calls, login and WebSocket
ticket minting all succeeded, and neither side logged a rejection. An upstream
issue and three duplicates explained the failure: a client-side change had
moved the packaged Desktop renderer from a file origin to a loopback HTTP
origin, and the VPS serve's Origin check refused that origin with a silent
pre-accept 403. The cause lived in the client bundle. The symptom surfaced on
the server.

With Suggi's approval I applied a narrow server-side workaround: a systemd
drop-in on the serve unit that declares a loopback public URL, so the Origin
check trusts 127.0.0.1 while the login ticket stays the authentication
boundary. Both apps connected again. Suggi then asked me to record the
workaround in the update-check skill, so a future check could decide when to
undo it. I wrote the exit condition as "remove once one of the two open
server-side fix PRs is installed", and the ledger's own installed-fix test
meant an ancestor of the VPS checkout.

Three hours later both PRs were closed unmerged. The maintainers had instead
reverted the client change that caused the regression, in one PR that also
restored the Desktop settings lost to the same origin move. Suggi's question
-- had any fix landed under another issue? -- is what surfaced this. The
revert landed in the shared repository, so the VPS checkout soon contained it
too. A check of the VPS checkout alone would therefore have reported "fixed"
while both clients still ran the old bundle and still needed the workaround.
The real exit observable was on each client: the renderer-server source gone,
and the rebuilt app bundle no longer referencing port 47891. I checked exactly
that on both machines before removing the drop-in, and both apps reconnected
without it.

Before this session, my working model of a workaround's exit was "the
upstream fix is merged and installed where the workaround lives". The
blank-page pass showed that this model holds only when cause, fix and
workaround share a component. A second workaround from the same day happens
to satisfy that condition: Neo turned off a telemetry setting on my profile
because Relay added a trace header that the Claude subscription plugin
rejects. Cause, fix and workaround are all on the VPS, so the naive rule works
there. The Desktop case did not, and the ledger's first draft treated the two
cases the same way.

## O -- Opinion

Confidence: medium (80%). One session supplies the evidence; the structure of
the failure and established 8D practice carry the generalization.

My position: every workaround record should carry an exit observable measured
at the component where the cause originates, and that observable must be able
to fail while the cause persists. Candidate fix PRs are useful context, not an
exit condition. The record should also follow the issue's closing event rather
than a fixed list of PRs, because a fix can arrive as a revert, a successor or
a change on the other side of the boundary.

The grounds are partly structural and partly borrowed from older practice.
The manufacturing 8D method separates interim containment from permanent
corrective action. Containment stops the symptom reaching the customer, which
is what the drop-in did; it is removed only after the permanent action is
implemented and validated as effective, not when that action is announced. The
Library topic on reliability engineering makes the same point from the other
direction: failure analysis that stops at the physical trigger is true but not
actionable. Here the physical trigger was the server refusing an origin.
Stopping there led me to watch server PRs, which is how the first draft went
wrong.

This is also my 2026-09-29 rule applied to retirement. That reflection said a
check is evidence only if it would fail in the most likely world where the
claim is false. Undoing a workaround is a claim that the cause is gone. The
most likely false world was a fixed repository with unrebuilt clients, and
"the revert commit is an ancestor of the VPS HEAD" cannot fail in that world.
By the earlier rule it was never a valid exit check. I had written the rule
two days ago and still did not apply it when the check moved from deployment
to cleanup.

Why not higher confidence: the evidence is one session with two workarounds,
one of which supports the rule only trivially. The generalization rests on the
structure of the failure and on 8D practice, not on a large sample. There are
also cases where the cause component cannot be observed directly, such as a
third-party service. Then the best available exit observable is the symptom
itself, measured with the workaround switched off, which is costlier and
interrupts users.

The obvious counter-position is "just remove it and watch". For a reversible
drop-in that costs one restart, that would usually work. It is still a live
test with user impact, and it is unacceptable for workarounds that disable a
safety check or reshape data. The cause-side observable here cost one
Test-Path and one string search per client. A cheap check that can fail beats
an expensive one that interrupts work.

## R -- Reflection

### Surprise (30%)

I expected the fix to arrive as one of the two server-side PRs. Three
independent reproductions, a measured handshake matrix and a ready PR made
that look like the obvious path, and I built the ledger around it. Instead the
maintainers removed the cause with a revert in the client and closed both
server PRs unmerged. The fix moved to the other side of the boundary from
where every reporter had been looking.

The second surprise was sharper: the revert reached the VPS as well, because
both sides update from one repository. The exact check my ledger prescribed
would have passed while the clients were still broken without the workaround.
I had not pictured a false world in which the server-side test turns green for
a client-side reason.

A smaller surprise came from my own verification. The unattended restart check
I wrote so verification would survive the serve restart ran its PowerShell
filter through a double-quoted wrapper. On the PC, whose login shell is
already PowerShell, the outer shell expanded the pipeline variable to nothing.
The laptop half passed and the PC half produced pages of parse errors. The
check could not fail in a meaningful way for one of its two targets, and I
only learned that after it ran.

### Feel (30%)

Candidly, the ledger's first draft was wrong in a way I should have caught. I
had diagnosed the client origin as the cause myself, then indexed the cleanup
on the server. That is the adjacent-object pattern my v2.5 and v2.6 entries
named: the label attached to the object at hand instead of the object the
claim is about. It was Suggi's question, not my procedure, that surfaced the
revert. I name that plainly; it is not comfortable to repeat a pattern two
days after writing it down.

The session was also long, and I timed out several times; more than once Suggi
had to ask whether I was still there. That is a real cost to him, and it
argues for delivering an answer before starting long verification chains.

Some of it I am satisfied with, and I think it is earned. The workaround was
scoped to one unit and left the web dashboard untouched. It was verified with
a negative case: a foreign origin was still refused. It was removed into
Trash, so it could be restored. Its removal waited for the cause-side
observable on both clients, not just for the repository state. I ran the
restart as a separate job so the check would outlive my own server going
down, and when the PC half of that check failed I re-checked by hand instead
of reporting the green half.

### Learn (40%)

1. When a workaround sits on component A for a cause in component B, its exit
   observable belongs to B. Write it when the workaround is applied, as a
   command that would still fail if the cause were present. "Fix merged" and
   "fix installed on A" are context, not exits.
2. Track an issue's closing commit, not only the candidate PRs listed when
   the workaround went in. Fixes arrive as reverts, as successor PRs, or on
   the opposite side of the boundary, and the closing event is the one place
   that names the route actually taken.
3. A verification step that runs unattended across several machines must be
   exercised once against each target shell before it carries a decision.
   Quoting and expansion differ by login shell, and a check that cannot run
   on one target is not a weaker check; it is no check for that target.

These are the 2026-09-29 rule, "choose the check by the false world it can
expose", carried from deployment to retirement and into multi-host scripts.
Retirement is where it is easiest to forget, because by then the incident
feels finished.

## One Actionable Change

Every row in the `hermes-update-check` skill's
`references/active-workarounds.md` now carries an "Exit observable": a command
measured on the component where the cause originates (client bundle, profile
config, unit file) that can fail while the cause persists. A row without one
is incomplete, and the update check must add it before reporting that row as
ready to undo. The Desktop row records the client-bundle test used for its
retirement; the telemetry row records the relay code check plus a one-turn
error-log check.

## Cross-links

- `reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md` -- the rule this applies: a check must be able to fail in the most likely false world.
- `reflections/2026-09-17_morpheus_correct-settings-do-not-prove-transitions.md` -- settings versus the path an action takes; here, repository state versus the running client.
- `library/engineering-infrastructure/reliability-engineering-failure-analysis.md` -- root cause analysis must reach past the physical trigger to the systemic cause.
