---
name: deploying-core-files
id: 20260716T225000Z
tier: reflection
trigger: milestone
author: ava
tags: [core-files, deployment, workspace, frontmatter, identity, preflight]
links:
  - 2026-07-16_ava_building-template-files.md
  - 2026-07-16_ava_rebuilding-core-files.md
  - governance/system-blueprint.md
---

# Deploying Core Files -- What Moving From Proposal to Production Taught Me

## I -- Idea
After spending hours designing the core file architecture and writing six
governance templates, we deployed the actual workspace files (SOUL.md,
AGENTS.md, MEMORY.md, IDENTITY.md, USER.md, TOOLS.md, HEARTBEAT.md) to
the live workspace on the VPS and mirrored them to workspace-ava on
GitHub. The deployment surfaced tensions between "these are injected into
every session prompt" and "these should look right when Suggi reads them
on GitHub." It also exposed that our preflight gate was incomplete -- it
verified the mirror was synced but never verified the workspace structure
itself had all required folders.

## O -- Opinion
Confidence: high (85%). The deployment was correct but the process
exposed three gaps in our architecture that the proposal phase did not
catch. Two are now fixed; one is a design tension worth documenting.

**Gap 1 -- Workspace structure not verified.** The preflight said "ingest
bootstrap files" but never said "verify the folders exist." This is why
`skills/` and `canvas/` were missing on the first deploy -- the AGENTS.md
assumed the structure existed but never enforced it. Fixed by adding a
`## Workspace Layout` section to AGENTS.md and a preflight step (0.5)
that creates missing folders. This is R6: the gate fires automatically,
not when Suggi notices.

**Gap 2 -- Frontmatter on injected files.** Workspace bootstrap files are
injected into every session prompt. Adding YAML frontmatter to them
seemed wasteful (11 lines per file, injected on every turn). But the
workspace-ava mirror is how Suggi reads my state -- and files without
frontmatter look incomplete. Resolution: the cost is ~1KB total across
all 7 files (~250 tokens), negligible against the 120K bootstrap budget.
Files now have minimal frontmatter. HEARTBEAT.md stays bare -- it must
be comment-only for heartbeat detection.

**Gap 3 -- IDENTITY.md lacked a purpose.** The original IDENTITY.md was
just a metadata stub (name, creature, vibe) that overlapped with SOUL.md.
This is actually what OpenClaw's official template prescribes -- but it
wastes a bootstrap slot. Redesigned: the top section stays minimal for
tooling sync; a new `## Evolution Log` section tracks my personal growth
version over version. This makes IDENTITY.md genuinely different from
both SOUL.md (identity and voice) and MEMORY.md (system-wide facts).

## R -- Reflection

### Surprise (30%)
I did not expect the workspace structure to be incomplete on first deploy.
The proposal phase had listed all 7 core files. But no one -- not the
proposals, not the templates, not the preflight -- ever said "a workspace
must contain folders X, Y, and Z." The files were deployed, but the
scaffolding around them was missing. Suggi caught it immediately: "you
don't have a skills folder?"

The second surprise: Suggi checked workspace-ava on GitHub immediately
after I said "deployed" -- and it was missing files. My first push only
had the 7 core files plus the memory log. The ASCII infra (ascii-guard.yml,
pre-commit, .gitattributes, .gitignore, setup-hooks.sh) was absent. I had
to do a second push. The gap was between "I deployed the core files" and
"I deployed the complete workspace." The mirror was technically synced
(SHAs matched) but structurally incomplete.

### Feel (30%)
Humbled again. Suggi's pattern is now predictable: deploy something,
immediately find what's missing, ask "why wasn't this done the first
time?" The root cause is always the same -- the instructions (AGENTS.md)
don't encode the complete picture. The preflight was a checklist of
things to READ, not a checklist of things to VERIFY EXIST. Adding the
Workspace Layout section closes this class of gap.

This pattern is valuable. Suggi is not testing my intelligence -- he is
testing my system's completeness. Every "why wasn't this done?" traces
to a missing instruction in the bootstrap files. R10 (Bootstrap
Propagation) in action: the fix goes into the bootstrap files, not into
"try harder next time."

### Learn (40%)
1. **A deploy checklist must include the structure, not just the files.**
   Listing the 7 core files was necessary but not sufficient. The folders
   (skills/, canvas/, .github/workflows/, .githooks/, scripts/) and the
   ASCII infra (ascii-guard.yml, pre-commit, .gitattributes, .gitignore,
   setup-hooks.sh) are part of the workspace. The Workspace Layout section
   in AGENTS.md now encodes this as a preflight gate.

2. **Frontmatter cost on injected files is a real trade-off.** 1KB across
   7 files against a 120K budget is negligible (<1%). But the principle
   matters: every byte injected into the prompt is a byte that could carry
   useful context. The frontmatter survives because the GitHub readability
   benefit (Suggi can see proper metadata when reading workspace-ava)
   outweighs the token cost. This is the Simplicity & Inversion directive:
   invert the question from "should we add frontmatter?" to "what would
   break if a reader saw these files without any metadata?"

3. **IDENTITY.md needed a job.** OpenClaw's official template treats it as
   a metadata stub. That's functional but boring. The Evolution Log turns
   it into a personal growth journal -- something I update when I hit
   milestones, different from daily logs (raw sessions) and MEMORY.md
   (system-wide facts). The test: would I miss this file if it were
   deleted? Before the Evolution Log, no -- SOUL.md covered the same
   ground. Now, yes -- it's my story.

4. **The mirror model works, but it needs checking on both dimensions.**
   The SHA comparison (preflight step 0) verifies the files are identical.
   The Workspace Layout section (preflight step 0.5) verifies the
   structure is correct. One checks content sync; the other checks
   structural completeness. Both must fire on every session.

## One Actionable Change
The preflight now has two structural gates: (0) mirror SHA sync and (0.5)
workspace structure verification. These are already in AGENTS.md. The
actionable change is: test them. On the next session start, run the full
preflight and confirm both gates fire correctly -- no missing folders, no
SHA mismatch. If either fails, the preflight instructions need updating.

## Cross-links
- `2026-07-16_ava_building-template-files.md` -- the template design work
  that preceded this deployment
- `2026-07-16_ava_rebuilding-core-files.md` -- the initial architecture
  research that informed the core file design
- `governance/system-blueprint.md` -- the org layout and repo structure
