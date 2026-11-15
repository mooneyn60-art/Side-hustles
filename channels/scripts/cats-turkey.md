# Can cats eat turkey?

Draft: Sunday, Nov 15, 2026 (America/New_York).  
Status: **not pushed**. Fact pack: `/workspace/drafts/facts/cats-turkey.md`.  
Specs: `/workspace/drafts/cats-turkey-v6-yt.json` (YouTube Short), `/workspace/drafts/tts-cats-turkey.json` (TikTok short twin), `/workspace/drafts/tt-cats-turkey.json` (TikTok minute cut, rules-default).  
Templates: YouTube + tts follow the dog-turkey / cat-sugar drawn-house pair (mystery music on YouTube, detective on the tts twin). The minute cut follows the newer pet minute schema (`tt-cat-sugar.json`, compared with `tt-dog-guilty-look.json`) and MASTER_ORDERS / Nolan 11/11 (about one swear per line, 6–9 sweary jokes).  
Written only from the fact pack. Pages in that pack were opened live on 2026-11-15. This script pass did not re-fetch those pages. Still needs a second-model check and a render/transcript pass before it can be scheduled.

Title uses the packaging statement form, 94 UTF-16 units: `If Cats Eat Turkey: Boneless and Fully Cooked, Says the ASPCA 🐱 (Things Living In Your House)`. No episode number is assigned. Series: Things Living In Your House.

Hashtags follow MASTER_ORDERS: YouTube description uses `#cancatseatturkey #turkeybones #thanksgivingpets #meatballmyths #shorts` (three topic tags, then brand, `#shorts` last). TikTok captions use `#cancatseatturkey #turkeybones #thanksgivingpets #catfoodsafety #bonelessturkey` (five topic tags, no brand, no `#fyp`).

Safety lines carry their condition (plain, boneless, skinless, fully cooked, small portions; bones; seasoning; skin and fat; cooked vs raw). Hedges use “generally,” “may,” and “can.” No gravy-is-safe line, no invented serving size, no dog-only FDA carcass claim applied to cats. His cat, Sauce (comma form) does the opposite and walks off; his dog, Noodle (comma form) ends up with the turkey. Jokes add no claim.

This is general information, not veterinary advice.

---

## A. YouTube Short (mild words)

**Estimated runtime: 18.7 seconds** (16–20s target). 4 lines, 60 spoken words, plus 0.2s of listed pads. Pacing is calibrated to the posted moose minute cut (289 words in 89.13s ≈ 194.5 wpm on Andrew at +10%). One mild word: “damn,” in the line 2 gag.

Hook and last line share the kitchen so the final “And” loops into the first line. Frame 0 is the cat already in view (`open: animal`). Meatball hops in around 2.3s. Line 2, the acted gag, starts at 3.4s (inside the 3–7s window). Studio should show Sauce walking off and Noodle ending up with the turkey; there is no Sauce/Noodle character key in the schema.

| # | Time | Scene | Spoken line | Fact IDs |
|---|---|---|---|---|
| 1 | 0.0–3.4s | open / kitchen | Can cats eat turkey? The ASPCA first recommends the normal diet. | CT-F1 (hook + ASPCA first recommends the normal diet) |
| 2 | 3.4–8.8s | kitchen | Meatball offered his cat, Sauce, a plate. Sauce walked off. His dog, Noodle, got the damn turkey. | (no fact; acted Sauce walk-off, Noodle gets the turkey) |
| 3 | 8.8–13.5s | study | If you share a small bite, the ASPCA says make it boneless and fully cooked. | CT-F1, CT-F2 (if you share a small bite: boneless and fully cooked) |
| 4 | 13.5–18.7s | kitchen | The AVMA says plain, boneless, and skinless turkey is generally safe for pets in small portions. And | CT-F9 (AVMA: generally safe if plain, boneless, and skinless, in small portions) |

