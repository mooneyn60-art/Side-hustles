# Bears vs Lions (animals, not the teams) — packaging draft

Status: draft only. No repo edit, commit, push, render, or post. Packaged only from the final scripts in `/workspace/drafts/`: `bears-vs-lions-v6-yt.json` (YouTube Short, about 19.9s at 194.5 wpm plus 0.2s of listed pads, 64 spoken words) and `tt-bears-vs-lions.json` (TikTok minute cut, replaced this turn: about 91.8s, 293 spoken words plus 1.40s of listed pads). The minute cut now ends on "Who would win, a bear or a lion?" Fact pack: `/workspace/drafts/facts/bears-vs-lions.md` (BL-F1–BL-F15), opened 2026-11-15. Both scripts say they are **not yet checked by a second model and not rendered.** Scheduling still needs Moondog88's okay. Suggested window if posted: Wednesday 11/25/2026 evening or Thursday 11/26/2026 morning, America/New_York, before the 1:00 pm ET kickoff (research 116).

A lighter 4–5-swear variant lives at `/workspace/drafts/tt-bears-vs-lions-v2.json` (kept until Moondog88 picks, per the default script note). A short TikTok twin of the YouTube cut lives at `/workspace/drafts/tts-bears-vs-lions.json`. This file packages the YouTube Short and the replaced rules-default minute cut only.

Every fact line below cites its fact ID and keeps the pack's condition or hedge. No facts from outside the pack. No bite-force number (not found). No polar-bear numbers. No invented winner. No `#nfl`, logos, helmets, uniforms, team colors as marks, players, league marks, score pick, or betting. The game, if named, is a date only.

## Title (both cuts; lint-clean packaging)

`Bear vs Lion Who Would Win: The Animals 🐻 (Would Meatball Survive?)`

68 UTF-16 units. Searched words in the first 40 characters. Statement form (no `?` in the core). One emoji. The title itself says it is the animals. Series tag last; episode `#N` is not assigned (`posted.csv` has bison as `#5` on Sat 11/21 11:00 ET).

**Script title, not used here:** `Bear vs Lion: Who Would Win? The Animals 🐻🦁 (Would Meatball Survive?)` (71 units). That wording would fail `postkit.py lint`: a `?` in the core title, and two emojis (the standard is one). Packaging keeps the script's meaning and uses the lint-clean line above.

## YouTube Short — description

Bear versus lion, who would win? The animals. The Smithsonian's National Zoo says a male African lion weighs 330 to 550 pounds (BL-F1). At Katmai National Park and Preserve, the U.S. Park Service says most adult male brown bears typically weigh 600 to 900 pounds in mid-summer, and that large adult males can weigh well over 1,000 pounds by October and November (BL-F14). A big coastal brown bear would probably win on size. Nobody has tested it (pack winner rule / BL-R1). Inland and lower-48 grizzly weight ranges overlap a male lion's (BL-F7, BL-F8, BL-F11), and agencies do not agree on a single bear top speed (BL-F8, BL-F11, BL-F12). The spoken Short itself states BL-F1, BL-F14, and the winner rule; overlap and the speed hedge are in this description and in the minute cut, not in the 20-second room. Timed for Thanksgiving, November 26, 2026. This is about the animals.

#bear #lion #grizzly #meatballmyths #shorts

Sources: /workspace/drafts/facts/bears-vs-lions.md (BL-F1, BL-F7, BL-F8, BL-F11, BL-F12, BL-F14); Smithsonian's National Zoo; U.S. National Park Service (Katmai, Yellowstone, Glacier, Staying Safe Around Bears); U.S. Fish and Wildlife Service. General information, not safety training.

The draft script description used "General information, not a predicted fight" and did not cite fact IDs. Packaging keeps the pack's hedges and uses the lint-required survival line. Hashtags are 3 topic + `#meatballmyths` + `#shorts` last.

## YouTube Short — tags (10, each ≤30 characters)

From the script's tags, plus a short form of one over-cap query the cuts actually answer. Dropped the script tag `grizzly bear vs lion who would win` (34 characters). Added `grizzly bear vs lion` and `bear vs lion`. No polar-bear tags (pack: different animal). No football tags.

1. bear vs lion who would win
2. bear versus lion
3. brown bear vs lion
4. grizzly bear vs lion
5. who would win a bear or a lion
6. coastal brown bear weight
7. African lion weight
8. would meatball survive
9. Meatball Myths
10. bear vs lion

## YouTube Short — pinned comment

Who would you pick, and why? Remember: nobody has tested it.

