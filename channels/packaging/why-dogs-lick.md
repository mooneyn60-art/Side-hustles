# Why dogs lick you — packaging draft (TikTok minute cut)

Status: draft only. No repo edit, commit, push, render, or post. Packaged only from the final script `/workspace/drafts/tt-dogs-lick.json` (TikTok minute cut, about 73.0s at 194.5 wpm plus 1.40s of listed pads, 232 spoken words) and the fact pack `/workspace/drafts/facts/dogs-lick.md` (DL-F1–DL-F8), opened 2026-11-15. The script says it is **not yet checked by a second model and not rendered.** Scheduling still needs Moondog88's okay.

Every fact line below cites its fact ID and keeps the pack's condition or hedge. No facts from outside the pack. Do not say licking you "is a kiss," "always means love," or "always means anxiety." Do not flatten lip licking into licking a person. Do not say dogs lick people for salt, for food taste, or to show love (not on the opened pages).

This file now packages the TikTok minute cut and, in the section below, the YouTube Short plus its short TikTok twin. The minute-cut packaging above is unchanged except where a sentence said no Short existed.

## Title (lint-clean, from the script)

`Why Dogs Lick You: Penn Vet Says It's Not a Kiss 🐶 (Things Living In Your House)`

81 UTF-16 units. Statement form. Searched words (`Why Dogs Lick You`) sit in the first 40. One emoji. Series tag last; no episode number is assigned. The sourced fact is DL-F1 (Penn Vet: not a "kiss"). "Your dog" is not the lead; the searched phrase wins under title-formula clause 10.

This is the script title. It already passes the title rules, so packaging does not rewrite it.

## TikTok caption (MASTER_ORDERS / 11/15 template)

Paste-ready wording is the final script caption. It already follows the 11/15 rule: searched phrase first, conditions kept, a question immediately before the hashtags, five topic hashtags, no brand tag. Fact IDs are listed under the caption, not in the posted text.

```
why do dogs lick you? 🐶 Penn Vet says it is not a kiss. It is a greeting behavior, but if a dog licks someone repeatedly, he may be anxious about that person. Lip licking is a different signal. Meatball puckered up at his dog, Noodle. Noodle already had the sandwich. What does your dog lick first, your face or your food?
#whydodogslickyou #doglicking #dogbehavior #dogsoftiktok #dogfacts
```

Fact IDs in that caption, with conditions kept: DL-F1 (Penn Vet: licking a person or another dog is not a "kiss"; it is a greeting behavior, but if a dog licks someone repeatedly, he may be anxious about that dog or person). "Lip licking is a different signal" is DL-F2 (the same handout: dog licks his lips — anxiety about a situation or interaction; not the same behavior as licking a person).

Spoken lines in the minute script also include AAHA listing lip licking and nose licking among common signs of anxiety or distress in dogs and cats (DL-F6; not "licking you"); Texas A&M listing licking lips, often with yawning, among signs of a nervous or alerted dog (DL-F7); a Tufts veterinary behaviorist saying an anxious dog may also appear extra friendly and lick a face (DL-F4, "may"); and Penn Vet saying dogs do not kiss, and they may be frightened by kissing (DL-F3). Texas A&M's lip-smacking / snack line (DL-F8) is not used as a reason dogs lick people. Jokes add no feeling or motive and do not turn a greeting lick into love or a lip-lick into a face-lick.

## Tags (9, each ≤30 characters, from `postkit.py kw`)

Keyword file: `/workspace/packaging/kw/kw-studio-assignments.csv` (run 2026-11-15, America/New_York), plus the script's shorter topic tags the cut actually answers. The script listed seven tags; two searched forms the spoken cut can answer were added to reach the 8–12 range. Body-part suggestions the pack does not treat (feet, hands, mouth, ears, legs, wounds) are omitted.

1. why do dogs lick you
2. why does my dog lick me
3. why do dogs lick your face
4. why do dogs lick you so much
5. dog licking face
6. dog greeting behavior
7. dog lip licking
8. things living in your house
9. Meatball Myths

Tag 3 stays because the cut states Tufts' "may also … lick their face" line (DL-F4) and keeps it separate from lip licking. Tag 4 stays because repeated licking is the DL-F1 condition.

