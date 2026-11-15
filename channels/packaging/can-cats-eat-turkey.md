# Can cats eat turkey — packaging draft

Status: draft only. No repo edit, commit, push, render, or post. Packaged only from the final scripts in `/workspace/drafts/`: `cats-turkey-v6-yt.json` (YouTube Short, about 18.7s at 194.5 wpm plus 0.2s of listed pads, 60 spoken words) and `tt-cats-turkey.json` (TikTok minute cut, about 91.8s, 293 spoken words plus 1.40s of listed pads). Fact pack: `/workspace/drafts/facts/cats-turkey.md` (CT-F1 to CT-F15), opened 2026-11-15. Both scripts say they are **not yet checked by a second model and not rendered.** A short TikTok twin of the YouTube cut lives at `/workspace/drafts/tts-cats-turkey.json`; this file packages the YouTube Short and the minute cut only.

Every fact line below cites its fact ID and keeps the pack's condition or hedge. No facts from outside the pack. No invented serving size in ounces or cubes. No "cats can eat turkey" without conditions. Do not say gravy is safe. Do not use the FDA carcass-in-the-trash line as a cat fact (CT-F15 is framed around dogs). Do not recite the FDA's dog pancreatitis symptom list as if it were the cat list (CT-F14).

Timed with Thanksgiving leftovers in mind (Thursday 11/26/2026), but the pack says the facts are about turkey and cats, not a holiday-only rule. A schedule slot is not assigned. Scheduling still needs Moondog88's okay. If it lands on an open date in the Night Shift week, Related video is the Things Living In Your House playlist (`related-video-rule.md`).

## Title (both cuts; lint-clean, from the scripts)

`If Cats Eat Turkey: Boneless and Fully Cooked, Says the ASPCA 🐱 (Things Living In Your House)`

94 UTF-16 units. Statement form (a leading `Can Cats Eat Turkey?` would fail lint). Searched words (`cats eat turkey`) sit in the first 40. One emoji. Series tag last; no episode number is assigned. The title follows CT-F1 (ASPCA: if you share a small bite, boneless and fully cooked). "Plain," "skinless," "generally," and "small portions" stay in the description (CT-F9) so the title does not read as a guarantee. "Your cat" is not the lead; searched words win under title-formula clause 10, same pattern as the posted dog-turkey Short.

This is the script title on both cuts. It already passes lint, so packaging does not rewrite it.

## YouTube Short — description

Can cats eat turkey? The ASPCA first recommends sticking to a pet's normal diet on Thanksgiving (CT-F1). If you do decide to feed your pet a small bite of turkey or other meat, it says make sure it is boneless and fully cooked (CT-F1). Raw or undercooked turkey may contain salmonella, and poultry bones can be a major choking hazard (CT-F2). The AVMA says plain, boneless, and skinless turkey is generally safe for pets in small portions, but gravy, sauces, dressing, and meat or poultry fat or skin can be hard to digest, and sometimes even a small amount can cause pancreatitis; the bones themselves can cause choking or intestinal blockage (CT-F9). An AVMA household-hazards brochure says cooked turkey bones can splinter and damage a pet's mouth or digestive system (CT-F11). The AVMA also discourages raw or undercooked animal-sourced protein for dogs and cats (CT-F12). Onions, garlic and chives can cause gastrointestinal irritation and red blood cell damage; the ASPCA says cats are more susceptible (CT-F7). The FDA says not to give pets high-fat scraps such as skin from a roasted turkey, which can cause an upset stomach and can cause pancreatitis; in cats, the symptoms are less clear and harder to notice, such as decreased appetite and weight loss (CT-F13, CT-F14). The ASPCA also says small amounts of lean cooked turkey free of bones and seasoning are okay, and that snacks should be no more than five percent of daily calories — that is their guideline, not a measured serving size (CT-F5, CT-F6). The spoken Short itself states CT-F1 (normal diet; boneless and fully cooked if you share a small bite) and CT-F9 (plain, boneless, and skinless, generally safe in small portions); the other conditions are in this description and in the minute cut. When in doubt, ask your vet.

#cancatseatturkey #turkeybones #thanksgivingpets #meatballmyths #shorts

Sources: /workspace/drafts/facts/cats-turkey.md (CT-F1, CT-F2, CT-F5, CT-F6, CT-F7, CT-F9, CT-F11, CT-F12, CT-F13, CT-F14); ASPCA, Thanksgiving Safety Tips, Sharing is Caring, and People Foods to Avoid Feeding Your Pets; AVMA, Thanksgiving pet safety, raw-or-undercooked policy, and household-hazards brochure (2022); FDA, Keep Your Dogs and Cats Safe From Holiday Hazards. Pages opened 2026-11-15. General information, not veterinary advice.

Hashtags are 3 topic + `#meatballmyths` + `#shorts` last, matching the scripts. The draft script description did not cite fact IDs; packaging adds the IDs and keeps every condition.

