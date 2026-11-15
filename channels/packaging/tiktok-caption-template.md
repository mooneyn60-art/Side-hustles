# TikTok caption template (Studio draft)

Status: draft only. **Do not use this template on a live post until Social Studio and the channel-brain orders agree on the hashtag rule.** No repo edit, commit, push, or publish from this file.

## Conflict to resolve (read this first)

Social Studio (this assignment) wants TikTok captions to open with the searched question, then use **3 topic hashtags + `#meatballmyths`**.

`MASTER_ORDERS.md` (11/12 Posting standard) currently wants a different TikTok ending:

- Five topic hashtags.
- No `#fyp`, no `#learnontiktok`, and **no brand tag**.
- `#meatballmyths` is the brand tag, so it is **not** allowed on TikTok under that order.
- Body shape: search phrase on screen, a checked fact with its condition, a clean Meatball gag, then a question. The question ends the body, then the hashtags.
- `postkit.py lint` on a `tt-` / `tts-` filename (or a spec with `search_top`) checks for 5 topic hashtags, a `?` before the hashtags, and no `#fyp` / `#learnontiktok` / brand.

These two rules cannot both be satisfied. This file writes Studio's version as requested, then shows the current MASTER_ORDERS shape so Studio can pick one and, if needed, update MASTER_ORDERS and the lint rule together.

The YouTube description hashtag rule is a separate fight (written 11/12: 3 topic + `#meatballmyths` + `#shorts`; lint still warns that "the standard is four"). It is not solved here. See `title-formula.md`.

## Studio template (requested)

```
{searched question}?

{one checked fact, with its condition. Clean Meatball gag. End on an open question?}
#topicone #topictwo #topicthree #meatballmyths
```

Rules inside Studio's version:

1. The caption **opens** with the searched question, ending in `?`. Put the same phrase on screen (`search_top`).
2. The next lines stay fact-true: hedge, condition, and the agency or paper named in the episode's own research. No new number. The gag does not add a danger, a dose, or a motive.
3. End the body with an open question (`?`), not a yes/no prompt, before the hashtags.
4. Then exactly four hashtags: three topic tags that the video actually answers, then `#meatballmyths`.
5. Still no `#fyp` and no `#learnontiktok`.
6. Clean wording (no swears).
7. Until Studio vs MASTER_ORDERS is resolved, lint a Studio caption only after renaming expectations; a `tt-` lint against the current tool will WARN or FAIL the 4-hashtag / brand-tag shape.

### Example in Studio's shape (facts from the cleared dog-turkey pack, not a new claim)

```
can dogs eat turkey?

The ASPCA says if you share, make it boneless and fully cooked. Meatball wrapped the bones and still had to use a bin Noodle could not get into, which is the FDA's move. What is the worst thing your dog ever got out of the trash?
#candogseatturkey #turkeybones #thanksgivingdogs #meatballmyths
```

That example is a shape demo. It does not replace the posted dog-turkey TikTok caption, and it has not had a new second-model check.

## MASTER_ORDERS shape (current written rule, for the decision)

```
{searched question}?

{one checked fact, with its condition. Clean Meatball gag. End on an open question?}
#topicone #topictwo #topicthree #topicfour #topicfive
```

Same body. Five topic hashtags. No `#meatballmyths` (no brand). No `#fyp`. No `#learnontiktok`.

### Same dog-turkey facts, recast to the current order

```
can dogs eat turkey?

The ASPCA says if you share, make it boneless and fully cooked. Meatball wrapped the bones and still had to use a bin Noodle could not get into, which is the FDA's move. What is the worst thing your dog ever got out of the trash?
#candogseatturkey #turkeybones #thanksgivingdogs #dogturkeysafety #bonelessturkey
```

## What this template does not do

- It does not invent captions for lick, knead, or chocolate. Those topics have no checked fact pack in the repo on this pass, so a caption would have no sourced second line.
- Bears vs Lions and cats/turkey captions live in their own files and follow Studio's hashtag shape, with this conflict restated there. Both are draft-pending.
- It does not change `postkit.py lint`. If Studio's rule wins, the lint check and MASTER_ORDERS need a matching update in a later, approved edit (not in this draft pass).
