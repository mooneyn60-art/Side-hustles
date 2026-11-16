# Audio and engagement audit: Meatball Myths YouTube + TikTok (Nov 15, 2026)

**By:** Jarvis, Sun Nov 15, 2026, 7:10-7:45 PM ET. Read-only on both channels: nothing posted, uploaded, deleted or changed in Studio/TikTok.
**Channels (verified with yt-dlp, 11/15 ~7:12 PM ET):**
- YouTube **@MeatballMyths**, "Meatball Myths", channel id `UCw98RQD81t_339LX5EJqcrg`, 1,010 subscribers, 89 Shorts + 13 long-forms public. This *is* the Meatball channel ("Oh Meatball" is the project name; "Would Meatball Survive?" is a series on it). `@ohmeatball` and `@wouldmeatballsurvive` don't exist (Social growth audit, 11/15). ⚠️ The new Metricool "FurEver Faces" brand links this same channel id; it should stay with Meatball, which is Moondog88's call.
- TikTok **@meatballmyths**, 100 posts listed.
- TikTok **@fureverfaces** is the shop account (1 post, "Zoomies Grand Prix", 153 plays). It isn't the Meatball account and wasn't audited here.

**Method:** public listings (yt-dlp; TikTok with `--impersonate chrome`) → ranked by views → downloaded 10 YT Shorts, 6 long-forms and 10 TikToks (top vs bottom, posts at least about 1.5 days old for the bottom group) → ffmpeg `loudnorm` (integrated LUFS, true peak, LRA), ffmpeg scene detection (threshold 0.30) for cuts, demucs `htdemucs` voice/music separation on the first 20 s for voice-vs-music level and ducking, pYIN pitch on the separated voice, faster-whisper for openings and speech rate. Raw numbers: [data/audio-audit-1115.csv](data/audio-audit-1115.csv); scripts: [data/audio-audit-analyze.py](data/audio-audit-analyze.py), [data/audio-audit-stems.py](data/audio-audit-stems.py).

## Sample

| Group | Video | Views (11/15) |
|---|---|---|
| YT Short top | Are Daddy Longlegs the Most Venomous Spiders? (Us0zIbxiR-A) | 2,457 |
| | The House Centipede You Squish Is Protecting You (EPimwC5VMgo) | 2,289 |
| | Your Roach Has 40 Babies (1hdMaSxJtkU) | 1,988 |
| | Your Bed Mites Die at 130°F (wHCrmIPdCgg) | 1,953 |
| | 3 'Mommy Longlegs' in Your Home (bm6LzV7eRwg) | 1,908 |
| YT Short bottom | Your Dog's Guilty Look… (xIbnhX10r7k) | 3 |
| | The US Planned to Nuke the Moon (88gaODWt4qY) | 10 |
| | A Brown Recluse Hides in Your Shoes (YrPzxjXZJCY) | 48 |
| | 8 Weeks of Mites in Your Skin (66YDY0wDiaU) | 65 |
| | A Camel Cricket in Your Basement (vn-MTvvQsbg) | 124 |
| YT long top | 3 Bugs in Your House You Should Never Kill (cH3HCZ8GlHk) | 213 |
| | How Wolves Became Dogs (Uqj0QL8G0d4) | 163 |
| | Weird Animal Facts You Didn't Know (z-Kg8sXCxlU) | 134 |
| YT long bottom | 12 Animal Myths… (RwbgzQisvYM) | 6 |
| | Every Bug in Your House, Ranked (bqij8Ht6SX4) | 5 |
| | 6 Creatures Living In Your House Right Now (Lid8JXhg1Q4) | 3 |
| TikTok top | why did the faa ground stop happen (7707843829264665887) | 17,600 |
| | bombardier beetle "Would you pick one up?" (7700968777902492958) | 6,033 |
| | house centipede part 2 (7703357929851800862) | 5,376 |
| | house centipede facts (7701402177754942751) | 4,040 |
| | house centipede in bathroom (7705514437402316062) | 1,637 |
| TikTok bottom | lizard on my ceiling (7707703103268687135) | 24 |
| | CIA fake mining ship (7701076793129717023) | 86 |
| | what to do if you see a grizzly (7707829612465769758) | 90 |
| | why do cats purr (7707849105136946445) | 100 |
| | possum fakes its death (7702121787953368350) | 123 |

Context (public, 11/15): YT Shorts median 997 views; long-form median 43. TikTok newest 100 median 242 plays; 88 of 100 have 0 comments; median likes are 2.0% of plays. On YouTube, 94 of 102 videos have 0-1 comments; median likes are 1.0% of views.

## Medians, top vs bottom

