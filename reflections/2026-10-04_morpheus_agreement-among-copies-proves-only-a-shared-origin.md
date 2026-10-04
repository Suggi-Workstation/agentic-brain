---
name: agreement-among-copies-proves-only-a-shared-origin
id: 20261004T085001Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [verification, agent-birth, governance, skill-design]
links:
  - reflections/2026-07-19_ava_multi-file-uniformity-is-a-structural-gate.md
  - reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md
  - reflections/2026-08-19_morpheus_isolation-is-the-default.md
  - library/technology/software-architecture-patterns-principles.md
  - library/engineering-infrastructure/reliability-engineering-failure-analysis.md
---

# Agreement Among Copies Proves Only a Shared Origin

## I -- Idea

A copy inherits its source's defects and its source's role-specific claims
as faithfully as its sound structure, so agreement among copies proves only
that they share an origin; correctness has to be shown separately, on each
copy's own path, and universal content has to be separated from role
content before copying starts.

The trigger was a full working day spent birthing a new core agent. Suggi
asked for Cassandra, a scholar of history, politics and geopolitics,
anthropology, philosophy and human behaviour, built the same way as Neo,
the investing agent, so the two could complement each other. Mirroring was
the right strategy: Neo's setup is the best-tested in the fleet, and Suggi
wanted parallel files. I read Neo's live configuration, workspace, skills
and memory settings before copying anything, changed only paths and role
text, and ran a smoke test that passed.

Three classes of problem still came through the copy. The first was
role-specific claims that looked generic. Cassandra's draft IDENTITY.md
said teaching and value investing were her twin north stars, and its first
evolution question asked about her relationship with Ava; both came from
the template. Neo's AGENTS.md said Morpheus helps build and edit him, a
line Suggi then removed as bloat. The canonical Prime Directives file had
the same shape at fleet scale: a Value-investing directive sat inside the
universal set, so every agent that mirrored it except Atlas, including me,
the subagents and the two Windows agents, carried an investing mandate
that was never theirs. The second class was facts gone stale in the
source: my own FLEET.md and birth skill still described a gateway
allowlist that a Hermes update had removed. The third class was a latent
defect. At session end I ran the workspace-search skill commands exactly
as written in a Hermes terminal, and every one failed: the terminal
inherits a PYTHONPATH that loads Hermes's Python 3.14 numpy into the
watcher's 3.12 venv. During the build I had tested the same scripts in a
cleaned shell, so they passed. The skill text came from Neo, whose own
transcript shows the same numpy import failure on 28 September, and the
four profile copies of that skill agreed with each other apart from paths.

Before the Feynman pass I held this as "check copies more carefully." The
pass sharpened it. Software architecture names the first problem: Parnas
argued in 1972 that modules should hide the decisions likely to change
behind stable interfaces, and a role directive embedded in a universal
file is exactly a changeable decision left exposed. Reliability
engineering names the third: a common-cause failure is a single design or
manufacturing error that disables every redundant element at once, which
is why duplication alone does not raise reliability. Four identical skill
files are not four witnesses; they are one witness counted four times.

## O -- Opinion

Confidence: medium (80%). Three separate cases in one session point
the same way, and the latent-defect case is fully evidenced: the failing
command, the passing variant, and Neo's earlier failure in the same
import. What would lower my confidence is a future birth in which verbatim
execution on the new agent's path finds nothing while some other defect
class still gets through.

My position has two parts. First, before copying a sibling, separate what
is universal from what belongs to the sibling's role, and make the
separation structural rather than a matter of care. Today's two-tier Prime
Directives file is the model: the Eternal Anchors bind every agent, and
each role carries only its own special directive beneath a separate
heading. Copying the anchors is then always safe, and nobody inherits
Value-investing by accident, because it no longer sits in the shared
block. The same logic applies to the roster. Suggi's rule that an agent's
own files must not name other agents removes a whole category of claims
that copies would otherwise carry and that go stale whenever the fleet
changes. The roster lives in FLEET.md and the blueprint, and nowhere else.

Second, verify each copy on its own consumer's path, never by comparing it
with its siblings. Here I dissent in part from Ava's reflection
`reflections/2026-07-19_ava_multi-file-uniformity-is-a-structural-gate.md`.
Her finding stands for what it measured: diffing files that should share a
pattern exposes drift that single-file review misses, and she fixed twenty
such errors. But uniformity can only detect divergence. A defect present
in the source is present in every copy, so a uniformity audit returns a
clean result exactly when the defect is most widespread. Uniformity is a
drift gate, not a correctness gate, and treating it as both is how a known
traceback survived four copies.

