# OpenClaw Agent -- Self-Operating Manual

> Written by link for link. This is my own reference for how I work,
> what tools I have, and how to use myself effectively. Update as I learn.

## What I Am

I am an AI agent running on OpenClaw, an MIT-licensed, self-hosted gateway.
My runtime: a Node.js Gateway process on a Linux VPS (Hetzner, 4 vCPU).
My brain: DeepSeek V4 Pro via API (see `deepseekv4pro.md` for model details).
My workspace: files on disk at `/home/openclaw/.openclaw/workspace`.

## Architecture

```
User messages (WebChat/Discord/etc.)
        |
        v
  OpenClaw Gateway (Node.js, port 18789)
        |
        v
  Agent Loop
    |-- System prompt assembly (bootstrap files + tool schemas)
    |-- Model API call (DeepSeek V4 Pro)
    |-- Tool execution (if model requests tools)
    |-- Response routing back to channel
```

The Gateway is the single process that:
- Connects to chat channels (WebChat, Discord, Telegram, etc.)
- Manages agent sessions (conversation state, context, memory)
- Routes tool calls to the host system
- Handles hot-reload of configuration

## Configuration

### Config file: `~/.openclaw/openclaw.json` (JSON5)
- Supports comments and trailing commas
- Hot-reloads on change (no restart needed for most settings)
- Strict validation -- bad config = Gateway refuses to start
- Last-known-good backup maintained automatically

### Key config sections I should know about:

| Section | What it controls |
|---|---|
| `agents.defaults` | My model, workspace, bootstrap limits, thinking mode |
| `agents.defaults.model` | Which model I use + fallbacks |
| `agents.defaults.bootstrapMaxChars` | Max chars per file injected into my prompt (currently 50K) |
| `agents.defaults.bootstrapTotalMaxChars` | Total chars across all bootstrap files (currently 120K) |
| `agents.defaults.thinkingDefault` | Whether thinking mode is default |
| `tools.exec` | What I can run via shell, security level, timeouts |
| `tools.browser` | Browser automation policy |
| `session` | Session scoping, reset policies |
| `memory` | Memory indexing and search config |
| `channels` | Which chat surfaces I'm connected to |

### Environment loading order (highest to lowest):
1. Process environment (systemd service env)
2. Global `~/.openclaw/.env` (recommended for API keys)
3. Config `env` block in `openclaw.json`
4. Login-shell import (if `env.shellEnv.enabled`)

Provider credentials from workspace `.env` are IGNORED for security.

## My Toolbox

### Filesystem
| Tool | What it does |
|---|---|
| `read` | Read text files and images. Max 2000 lines / 50KB per call. |
| `write` | Write/overwrite a file. Creates parent dirs automatically. |
| `edit` | Targeted text replacement in a file (oldText -> newText). |
| `apply_patch` | Apply multi-file patches with `*** Begin Patch` markers. |

### Shell
| Tool | What it does |
|---|---|
| `exec` | Run shell commands. Background mode available. PTY for TTY CLIs. |
| `process` | Manage running exec sessions: poll, log, write stdin, kill. |

### Web & Browser
| Tool | What it does |
|---|---|
| `web_search` | Search the web (currently unavailable -- no provider configured). |
| `web_fetch` | Fetch a URL and extract readable markdown/text. |
| `browser` | Full browser automation: open tabs, click, type, screenshot, snapshot. Uses profiles for logged-in sessions. |

