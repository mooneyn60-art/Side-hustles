# Can dogs eat chocolate?

Draft: Sunday, Nov 15, 2026 (America/New_York).  
Status: **not pushed**. Fact pack: `/workspace/drafts/facts/chocolate.md`.  
Specs: `/workspace/drafts/chocolate-v6-yt.json` (YouTube Short, December v6), `/workspace/drafts/tts-chocolate.json` (TikTok short twin). No TikTok minute cut was requested on this pass.  
Templates: YouTube + tts follow the dog-turkey / cat-sugar drawn-house pair (mystery music on YouTube, detective on the tts twin).  
Written only from the fact pack, using the FDA figures that match the December 12/01 16:00 ET packaging title. Pages in that pack were opened live on 2026-11-15. This script pass did not re-fetch those pages. Still needs a second-model check and a render/transcript pass before it can be scheduled.

Title uses the packaging statement form, 95 UTF-16 units: `Can Dogs Eat Chocolate: Mild Signs Can Start at 9 mg Per Pound 🍫 (Things Living In Your House)`. No episode number is assigned. Series: Things Living In Your House.

Hashtags follow MASTER_ORDERS: YouTube description uses `#dogchocolate #candogseatchocolate #theobromine #meatballmyths #shorts` (three topic tags, then brand, `#shorts` last). TikTok caption uses `#dogchocolate #candogseatchocolate #theobromine #dogsafety #pethealth` (five topic tags, no brand, no `#fyp`). Cake and chocolate-chip search tags from the packaging lint were dropped because the spoken cut does not name those foods; chips remain in the fact pack and can return if a later cut covers them.

The Short uses FDA units only (mg per pound of body weight; theobromine per ounce). Merck mg/kg and UC Davis oz/lb figures stay in the pack and are not spoken. No invented dose thresholds. No amount is called safe. His dog, Noodle (comma form) goes for the tin as action only — the joke does not add that Noodle was fine or got sick. The call-for-help line is on the last YouTube card and in the description, in the FDA's wording. The tts twin speaks a shortened “Call your veterinarian,” clean, with the reaction after.

This is general information, not veterinary advice.

---

## A. YouTube Short (mild words)

**Estimated runtime: 19.9 seconds** (16–20s target). 4 lines, 64 spoken words, plus 0.20s of listed pads. Pacing is calibrated to the posted moose minute cut (289 words in 89.13s ≈ 194.5 wpm on Andrew at +10%). One mild word: “damn,” in the line 2 gag.

Hook and last line share the kitchen so the final “And” loops into the first line. Frame 0 is the dog already in view (`open: animal`). Line 2, the acted gag, starts at 3.1s (inside the 3–7s window). Studio should show Meatball hiding the cake and Noodle getting the tin; there is no Noodle character key in the schema.

| # | Time | Scene | Spoken line | Fact IDs |
|---|---|---|---|---|
| 1 | 0.0–3.1s | open / kitchen | Can dogs eat chocolate? The FDA says chocolate is toxic. | CH-F1 (hook + FDA: chocolate is toxic [to dogs; “to dogs” is on the card and in the description]) |
| 2 | 3.1–6.7s | kitchen | Meatball hid the cake. His dog, Noodle, got the damn tin. | (no fact; acted Meatball gag; Noodle plant, comma form; action only) |
| 3 | 6.7–13.8s | study | Theobromine can cause mild signs as low as 9 milligrams per pound of body weight, and severe signs around 18, the FDA says. | CH-F4 (theobromine; mild signs as low as 9 milligrams per pound of body weight; severe signs around 18; FDA) |
| 4 | 13.8–19.9s | kitchen | Dark chocolate, 70 to 85 percent cacao, has about 227 milligrams an ounce, it says; milk chocolate, about 57. And | CH-F3 (FDA table: dark chocolate 70–85% cacao about 227 mg an ounce; milk chocolate about 57) |

**Mild word (1):** damn (line 2).  
**Sourced facts:** CH-F1 (FDA: chocolate is toxic to dogs; theobromine is the main culprit, named in line 3), CH-F4 (9 mg per pound of body weight, mild; around 18, severe), CH-F3 (dark vs milk as the FDA table states).

The last card also carries: “IF YOUR PET IS SICK, CALL YOUR VETERINARIAN.” The description quotes the fuller FDA wording: “If your pet is sick or has a veterinary emergency, call your veterinarian. If your veterinarian is unavailable, call your local emergency animal hospital or an animal poison control center.”

### Alternate first-3-second hooks (Short)

