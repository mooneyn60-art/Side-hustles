# TikTok blockers — @meatballmyths

**Documents only. Do not post, schedule, or change TikTok, Metricool, or Studio from this file.**

Times are America/New_York (ET, UTC-5). Written Mon 11/16/2026 morning for Jarvis, who asked what is blocking `@meatballmyths` posting. Standing rule: Moondog88 posts TikTok himself unless he says otherwise, and every post needs his explicit okay. Jarvis's note that he can now sign into TikTok on his computer and post directly does not replace that okay.

Account evidence in the files: `/workspace/audio-audit/tt_flat.json` is a public scrape of https://www.tiktok.com/@meatballmyths (title `meatballmyths`, uploader id `7634772285450994701`, channel id `MS4wLjABAAAAN37cCqH777QY_LhrS_nPXIp6a0oPzDnYSYgy5Nx7UNilukzLu31oOib7U2Z3VhEj`, 100 public videos in that pull). The account exists and has already posted. This sheet does not claim a login or Studio/TikTok setting was checked live today.

---

## Blockers

### 1. Metricool is linked to FurEver Faces, not @meatballmyths

**What's wrong.** Metricool brand **8135499** ("fureverfaces") has TikTok **@fureverfaces**. The same brand also links the Meatball YouTube channel `UCw98RQD81t_339LX5EJqcrg`. That is documented in `/workspace/tiktok-content/plan.md` and in the Nov 15 research/packaging notes. The week-1 Metricool drafts in `/workspace/tiktok-content/` are **shop** posts for FurEver Faces, not Meatball Myths. Packaging was told to ignore Metricool TikTok numbers for this reason.

**Why it blocks Meatball posting.** You cannot reliably schedule or read `@meatballmyths` analytics from the current Metricool brand. A Meatball post scheduled on that brand would go to the shop account, or would not be available at all. Best-time-to-post for TikTok from Metricool is therefore also the shop audience, not Meatball.

**Owner:** **Moondog88** (connect or create a Metricool brand whose TikTok is `@meatballmyths`, and keep it separate from FurEver Faces). Jarvis can prepare the ask and confirm the connection. Claude should not post or relink Metricool.

**Until that's done:** post `@meatballmyths` by hand (Moondog88, or Jarvis only after an explicit okay), not through the fureverfaces Metricool brand.

---

### 2. The requested @meatballmyths analytics CSV is still missing

**What's wrong.** TASKS.md (Nov 15, Packaging request) asked Claude for `channels/packaging/tiktok-per-video-90d.csv` plus a short `tiktok-per-video-90d.md` source note, with real TikTok Analytics columns: caption/title, post date (ET), views, avg watch time, completion, likes, shares, follows. The file is **not** in `/workspace/notebook/channels/packaging/` or `/workspace/packaging/`. Growth-plan and the channel-fix list both still list this as a data gap.

**Why it blocks.** It does not stop a single post from going up, but it does block any performance-based TikTok cadence, caption tests, or "what time works" claims. Do not substitute `fureverfaces` numbers or invent rows.

**Owner:** **Claude via TASKS.md** (export from TikTok Analytics for `@meatballmyths` only). **Moondog88** must provide Analytics access or a screenshot/export if Claude cannot log in. Jarvis tracks the request.

---

### 3. No TikTok cuts of the two approved rv2 Shorts (or of the new teasers)

**What's wrong.** The dual-cut order in TASKS.md (and PR #1) requires a **61–75 s** TikTok cut, over 60 s for Creator Rewards, with retention beats every 5–8 s. The approved files are YouTube-length only:

- `/workspace/meatball-animation-v2/samples/rv2_house-centipede_retention-v2.mp4` — 16.35 s
- `/workspace/meatball-animation-v2/samples/rv2_daddy-longlegs_retention-v2.mp4` — 17.59 s

`--cut tiktok` in `rv2.py` is a Claude task, not done. Spider, cockroach, dust-mite, and bed-bug teasers are script-only; they have no TikTok cut either. Older queued `tt-` / `tts-` minute files in `posted.csv` are a different format, not these rv2 episodes.

**Why it blocks.** Posting the 16–18 s YT files to TikTok would miss the Creator Rewards length rule the current spec set. They should not be posted to TikTok unless Moondog88 explicitly okays a short cut.

