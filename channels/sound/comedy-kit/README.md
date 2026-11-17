# Comedy SFX kit (in-house)

Draft only, Monday, Nov 16, 2026, about 9:33 p.m. (America/New_York). Box path was `/workspace/sound/comedy-kit/`; this copy is `channels/sound/comedy-kit/`. Nothing here was posted or added to the render pipeline.

All four cues were **synthesized in-house on 2026-11-16** with Python (numpy) and written as 48 kHz, 16-bit, mono WAV, peak-normalized to **−3 dBFS**, then trimmed. No third-party samples, no downloads, no account-gated sites.

The pipeline kit on `mooneyn60-art/skills` branch `claude/youtube-monetization-strategy-m9vz6i` was checked and **not copied**:

- `skills/oh-meatball/sfx/v2/boing.wav` is from Kenney Impact Sounds, CC0 1.0 (`sfx/LICENSE.txt` would have permitted reuse with optional "Kenney.nl" credit). A fresh in-house spring boing was synthesized instead so this kit is one license.
- There is no record-scratch, bleep, or sad-trombone file in `sfx/v2/`. The v1 synth named `scratch.wav` is a short noise swipe, not a DJ record scratch, and was not copied.

A `make_bleep.py` script is in this folder for a bleep of any length.

## House rule (swears)

**Strong swears get bleeped. None at all in the first 7 seconds.** Use `bleep-0.3s.wav` (or a custom length from `make_bleep.py`) over the swear, not a mute, unless editorial asks for a mute. This matches the 11/16 TikTok cut-plan check ("The first 7 s are clean") and the part-2 template's first-7-seconds swear check. Mild words on YouTube, and any allowed TikTok swearing after 7 s, still follow the meatball bible / MASTER_ORDERS; this kit does not change those rules.

## Files

| File | Duration | Source / license | What it is |
|---|---:|---|---|
| `bleep-0.3s.wav` | 0.300 s | synthesized in-house 2026-11-16 | 1 kHz sine, 5 ms fades, 0.3 s |
| `bleep-0.6s.wav` | 0.600 s | synthesized in-house 2026-11-16 | same, 0.6 s |
| `bleep-1.0s.wav` | 1.000 s | synthesized in-house 2026-11-16 | same, 1.0 s |
| `make_bleep.py` | — | in-house script | `python3 make_bleep.py DURATION [OUT.wav]` for any length |
| `sad-trombone.wav` | 1.925 s | synthesized in-house 2026-11-16 | four descending half-steps (C4–B3–A♯3–A3), brass-ish saw + formant "wah"; vibrato (~5.5 Hz, 45 cents) on the last, longer "wahhh" |
| `boing.wav` | 0.650 s | synthesized in-house 2026-11-16 | cartoon spring: falling chirp ~720→110 Hz with bounce, decaying |
| `record-scratch.wav` | 0.550 s | synthesized in-house 2026-11-16 | vinyl crackle + a backward swipe (~2.4 kHz→280 Hz) and a short forward swipe |

All peaks measure **−3.00 dBFS**.

## Suggested levels under voice

JUDGMENT only (not a measured mix). These are comic punctuation, not a bed.

- Sit them **about 3–6 dB under the voice peak**, and duck ~6 dB if a cue overlaps a word (same idea as the current Shorts mixer: `sfx_duck_db: -6`, `sfx_gain: 0.22` in `drawn.py`). Never louder than Andrew, and never in the first 7 s except a bleep that is covering a swear — which should not happen, because there should be no swear there to cover.
- **Bleep:** on the swear only, full length of the word, level with or just under the voice so the tone is obvious. Prefer `bleep-0.3s.wav` for a one-syllable bleep; use 0.6 s or `make_bleep.py` for a longer mask.
- **Record scratch / sad trombone / boing:** one-shot, usually in a pause or on a cut, not under a safety line. Trombone is the longest (1.93 s) — leave it room after the joke lands.

These names are **not** already in Claude's `sfx/v2/` kit. Using them in a render means pointing at this folder (or copying the wavs in) — do not invent a pipeline name, and do not drop them into `sfx/v2/` unless Social Studio asks for that as a pipeline change.