## Pinned comment

What does your dog lick first, your face or your food?

Open question, not yes/no. The "food" half is a viewer question about the gag (Noodle already had the sandwich), not a claim that dogs lick people for food.

## Cover concept — TikTok only

This cover is for the TikTok minute cut, 9:16 only. The YouTube Short gets no custom cover frame; its 16:9 thumbnail is the `LICK OR LUNCH?` hook card in `thumbnail-concepts.md`. The short TikTok twin can reuse `NOT A KISS`.

White or plain field; one huge drawn close-up of a dog's face and tongue, no Meatball; hand-lettered `NOT A KISS` (3 words) with `KISS` in red; one arrow to the tongue or to the word `KISS`; still readable when the cover is small on a For You feed. The line is DL-F1. Do not letter "it's love," "food ask," or "always anxious." Do not put a sandwich on this cover as if lunch were the cause (the pack does not support salt or food-taste as a reason dogs lick you).

The audit hook `LICK OR LUNCH?` is updated in `thumbnail-concepts.md` as a question card, not a cause. It is not the TikTok cover, because "lunch" is not a sourced mechanism.

## Related video (minute cut)

Related video is a YouTube Studio field. The minute cut is TikTok-only, so no Related video is set here. The YouTube Short target is in the section below.

## YouTube Short + short TT cut

Status: draft only. Packaged from `/workspace/drafts/dogs-lick-v6-yt.json` (YouTube Short, about 19.0s at 194.5 wpm plus 0.2s of listed pads, 61 spoken words), `/workspace/drafts/tts-dogs-lick.json` (short TikTok twin, about 22.1s, 71 spoken words), and the readable copy `/workspace/drafts/dogs-lick-short.md`. Facts in the spoken Short are DL-F1 and DL-F2. The lip-licking anxiety wording belongs in the description, not as a shortened “licking you means anxiety” line. Both scripts say they are **not yet checked by a second model and not rendered.**

### YouTube title

`Why Dogs Lick You: Penn Vet Says It's Not a Kiss 🐶 (Things Living In Your House)`

81 UTF-16 units. This is Scriptwriter’s draft title, and it already matches the 11/12 formula and the minute-cut title: statement form, searched words in the first 40, one sourced fact (DL-F1), one emoji, series tag last, no banned words. **Kept.** The episode number is unassigned. In `posted.csv`, the highest Things Living In Your House number already in a title is **#70** (`If Dogs Eat Turkey: Boneless and Fully Cooked, Says the ASPCA`, YouTube 2026-11-12 21:47 ET). The next free number is **#71**. Historical gaps (#10–#18, #23–#36) and unnumbered hook-test / sim3d titles are not reused as “next.” Do not add `#71` to the title until Studio assigns it. If this Short and the knead Short are both scheduled, they should take the next free numbers in the order they go up (#71, then #72).

### YouTube description

Why do dogs lick you? A University of Pennsylvania School of Veterinary Medicine handout says a dog licking a person or another dog is not a "kiss." It is a greeting behavior, but if a dog licks someone repeatedly, he may be anxious about that dog or person (DL-F1). Lip licking is a different signal: Penn Vet lists it as anxiety about a situation or interaction (DL-F2). That anxiety reading is about a dog licking his own lips, not about licking a person. A lick is not automatically love, and it is not automatically anxiety.

#whydodogslickyou #doglicking #dogbehavior #meatballmyths #shorts

Sources: /workspace/drafts/facts/dogs-lick.md (DL-F1, DL-F2); University of Pennsylvania School of Veterinary Medicine, Dog Body Language Basics, https://www.vet.upenn.edu/wp-content/uploads/2024/12/dogbodylanguagebasics-pdf.pdf . Pages opened 2026-11-15. General information, not a diagnosis of your dog.

Scriptwriter’s hashtags are kept: 3 topic tags, then `#meatballmyths`, then `#shorts` last. The draft script description already had the lip-licking anxiety wording and did not cite fact IDs; packaging adds the IDs and the lips-vs-person condition. The spoken Short names lip licking as a different signal (DL-F2) and leaves this anxiety wording in the description, to stay inside 20s. Tufts, AAHA, and Texas A&M lines from the pack are used in the minute cut, not in this Short.

