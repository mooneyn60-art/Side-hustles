# Sound cue sheet: first two 11/16 render samples

Draft only, Monday, Nov 16, 2026 (America/New_York). Box path: `/workspace/drafts/sound-cues-1116.md`. Intended for `channels/shorts-push-1116/sound-cues.md` (Social Studio commits). Nothing here was committed, rendered, or posted. No pipeline or TTS changes.

**Why this exists.** Moondog88 said the content feels boring. Social Studio's review: the voice is flat, the top Short has no music, and there is no SFX. This sheet is for Claude to implement on the first two sample renders, using only direction the current renderer can already do.

**Scripts used (GitHub `mooneyn60-art/Side-hustles`, `main`, `channels/shorts-push-1116/` — every file read):** `index.md`, `bed-bugs.md`, `wms-wednesdays-ep1-4.md`, `wms.md`, `spider-venomous.md`, `reply-to-comment.md`, `rulings-1116.md`, `factcheck-shorts-push-1116.md`. Spoken lines below are the current scripts (`bed-bugs.md`, `wms-wednesdays-ep1-4.md`). Fact-check of these two Shorts: Pass (do not change hedge words: "likely won't", "may", "especially if", "Large", "up to", "probably not", "Nothing's guaranteed"). The `index.md` inventory hook for bedbug-lights is behind the script; this sheet uses the script.

**Locked voice (do not change):** `en-US-AndrewMultilingualNeural`, top-level `rate: "+10%"`, `pitch: "+3Hz"`.

**Labels.** **SOURCED** = observed in a cited repo file. **JUDGMENT** = a mix recommendation, not a measured finished cut and not a go-ahead to invent pipeline features.

---

## Pipeline facts (what Claude can actually do)

All of this is **SOURCED** from `mooneyn60-art/skills` branch `claude/youtube-monetization-strategy-m9vz6i`, mainly `skills/oh-meatball/tools/drawn.py`, `skills/oh-meatball/tools/music.py`, `skills/oh-meatball/sfx/LICENSE.txt`, and `skills/oh-meatball/tools/make_sfx2.py`. Current Shorts JSON in Side-hustles (`channels/scripts/*-v6-yt.json`, `tt-*.json`, `tts-*.json`) already use the top-level fields `voice`, `rate`, `pitch`, `music`, `music_db`, `cut_whoosh`, `loop`.

### Voice (Andrew)

The renderer **does** speak each beat as its own edge-tts clip (`drawn.py` `plan()`: `tts(b["say"], voice, rate, pitch, ...)`). **It does not** read a per-line `rate` or `pitch`. Those come only from the top-level spec. Do not add beat-level rate/pitch for this pass.

Free edge-tts also rejects custom SSML (prior 11/15 listen-test). Do not put `<emphasis>`, `<break>`, `<prosody>`, or `<phoneme>` in `say`.

**Methods this sheet uses (all already wired):**

| Method | How | Field |
|---|---|---|
| Punctuation | commas, ellipses (`...`), em dashes, question marks — edge-tts pauses on these | beat `say` (words and hedges stay the same) |
| Sentence splits | already in the scripts (two short sentences on the gag / verdict). Do not add new beats just for pace; that would reshuffle cards and scenes | beat `say` |
| Inserted silence | `pad` is seconds of silence **after** the trimmed speech of that line (`dur = speech + b.get("pad", 0.08)`). Default if omitted: **80 ms**. Express gaps in ms here; write seconds in JSON (`0.25` = 250 ms) | beat `pad` |

A 11/15 hook note (`shorts-hooks-1s-1115.md`) asked for no added silence beyond a ~80 ms loop pad. This sheet uses slightly longer pads before punchlines because Social Studio now wants a less-flat read. Pads below keep each Short inside the 16–20 s YouTube band, measured on the script's 194.5 wpm word time plus the pads (actual TTS length will differ after `trim_air`).

### Music

`spec.music` is a `tools/music.py` bed **kind**, rendered to the exact length of the video, loop-safe. Current YouTube v6 scripts use `music: "mystery"`; TikTok / `tts-*` twins use `music: "detective"`. Keep `music_db: -13` **as-is** (every current short-form JSON; Social Studio 11/15: do not change the number). Keep `loop: true`.

