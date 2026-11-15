# Bug Shorts packaging drafts (11/14–11/20)

Read-only drafts only. This file lives at `/workspace/packaging/bug-shorts-1114-1120.md`. Nothing in `mooneyn60-art/skills` was edited, committed, or pushed. Lint copies are under `/workspace/packaging/lint-specs/` (not in the clone).

Branch checked: `mooneyn60-art/skills`, `claude/youtube-monetization-strategy-m9vz6i`. The nine Shorts are the YouTube `drawn-house` bug cuts that `skills/oh-meatball/data/pending-swaps.csv` and `MASTER_ORDERS.md` ('Tags and everything') describe as having received the funny video and hashtag-order pass on 11/13, but still keeping 6 tags and the old first sentence.

Today in the report (America/New_York): Sunday, Nov 15, 2026, 1:50 PM ET.

## How to read this

- **Current metadata** is taken from each Short's `*-v6-yt.json` spec. `posted.csv` titles are shown when they differ (several JSON titles omit the series number; the carpet-beetle JSON title also differs in wording). YouTube tag lists are **not in these nine specs** (the 11/12-standard pet Shorts store an 8–12 item `tags` array; these do not). The '6 tags' still on the Metricool posts were not exportable from the repo.
- **New drafts** follow the 11/12 MASTER_ORDERS standard, using only facts already in that Short's spec (`beats`, `sources`, and the existing description). Search suggestions were pulled this turn with `postkit.py kw` (YouTube and web `suggestqueries`); raw rows are in `/workspace/packaging/kw/`.
- **Hashtag-count mismatch:** MASTER_ORDERS (and this task) say the first **three** hashtags are the topic's own, then `#meatballmyths`, then `#shorts` (five total). `postkit.py lint` is coded for **two** topic tags (four total), which is also what later pet Shorts use. Drafts follow the written MASTER_ORDERS rule (3+2). Lint therefore **warns** but still **passes** (exit 0). YouTube hashtag *feeds* ('the ones shown above the title') were not fetched; topic hashtags are the ones already in each spec, reordered.
- **TikTok captions** are drafted for every Short because the specs already carry `tiktok_caption`. Most of these nine do **not** have a matching TikTok row in `posted.csv` for 11/14–11/20; where a related TikTok exists, it is a different file/cut and is noted.
- **Second-model check is still required** before any of this wording is applied to a live or scheduled post, per MASTER_ORDERS.
- `postkit.py lint` was run on local copies of each draft spec (YouTube filename and a `tt-` copy so caption rules also run). MP4s were not in the sparse clone, so length was not linted.

## Per-Short summary

