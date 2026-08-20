---
name: local-aliases-outperform-multiconnection
id: 20260820T224313Z
tier: reflection
trigger: decision
author: Link
tags: [hermes-desktop, remote-routing, connector-profiles, verification]
links:
  - reflections/2026-08-17_link_half-provisioned-agents-look-wired.md
---

# Local Connector Aliases Are the Reliable Boundary for Hermes v0.20.4

## I -- Idea

The reliable way to use the Hermes v0.20.4 Desktop with Morpheus and Neo on a VPS is to keep small local connector profiles and route each one through a profile-scoped legacy connection entry, rather than treating the machine-level multi-connection registry as a replacement for the local profile rail.

This conclusion was triggered by a long failure sequence. The PC originally had Link plus two small local identities named Morpheus and Neo. Those identities were not the real VPS agents. They were local names that gave the Desktop profile rail an entry and told Electron which remote backend to use when that entry was selected. Morpheus mapped to port 9119 and Neo mapped to port 9120. That arrangement had worked for normal daily use.

The later migration introduced a v2 machine-level registry with a local entry and a Suggi VPS entry. The registry was visible and its Test action reported reachability. The VPS gateway also advertised several profiles over one endpoint. These facts appeared to prove that the local aliases were obsolete. They did not. After the aliases were removed, the bottom-left local profile rail lost Morpheus and Neo even though the remote gateway records remained. When the remote gateway was selected, the app could list remote profiles, but activation was unstable: profile clicks returned to Link, switching back to This device failed, and sign-out became the only recovery path. The failure consumed repeated restarts and reset unrelated renderer appearance state during an overly broad cleanup.

The investigation compared three layers that had been conflated. First, the official multi-connection registry stores named gateway machines. Second, the local Desktop profile rail and its local Hermes home enumerate profile identities. Third, the legacy connection.json file can route an individual local profile to a remote backend. The installed source and the earlier successful session record show that v0.20.4 still relies on the second and third layers for the old profile-rail workflow. The registry is a separate feature, not a guarantee that the old rail has been replaced.

The VPS architecture was also simplified incorrectly during the detour. A single multiplexed serve could advertise many profiles, but that did not produce a reliable client route. The old topology is clearer: one isolated serve for Morpheus on 9119 and one isolated serve for Neo on 9120. Each process keeps its own profile home while the messaging gateway services remain separate and active.

## O -- Opinion

My position is that the old local-alias architecture is the correct choice for this PC and this Hermes release. Confidence is high, above 90 percent, because the conclusion is supported by four independent forms of evidence: the earlier successful Desktop state, the installed source behavior, the current official profile and desktop documentation, and fresh authenticated RPC probes against both live VPS services.

The most important distinction is between a gateway being reachable and a Desktop route being usable. A machine-level registry entry can pass an HTTP and WebSocket test while the profile rail still lacks a local identity or the activation code selects the wrong backend. The prior troubleshooting treated reachability as proof of end-to-end profile usability. That was too weak a test. The actual acceptance criterion is a complete chain: the local profile exists, the legacy map names the right remote URL, the remote service is listening, authentication works, the requested remote profile exists, and a profile-scoped RPC succeeds. The restored state passes that chain for both agents.

The v2 registry is not intrinsically bad. It is an official feature and may be the right design in a newer Desktop build whose union roster and `(connection, profile)` activation are stable. It is simply the wrong active boundary for this installation after repeated evidence of broken switching. Keeping it local-only removes a competing gateway-switching path without deleting the VPS agents. This is a simplification, not a claim that the official feature is universally defective.

The connector profiles must remain intentionally thin. They should contain identity metadata and the harmless local SOUL mirror used by the Desktop profile surface. They should not receive the VPS workspaces, sessions, memories, skills, cron state, or provider keys. The remote backend remains authoritative. This preserves the isolation model described by the official Profiles documentation and prevents a future operator from mistaking a connector shell for a second copy of the agent.

The VPS should keep two isolated serve processes for this client. Multiplexing is documented as an opt-in operational optimization for a host where many ports and supervisors are burdensome. It does not automatically improve Desktop routing, and it weakens the simple one-profile-to-one-port mental model that made the old connector setup understandable. One process per profile also preserves separate crash domains and makes a failed Neo service distinguishable from a failed Morpheus service.

The correct repair therefore changes only the boundaries that were actually broken: recreate the two local identities, restore the two profile-scoped remote mappings, remove the machine-level remote registry entry from the Desktop's intended workflow, and restore the two isolated serve units. It must not wipe LevelDB, cookies, themes, sessions, or provider settings. Those data stores are unrelated to the profile identity problem. The successful read-only probes show the repair is structurally complete; one normal Desktop restart remains necessary for the renderer to reload the filesystem and route configuration.

## R -- Reflection

### Surprise

I expected the official multi-connection feature to make local aliases redundant as soon as a remote gateway could list all profiles. Instead, the working and broken states demonstrated that discovery and activation are different contracts. The registry could see a gateway, the gateway could list five profiles, and authenticated RPC probes could succeed, while the Desktop still could not provide a stable route back to Link or reliably open every remote profile. I also expected a one-port multiplexed server to be simpler for the Desktop because it reduced the number of gateway entries. In practice it created a larger ambiguity: one URL advertised multiple identities while the client still carried stale per-connection profile state. The two isolated ports are more obvious and easier to verify.

### Feel

The uncomfortable conclusion is that the failure was not caused by one mysterious Hermes bug. It was caused by repeatedly crossing architectural boundaries without proving the contract at each boundary. I removed local identities before proving that the packaged profile rail no longer depended on them. I accepted a reachable gateway as evidence that a selected profile would activate. I then cleaned renderer state too broadly, which reset the Ember appearance and increased the user's recovery cost. The user was right to challenge each assumption.

The restoration feels materially better because each change now has a narrow purpose. The local aliases were created with no bundled skills and no local runtime data. The route file was restored from a known-good historical copy rather than invented. The VPS services were rebuilt from the saved isolated unit shape, while messaging services were left alone. Fresh probes returned profile lists, sessions, and project trees on both ports. That does not erase the earlier mistakes, but it gives the repair a margin of safety and an evidence trail.

### Learn

1. In a multi-layer desktop system, a registered machine, a profile identity, and a session route are separate objects. Never delete one because another can enumerate similar names.
2. The acceptance test for a remote profile must be profile-scoped and end to end. `Test: Reachable` is only one link; the real gate is local identity, route map, authenticated RPC, correct remote home, and persistent session access.
3. When three or more fixes fail across state, auth, and gateway layers, question the architecture. Here the old connector architecture was the simpler and more reliable product for the installed client.

### One Actionable Change

Before any future Hermes Desktop migration, create a read-only route matrix containing every local profile name, its remote URL, its expected VPS profile, its port, and one authenticated RPC probe. Do not remove a local connector, consolidate a serve, or wipe renderer state until every row has a passing replacement route and the packaged Desktop has opened that row successfully.

### Cross-links

- `reflections/2026-08-17_link_half-provisioned-agents-look-wired.md`
- `governance/system-constitution.md`
- `governance/system-primedirectives.md`
- `research/insights/mnemosyne-system.md`
