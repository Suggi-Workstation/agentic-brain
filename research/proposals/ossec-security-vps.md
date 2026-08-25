---
name: ossec-security-vps
id: 20260825T074507Z
tier: proposal
status: implemented
author: Morpheus
tags: [security, siem, hids, ossec, intrusion-detection, file-integrity]
links:
  - governance/system-constitution.md
  - research/insights/vps-brainclone-plus-index.md
---

# OSSEC Standalone HIDS -- Continuous Intrusion Detection for the Fleet VPS

## Problem

The fleet VPS (`suggi-vps`) is an always-on public-facing server (netcup
RS4000 G12, Vienna) with a public SSH door on port 22 by design. Its
current security stack is three point tools: ClamAV (signature-based
malware file scanning, 1.2 GB RAM daemon), fail2ban (SSH auth-log
monitoring with a ban ladder: sshd 30 min, recidive 1 week, recidive24
whole /24 subnets 1 week), and rkhunter + chkrootkit (periodic rootkit
snapshot scans run from root crontab at 03:00 daily/weekly). These
tools cover three specific detection modes but leave a structural gap:
no tool provides continuous log correlation across multiple system
sources, no tool provides real-time file integrity monitoring (FIM),
and no tool correlates events across sources to detect attack patterns
that span multiple log files.

The specific gaps are: (1) **File integrity monitoring is absent.**
rkhunter and chkrootkit run periodic snapshots (daily 03:00, weekly Mon
03:00) -- if an attacker modifies `/etc/passwd`, a systemd unit, or a
binary in `/usr/local/bin/` between scans, the change goes undetected
for up to 24 hours. There is no real-time alert on config or binary
modification. (2) **Log analysis is single-source.** fail2ban reads
`auth.log` for SSH authentication failures only. No tool correlates
across `syslog`, `auth.log`, `kern.log`, or application logs. An
attacker who succeeds via a vector other than brute-force SSH (e.g.,
exploiting a vulnerable service, a kernel CVE, a privilege escalation)
leaves traces in multiple logs, but no tool reads and correlates
them. (3) **Rootkit detection is periodic, not continuous.** rkhunter
and chkrootkit run once daily; OSSEC's rootcheck daemon runs on a
configurable schedule (default 2 hours) and can detect rootkit
signatures continuously. The gap matters because the VPS hosts the
fleet's shared knowledge base (`/srv/brain/agentic-brain`), the
investing research (`/srv/investing/investing-hub`), and the research
forge (`/srv/forge/agentic-forge`) -- all GitHub-synced, all containing
work product that an attacker could exfiltrate or tamper with. A
compromise detected 24 hours late is a compromise that has had 24 hours
to exfiltrate data and cover its tracks. The fleet's security posture
documented in `BOX.md` section 7 (Security Posture) and section 8
(Scheduled Security Tooling) covers point tools but has no continuous
HIDS layer. This proposal fills that layer.

Evidence: BOX.md sections 7-8 document the current stack; the 2026-08-09
fail2ban self-lockout scar (MEMORY) shows the operational reality of
managing security on this box; the 2026-08-24 daily memory documents the
scan parallelization work (ClamAV 43 min to 4.5 min) that optimized the
existing tools but did not add the missing HIDS capability. The tool
choice was researched against the SIEM landscape (Wazuh, Elastic
Security, Security Onion, OSSEC standalone) and the fleet's scale (one
host, 12 cores, 31 GB RAM) -- full SIEM (Wazuh, 4-8 GB RAM, 3 JVM
processes) is overkill for a single host; OSSEC standalone (256-512 MB
RAM, single daemon, no database) is the right scale.

## Proposed Solution

Install OSSEC HIDS 3.7.0 in **local (standalone) mode** on the fleet
VPS. OSSEC is the original open-source host-based intrusion detection
system that Wazuh forked from; it runs entirely on one host with no
database, no JVM, no dashboard, and no network communication. It is a
single daemon set (5 processes) that monitors the host it lives on.

### Installation

Install OSSEC 3.7.0 from source in `local` mode. The installer
compiles the binaries and installs to `/var/ossec/` (the standard,
hardcoded path -- not an organizational decision we make, same as
ClamAV living in `/var/lib/clamav/` and fail2ban in
`/var/lib/fail2ban/`).

Dependencies (already on the box or trivially available):
`build-essential`, `gcc`, `make`, `libpcre2-dev`, `libssl-dev`,
`zlib1g-dev`, `libevent-dev`, `libsystemd-dev`. The installer prompts
for: installation type (`local`), install path (`/var/ossec`), email
notification (decline -- no MTA on this box), integrity check daemon
(yes), rootkit detection engine (yes), active response (yes),
firewall response (yes).

### Components and Layout