| Group | LUFS | True peak | Cuts/min | Avg shot | Voice − music (LU) | Music under voice | Music in pauses | Ducking | Voice f0 IQR |
|---|---|---|---|---|---|---|---|---|---|
| YT Short top | -15.4 | -4.3 | **19.6** | **2.5 s** | 11.2 | -11.5 dB | -10.0 dB | 1.5 dB | 6.9 st |
| YT Short bottom | -15.6 | -4.4 | 12.4 | 4.0 s | 15.3 | -17.5 | -9.7 | 1.8 | 6.4 |
| YT long top | -14.2 | -1.2 | 6.4 | 9.2 s | 15.7 | -26.8 | -15.9 | 11.5 | 6.6 |
| YT long bottom | -15.0 | -3.0 | 5.2 | 11.2 s | 15.0 | -33.7 | n/a | n/a | 6.8 |
| TikTok top | -12.4 | -1.1 | **14.2** | **4.0 s** | 13.0 | -12.5 | -16.1 | 0.8 | 6.7 |
| TikTok bottom | -12.6 | -1.0 | 8.5 | 6.6 s | 14.2 | -26.5 | -9.6 | 2.0 | 6.9 |

YT Shorts speech rate (faster-whisper base, transcripts checked against the on-screen captions): **top median 205 wpm** (217, 232, 161, 196, 205) vs **bottom 171** (165, 171, 172, 203, 166).

## Findings

1. **Topic and hook beat everything audio.** Winners are house bugs, spiders and (TikTok) breaking news. Losers are pets, big animals, history and conspiracy. Every winning opening is second-person + home + number or stakes ("One bug in your house can put you in the hospital", "your roach is carrying 40 babies", "Something with 30 legs hunts in your house tonight"). The losers open in the third person ("A Chicago physicist…", "When it's scared, this animal…", "What if I told you the CIA…"). All 26 start talking at 0.0 s, so speed of start isn't the problem; the wording is.
2. **Winners talk faster:** 205 vs 171 wpm on YT Shorts (4 of 5 winners at 196 or more; 4 of 5 losers at 172 or less).
3. **Winners cut faster:** 19.6 vs 12.4 cuts a minute on YT Shorts, and 14.2 vs 8.5 on TikTok. The best long-form cuts 13.2 a minute (4.5 s shots) vs 5.0-6.4 (9-12 s) on every other long-form. Exception: the #1 and #2 Shorts are slow-cut (9.0 and 7.8 a minute), so this is a lean, not a rule.
4. **The current renderer doesn't duck music.** On the drawn v6 videos the music sits 10-12 dB under the voice while he talks and rises only 0-3 dB in pauses. The October sidechained videos ducked 11-17 dB. In code, `drawn.py mix_audio()` ducks the SFX bus but applies one fixed gain to the music. The voice-to-music gap ranges from **1.1 LU** (6 Creatures, 3 views) to **34 LU** (no music), so there's no house mix. This doesn't separate winners from losers, but it's why the mix sounds flat and why the music can't build at reveals.
5. **Every video uses the same two beds.** `mystery` (96 bpm) or `detective` (112 bpm) are on every spec in `channels/scripts/`, and on 111 of 113 in `scripts/drawn-tt/`. There's no per-series sound identity and no change at reveals (reveal hits only fire on counter videos).
6. **YT Shorts are about 1.5 dB too quiet:** median -15.4 LUFS, as low as -16.0, with true peak around -4.4 dBTP. YouTube doesn't raise quiet uploads. The cause is single-pass `loudnorm` in `drawn.encode_cmd` on short clips; long-form builders already use two-pass and land at -14.1 to -14.9. One TikTok (CIA mining ship) peaks at **+0.26 dBTP**, which clips.
7. **Voice flatness isn't the separator.** Same Andrew voice everywhere; pitch IQR 6.9 vs 6.4 semitones (YT) and 6.7 vs 6.9 (TikTok), top vs bottom. What's missing is contrast *between* lines: every line has the same rate and pitch, with no hook push and no pre-reveal beat.
8. **Visual (observed, not measured):** in three bottom performers the drawn bear, dog and lizard share one generic four-legged body. Pets and big animals are the weakest topics on both platforms.

## What couldn't be checked

- **Retention curves and average view duration** per video: not public (Studio/TikTok Analytics). The 11/12 Studio export in `oh-meatball/research/data/100-shorts-table.csv` shows drawn v6 Shorts at 83% average viewed vs 61% for older styles.
- **TikTok and long-form speech rate:** two speech models (base and small) dropped whole stretches on these files, even on the separated voice track, so those wpm numbers aren't reported. YT Shorts transcripts matched the captions and are used.
- **SFX count per video:** not separated; the SFX rules come from code (`cut_whoosh` on every line change).
- **Whether TikTok re-processed loudness:** the TikTok numbers are for the files TikTok serves.
- **Music genre "energy"** beyond tempo: tempo comes from beat tracking on the separated music, ±10%.
- **Captions:** presence was checked on contact sheets (all have word captions); size and readability weren't scored.
- Sample is 26 videos; differences are directional, not statistically tested.
