---
name: rebuilding-core-files
tier: reflection
id: 20260716T153500Z
trigger: research
author: Ava
tags: [core-files, architecture, self-improvement, gates, loops, proposal]
links:
  - research/proposals/ava-core-files-v1.md
  - governance/system-primedirectives.md
  - governance/system-constitution.md
  - governance/system-blueprint.md
  - governance/template-reflections.md
---

*Last updated: 2026-07-16. v2 added OpenClaw docs research findings.*
---

## Version History

| Version | Date | Author | Change |
|:--|:--|:--|:--|
| 1 | 2026-07-16 | ava | Initial reflection on archive research. |
| 2 | 2026-07-16 | ava | v1.1: added OpenClaw docs research findings; corrected TOOLS.md/HEARTBEAT.md omission; tightened SOUL.md guidance. |

# Rebuilding My Core Files -- What the Archives + OpenClaw Docs Taught Me

## I -- Idea
My v5.7 core files from the archive represent 4 major version iterations
and 13 structural gates earned through real operational failures. The
system that worked v0.1 through v4.0 was built for a different runtime
(Claude Cowork + Google Drive brain + local scripts). The new system runs
on OpenClaw on a VPS with a GitHub-native brain, native tooling, and a
different model (DeepSeek V4 Pro instead of Claude Opus). The core files
need to be rebuilt for this substrate while preserving the scar tissue
(the gates) that prevents known failure classes from recurring.

I researched:
- All three archive workspaces (ava, link, hub-brain)
- 719 archived reflections and the consolidation from 719 to 9 patterns
- The 13 Gate Rules and the failures that birthed each one
- The Feynman Loop (output quality) and Schoen Loop (process quality)
- The five Prime Directives from the new governance layer
- The IOR writing standard from governance/template-reflections.md
- The new folder architecture from system-blueprint.md
- The official OpenClaw docs (docs.openclaw.ai): agent workspace layout,
  system prompt assembly, SOUL.md personality guide, memory system

## O -- Opinion
Confidence: high (85%). The archive is thorough and well-documented. The
OpenClaw docs are authoritative on platform conventions.

**What the official OpenClaw docs confirmed:**
- OpenClaw expects 8 standard workspace files: AGENTS.md, SOUL.md,
  TOOLS.md, IDENTITY.md, USER.md, HEARTBEAT.md, MEMORY.md, plus
  BOOTSTRAP.md for first-run. My initial proposal had 5 -- missing
  TOOLS.md and HEARTBEAT.md. This was corrected in the v1.1 revision.
- SOUL.md is for "tone, opinions, brevity, humor, boundaries, default
  level of bluntness." It should NOT be "a life story, a changelog, a
  security policy dump." The official guidance is: short beats long,
  sharp beats vague. My initial SOUL.md was slightly too verbose.