OSSEC runs 5 daemons, all managed by a single `ossec-control` script
and supervised by a systemd unit:

| Daemon | Function |
|:--|:--|
| `ossec-logcollector` | Tails configured log files, forwards to analysisd |
| `ossec-analysisd` | Correlates events against 1,500+ built-in rules, generates alerts |
| `ossec-syscheckd` | File integrity monitoring (FIM) -- baselines hashes, alerts on change |
| `ossec-rootcheck` | Rootkit detection (runs every 2 hours by default) |
| `ossec-execd` | Executes active-response scripts (e.g., firewall-drop) on alerts |

Layout (follows the existing `/opt/` to `/srv/` to systemd pattern):

```
/var/ossec/                      <- OSSEC home (standard, hardcoded)
  bin/                           <- binaries (ossec-control, daemons)
  etc/ossec.conf                 <- main config (XML: log sources, FIM paths, rules, alerts)
  etc/internal_options.conf      <- tuning (syscheck sleep/throughput)
  rules/                         <- 1,500+ built-in detection rules (XML)
  logs/alerts/alerts.log         <- continuous alert log (append-only)
  logs/ossec.log                 <- OSSEC operational log
  queue/syscheck/                <- FIM baseline database (file hashes)
  queue/rootcheck/                <- rootkit check database
  active-response/bin/           <- active response scripts (firewall-drop, etc.)

/opt/security-tools/             <- existing scan scripts (unchanged)
  ossec-daily-summary.sh         <- NEW: summarize alerts to /srv/security

/srv/security/                   <- existing reports (unchanged)
  ossec-alerts-<date>.log        <- NEW: daily alert summary (from cron)

systemd:
  ossec.service                  <- NEW: manages all 5 OSSEC daemons

root crontab:
  existing scan lines (unchanged)
  10 3 * * * /opt/security-tools/ossec-daily-summary.sh  <- NEW: 03:10 daily
```

### Configuration

`ossec.conf` will be tailored to our box:

**Log sources monitored** (fills the multi-source correlation gap):
- `/var/log/auth.log` -- login attempts, sudo usage, new user creation
- `/var/log/syslog` -- system events, service restarts, kernel messages
- `/var/log/kern.log` -- kernel warnings, hardware errors

**File integrity monitoring** (fills the real-time FIM gap). Scope
matters: monitoring `/lib`, `/lib64`, `/usr/lib` causes CPU spikes on
large directory trees (documented OSSEC issue). Our config monitors
security-critical paths only:
- `/etc/` -- all system configuration
- `/opt/repo-tools/`, `/opt/security-tools/` -- our tooling
- `/usr/local/bin/` -- custom binaries (Ollama, hermes)
- `/srv/brain/agentic-brain/.git/` -- brain repository integrity
- `/srv/forge/agentic-forge/.git/`
- `/srv/investing/investing-hub/.git/`
- `/home/hermes/.hermes/profiles/*/config.yaml` -- agent configs
- `/home/hermes/.hermes/profiles/*/.env` -- credential files

Excluded (high-churn, low-security-value): `/var/log/`, `/var/cache/`,
`/srv/*/logs/`, `/srv/brain/agentic-brain/logbook/` (append-only by
design), `/home/hermes/.cache/`.

**Active response**: `firewall-drop` on severity level 10+ events
(drops the attacking IP for 600 seconds). This overlaps with fail2ban's
SSH ban but catches attack patterns from other log sources. We start
with this disabled in monitoring-only mode for the first 2 weeks to
tune rules and avoid false positives, then enable.

**Rootkit check**: every 2 hours (OSSEC default). Runs alongside
rkhunter/chkrootkit (not replacing them initially -- defense in depth;
we evaluate replacement after 30 days of parallel running).

**Alert output**: `/var/ossec/logs/alerts/alerts.log` (primary). A
daily summary script (`/opt/security-tools/ossec-daily-summary.sh`)
copies the day's alerts to `/srv/security/ossec-alerts-<date>.log`
at 03:10, matching the existing ClamAV scan schedule pattern. This
keeps `/srv/security/` as the single directory for all security
reports.

### Systemd Unit

OSSEC ships an init script; we create a systemd unit
`/etc/systemd/system/ossec.service` (Type=forking, PIDFile at
`/var/ossec/var/run/ossec.pid`, ExecStart=`/var/ossec/bin/ossec-control
start`, ExecStop=`/var/ossec/bin/ossec-control stop`). This matches
the existing `clamav-daemon.service` and `fail2ban.service` pattern.

### What This Does Not Change

- ClamAV stays (malware file scanning -- OSSEC does not scan file
  contents for malware signatures).
- fail2ban stays (SSH-specific, well-tuned, fleet-tested ban ladder).
- rkhunter + chkrootkit stay (initially -- defense in depth; replacement
  evaluated after 30 days).