| Slot (ET) | Status | Topic | Old title (scheduled / posted.csv) | New title |
|---|---|---|---|---|
| Sat 2026-11-14 11:00 ET | slot passed (likely live) | House centipede vs cellar spider in the basement | House Centipede vs Spider in Your Basement: 2 Hunters 🕷️ (Things Living In Your House #59) | House Centipede vs Spider in Your Basement: 2 Hunters 🕷️ (Things Living In Your House #59) |
| Sat 2026-11-14 15:00 ET | slot passed (likely live) | Cellar spider silk-flick; recorded eating heavier house spiders | 8 Skinny Legs in Your Corner Tie Up Heavier Spiders 🕷️ (Things Living In Your House #60) | Cellar Spider in Your Corner: Recorded Eating Heavier Spiders 🕷️ (Things Living In Your House #60) |
| Sun 2026-11-15 19:00 ET | queued | Cellar spider diet: 102 leftovers in one English shed | Your Corner Spider Leaves Spider Leftovers: 102 in One Shed 🕷️ (Things Living In Your House #61) | Cellar Spider Leftovers: 102 in One Shed Were All Spiders 🕷️ (Things Living In Your House #61) |
| Mon 2026-11-16 16:00 ET | queued | Dust mites in the bed: eggs, lifespan, humidity | Female Dust Mites in Your Bed Lay About 50 Eggs 😬 (Things Living In Your House #56) | Dust Mites in Your Bed: Females Lay About 50 Eggs 😬 (Things Living In Your House #56) |
| Tue 2026-11-17 16:00 ET | queued | Carpet beetles at the window; 40 eggs on wool; long-lived larvae | Carpet Beetles at Your Window Can Lay 40 Eggs in Your Wool 🧶 (Things Living In Your House #58) | Carpet Beetles at Your Window Typically Lay 40 Eggs on Wool 🧶 (Things Living In Your House #58) |
| Wed 2026-11-18 19:00 ET (two hours after the Christmas-tree long-form at 17:00) | queued | Praying-mantis egg case on a Christmas tree, about 100 eggs | Your Christmas Tree Can Hide About 100 Mantis Eggs 🎄 (Things Living In Your House #62) | Bugs in Your Christmas Tree Can Hide About 100 Mantis Eggs 🎄 (Things Living In Your House #62) |
| Thu 2026-11-19 16:00 ET | queued | Pantry moth vs clothes moth: two rooms, larvae do the eating | Pantry Moth vs Clothes Moth: 2 Different Rooms in Your House 🦋 (Things Living In Your House #63) | Pantry Moth vs Clothes Moth: 2 Different Rooms in Your House 🦋 (Things Living In Your House #63) |
| Thu 2026-11-19 19:00 ET | queued | Cluster flies overwintering in walls and attics | Why Thousands of Flies Can Wake Up in Your House Walls 🪰 (Things Living In Your House #52) | Cluster Flies in Your House Walls Can Wake on Warm Days 🪰 (Things Living In Your House #52) |
| Fri 2026-11-20 16:00 ET | queued | Booklice (psocids) in kitchen cupboards; humidity | Tiny Bugs in Your Kitchen Cupboards Love 75% Humidity 📚 (Things Living In Your House #55) | Tiny Bugs in Kitchen Cupboards: Booklice Do Best at 75-90% RH 📚 (Things Living In Your House #55) |

---

## 1. House centipede vs cellar spider in the basement

- **Slot:** Sat 2026-11-14 11:00 ET
- **Status:** SLOT PASSED (yesterday). Not independently confirmed live on YouTube or Metricool in this read-only pass; treat as already posted unless a scheduler check says otherwise.
- **Video:** `skills/oh-meatball/episodes/drawn-house/yt-centipede-vs-spider-v6.mp4`
- **Spec:** `skills/oh-meatball/scripts/drawn-house/centipede-vs-spider-v6-yt.json`
- **Scheduler:** pending-swaps: done 11/13 10:47–10:50 ET, Metricool id 427123725; media swap only.
- **TikTok slot:** No TikTok row in posted.csv for this exact cut in the 11/14–11/20 window. A different cut, tt-house-centipede-5.mp4, is logged for Sun 11/15 20:15 ET.
- **New title length:** 91 UTF-16 units (max 100); first 40 characters: `House Centipede vs Spider in Your Baseme`

JSON title lacked the #59 series number already in posted.csv; draft matches posted.csv (search phrase already in the first 40 characters). Description now opens with the typed question. Added 10 tags from kw suggestions the Short actually answers. Hashtags reordered to 3 topic + #meatballmyths + #shorts last (they currently start with #shorts). TikTok caption adds the Meatball gag from line 2, a closing question, five topic hashtags, and drops the brand tag #meatballmyths. Related-video line added to the existing open pinned question.

### Old (current in the spec)

**Title in posted.csv (scheduled)**

```
House Centipede vs Spider in Your Basement: 2 Hunters 🕷️ (Things Living In Your House #59)
```

**Title in the JSON spec**

```
House Centipede vs Spider in Your Basement: 2 Hunters 🕷️ (Things Living In Your House)
```

**Description**

```
House centipede vs spider: in your basement, a house centipede chases prey down at night and a cellar spider waits in an irregular web, and both eat spiders, per Penn State Extension, UConn's CAES and Utah State Extension. #shorts #housecentipede #cellarspider #basement #meatballmyths
Sources: Connecticut Agricultural Experiment Station (House Centipede); Penn State Extension (House Centipedes; Longbodied cellar spider); Utah State University Extension (Cellar Spiders).
```

_YouTube tags: none in the spec._

**TikTok caption**

```
house centipede vs spider in your basement 🕷️ one chases prey down at night, the other waits in a messy web, and both eat spiders. What lives in yours? #housecentipede #cellarspider #basement #meatballmyths
```

**Pinned comment**

```
What's the weirdest thing you've seen living in your basement, and did you leave it alone?
```

### New draft

**Title**

```
House Centipede vs Spider in Your Basement: 2 Hunters 🕷️ (Things Living In Your House #59)
```

**Description**

```
House centipede vs spider? In your basement, a house centipede chases prey down at night and a cellar spider waits in an irregular web, and both eat spiders, per Penn State Extension, the Connecticut Agricultural Experiment Station, and Utah State Extension. Threatened, the cellar spider can rapidly vibrate in its web until it is hard to see. House centipedes have 15 pairs of legs and are nocturnal; in homes they turn up in basements, cellars, and first-floor bathrooms.

#housecentipede #cellarspider #basement #meatballmyths #shorts

Sources: Connecticut Agricultural Experiment Station (House Centipede); Penn State Extension (House Centipedes; Longbodied cellar spider); Utah State University Extension (Cellar Spiders).
```

**YouTube tags (8–12, each ≤30 characters, from this turn's `postkit.py kw` suggestions the Short answers)**

```
["house centipede vs spider", "house centipede and spiders", "house centipede eats spider", "house centipede", "house centipede in basement", "cellar spider", "cellar spider vs house spider", "cellar spider vibrating", "things living in your house", "Meatball Myths"]
```

**TikTok caption**

```
house centipede vs spider in your basement? one chases prey down at night, the other waits in an irregular web, and both eat spiders. Meatball just screams. What lives in yours? #housecentipede #cellarspider #basementbugs #housespiders #spiderfacts
```

**Pinned comment**

```
What's the weirdest thing you've seen living in your basement, and did you leave it alone? Full list in the Related video 👆
```

### Lint (`postkit.py lint` on local copies)

YouTube-named spec:

```
lint /workspace/packaging/lint-specs/centipede-vs-spider-v6-yt.json  (youtube)
  ok   spoken: 1 mild word(s), no strong ones
  ok   title 91 of 100 units
  WARN description has 5 hashtags (the standard is four: two topic, #meatballmyths, #shorts)
  ok   10 tags, 236 characters, longest 29
  => pass (0 fail, 1 warn)
```

TikTok-named copy (caption rules):

```
lint /workspace/packaging/lint-specs/tt-centipede-vs-spider-v6-yt.json  (tiktok)
  ok   spoken: 0 strong word(s), none shown in full in the captions
  ok   caption 248 of 2,200 units, 5 hashtags
  => pass (0 fail, 0 warn)
```

---

## 2. Cellar spider silk-flick; recorded eating heavier house spiders

- **Slot:** Sat 2026-11-14 15:00 ET
- **Status:** SLOT PASSED (yesterday). Not independently confirmed live on YouTube or Metricool in this read-only pass; treat as already posted unless a scheduler check says otherwise.
- **Video:** `skills/oh-meatball/episodes/drawn-house/yt-cellar-flick-v6.mp4`
- **Spec:** `skills/oh-meatball/scripts/drawn-house/cellar-flick-v6-yt.json`
- **Scheduler:** pending-swaps: done 11/13 10:47–10:50 ET, Metricool id 427123846; media swap only.
- **TikTok slot:** A related TikTok, tt-corner-spider.mp4, is logged for Sat 11/14 20:15 ET with a different title: 'Cellar Spider in Your Corner: What It Eats; and Is It Venomous?' — not this exact Short cut.
- **New title length:** 99 UTF-16 units (max 100); first 40 characters: `Cellar Spider in Your Corner: Recorded E`

Old title led with '8 Skinny Legs', so 'cellar spider' / 'spider in the corner' were not in the first 40 characters. New title leads with 'Cellar Spider in Your Corner' and keeps the hedge 'recorded' (the 102-unit 'Giant House Spiders' wording ran over the 100-unit cap, so 'Heavier' is used; that word is in the BAS source). Pinned comment was yes/no ('Would you let it live'); rewritten as an open question plus the Related-video line (this is a cellar-spider long-form companion). TikTok gag cleaned of 'damn' from the script line.

### Old (current in the spec)

**Title in posted.csv (scheduled)**

```
8 Skinny Legs in Your Corner Tie Up Heavier Spiders 🕷️ (Things Living In Your House #60)
```

**Title in the JSON spec**

```
8 Skinny Legs in Your Corner Tie Up Heavier Spiders 🕷️ (Things Living In Your House)
```

**Description**

```
Cellar spider silk flick: the skinny spider in your corner keeps its distance, flicks silk over prey with its back legs, then bites once the prey is tied up, and British experts recorded it eating giant house spiders. #shorts #cellarspider #spiderinhouse #thingslivinginyourhouse #meatballmyths
Sources: British Arachnological Society (Daddy-long-legs spider factsheet 3); Japyassu & Macagnan 2004, Revista de Etologia.
```

_YouTube tags: none in the spec._

**TikTok caption**

```
cellar spider in your corner 🕷️ it keeps its distance, flicks silk over prey with its back legs, then bites once it's tied up, and it's been recorded eating giant house spiders. Keep it or sweep it? #cellarspider #spiderinhouse #thingslivinginyourhouse #meatballmyths
```

**Pinned comment**

```
Would you let the skinny spider in your corner live now that you know it ties up heavier spiders? Full story: Don't Kill the Spider in Your Corner, on the channel.
```

### New draft

**Title**

```
Cellar Spider in Your Corner: Recorded Eating Heavier Spiders 🕷️ (Things Living In Your House #60)
```

**Description**

```
What do cellar spiders eat? The skinny spider in your corner keeps its distance, flicks silk over prey with its back legs, then bites once the prey is tied up, and British experts recorded it eating much heavier large house spiders.

#cellarspider #daddylonglegs #housespiders #meatballmyths #shorts

Sources: British Arachnological Society (Daddy-long-legs spider factsheet 3); Japyassu & Macagnan 2004, Revista de Etologia.
```

**YouTube tags (8–12, each ≤30 characters, from this turn's `postkit.py kw` suggestions the Short answers)**

```
["what do cellar spiders eat", "cellar spider", "cellar spider vs house spider", "daddy long legs in house", "daddy long legs spider", "spider in the corner", "daddy long legs in my house", "cellar spider web", "things living in your house", "Meatball Myths"]
```

**TikTok caption**

```
what do cellar spiders eat? the skinny spider in your corner keeps its distance, flicks silk over prey with its back legs, then bites once the prey is tied up, and it has been recorded eating heavier large house spiders. Meatball can't even wrap a gift. What has yours caught? #cellarspider #daddylonglegs #housespiders #spiderinhouse #spiderfacts
```

**Pinned comment**

```
What's the scariest thing you've watched a corner spider catch? Full list in the Related video 👆
```

### Lint (`postkit.py lint` on local copies)

YouTube-named spec:

```
lint /workspace/packaging/lint-specs/cellar-flick-v6-yt.json  (youtube)
  ok   spoken: 1 mild word(s), no strong ones
  ok   title 99 of 100 units
  WARN description has 5 hashtags (the standard is four: two topic, #meatballmyths, #shorts)
  ok   10 tags, 228 characters, longest 29
  => pass (0 fail, 1 warn)
```

TikTok-named copy (caption rules):

```
lint /workspace/packaging/lint-specs/tt-cellar-flick-v6-yt.json  (tiktok)
  ok   spoken: 0 strong word(s), none shown in full in the captions
  ok   caption 347 of 2,200 units, 5 hashtags
  => pass (0 fail, 0 warn)
```

---

## 3. Cellar spider diet: 102 leftovers in one English shed

- **Slot:** Sun 2026-11-15 19:00 ET
- **Status:** STILL QUEUED as of 1:50 PM ET, Nov 15, 2026 (slot is later today). First still-queued Short in the set — soonest for the metadata pass.
- **Video:** `skills/oh-meatball/episodes/drawn-house/yt-cellar-102-v6.mp4`
- **Spec:** `skills/oh-meatball/scripts/drawn-house/cellar-102-v6-yt.json`
- **Scheduler:** pending-swaps: done 11/13 10:47–10:50 ET, Metricool id 427123967; media swap only.
- **TikTok slot:** No TikTok row in posted.csv for this cut in the 11/14–11/20 window.
- **New title length:** 95 UTF-16 units (max 100); first 40 characters: `Cellar Spider Leftovers: 102 in One Shed`

Old title led with 'Your Corner Spider Leaves Spider Leftovers' (no 'cellar spider' or diet phrase in the first 40 characters). The 102 count stays hedged as one shed, one summer. Pinned comment was yes/no; rewritten open, plus Related-video line.

### Old (current in the spec)

**Title in posted.csv (scheduled)**

```
Your Corner Spider Leaves Spider Leftovers: 102 in One Shed 🕷️ (Things Living In Your House #61)
```

**Title in the JSON spec**

```
Your Corner Spider Leaves Spider Leftovers: 102 in One Shed 🕷️ (Things Living In Your House)
```

**Description**

```
Cellar spider diet: in one English garden shed, 102 prey remains were cleared from cellar spider webs over a summer, 63 common house spiders, 6 other cellar spiders and the rest broken spider bits, so every leftover was a spider. #shorts #cellarspider #spiderinhouse #thingslivinginyourhouse #meatballmyths
Sources: British Arachnological Society (Daddy-long-legs spider factsheet 3).
```

_YouTube tags: none in the spec._

**TikTok caption**

```
cellar spider diet 🕷️ in one English garden shed, 102 leftovers came out of cellar spider webs over a summer: 63 common house spiders, 6 other cellar spiders, the rest broken spider bits. Every one a spider. #cellarspider #spiderinhouse #thingslivinginyourhouse #meatballmyths
```

**Pinned comment**

```
If you cleaned the webs in your corner, would you expect every leftover to be a spider? Full story: Don't Kill the Spider in Your Corner, on the channel.
```

### New draft

**Title**

```
Cellar Spider Leftovers: 102 in One Shed Were All Spiders 🕷️ (Things Living In Your House #61)
```

**Description**

```
What do cellar spiders eat? In one English garden shed, 102 prey remains were cleared from cellar spider webs over a summer: 63 common house spiders, 6 other cellar spiders, and the rest broken spider bits, so every leftover was a spider, per the British Arachnological Society.

#cellarspider #daddylonglegs #housespiders #meatballmyths #shorts

Sources: British Arachnological Society (Daddy-long-legs spider factsheet 3).
```

**YouTube tags (8–12, each ≤30 characters, from this turn's `postkit.py kw` suggestions the Short answers)**

```
["what do cellar spiders eat", "cellar spider", "cellar spider vs house spider", "daddy long legs in house", "daddy long legs spider", "spider in the corner", "daddy long legs in my house", "cellar spider web", "things living in your house", "Meatball Myths"]
```

**TikTok caption**

```
what do cellar spiders eat? in one English garden shed, 102 leftovers came out of cellar spider webs over a summer: 63 common house spiders, 6 other cellar spiders, the rest broken spider bits. Every one a spider. Meatball's leftovers? Cold pizza. What would you find in yours? #cellarspider #daddylonglegs #housespiders #spiderinhouse #spiderfacts
```

**Pinned comment**

```
If you cleaned the webs in your corner, what leftovers would you expect to find? Full list in the Related video 👆
```

### Lint (`postkit.py lint` on local copies)

YouTube-named spec:

```
lint /workspace/packaging/lint-specs/cellar-102-v6-yt.json  (youtube)
  ok   spoken: 1 mild word(s), no strong ones
  ok   title 95 of 100 units
  WARN description has 5 hashtags (the standard is four: two topic, #meatballmyths, #shorts)
  ok   10 tags, 228 characters, longest 29
  => pass (0 fail, 1 warn)
```

TikTok-named copy (caption rules):

```
lint /workspace/packaging/lint-specs/tt-cellar-102-v6-yt.json  (tiktok)
  ok   spoken: 0 strong word(s), none shown in full in the captions
  ok   caption 348 of 2,200 units, 5 hashtags
  => pass (0 fail, 0 warn)
```

---

## 4. Dust mites in the bed: eggs, lifespan, humidity

- **Slot:** Mon 2026-11-16 16:00 ET
- **Status:** STILL QUEUED
- **Video:** `skills/oh-meatball/episodes/drawn-house/yt-dust-mites-v6.mp4`
- **Spec:** `skills/oh-meatball/scripts/drawn-house/dust-mites-v6-yt.json`
- **Scheduler:** pending-swaps: done 11/13 10:47–10:50 ET, Metricool id 427124618; funny media swapped; hashtags put in standard order in Metricool; 'no other wording changed'. Repo JSON description still starts with #shorts, so the Metricool copy may differ from the spec.
- **TikTok slot:** No TikTok row in posted.csv for this cut in the 11/14–11/20 window.
- **New title length:** 86 UTF-16 units (max 100); first 40 characters: `Dust Mites in Your Bed: Females Lay Abou`

Title keeps the 'about 50' hedge and moves 'Dust Mites in Your Bed' to the front (yt/web suggestions). Opening question is the web suggestion 'do dust mites live in my bed'. Tags skip 'how to get rid / control' phrases — the Short states a humidity condition, it is not a treatment guide. TikTok gag cleaned of 'damn' from the script.

### Old (current in the spec)

**Title in posted.csv (scheduled)**

```
Female Dust Mites in Your Bed Lay About 50 Eggs 😬 (Things Living In Your House #56)
```

**Title in the JSON spec**

```
Female Dust Mites in Your Bed Lay About 50 Eggs 😬 (Things Living In Your House)
```

**Description**

```
Dust mites in your bed: a female lays about 50 eggs, under ideal conditions they grow from egg to adult in about a month, adults live 1-2 months, and humidity below 50 percent makes survival difficult, per University of Kentucky Entomology. #shorts #dustmites #bedroom #bugsinyourhouse #meatballmyths
Sources: University of Kentucky Entomology (House Dust Mites, ENTFACT-646).
```

_YouTube tags: none in the spec._

**TikTok caption**

```
dust mites in your bed 😬 a female lays about 50 eggs, they can be adults in a month, and dry air makes life hard for them. What's your bedtime habit? #dustmites #bedroom #bugsinyourhouse #meatballmyths
```

**Pinned comment**

```
What's one thing in your bedroom routine you'd change if you knew how many dust mites could be in your bed?
```

### New draft

**Title**

```
Dust Mites in Your Bed: Females Lay About 50 Eggs 😬 (Things Living In Your House #56)
```

**Description**

```
Do dust mites live in your bed? A female lays about 50 eggs; under ideal conditions they grow from egg to adult in about a month; adults live about 1-2 months; and humidity below 50 percent makes survival difficult, per University of Kentucky Entomology. They tend to be most numerous in beds, overstuffed sofas and chairs, and adjacent carpeted areas.

#dustmites #bedroom #bugsinyourhouse #meatballmyths #shorts

Sources: University of Kentucky Entomology (House Dust Mites, ENTFACT-646).
```

**YouTube tags (8–12, each ≤30 characters, from this turn's `postkit.py kw` suggestions the Short answers)**

```
["dust mites in bed", "dust mites in your bed", "do dust mites live in my bed", "dust mites in mattress", "dust mites in bedroom", "dust mites in bed sheets", "dust mites on bedsheet", "dust mites", "things living in your house", "Meatball Myths"]
```

**TikTok caption**

```
do dust mites live in your bed? a female lays about 50 eggs, and under ideal conditions they can be adults in about a month; humidity below 50 percent makes survival difficult. Meatball hasn't washed his sheets since March. What's your bedtime habit? #dustmites #bedroom #housebugs #mattress #mitefacts
```

**Pinned comment**

```
What's one thing in your bedroom routine you'd change if you knew how many dust mites could be in your bed?
```

### Lint (`postkit.py lint` on local copies)

YouTube-named spec:

```
lint /workspace/packaging/lint-specs/dust-mites-v6-yt.json  (youtube)
  ok   spoken: 1 mild word(s), no strong ones
  ok   title 86 of 100 units
  WARN description has 5 hashtags (the standard is four: two topic, #meatballmyths, #shorts)
  ok   10 tags, 216 characters, longest 28
  => pass (0 fail, 1 warn)
```

TikTok-named copy (caption rules):

```
lint /workspace/packaging/lint-specs/tt-dust-mites-v6-yt.json  (tiktok)
  ok   spoken: 0 strong word(s), none shown in full in the captions
  ok   caption 302 of 2,200 units, 5 hashtags
  => pass (0 fail, 0 warn)
```

---

## 5. Carpet beetles at the window; 40 eggs on wool; long-lived larvae

- **Slot:** Tue 2026-11-17 16:00 ET
- **Status:** STILL QUEUED
- **Video:** `skills/oh-meatball/episodes/drawn-house/yt-carpet-beetle-window-v6.mp4`
- **Spec:** `skills/oh-meatball/scripts/drawn-house/carpet-beetle-window-v6-yt.json`
- **Scheduler:** pending-swaps: done 11/13 10:47–10:50 ET, Metricool id 427124763; funny media swapped; hashtags reordered in Metricool; 'no other wording changed'. Repo JSON title differs from posted.csv (see old vs new).
- **TikTok slot:** No TikTok row in posted.csv for this cut in the 11/14–11/20 window.
- **New title length:** 96 UTF-16 units (max 100); first 40 characters: `Carpet Beetles at Your Window Typically `

Scheduled/posted.csv title already names carpet beetles (better than the JSON title 'Small Brown Bugs in Your House…', which does not name the creature in the way the lady-beetle flop warned against). Draft keeps that lead and swaps 'Can Lay 40' for 'Typically Lay 40', the hedge in the spec/UC IPM wording. First 40 characters: 'Carpet Beetles at Your Window Typically '. Opening question uses the web/yt family 'small brown bugs in my house'. Tags skip 'how to get rid' and 'vs bed bugs'.

### Old (current in the spec)

**Title in posted.csv (scheduled)**

```
Carpet Beetles at Your Window Can Lay 40 Eggs in Your Wool 🧶 (Things Living In Your House #58)
```

**Title in the JSON spec**

```
Small Brown Bugs in Your House Can Lay 40 Eggs in Your Wool 🧶 (Things Living In Your House)
```

**Description**

```
Small brown bugs in my house: carpet beetle adults sit at your windows, and a varied carpet beetle typically lays 40 eggs on wool, fur and carpet; the larvae can live up to 630 days and leave shed skins, per UC IPM. #shorts #carpetbeetle #smallbrownbugs #bugsinyourhouse #meatballmyths
Sources: UC Statewide IPM Program, Pest Notes: Carpet Beetles (7436).
```

_YouTube tags: none in the spec._

**TikTok caption**

```
small brown bugs in your house 🧶 the one sitting at your window can lay 40 eggs on wool, fur and carpet, and the babies leave shed skins. What did you find first? #carpetbeetle #smallbrownbugs #bugsinyourhouse #meatballmyths
```

**Pinned comment**

```
What was the first sign of carpet beetles you found in your house: a bug at the window, or a shed skin somewhere?
```

### New draft

**Title**

```
Carpet Beetles at Your Window Typically Lay 40 Eggs on Wool 🧶 (Things Living In Your House #58)
```

**Description**

```
What are the small brown bugs in my house? Carpet beetle adults sit at your windows, and a varied carpet beetle typically lays 40 eggs on wool, fur, and carpet; the larvae can live up to 630 days and leave shed skins, per UC IPM. Adults gather at windows, drawn to light.

#carpetbeetle #smallbrownbugs #bugsinyourhouse #meatballmyths #shorts

Sources: UC Statewide IPM Program, Pest Notes: Carpet Beetles (7436).
```

**YouTube tags (8–12, each ≤30 characters, from this turn's `postkit.py kw` suggestions the Short answers)**

```
["carpet beetles", "carpet beetles in house", "small brown bugs in my house", "tiny brown bugs in house", "carpet beetle eggs", "carpet beetle larvae", "carpet beetle larvae in house", "varied carpet beetle larvae", "things living in your house", "Meatball Myths"]
```

**TikTok caption**

```
what are the small brown bugs in my house? the carpet beetle sitting at your window typically lays 40 eggs on wool, fur, and carpet, and the larvae can live up to 630 days and leave shed skins. Meatball's whole closet is wool. What did you find first? #carpetbeetle #smallbrownbugs #housebugs #woolpests #beetlefacts
```

**Pinned comment**

```
What was the first sign of carpet beetles you found in your house: a bug at the window, or a shed skin somewhere?
```

### Lint (`postkit.py lint` on local copies)

YouTube-named spec:

```
lint /workspace/packaging/lint-specs/carpet-beetle-window-v6-yt.json  (youtube)
  ok   spoken: 1 mild word(s), no strong ones
  ok   title 96 of 100 units
  WARN description has 5 hashtags (the standard is four: two topic, #meatballmyths, #shorts)
  ok   10 tags, 233 characters, longest 29
  => pass (0 fail, 1 warn)
```

TikTok-named copy (caption rules):

```
lint /workspace/packaging/lint-specs/tt-carpet-beetle-window-v6-yt.json  (tiktok)
  ok   spoken: 0 strong word(s), none shown in full in the captions
  ok   caption 316 of 2,200 units, 5 hashtags
  => pass (0 fail, 0 warn)
```

---

## 6. Praying-mantis egg case on a Christmas tree, about 100 eggs

- **Slot:** Wed 2026-11-18 19:00 ET (two hours after the Christmas-tree long-form at 17:00)
- **Status:** STILL QUEUED
- **Video:** `skills/oh-meatball/episodes/drawn-house/yt-christmas-tree-bugs-v6.mp4`
- **Spec:** `skills/oh-meatball/scripts/drawn-house/christmas-tree-bugs-v6-yt.json`
- **Scheduler:** pending-swaps: done 11/13 10:47–10:50 ET, Metricool id 427124926; funny media swapped; hashtags reordered in Metricool; 'no other wording changed'. A tiny companion file exists: episodes/drawn-house/yt-christmas-tree-bugs-v6.mp4.post.json (85 bytes).
- **TikTok slot:** A related TikTok, tt-christmas-tree-check.mp4, is logged for Wed 11/18 20:15 ET ('Bugs in Your Christmas Tree: Mantis Egg Case and Fake Ticks') — a different cut (the long-form check), not this 16–20 s Short.
- **New title length:** 95 UTF-16 units (max 100); first 40 characters: `Bugs in Your Christmas Tree Can Hide Abo`

Old title led with 'Your Christmas Tree Can Hide…'; new title leads with 'Bugs in Your Christmas Tree' (web suggestions; YouTube suggest returned no list for 'bugs in christmas tree' / 'bugs in my christmas tree'). 'About 100' hedge kept (Missouri per foamy mass; Illinois's 200–400 per female is noted only in Sources, not used as the Short's number). Description already opened with a question; tightened to a typed-style question and added the clip-and-tuck step already in the script. Related-video line added (companion to the 17:00 long-form). Current description hashtags had #bugsinhouse #bugsinyourhouse and no #meatballmyths.

### Old (current in the spec)

**Title**

```
Your Christmas Tree Can Hide About 100 Mantis Eggs 🎄 (Things Living In Your House #62)
```

**Description**

```
Bugs in Christmas trees? A praying-mantis egg case on a tree can hold about 100 eggs, and indoor warmth can hatch them. Check the twigs for a foamy case before you bring it in.

#shorts #christmastree #prayingmantis #bugsinhouse #bugsinyourhouse

Sources: University of Missouri Extension; Penn State Extension.
```

_YouTube tags: none in the spec._

**TikTok caption**

```
bugs in christmas trees 🎄 a praying-mantis egg case can hold about 100 eggs, and if it rides your tree indoors the warmth can hatch dozens of babies. Check the twigs for a foamy case before you bring it in. Ever found one? #christmastree #prayingmantis #bugsinhouse #meatballmyths
```

**Pinned comment**

```
What's the strangest thing that ever crawled out of your Christmas tree?
```

### New draft

**Title**

```
Bugs in Your Christmas Tree Can Hide About 100 Mantis Eggs 🎄 (Things Living In Your House #62)
```

**Description**

```
What are the bugs in my Christmas tree? A praying-mantis egg case on a tree can hold about 100 eggs, and indoor warmth can hatch them; with no food, the babies can eat each other. Check the twigs for a foamy case before you bring the tree in; extension advice is to clip the twig and put it in an evergreen outside.

#christmastree #prayingmantis #bugsinhouse #meatballmyths #shorts

Sources: University of Missouri Extension; Penn State Extension, Insects on Real Christmas Trees; University of Illinois Extension, Christmas tree hitchhikers (clip-and-tuck step). The Short uses Missouri's 'about 100' eggs per foamy mass, not Illinois's 200 to 400 eggs per female.
```

**YouTube tags (8–12, each ≤30 characters, from this turn's `postkit.py kw` suggestions the Short answers)**

```
["bugs in my christmas tree", "bugs in the christmas tree", "christmas tree bugs", "christmas tree insects", "christmas tree bugs in house", "praying mantis eggs", "praying mantis egg case", "praying mantis eggs hatching", "mantis egg case", "mantis egg case hatching", "things living in your house", "Meatball Myths"]
```

**TikTok caption**

```
what are the bugs in my christmas tree? a praying-mantis egg case can hold about 100 eggs, and if it rides your tree indoors the warmth can hatch them. Meatball screamed. Ever found a foamy case on the twigs? #christmastree #prayingmantis #mantiseggs #treebugs #housebugs
```

**Pinned comment**

```
What's the strangest thing that ever crawled out of your Christmas tree? Full list in the Related video 👆
```

### Lint (`postkit.py lint` on local copies)

YouTube-named spec:

```
lint /workspace/packaging/lint-specs/christmas-tree-bugs-v6-yt.json  (youtube)
  ok   spoken: 1 mild word(s), no strong ones
  ok   title 95 of 100 units
  WARN description has 5 hashtags (the standard is four: two topic, #meatballmyths, #shorts)
  ok   12 tags, 281 characters, longest 28
  => pass (0 fail, 1 warn)
```

TikTok-named copy (caption rules):

```
lint /workspace/packaging/lint-specs/tt-christmas-tree-bugs-v6-yt.json  (tiktok)
  ok   spoken: 0 strong word(s), none shown in full in the captions
  ok   caption 271 of 2,200 units, 5 hashtags
  => pass (0 fail, 0 warn)
```

---

## 7. Pantry moth vs clothes moth: two rooms, larvae do the eating

- **Slot:** Thu 2026-11-19 16:00 ET
- **Status:** STILL QUEUED
- **Video:** `skills/oh-meatball/episodes/drawn-house/yt-pantry-vs-clothes-moth-v6.mp4`
- **Spec:** `skills/oh-meatball/scripts/drawn-house/pantry-vs-clothes-moth-v6-yt.json`
- **Scheduler:** pending-swaps: done 11/13 10:47–10:50 ET, Metricool id 427125342; funny media swapped; hashtags reordered in Metricool; 'no other wording changed'.
- **TikTok slot:** No TikTok row in posted.csv for this cut in the 11/14–11/20 window.
- **New title length:** 97 UTF-16 units (max 100); first 40 characters: `Pantry Moth vs Clothes Moth: 2 Different`

JSON title lacked #63; draft matches posted.csv (search phrase already in the first 40 characters). Description now opens with the vs question people type. Current hashtags started with #shorts and had no #meatballmyths. Tags skip 'how to get rid / trap / treatment'. TikTok gag is the on-screen card line 'Meatball blamed the dryer.'

### Old (current in the spec)

**Title in posted.csv (scheduled)**

```
Pantry Moth vs Clothes Moth: 2 Different Rooms in Your House 🦋 (Things Living In Your House #63)
```

**Title in the JSON spec**

```
Pantry Moth vs Clothes Moth: 2 Different Rooms in Your House 🦋 (Things Living In Your House)
```

**Description**

```
Pantry moth vs clothes moth: two different moths in two different rooms. Clothes moths lay about 40 to 50 eggs in dark closets, pantry moths usually arrive in food packages, and in both it's the larvae that do the eating.

#shorts #pantrymoth #clothesmoth #mothsinhouse #bugsinyourhouse

Sources: University of Kentucky Entomology (ENTFACT-609); UC IPM Pest Notes (Clothes Moths, Pantry Pests).
```

_YouTube tags: none in the spec._

**TikTok caption**

```
pantry moth vs clothes moth 🦋 two different moths in two different rooms: clothes moths lay about 40 to 50 eggs in your dark closet, pantry moths ride in on food packages, and in both it's the larvae that eat. Which have you found? #pantrymoth #clothesmoth #mothsinhouse #meatballmyths
```

**Pinned comment**

```
Which moths did you find first, the ones in your closet or the ones in your kitchen? What gave them away?
```

### New draft

**Title**

```
Pantry Moth vs Clothes Moth: 2 Different Rooms in Your House 🦋 (Things Living In Your House #63)
```

**Description**

```
Pantry moth vs clothes moth? They are two different moths in two different rooms. Clothes moths lay about 40 to 50 eggs in dark closets, on wool, fur, silk, and other animal fibers; pantry moths usually arrive in food packages; and in both, it is the larvae that do the eating, not the adults, per University of Kentucky Entomology and UC IPM. Similar-looking moths in kitchens and other well-lighted rooms may be grain moths from stored food.

#pantrymoth #clothesmoth #mothsinhouse #meatballmyths #shorts

Sources: University of Kentucky Entomology (ENTFACT-609); UC IPM Pest Notes (Clothes Moths, Pantry Pests).
```

**YouTube tags (8–12, each ≤30 characters, from this turn's `postkit.py kw` suggestions the Short answers)**

```
["pantry moth vs clothes moth", "clothes moth", "clothes moth larvae", "clothes moth eggs look like", "clothes moth life cycle", "pantry moths", "pantry moth larvae", "pantry moth life cycle", "pantry moth eggs", "things living in your house", "Meatball Myths"]
```

**TikTok caption**

```
pantry moth vs clothes moth? two different moths in two different rooms: clothes moths lay about 40 to 50 eggs in a dark closet, pantry moths usually ride in on food packages, and in both it is the larvae that eat. Meatball blamed the dryer. Which have you found? #pantrymoth #clothesmoth #mothsinhouse #closetpests #pantrybugs
```

**Pinned comment**

```
Which moths did you find first, the ones in your closet or the ones in your kitchen? What gave them away?
```

### Lint (`postkit.py lint` on local copies)

YouTube-named spec:

```
lint /workspace/packaging/lint-specs/pantry-vs-clothes-moth-v6-yt.json  (youtube)
  ok   spoken: 1 mild word(s), no strong ones
  ok   title 97 of 100 units
  WARN description has 5 hashtags (the standard is four: two topic, #meatballmyths, #shorts)
  ok   11 tags, 227 characters, longest 27
  => pass (0 fail, 1 warn)
```

TikTok-named copy (caption rules):

```
lint /workspace/packaging/lint-specs/tt-pantry-vs-clothes-moth-v6-yt.json  (tiktok)
  ok   spoken: 0 strong word(s), none shown in full in the captions
  ok   caption 327 of 2,200 units, 5 hashtags
  => pass (0 fail, 0 warn)
```

---

## 8. Cluster flies overwintering in walls and attics

- **Slot:** Thu 2026-11-19 19:00 ET
- **Status:** STILL QUEUED
- **Video:** `skills/oh-meatball/episodes/drawn-house/yt-cluster-flies-v6.mp4`
- **Spec:** `skills/oh-meatball/scripts/drawn-house/cluster-flies-v6-yt.json`
- **Scheduler:** pending-swaps: done 11/13 10:47–10:50 ET, Metricool id 427125458; funny media swapped; hashtags reordered in Metricool; 'no other wording changed'.
- **TikTok slot:** No TikTok row in posted.csv for this cut in the 11/14–11/20 window.
- **New title length:** 92 UTF-16 units (max 100); first 40 characters: `Cluster Flies in Your House Walls Can Wa`

Old title led with 'Why Thousands of Flies…' (no 'cluster flies' in the first 40 characters; 'thousands' in the script is a 'can' line, and Penn State's 'thousands' is about what a dust treatment may kill). New title names cluster flies, keeps 'can', and uses the warm-day fact. Description already opened with the exact typed question; fact sentences tightened to 'can't reproduce indoors' (CSU) and 'gather in large numbers' (Penn State) rather than restating 'thousands' as a count. Tags skip 'how to get rid / home remedy / kill / treatment'. Current hashtags had no #meatballmyths.

### Old (current in the spec)

**Title in posted.csv (scheduled)**

```
Why Thousands of Flies Can Wake Up in Your House Walls 🪰 (Things Living In Your House #52)
```

**Title in the JSON spec**

```
Why Thousands of Flies Can Wake Up in Your House Walls 🪰 (Things Living In Your House)
```

**Description**

```
Why are there so many flies in my house? Cluster flies spend the winter in attics and wall voids, then crawl out on warm days. They can't breed indoors.

#shorts #clusterflies #flysinhouse #winterpests #bugsinyourhouse

Sources: Penn State Extension (Cluster Flies); Colorado State University Extension (Cluster Flies and Other Winter Flies).
```

_YouTube tags: none in the spec._

**TikTok caption**

```
why are there so many flies in my house 🪰 cluster flies spend winter in your attic and wall voids, then crawl out on warm days. They can't breed indoors: their babies grow inside earthworms. Ever had a winter fly invasion? #clusterflies #flysinhouse #winterpests #meatballmyths
```

**Pinned comment**

```
What's the strangest place you've ever found a pile of winter flies?
```

### New draft

**Title**

```
Cluster Flies in Your House Walls Can Wake on Warm Days 🪰 (Things Living In Your House #52)
```

**Description**

```
Why are there so many flies in my house? Cluster flies spend the winter in attics and wall voids, then crawl out on warm days. They can't reproduce indoors; they develop by feeding on earthworms. On warm winter days they can gather in large numbers at windows and fly sluggishly, per Penn State Extension and Colorado State University Extension.

#clusterflies #flysinhouse #winterpests #meatballmyths #shorts

Sources: Penn State Extension (Cluster Flies); Colorado State University Extension (Cluster Flies and Other Winter Flies).
```

**YouTube tags (8–12, each ≤30 characters, from this turn's `postkit.py kw` suggestions the Short answers)**

```
["so many flies in my house", "cluster flies", "cluster flies in house", "cluster flies in attic", "cluster flies vs house flies", "cluster flies in my house", "cluster flies in basement", "flies in my house walls", "things living in your house", "Meatball Myths"]
```

**TikTok caption**

```
why are there so many flies in my house? cluster flies spend winter in your attic and wall voids, then crawl out on warm days. They can't reproduce indoors: they develop by feeding on earthworms. Meatball needs three alarms. Ever had a winter fly invasion? #clusterflies #flysinhouse #winterpests #atticflies #houseflies
```

**Pinned comment**

```
What's the strangest place you've ever found a pile of winter flies?
```

### Lint (`postkit.py lint` on local copies)

YouTube-named spec:

```
lint /workspace/packaging/lint-specs/cluster-flies-v6-yt.json  (youtube)
  ok   spoken: 0 mild word(s), no strong ones
  ok   title 92 of 100 units
  WARN description has 5 hashtags (the standard is four: two topic, #meatballmyths, #shorts)
  ok   10 tags, 233 characters, longest 28
  => pass (0 fail, 1 warn)
```

TikTok-named copy (caption rules):

```
lint /workspace/packaging/lint-specs/tt-cluster-flies-v6-yt.json  (tiktok)
  ok   spoken: 0 strong word(s), none shown in full in the captions
  ok   caption 320 of 2,200 units, 5 hashtags
  => pass (0 fail, 0 warn)
```

---

## 9. Booklice (psocids) in kitchen cupboards; humidity

- **Slot:** Fri 2026-11-20 16:00 ET
- **Status:** STILL QUEUED
- **Video:** `skills/oh-meatball/episodes/drawn-house/yt-booklice-cupboard-v6.mp4`
- **Spec:** `skills/oh-meatball/scripts/drawn-house/booklice-cupboard-v6-yt.json`
- **Scheduler:** pending-swaps: done 11/13 10:47–10:50 ET, Metricool id 427125573; funny media swapped; hashtags reordered in Metricool; 'no other wording changed'.
- **TikTok slot:** No TikTok row in posted.csv for this cut in the 11/14–11/20 window.
- **New title length:** 98 UTF-16 units (max 100); first 40 characters: `Tiny Bugs in Kitchen Cupboards: Booklice`

Old title had the search phrase but said 'Love 75% Humidity' (75% is only the low end of the 75-90% range) and did not name booklice in the first 40 characters. New title is 'Tiny Bugs in Kitchen Cupboards: Booklice Do Best at 75-90% RH' (98 UTF-16 units; 'RH' shortens 'humidity' to fit the range and 'do best at'). Opening question follows the typed phrase. Tags skip 'how to get rid'. Current TikTok caption said 'about a millimeter' and 'like humid air' and had only four hashtags, including no fifth topic tag.

### Old (current in the spec)

**Title in posted.csv (scheduled)**

```
Tiny Bugs in Your Kitchen Cupboards Love 75% Humidity 📚 (Things Living In Your House #55)
```

**Title in the JSON spec**

```
Tiny Bugs in Your Kitchen Cupboards Love 75% Humidity 📚 (Things Living In Your House)
```

**Description**

```
Tiny bugs in kitchen cupboards: booklice are about 1/25 inch long, feed on mold plus flour, grains, cereal and dried fruit, and do best at 75-90% humidity, per Clemson and Utah State extension. #shorts #booklice #psocids #kitchenbugs #meatballmyths
Sources: Clemson Cooperative Extension (Booklice, HGIC); Utah State University Extension (Booklice and Psocids).
```

_YouTube tags: none in the spec._

**TikTok caption**

```
tiny bugs in your kitchen cupboards 📚 booklice are about a millimeter long, eat mold plus flour and dried fruit, and like humid air. Found any in your pantry? #booklice #tinybugs #pantry #meatballmyths
```

**Pinned comment**

```
What's the tiniest bug you've ever found in your kitchen cupboards, and where did you find it?
```

### New draft

**Title**

```
Tiny Bugs in Kitchen Cupboards: Booklice Do Best at 75-90% RH 📚 (Things Living In Your House #55)
```

**Description**

```
What are the tiny bugs in my kitchen cupboards? Booklice, also called psocids, are about 1/25 inch long (about a millimeter), feed on molds plus flour, grains, cereal, and dried fruit, and do best at 75-90% relative humidity, per Clemson and Utah State extension. They can gather around leaking or sweating pipes. They are negatively affected by low humidity (50-60%) and can die within weeks if levels stay low; control is described as reducing humidity below 50%.

#booklice #psocids #kitchenbugs #meatballmyths #shorts

Sources: Clemson Cooperative Extension (Booklice, HGIC); Utah State University Extension (Booklice and Psocids).
```

**YouTube tags (8–12, each ≤30 characters, from this turn's `postkit.py kw` suggestions the Short answers)**

```
["tiny bugs in kitchen cupboards", "tiny bugs in kitchen", "tiny bugs in kitchen cabinets", "tiny bugs in kitchen pantry", "booklice", "booklice in kitchen", "booklice in kitchen cupboards", "psocids", "psocids in kitchen", "booklice (psocids)", "things living in your house", "Meatball Myths"]
```

**TikTok caption**

```
what are the tiny bugs in my kitchen cupboards? booklice are about 1/25 inch long, feed on mold plus flour, grains, cereal, and dried fruit, and do best at 75-90% humidity. Meatball's cereal expired years ago. Found any in your pantry? #booklice #psocids #kitchenbugs #pantrybugs #cupboardbugs
```

**Pinned comment**

```
What's the tiniest bug you've ever found in your kitchen cupboards, and where did you find it?
```

### Lint (`postkit.py lint` on local copies)

YouTube-named spec:

```
lint /workspace/packaging/lint-specs/booklice-cupboard-v6-yt.json  (youtube)
  ok   spoken: 0 mild word(s), no strong ones
  ok   title 98 of 100 units
  WARN description has 5 hashtags (the standard is four: two topic, #meatballmyths, #shorts)
  ok   12 tags, 257 characters, longest 30
  => pass (0 fail, 1 warn)
```

TikTok-named copy (caption rules):

```
lint /workspace/packaging/lint-specs/tt-booklice-cupboard-v6-yt.json  (tiktok)
  ok   spoken: 0 strong word(s), none shown in full in the captions
  ok   caption 293 of 2,200 units, 5 hashtags
  => pass (0 fail, 0 warn)
```

## Lint and gaps (all nine)

### Lint

- All nine YouTube draft specs **passed** `postkit.py lint` (exit 0) with a **warning** that the description has 5 hashtags rather than lint's coded standard of 4 (two topic + `#meatballmyths` + `#shorts`). That is the MASTER_ORDERS vs `postkit.py` mismatch noted above. No FAILs.
- All nine TikTok-named copies **passed** caption lint (5 topic hashtags, caption text ends with a question, no `#fyp` / brand / links / swears).
- Spoken-line results (mild-word counts, etc.) are from the existing funny-pass scripts, which were not rewritten.
- `--mp4` was not passed: the sparse clone excluded episode media, so duration was not checked.

### Gaps

1. **Second-model check still needed** before any draft is applied to Metricool or the repo, per MASTER_ORDERS ('any change of wording goes through the second-model check first').
2. **Metricool's live/queued tag lists and the exact first sentence currently on each post were not readable from the repo.** Specs have no `tags` key. pending-swaps says the later six had hashtags reordered in Metricool on 11/13 without other wording changes; the JSON files still start their hashtag runs with `#shorts`, so the scheduler copy may already differ.
3. **YouTube hashtag feeds were not fetched.** Topic hashtags are the ones already in each spec, reordered. `postkit.py kw` covers search suggestions, not the hashtags YouTube shows above a title.
4. **11/14 11:00 and 15:00 slots have already passed** (and were not confirmed live from Studio or Metricool). Applying new metadata there would be a live edit, not a pre-schedule update.
5. **JSON vs posted.csv title drift:** most JSON titles omit the series number (`#52`, `#55`, `#56`, `#58`–`#63`) that `posted.csv` already uses. The carpet-beetle JSON title is 'Small Brown Bugs in Your House Can Lay 40 Eggs in Your Wool 🧶 (Things Living In Your House)' vs scheduled 'Carpet Beetles at Your Window Can Lay 40 Eggs in Your Wool 🧶 (Things Living In Your House #58)'. Drafts follow the scheduled naming plus the 11/12 title rules.
6. **Lint will keep warning** until either MASTER_ORDERS is changed to two topic hashtags or `postkit.py` is updated to five. These drafts do not change that tool.
7. **'Your cat' / 'Your dog' leading titles** do not apply: these nine are house-bug/spider Shorts, not pet episodes.
8. Tags that promise control advice ('how to get rid of', 'treatment', 'home remedy', 'kill') were left out even when they appeared in suggestion lists, because the Shorts do not give that advice (except booklice, whose description reports the humidity-reduction line already in the Clemson source).

### Tools run

- `postkit.py kw` on topic seeds (YouTube + web suggestions), 15 Nov 2026, output in `/workspace/packaging/kw/kw-bug-shorts.csv` and `kw-bug-shorts-2.csv`.
- `postkit.py lint` on `/workspace/packaging/lint-specs/*-v6-yt.json` and `tt-*-v6-yt.json`.
- Sparse clone used for reads and lint only: `/workspace/skills-readonly` (branch `claude/youtube-monetization-strategy-m9vz6i`). Git status was not modified.

