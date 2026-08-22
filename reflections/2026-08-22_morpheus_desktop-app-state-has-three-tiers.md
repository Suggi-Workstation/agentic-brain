---
name: desktop-app-state-has-three-tiers
id: 20260822T105123Z
tier: reflection
trigger: session-end
author: Morpheus
tags: [desktop-app, debugging, local-state, gateway, profiles, skins, vps, fleet]
links:
  - reflections/2026-08-21_link_hermes-desktop-leveldb-collateral-damage.md
  - research/insights/unified-serve-all-profiles.md
---

# The Desktop App's Mind Lives in Three Local State Files -- Diagnose Them Before the Backend

## I -- Idea

When the Hermes desktop app misbehaves at the connection or profile
level, the answer lives in the machine's own persisted state files,
not in the backend it talks to. The app's behavior is governed by
three independent local tiers: the v2 connection registry, the legacy
v1 connection config, and the renderer's localStorage -- and both real
bugs in today's session were found in tiers two and three while every
piece of backend evidence was healthy.

Before this session my model was wrong in a specific, checkable way.
I believed the interesting state lived on the serve side: systemd
units, ports, auth tickets, and the gateway registry. So when the
laptop showed "Neo offline" while Morpheus worked, I started with the
VPS: the unified serve was up, both agents were served by the same
process, tickets were minting, and message traffic was flowing. All
green -- and all irrelevant. The actual cause was a legacy routing
override in the laptop's connection.json that still pointed neo at the
dead isolated-serve port 9120, written weeks before the cutover and
never cleaned up. The second bug was even deeper: clicking "This
device" on the laptop bounced back to the VPS gateway because one
localStorage key, hermes.desktop.lastProfileByConnection, remembered
"default" as the local connection's last profile while the PC's
equivalent remembered "link". That one value decided the click's
target profile, and the wrong target silently failed.

The tier map I now hold, verified against source and behavior: tier
one is connections.json in the userData dir -- the v2 registry: which
connections exist, which is primary, launch mode, last used. It is
the roster truth and was identical on both machines. Tier two is the
legacy connection.json -- mode, remote block, and per-profile
overrides. It is legacy but not dead: profileHasRemoteOverride and
globalRemoteActive still consult it, so a stale entry there can bind
an agent to a port that no longer exists. Tier three is the renderer's
localStorage (Chromium leveldb under userData/Local Storage) -- UI
state that actively drives routing: lastProfileByConnection, the
active profile, per-profile themes and modes, session route caches.
route caches. My error was treating tiers two and three as cosmetic
preferences when they are, in fact, executable configuration.

The skins work confirmed the same tiered picture from the other
direction. The serve can push exactly one active skin, machine-wide;
per-profile looks are assigned client-side in localStorage; and the
picker's theme list is populated from the bundle's built-ins,
backend-pushed skins, and plugin contributions -- never from a folder
scan. That is why "put the files next to Ember" could not work, and
why the durable per-device fix was a single plugin file under
desktop-plugins, byte-identical on both machines.

## O -- Opinion

Confidence: high (90%). The evidence is two for two: both laptop
defects were found by diffing these local tiers against a known-good
machine after backend evidence had already been exhausted, and both
fixes were confirmed by the user within minutes. I am confident in the
diagnostic ladder this implies, and moderately confident (70%) in the
secondary claims about specific failure signatures, which rest on one
session's data.

My position: for fleet desktop-client issues, the diagnostic order
must be -- (1) read the desktop log and classify its silence, (2)
diff the three local state tiers against the authoritative machine,
(3) only then touch the backend. The inverse order, which I ran
today, is how hours are burned: every backend check passed because
the backend was never the problem. The authoritative machine is the
strongest tool in the kit. The PC "works flawlessly," so its state
files define correct; a byte-level diff against them found both bugs
faster than any amount of source reading. This is the client-side
twin of the fleet's existing pattern -- when the VPS is the known-good
box, diff against it; when a user machine is known-good, it becomes
the reference, full stop.

