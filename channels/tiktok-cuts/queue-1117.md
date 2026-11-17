# Proposed TikTok queue, @meatballmyths, Tue 11/17 – Mon 11/30 (all times ET)
**PROPOSAL ONLY.** Nothing is scheduled, posted or changed in Metricool, TikTok or the repo.
Rules: slots at 10:00 / 14:00 / 19:00 only, 2–3 a day, ≥3 h apart (the tightest gap is 4 h). The existing items come from /workspace/fixes/queue-audit-1116.md (repo posted.csv), moved only into allowed slots. Originality evidence is in originality/originality-1116.md. The live list (112 videos, fetched 9:40 PM ET) is in originality/live-tiktok-et.txt.
**Date note:** the brief said "Sat 11/22" and "Sun 11/23", but 11/22/2026 is a **Sunday** and 11/23 a **Monday**. I followed the dates. If Saturday/Sunday was meant, shift EP5 to Sat 11/21 19:00 (T1) and Sun 11/22 14:00 + 19:00 (T2, T3). The Part 1 → Part 2 gap stays 19 h either way.

Flag key: **NO-ORIG** repeats a live video · **TOPIC** topic already live (content not compared) · **<61** / **>75** length vs the TikTok spec · **OLD** old look (stick-figure or 3D, not the cartoon kit) · **OLD?** look unverified (old pipeline folder) · **RENDER** waiting on a render · **?LEN** length unknown (no media)

| Day | 10:00 | 14:00 | 19:00 |
|---|---|---|---|
| Tue 11/17 | tt-cassowary · OLD? ?LEN · TOPIC (posted.csv: TikTok 10/25 "I Tried to Befriend a Cassowary"; not in the visible live list) | tt-hummingbird · OLD? ?LEN | tt-shark-wms · OLD · **>75 (86.9 s)** · the 11/15 repo commit says "shark short TikTok pulled", but it's still in posted.csv, so confirm |
| Wed 11/18 | tt-sea-otter · OLD? ?LEN | yt-bedbugs-explainer (YT-named file) · OLD? (sim3d) ?LEN · TOPIC (bed bugs live 10/30, 11/09) | tt-christmas-tree-check · OLD? ?LEN |
| Thu 11/19 | tts-dog-stare · OLD · **<61 (25.2 s)** · TOPIC (dog-stare YT Short 11/13) | tt-honey-badger · OLD? ?LEN · TOPIC (honey badger live 10/25) | **~~tts-grizzly-wms~~ PULL: NO-ORIG** (72% same audio as live 11/13 20:15; swear at ~1 s; <61). Slot → **vacuum-spider TikTok, when render lands** (placeholder, below) |
| Fri 11/20 | tt-drain-fly · OLD? ?LEN · TOPIC (drain flies in the live 11/02 list video) | tt-woodpecker · OLD? ?LEN | yt-silverfish-hook · OLD (3D) · **<61 (18.7 s)** · TOPIC (3rd silverfish: live 10/28 + 11/16) · same file on YT 11/21. Footage/audio original (0% overlap), but **recommend pulling on spec**; leave the slot empty (no original replacement on the box) |
| Sat 11/21 | tts-dog-turkey · OLD · **<61 (25.1 s)** | open | tt-waterbug · OLD? ?LEN · TOPIC (water bug in the live 11/05 list video) |
| Sun 11/22 | tt-polar-bear (moved from 19:00) · OLD? ?LEN · wording check owed ("transparent fur") | open | **EP5 T1 "Why is there a spider in my bathtub?" Part 1/3** · 67.87 s · **RENDER** (Claude) · plan locked |
| Mon 11/23 | tt-platypus (moved from 19:00) · OLD? ?LEN | **EP5 T2 "Is it a hobo spider?" Part 2/3** · 66.94 s · **RENDER** | **EP5 T3 "How do I get a tub spider out?" Part 3/3** · 62.31 s · **RENDER** |
| Tue 11/24 | open | open | tt-wombat · OLD? ?LEN |
| Wed 11/25 | open | open | tt-greenland-shark · OLD? ?LEN |
| Thu 11/26 | open | open | open |
| Fri 11/27 | open | open | open |
| Sat 11/28 | open | open | open |
| Sun 11/29 | open | open | open |
| Mon 11/30 | open | open | open |

## Removed or moved
- **tt-electric-eel** (the audit moved it to 11/22 10:00): **dropped, already live**, 11/16 21:30 ET (65 s, id 7708962194335042847).
- **tts-grizzly-wms** 11/19 19:00: pull (NO-ORIG). Its slot goes to the vacuum-spider placeholder.
- tt-polar-bear 19:00 → 10:00 (11/22) and tt-platypus 19:00 → 10:00 (11/23), to make room for EP5.
- tt-drain-fly is at 11/20 10:00 (it was 11/18 21:30, an off-pattern slot).

## Placeholders and series rules
- **Vacuum-spider TikTok** ("What happens if you vacuum a spider? Inside your vacuum", 220 words / 67.87 s, /workspace/scripts/hero-vacuum-spider.md Part 2). Status: script PROPOSAL pending Moondog88's review; **no render on the box**. It's placed at the earliest open slot, Thu 11/19 19:00 (freed by the grizzly pull); the fallback is Sat 11/21 14:00. **Flag:** it ends on "What happens to a spider egg sac in the vacuum? Part 2." By the Part rule, that's only allowed if Part 2 is cut and queued, and it isn't. So it needs a loop-ending variant, or a queued Part 2.
- **EP5 Part 1/2/3:** TikTok-only Part cards (Studio ruling). Post only if all 3 renders land and pass build_tt. If any one slips, swap T1/T2 to loop endings (part2.md). T2 goes out ≤24 h after T1 and is queued before T1 posts.

## Flag summary
- **Non-original:** tts-grizzly-wms (pull). Also the already-live 11/16 silverfish sample is a 100% repeat of live 10/28, and the other 11/16 Lid8 samples likely repeat 10/2x Parts. Those are live, and I didn't touch them.
- **Under 61 s:** tts-dog-stare 25.2, tts-dog-turkey 25.1, yt-silverfish-hook 18.7 (tts-grizzly ~25 est.).
- **Over 75 s:** tt-shark-wms 86.9.
- **Old look:** every carried repo item (seen: shark, dog-stare, dog-turkey, silverfish-hook; the rest are unverified but come from old pipelines). 1K-JAIL #5 says re-skin or hold.
- **Waiting on renders:** EP5 T1–T3 (Claude), vacuum-spider TikTok.
- **Unknown length:** 13 drawn-tt/drawn-house items with no media on the box.
