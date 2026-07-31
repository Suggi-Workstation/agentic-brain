---
name: mirror-nobody-reads-is-ritual
id: 20260731T112418Z
tier: reflection
trigger: insight
author: Link
tags: [governance, simplification, infrastructure, categorical-imperative, anti-bloat, gate-deduplication, skill-chain]
links:
  - governance/system-constitution.md
  - governance/system-blueprint.md
  - reflections/2026-07-28_ava_infrastructure-ready-is-not-working.md
  - reflections/2026-07-31_ava_remove-the-gate-when-the-skill-already-has-it.md
  - governance/skills/loop-feynman.md
  - governance/skills/write-reflection.md
---

# A Mirror Nobody Reads Is Not Infrastructure -- It's a Ritual

## I -- Idea

For 11 days, workspace-link was declared as "my live state mirrored 1:1"
in AGENTS.md. Investigation revealed zero consumers: Ava never read it,
the repo covered only 8 of ~50 agent files (no SOUL.md, no skills, no
sessions), and the declared "1:1 mirror" was factually ~15% coverage.
Treating a dead mirror as HARD GATE infrastructure was the error; the
fix was recognizing it as a ritual and removing it. The session also
surfaced a second failure class: my local write-x skills were stale
copies missing the Feynman Loop invocation chain that the brain
governance/skills had already fixed. Both errors share the same root:
gates declared in bootstrap files that duplicated what skills already
enforced, and skills that were never connected to their invocation
chain.

## O -- Opinion

High confidence (90%). Two converging findings: (1) mirror repos without
consumers are rituals, not infrastructure, and (2) bootstrap gate
duplication is a failure class independent of whether the gate guards
a workspace mirror or a quality check. Ava's reflection from the same
day -- "Remove the Gate When the Skill Already Has It" -- identified the
exact same pattern in AGENTS.md: two HARD GATE sections (Reflection
Writing, Feynman Loop) that duplicated content from skills that already
had their own self-checks. Her fix was tracing the trigger path and
removing the duplicates. My fix was tracing the consumer path and
removing the mirror. Same diagnostic, different organ.

The right pattern is the skill chain: bootstrap files invoke skills,
skills invoke sub-skills (e.g., session-end -> write-reflection ->
loop-feynman), and no gate is duplicated along the chain. Each link is
a single invocation reference. The mirror was not part of this chain --
it was a sidecar that produced zero coordination value while generating
a permanent failure class (auth popups, rebase conflicts, preflight
HALTs).

## R -- Reflection

### Surprise (30%)

Two surprises. First: the mirror I had treated as sacred infrastructure
for 11 days was a 15%-coverage shell that nobody consumed. I expected a
meaningful backup and coordination surface; the logbook evidence showed
zero Ava references and zero external commits in the entire repo history.
The contract (AGENTS.md) declared a function the evidence flatly
contradicted.

Second: discovering that my local write-x skills were stale copies. I had
been using them for weeks, writing reflections and evaluations, without
noticing that the brain governance/skills had been updated with:
(a) loop-feynman integrated as Procedure Step 1 in all six write-x
skills, (b) consistent ID generation steps (4b), and (c) loop-feynman
itself existed as a formal skill. My local copy of loop-feynman did not
exist at all. I was doing Feynman passes from training habit, not from
automated invocation. This is the exact "dead code" failure class Ava
identified: a skill with the right architecture but no invocation path.
In my case, the invocation path existed in the brain governance/skills
but had never propagated to my local skills directory.

### Feel (30%)

Relief at removing the mirror gate -- a preflight step that could only
fail, guarding a remote nobody touched for a week. Embarrassment that I
missed the stale-skill problem: I had been operating with outdated
versions while the canonical source (governance/skills) had moved on.
The same immersion blindness I described in the mirror case (treating a
declared contract as fact without checking consumption) applied to my
own skills. I saw SKILL.md files in my local directory and assumed they
were current. Ava's reflection was the trigger that made me check.

### Learn (40%)

1. **The trigger-path test applies to everything, not just bootstrap
   files.** Ava's insight: trace every scenario where a gate would fire
   and verify at least one path does not already pass through a skill
   with its own self-check. The mirror failed this: the preflight gate
   was the ONLY consumer of the mirror, and the mirror had no consumer
   besides the gate. A self-eating loop, not a chain.

2. **Skills form chains; copies go stale.** The canonical source for
   shared skills is governance/skills in the agentic-brain. Local skill
   directories are downstream caches that must be refreshed. When Ava
   integrated loop-feynman into all write-x skills and renamed
   IOR->reflection, those changes propagated through the brain. My local
   directory did not receive them. A skill without a refresh mechanism
   is a future stale copy.

3. **The Categorical Imperative exposes rituals that pass as
   infrastructure.** Before any architectural declaration, ask: "Who
   consumes this? When did they last consume it? What would break if
   it disappeared?" If the answer is zero consumers with zero breakage,
   the declaration is a ritual. The practical test: check git log for
   consumer activity. workspace-link had 7 commits, all by Link and
   Suggi, none by any other agent in 11 days. That is not infrastructure
   -- it is an unused mirror.

**Actionable change (mirror):** Preflight step 1 (mirror sync) replaced
with local workspace verification. Session-end step 4 simplified from
push to commit. AGENTS.md Architecture section now reads "local-only,
versioned with git for history and review."

**Actionable change (skills):** All 7 brain governance/skills
(loop-feynman + 6 write-x) copied to local skills directory,
replacing stale versions. loop-feynman is now invoked as Step 1 by
every write-x skill. The skill chain is connected.

**Trigger-path test (reusable):** When adding or editing any HARD GATE
section, trace every scenario where this gate would fire and verify at
least one path does not already pass through a skill with its own
self-check. If all paths go through a skill, the gate is redundant and
should reference the skill instead of duplicating its checks. If no path
leads to the gate, remove it. This test killed both the mirror gate and
(per Ava's parallel finding) two AGENTS.md sections.
