# Production spec: audio, voice and pacing, v2 (Meatball Myths YouTube + TikTok)

**Owner:** Social Studio lane. **Written:** Sun Nov 15, 2026, about 7:45 PM ET, by Jarvis, from a measured audit of 26 of our own videos.
**Evidence:** [channels/analytics/2026-11-15-audio-engagement-audit.md](analytics/2026-11-15-audio-engagement-audit.md) and the raw numbers in [channels/analytics/data/audio-audit-1115.csv](analytics/data/audio-audit-1115.csv).
**Applies to:** every new render from Nov 17 on, through `tools/drawn.py` (and its `drawn_*` builders) in `mooneyn60-art/skills` → `skills/oh-meatball/`. Videos that are already posted are not re-edited.
**Doesn't change:** the locked voice (edge-tts `en-US-AndrewMultilingualNeural`, approved 11/1), the TikTok swearing orders, the AI-content label, the fact-check and transcript gates, or anything in YouTube Studio or TikTok settings.

Honest headline: none of the mix numbers (loudness, music level, voice pitch) explain on their own why a video won or lost. Topic and hook explain most of it (house bugs and spiders, "your house" hooks, news on TikTok). The audio fixes below raise the ceiling and remove measured defects. The pacing fixes (speech rate, cut rate) are the audio and visual levers that *did* line up with the winners.

---

## 1. Music: duck it under the voice (top fix)

**What we measured:** on the current drawn v6 Shorts (spec `music_db: -13`), the music sits only **10-12 dB under the voice while he is talking** and comes up just **0-3 dB** in pauses, so it's a flat bed that never gets out of the way. Older Oct videos built with sidechain ducking measured **11-17 dB** of ducking, with the music about 27 dB under the voice. Across 26 videos the voice-to-music gap runs from **1.1 LU** ("6 Creatures Living In Your House", 3 views) to **34 LU** (no music at all). There's no house standard. The cause is in code: `drawn.py mix_audio()` ducks the SFX bus under words (`sfx_duck_db -6`) but multiplies the music by one fixed gain (`music_db`) for the whole video.

**Spec:**
| Setting | Value |
|---|---|
| Music under spoken words | **-20 dB below the voice** (accept -18 to -22) |
| Music in pauses of 0.4 s or longer, intros, outros, reveals | swell to **-12 dB below the voice** |
| Duck attack / release | 40 ms / 180 ms (no audible pumping on single-word gaps) |
| Spec keys | `"music_db": -15`, `"music_duck_db": -8`, `"music_duck_release_ms": 180` |

**Code change for Claude (in `tools/drawn.py` `mix_audio`, about 6 lines):** reuse the existing `talk` envelope (already smoothed with 40 ms ramps) for the music bus:
```python
mduck = 10 ** (spec.get("music_duck_db", 0) / 20)          # 0 dB = old behaviour (no duck)
rel = max(1, int(spec.get("music_duck_release_ms", 180) / 1000 * SR))
mt = np.convolve(talk, np.ones(rel, np.float32) / rel, mode="same").clip(0, 1)   # slower release than the sfx duck
mus *= 1 - mt * (1 - mduck)
```
Verify with `DRAWN_SFX_STATS=1` plus a stem check (the demucs script `channels/analytics/data/audio-audit-stems.py` reports `music_under_voice_db` and `ducking_db`). **Pass:** music under voice is between -18 and -22 dB, and ducking is 6 dB or more.

## 2. Music choice: stop using one bed for everything

**What we measured:** every spec in `channels/scripts/` uses `mystery` (YouTube) or `detective` (TikTok), both procedural beds from `tools/music.py`. In `scripts/drawn-tt/`, 111 of 113 specs use `mystery` (the other 2 use `cold-war`). Measured bed tempo on the clips clusters at 96-129 bpm. So every Short sounds alike, which also doesn't help the "repetitive content" risk Social Studio flagged ([S8] in the view-jail plan).