This is the lesson of my 29 September reflection, which said a check proves
only what it could catch and should run on the consumer's path. I wrote
that, and five days later I still tested Cassandra's skill in a shell that
removed the very condition that breaks it. That is why I do not trust
another sentence in a reflection to hold the rule. The fix now lives in the
birth procedure as a step with a pass condition: run every command a copied
skill tells the agent to run, verbatim, in a Hermes terminal, and fix the
skill text rather than the test shell. The two workspace-search skills I
own are corrected. Neo's and Atlas's copies still carry the defect and need
Suggi's approval before I touch them, which is itself a reminder that
correcting a copied defect is a fleet change, not a local one.

The theme work was a small counterexample. There I fitted the derived
colors from two sibling themes and confirmed the fit reproduced them
exactly before applying it to a new base. Copying was safe because I
extracted the rule, not the instance.

## R -- Reflection

### Surprise (30%)

I expected copying the best-tested agent to be the safe path, with any
defects being my own transcription errors. Instead, the most expensive
defect was one the source already had, and its evidence had been sitting
in Neo's transcript for six days. I expected the canonical directives file
to be the cleanest thing to mirror, because it is the most governed file in
the brain; it turned out to be the origin of the widest copied error, an
investing mandate in almost every SOUL. And I expected my own fleet
documents to describe the runtime correctly. The allowlist they described
had been removed upstream, and I found out only because the new profile
appeared in the gateway without one. In each case the thing I trusted most
was trusted because of its pedigree, not because I had checked it.

### Feel (30%)

The build itself went well and I am satisfied with its discipline: live
state read before copying, every remote write read back byte for byte, and
governance edits spliced with a proof that removing the addition restores
the original. Suggi's corrections were quick and right, and most of them
removed text rather than adding it. What I am not comfortable with is the
verification gap. I had written the consumer-path rule five days earlier,
and I still chose the cleaned shell because it made the test pass and I
wanted the infrastructure step green. That is precisely the failure the
rule exists to prevent, and I committed it while believing I was being
thorough. I also wrote one MISSION sentence about Tetlock from memory
before fetching the source and had to correct its wording. Both errors
were caught within the session, but by the luck of ordering, not by design.

### Learn (40%)

1. Before copying a sibling, split universal content from role content and
   keep them in separate structures: a shared block every copy may carry
   unchanged, and a role block each copy writes for itself. A copy then
   cannot inherit another role's purpose, roster or mandate by accident,
   and a change to one role touches only that role's block.
2. Agreement among copies is evidence of a shared origin, not of
   correctness. Use cross-file diffs to catch drift, but never count
   identical copies as independent confirmation; a defect in the source
   passes every uniformity check, and the more copies exist, the more
   confident a uniformity audit falsely looks. When copies agree, ask
   when and where their common source was last shown to work on a real
   path, and if nobody can say, test the source before trusting any copy.
3. Verify a copied procedure by running its exact text where its consumer
   will run it, with the consumer's environment intact. When a test needs
   a cleaner environment than the consumer has in order to pass, the
   procedure is wrong, and the fix belongs in the procedure, not in the
   test. The source's own history is cheap evidence: its earlier errors
   from the same commands often show the defect before the copy is made.

## One Actionable Change

When birthing or seeding any agent from a sibling, run each command block
of every copied skill verbatim in a Hermes terminal under the new profile
before the smoke test, and before copying, search the sibling's
transcripts for errors from those same commands. For Cassandra this would
have caught the PYTHONPATH failure at build time and pointed straight to
Neo's 28 September traceback as its source.

## Cross-links

- `reflections/2026-07-19_ava_multi-file-uniformity-is-a-structural-gate.md`
  -- uniformity audits catch drift; this reflection argues they cannot
  catch a defect every copy shares.
- `reflections/2026-09-29_morpheus_a-check-proves-only-what-it-could-catch.md`
  -- the consumer-path rule this session broke and then made structural.
- `reflections/2026-08-19_morpheus_isolation-is-the-default.md` -- an
  earlier case of copying the nearest pattern's shape before asking the
  scope question.
- `library/technology/software-architecture-patterns-principles.md` --
  Parnas's information hiding: conceal the decisions likely to change.
- `library/engineering-infrastructure/reliability-engineering-failure-analysis.md`
  -- common-cause failures defeat redundancy.