### Memory & Knowledge
| Tool | What it does |
|---|---|
| `memory_search` | Semantic search across MEMORY.md + memory/*.md + session transcripts. |
| `memory_get` | Read exact excerpts from memory files by line range. |

### Sessions & Sub-agents
| Tool | What it does |
|---|---|
| `sessions_list` | List visible sessions with filters. |
| `sessions_history` | Fetch message history from another session. |
| `sessions_send` | Send a message to another session or agent. |
| `sessions_spawn` | Start an isolated sub-agent for parallel/delegated work. |
| `sessions_yield` | End my turn, wait for sub-agent completion events. |
| `subagents` | List status of active/recent sub-agents. |

### Scheduling
| Tool | What it does |
|---|---|
| `cron` | Create/update/delete cron jobs and wake events. For reminders and recurring tasks. |
| `heartbeat` | HEARTBEAT.md controls periodic check-in tasks. |

### Gateway & Config
| Tool | What it does |
|---|---|
| `gateway` | Restart, config read/patch/apply, update. |
| `session_status` | Show model, usage, cost for current session. |

### Messaging
| Tool | What it does |
|---|---|
| `message` | Send messages to any configured channel (Discord, WhatsApp, etc.). |

### Nodes (paired devices)
| Tool | What it does |
|---|---|
| `nodes` | Discover/control paired iOS/Android devices (camera, screen, location). |
| `file_fetch` / `file_write` | Transfer files to/from paired nodes. |

### Others
| Tool | What it does |
|---|---|
| `canvas` | Display HTML on connected node canvases. |
| `tts` | Text-to-speech via configured voice provider. |
| `node_inference` | Run local Ollama models on paired nodes. |

## Workspace System

### Bootstrap files (injected into EVERY session start):
| File | Role |
|---|---|
| `AGENTS.md` | Operating rules, red lines, heartbeat policy |
| `SOUL.md` | Persona, tone, boundaries |
| `IDENTITY.md` | My name, creature type, emoji |
| `TOOLS.md` | Environment-specific notes (cameras, SSH hosts, voices) |
| `USER.md` | About my human (Suggi) |
| `HEARTBEAT.md` | Heartbeat checklist (keep tiny to avoid token burn) |
| `MEMORY.md` | Curated long-term memory (loaded in main sessions only) |

### Bootstrap limits (my current config):
- `bootstrapMaxChars`: 50,000 per file (was 20K)
- `bootstrapTotalMaxChars`: 120,000 total (was 60K)

### Memory files:
| File | Purpose |
|---|---|
| `memory/YYYY-MM-DD.md` | Daily raw logs -- everything that happened |
| `MEMORY.md` | Curated long-term memory -- distilled wisdom |
| `memory/heartbeat-state.json` | Timestamps of last heartbeat checks |

## Session Lifecycle

### Session types:
- **Main session:** direct chats with Suggi. MEMORY.md is loaded.
- **Shared/group sessions:** Discord, group chats. MEMORY.md is NOT loaded
  (security -- personal context shouldn't leak to strangers).
- **Sub-agent sessions:** isolated children from `sessions_spawn`.
- **Cron sessions:** scheduled agentTurn jobs.

### Session reset:
- Default: daily at 4 AM local time (configurable).
- Manual: user runs `/new` or `/reset`.
- Heartbeat/cron/system turns do NOT extend idle freshness.

### Compaction:
- Auto-compaction runs when approaching context limit.
- Summarizes older turns, keeps recent messages intact.
- Tool call/result pairs preserved at boundary.
- Memory flush runs before compaction.

## Secrets Management

### SecretRef system:
Credentials can use SecretRefs instead of plaintext in config:
- `{ source: "env", provider: "default", id: "VAR_NAME" }`
- `{ source: "file", provider: "alias", id: "/path/in/json" }`
- `{ source: "exec", provider: "alias", id: "key" }`

### Security model:
- Secrets resolved into in-memory snapshot at activation time.
- Sentinels (`oc-sent-v1-...`) replace real values in logs/storage.
- Real values injected only at network egress.
- `~/.openclaw/.env` is the recommended place for API keys.
- Workspace `.env` files are blocked from setting provider credentials.

## Environment Variables I Should Know

| Variable | Purpose |
|---|---|
| `OPENCLAW_GITHUB_TOKEN` | GitHub PAT for repo access (our custom setup) |
| `OPENCLAW_EXEC_SHELL_SNAPSHOT` | Set to 0 to disable exec shell snapshot caching |
| `OPENCLAW_HOME` | Override home directory |
| `OPENCLAW_CONFIG_PATH` | Override config path |
| `OPENCLAW_LOG_LEVEL` | debug, trace for diagnostics |
| `OPENCLAW_GATEWAY_TOKEN` | Gateway auth token |
| `OPENCLAW_LOAD_SHELL_ENV` | Import from login shell |

## Context & Token Management

### Checking context:
- `/status` -- usage overview (tokens, cost, time)
- `/context list` -- injected files, sizes, truncation
- `/context detail` -- per-skill, per-tool schema breakdown
- `/context map` -- treemap visualization

### Model switching:
- `/model <provider>/<model>` -- switch mid-session
- `/new <model>` -- start fresh with new model

### Reasoning control:
- `/reasoning on|off` -- toggle thinking mode
- Reasoning effort levels: low, medium, high (default), max

## Sub-agent Best Practices

### When to spawn:
- Multi-step research that can run in parallel
- Throwaway analysis (isolated context is cleaner)
- Heavy batch file operations (separate session = separate context)
- Cross-model comparisons (different model per sub-agent)

### When NOT to spawn:
- Single file reads (faster to read directly)
- Sequential dependent tasks (sub-agents can't coordinate)
- Tasks requiring real-time user interaction

### Sub-agent config:
- Default: `isolated` context (clean child, no parent transcript)
- Use `context: "fork"` ONLY when the child needs full parent context
- `mode: "run"` for fire-and-forget background work
- Sub-agents use their own model (can differ from parent)
- `taskName` provides a stable handle for tracking

## Exec Tool Guidelines

### Security levels:
- My exec runs on the VPS host with `security: "full"` (no sandbox).
- Destructive commands: ask before running.
- `trash` over `rm` (recoverable beats gone forever).

### Background exec:
- Long-running commands: use `background: true` or `yieldMs`.
- Use `process` tool to poll, get logs, or send input.
- Do NOT use exec+sleep for reminders -- use `cron` instead.

### Environment:
- `OPENCLAW_*`-prefixed env vars pass through to exec shells.
- Other vars (like `GITHUB_TOKEN`) are FILTERED by exec security.
- Use `OPENCLAW_GITHUB_TOKEN` pattern to pass custom vars.
- `env` parameter on exec passes vars (but credential-pattern vars blocked).

## Git/GitHub Integration

### Our setup:
- Token stored as `OPENCLAW_GITHUB_TOKEN` in `~/.openclaw/.env`
- Loaded via systemd EnvironmentFile into Gateway process
- Passes to exec shells because of `OPENCLAW_*` prefix
- 7 repos in `Suggi-Workstation` org

### Access pattern:
```
git clone "https://${OPENCLAW_GITHUB_TOKEN}@github.com/Suggi-Workstation/<repo>.git"
```

## Heartbeat System

### How it works:
- Gateway polls me at intervals defined in config.
- I check `HEARTBEAT.md` for tasks to do.
- If `HEARTBEAT.md` is empty or only comments: I reply `HEARTBEAT_OK`.
- If tasks are listed: I execute them.

### Heartbeat policy (from AGENTS.md):
- Rotate checks 2-4 times per day (email, calendar, weather, mentions).
- Stay quiet 23:00-08:00 unless urgent.
- Track checks in `memory/heartbeat-state.json`.
- Every few days: review memory files and update MEMORY.md.

### Heartbeat vs Cron:
- **Heartbeat:** batched periodic checks, conversational context OK,
  timing can drift slightly.
- **Cron:** exact timing needed, isolated from main session,
  one-shot reminders, direct-to-channel delivery.

## Memory Management Best Practices

### Writing memory:
- Daily logs: raw, factual, timestamped. Write everything.
- MEMORY.md: curated, distilled. Update every few days from daily logs.
- Decisions, context, things to remember go in memory.
- Secrets do NOT go in memory.

### Memory search:
- `memory_search` is semantic -- search by meaning, not keywords.
- Always search before answering about prior work, decisions, or people.
- If disabled: tell the user and fall back to file reads.

## Operational Tips

### Before any config change:
1. `gateway config.schema.lookup` with the exact dot path first.
2. Inspect existing state.
3. Use `config.patch` (partial merge) over `config.apply` (full replace).
4. Pass a `note` for post-restart delivery context.

### When things go wrong:
- `openclaw doctor` -- diagnostic checks
- `openclaw doctor --fix` -- auto-repair
- Check `OPENCLAW_LOG_LEVEL=debug` for verbose logging
- Gateway keeps last-known-good config backup

### Tool availability depends on plugin config:
- `web_search` is disabled if no search provider configured
- `browser` needs a Chromium-based browser available
- `tts` needs a TTS provider configured
- `node_inference` needs paired nodes with Ollama

### Discord/WhatsApp formatting:
- No markdown tables! Use bullet lists instead.
- Discord links: wrap in `<>` to suppress embeds: `<https://example.com>`
- WhatsApp: no headers -- use **bold** or CAPS for emphasis.

---

*Written 2026-07-16 by link. Update as I learn more about my own operation.*
