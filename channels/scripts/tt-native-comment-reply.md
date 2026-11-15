# TikTok-native original: comment-reply template (can dogs eat chocolate?)

Draft: Sunday, Nov 15, 2026 (America/New_York).  
Status: **not pushed**. Fact pack: `/workspace/drafts/facts/chocolate.md`.  
Spec: `/workspace/drafts/tt-native-comment-reply.json`.  
This is a reusable comment-reply format plus one worked example. It is a TikTok-native original, not a Duet or a Stitch. No commenter's name or quote was invented. The worked example uses our own pinned question from the chocolate Short: “What would you do if your dog got to the tin?”

Punch-up (this job and future ones): the hedge-mocking tag is used **at most once per script**. This cut uses it **zero** times. Hedges stay in the fact; the reaction is a Meatball action (he points at the word, squints at the bag, holds both bars up, rereads the white-chocolate line, picks up the phone).

Written only from the fact pack, using the FDA figures that match the December packaging title. Pages in that pack were opened live on 2026-11-15. This script pass did not re-fetch those pages. Still needs a second-model check and a render/transcript pass before it can be scheduled.

Title, 95 UTF-16 units: `Can Dogs Eat Chocolate: Mild Signs Can Start at 9 mg Per Pound 🍫 (Things Living In Your House)`. No episode number. Series: Things Living In Your House.

Hashtags (TikTok caption): `#dogchocolate #candogseatchocolate #theobromine #dogsafety #pethealth` (five topic tags, no brand, no `#fyp`). Cake and chocolate-chip search tags stay out of the spoken cut; chips remain in the pack.

Spoken numbers are FDA units only (mg per pound of body weight; theobromine per ounce). Merck mg/kg and UC Davis oz/lb stay in the pack. No amount is called safe. White chocolate is not called safe. His dog, Noodle (comma form) goes for the tin as action only — the joke does not add that Noodle was fine or got sick. The call-for-help line uses the FDA's wording, said clean. Cats are in the description, not spoken, to keep the runtime inside 92s.

This is general information, not veterinary advice. This is an original drawn video, not a Duet or Stitch.

---

## Template (reusable)

Comment slot: `{{COMMENT_TEXT}}`

First-line template:

> Can dogs eat chocolate? {{COMMENT_TEXT}} Holy shit.

Rules for a later swap:

- Do not invent a commenter's name, handle, or quote.
- When a real viewer comment exists, paste it verbatim into `COMMENT_TEXT` and credit it as a comment on our video, not as a named person.
- Keep the first spoken clause as the searched question.
- If the real comment asks for a dose, a home treatment, or an "is this much safe" figure the pack does not support, do not invent an answer. Stay on the checked FDA/ASPCA lines.

Worked example (this JSON): our own pinned question, labeled on the comment bar as “Pinned question on our chocolate Short.” Spoken setup: “Our pinned question was, what would you do if your dog got to the tin?”

---

## Worked-example script (`tt-native-comment-reply.json`)

**Estimated runtime: 90.9 seconds** (65–92s sweary window; over 61s for Creator Rewards). 11 lines, 290 spoken words, plus 1.40s of listed pads (0.25s on the gag and the first fact beat, 0.9s on the punch).

Hook is the searched question. A drawn comment bar shows the pinned question for the first 5s (question text only; no fake username). Line 2, the acted gag, starts at 6.5s (inside the 3–7s window). Noodle is planted early and gets the tin on the late payoff. The last line loops into the hook.

| # | Time | Scene | Spoken line | Fact IDs |
|---|---|---|---|---|
| 1 | 0.0–6.5s | open / kitchen + comment bar | Can dogs eat chocolate? Our pinned question was, what would you do if your dog got to the tin? Holy shit. | CH-F1 (hook) |
| 2 | 6.5–11.4s | kitchen | Meatball hid the cake. His dog, Noodle, was already in the kitchen. Tiny fucking plan. | (no fact; acted gag; Noodle plant, comma form) |
| 3 | 11.4–18.4s | study | The FDA says chocolate is toxic to dogs, and that theobromine is the main culprit. Meatball pointed at the word. Fucking highlighted. | CH-F1 (FDA: chocolate is toxic to dogs; theobromine is the main culprit) |
| 4 | 18.4–28.0s | basement | Theobromine can cause mild signs as low as 9 milligrams per pound of body weight, the FDA says, and severe signs around 18. Per pound of the dog. Worst fucking math. | CH-F4 (9 mg per pound of body weight, mild; around 18, severe; per pound of the dog) |
| 5 | 28.0–40.0s | bathroom | Several things can play a role, the FDA says: the amount and type of chocolate, the dog's size, and how sensitive the dog is to theobromine. No page we checked calls any amount safe. Meatball squinted. Fucking tiny print. | CH-F2 (type, amount, size, sensitivity; FDA does not call any amount safe) |
| 6 | 40.0–49.9s | garden | Dark chocolate with 70 to 85 percent cacao has about 227 milligrams of theobromine an ounce, the FDA table says; milk chocolate has about 57. Meatball held both bars up. Fucking scale. | CH-F3 (FDA table: 70–85% dark about 227 mg an ounce; milk about 57) |
| 7 | 49.9–59.4s | kitchen | Signs of chocolate toxicity can appear within a few hours, the FDA says, and can range from mild to severe. Severe toxicity can lead to death in some cases. Fucking list. | CH-F5 (signs can appear within a few hours; severe toxicity can lead to death in some cases) |
| 8 | 59.4–66.8s | study | The ASPCA says white chocolate has almost no theobromine, but sugar and fat may still lead to pancreatitis. Meatball reread it. Fucking plot twist. | CH-F7 (ASPCA: white chocolate has almost no theobromine, but sugar and fat may still lead to pancreatitis) |
| 9 | 66.8–79.2s | bedroom | If your pet is sick or has a veterinary emergency, call your veterinarian. If your veterinarian is unavailable, call your local emergency animal hospital or an animal poison control center, the FDA says. Meatball picked up the phone. Fucking finally. | CH-F6 (FDA call-for-help wording, said clean) |
| 10 | 79.2–82.2s | garden | His dog, Noodle, already had the tin. Little fucking vacuum. | (no fact; Noodle payoff, action only) |
| 11 | 82.2–90.9s | kitchen | So can dogs eat chocolate? No page we checked calls any amount safe. What would you do if your dog got to the tin? Be fucking honest. And | (loop; no amount called safe; no new claim) |

