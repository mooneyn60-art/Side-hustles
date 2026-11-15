# Why dogs lick you — packaging draft (TikTok minute cut)

Status: draft only. No repo edit, commit, push, render, or post. Packaged only from the final script `/workspace/drafts/tt-dogs-lick.json` (TikTok minute cut, about 73.0s at 194.5 wpm plus 1.40s of listed pads, 232 spoken words) and the fact pack `/workspace/drafts/facts/dogs-lick.md` (DL-F1–DL-F8), opened 2026-11-15. The script says it is **not yet checked by a second model and not rendered.** Scheduling still needs Moondog88's okay.

Every fact line below cites its fact ID and keeps the pack's condition or hedge. No facts from outside the pack. Do not say licking you "is a kiss," "always means love," or "always means anxiety." Do not flatten lip licking into licking a person. Do not say dogs lick people for salt, for food taste, or to show love (not on the opened pages).

This file packages the TikTok minute cut only. No YouTube Short script was in this pass.

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

This is a TikTok minute cut, so the cover is 9:16 only. There is no YouTube Short in this pass, and MASTER_ORDERS drops custom cover frames on YouTube Shorts anyway.

White or plain field; one huge drawn close-up of a dog's face and tongue, no Meatball; hand-lettered `NOT A KISS` (3 words) with `KISS` in red; one arrow to the tongue or to the word `KISS`; still readable when the cover is small on a For You feed. The line is DL-F1. Do not letter "it's love," "food ask," or "always anxious." Do not put a sandwich on this cover as if lunch were the cause (the pack does not support salt or food-taste as a reason dogs lick you).

The audit hook `LICK OR LUNCH?` is updated in `thumbnail-concepts.md` as a question card, not a cause. It is not the TikTok cover, because "lunch" is not a sourced mechanism.

## Related video

Related video is a YouTube Studio field. This package is a TikTok cut, so no Related video is set here. If a YouTube Short twin is later made, it is a pet house video: Things Living In Your House playlist, not that week's long-form, unless a same-creature house long-form is later scheduled as that week's lead (Claude is confirming Saturday long-form order with Nolan). Off-topic pins stay an open question and drop the Related-video line. See `related-video-rule.md`.

## Lint (`postkit.py lint`, 2026-11-15, America/New_York)

TikTok stub: `/workspace/packaging/lint-specs/tt-dogs-lick.json`. **Pass (0 fail, 0 warn).** Caption 391 of 2,200 units, five topic hashtags. A title-only YouTube stub (`yt-why-dogs-lick-title.json`) also passed with the expected 1 WARN (5 YouTube hashtags vs coded four). This package is a TikTok cut; that YT stub was only to confirm the title is lint-clean (81 units).
