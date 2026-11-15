# Why do cats knead? (YouTube Short + TikTok twin)

Draft: Sunday, Nov 15, 2026 (America/New_York).  
Status: **not pushed**. Fact pack: `/workspace/drafts/facts/cats-knead.md`.  
Specs: `/workspace/drafts/cats-knead-v6-yt.json` (YouTube Short), `/workspace/drafts/tts-cats-knead.json` (TikTok short twin).  
The TikTok minute cut remains `/workspace/drafts/tt-cats-knead.json` and `/workspace/drafts/cats-knead.md`. This file is the Short pair only.

Templates: YouTube + tts follow the newest drawn-house pair (chocolate / cats-turkey: mystery music on YouTube, detective on the tts twin). Written only from the fact pack. Pages in that pack were opened live on 2026-11-15. This script pass did not re-fetch those pages. Still needs a second-model check and a render/transcript pass before it can be scheduled.

Title uses the packaging statement form, 84 UTF-16 units: `Why Cats Knead: It May Start When They Were Kittens 🐱 (Things Living In Your House)`. No banned YouTube title words (TRUE or FALSE, Myth, Believe, Cartoons, Lied, "Did you know"). No episode number. Series: Things Living In Your House.

Hashtags follow MASTER_ORDERS: YouTube description uses `#whydocatsknead #catkneading #catbehavior #meatballmyths #shorts` (three topic tags, then brand, `#shorts` last). TikTok caption uses `#whydocatsknead #catkneading #catbehavior #catsoftiktok #makingbiscuits` (five topic tags, no brand, no `#fyp`). Hashtag feeds were not re-run on this pass.

Hedges stay (“most likely,” “traces it to”). No hedge-mocking tag. Grigg's “You are someone who is important to me” is not voiced as the cat’s monologue. No invented paw-scent marking. His cat, Sauce (comma form) does the opposite and walks off; Meatball kneads the pillow. Jokes add no feeling or motive.

This is general information, not a diagnosis of your cat.

---

## A. YouTube Short (mild words)

**Estimated runtime: 19.9 seconds** (lint window 15.0–20.05s; 16–20s target). 4 lines, 64 spoken words, plus 0.2s of listed pads. Pacing is calibrated to the posted moose minute cut (289 words in 89.13s ≈ 194.5 wpm on Andrew at +10%). One mild word: “damn,” in the line 2 gag.

Hook and last line share the kitchen so the final “And” loops into the first line. Frame 0 is the cat already in view (`open: animal`). Line 2, the acted gag, starts at 3.4s (inside the 3–7s window). Studio should show Sauce walking off and Meatball kneading the pillow; there is no Sauce character key in the schema. Beat 2 includes a Sauce walk-off `hero_moves` cue.

| # | Time | Scene | Spoken line | Fact IDs |
|---|---|---|---|---|
| 1 | 0.0–3.4s | open / kitchen | Why do cats knead? International Cat Care traces it to kittens. | CK-F1 (hook + International Cat Care traces kneading to kittens) |
| 2 | 3.4–8.2s | kitchen | Meatball offered his cat, Sauce, a pillow. Sauce walked off. Meatball kneaded the damn pillow. | (no fact; acted gag; Sauce plant, walk-off, Meatball kneads the pillow) |
| 3 | 8.2–14.4s | study | Kittens tread with alternate front paws on the mother's abdomen to stimulate the flow of milk, International Cat Care says. | CK-F1 (kittens tread with alternate front paws on the mother's abdomen to stimulate the flow of milk) |
| 4 | 14.4–19.9s | kitchen | Emma Grigg at UC Davis says it is most likely carried over from their days as kittens. And | CK-F6 (Emma Grigg, UC Davis: most likely carried over from their days as kittens) |

**Mild word (1):** damn (line 2).  
**Sourced facts:** CK-F1 (International Cat Care: kittens / treading for milk), CK-F6 (Grigg, UC Davis: most likely a carry-over from kittenhood).

### Alternate first-3-second hooks (Short)

Hook 1 is in the JSON.

1. **Draft hook (in the JSON):** “Why do cats knead? International Cat Care traces it to kittens.” (~3.4s). Leaves room for the gag inside the 3–7s window.
2. **Grigg hedge in the hook:** “Why do cats knead? A UC Davis behaviorist says it is most likely carried over from their days as kittens.” (~5.6s). Stronger “most likely” in the first line, but it delays International Cat Care and pushes the gag later in the window.
3. **Lap line in the hook:** “Why do cats knead? If they knead on your lap, International Cat Care says this shows they associate you with their mother.” (~6.8s). Uses the “this shows” wording early, but it is long enough to crowd the gag and shortens the source sentence.

---

## A2. TikTok short twin (`tts-cats-knead.json`)

Same facts, same four-beat shape, sweary reactions. **Estimated runtime: 23.0 seconds** (the bison / chocolate tts twins also run longer than their 16–20s YouTube cuts). 74 spoken words, plus 0.2s of pads. `search_top` shows **WHY DO CATS / KNEAD?** for 2.5s. Captions use `cap_swap`.

| # | Time | Scene | Spoken line | Fact IDs |
|---|---|---|---|---|
| 1 | 0.0–4.0s | open / kitchen | Why do cats knead? International Cat Care traces it to kittens. Holy shit. | CK-F1 (hook + International Cat Care traces it to kittens) |
| 2 | 4.0–8.8s | kitchen | Meatball offered his cat, Sauce, a pillow. Sauce walked off. Meatball kneaded the fucking pillow. | (no fact; acted gag; Sauce walk-off) |
| 3 | 8.8–15.9s | study | Kittens tread with alternate front paws on the mother's abdomen to stimulate the flow of milk, International Cat Care says. Tiny fucking bakers. | CK-F1 (treading for milk). “Tiny fucking bakers” is a biscuit gag, not a number. |
| 4 | 15.9–23.0s | kitchen | Emma Grigg at UC Davis says it is most likely carried over from their days as kittens. Meatball kept kneading. Fucking committed. And | CK-F6 (most likely a carry-over). “Most likely” stays in the fact; the reaction is a Meatball action, not a hedge-mock. |

Swears: Holy shit (hook); fucking pillow (gag); Tiny fucking bakers (after the iCatCare line); Fucking committed (after “Meatball kept kneading”). Facts, credits and the “most likely” hedge stay clean. No hedge-mocking tag.

### Fact-check (spoken lines vs the 2026-11-15 pack)

Pages were not re-fetched on this script pass. Each factual line is checked against quotes already in `/workspace/drafts/facts/cats-knead.md`.

| Line | Spoken claim | Pack support | Pass? |
|---|---|---|---|
| 1 | International Cat Care traces it to kittens. | CK-F1, iCatCare, updated 26 September 2025. Short setup for the treading line. | Yes |
| 3 | Kittens tread with alternate front paws on the mother's abdomen to stimulate the flow of milk, International Cat Care says. | CK-F1: “Kittens suckle their mothers by treading with alternate front paws on her abdomen to stimulate the flow of milk.” Spoken line keeps treading, alternate front paws, abdomen, and milk; it drops “suckle their mothers” to stay inside 20s. | Yes, with “suckle their mothers” left in the pack / description |
| 4 | Emma Grigg at UC Davis says it is most likely carried over from their days as kittens. | CK-F6. “Most likely” is kept. Her full title (“an animal behaviorist at UC Davis”) is in the description. | Yes |

No paw-scent-marking claim. Grigg's bond illustration is not spoken as the cat's thoughts (it is in the description only). The “never punished” line is in the description, not the 20s cut.

Pinned comment: “Does your cat knead you, a blanket, or both?”