### Tags (9, each ≤30 characters, from `postkit.py kw`)

Same set as the minute-cut packaging, from `/workspace/packaging/kw/kw-studio-assignments.csv` (run 2026-11-15, America/New_York). Scriptwriter’s draft listed seven tags; two searched forms the Short can answer (`why do dogs lick your face`, `why do dogs lick you so much`) were kept so the list meets 8–12. Body-part suggestions the pack does not treat (feet, hands, mouth, ears, legs, wounds) stay out.

1. why do dogs lick you
2. why does my dog lick me
3. why do dogs lick your face
4. why do dogs lick you so much
5. dog licking face
6. dog greeting behavior
7. dog lip licking
8. things living in your house
9. Meatball Myths

### TikTok caption (short cut)

Paste-ready wording is the `tts-dogs-lick.json` caption. Five topic hashtags, no brand tag, ends on the question. The lip-licking anxiety wording stays in the YouTube description; the short caption, like the spoken Short, only names lip licking as a different signal.

```
why do dogs lick you? 🐶 Penn Vet says it is not a kiss. It is a greeting behavior, but if a dog licks someone repeatedly, he may be anxious about that person. Lip licking is a different signal. Meatball puckered up. His dog, Noodle, got the sandwich. What does your dog lick first, your face or your food?
#whydodogslickyou #doglicking #dogbehavior #dogsoftiktok #dogfacts
```

Fact IDs: DL-F1 (not a "kiss"; greeting; if a dog licks someone repeatedly, he may be anxious about that person). "Lip licking is a different signal" is DL-F2; the pack’s anxiety-about-a-situation wording is in the YouTube description.

### Pinned comment

What does your dog lick first, your face or your food?

Scriptwriter’s draft pin, kept. Open question, not yes/no. No Related-video line: the proposed slot is off-topic to that week’s long-form.

### Related video and a proposed slot

Related video: **Things Living In Your House playlist**, per `related-video-rule.md`, unless the Short later lands in an on-topic house-creature week. This is a pet house Short, not a same-creature trailer.

`posted.csv` has no YouTube Short queued after Sat 11/21 14:00 (silverfish) until Wed 11/25 17:00 (Night Shift v2) and 19:00 (teaser), and none after that until Sat 12/5 08:00 (polar bear long-form). The 14 empty days from Sat 11/21 19:00 through Fri 12/04 already have draft topics in `open-dates-1121-1204.md`; this Short is not auto-dropped into one of those.

**Proposed slot:** Sun 12/06/2026 14:00 ET (usual Sunday Short hour; first usual-hour opening after that already-drafted window and the Sat 12/5 08:00 polar long-form). Related video stays the house playlist (off-topic to the polar bear long-form). At least a day from the knead Short if that one takes Mon 12/07 16:00. Studio may instead swap this into an earlier already-drafted pet day; do not add a second Short on a day that already has a packaged draft without an explicit okay. Scheduling still needs Moondog88’s okay.

### No custom Shorts cover

MASTER_ORDERS drops custom cover frames on YouTube Shorts. Leave the Shorts cover on auto / unset. The 16:9 thumbnail is `LICK OR LUNCH?` in `thumbnail-concepts.md` (a question card, not a food-cause claim). The short TikTok twin may use the `NOT A KISS` cover already specified for the minute cut.

## Lint (`postkit.py lint`, 2026-11-15, America/New_York)

- Minute-cut TikTok (`tt-dogs-lick.json`): pass (0 fail, 0 warn). Caption 391 of 2,200 units, five topic hashtags.
- YouTube Short (`yt-dogs-lick-short.json`): pass (0 fail, 1 warn). Title 81 of 100 units, 9 tags. The warning is "description has 5 hashtags (the standard is four…)." The draft follows written MASTER_ORDERS: three topic tags, then `#meatballmyths`, then `#shorts` last.
- Short TikTok twin (`tts-dogs-lick-short.json`): pass (0 fail, 0 warn). Caption 374 of 2,200 units, five topic hashtags.