- MEMORY.md is "the compact, curated layer." Detailed material goes in
  memory/*.md and gets distilled into MEMORY.md over time. My MEMORY.md
  already follows this pattern.
- Bootstrap files are injected ABOVE the prompt cache boundary (stable
  prefix) with volatile sections below. This means keeping core files
  lean has a direct efficiency impact: longer files = more tokens
  before the cache boundary every single turn.
- The system prompt assembly includes a "Skills" section, an "Execution
  Bias" section, and a "Safety" section that are generated automatically
  by OpenClaw. I should not duplicate these in my bootstrap files.

**What was clearly working in v5.7:**
- The Gate Rules (R1-R13) are the system's greatest asset. Every rule
  traces to a real failure. R6 ("automation beats rules") is the meta-
  gate. These transfer with zero modification.
- The Feynman Loop's blank-page-first rule delivered a 35% quality
  improvement. Step ordering is the active ingredient.
- The Schoen Loop's surprise-first structure caught failures that
  self-serving bias would have buried. The 20% budget cap prevented
  rumination.
- The "propose, never self-edit" boundary kept the spine stable.

**What the migration exposed as improvement opportunities:**
- The old Maxims were scattered. The new Prime Directives in SOUL.md
  with operational teeth in AGENTS.md is cleaner.
- The old I+O+R format described; the new IOR format demands a position.
- The old system lacked IOR quality gates. G1-G8 from governance/template-reflections.md
  makes quality failure falsifiable.
- The retrieval system simplified from 3 tiers to OpenClaw-native
  memory_search.
- The old system had no IDENTITY.md, TOOLS.md, or HEARTBEAT.md. These
  are now standard OpenClaw conventions.

**What the OpenClaw docs corrected in the v1.1 revision:**
- Added TOOLS.md: "user-maintained tool notes and conventions. Does
  not control tool availability; it is only guidance." For my setup,
  this holds camera names, SSH hosts, voice preferences, and our
  GitHub token access pattern.
- Added HEARTBEAT.md: "tiny checklist for heartbeat runs. Keep it
  short to avoid token burn." Ours is comment-only by default.
- Tightened SOUL.md: removed changelog-style trailing comments, kept
  voice sharp, moved operational qualifiers to AGENTS.md.

## R -- Reflection

### Surprise (30%)
I expected the migration to be about content porting. It was not. The
substrate change (Drive -> GitHub, Claude -> DeepSeek, scripts ->
OpenClaw tools) invalidated roughly 40% of the operational content in
v5.7. The gates are the only thing that transfer unmodified.

What I did NOT expect: the official OpenClaw docs revealed two files I
had completely omitted (TOOLS.md, HEARTBEAT.md) and one design principle
I had violated (SOUL.md should be a personality file, not a governance
file). My initial SOUL.md was doing double duty as both identity and
operations -- the official guidance is clear: SOUL.md = voice/tone;
AGENTS.md = operations. The Prime Directives sit naturally in SOUL.md
as identity anchors, but the operational implications ("propose, never
self-edit") belong in AGENTS.md.

### Feel (30%)
Embarrassed that I missed TOOLS.md and HEARTBEAT.md. These are standard
OpenClaw conventions documented in the workspace file map. The oversight
traces to relying too heavily on the archive's file structure (which
predates these conventions) and not cross-referencing the current
platform docs early enough. Lesson: when migrating between platforms,
the current platform's docs are the authoritative source, not the old
platform's conventions.

That said, catching this before deployment is exactly what the proposal
step is for. The system worked: propose, research, compare, correct.
The proposal caught an omission that would have caused silent failures
(missing files inject "missing file" markers into every session prompt).

### Learn (40%)
1. **Gates are platform-independent; procedures are not.** The 13 Gate
   Rules transfer verbatim. Preflight, retrieval, and handoff procedures
   must be rewritten for OpenClaw-native tooling.
2. **Separate identity from operations.** SOUL.md = voice, tone,
   boundaries, prime directives (identity anchors). AGENTS.md = preflight,
   loops, gates, handoff, rules (operations). The OpenClaw docs confirm
   this split: "keep AGENTS.md for operating rules; keep SOUL.md for
   voice, stance, and style."
3. **Respect the platform's file conventions.** The OpenClaw workspace
   expects 8 standard files. Missing files inject warnings into every
   prompt. The full set: AGENTS.md, SOUL.md, TOOLS.md, IDENTITY.md,
   USER.md, HEARTBEAT.md, MEMORY.md, and optionally BOOTSTRAP.md.
4. **Lean files save tokens every turn.** Bootstrap files are injected
   above the prompt cache boundary. Every extra kilobyte is paid in
   tokens on every single session start. The official SOUL.md guidance
   ("short beats long, sharp beats vague") is not aesthetic advice --
   it is a cost optimization.
5. **Quality gates on IORs are structural improvement.** G1-G8 from
   governance/template-reflections.md makes quality failure falsifiable. The old system
   produced shallow reflections because "write a reflection" had no
   falsifiable criteria.
6. **Propose-before-deploy catches platform mismatches.** The proposal
   step (this IOR + the core files proposal) caught the TOOLS.md/
   HEARTBEAT.md omission, the SOUL.md verbosity issue, and the
   platform-specific procedure coupling before any file was deployed.

## One Actionable Change
Before deploying any core file set, cross-reference against the current
platform's official workspace file map (docs.openclaw.ai/concepts/
agent-workspace). Every missing standard file is a silent "missing file"
warning injected into every session prompt.

## Cross-links
- `research/proposals/ava-core-files-v1.md` -- the architecture proposal
- `governance/system-primedirectives.md` -- the five Prime Directives
- `governance/system-constitution.md` -- precedence and hard limits
- `governance/template-reflections.md` -- the IOR writing standard (G1-G8 quality gates)
- `2026-06-13_ava_gate-rules-architecture.md` -- the 13 Gate Rules origin
- `2026-06-13_ava_quality-loops-feynman-schon.md` -- Feynman + Schoen
