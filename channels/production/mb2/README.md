# mb2: Meatball animation pipeline v2 (prototype)

Built by Jarvis on 2026-11-15 to test a visual upgrade for the Meatball Myths channel (YouTube + TikTok). It covers the Meatball channel only; nothing here touches FurEver Faces, Etsy or Shopify. It hasn't been posted or scheduled anywhere.

It re-renders an already fact-checked, already posted script (Would Meatball Survive? #3, the grizzly, `scripts/drawn-house/grizzly-wms-v6-yt.json` in `mooneyn60-art/skills`) word-for-word in three candidate styles, so Moondog88 can keep or toss each one.

| Style | What it is | Cost |
|---|---|---|
| `rig` (A) | Fully procedural vector: a new Meatball puppet rig (squash and stretch, blinks, brows, lip flap from the voice, run cycle, poses), species rigs with real silhouettes (grizzly hump and claws, horse), parallax forest/snow, camera punch-ins, impact frames, speed lines, a new composition every 1.3 s | $0, about 35 s to render |
| `panels` (B) | Illustrated key-art panels (6 images in `art/`, made with the built-in image generator from a character reference sheet) animated with Ken Burns moves, punch-ins, shake, flashes and FX, cut every 1.3 s | 6 images per Short (no cash cost); consistency needs a reference sheet |
| `hybrid` (C) | Panels for the money shots (hook, play dead, fight, loop), rig animation for the action beats | Same as B |
| **`hybrid2` (C v2, HOUSE STYLE since 11/15)** | C with the clash fixed: panels regenerated from the one locked sheet `art/meatball_ref_sheet_v1.jpg`; rig restyled to the panels (screen-constant 11 px / 7 px ink lines, palette sampled from the sheet and panels, painted gradient shading, fur-tuft bear edges, gloss on the sauce); rig shots sit on a painted plate (`art/bg_forest_plate.jpg`) in the same style; one grade + paper grain + slight softening over every shot; diagonal ink-wipe on every panel<->rig cut (whoosh on each) | about 4 images per Short + 1 plate per location |

All three share the audio from `channels/production-spec-audio-v2.md`: Andrew voice at +14% (hook line +18%/+6Hz), about 190-205 wpm, presence EQ and compression, a procedural "danger clock" bed ducked under the voice, synthesized SFX on location changes and hits only, and mastering. v2 mastering (`audio.master`) is gain + 4x-oversampled limiter, measured on the encoded AAC and iterated to -14.0 ±0.1 LUFS, TP ≤ -1.5 dBTP (`REMASTER=1` re-does the sound on an existing render without re-drawing).

## Run
```
python3 -m venv .venv && .venv/bin/pip install skia-python edge-tts numpy pillow
.venv/bin/python channels/production/mb2/render.py rig out.mp4 --label "OPTION A"    # or panels / hybrid
.venv/bin/python channels/production/mb2/render.py hybrid2 out.mp4                  # house style (C v2)
.venv/bin/python channels/production/mb2/thumbs_v2.py out_dir/                        # v2 thumbnails + 168x94 phone checks
STILLS=0.6,2.2 .venv/bin/python channels/production/mb2/render.py hybrid2 x.mp4     # PNG stills only, for checks
.venv/bin/python channels/production/mb2/tts.py "line text" path/v1 +14% +3Hz        # voice + word timings
```
Needs ffmpeg. Fonts: Anton and Bangers (OFL; see `assets/LICENSES.txt`).

## Files
- `kit.py`: skia helpers, easing (spring, back-out), outlined text.
- `characters.py`: the `meatball()` rig and the `quadruped()` species rig (`SPECS` holds the grizzly and horse; add a dog or cat here with its silhouette tells).
- `render.py`: the episode spec (`EP`), the shot list (`shots()`, each anchored to a spoken word), rig shots, panel motion, kinetic captions, fact cards and the encoder.
- `audio.py`: assembles the lines, runs the voice chain, makes the lip-flap envelope, synthesizes SFX and the bed, ducks the music, and masters.
- `episodes/grizzly-wms-3/`: the voiced lines and word timings used for the samples.

## Known gaps (prototype)
- Integrated loudness lands at -14.6 LUFS (TP -1.2) because the roar/impact SFX set the peak. Add a -3 dB pre-limiter on the SFX bus to hit -14.0.
- The shot list is hand-written per episode. To port it, map drawn.py macros (`hook/chase/xray/scale/punch`) to the `shots()` vocabulary so specs can drive it.
- The horse rig is basic. Panel art is 720x1280, upscaled 1.5x.