**Sweary jokes:** Tiny fucking plan; Fucking highlighted; Worst fucking math; Fucking tiny print; Fucking scale; Fucking list; Fucking plot twist; Fucking finally; Little fucking vacuum; plus hook/loop reactions (Holy shit; Be fucking honest). No hedge-mock. Facts, doses, and the call-for-help line stay clean.

Pinned comment (same as the worked-example slot): “What would you do if your dog got to the tin?”

### Alternate first-line hooks

Hook 1 is in the JSON.

1. **Draft hook (in the JSON):** “Can dogs eat chocolate? Our pinned question was, what would you do if your dog got to the tin? Holy shit.” (~6.5s). Searched question first; the slot is clearly our pin, not a viewer quote.
2. **Dose in the hook:** “Can dogs eat chocolate? The FDA says mild signs can start as low as 9 milligrams per pound of body weight. Holy shit.” (~6.5s). Matches the packaging title, but it delays the pinned question and crowds the gag.
3. **Call-for-help in the hook:** “Can dogs eat chocolate? If your pet is sick or has a veterinary emergency, call your veterinarian.” (~6.2s). Front-loads the safety line, but it drops the pin and the "toxic / theobromine" stake from the first seconds.

### Fact-check (spoken lines vs the 2026-11-15 pack)

Pages were not re-fetched on this script pass.

| Line | Spoken claim | Pack support | Pass? |
|---|---|---|---|
| 3 | The FDA says chocolate is toxic to dogs, and that theobromine is the main culprit. | CH-F1. | Yes |
| 4 | Theobromine can cause mild signs as low as 9 milligrams per pound of body weight, and severe signs around 18. Per pound of the dog. | CH-F4. Unit kept. "Around 18" keeps the unit already stated. | Yes |
| 5 | Several things can play a role: amount, type, size, sensitivity. No page we checked calls any amount safe. | CH-F2, plus the pack's "Do not say" line (no amount is called safe). | Yes |
| 6 | Dark chocolate, 70 to 85 percent cacao, about 227 milligrams of theobromine an ounce; milk chocolate about 57. | CH-F3, FDA table, "about" marks the table as approximate. | Yes |
| 7 | Signs can appear within a few hours and can range from mild to severe. Severe toxicity can lead to death in some cases. | CH-F5, FDA wording (not Merck's 6–12 hours or UC Davis 2–24). | Yes |
| 8 | White chocolate has almost no theobromine, but sugar and fat may still lead to pancreatitis. | CH-F7, ASPCA. Not called safe. "Meatball reread it" is an action, not a new rule. | Yes |
| 9 | If your pet is sick or has a veterinary emergency, call your veterinarian. If your veterinarian is unavailable, call your local emergency animal hospital or an animal poison control center, the FDA says. | CH-F6, full FDA wording, said clean. "Meatball picked up the phone" is an action after the credit. | Yes |
| 10 | Noodle already had the tin. | Action only. The line does not say he was fine or got sick. | Yes (no added claim) |

No Merck mg/kg or UC Davis oz/lb figures are spoken. No amount is called safe. No "a bite always kills" line.

---

## What Studio needs (drawn-house pipeline)

The current renderer has no comment-bar layer.

1. A reusable drawn comment bar at the top of the frame, driven by `tiktok_native.comment_slot`.
2. For this worked example, the bar shows only the question “What would you do if your dog got to the tin?” with a small credit “Pinned question on our chocolate Short.” **No fake username, avatar, or handle.**
3. A swap path so a later real comment can be pasted verbatim into `COMMENT_TEXT` and onto the first spoken line without re-laying the whole cut. If that comment asks for a figure or a home treatment the pack does not support, do not invent an answer.
4. If the finished video is posted with TikTok's native Reply-to-comment on our own pin (or, later, on a real viewer comment), use the in-app comment chrome and hide our drawn bar so the question is not shown twice. Still never a Duet or a Stitch.
5. Same rooms, cards, Andrew voice, and the Noodle/tin gag as a standard drawn-house minute. There is still no Noodle character key.
6. **Post as an original 61s+ video** (or an in-app comment reply, which is still original content), never a Duet or a Stitch, so it can stay Creator Rewards-eligible.

New spec keys: `tiktok_native` (format `comment_reply`, `comment_slot`, `worked_example`), `comment_bar`, `say_template` on beat 1.