Hook 1 is in the JSON.

1. **Draft hook (in the JSON):** “Can dogs eat chocolate? The FDA says chocolate is toxic.” (~3.1s). Leaves room for the gag inside the 3–7s window. “To dogs” is on the card, because the 20s cap was tight.
2. **Dose in the hook:** “Can dogs eat chocolate? The FDA says mild signs can start as low as 9 milligrams per pound of body weight.” (~5.9s). Matches the packaging title, but it delays the “toxic” line and theobromine, and it crowds the gag.
3. **Dark vs milk in the hook:** “Can dogs eat chocolate? The FDA says dark chocolate with 70 to 85 percent cacao has about 227 milligrams of theobromine an ounce; milk chocolate, about 57.” (~8.3s). Too long for the first-line window; it would push the gag past 7s.

---

## A2. TikTok short twin (`tts-chocolate.json`)

Same facts, same four-beat shape, sweary reactions. **Estimated runtime: 22.4 seconds** (the bison / dog-turkey tts twins also run longer than their 16–20s YouTube cuts). 72 spoken words, plus 0.20s of pads. `search_top` shows **CAN DOGS EAT / CHOCOLATE?** for 2.5s. Captions use `cap_swap`.

| # | Time | Scene | Spoken line | Fact IDs |
|---|---|---|---|---|
| 1 | 0.0–3.7s | open / kitchen | Can dogs eat chocolate? The FDA says chocolate is toxic. Holy shit. | CH-F1 (hook + FDA: chocolate is toxic) |
| 2 | 3.7–7.3s | kitchen | Meatball hid the cake. His dog, Noodle, got the fucking tin. | (no fact; acted Meatball gag; Noodle plant, comma form) |
| 3 | 7.3–14.7s | study | Theobromine can cause mild signs as low as 9 milligrams per pound of body weight, and severe signs around 18, the FDA says. Fuck. | CH-F4 (theobromine; 9 mg per pound of body weight, mild; around 18, severe; FDA) |
| 4 | 14.7–22.4s | kitchen | Dark chocolate, 70 to 85 percent cacao, has about 227 milligrams an ounce, it says; milk chocolate, about 57. Call your veterinarian. Fucking typical. And | CH-F3, CH-F6 (FDA table, dark vs milk; shortened call-for-help: “Call your veterinarian”) |

Swears: Holy shit (hook); fucking tin (gag); Fuck (after the FDA dose line); Fucking typical (after “Call your veterinarian”). Facts, credits, doses and the call-for-help fragment stay clean. The spoken call is shorter than the FDA paragraph; the full FDA wording is in the shared description.

Pinned comment: “What would you do if your dog got to the tin?”

### Fact-check (spoken lines vs the 2026-11-15 pack)

Pages were not re-fetched on this script pass. Each factual line is checked against quotes already in `/workspace/drafts/facts/chocolate.md`.

| Line | Spoken claim | Pack support | Pass? |
|---|---|---|---|
| 1 | The FDA says chocolate is toxic. | CH-F1: “Chocolate is toxic to dogs.” Species is in the hook and on the card. | Yes, with “to dogs” on the card / in the description |
| 3 | Theobromine can cause mild signs as low as 9 milligrams per pound of body weight, and severe signs around 18, the FDA says. | CH-F4: “Theobromine can cause mild signs in dogs with doses as low as 9 mg per pound of body weight, and severe signs starting around 18 mg per pound of body weight.” Spoken “around 18” keeps the unit already stated. | Yes |
| 4 | Dark chocolate, 70 to 85 percent cacao, has about 227 milligrams an ounce; milk chocolate, about 57. | CH-F3, FDA table, approximate theobromine in 1 ounce: milk 57 mg; dark chocolate with 70–85% cacao 227 mg. “About” marks the table as approximate. | Yes |
| tts 4 | Call your veterinarian. | CH-F6 / FDA: “If your pet is sick or has a veterinary emergency, call your veterinarian. If your veterinarian is unavailable, call your local emergency animal hospital or an animal poison control center.” Spoken line is the short first clause only. | Yes, as a shortened first clause; full wording is not spoken |
| — | No Merck mg/kg or UC Davis oz/lb figures are spoken. | Pack disagreement (CH-F8, CH-F10) is left in the pack. Units are not converted across sources. | Yes |
| — | Noodle got the tin. | Action only. The line does not say he was fine or got sick. | Yes (no added claim) |

White chocolate is not called safe (it is not in this spoken cut). No amount is called safe. No “a bite always kills” line.

