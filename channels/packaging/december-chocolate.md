# December chocolate — packaging draft (YouTube Short)

Status: draft only. No repo edit, commit, push, render, or post. Packaged only from the final script `/workspace/drafts/chocolate-v6-yt.json` (YouTube Short, about 19.9s at 194.5 wpm plus 0.2s of listed pads, 64 spoken words; packaging slot Tue 12/01/2026 16:00 ET, America/New_York) and the fact pack `/workspace/drafts/facts/chocolate.md` (CH-F1–CH-F15), opened 2026-11-15. The script says it is **not yet checked by a second model and not rendered.** Scheduling still needs Moondog88's okay. A short TikTok twin lives at `/workspace/drafts/tts-chocolate.json`; this file packages the YouTube Short only.

Every fact line below cites its fact ID and keeps the pack's condition or hedge. No facts from outside the pack. Do not invent a dose, convert Merck mg/kg figures into mg/lb and present the result as Merck's number, say any amount is safe, give one dose for all dogs, or say a bite always kills. Size, type of chocolate, and individual sensitivity all matter (CH-F2). Do not say white chocolate is safe (CH-F7: sugar and fat may still lead to pancreatitis). Do not say chocolate is harmless to cats (CH-F8).

The FDA call-your-vet line stays in the YouTube description, with its condition (CH-F6).

## Title (lint-clean, from the script)

`Can Dogs Eat Chocolate: Mild Signs Can Start at 9 mg Per Pound 🍫 (Things Living In Your House)`

95 UTF-16 units. Statement form. Searched words (`Can Dogs Eat Chocolate`) sit in the first 40. The hedge is `Can` / `Can Start`. The sourced fact is CH-F4 (FDA: theobromine can cause mild signs at doses as low as 9 mg per pound of body weight). One emoji. Series tag last; no episode number is assigned. This matches the open-slot title already drafted for Tue 12/01 16:00 ET in `open-dates-1121-1204.md`.

This is the script title. It already passes the title rules, so packaging does not rewrite it.

## YouTube Short — description

Can dogs eat chocolate? The FDA says chocolate is toxic to dogs, and that theobromine is the main culprit (CH-F1). Theobromine can cause mild signs in dogs with doses as low as 9 mg per pound of body weight, and severe signs starting around 18 mg per pound (CH-F4). That dose is per pound of the dog's body weight, so the same amount can be milder for a large dog and severe for a small one (CH-F2, CH-F4). The same FDA table lists about 57 mg of theobromine in an ounce of milk chocolate, and about 227 mg in dark chocolate with 70-85% cacao (CH-F3; those figures are approximate, per ounce of that chocolate type). Do not say any amount is safe, and do not say a bite always kills. The ASPCA says cats are also sensitive to theobromine, though they tend not to eat as much chocolate (CH-F8; "tend," "less likely," not "never"). If your pet is sick or has a veterinary emergency, call your veterinarian. If your veterinarian is unavailable, call your local emergency animal hospital or an animal poison control center (CH-F6).

#dogchocolate #candogseatchocolate #theobromine #meatballmyths #shorts

Sources: /workspace/drafts/facts/chocolate.md (CH-F1, CH-F2, CH-F3, CH-F4, CH-F6, CH-F8); FDA, Leave Chocolate Out of Rover's Celebrations, https://www.fda.gov/animal-veterinary/animal-health-literacy/leave-chocolate-out-rovers-celebrations ; ASPCA, What to Do If Your Pet Gets into Chocolate, https://www.aspca.org/news/what-do-if-your-pet-gets-chocolate . Pages opened 2026-11-15. General information, not veterinary advice.

Hashtags are 3 topic + `#meatballmyths` + `#shorts` last, matching the script. The draft script description did not cite fact IDs; packaging adds the IDs and keeps every condition, including the CH-F6 call-your-vet line. The spoken Short itself states CH-F1, CH-F4, and CH-F3 (with CH-F6 on the last card and in this description; the script note says the call-for-help line is spoken on the tts twin). Merck mg/kg figures (CH-F11) are not used here.

## YouTube Short — tags (8, each ≤30 characters, from `postkit.py kw`)

These are the script tags, from `/workspace/packaging/kw/kw-studio-assignments.csv` and `/workspace/packaging/kw/kw-open-dates-1121-1204.csv` (run 2026-11-15, America/New_York). Cake, chips, ice cream, cookies, donuts, brownies, chocolate milk, "a little chocolate," puppies, and white chocolate were dropped because the spoken cut does not name those foods, and "a little" would sound like a safe amount.

1. can dogs eat chocolate
2. can dogs eat dark chocolate
3. could dogs eat chocolate
4. why can't dogs eat chocolates
5. theobromine in chocolate
6. chocolate toxicity in dogs
7. things living in your house
8. Meatball Myths

Tag 2 stays because the cut states the FDA dark-vs-milk table (CH-F3, 70–85% cacao).

## YouTube Short — pinned comment

What would you do if your dog got to the tin?

Open question, not yes/no. No Related-video line: this Short, if it keeps the Tue 12/01/2026 16:00 ET slot, is a pet house video in the Night Shift week, so it is off-topic to that long-form.

## Thumbnail concept (YouTube, 16:9) — no custom Shorts cover

MASTER_ORDERS drops custom cover frames on YouTube Shorts. Do not upload a custom Shorts cover. Related video is a Studio field, not a frame. The card below is the 16:9 thumbnail only. Updates `NOT A TREAT` in `thumbnail-concepts.md`.

White or plain background. The card is a warning, not a "safe amount" claim. No Meatball. One red word, one arrow, readable at 168 px.

- `_a` (Short and default): on-image `NOT A TREAT` (3 words), red word `NOT`. One huge drawn chocolate bar or tin; arrow to the chocolate. Supported by CH-F1 (chocolate is toxic to dogs). Do not letter a mg/lb dose, a dark-vs-milk number, or "one square is enough" on this small card. Those figures stay in the description (CH-F3, CH-F4).
- `_b` (long-form only): `LEAVE THE TIN` (3 words), red word `LEAVE`. Still no dose.
- `_c` (long-form only): `NOT FOR DOGS` (3 words), red word `NOT`. Do not letter "safe for cats" (CH-F8: cats are also sensitive). Still no dose.

Studio A/B is long-form only. This piece is a Short, so shoot `_a` only and do not set a cover frame.

## Related video

Things Living In Your House playlist (locked in `related-video-rule.md` for the Tue 12/01/2026 16:00 ET dog-chocolate slot). It is off-topic to Night Shift v2, which remains the week's long-form until Sat 12/5 08:00. Claude is confirming later Saturday long-form order with Nolan.

## Lint (`postkit.py lint`, 2026-11-15, America/New_York)

YouTube stub: `/workspace/packaging/lint-specs/yt-december-chocolate.json`. **Pass (0 fail, 1 warn).** Title 95 of 100 units, 8 tags. The warning is "description has 5 hashtags (the standard is four…)." The draft follows written MASTER_ORDERS line 101: three topic tags, then `#meatballmyths`, then `#shorts` last. The CH-F6 call-your-vet line is in the description, with its condition.