**Mild word (1):** damn (line 2).  
**Sourced facts:** CT-F1 (ASPCA: normal diet first; if you share a small bite, boneless and fully cooked), CT-F9 (AVMA: generally safe if plain, boneless, and skinless, in small portions).

### Alternate first-3-second hooks (Short)

Hook 1 is in the JSON.

1. **Draft hook (in the JSON):** “Can cats eat turkey? The ASPCA first recommends the normal diet.” (~3.4s). Leaves room for the gag inside the 3–7s window.
2. **Condition in the hook:** “Can cats eat turkey? Only if it's plain, boneless, skinless, and fully cooked.” (~4.3s). Front-loads the conditions but drops the agency credit and the “generally / if you share / small portions” hedges unless the line runs longer.
3. **AVMA hedge in the hook:** “Can cats eat turkey? The AVMA says plain, boneless, and skinless turkey is generally safe for pets in small portions.” (~6.8s). Stronger stake, but it delays the gag and spends the “generally” before the ASPCA's first recommendation is heard.

---

## A2. TikTok short twin (`tts-cats-turkey.json`)

Same facts, same four-beat shape, sweary reactions. **Estimated runtime: 21.2 seconds** (the bison / dog-turkey tts twins also run longer than their 16–20s YouTube cuts). 68 spoken words, plus 0.2s of pads. `search_top` shows **CAN CATS / EAT TURKEY?** for 2.5s. Captions use `cap_swap`.

| # | Time | Scene | Spoken line | Fact IDs |
|---|---|---|---|---|
| 1 | 0.0–4.0s | open / kitchen | Can cats eat turkey? The ASPCA first recommends the normal diet. Holy shit. | CT-F1 (hook + ASPCA first recommends the normal diet) |
| 2 | 4.0–9.5s | kitchen | Meatball offered his cat, Sauce, a plate. Sauce walked off. His dog, Noodle, got the fucking turkey. | (no fact; acted Sauce walk-off, Noodle gets the turkey) |
| 3 | 9.5–15.0s | study | If you share a small bite, the ASPCA says make it boneless and fully cooked. Fucking typical, Meatball. | CT-F1, CT-F2 (if you share a small bite: boneless and fully cooked) |
| 4 | 15.0–21.2s | kitchen | The AVMA says plain, boneless, and skinless turkey is generally safe for pets in small portions. Generally. Fucking generally. And | CT-F9 (AVMA: generally safe if plain, boneless, and skinless, in small portions) |

Swears: Holy shit (hook); fucking turkey (gag); Fucking typical (after the ASPCA condition); Fucking generally (after the AVMA hedge). Facts, credits and the “generally safe” hedge stay clean.

---

## B. TikTok minute cut, rules-default (`tt-cats-turkey.json`)

**Estimated runtime: 91.8 seconds** (65–92s sweary window). 13 lines, 293 spoken words, plus 1.40s of listed pads (0.25s on the gag and the Sauce walk-off, 0.9s on the punch).

**This cut follows MASTER_ORDERS / Nolan 11/11:** about one swear per line; 6–9 sweary jokes. Facts, credits and hedges are said clean, with the swear after. Hook is the searched question. Line 2 is the acted Meatball gag. Sauce is planted early (comma form) and walks off; Noodle gets the turkey on the late payoff. The last line loops into the hook.