## YouTube Short — tags (10, each ≤30 characters)

These are the script tags. They match the earlier `postkit.py kw` set in `/workspace/packaging/kw/kw-studio-assignments.csv` (run 2026-11-15, America/New_York). Processed-meat suggestions are omitted. `can cats eat turkey carcass` is omitted because CT-F15 is framed around dogs.

1. can cats eat turkey
2. can cats have turkey
3. can cats eat turkey meat
4. can cats eat turkey breast
5. can cats eat turkey bones
6. do cats eat turkey bones
7. can cats eat bones
8. can cats eat raw turkey bones
9. things living in your house
10. Meatball Myths

Tag 8 is supported by the minute cut (CT-F2 / CT-F12 raw or undercooked). The YouTube Short states "boneless and fully cooked" but does not itself say "raw." "Turkey breast" is not named as a separate cut; it stays only as a search form of turkey meat under the same plain / boneless / skinless / fully cooked conditions.

## YouTube Short — pinned comment

What did your cat try to steal off the Thanksgiving table?

Open question, not yes/no. No Related-video line unless this Short is on-topic to that week's long-form. On the open November/December dates as now scheduled, it is a pet house Short: Related video is the Things Living In Your House playlist.

## TikTok minute cut — caption (MASTER_ORDERS / 11/15 template)

Paste-ready wording is the final script caption. It already follows the 11/15 rule: searched phrase first, conditions kept, a question immediately before the hashtags, five topic hashtags, no brand tag. Fact IDs are listed under the caption, not in the posted text.

```
can cats eat turkey? 🐱 The ASPCA first recommends your pet's normal diet. If you share a small bite, make it boneless and fully cooked. The AVMA says plain, boneless, and skinless turkey is generally safe for pets in small portions. Bones can choke, block, or splinter. Skin and fat can be hard to digest and can sometimes cause pancreatitis. Meatball offered a plate to his cat, Sauce. Sauce walked off. His dog, Noodle, got the turkey. What did your cat try to steal off the Thanksgiving table?
#cancatseatturkey #turkeybones #thanksgivingpets #catfoodsafety #bonelessturkey
```

Fact IDs in that caption, with conditions kept: CT-F1 (ASPCA first recommends the normal diet; if you share a small bite, boneless and fully cooked); CT-F9 (AVMA: plain, boneless, and skinless, generally safe in small portions; fat or skin can be hard to digest, and sometimes even a small amount can cause pancreatitis; bones can choke or block); CT-F11 (cooked turkey bones can splinter); CT-F13 (FDA: don't give high-fat scraps such as skin). Spoken lines in the minute script also include raw or undercooked turkey may contain salmonella (CT-F2), the AVMA discourages raw or undercooked animal-sourced protein (CT-F12), onions, garlic and chives, with cats more susceptible (CT-F3, CT-F7), FDA cat pancreatitis signs less clear, such as decreased appetite and weight loss (CT-F14), and the ASPCA five-percent snack guideline, not a measured serving size (CT-F5, CT-F6). Jokes add no claim, number, danger, feeling, motive, or safety instruction.

## TikTok minute cut — pinned comment

What did your cat try to steal off the Thanksgiving table?

## Thumbnail concept (YouTube, 16:9)

Updates `BONES OUT FIRST` in `thumbnail-concepts.md`. White or plain background. The card is a warning, not a "cats can eat this" claim. No Meatball. One red word, one arrow, readable at 168 px.

- `_a` (Short and default): on-image `BONES OUT FIRST` (3 words), red word `BONES`. One huge drawn turkey bone (or a bone-in drumstick); arrow to the bone. Bones can choke (CT-F2), block (CT-F9), or splinter (CT-F11). No serving size, no gravy boat labeled safe or unsafe.
- `_b` (long-form only): `CAN SPLINTER` (2 words), red word `SPLINTER` (CT-F11). Do not letter a cat-and-the-trash claim (CT-F15 is framed around dogs).
- `_c` (long-form only): `NO TURKEY BONES` (3 words), red word `NO`. Supported by CT-F1, CT-F9, and CT-F11.

Studio A/B is long-form only. If this stays a Short, shoot `_a` only.

## Cover concept — TikTok only

MASTER_ORDERS drops custom cover frames on YouTube Shorts. Do not upload a custom Shorts cover. Related video is a Studio field, not a frame.

For the TikTok minute cut only, a 9:16 cover: white or plain field; the same huge turkey bone as the subject, no Meatball; hand-lettered `BONES OUT FIRST` with `BONES` in red; one arrow; still readable when the cover is small on a For You feed. Do not letter a serving size, "gravy is fine," or a guarantee on the cover.

## Related video

Things Living In Your House playlist, unless a same-week house long-form later makes this Short on-topic (Claude is confirming Saturday long-form order with Nolan). See `related-video-rule.md`.