Open question, not yes/no. If this Short is scheduled in the Night Shift week (after Wed 11/25 17:00 ET) it is off-topic to that long-form, so Related video is the Would Meatball Survive? playlist and this pin does not add a Related-video line. See `related-video-rule.md`.

## TikTok minute cut — caption (MASTER_ORDERS / 11/15 template)

Rebuilt from the replaced `tt-bears-vs-lions.json` caption (facts, hedges, Thanksgiving date, five topic hashtags). Lint-clean changes only: a `?` after the opening searched phrase; the exact line "General info, not safety training." in place of the script's "General info, not a predicted fight."; and the caption now ends, as the new spoken cut does, on "Who would win, a bear or a lion?" before the hashtags. Fact IDs are listed under the paste-ready caption, not in the posted text.

```
bear versus lion who would win? The animals. A male African lion, the Smithsonian's National Zoo says, weighs 330 to 550 pounds; a San Diego Zoo Wildlife Alliance fact sheet lists males at 331 to 496. In the lower 48, the U.S. Fish and Wildlife Service says adult male grizzlies average 400 to 600 pounds — those ranges overlap. At Katmai, most adult male brown bears typically weigh 600 to 900 pounds in mid-summer, and large adult males can weigh well over 1,000 by fall. A big coastal brown bear would probably win on size. Nobody has tested it. Bear speed is not one number. Timed for Thanksgiving, November 26, 2026. General info, not safety training. Who would win, a bear or a lion?
#bear #lion #grizzly #brownbear #wildlife
```

Fact IDs in that caption, with conditions kept: BL-F1 (Smithsonian male African lion 330–550 lb); BL-F3 (SDZWA males 331–496 lb); BL-F7 (lower-48 adult male grizzlies average 400–600 lb; ranges overlap a male lion); BL-F14 (Katmai typical mid-summer adult males 600–900 lb; large adult males well over 1,000 by fall); pack winner rule / BL-R1 (a big coastal brown bear would probably win on size; nobody has tested it); bear speed is not one number (BL-F8, BL-F11, BL-F12).

Spoken facts in the replaced minute script also include Yellowstone ecology males 200–700 lb (BL-F8), Glacier adult males 300–440 lb (BL-F11), lion bursts 45–60 km/hr (24–37 mph) for short distances (BL-F5), no documented Yellowstone grizzly over 900 lb (BL-F15), and a separate inland-overlap line (BL-R2). Those stay in the spoken cut. The new last line is: "Nobody has tested it. Who would win, a bear or a lion?" Jokes in the script add no number, danger, feeling, motive, or safety instruction.

## TikTok minute cut — pinned comment

Who would you pick, and why? Remember: nobody has tested it.

## Thumbnail concept (YouTube, 16:9)

Updates `NOT THE TEAMS` in `thumbnail-concepts.md`. White or plain background. One huge drawn face-off (grizzly or coastal brown bear and an African lion), heads filling the frame, no stadium, no logos or team marks, no Meatball, no winner ribbon, no score. Hand-lettered words, one red word, one arrow, readable at 168 px.

- `_a` (Short and default): on-image `NOT THE TEAMS` (3 words), red word `TEAMS`. Arrow underlines `TEAMS` or points from the animals to that word. This is the hook, not a weight claim.
- `_b` (long-form only, if a long "who would win" is built): `ON SIZE ONLY` (3 words), red word `SIZE`. Use only with the pack's "probably win on size" + "nobody has tested it" (coastal brown bear vs male African lion, BL-F14 vs BL-F1). Do not letter a single mph or a generic "grizzly wins."
- `_c` (long-form only): `RANGES OVERLAP` (2 words), red word `OVERLAP`. For the inland / lower-48 overlap (BL-F7, BL-F8, BL-F11). If two animals muddy the 168 px test, keep one huge subject and the words.

Studio A/B is long-form only. If this stays a Short, shoot `_a` only.

## Cover concept — TikTok only

MASTER_ORDERS drops custom cover frames on YouTube Shorts. Do not upload a custom Shorts cover. Related video is a Studio field, not a frame.

For the TikTok minute cut only, a 9:16 cover: white or plain field; the same huge animal face-off, no marks, no Meatball; hand-lettered `NOT THE TEAMS` with `TEAMS` in red; one arrow; still readable when the cover is small on a For You feed. Do not put weight numbers or a "winner" badge on the cover.

## Related video

Would Meatball Survive? playlist, unless a same-creature WMS long-form is later scheduled as that week's lead (Claude is confirming Saturday long-form order with Nolan). See `related-video-rule.md`.