| # | Time | Scene | Spoken line | Fact IDs |
|---|---|---|---|---|
| 1 | 0.0–4.0s | open / kitchen | Can cats eat turkey? The ASPCA first recommends the normal diet. Holy shit. | CT-F1 (hook + ASPCA first recommends the normal diet) |
| 2 | 4.0–7.3s | kitchen | Meatball plated leftovers for his cat, Sauce. Fancy as fuck. | (no fact; acted Meatball gag; Sauce plant, comma form) |
| 3 | 7.3–10.7s | bedroom | Sauce walked off. Meatball stood there like a fucking waiter. | (no fact; Sauce walks off) |
| 4 | 10.7–16.8s | study | If you share a small bite of turkey, the ASPCA says make it boneless and fully cooked. Fucking typical, Meatball. | CT-F1, CT-F2 (if you share a small bite: boneless and fully cooked) |
| 5 | 16.8–24.3s | basement | Raw or undercooked turkey may contain salmonella, the ASPCA says. The AVMA discourages raw or undercooked poultry for dogs and cats. Serious as fuck. | CT-F2, CT-F12 (raw/undercooked may contain salmonella; AVMA discourages raw poultry) |
| 6 | 24.3–32.6s | bathroom | Poultry bones can be a major choking hazard, the ASPCA says. The AVMA says bones can choke or block, and cooked turkey bones can splinter. Fucking souvenir. | CT-F2, CT-F9, CT-F11 (bones: choke, block, splinter, including cooked turkey bones) |
| 7 | 32.6–40.0s | garden | Onions, garlic and chives can be toxic to pets, the ASPCA says, and can damage red blood cells. Cats are more susceptible. Fucking seasoning. | CT-F3, CT-F7 (onions, garlic, chives; red blood cells; cats more susceptible) |
| 8 | 40.0–49.9s | kitchen | The FDA says don't give high-fat scraps such as fat trimmings or skin from a roasted turkey. They can cause an upset stomach, and they can also cause pancreatitis. Put the skin down, Meatball. Fucking hell. | CT-F13 (FDA: no high-fat scraps such as fat trimmings or roasted turkey skin; can upset the stomach and can cause pancreatitis) |
| 9 | 49.9–62.2s | study | The AVMA says plain, boneless, and skinless turkey is generally safe for pets in small portions. Gravy, sauces, dressing, and fat or skin can be hard to digest, and sometimes even a small amount can cause pancreatitis. Generally. Fucking generally. | CT-F9 (AVMA: generally safe if plain, boneless, and skinless, in small portions; gravy, sauces, dressing, fat or skin can be hard to digest, and sometimes even a small amount can cause pancreatitis) |
| 10 | 62.2–72.7s | bedroom | The ASPCA also says small amounts of lean cooked turkey free of bones and seasoning are okay. Snacks should be no more than five percent of daily calories. That's their guideline. Fucking math class. | CT-F5, CT-F6 (small amounts of lean cooked turkey free of bones and seasoning; five-percent snack figure, credited as the ASPCA's guideline) |
| 11 | 72.7–80.4s | basement | In cats, the FDA says pancreatitis symptoms are less clear, such as decreased appetite and weight loss. Not the dog list. Fucking easy to miss. | CT-F14 (in cats, pancreatitis symptoms are less clear; not the dog list) |
| 12 | 80.4–83.5s | garden | His dog, Noodle, already had the turkey. Little fucking vacuum. | (no fact; Noodle payoff, comma form) |
| 13 | 83.5–91.8s | kitchen | So can cats eat turkey? Only with those conditions. What did your cat try to steal off the Thanksgiving table? Be fucking honest. And | (loop question; no new claim) |

On-screen for the first 2.5s: **CAN CATS / EAT TURKEY?**

**Swears:** one per line.  
**Sweary jokes (8):** Fancy as fuck; like a fucking waiter; Fucking typical; Fucking souvenir; Fucking seasoning; Fucking raccoon energy; Fucking math class; Little fucking vacuum.  
**Bare reactions after clean facts or hedges:** Holy shit; Serious as fuck; Generally. Fucking generally; Fucking easy to miss; Be fucking honest.

Auto acting is off on the safety beats so the cat does not chomp while hazards are named.

### Alternate first-3-second hooks (minute cut)

