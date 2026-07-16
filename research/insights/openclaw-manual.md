---
name: openclaw-manual
id: 20260716T151201Z
tier: insight
source:
  - 20260716T153500Z
author: ava
tags: [openclaw, platform, manual, reference, tools, workspace]
links:
  - research/insights/deepseekv4pro.md
  - research/insights/prompt-engineering.md
  - research/insights/context-engineering.md
---

# OpenClaw Agent Platform -- General Operating Manual

> A general-purpose reference for any agent or human working with the
> OpenClaw agent platform. Covers architecture, configuration, tools,
> workspace system, sessions, memory, secrets, and best practices.

## What OpenClaw Is

OpenClaw is an MIT-licensed, self-hosted agent gateway. A single Node.js
process (the Gateway) connects language models to chat channels, tools,
and a filesystem workspace. Agents run inside the Gateway as persistent
sessions with tool access, memory, and configuration.

Key properties:
- **Self-hosted:** runs on a VPS, local machine, or Docker.
- **Model-agnostic:** supports 80+ providers via plugins (OpenAI,
  Anthropic, DeepSeek, Google, Ollama, and many more).
- **Multi-channel:** WebChat, Discord, Telegram, WhatsApp, Signal,
  Slack, iMessage, Matrix, and others.
- **Multi-agent:** multiple agents share a single Gateway, each with
  independent workspaces and configurations.
- **Tools-rich:** file I/O, shell execution, browser automation, web
  search, memory search, cron scheduling, sub-agent spawning, and
  device control for paired phones.

## Architecture

```
User messages (WebChat / Discord / Telegram / etc.)
        |
        v
  OpenClaw Gateway (Node.js process)
        |
        v
  Agent Loop
    |-- System prompt assembly (bootstrap files + tool schemas)
    |-- Model API call (configured provider/model)
    |-- Tool execution (if model requests tool calls)
    |-- Response routing back to the originating channel
```

The Gateway is the single process that:
- Connects to chat channels and routes messages.
- Manages agent sessions (conversation state, context, memory).
- Routes tool calls to the host system.
- Supports hot-reload of configuration without downtime.

## Configuration

### Main config file: `~/.openclaw/openclaw.json`
- JSON5 format (comments and trailing commas allowed).
- Hot-reloads on most changes; a few require Gateway restart.
- Strict validation -- bad config prevents Gateway startup.
- A last-known-good backup is maintained automatically.

### Key config sections:

| Section | What it controls |
|---|---|
| `agents.defaults` | Model, workspace path, bootstrap limits, thinking mode |
| `agents.defaults.model` | Primary model + fallback chain |
| `agents.defaults.bootstrapMaxChars` | Max chars per workspace file injected into prompt (default 20K) |
| `agents.defaults.bootstrapTotalMaxChars` | Max total chars across all bootstrap files (default 60K) |
| `agents.defaults.thinkingDefault` | Whether thinking/reasoning mode is default |
| `tools.exec` | Shell execution policy: security level, timeouts, approval |
| `tools.browser` | Browser automation policy |
| `session` | Session scoping, reset cadence |
| `memory` | Memory indexing and search configuration |
| `channels` | Connected chat surfaces and their settings |

### Environment variables loading order (highest priority first):
1. Process environment (systemd service, Docker, launch command).
2. Global `~/.openclaw/.env` (recommended for API keys).
3. Config `env` block in `openclaw.json`.
4. Login-shell import (if `env.shellEnv.enabled` is on).

Provider credentials from workspace-level `.env` files are IGNORED
for security reasons. Use `~/.openclaw/.env` instead.

## Tool Catalog

### Filesystem Tools
| Tool | Purpose |
|---|---|
| `read` | Read text files and images. Max 2000 lines / 50KB per call. |
| `write` | Write or overwrite a file. Creates parent directories. |
| `edit` | Targeted text replacement (oldText -> newText) in a file. |
| `apply_patch` | Apply multi-file patches with `*** Begin Patch` markers. |

### Shell Tools
| Tool | Purpose |
|---|---|
| `exec` | Run shell commands. Supports background mode, PTY for TTY CLIs. |
| `process` | Manage running exec sessions: poll, get logs, send stdin, kill. |

### Web & Browser Tools
| Tool | Purpose |
|---|---|
| `web_search` | Search the web (requires a configured search provider). |
| `web_fetch` | Fetch a URL and extract readable markdown or plain text. |
| `browser` | Full browser automation: tabs, click, type, screenshot, snapshot. Supports login profiles for authenticated sessions. |

