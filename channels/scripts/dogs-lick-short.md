# Why do dogs lick you? (YouTube Short + TikTok twin)

Draft: Sunday, Nov 15, 2026 (America/New_York).  
Status: **not pushed**. Fact pack: `/workspace/drafts/facts/dogs-lick.md`.  
Specs: `/workspace/drafts/dogs-lick-v6-yt.json` (YouTube Short), `/workspace/drafts/tts-dogs-lick.json` (TikTok short twin).  
The TikTok minute cut remains `/workspace/drafts/tt-dogs-lick.json` and `/workspace/drafts/dogs-lick.md`. This file is the Short pair only.

Templates: YouTube + tts follow the newest drawn-house pair (chocolate / cats-turkey: mystery music on YouTube, detective on the tts twin). Written only from the fact pack. Pages in that pack were opened live on 2026-11-15. This script pass did not re-fetch those pages. Still needs a second-model check and a render/transcript pass before it can be scheduled.

Title uses the packaging statement form, 81 UTF-16 units: `Why Dogs Lick You: Penn Vet Says It's Not a Kiss 🐶 (Things Living In Your House)`. No banned YouTube title words (TRUE or FALSE, Myth, Believe, Cartoons, Lied, "Did you know"). No episode number. Series: Things Living In Your House.

Hashtags follow MASTER_ORDERS: YouTube description uses `#whydodogslickyou #doglicking #dogbehavior #meatballmyths #shorts` (three topic tags, then brand, `#shorts` last). TikTok caption uses `#whydodogslickyou #doglicking #dogbehavior #dogsoftiktok #dogfacts` (five topic tags, no brand, no `#fyp`). Hashtag feeds were not re-run on this pass.

Lip licking is kept separate from licking a person. The hedge "may" is kept. No hedge-mocking tag. His dog, Noodle (comma form) is planted in the line 2 gag and ends up with the sandwich. Jokes add no feeling or motive.

This is general information, not a diagnosis of your dog.

---

## A. YouTube Short (mild words)

**Estimated runtime: 19.0 seconds** (lint window 15.0–20.05s; 16–20s target). 4 lines, 61 spoken words, plus 0.2s of listed pads. Pacing is calibrated to the posted moose minute cut (289 words in 89.13s ≈ 194.5 wpm on Andrew at +10%). One mild word: “damn,” in the line 2 gag.

Hook and last line share the kitchen so the final “And” loops into the first line. Frame 0 is the dog already in view (`open: animal`). Line 2, the acted gag, starts at 4.0s (inside the 3–7s window). Studio should show Meatball puckering up and Noodle ending up with the sandwich; there is no Noodle character key in the schema.

| # | Time | Scene | Spoken line | Fact IDs |
|---|---|---|---|---|
| 1 | 0.0–4.0s | open / kitchen | Why do dogs lick you? Penn Vet says it is not a kiss. | DL-F1 (hook + Penn Vet: not a “kiss”) |
| 2 | 4.0–7.3s | kitchen | Meatball puckered up. His dog, Noodle, got the damn sandwich. | (no fact; acted gag; Noodle plant and sandwich payoff, comma form) |
| 3 | 7.3–15.9s | study | Licking a person or another dog is a greeting behavior, the same handout says, but if a dog licks someone repeatedly, he may be anxious about that person. | DL-F1 (greeting behavior; if a dog licks someone repeatedly, he may be anxious about that person) |
| 4 | 15.9–19.0s | kitchen | Lip licking is a different signal, Penn Vet says. And | DL-F2 (lip licking is a different signal) |

**Mild word (1):** damn (line 2).  
**Sourced facts:** DL-F1 (Penn Vet: not a kiss; greeting; repeated licking may be anxiety), DL-F2 (lip licking is a different signal).

### Alternate first-3-second hooks (Short)

Hook 1 is in the JSON.

1. **Draft hook (in the JSON):** “Why do dogs lick you? Penn Vet says it is not a kiss.” (~4.0s). Leaves room for the gag inside the 3–7s window.
2. **Repeated-licking hedge in the hook:** “Why do dogs lick you? If a dog licks someone repeatedly, Penn Vet says, he may be anxious.” (~5.6s). Front-loads the “may” but delays “not a kiss” and pushes the gag later in the window.
3. **Lip-lick warning in the hook:** “Why do dogs lick you? Lip licking is a different signal, Penn Vet says.” (~4.0s). Useful as a correction, but it answers a different behavior than the searched “lick you” question.

---

## A2. TikTok short twin (`tts-dogs-lick.json`)

Same facts, same four-beat shape, sweary reactions. **Estimated runtime: 22.1 seconds** (the bison / chocolate tts twins also run longer than their 16–20s YouTube cuts). 71 spoken words, plus 0.2s of pads. `search_top` shows **WHY DO DOGS / LICK YOU?** for 2.5s. Captions use `cap_swap`.

| # | Time | Scene | Spoken line | Fact IDs |
|---|---|---|---|---|
| 1 | 0.0–4.6s | open / kitchen | Why do dogs lick you? Penn Vet says it is not a kiss. Holy shit. | DL-F1 (hook + Penn Vet: not a “kiss”) |
| 2 | 4.6–7.9s | kitchen | Meatball puckered up. His dog, Noodle, got the fucking sandwich. | (no fact; acted gag; Noodle plant and sandwich payoff) |
| 3 | 7.9–18.4s | study | Licking a person or another dog is a greeting behavior, the same handout says, but if a dog licks someone repeatedly, he may be anxious about that person. Meatball wiped his cheek. Fucking typography. | DL-F1 (greeting; repeated licking may be anxiety). Meatball action after the hedge, not a hedge-mock. |
| 4 | 18.4–22.1s | kitchen | Lip licking is a different signal, Penn Vet says. Fucking footnote. And | DL-F2 (lip licking is a different signal) |

Swears: Holy shit (hook); fucking sandwich (gag); Fucking typography (after the “may” line, with a cheek wipe); Fucking footnote (after the lip-lick fact). Facts, credits and the “may” hedge stay clean. No hedge-mocking tag.

### Fact-check (spoken lines vs the 2026-11-15 pack)

Pages were not re-fetched on this script pass. Each factual line is checked against quotes already in `/workspace/drafts/facts/dogs-lick.md`.

| Line | Spoken claim | Pack support | Pass? |
|---|---|---|---|
| 1 | Penn Vet says it is not a kiss. | DL-F1: “Dog licks person or other dog: not a “kiss”.” | Yes |
| 3 | Licking a person or another dog is a greeting behavior; if a dog licks someone repeatedly, he may be anxious about that person. | DL-F1, same sentence. “May” is kept. “That person” is the pack’s “that dog or person,” shortened at the end of a long line. | Yes, with a minor shortening of “that dog or person” |
| 4 | Lip licking is a different signal, Penn Vet says. | DL-F2: “Dog licks his lips: anxiety about a situation or interaction.” The spoken Short names it as a different signal and leaves the anxiety reading in the description, to stay inside 20s. | Yes, as a shortened different-signal claim; the lip-lick anxiety wording is in the description |

No salt, “they like the taste,” or “it’s always love” line. No hedge-mock.

Pinned comment: “What does your dog lick first, your face or your food?”
