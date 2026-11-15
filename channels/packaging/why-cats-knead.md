# Why cats knead — packaging draft (TikTok minute cut)

Status: draft only. No repo edit, commit, push, render, or post. Packaged only from the final script `/workspace/drafts/tt-cats-knead.json` (TikTok minute cut, about 89.0s at 194.5 wpm plus 1.40s of listed pads, 284 spoken words) and the fact pack `/workspace/drafts/facts/cats-knead.md` (CK-F1–CK-F7), opened 2026-11-15. The script says it is **not yet checked by a second model and not rendered.** Scheduling still needs Moondog88's okay.

Every fact line below cites its fact ID and keeps the pack's condition or hedge. No facts from outside the pack. Do not say "your cat thinks you are its mother." Do not say kneading always means the cat is happy, or that cats knead to mark you with scent glands (not on the iCatCare or UC Davis pages opened for this pack). Do not invent a number of kneads, or say every adult cat still does it (CK-F4 is "a few").

This file packages the TikTok minute cut only. No YouTube Short script was in this pass.

## Title (lint-clean, from the script)

`Why Cats Knead: It May Start When They Were Kittens 🐱 (Things Living In Your House)`

84 UTF-16 units. Statement form. Searched words (`Why Cats Knead`) sit in the first 40. The hedge is `May`. The sourced fact is CK-F6 (Emma Grigg, UC Davis: most likely carried over from kittenhood) with CK-F1 (International Cat Care: kittens tread to stimulate milk). One emoji. Series tag last; no episode number is assigned. "Your cat" is not the lead; the searched phrase wins under title-formula clause 10.

This is the script title. It already passes the title rules, so packaging does not rewrite it.

## TikTok caption (MASTER_ORDERS / 11/15 template)

Paste-ready wording is the final script caption. It already follows the 11/15 rule: searched phrase first, hedges kept (`most likely`, `almost like`), a question immediately before the hashtags, five topic hashtags, no brand tag. Fact IDs are listed under the caption, not in the posted text.

```
why do cats knead? 🐱 International Cat Care traces it to kittens treading to stimulate milk. UC Davis behaviorist Emma Grigg says it is most likely carried over from kittenhood, and on a person or bed it is a self-soothing behavior, almost like a sign of the bond. Meatball offered his cat, Sauce, a pillow. Sauce walked off. Does your cat knead you, a blanket, or both?
#whydocatsknead #catkneading #catbehavior #catsoftiktok #makingbiscuits
```

Fact IDs in that caption, with conditions kept: CK-F1 (International Cat Care: kittens treading with alternate front paws on the mother's abdomen to stimulate the flow of milk); CK-F6 (Grigg: most likely carried over from their days as kittens); CK-F7 (when they do it on a favorite person or bed, it is a self-soothing behavior; with humans it is almost like a sign of the bond — "almost like," and not voiced as the cat's thoughts).

Spoken lines in the minute script also include: if a cat kneads on your lap or chest, International Cat Care says this shows they associate your relationship with that of their mother when they were a kitten (CK-F2; location condition: lap or chest; do not harden it into "thinks you are its mother"); some cats dribble as they anticipate the milk-feed that kneading usually predicted (CK-F3, "some cats"); cats grow out of it when it ceases to be necessary, but a few retain it into adulthood, particularly around someone they feel safe with, or on a fluffy cushion or blanket (CK-F4, "a few," "particularly"); and kneading is a perfectly normal behavior, and cats should never be punished for it, even if the claws are a little painful (CK-F5). "Making biscuits" appears only as a popular name in the hashtags, not as a mechanism. Jokes add no feeling or motive.

## Tags (10, each ≤30 characters, from `postkit.py kw`)

Keyword file: `/workspace/packaging/kw/kw-studio-assignments.csv` (run 2026-11-15, America/New_York), plus the script's shorter tags. The script listed seven tags; three searched forms the spoken cut can answer were added to reach the 8–12 range. Over-30-character suggestions (`why do cats knead with their paws`, 31; `why do cats knead on soft blankets`, 32) are omitted. "Knead and bite" and "purr and knead" are omitted because the spoken cut does not treat biting or purring.

1. why do cats knead
2. why does my cat knead
3. why do cats knead you
4. cat kneading
5. cats making biscuits
6. cat knead blanket
7. why do cats knead on people
8. why do cats knead and nurse
9. things living in your house
10. Meatball Myths

Tag 8 stays because the cut traces kneading to kittens treading to stimulate milk (CK-F1, CK-F6). Tag 6 stays because CK-F4 names a fluffy cushion or blanket as a place a few adults retain the behavior.

## Pinned comment

Does your cat knead you, a blanket, or both?

Open question, not yes/no.

## Cover concept — TikTok only

This is a TikTok minute cut, so the cover is 9:16 only. There is no YouTube Short in this pass, and MASTER_ORDERS drops custom cover frames on YouTube Shorts anyway.

White or plain field; one huge pair of drawn front paws kneading a folded blanket, no Meatball; hand-lettered `WHY THE BISCUITS?` (3 words) with `BISCUITS` in red; one arrow to the paws; still readable when the cover is small on a For You feed. "Biscuits" is the popular name, not a sourced mechanism. Do not letter "thinks you're mom," scent glands, a knead count, or "always happy."

A claim-backed long-form challenger, `MAY START THEN` / `MAY` or `FROM KITTENHOOD`, is in `thumbnail-concepts.md` and is not this cover.

## Related video

Related video is a YouTube Studio field. This package is a TikTok cut, so no Related video is set here. If a YouTube Short twin is later made, it is a pet house video: Things Living In Your House playlist, not that week's long-form, unless a same-creature house long-form is later scheduled as that week's lead (Claude is confirming Saturday long-form order with Nolan). Off-topic pins stay an open question and drop the Related-video line. See `related-video-rule.md`.

## Lint (`postkit.py lint`, 2026-11-15, America/New_York)

TikTok stub: `/workspace/packaging/lint-specs/tt-cats-knead.json`. **Pass (0 fail, 0 warn).** Caption 444 of 2,200 units, five topic hashtags. A title-only YouTube stub (`yt-why-cats-knead-title.json`) also passed with the expected 1 WARN (5 YouTube hashtags vs coded four). This package is a TikTok cut; that YT stub was only to confirm the title is lint-clean (84 units).
