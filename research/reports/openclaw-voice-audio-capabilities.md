---
name: openclaw-voice-audio-capabilities
id: 20260717T080900Z
tier: report
author: ava
tags: [openclaw, voice, tts, stt, talk, realtime, audio, webchat]
links:
  - research/insights/openclaw-manual.md
---

# OpenClaw Voice and Audio Capabilities -- Options and Costs

## Executive Summary

**Question:** How can voice be enabled in OpenClaw, and what are the
cost implications? **Answer:** OpenClaw has two separate voice
systems -- TTS (text-to-speech for agent replies) and Talk (realtime
two-way voice conversations). TTS works out of the box with the
default provider chain and costs nothing with Microsoft Edge. Talk
requires a configured realtime provider (OpenAI, ElevenLabs) and an
API key. The WebChat voice button uses Talk mode, not TTS, which is
why Suggi saw the "Realtime voice provider not configured" error
despite TTS functioning fine. Recommendation: enable free Microsoft
TTS for agent replies now; defer full Talk setup until an API key is
available. Confidence: high (90%).

## Research Question

What voice and audio capabilities does OpenClaw provide, how do they
differ, what are the provider options and costs, and why does the
WebChat voice button show an error despite the `tts` tool working?

**Scope: in.** TTS, Talk/realtime, WebChat voice button, provider
options, token/audio costs, free alternatives.

**Scope: out.** Channel-specific voice (Telegram voice notes, Discord
voice), voice cloning, telephony integration.

## Methodology

**Approach:** Documentation review. Read the full OpenClaw TTS docs
(`docs/tools/tts.md`), Talk mode docs (`docs/nodes/talk.md`), and
WebChat docs (`docs/web/webchat.md`). Tested the `tts` tool directly
from a session to confirm it works without explicit configuration.

**Sources:** OpenClaw 2026.7.1 local documentation. WebChat live test
(tts tool invocation succeeded, WebChat voice button returned error).

**Limitations:** Full Talk mode not tested (requires API key). Cost
estimates are from docs/published pricing, not live billing.

## Findings

### Finding 1: Two Separate Voice Systems

OpenClaw has two distinct voice paths with different purposes:

| Feature | TTS (text-to-speech) | Talk (realtime voice) |
|:--------|:---------------------|:----------------------|
| Purpose | Agent replies as audio | Two-way voice conversation |
| How it works | Text -> audio file -> attached to reply | Continuous audio stream both ways |
| Input method | You type, agent speaks reply | You speak, agent speaks back |
| WebChat button | No (manual `/tts` or auto-TTS) | Yes (the voice button in WebChat) |
| Default state | Works out of the box | Needs explicit config + API key |
| Free option | Microsoft Edge TTS | None (all need API keys) |

The WebChat voice button triggers Talk mode -- not TTS. This is why
Suggi's TTS tool worked but the voice button showed an error. They
are different systems with different configuration paths.

### Finding 2: 14 TTS Providers, One Completely Free

OpenClaw supports 14 TTS providers. Most require API keys. Microsoft
Edge TTS is the only fully free option that requires no API key:

| Provider | API Key | Cost Model | Quality |
|:---------|:--------|:-----------|:--------|
| **Microsoft Edge** | None | Free (no SLA) | Neural, good |
| OpenAI | Yes | ~$0.015/1K chars | High |
| ElevenLabs | Yes | ~$0.015/1K chars | Highest |
| Google Gemini | Yes | Usage-based | High |
| DeepInfra | Yes | Usage-based | Medium |
| OpenRouter | Yes | Usage-based | Medium |
| Local CLI | None | Free (needs local tool) | Varies |

### Finding 3: Talk/Realtime Costs Are Per-Minute, Not Per-Token

Full two-way voice via Talk mode requires a realtime provider.
OpenAI Realtime API pricing (gpt-realtime-2.1):

- Audio input: ~$0.06/minute
- Audio output: ~$0.24/minute
- Text tokens: standard model rates apply for thinking/inference

A 10-minute voice conversation: approximately $3.00 in audio costs
plus token costs for the model's responses. This is separate from
and additional to the normal chat model cost.

### Finding 4: TTS Already Functional Without Any Configuration

The `tts` tool worked on first invocation with no explicit config.
OpenClaw's default provider auto-select chain found a working
provider (likely Microsoft Edge via `node-edge-tts`, which needs no
API key). The audio was delivered as an attachment in the chat.

Auto-TTS (every reply spoken automatically) can be enabled by adding
to `~/.openclaw/openclaw.json`:

```json5
{
  messages: {
    tts: {
      auto: "always",
      provider: "microsoft",
      providers: {
        microsoft: {
          speakerVoice: "en-US-MichelleNeural",
          lang: "en-US",
        },
      },
    },
  },
}
```

This makes every agent reply come as audio by default -- no manual
`/tts` command needed.

## Discussion

The two-system separation is deliberate design. TTS is a reply
delivery mechanism (text goes out as audio, one-directional). Talk
is a full conversation modality (audio goes both ways with streaming,
interruption detection, and phase transitions between listening,
thinking, and speaking). They serve different interaction models:
TTS = "I speak to you while you type." Talk = "We have a phone call."

For Suggi's use case (preferring voice over typing), the full Talk
experience would be ideal -- speak naturally, hear replies. But it
requires an OpenAI API key and has per-minute costs. The free
alternative is a hybrid: type to the agent, hear spoken replies via
Microsoft TTS. This is available now at zero additional cost.

The WebChat voice button error is technically correct but confusing.
The button requires a configured Talk provider, and none exists.
Users who have heard the agent speak via TTS may reasonably expect
the voice button to use the same system, but it does not.

## Conclusion

Enable free Microsoft TTS with `auto: "always"` for immediate
spoken replies at zero cost. Defer full Talk (two-way voice) until
an OpenAI or ElevenLabs API key is available.

The error "Realtime voice provider 'openai' is not configured" is
about Talk mode, not TTS. The two are separate systems. The TTS
tool already works and will continue to work regardless of Talk
configuration.

**Recommendation:** Set up auto-TTS with Microsoft Edge for now.
This gives Suggi spoken replies on every message at no cost.
Revisit Talk mode when an OpenAI API key is available.

**Open questions:**
- Does Microsoft Edge TTS have rate limits or throttling in practice
  on this VPS? Untested at scale.
- Would the free TTS quality be sufficient for Suggi's daily use?
  Subjective, requires testing.
- Can local STT (whisper.cpp or similar) be wired into OpenClaw for
  free voice input? Needs separate research.

---

## Evaluation History

*Not yet evaluated. First-pass report. Awaiting review.*
