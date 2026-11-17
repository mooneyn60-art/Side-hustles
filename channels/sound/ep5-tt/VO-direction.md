# EP5 TikTok ending VO — direction and takes

Draft written Monday, Nov 16, 2026, about 9:33 p.m. (America/New_York). **APPROVED by Social Studio 2026-11-16:** `t1-hobo-take2.wav` and `t2-tub-take2.wav`. Box path was `/workspace/sound/ep5-tt/`; this copy is `channels/sound/ep5-tt/`. Due Tuesday, Nov 17, 2026, 3:00 p.m. ET. Nothing here was posted or wired into the pipeline.

**Source.** `/workspace/shorts/tiktok-cuts/ep5/cut-plan.md`. T1 and T2 ending lines, exact wording:

- T1 cliffhanger (Part 1/3 end, T2's first line voiced in T1's VO): **Is it a hobo spider?**
- T2 cliffhanger (Part 2/3 end, T3's first line): **How do I get a tub spider out?**

The cut plan does **not** specify a spoken lead-in for these endings. The joke just before each line stays in the existing VO ("Sauce slept through all of this." on T1; "Mix-up fixed. Meatball's ego, not so much." on T2). The `PART 2 ▶` / `PART 3 ▶` cards are silent and sit over the last 1.0 s of the picture. These files are the cliffhanger lines only, using the cut-plan wording (not T3's script hook "How do I get a spider out of the tub?").

**Voice (locked, unchanged).** edge-tts `en-US-AndrewMultilingualNeural`, rate `+10%`, pitch `+3Hz`. Confirmed in `meatball-bible.md` (MASTER_ORDERS, approved 11/1). The cut plan does not name a different voice.

Free edge-tts rejects custom SSML, so timing comes from punctuation, ellipses, split clips, and ffmpeg-inserted silences. No per-line rate change.

**Loudness.** Target: about −14 LUFS integrated, true peak ≤ −1 dBTP, measured with ffmpeg `ebur128=peak=true` after a two-pass `loudnorm` (plus light compression and a −1 dBTP limiter so short dry VO could get closer to the target). Takes with a comic pause measure a little quieter on *file* integrated loudness because the silence is in the file; a speech-only figure (pauses removed, then ebur128) is also reported. LRA is 0.0 LU on all of these short clips, which is expected.

**EDL slots** (cut-plan estimates): T1 ending 64.5–66.0 s (1.5 s; the plan also allows render pauses, total ≈ 67–68 s). T2 ending 64.5–66.9 s (2.4 s). Takes were kept in that neighborhood.

---

## T1 — "Is it a hobo spider?"

Payoff word: **hobo**. Emphasis (punctuation only, no SSML): **hobo**, and the question.

### t1-hobo-take1.wav — 1.362 s

- Exact TTS text: `Is it a... hobo spider?`
- Method: punctuation only (ellipsis before "hobo"); one clip, no extra silence.
- Pause: Andrew's built-in ellipsis pause only (about 150–250 ms, not measured as a separate insert).
- File loudness: **I = −14.0 LUFS**, LRA = 0.0 LU, **TP = −1.2 dBTP**. Speech-only: I = −14.0 LUFS, TP = −1.2 dBTP.
- Whisper (session check): tiny.en / base.en / small.en all "Is it a hobo spider?" — pass.
- Tightest take. Use if the 1.5 s EDL slot must be hit exactly.

### t1-hobo-take2.wav — 1.563 s  ← APPROVED by Social Studio 2026-11-16

- Exact TTS text, two clips: `Is it a` + **350 ms** silence + `hobo spider?`
- Method: split clips + ffmpeg silence. Beat is in the 300–500 ms range requested, before the payoff word **hobo**.
- Pause: **350 ms** inserted before "hobo spider?"
- File loudness: **I = −14.9 LUFS**, LRA = 0.0 LU, **TP = −1.3 dBTP**. Speech-only: **I = −14.0 LUFS**, TP = −1.3 dBTP. The file figure is 0.9 LU quieter because of the inserted beat.
- Whisper (session check): tiny.en and small.en "Is it a hobo spider?" — pass. (base.en hallucinated on this short pause-split clip; the other two models agreed.)
- Why it was recommended: a clear comic beat without over-dragging, still close to the 1.5 s slot, speech loudness on target.

### t1-hobo-take3.wav — 1.829 s

- Exact TTS text, two clips: `Is it a` + **500 ms** silence + `hobo... spider?`
- Method: 500 ms beat before **hobo**, plus an ellipsis inside the question to drag it.
- Pause: **500 ms** inserted, then a second, shorter TTS ellipsis between "hobo" and "spider?"
- File loudness: **I = −15.0 LUFS**, LRA = 0.0 LU, **TP = −1.0 dBTP**. Speech-only: **I = −14.2 LUFS**, TP = −1.0 dBTP.
- Whisper (session check): tiny.en and small.en "Is it a hobo spider?" — pass.
- Longest T1 take. Use if the cliffhanger should hang longer under the PART 2 card.

---

## T2 — "How do I get a tub spider out?"

Payoff word: **out**. Emphasis: **tub spider**, **out**.

### t2-tub-take1.wav — 1.588 s

- Exact TTS text: `How do I get a tub spider... out?`
- Method: punctuation only (ellipsis before "out?"); one clip, no extra silence.
- Pause: Andrew's built-in ellipsis only.
- File loudness: **I = −15.6 LUFS**, LRA = 0.0 LU, **TP = −1.0 dBTP**. Speech-only: **I = −15.2 LUFS**, TP = −1.0 dBTP. Could not be raised further without breaking the true-peak cap (short question, high crest factor).
- Whisper (session check): the isolated "out?" after the ellipsis is easy for ASR to mishear; a speech-only small.en pass recovered "Out!" Combined evidence: the words are present, but this is the least clear "out?" of the three.

### t2-tub-take2.wav — 1.788 s  ← APPROVED by Social Studio 2026-11-16

- Exact TTS text, two clips: `How do I get a tub spider` + **350 ms** silence + `out?`
- Method: split clips + ffmpeg silence before the payoff word **out?**
- Pause: **350 ms** inserted before "out?"
- File loudness: **I = −15.4 LUFS**, LRA = 0.0 LU, **TP = −1.0 dBTP**. Speech-only: **I = −14.9 LUFS**, TP = −1.0 dBTP. About 0.9 LU shy of −14 on speech-only; limited by the true-peak cap.
- Whisper (session check): tiny.en "How do I get a tub spider? Out?" · base.en **"How do I get a tub spider out?"** (exact) — pass.
- Why it was recommended: a clean comic beat before "out?", the only T2 take that base.en transcribed exactly, duration sits comfortably in the 2.4 s slot.

### t2-tub-take3.wav — 2.573 s

- Exact TTS text, two clips: `How do I get a` + **450 ms** silence + `tub spider... out?`
- Method: 450 ms beat before **tub spider**, plus an ellipsis before "out?" to drag the question.
- Pause: **450 ms** inserted; additional TTS ellipsis before "out?"
- File loudness: **I = −14.9 LUFS**, LRA = 0.0 LU, **TP = −1.1 dBTP**. Speech-only: **I = −14.1 LUFS**, TP = −1.1 dBTP.
- Whisper (session check): small.en "How do I get a... Tub Spider? Out?" — pass. A little long for a 2.4 s slot (2.57 s); still inside the plan's "render pauses" wiggle room.
- Use if you want a bigger hold before the subject, and the picture can spare the extra third of a second.

---

## Recommended / approved takes

| Cut | File | Duration | Status |
|---|---|---|---|
| T1 | `t1-hobo-take2.wav` | 1.563 s | **APPROVED by Social Studio 2026-11-16** |
| T2 | `t2-tub-take2.wav` | 1.788 s | **APPROVED by Social Studio 2026-11-16** |

Fallbacks if a recut is needed: T1 take1 if the line must stay under ~1.4 s; T1 take3 / T2 take3 for a more dragged question.

---

## Fallback VO direction for Claude (re-render)

Do not change the pipeline. If these takes need a re-render:

1. Voice stays `en-US-AndrewMultilingualNeural`, `rate: "+10%"`, `pitch: "+3Hz"`. No SSML.
2. Spoken text is exactly `Is it a hobo spider?` and `How do I get a tub spider out?` (cut-plan wording). No added lead-in. Do not swap in "How do I get a spider out of the tub?"
3. Preferred method (the approved takes): render two clips and insert **350 ms** of silence with ffmpeg before the payoff word — `hobo spider?` on T1, `out?` on T2.
4. Alternate: a single clip with an ellipsis before the payoff word (`Is it a... hobo spider?` / `How do I get a tub spider... out?`).
5. Trim edge-tts lead-in/tail before inserting the beat (keep ~40–60 ms of natural air on each stem).
6. Loudness-normalize to about −14 LUFS integrated, true peak ≤ −1 dBTP (ffmpeg two-pass `loudnorm`, then `ebur128=peak=true` to measure). On short clips with an inserted pause, also check a speech-only measure; do not raise the voice past the true-peak cap just to make the file-integrated number look like −14.
7. Lay the line under the silent PART card (last 1.0 s of the picture). No CTA in the audio.

---

## File list

- `t1-hobo-take1.wav`
- `t1-hobo-take2.wav` (APPROVED by Social Studio 2026-11-16)
- `t1-hobo-take3.wav`
- `t2-tub-take1.wav`
- `t2-tub-take2.wav` (APPROVED by Social Studio 2026-11-16)
- `t2-tub-take3.wav`
- `VO-direction.md`