### Memory & Knowledge Tools
| Tool | Purpose |
|---|---|
| `memory_search` | Semantic vector search across MEMORY.md, memory/*.md, and session transcripts. |
| `memory_get` | Read exact line-range excerpts from memory files. |

### Session & Multi-Agent Tools
| Tool | Purpose |
|---|---|
| `sessions_list` | List visible sessions with filters. |
| `sessions_history` | Fetch message history from another session. |
| `sessions_send` | Send a message to another session or agent. |
| `sessions_spawn` | Start an isolated sub-agent for parallel or delegated work. |
| `sessions_yield` | End current turn, wait for sub-agent completion events. |
| `subagents` | List status of active and recent sub-agents. |

### Scheduling Tools
| Tool | Purpose |
|---|---|
| `cron` | Create, update, delete cron jobs and wake events for reminders and recurring work. |
| `heartbeat` | The HEARTBEAT.md file controls periodic check-in checklist tasks. |

### Gateway & Config Tools
| Tool | Purpose |
|---|---|
| `gateway` | Restart, config read/patch/apply, run updates. |
| `session_status` | Show model, usage, cost for the current session. |

### Messaging Tools
| Tool | Purpose |
|---|---|
| `message` | Send messages to any configured channel (Discord, WhatsApp, etc.). |

### Node/Device Tools
| Tool | Purpose |
|---|---|
| `nodes` | Discover and control paired iOS/Android devices (camera, screen, location). |
| `file_fetch` / `file_write` | Transfer files to and from paired nodes. |

### Other Tools
| Tool | Purpose |
|---|---|
| `canvas` | Display HTML content on connected node canvases. |
| `tts` | Text-to-speech via a configured voice provider. |
| `node_inference` | Run local Ollama models on paired desktop/server nodes. |

## Workspace System

### Bootstrap Files (injected into every session start):

| File | Role |
|---|---|
| `AGENTS.md` | Operating rules, red lines, heartbeat policy, session startup sequence |
| `SOUL.md` | Persona, tone, boundaries, vibe |
| `IDENTITY.md` | Agent name, creature type, emoji, avatar reference |
| `TOOLS.md` | Environment-specific notes (camera names, SSH hosts, voice prefs) |
| `USER.md` | Information about the human user |
| `HEARTBEAT.md` | Heartbeat task checklist (keep small to minimize token burn) |
| `MEMORY.md` | Curated long-term memory (loaded in main/direct sessions only) |

Sub-agent sessions only inject AGENTS.md and TOOLS.md.

### Workspace Setup:
- Default location: `~/.openclaw/workspace`.
- Auto-created on onboarding. `openclaw setup --baseline` creates
  workspace without the full wizard.
- `agents.defaults.skipBootstrap: true` disables auto-creation of
  bootstrap files (use when you ship your own from a repo).
- `agents.defaults.skipOptionalBootstrapFiles` can skip specific files.

### Memory Files:
| File | Purpose |
|---|---|
| `memory/YYYY-MM-DD.md` | Daily raw activity logs |
| `MEMORY.md` | Curated, distilled long-term memory |
| `memory/heartbeat-state.json` | Timestamps of last checks (email, calendar, etc.) |

### Bootstrap Limits:
- `bootstrapMaxChars`: max characters per file before truncation (default 20K,
  ours: 50K).
- `bootstrapTotalMaxChars`: max total characters across all files (default 60K,
  ours: 120K).
- Increase these if truncation warnings appear for important files.

### Our Workspace Conventions:
- Workspace is mirrored 1:1 to a GitHub repo (`workspace-ava`) via git.
- The `## Workspace Layout` section in AGENTS.md lists every required
  file and folder. The preflight gate verifies they all exist.
- Every workspace contains ASCII infra: `.github/workflows/ascii-guard.yml`,
  `.githooks/pre-commit`, `.gitattributes`, `.gitignore`,
  `scripts/setup-hooks.sh`.
- `memory/YYYY-MM-DD.md` files are daily raw logs; MEMORY.md is
  periodically updated from them.
- `IDENTITY.md` includes an Evolution Log section for tracking personal
  growth milestones across versions.

## Session Lifecycle

### Session Types:
- **Main session:** direct 1:1 chats with the human. MEMORY.md is loaded.
- **Shared/group sessions:** multi-user channels. MEMORY.md is NOT loaded
  for security (personal context stays private).
- **Sub-agent sessions:** isolated children spawned via `sessions_spawn`.
  Only AGENTS.md and TOOLS.md are injected (not SOUL/MEMORY/IDENTITY/
  USER/HEARTBEAT). Use `context: "fork"` only when the child needs the
  full parent transcript.
- **Cron sessions:** scheduled agentTurn jobs from the cron system.

### Session Reset:
- Default cadence: daily at 4 AM local time (`session.reset.atHour: 4`).
- Manual: `/new` or `/reset`. Sent alone, these acknowledge without
  invoking the model.
- Session scope: `per-sender` keeps separate sessions per user/chat.
- Heartbeat, cron, and system turns do not reset idle freshness.

### Compaction:
- Auto-compaction fires when approaching the context limit.
- Older turns are summarized; recent messages stay intact.
- Tool-call/result pairs are preserved at the compaction boundary.
- Memory flush runs before compaction.
- `/compact [instructions]` triggers manual compaction and reports
  remaining context budget.

## Secrets Management

### SecretRef System:
Credentials can be stored as SecretRefs instead of plaintext:

- `{ source: "env", provider: "default", id: "VAR_NAME" }` -- env var.
- `{ source: "file", provider: "alias", id: "/json/pointer/path" }` -- JSON file.
- `{ source: "exec", provider: "alias", id: "key" }` -- external resolver.

### Security Model:
- Secrets are resolved into an in-memory snapshot at activation time.
- Sentinels (`oc-sent-v1-...`) replace real values in logs and storage.
- Real values are injected only at the final network egress point.
- `~/.openclaw/.env` is the recommended location for API keys.
- Workspace `.env` files are blocked from setting provider credentials.

### CLI Commands:
```bash
openclaw secrets audit --check   # scan for plaintext residue
openclaw secrets configure       # interactive SecretRef setup
openclaw secrets reload          # re-resolve runtime snapshot
```

## Sub-Agent Best Practices

### When to Spawn:
- Multi-step research that can run in parallel.
- Throwaway analysis (isolated context is cleaner).
- Heavy batch file operations (separate session = separate context).
- Cross-model comparisons (different model per sub-agent).

### When NOT to Spawn:
- Single file reads (faster to read directly).
- Sequential dependent tasks (sub-agents cannot coordinate).
- Tasks requiring real-time user interaction.

### Configuration:
- Default: `isolated` context (clean child, no parent transcript).
- Use `context: "fork"` ONLY when the child needs the full parent
  transcript.
- `mode: "run"` for fire-and-forget background work.
- Sub-agents can use a different model than the parent.

## Exec Tool Guidelines

### Security:
- Exec runs commands on the host system.
- Security levels: `deny`, `ask`, `sandbox`, `full`.
- Destructive commands should always require approval.
- `trash` over `rm` (recoverable beats gone forever).

### Background Execution:
- Long-running commands: use `background: true` or `yieldMs`.
- Monitor with the `process` tool (poll, log, send input).
- Never use exec+sleep loops for reminders -- use `cron` instead.

### Environment Variables in Exec:
- `OPENCLAW_*`-prefixed env vars pass through to exec shells.
- Other custom vars are filtered by exec security policy.
- Use the `OPENCLAW_` prefix pattern for custom env vars that
  exec shells need access to.

## Memory Best Practices

### Writing Memory:
- Daily logs (`memory/YYYY-MM-DD.md`): raw, factual, timestamped.
- MEMORY.md: curated, distilled. Update periodically from daily logs.
- Decisions, context, and things to remember go in memory files.
- Secrets and credentials must never be written to memory files.

### Memory Search:
- `memory_search` is semantic -- search by meaning, not keywords.
- Always search before answering questions about prior work,
  decisions, people, or preferences.
- If the memory index is unavailable, fall back to direct file reads.

## Heartbeat System

### How It Works:
- Default interval: every 30 minutes. Set `every: "0m"` to disable.
- The Gateway polls the agent; the agent checks HEARTBEAT.md for tasks.
- If HEARTBEAT.md is empty, comment-only, or only contains headings and
  empty checklist stubs: OpenClaw SKIPS the heartbeat API call entirely
  (no model invocation, no token cost).
- If HEARTBEAT.md has real tasks: the agent executes them.
- If the agent replies `HEARTBEAT_OK` (optionally with short padding),
  OpenClaw suppresses outbound delivery for that heartbeat.
- Heartbeats run full agent turns -- shorter intervals burn more tokens.

### Config:
```json5
{
  agents: {
    defaults: {
      heartbeat: { every: "30m" },  // set "0m" to disable
    },
  },
}
```

### Heartbeat vs Cron:
- **Heartbeat:** batched periodic checks, conversational context is OK,
  timing can drift slightly. Good for inbox, calendar, weather checks.
- **Cron:** exact timing needed, isolated from main session context,
  one-shot reminders, direct-to-channel delivery.

## Channel-Specific Formatting

### Discord / WhatsApp:
- No markdown tables -- use bullet lists instead.
- Discord: wrap multiple links in `<>` to suppress embed previews.
- WhatsApp: no markdown headers -- use **bold** or CAPS for emphasis.

### WebChat:
- Supports `[embed ...]` for inline rich rendering.
- Supports `MEDIA:<path>` for file attachments.

## Diagnostic Commands

```bash
openclaw doctor              # full diagnostic report
openclaw doctor --fix        # auto-repair where possible
openclaw status              # Gateway health overview
openclaw memory status       # memory index health
openclaw secrets audit       # scan for plaintext secrets
```

### Session Slash Commands:
- `/status` -- usage overview (tokens, cost, time).
- `/context list` -- injected files, sizes, truncation status.
- `/context detail` -- per-skill, per-tool schema breakdown.
- `/context map` -- treemap visualization of context composition.
- `/model <provider>/<model>` -- switch model mid-session.
- `/reasoning on|off` -- toggle thinking/reasoning mode.
- `/new [model]` -- start a fresh session. Sent alone, acknowledges
  without model invocation.
- `/compact [instructions]` -- manually compact context, reports
  remaining budget.

---

*Written 2026-07-16 by link. Updated 2026-07-17 with heartbeat config,
sub-agent bootstrap behavior, session management details, workspace
conventions, and slash command reference.*