1. **Draft hook (in the JSON):** “Can cats eat turkey? The ASPCA first recommends the normal diet. Holy shit.” (~4.0s).
2. **Condition in the hook:** “Can cats eat turkey? Only if it's plain, boneless, skinless, and fully cooked. Holy shit.” (~5.2s). Front-loads the conditions but drops the agency credit unless the line runs longer, and it delays the gag.
3. **AVMA hedge in the hook:** “Can cats eat turkey? The AVMA says plain, boneless, and skinless turkey is generally safe for pets in small portions. Holy shit.” (~7.7s). Stronger stake, but it spends the “generally” before the ASPCA's first recommendation and the acted gag.

---

## Fact-check table

Pages were opened live on 2026-11-15 (America/New_York) when `/workspace/drafts/facts/cats-turkey.md` was built. “Verified” means the pack's quoted wording still supports the spoken line or card. This script pass did not re-fetch those pages.

| Line (cut) | Claim in the cut | Source URL | Verified | Note |
|---|---|---|---|---|
| Short 1 / Minute 1 | The ASPCA first recommends the normal diet / sticking to your pet's normal diet. | https://www.aspca.org/pet-care/general-pet-care/thanksgiving-safety-tips | Yes, against the pack quote | “While we recommend sticking to your pet's normal diet on Thanksgiving.” The short says “the normal diet”; the minute says “your pet's normal diet.” “Pets” on this page includes cats and dogs. |
| Short 3 / Minute 4 | If you share a small bite, the ASPCA says make it boneless and fully cooked. | https://www.aspca.org/pet-care/general-pet-care/thanksgiving-safety-tips | Yes, against the pack quote | “If you do decide to feed your pet a small bite of turkey or other meat, make sure it's boneless and fully cooked.” The short drops “of turkey or other meat” for time; the minute keeps “of turkey.” The “if you share / if you do” condition is spoken. |
| Short 4 / Minute 9 | The AVMA says plain, boneless, and skinless turkey is generally safe for pets in small portions. | https://www.avma.org/resources-tools/pet-owners/petcare/thanksgiving-pet-safety | Yes, against the pack quote | Word-for-word conditions: plain, boneless, and skinless; “generally safe”; “for pets in small portions.” |
| Minute 5 | Raw or undercooked turkey may contain salmonella, the ASPCA says. The AVMA discourages raw or undercooked poultry for dogs and cats. | https://www.aspca.org/pet-care/general-pet-care/thanksgiving-safety-tips and https://www.avma.org/resources-tools/avma-policies/raw-or-undercooked-animal-source-protein-cat-and-dog-diets | Yes, against the pack quotes | ASPCA: “may contain.” AVMA “discourages,” and names dogs and cats and poultry. |
| Minute 6 | Poultry bones can be a major choking hazard (ASPCA). The AVMA says bones can choke or block, and cooked turkey bones can splinter. | https://www.aspca.org/pet-care/general-pet-care/thanksgiving-safety-tips ; https://www.avma.org/resources-tools/pet-owners/petcare/thanksgiving-pet-safety ; https://ebusiness.avma.org/files/productdownloads/mcm-client-brochures-household-hazards-2022.pdf | Yes, against the pack quotes | Thanksgiving page: choking or intestinal blockage. Brochure: cooked turkey bones can splinter. The spoken “choke or block” is a tight reading of that AVMA sentence, not a new mechanism. |
| Minute 7 | Onions, garlic and chives can be toxic to pets, the ASPCA says, and can damage red blood cells. Cats are more susceptible. | https://www.aspca.org/pet-care/general-pet-care/thanksgiving-safety-tips and https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets | Yes, against the pack quotes | Thanksgiving page names onions and garlic as toxic to pets. The people-foods page adds chives, red blood cell damage / anemia, and “cats are more susceptible.” |
| Minute 8 | The FDA says don't give high-fat scraps such as fat trimmings or skin from a roasted turkey. They can cause an upset stomach, and they can also cause pancreatitis. | https://www.fda.gov/consumers/consumer-updates/keep-your-dogs-and-cats-safe-holiday-hazards | Yes, against the pack quote | Spoken as “they can,” not “your cat will.” The page's “potentially life-threatening” wording is left out of speech (same caution used on the dog-turkey check). The carcass-in-the-trash line is not used; it is framed as “Dogs, especially.” |
| Minute 9 (the “but” clause) | Gravy, sauces, dressing, and fat or skin can be hard to digest, and sometimes even a small amount can cause pancreatitis. | https://www.avma.org/resources-tools/pet-owners/petcare/thanksgiving-pet-safety | Yes, against the pack quote | Spoken so gravy is not called safe. The ASPCA Thanksgiving “drizzle of gravy” line is unused. |
| Minute 10 | The ASPCA also says small amounts of lean cooked turkey free of bones and seasoning are okay. Snacks should be no more than five percent of daily calories. That's their guideline. | https://www.aspca.org/news/sharing-caring-foods-you-can-safely-share-your-pet | Yes, against the pack quote | Five percent is credited as the ASPCA's guideline, not a measured serving size. |
| Minute 11 | In cats, the FDA says pancreatitis symptoms are less clear, such as decreased appetite and weight loss. Not the dog list. | https://www.fda.gov/consumers/consumer-updates/keep-your-dogs-and-cats-safe-holiday-hazards | Yes, against the pack quote | The page also says “harder to notice”; the spoken line keeps “less clear” and the two cat examples. The dog symptom list is not recited as a cat list. |
| Unused on purpose | FDA turkey-carcass trash warning | https://www.fda.gov/consumers/consumer-updates/keep-your-dogs-and-cats-safe-holiday-hazards | Yes (unused) | Framed as “Dogs, especially.” Not applied to cats. |
| Unused on purpose | ASPCA “drizzle of gravy” / “A Feast Fit for a King” | https://www.aspca.org/pet-care/general-pet-care/thanksgiving-safety-tips | Yes (unused) | Conflicts with the same page's bouillon/sodium warning and with the AVMA gravy grouping. |
| Unused on purpose | A serving size in ounces or cubes | — | n/a | Not on the agency pages in the pack. Not invented. |