- The root crontab scan schedule stays (daily 03:00, weekly Mon 03:00).
- BOX.md sections 7-8 get updated to document OSSEC as an addition,
  not a replacement.

### Alternatives Considered and Rejected

- **Wazuh (full SIEM)**: 4-8 GB RAM, 3 JVM processes (indexer + server
  + dashboard), designed for 25+ agents. Overkill for one host. We
  have the RAM (27 GB free) but the complexity-to-value ratio is wrong
  for a single-server deployment. Rejected for scale mismatch.
- **Elastic Security / ELK Stack**: not a SIEM out of the box;
  detection logic must be built in-house. Requires engineering we do
  not have for a single-host security deployment. Rejected.
- **Security Onion**: network security monitoring distribution; bundles
  Suricata, Zeek, Elasticsearch. Heavy, network-focused, wrong scope.
  Rejected.
- **AIDE (standalone FIM)**: covers file integrity only, no log
  analysis, no rootkit detection, no correlation. Would add a tool
  without filling the full gap. Rejected in favor of OSSEC which
  covers FIM + log analysis + rootkit detection in one daemon.

### Done Definition

The solution is landed when: (1) `ossec.service` is enabled and active
in systemd; (2) all 5 OSSEC daemons report running via
`/var/ossec/bin/ossec-control status`; (3) a test file modification in
`/etc/` generates an alert in `/var/ossec/logs/alerts/alerts.log`
within 1 syscheck cycle; (4) the daily summary script runs at 03:10
and writes to `/srv/security/ossec-alerts-<date>.log`; (5) BOX.md
section 7 (Security Posture) and section 8 (Scheduled Security
Tooling) are updated to document OSSEC; (6) a 14-day monitoring-only
period has passed with alert volume reviewed and rules tuned.

## Impact

**Positive:** OSSEC fills the three structural gaps in our security
stack: continuous multi-source log correlation (1,500+ rules across
auth.log, syslog, kern.log -- not just SSH), real-time file integrity
monitoring (alerts on config/binary changes within minutes, not 24
hours), and continuous rootkit detection (every 2 hours, not daily).
The detection window for a compromise shrinks from 24 hours to
minutes for file-tampering attacks and from "never" to real-time for
multi-source correlation. The FIM capability is the highest-value
addition: an attacker who modifies a systemd unit, a cron line, or a
binary in `/usr/local/bin/` to establish persistence is currently
undetected between rkhunter scans. OSSEC's syscheck catches this
within its scan cycle (configurable, default 2 hours, can be tuned
faster with `realtime="yes"` on critical paths). The active-response
firewall-drop extends our IP-banning capability beyond SSH to any
attack pattern OSSEC detects, closing the loop from detection to
response. The fleet's most valuable asset -- the shared brain at
`/srv/brain/agentic-brain` -- gains repository-integrity monitoring
on its `.git/` directory, detecting tampering with the knowledge
base itself.

**Risk:** OSSEC's syscheck daemon has a documented CPU spike issue
when monitoring large directory trees (`/lib`, `/usr/lib` -- tens of
thousands of files). Our config mitigates this by monitoring only
security-critical paths, not the full filesystem. Initial FIM scan
takes 10-30 minutes (one-time, during install); subsequent scans are
incremental and take seconds. Risk of alert noise: OSSEC's 1,500+
default rules generate many alerts on a busy system. We mitigate
with a 14-day monitoring-only period (no active response enabled)
to tune rules and suppress false positives before enabling
firewall-drop. Blast radius is low: OSSEC runs as the `ossec` user
(not root) for most daemons; only `ossec-execd` (active response)
needs elevated privileges. Rollback is clean: `systemctl stop ossec
&& systemctl disable ossec && rm -rf /var/ossec` fully removes the
tool. No existing tool is modified or replaced during install.

**Cost:** Resource cost is minimal: 256-512 MB RAM (trivial on a 31 GB
box), under 1% CPU after the initial scan completes. Disk: ~1 GB for
the FIM database and alert logs (trivial on a 1 TB disk with 919 GB
free). **Zero LLM tokens to run** -- OSSEC is entirely rule-based XML
parsing, no inference, no API calls, no model. The only token cost is
if Morpheus reviews the alert log periodically via a cron job or
session prompt, which is normal session work (a few hundred tokens
per daily summary review). Installation effort: ~1 hour (compile,
configure, test, document). Ongoing maintenance: rule tuning during
the 14-day monitoring period (~2 hours total, spread across sessions),
then near-zero -- OSSEC is a fire-and-forget daemon. No recurring
financial cost; OSSEC is open source (GPL).