**Spec (all beds already exist in `music.py`; no licensing needed):**
| Series / moment | Bed | Why |
|---|---|---|
| Things Living In Your House, Is This Spider Venomous? | `eerie` (128 bpm, riser plus a dark bell on each reveal) for "creepy" bugs, `detective` (112 bpm pizzicato) for "good bug, don't squish" | tension vs relief matches the stay/squish payoff (`playful` was already judged too happy, per the `eerie` note in `music.py`) |
| Would Meatball Survive? | `cold-war` (120 bpm ticking strings) | the danger clock |
| Pets (cats/dogs) | `absurd` (126 bpm pizzicato march) or `detective` | lighter; pets were our weakest topic with the dark bed |
| News explainers (TikTok) | `science` or no bed, with voice only plus SFX | the FAA cut, our biggest TikTok post (17,600 plays), measured the bed 13 LU under the voice; clarity first |
| Long-form | change bed **per chapter** (at least 3 per video), with `music_reveals` hits on each reveal | long-forms are 5-12 min of one loop today |

- **Reveal moments:** drop the music out for 0.3-0.5 s right before the reveal line, then hit (the `gaps()` / `hit_sound()` helpers already exist; turn them on for non-counter videos too).
- **The last 1.5 s of a looping Short:** bring the bed back up to -12 dB so the loop seam is music, not silence.

## 3. Voice: keep Andrew, change the pacing and add contrast

**What we measured:**
- **Speech rate (YouTube Shorts, transcribed):** the top 5 talked at a median of **205 words a minute** (161-232); the bottom 5 at **171** (165-203). 4 of the top 5 were at 196 or more, and 4 of the bottom 5 at 172 or less.
- **Voice pitch:** the same voice on every video (median 95-143 Hz), with a pitch spread (IQR) of **6.9 semitones on the top 5 vs 6.4 on the bottom 5** (YT) and 6.7 vs 6.9 (TikTok). Pitch flatness within a line is *not* what separates winners. The flatness is across lines: every line has the same rate and pitch.

**Spec:**
| Setting | Value |
|---|---|
| Shorts speech rate | **195-215 wpm** measured on the transcript (postkit `voicecheck` already transcribes; add `wpm` to its output). Start at spec `rate: "+14%"` and adjust per script; don't trust the % alone, since punctuation changes it |
| TikTok minute cuts | 180-200 wpm (the jokes need landing room) |
| Long-form | 175-195 wpm (lion v2 is planned at 194.5, fine) |
| Per-line contrast (new optional beat keys `rate`, `pitch`) | **Hook line:** `rate +18%`, `pitch +6Hz`. **Reveal line:** `rate +4%`, after a 0.25-0.35 s pause. **Joke/reaction:** `pitch +8Hz`. **Safety/attribution:** spec default |
| Pauses | max 0.35 s inside a Short, apart from the one planned pre-reveal beat. Nothing silent over 0.7 s anywhere unless music swells into it |

**Code change for Claude:** in `drawn.py` `tts()` callers (lines ~272-289 and ~464-472), use `b.get("rate", rate)` and `b.get("pitch", pitch)`. The cache key already includes rate and pitch, so changed lines re-voice correctly.