---

## Rules these drafts could not fully satisfy

- **Second-model check before scheduling.** MASTER_ORDERS requires a different model to check every changed line against the live pages. These drafts were written from pack quotes opened on 2026-11-15, but this is still the writer's pass, and the pages were not re-fetched on this script pass.
- **Exact runtime and the 2.3s Meatball hop.** Runtimes are word-count estimates. The hop-in is a renderer convention. No render, lint, or voicecheck was run.
- **Sauce and Noodle on screen.** The drawn-house schema used here is one `stage.creature` (a cat). There is no Sauce or Noodle character key. Line 2–3 and the Noodle payoff are written as acted shots; Studio has to draw them. The YouTube short also has to show both pets in one gag line.
- **Episode number and Related video.** Packaging left the episode number unassigned, so the title has no `#N`. The pinned question does not add “Full list in the Related video 👆” because this pass does not have a confirmed on-topic long-form or playlist target for the week it would post.
- **YouTube short does not speak raw turkey, bones, skin, or seasoning.** Those conditions are in the description, the minute cut, and (for raw) a YouTube tag. The 16–20s cap only fit the ASPCA first recommendation, the boneless-and-fully-cooked “if you share” line, and the AVMA “generally safe” conditions.
- **“An ASPCA article” vs the Sharing-is-Caring title.** The minute credits “The ASPCA also says” for the lean-cooked / five-percent lines (CT-F5, CT-F6). The full article title stays in the sources and the description.
- **AVMA “choke or block.”** Tightened from “can cause choking or intestinal blockage” to fit the runtime. The card keeps the fuller wording.
- **Hashtag feeds were not re-run on this pass.** Topic tags follow the 2026-11-15 packaging / `postkit.py kw` list already written for this title.

Nothing was pushed.