**Owner:** **Claude via TASKS.md** (render the TikTok cuts after PRs #1 / #2 are in the production pipeline). Jarvis reviews the cuts before anyone posts. Moondog88 okays each post.

---

### 4. Captions and hashtags are not TikTok-ready for the new posts

**What's wrong.**

- YouTube descriptions use 3 topic tags + `#meatballmyths` + `#shorts`.
- TikTok captions, per `/workspace/packaging/tiktok-caption-template.md` (locked 11/15), open with the searched question, end on an open question, then use **exactly five topic hashtags and no brand tag**. No `#meatballmyths`, no `#fyp`, no `#learnontiktok`. WMS captions must include the exact line `General info, not safety training.`
- The approved rv2 post copy (`rv2_post_copy.md`) is YouTube-shaped. The daddy-longlegs title and pin also use banned words (TRUE / FALSE / Believe) and `#spidermyths`. That has to be rewritten before a TikTok caption is pasted.
- No TikTok caption file exists for the rv2 pair, the spider teasers, or the other new bug teasers.
- Shop captions in `/workspace/tiktok-content/` and `/workspace/packaging/tiktok-shop-captions.md` are FurEver Faces / TikTok Shop and must not be used on `@meatballmyths`.

**Owner:** **Social Studio / Scriptwriter** drafts the captions from the template and the fact-checked lines. **Jarvis** puts the accepted captions next to the renders. **Moondog88** okays them before post. Claude should not invent captions or hashtags.

---

### 5. Audio is a technical hold on new renders, not a licensing hold

**What's wrong.** The Nov 15 audio audit (`/workspace/audio-audit/audio-audit-1115.csv`, `channels/production-spec-audio-v2.md`, PR #2) measured 26 videos, including TikToks.

- Beds come from procedural `tools/music.py`. The spec says **no licensing is needed** for those beds. No takedown or third-party cue-sheet problem is in the files.
- Several Meatball TikToks were **hotter than the new target**: around **-12 LUFS** (YouTube Shorts were about -15.4). One older TikTok (the CIA-sub cut, already off-lane) peaked at **+0.26 dBTP**. The v2 gate is about -14.5 to -13.5 LUFS and true peak no higher than -1.0 dBTP, with music ducked 6 dB or more under the voice.
- PR #2 (`jarvis/audio-spec-v2`) is **open and not merged**. New TikTok renders should not ship on the old mix.

**Owner:** **Claude via TASKS.md** (port the ducking / two-pass loudnorm / master from the spec and PR #2, then measure the first TikTok cuts with the stem script). Jarvis reviews. This is not a Moondog88 legal/licensing task unless someone later adds non-`music.py` audio.

---

### 6. Animation-v2 / audio-v2 are not in the production pipeline yet

**What's wrong.** PRs on `mooneyn60-art/Side-hustles` (read-only check today):

- PR #1 `jarvis/animation-v2` — open, mergeable_state **dirty** (does not merge cleanly onto `main`).
- PR #2 `jarvis/audio-spec-v2` — open, mergeable_state **clean**.

The house style is C v3. Queued TikToks in `posted.csv` were built on the older drawn-tt / tts pipeline. New Meatball TikToks are supposed to be fully animated dual-cuts. Voice and animation on the December long-forms and their teasers were waiting on this spec; Claude is now unblocked to do the heavy render, but the PRs still have to land.

**Owner:** **Claude via TASKS.md** (rebase / merge as Jarvis directs, port `rv2.py --cut tiktok`, panels path, mastering). **Jarvis** owns the spec and reviews renders. Moondog88 already picked the style; no new style decision is needed.

---

### 7. The existing TikTok queue is partly off-lane

**What's wrong.** `posted.csv` still has `@meatballmyths` items dated 11/16–11/25 that are pets or off-lane animal facts (dog guilty look, dog tail wag, dog stare, dog turkey, naked mole rat, electric eel, hummingbird, sea otter, woodpecker, platypus, wombat, Greenland shark, and a polar-fur cut whose pack-98 wording still needs a check). News TikToks from 11/13 (FAA, and others) already went up; the matching YouTube news Shorts are on the unlist list. Pets, news, and CIA are paused.

**Why it blocks.** Posting the leftover pet / off-lane queue would fight the lane Moondog88 set on Nov 15. Holding those slots without a 61–75 s on-lane replacement leaves TikTok empty on those days (see `posting-plan-1116-1205.md`). That is intended. Do not invent replacements.

**Owner:** **Moondog88** okays each hold (or an exception). **Jarvis** can unschedule or skip a queued item only after that okay, and not through the fureverfaces Metricool brand. Claude updates `held.csv` / the queue log after the fact, via TASKS.md.

---

### 8. Account and shop-channel confusion, and who may post

**What's wrong.**

- `@meatballmyths` and `@fureverfaces` are different accounts. Etsy / Social rules keep the shop and the Meatball channels strictly separate. TikTok Shop is parked and is an Etsy Studio surface, not a Meatball posting path.
- Moondog88's standing decision: he posts Pinterest, Facebook group, and TikTok content personally; agents prepare posts and never post them. That was given in Etsy Studio's chat for shop posts and is repeated as the Meatball standing rule.
- Jarvis now says he can sign into TikTok on his computer and post directly. That is useful for *capability*, but it is not a blanket okay to publish.
- This box has no authenticated `@meatballmyths` TikTok session to inspect unpublished drafts, privacy, AI-label defaults, or Creator Rewards enrollment. Those account-state details are **TBD** until someone with the login reads them.

**Owner:** **Moondog88** (who posts, AI-generated label, Creator Rewards enrollment, any login Jarvis may use). Jarvis reports account state after a login only if Moondog88 asked him to look. Do not scrape a session or reuse shop credentials.

---

## What is *not* a blocker

- The `@meatballmyths` account exists and already has a back catalog (100 public videos in the Nov 15 scrape).
- Music beds in the current pipeline are procedural (`music.py`); the audio spec does not require a license purchase.
- YouTube-side related links, titles, and unlists are a Studio job (`fix-batch-apply-sheet.md`), not a TikTok login job.
- FurEver Faces week-1 TikToks in Metricool are a shop track. They should stay off this account; they are not Meatball backlog.

---

## Suggested order of work

1. Moondog88 confirms who may press Post on `@meatballmyths` (himself, or Jarvis per post).
2. Moondog88 or Jarvis holds the pet / off-lane TikToks still sitting in the 11/16–11/25 queue.
3. Claude exports `tiktok-per-video-90d.csv` once Analytics access exists, and renders the first two TikTok dual-cuts (house centipede, daddy-longlegs) after the pipeline PRs are in.
4. Social Studio delivers TikTok captions for those two cuts (no banned words, five topic hashtags, WMS safety line if a WMS cut is posted).
5. Moondog88 (or Jarvis with an explicit okay) posts from the TikTok app, with the AI-generated label on, not via the fureverfaces Metricool brand.
6. In parallel, Moondog88 connects a Metricool brand to `@meatballmyths` so later scheduling and analytics are not blocked.