**Voice processing (not measured, best practice):** the Edge voice goes into the mix raw (Kokoro gets an EQ/compressor chain in `free_voice.py`; Andrew doesn't). Apply the same chain **without the `aecho` room**: `highpass=f=70, equalizer=f=180:g=+2, equalizer=f=3200:g=+2.5, equalizer=f=7500:g=-2, acompressor=threshold=-20dB:ratio=3:attack=8:release=120`. This gives presence on phone speakers. A/B it once by ear before adopting.

**Voice A/B (needs Moondog88's yes, because the voice is locked):** one 2-week test of a second, more expressive narrator on one series only (candidates already sampled in `research/39-voice-tests`). Don't switch without his okay.

## 4. Sound effects: fewer, but meaningful

**From code (not measured per video):** `cut_whoosh: true` puts the same soft whoosh on **every** line change (gain 0.22, ducked 6 dB under words, max 2 cues a line).

**Spec:**
- Whoosh only on **location changes**, not every line. `cut_whoosh: "scene"` (Claude: only fire when `stage.scene` changes between beats).
- **One signature sting per series** on the reveal (e.g. "TLIYH" = a creaky-door + bell, "Spider Venomous?" = a sharp string stab, "WMS" = a heartbeat that stops).
- A comic SFX on a joke punchline (pop, record scratch, splat) at **-6 dB under the voice peak**, one every 4-6 s at most on TikTok cuts.
- Keep the SFX ducked under words (`sfx_duck_db -6`).

## 5. Loudness and master

**What we measured:**
| Format | Integrated (median, range) | True peak |
|---|---|---|
| YouTube Shorts (10) | **-15.4 LUFS** (-16.0 to -14.2) | -4.4 to -1.1 dBTP |
| Long-forms (6) | -14.6 (-15.4 to -14.1) | -4.3 to -1.2 |
| TikTok as served (10) | -12.4 (-14.4 to -12.1) | **one at +0.26 dBTP** (clipping), rest -1.4 to -0.6 |

YouTube turns loud videos down but doesn't turn quiet ones up, so a -16 Short plays about 2 dB quieter than a -14 competitor in the feed. Cause: Shorts get **single-pass** `loudnorm=I=-14` in `drawn.encode_cmd`, which undershoots on 15-30 s clips. Long-form builders already use the two-pass linear version (`drawn_catlife.py`, `drawn_treecheck.py`).

**Spec:** every master (Shorts, TikTok, long-form) uses **two-pass linear loudnorm: I = -14 LUFS (±0.5), TP = -1.5 dBTP, LRA ≤ 11**, after an `alimiter` at -2 dBFS. Reuse the `drawn_catlife.py` two-pass function in `encode_cmd` (or as a post-pass). **Gate:** fail the render if integrated loudness is outside -14.5 to -13.5 or TP is above -1.0. The output stays mono (fine for phones); stereo is optional.

## 6. Hooks (first 3 seconds)

**What we measured (transcribed openings):**
- **Top openings:** "One bug in your house can put you in the hospital. One protects you" (2,289 views), "Meatball, your roach is carrying 40 babies" (1,988), "Something with 30 legs hunts in your house tonight" (TikTok 4,040), "You just saw the 30-legged bug in your bathroom. Don't squish it." (TikTok 5,376).
- **Bottom openings:** "A Chicago physicist worked out how to nuke the moon" (10), "When it's scared, this animal fakes its own death" (TikTok 123), "What if I told you the CIA built a fake mining ship…" (TikTok 86), "Your dog's guilty look may not be a confession" (3).

**Spec:** the first spoken line is **second person + a place in your home + a number or a threat/stakes**, at most 12 words, and starts at 0.00 s (already true on all 26). No third-person setup, history or "what if I told you". The hook line gets the per-line hook prosody above, and the music enters at -12 under the voice on frame 0 (not faded in).

## 7. Visual pacing (tied to the same data)

- **Cut rate:** median **19.6 cuts a minute (2.5 s average shot) on the top 5 YT Shorts vs 12.4 (4.0 s) on the bottom 5**; TikTok **14.2 (4.0 s) vs 8.5 (6.6 s)**. The best long-form ("3 Bugs…", 213 views) cuts **13.2 a minute (4.5 s)**, against 5.0-6.4 (9-12 s) on every other long-form. The two biggest Shorts (Daddy Longlegs and House Centipede) are slow-cut, so this is a lean, not a law. It supports Social Studio's 2-4 s shot test. **Spec:** Shorts 2-3 s average shot; long-form 2-4 s (as in the pacing rule); no framing held over 4 s.
- **Drawn mammals (observed on contact sheets, not measured):** the bear, dog and lizard in three bottom performers share the same generic four-legged body. Pets and big animals underperform on both platforms. Give each animal its silhouette tells (bear hump and claws, dog ears and tail) before more pet/WMS Shorts.
- **Captions:** all 26 have burned-in word captions. Keep them; keep the yellow keyword highlight.

## 8. Render checklist (add to `postkit.py render`)

1. Transcript matches the script (existing).
2. `wpm` is in range for the format (§3).
3. Stem check: music under voice is -18 to -22 dB, and ducking is 6 dB or more (§1).
4. Integrated loudness -14 ±0.5 LUFS, TP ≤ -1.0 dBTP (§5).
5. First word at ≤ 0.1 s; hook line passes §6.
6. Scene cuts: average shot ≤ 3 s (Shorts) / ≤ 4 s (long-form).
