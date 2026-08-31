---
name: stateful-runtime-upgrade-is-a-data-migration
id: 20260831T111334Z
tier: reflection
trigger: surprise
author: Morpheus
tags: [openclaw, migration, verification, infrastructure, trust-boundary]
links:
  - research/reports/openclaw-server-migration.md
  - reflections/2026-08-20_morpheus_terminal-cwd-gateway-restart.md
  - reflections/2026-08-27_morpheus_stale-code-refusal-is-not-a-bug.md
  - reflections/2026-08-31_neo_verification-must-precede-the-claim.md
---

# A Stateful Runtime Upgrade Is a Data Migration, Not a Package Replacement

## I -- Idea

A stateful agent-runtime upgrade must be designed and verified as a data migration across every live boundary, not as a package replacement followed by a version check.

My blank-page model at the start of this work was simpler. OpenClaw was installed globally under the `openclaw` Linux user, its durable state lived under `~/.openclaw`, and its Gateway ran from a user-level systemd unit behind Tailscale Serve. I expected the job to have four parts: identify the official OpenClaw 2.0 release, audit the package, install it as the correct user, and confirm that the Gateway reported the new version. I knew plugins might need updates and that a restart would be necessary. I did not yet model the upgrade as a coordinated transition among database schemas, plugin ownership, capability consent, memory engines, session stores, process working directories, and reverse-proxy attribution.

The first gap appeared during what I believed was a read-only compatibility probe. I ran a staged OpenClaw 2.0 CLI against the live OpenClaw 1.x state with a plugin update dry-run. The subcommand promised a preview, but process startup happened before the subcommand. Startup detected an old shared-state schema and migrated it to schema 15. The old CLI could no longer open that database. The dry-run was read-only only inside the update command; it was not read-only across the process bootstrap that preceded the command. That distinction converted an exploratory probe into an irreversible forward dependency: completing the core upgrade was now required to restore a restartable system.

The next gaps exposed other boundaries. Doctor needed exclusive ownership to import legacy exec approvals, so the Gateway had to stop. Doctor then failed with `EACCES`, not because Ava's files had the wrong ownership, but because `sudo -u openclaw` preserved Morpheus's private working directory and child processes attempted to return to a path they could not traverse. The core package succeeded, but OpenClaw 2.0 externalized providers that older releases bundled, so package readiness depended on plugin package installation, capability consent, and artifact-bound verification. Lossless Claw loaded but its prompt hook was blocked until conversation access was explicitly granted. QMD was retired as a memory backend, so the correct replacement required a verified embedding-only llama.cpp service and a full rebuild of all three configured agent indexes.

The final gap was the most important because it survived every local green check. The Gateway was active. Local HTTP returned 200. RPC reported version `2026.8.1`. The plugin inventory was clean. Tailscale Serve still mapped the root path to `127.0.0.1:18789`. I called the upgrade complete. Suggi then opened the exact browser URL and received `proxy_attribution_required`. OpenClaw 2.0 had strengthened reverse-proxy attribution; the established loopback Serve proxy now required explicit trust of `127.0.0.1`. The route existed, but the user's path failed. The completed migration was not merely package plus database plus plugins plus memory. It also included the ingress trust contract that connected the user to the service.

## O -- Opinion

Confidence: high (95%). My position is that the minimum unit of an agent-runtime upgrade is the entire operational path from signed artifact to durable state to the human's exact entry point. A version string is necessary evidence, but it is weak evidence. A process can report the target version while its database is half-migrated, a critical plugin is consent-blocked, semantic memory is paused, or the reverse proxy rejects every real browser request. Calling that system upgraded is a category error.

This position extends, rather than replaces, prior brain work. `research/reports/openclaw-server-migration.md` established that OpenClaw state is distributed across config, credentials, sessions, plugin state, memory indexes, systemd, package code, and Tailscale. That report studied moving machines; this session showed that a major in-place release crosses many of the same boundaries. `reflections/2026-08-27_morpheus_stale-code-refusal-is-not-a-bug.md` established that the running build, not the disk checkout alone, determines behavior after an update. Here the same principle applied to schemas and plugin generations: installed files were not proof that the running Gateway had converged. `reflections/2026-08-20_morpheus_terminal-cwd-gateway-restart.md` established that a correct config file is not proof that a running process has consumed it. Here even the caller's cwd became a hidden process dependency during migration. Neo's `verification-must-precede-the-claim` reflection states the communication boundary directly: a verdict must wait for the discriminating probe.

The resulting verification model should have four layers. First, artifact integrity: official source, exact version, registry hash, signatures, attestations, malware scan, lifecycle code, and dependency audit. Second, migration integrity: database schemas, config rewrite, legacy-source receipts, state ownership, and clean removal only after read-back verification. Third, component convergence: core, plugins, capability consent, memory engines, session stores, systemd, and loaded-build identity agree. Fourth, user-path verification: make the same request the human makes through the same hostname, proxy, auth boundary, and route. Each layer catches a different failure class. Passing one cannot substitute for another.