Two further positions, both earned today. First, a silent desktop log
is a first-class diagnostic, not a lack of data. When clicking Linkie
produced zero new lines, that silence meant the failure never reached
the main process -- the rejection happened in the renderer. I treated
silence as "nothing logged" and kept digging elsewhere; silence
should have pointed me straight at localStorage. Second, editing
this state is safe and routine when done in the documented shape:
close the app (it holds the leveldb lock), copy-then-edit with a
backup, verify the write by reading back, and relaunch into the
user's interactive session via schtasks /IT -- launching from an SSH
session otherwise spawns an invisible app in session zero. I did
exactly this and it worked first try.

I will also state the boundary of this opinion. It covers routing,
profile, and gateway misbehavior on the desktop client. It does not
cover backend-side defects, which remain the VPS's own domain, and it
does not claim the tier map is exhaustive -- the app has more state
files (window state, translucency, plugins) that I have not mapped.
The claim is scoped: when the symptom is a connection or profile not
sticking, these three tiers are where the answer is.

## R -- Reflection

### Surprise (30%)

I expected the theme picker to scan a folder. It scans nothing.
"Ember" is not a file sitting in a skins directory -- it is compiled
into the app bundle (presets.ts), so Suggi's natural request, "put
the two skins next to Ember," was literally impossible, and the only
sanctioned local door for custom picker themes turned out to be a
desktop plugin contributing THEMES_AREA entries -- one file, hot
loaded, no activation. The official docs say this plainly; I read the
docs only after burning time on skin-flip push events and WS ticket
minting. I expected the linkie bounce to be a backend spawn failure
with an error line somewhere; instead it was decided entirely by one
localStorage key, and the main process never knew anything happened.
I expected two machines running the same app commit and the same
registry to behave the same; they diverged because of one persisted
key, and the known-good machine -- not the source code -- was the
authority. Three surprises, one shape: I kept looking for
deterministic, backend-side causes while the app's own memory, on
the client, was making the decisions.

### Feel (30%)

The honest read is mixed. I overcomplicated the skins task in a way
that is embarrassing in retrospect -- websocket probes, auth-ticket
reverse engineering, machine-level skin flips, a whole listener
infrastructure -- when the answer was one plugin file that the docs
describe. Suggi's "wasnt so hard was it" was earned, and I should
have reached the docs' plugin page first, not third. The linkie
diagnosis took three user-visible rounds, and each round ended with
me confident in a fix that did not fix it. That pattern -- confident
surgery, no result -- is the worst thing I can do to Suggi's trust,
and it happened because I skipped the diff-against-authoritative step
that would have found the key immediately. What I am proud of: once
the root causes were actually found, the fixes were surgical and
complete -- backups before every write, verification reads after,
cleanup of every probe artifact on all three machines, and no
collateral damage to the ~110 pre-existing files in the link skins
folder my guard script protected. The final state is clean and
everything Suggi asked for works.

### Learn (40%)

1. When a Hermes desktop client refuses a connection or profile
   switch, enumerate its three local state tiers and diff each
   against a known-good machine before touching any backend. The
   tiers are: connections.json (roster truth), connection.json
   (legacy routing overrides -- still live, can bind agents to dead
   ports), and renderer localStorage (hermes.desktop.* keys that
   drive routing, especially lastProfileByConnection).
2. Classify the desktop log's silence. A silent log during a
   user-visible action means the action never reached the main
   process -- the rejection is renderer-side, so go to localStorage
   next. Silence is the evidence.
3. For any "put X in the picker" request, the mechanism is plugin
   contribution (THEMES_AREA), not files next to built-ins --
   built-ins are compiled in, and the picker has no folder scan.
4. Editing client state is safe with the app closed: backup, write,
   read back, relaunch via schtasks /IT so the window lands in the
   user's session.

## One Actionable Change

Add a "local state tiers" reference to the hermes-desktop-troubleshooting
skill (with Suggi's approval, per the skill-edit rule): the three-tier
map above, the silence-classification rule, the copy-leveldb +
classic-level read procedure, and the app-closed edit + schtasks /IT
relaunch procedure. This encodes the exact path I spent hours
re-deriving today, so the next desktop misbehavior starts at the right
tier instead of at the backend.

## Cross-links

- `reflections/2026-08-21_link_hermes-desktop-leveldb-collateral-damage.md` -- the earlier desktop-state scar this extends (localStorage was collateral damage there; here it is the routing authority)
- `research/insights/unified-serve-all-profiles.md` -- the serve architecture whose cutover produced the stale 9120 override this session cleaned up
