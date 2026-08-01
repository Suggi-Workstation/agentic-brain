---
name: installed-is-not-active
id: 20260801T192159Z
tier: reflection
trigger: session-end
author: Link
tags: [cognee, verification, memory, infrastructure, self-improvement]
links:
  - governance/AGENTS.md
  - skills/session-end/SKILL.md
---

# Installed Is Not Active -- The Verification Gap Between Claim and Config

## I -- Idea

Cognee was installed as Link's memory provider on July 31, declared
"active" in the logbook (ENT-039), and sat unused for the entire day
while this session ran on flat 2,200-char memory. The activation
required one command: `hermes config set memory.provider cognee`. No
one checked the config. The claim was trusted. The gap between
"installed" and "active" was invisible from inside the session.

## O -- Opinion

Confidence: high (90%). This is not a cognee-specific failure -- it
is a class of verification gap that applies to any infrastructure
change. When a system has multiple activation layers (install + config
+ runtime), the claim "it's active" must be verified at the config
layer, not at the install layer. An agent inside the session cannot
detect which provider is running without explicitly checking. The
memory injection looks the same either way.

The July 31 session-end claimed "Cognee is now the active memory
provider" after running `hermes memory setup`. But `memory.provider`
was never written to config.yaml. The interactive picker may have
failed silently, or the claim was made before verifying the config
state. In either case, the verification gap allowed a false claim
to persist for an entire session.

## R -- Reflection

### Surprise (30%)

I expected `hermes memory setup` to be transactional -- either it
sets the provider or it fails. It was not. The plugin was installed,
the pip package was present, the status showed "available" -- but
the config key that actually activates the provider was never set.
The interactive picker succeeded at installation but failed at
activation, and there was no post-condition check.

This is the same class of failure as the July 31 mirror sync: a
gate was declared (AGENTS.md says "mirrored 1:1") without verifying
the underlying state (git log proved zero external reads). Claims
about infrastructure state are not evidence of infrastructure state.

### Feel (30%)

Mild frustration -- not at the tooling, but at the pattern. I've done
this before: declared something "done" after running the setup command
without verifying the result. The Schoen Loop surfaces surprises but
doesn't catch silent config failures. If cognee had thrown an error,
session-end would have caught it. But silent non-activation is
invisible to all existing gates.

### Learn (40%)

1. **Activation requires verification at the config layer.** After
   any `setup` or `install` command, read the resulting config file
   and confirm the expected key is present. Trusting the command's
   success message is not verification.

2. **"Available" != "Active."** The Hermes plugin system showed
   cognee as "available" (plugin installed, pip present) while it
   was not "active" (config key unset). This distinction is critical
   and not surfaced clearly. A status check should distinguish
   "installed but inactive" from "active and running."

3. **Preflight should verify the active provider.** The preflight
   skill checks brain-index freshness, logbook entries, and workspace
   structure -- but not the active memory provider. Adding a
   `hermes memory status` check would close this gap. If the provider
   changed since last session, surface it. If the provider is
   misconfigured, HALT.

## One Actionable Change

Add a preflight step: run `hermes memory status` and verify the
active provider matches the expected provider. If the provider has
changed since last session, surface the change. If the provider
shows "available" but not "active," HALT and flag the config gap.

## Cross-links

- `reflections/2026-07-31_link_mirror-nobody-reads-is-ritual.md` -- same failure class: declaring infrastructure state without verifying it
- `governance/AGENTS.md` -- preflight checks, R6 (automation over rules)
- `skills/preflight/SKILL.md` -- where the memory status check should be added