I also think the word "dry-run" must always carry an explicit scope. A dry-run option belongs to a subcommand; it says nothing about import-time code, startup migrations, plugin discovery, or config normalization unless the program documents those phases as read-only too. The safe assumption for a newer stateful binary is the inverse: process startup may mutate. Therefore a staged newer CLI must never touch older live state merely to preview an update. Preview through the installed CLI, use an isolated copy of state, or run a documented migration dry-run whose ownership includes startup.

The worst-case inversion supports this standard. The worst outcome is not that installation fails loudly. It is that the package update succeeds, state partially advances, the old binary becomes unable to recover, and local probes still look healthy enough to justify a false completion claim. That combination narrows rollback while hiding user-facing failure. The defense is not more confidence or more commands. It is ordering: audit first, isolate previews, migrate under exclusive ownership, verify each state transition, and end with the user's exact URL. This standard is slightly slower than `npm install` plus `--version`, but it is dramatically cheaper than repairing a state split after telling the operator the job is done.

## R -- Reflection

### Surprise (30%)

I expected the new package to be the risky part, but the package was the most straightforward component. It installed in seconds after hashes, signatures, attestations, ClamAV, lifecycle code, and dependencies had been checked. I did not expect a dry-run subcommand to advance the live database before showing its preview. I expected Doctor's permission error to point at Ava's state ownership, but strace showed that the inaccessible object was Morpheus's inherited cwd. I expected plugin status `loaded` to mean fully functional, but Lossless Claw's prompt hook remained blocked by a separate conversation-access policy. I expected the unchanged Tailscale Serve map and local HTTP 200 to prove the browser path, but OpenClaw 2.0 added a proxy-attribution contract that the old architecture had never authored. Every surprise came from a boundary outside the package itself.

The largest surprise was the asymmetry between local correctness and human correctness. I had strong evidence: RPC build identity, systemd stability, config validity, plugin convergence, zero diagnostics, and three clean semantic indexes. Yet Suggi could not open the UI. That means the evidence set was broad but still incomplete. The user's exact request path was not an optional acceptance test; it was the final system boundary.

### Feel (30%)

I am proud of the recovery discipline and dissatisfied with the premature completion claim. Once the staged CLI advanced the schema, I did not invent output or hide the change. I stopped, inspected source, preserved the legacy approvals file until its SQLite import was verified, traced the permission error with strace, audited each plugin artifact before consent, and kept working through the long memory rebuilds. The system ended stronger than it began: current schemas, current plugins, semantic memory restored, Lossless hooks active, and Tailscale access repaired.

But Suggi should not have needed to tell me that `BOX.md` already documented the route. I had read that file during preflight and still treated the route's existence as sufficient proof instead of using the living architecture map to construct the real acceptance test. The error was not lack of effort; it was the wrong terminal condition. I stopped when the components agreed with one another, not when the human path worked. That is precisely the kind of gap R20 warns about: a gate must verify every dimension of its claim.

### Learn (40%)

1. A stateful runtime upgrade is a migration graph. The nodes are code, schemas, config, plugins, capabilities, memory, process supervision, and ingress. Completion requires every edge to converge.

2. Dry-run is scoped, not absolute. Never expose live older state to a newer staged binary unless startup and import phases are explicitly documented as read-only.

3. User switching does not imply environment switching. Identity, cwd, HOME, PATH, state directory, and service lock ownership are separate inputs and must be verified independently.

4. Component health is not service availability. The final probe must traverse the exact hostname, proxy, auth method, path, and browser route used by the human.

5. Living architecture files are executable context. If `BOX.md` says Tailscale Serve fronts the root path, the verification plan must include that root path before any completion claim.

## One Actionable Change

For every future OpenClaw major upgrade, execute the personal `vps-agent-runtime-hosting/references/openclaw-2-upgrade.md` gate as the acceptance contract: preview only with the installed CLI or isolated state; audit exact artifacts; migrate under exclusive ownership from an accessible runtime-user cwd; converge plugins and memory; verify loaded hooks and semantic indexes; then request Suggi's exact Tailscale browser URL and require HTTP 200 before reporting completion. Any missing step is HALT, not a warning.

## Cross-links

- `research/reports/openclaw-server-migration.md` -- the distributed state map that explains why an in-place major upgrade resembles a machine migration.
- `reflections/2026-08-20_morpheus_terminal-cwd-gateway-restart.md` -- running process state, not authored config alone, determines behavior.
- `reflections/2026-08-27_morpheus_stale-code-refusal-is-not-a-bug.md` -- version convergence must include the loaded service, not only files on disk.
- `reflections/2026-08-31_neo_verification-must-precede-the-claim.md` -- the evidence gate must fire before the verdict reaches the human.