Kinds in `music.py` `BEDS` (BPM / feel from that file's docstrings):

| Kind | Feel | BPM |
|---|---|---|
| `mystery` (alias `conspiracy`) | dark pulsing synth, bass in eighths, clock ticks, plucked minor-second tension, pad | 96 |
| `detective` | lighter curious pizzicato, walking pizz bass, snaps | 112 |
| `ocean` | low drones, wave wash, sonar pings | 60 |
| `cold-war` | tense ticking strings, staccato ostinato, cello pedal, clock tick | 120 |
| `ufo` | eerie theremin, hollow pads, high shimmer | 72 |
| `absurd` | mischievous pizzicato march, oom-pah, woodblock | 126 |
| `science` | square-wave arpeggio, sub pulse, static crackle | 124 |
| `waltz` | eerie music-box waltz in 3/4 | 150 |
| `playful` | bright explainer pop, marimba + glock; **continuous** (no drop-out) | 160 |
| `eerie` | chorused e-piano / music-box, G# minor; **continuous** (no drop-out) | 128 |
| `sleep` | soft slow pad, no beat, no hits (sleep-compilation bed) | none |

**Gap (SOURCED):** `music.py` can rise into reveal times, drop out before a stamp, and hit on the stamp — but `drawn.py` `mix_audio()` only passes reveal times when `music_reveals` is `"counter"`. These Shorts have no counter, so the mixer currently plays **one bed for the whole duration** at `music_db: -13`. Desired shift points below are mix intent, not a new field. Do not invent `music_reveals` values or change the mixer for this pass. Kind choice does the work.

Do **not** use `themes.py` theme `"animals"` (`music/quiz-bed.m4a`). That path also rewrites rate/pitch/tempo and would break the locked voice.

### SFX

Default kit: `sfx_kit: "v2"` (`drawn.py` loads `skills/oh-meatball/sfx/v2/{name}.wav`, then falls back to `skills/oh-meatball/sfx/{name}.wav`).

Beat field: `"sfx": ["name@word", "name@0.4"]` — a kit name at a word in that line, or a time in seconds inside the beat. **At most 2 cues per line, and 0.5 s between any two cues** (`SFX_MAX=2`, `SFX_GAP=0.5`).

`cut_whoosh: true` (already on every current short-form JSON): a soft `whoosh` at each line change, **80 ms before** beats 2…N. There is **no** automatic whoosh at 0.00 s. Because of the 0.5 s gap, a line's own `sfx` will be dropped if it sits within 0.5 s of that whoosh — so do not place a line SFX in the first ~0.42 s of beats 2…N.

Defaults, keep as-is: `sfx_gain: 0.22`, `sfx_duck_db: -6` (SFX is ducked 6 dB under spoken words).

**v2 names (do not invent others):**

| Name | What it is (from `make_sfx2.py` / `sfx/LICENSE.txt`) | In v2? | In `sfx/` root? |
|---|---|---|---|
| `whoosh` | soft cloth swish (Kenney RPG Audio cloth2, CC0) | yes | yes (older synth in root) |
| `boing` | soft landing bump (Kenney Impact, CC0) | yes | yes |
| `pop` | leather drop (Kenney RPG Audio, CC0) | yes | yes |
| `scratch` | paper flick (Kenney RPG Audio bookFlip2, CC0) | yes | yes |
| `thud` | soft heavy bump (Kenney Impact, CC0) | yes | yes |
| `hit` | light body punch (Kenney Impact, CC0) | yes | yes |
| `tink` | soft light tap (Kenney Impact, CC0; in SOFT, −8 dB) | yes | yes |
| `click` | short tap / clock ticks (Kenney Impact, CC0; SOFT) | yes | yes |
| `step` | one grass footstep (Kenney RPG Audio, CC0) | yes | **no** (v2 only) |
| `sting` | series signature cue: low whoomp + warm pluck (synthesized in `make_sfx2.py`, nothing to license) | yes | **no** (v2 only) |
| `zap` | electric crackle; kit comment: **unused, too sharp** | yes | yes |
| `splash` | synth / v1 copy (ffmpeg lavfi; LICENSE) | yes (copy) | yes |
| `crunch` | Kenney Impact, CC0 | yes (copy) | yes |
| `plate` | Kenney Impact, CC0 | yes (copy) | yes |
| `stamp` | rubber-stamp thump + paper slap (synthesized in `investigate.py`) | yes (copy) | yes |
| `case` | typewriter clacks into a dun-DUN sting (synthesized in `investigate.py`) | yes (copy) | yes |

A separate file `skills/oh-meatball/brand/sting.wav` exists. It is **not** a drawn.py SFX name. Use kit name `sting` (resolves to `sfx/v2/sting.wav`).

---

## Shared first-second hook audio

**SOURCED** (`MASTER_ORDERS.md` v6 template, quoted in `shorts-push-1116/index.md`; also the 11/16 scripts): narration starts at **0.00 s**; frame 0 is the animal already moving; Meatball hops in small at **~2.3 s**; keyword card in seconds 1–4; no spoken countdown, no silent intro.

**JUDGMENT** (this is the fix for "the top Short has no music" / "no SFX"):

- Start the music bed at 0.00 s, `music_db: -13`, `loop: true`. The first second is **voice lead + bed under it**, not a cold open.
- Do not add a pre-roll or a silent count. Do not raise `sfx_gain` to "make the hook hit."
- Any open SFX is short, at or just after 0.00 s, and relies on the existing −6 dB duck under the hook words so Andrew stays intelligible in second 1.
- Meatball's hop at ~2.3 s (still on line 1) can take a second cue; it is more than 0.5 s after 0.00 s.

---

## 1. `wmsw-ep1-saltwater-crocodile`

Source: `channels/shorts-push-1116/wms-wednesdays-ep1-4.md`. 56 words, **17.28 s** at 194.5 wpm (word time only). Title: *Would Meatball Survive a Saltwater Crocodile?* Series open: WOULD MEATBALL SURVIVE? WEDNESDAYS · EP 1.

**Top-level (implement these):** `voice` / `rate` / `pitch` locked as above; `music: "ocean"`; `music_db: -13`; `cut_whoosh: true`; `loop: true`; `sfx_kit: "v2"`; leave `sfx_gain` / `sfx_duck_db` at defaults.

**Music.** **JUDGMENT**, kind **SOURCED** from `music.py`: use `ocean` (60 bpm, low drones, wave wash, sonar pings) — a real pipeline name, and a better fit than the house YouTube default `mystery` for a billabong / river Short. Keep `-13`. Do not use `sleep` (no beat; would keep the cut feeling flat). If a TikTok twin is cut later, this repo's pattern is `detective`; for this YouTube sample render, use `ocean`.

Desired feel at story beats (intent only; reveals are not passed today): hook (L1) already moving, wave wash under the hour figure; gag (L2) can stay the same bed; rise under the knee-deep attack (L3) and the Queensland rule (L4); let the bed breathe under the VERDICT stamp (L5) so the stamp + "probably not" land; keep enough bed under the loop line (L6) that the loop has no silent seam.

Times below are **script estimates at 194.5 wpm with no pad**. Real `t0` comes from TTS + `pad`.

### Line-by-line

**L1 — hook.** Est. 0.00–3.39 s. CB28.

- Original `say`: `Large saltwater crocodiles can stay underwater up to an hour. You?`
- Punctuation (JUDGMENT; words unchanged): `Large saltwater crocodiles can stay underwater up to an hour... You?` — method: **ellipsis** before the punch `You?`
- Speed: baseline (locked rate). Let the ellipsis make the hour-figure land, then the question.
- Emphasis (JUDGMENT, punctuation only, no SSML, no all-caps): **up to an hour**, **You?**
- `pad`: **200 ms** (`0.20`) after the line — pause before the gag.
- SFX: `sting@0.0` (series open. **SOURCED** from the EP 1–4 script: "the same short sting on every episode" from frame 0; kit name **SOURCED** from `make_sfx2.py`: "the series' signature cue"). And `boing@2.3` for Meatball's hop (**JUDGMENT**; `boing` = v2 soft landing bump). Two cues, 2.3 s apart. First-second audio: voice + `ocean` at −13 + short ducked `sting`.

**L2 — gag.** Est. 3.39–6.48 s. (Meatball already hopped at ~2.3 s, during L1.)

- Original `say`: `Meatball held his breath. His cat, Sauce, stopped the stopwatch.`
- Punctuation (JUDGMENT): `Meatball held his breath... His cat, Sauce, stopped the stopwatch.` — method: **ellipsis** between the two sentences (already a sentence split).
- Emphasis: **held his breath**, **stopped the stopwatch**.
- `pad`: **250 ms** (`0.25`) after the gag, before the danger fact.
- SFX: `click@stopwatch` (**JUDGMENT**; `click` = short tap / clock ticks). Do not put a cue on "Meatball" — `cut_whoosh` sits 80 ms before this line. One cue only.

**L3 — fact.** Est. 6.48–10.18 s. CB27.

- Keep `say` as written: `They can attack in knee-deep water, so even wading can be dangerous.` (commas already do the work.)
- Emphasis: **knee-deep**, **wading**, **dangerous**.
- Speed: baseline. `pad`: **80 ms** (`0.08`, default).
- SFX: `splash@attack` (**JUDGMENT**; `splash` is a real kit name, v1/v2 copy). Mid-line, clear of the whoosh.

**L4 — safety rule.** Est. 10.18–13.27 s. CB42.

- Punctuation (JUDGMENT): `Queensland's rule where they live: keep out of the water.` — already has a colon; leave it. Do not add drama that softens the official rule.
- Emphasis: **keep out of the water**.
- `pad`: **300 ms** (`0.30`) — pause **before the verdict punchline**.
- SFX: none besides `cut_whoosh`. No kit name is a warning-sign or "stay back" cue. Do not invent one.

**L5 — verdict.** Est. 13.27–15.73 s. CB50.

- Original `say`: `Verdict: in the water, probably not. Nothing's guaranteed.`
- Punctuation (JUDGMENT): `Verdict: in the water... probably not. Nothing's guaranteed.` — method: **ellipsis** before **probably not**; the second sentence stays the house closer.
- Emphasis: **probably not**, **Nothing's guaranteed**.
- `pad`: **200 ms** (`0.20`) before the loop question.
- SFX: `stamp@probably` (**JUDGMENT**; `stamp` = rubber-stamp thump, matches the VERDICT stamp). Anchored on "probably", not line start, so it is not dropped next to `cut_whoosh`.

**L6 — loop / comment question.** Est. 15.73–17.28 s.

- Keep `say`: `Would you wade in? And` (question mark already there; last line must still end on `And` and flow into the hook).
- Speed: do not slow this line; it is the loop seam.
- `pad`: **80 ms** (`0.08`) — the tiny loop pad.
- SFX: `cut_whoosh` only.

**Pad budget.** Word time 17.28 s + pads 0.20+0.25+0.08+0.30+0.20+0.08 = **18.39 s** estimated, still inside 16–20 s. If a real TTS take runs long, shrink L4's pad first, then L5, never the hook start.

---

## 2. `bedbug-lights`

Source: `channels/shorts-push-1116/bed-bugs.md` (ruling 2 already applied: hook is "Sleeping with your lights on likely won't deter hungry bed bugs."). 55 words, **16.97 s** at 194.5 wpm (word time only). Title: *Do Lights Keep Bed Bugs Away? 💡 (Things Living In Your House)*.

**Top-level:** same locked voice; `music: "mystery"`; `music_db: -13`; `cut_whoosh: true`; `loop: true`; `sfx_kit: "v2"`; default SFX gain/duck.

**Music.** **JUDGMENT**, kind **SOURCED**: use `mystery` (96 bpm, dark pulse, clock ticks) — the house YouTube v6 music name already on Side-hustles `*-v6-yt.json`, and the clock-tick bed fits a night / feeding-cycle Short. Keep `-13`. Do not use `sleep` (that bed is a no-beat sleep-compilation pad and would keep this feeling flat). `eerie` (128 bpm, continuous, no drop-out) is a valid alternate if the `mystery` take feels thin under a loop; it is not the first pick, because YT samples in this repo already say `mystery`.

Desired feel (intent only): tense from 0.00 s under the "lights on" hook; same bed under the flashlight gag; clock-tick character can sit under "feeding cycle" (L3) and the day-feeding fact (L4); do not let the bed disappear on the loop line.

### Line-by-line

**L1 — hook.** Est. 0.00–3.39 s. BB32.

- Keep `say` as written: `Sleeping with your lights on likely won't deter hungry bed bugs.` Do not move "likely" or "won't" (fact-check hedge). Optional UKY wording ("is not likely to") is **not** applied here.
- Punctuation (JUDGMENT): `Sleeping with your lights on... likely won't deter hungry bed bugs.` — method: **ellipsis** after the folk trick, then the hedged payoff. Words unchanged.
- Emphasis: **lights on**, **likely won't**, **hungry**.
- Speed: baseline. `pad`: **200 ms** (`0.20`).
- SFX: no series `sting` (this is not a WMS Wednesdays episode). First second = voice + `mystery` at −13, no open hit covering the hook. `boing@2.3` for Meatball's hop (**JUDGMENT**). One cue on this line.
- No kit name is a "lamp switch" or "bed bug walk." Do not invent one, and do not use `zap` (kit: unused, too sharp).

**L2 — gag.** Est. 3.39–7.40 s.

- Original `say`: `Meatball taped a flashlight to the headboard. His dog, Noodle, carried it off.`
- Punctuation (JUDGMENT): `Meatball taped a flashlight to the headboard... His dog, Noodle, carried it off.` — method: **ellipsis** between the two sentences.
- Emphasis: **taped**, **carried it off**.
- `pad`: **250 ms** (`0.25`).
- SFX: `pop@carried` (**JUDGMENT**; v2 `pop` = leather drop, for Noodle taking the flashlight). There is **no** tape-peel or flashlight-click name in the kit. Do not invent one; do not reuse `click` here (saved for the clock on L3). Keep this cue mid-line, clear of `cut_whoosh`.

**L3 — fact.** Est. 7.40–10.18 s. BB32.

- Keep `say`: `They'll adjust their feeding cycle to your sleep patterns.`
- Emphasis: **adjust**, **feeding cycle**, **your sleep patterns**.
- `pad`: **80 ms** (`0.08`).
- SFX: `click@cycle` (**JUDGMENT**; `click` is documented as clock ticks — matches the clock-face visual).

**L4 — fact.** Est. 10.18–14.50 s. BB16.

- Keep `say`: `Hungry ones may even feed by day, especially if that's when you normally sleep.` Keep **may** and **especially if**. The commas/condition already slow the second half.
- Emphasis: **may**, **by day**, **especially if**.
- `pad`: **300 ms** (`0.30`) — a hold before the loop question (this Short has no spoken verdict stamp).
- SFX: none besides `cut_whoosh`. No "daylight" or "creep" name in the kit.

**L5 — loop / comment question.** Est. 14.50–16.97 s.

- Keep `say`: `Lights on or off when you sleep? And`
- Emphasis: **Lights on or off**. Do not slow the loop seam.
- `pad`: **80 ms** (`0.08`).
- SFX: `cut_whoosh` only.

**Pad budget.** Word time 16.97 s + pads 0.20+0.25+0.08+0.30+0.08 = **17.88 s** estimated, inside 16–20 s. If TTS runs long, shrink L4's pad first.

---

## Implementer checklist (Claude)

For each of the two specs:

1. Keep Andrew at +10% / +3Hz. Do not add beat-level rate/pitch, SSML, or a `themes.py` override.
2. Write the punctuated `say` strings above (same words). Set per-beat `pad` as listed.
3. Set `music` and `music_db: -13`, `loop: true`, `cut_whoosh: true`, `sfx_kit: "v2"`.
4. Set beat `sfx` arrays exactly as listed, using only the names in the v2 table. Honor the 2-cues / 0.5 s rule, and do not place a cue in the first ~0.42 s of beats 2…N.
5. Leave `sfx_gain` 0.22 and `sfx_duck_db` -6. Confirm in the take that second 0–1 is voice-led (hook words clear over the bed; open `sting` on EP 1 ducked).
6. Human-listen the two takes for pace and whether hyphen-free punctuation actually added pauses. Adjust `pad` only if the cut breaks 15–20 s or the loop slams.

---

## Gaps

- These two Shorts are markdown only on GitHub. They have no render JSON yet, so they currently have **no** `music`, `music_db`, `cut_whoosh`, `pad`, or `sfx` fields — which matches the review (no music, no SFX, flat one-rate Andrew).
- Per-line rate/pitch is **not** supported, even though TTS is per line. Pace is punctuation + `pad` only.
- Music energy shifts at story beats are **not** wired unless the Short has a counter and `music_reveals: "counter"`. No other reveal-time field is in `drawn.py` `mix_audio()`.
- No pipeline SFX for: tape peel, flashlight / lamp switch, bed-bug walk, water ripple (as distinct from `splash`), warning-sign hit, or crocodile submerge. Those were not invented; the lines either use a nearby real name or take no extra cue.
- `zap` exists but is documented as unused / too sharp — not used here.
- `brand/sting.wav` and `brand/music/quiz-bed.m4a` exist in the skills repo but are not the current Shorts path (`drawn.py` + `music.py` kinds + `sfx/v2`).
- `sfx/v3-proto/` is an older, smaller kit (no `sting`, `click`, `step`, `stamp`, `case`). Do not point these renders at it.
- Channel-brain (`skills/channel-brain/`) has no SFX or music asset list. The names came from `skills/oh-meatball/` (tools + `sfx/`), plus Side-hustles script fields `music`, `music_db`, `cut_whoosh`.