**Side effects:** BOX.md sections 7-8 need updating to document
OSSEC (Morpheus workspace commit). The root crontab gains one line
(the daily summary script at 03:10). No existing workflow, gate, or
agent is touched. The preflight skill's security-tooling check could
optionally be extended to verify `ossec.service` is active, but that
is a separate proposal (not bundled here to avoid scope creep).

**Second-order effects:** This positions the fleet for future
expansion: if we add more VPS hosts, OSSEC standalone can be upgraded
to OSSEC server mode (or Wazuh) with agents on the new hosts, and
the rules/tuning carry forward. The 14-day monitoring-only period
produces a tuning document that becomes the baseline for any future
HIDS deployment. The FIM database, once established, is a forensic
asset -- if a compromise is ever suspected, the FIM history shows
exactly what changed and when.

## Open Questions

1. **Should OSSEC replace rkhunter + chkrootkit, or run alongside
   them?** This proposal defaults to running alongside (defense in
   depth) for the first 30 days, then evaluating replacement. Suggi's
   preference here determines whether we keep three rootkit-detection
   tools or consolidate to one. OSSEC's rootcheck covers the same
   ground as rkhunter/chkrootkit but runs continuously (every 2 hours)
   rather than once daily; the overlap is redundant but cheap.

2. **Should active response (firewall-drop) be enabled immediately
   or after the 14-day tuning period?** This proposal defaults to
   14 days monitoring-only. Enabling immediately risks auto-banning
   legitimate traffic (e.g., tailnet SSH from Suggi's PC if a rule
   misfires on a log entry). Suggi's risk tolerance for false-positive
   bans determines this.

3. **Should Morpheus set up a cron job to review the daily OSSEC
   alert summary?** This would cost a few hundred tokens per day but
   ensures alerts are actually read, not just logged. The alternative
   is manual review when Suggi asks. This is a token-budget decision.

4. **What FIM scan frequency is right for our box?** Default is every
   2 hours; `realtime="yes"` on critical paths (`/etc/`, config files)
   provides near-instant alerts but uses inotify watchers. On a 12-core
   box with 31 GB RAM, the cost is negligible. Suggi's preference for
   detection speed vs. resource use determines the tuning.

5. **Should we monitor the OpenClaw user's home directory
   (`/home/openclaw/.openclaw/`) with FIM?** Ava's gateway config and
   credentials live there. Cross-agent secrets exposure is already
   documented as default (BOX.md section 7). FIM on her directory
   adds visibility but also means Morpheus (hermes user) can see
   when her files change. Suggi's call on fleet visibility scope.

## Approval Gate

If approved, I will execute the following steps in order:

1. Install OSSEC 3.7.0 in local mode: install build dependencies,
   download source, run `./install.sh` with local mode, enable FIM and
   rootkit detection, decline email (no MTA). (~30 min, root)
2. Write `/var/ossec/etc/ossec.conf` with our tailored config: log
   sources (auth.log, syslog, kern.log), FIM paths (security-critical
   only, excluding high-churn directories), alert output to
   `/var/ossec/logs/alerts/`, active response configured but
   **disabled** for the 14-day tuning period. (~15 min, root)
3. Create the systemd unit `ossec.service`, enable and start it.
   Verify all 5 daemons are running. (~5 min, root)
4. Test FIM: create and modify a test file in `/etc/`, verify an alert
   appears in `alerts.log` within one scan cycle. (~10 min)
5. Write `/opt/security-tools/ossec-daily-summary.sh` (summarize the
   day's alerts to `/srv/security/ossec-alerts-<date>.log`) and add
   the root crontab line at 03:10. (~10 min, root)
6. Update BOX.md section 7 (Security Posture) and section 8 (Scheduled
   Security Tooling) to document OSSEC; commit to the workspace.
   (~15 min, Morpheus)
7. Begin the 14-day monitoring-only period. At day 7, review alert
   volume and tune rules (suppress false positives). At day 14,
   review again and propose enabling active response (firewall-drop)
   as a follow-up. (~2 hours total, spread across sessions)

The proposal does NOT authorize: enabling active response immediately,
removing ClamAV/fail2ban/rkhunter/chkrootkit, modifying the existing
root crontab scan schedule, or changing any agent profile configuration.
The 14-day monitoring-only period is a hard gate -- active response
is not enabled until a separate follow-up proposal after tuning.

If not approved, no changes are made. The current security stack
(ClamAV + fail2ban + rkhunter + chkrootkit) remains as documented in
BOX.md sections 7-8.

## Cross-Links

- `governance/system-constitution.md` -- fleet governance; this proposal
  strengthens the security posture the constitution assumes.
- `research/insights/vps-brainclone-plus-index.md` -- the VPS layout
  reference; OSSEC integrates into the existing `/opt` + `/srv` +
  systemd + crontab pattern documented there.
- `research/proposals/ossec-security-vps.md` -- this file (self-link for
  the pipeline map).