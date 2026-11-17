# A/B repack for Test & Compare, 11/16

**Applying in Studio needs Moondog88's own okay.** Nothing here has been uploaded, applied, posted or committed.

Made by Social: Packaging & Thumbnails for Social Studio on Mon 11/16 (ET). Due Tue 11/17, 3 PM ET.

## How Test & Compare works (YouTube Help 13861714, read 11/16)
- It tests up to 3 titles and/or thumbnails, on desktop Studio only, for long-form videos only. The winner is picked by **watch-time share**, not CTR.
- If the result is "Inconclusive", the **first** pair you upload stays as the default, and the small control group also sees the default. So **upload the "A" pair first**.
- Changing the title or thumbnail during the test stops it. Use **Title and thumbnail** mode with the 3 pairs below.

## Honesty flags (read first)
1. **Neither priority video has house-bug content.** Weird Animal Facts (`animal-myths-05.json`) has no spider, centipede, roach or bed bug. Animals Thought Extinct (`explains-01-extinct.json`) has a stick insect, but on a sea cliff in Australia, not in a house. **No "never kill" or house-bug angle is used.** I used the strongest creature that is really in each video.
2. **None of the vidIQ terms fit these two** (black widow, can you survive, would you survive, bed bugs, house centipede). The searched words I used come from each video's own tags: "weird animal facts", "animals thought extinct found alive" and "extinct animals found alive".
3. The only honest house angle among the 5 videos is **daddy longlegs / the cellar spider "in your basement"** in `RwbgzQisvYM` (retitle option 2 below).
4. **`2EC5LDtbUbo` has already been retitled live** to "The CIA Tried to Turn a Cat Into a Spy 🐱" (YouTube oEmbed, checked 11/16). The 0.87% CTR on 115 impressions was measured under the **old** title, so we don't know yet how the new one performs. It's also outside the animals/house-bugs lane (CIA / Cold War).
5. **Art caveats I can see at full size:** extinct-A has a visible vertical seam where the dark background changes, about 50% across. The coelacanth in extinct-B has ordinary-looking fins, not the "fins like little legs" from the script. In extinct-C, Shep is a generic ranch dog (the script gives no breed), and the ferret is shown alive next to him; the script only says Shep "brought one home". Weird-A's three suspect birds are small at 168 px but still read as birds.

6. **First-40-character check:** the searched phrase is inside the first 40 characters in every title. The creature name is also inside the first 40 in the Weird Animal Facts titles and in extinct-B ("fish"). In extinct-A, "Tree Lobster" starts at character 37 and runs past 40, and extinct-C names the dog, not the ferret. Both are trade-offs to keep the searched phrase first.

## Meatball face size (what I actually see, not a script measurement)
Judged by eye on the full-size PNGs and the 168 px sheet:

| File | Meatball width | Meatball height | Width at 168 px |
|---|---|---|---|
| weird-A | ~48% | ~89% | ~80 px |
| weird-B | ~45% | ~84% | ~75 px |
| weird-C | ~58% (cropped at right/bottom) | ~97% | ~95 px |
| extinct-A | ~47% | ~88% | ~80 px |
| extinct-B | ~53% (cropped) | ~99% | ~88 px |
| extinct-C | ~49% (cropped at left/bottom) | ~97% | ~82 px |

That's roughly half the frame in all six, and his eyes and mouth read clearly at 168 px. For comparison, v6b was about 25%.

## Files
- 1280x720 PNGs: `weird-A-3-are-fake.png`, `weird-B-cracks-glass.png`, `weird-C-cube-poop.png`, `extinct-A-hiding-80-years.png`, `extinct-B-outlived-dinosaurs.png`, `extinct-C-a-dog-found-it.png`
- `phone-preview-168.png`: all six thumbnails at 168 px wide.
- `_work/`: the raw GenerateImage art (`gen-*.jpg`, text-free, Meatball drawn from `sd-6-toon-whoa.jpg`), `compose.py` (Anton text in PIL), `contact-sheet.png`, the current live thumbnails (`cur-*.jpg`) for before/after, and `phone-preview-168-x3.png`.
- Style: navy #0B1A2E background, Anton text in yellow #FFD21F with one red #E0201B word and a dark outline, 2–3 words per thumbnail. Words sit at the top, clear of the bottom-right timestamp badge.

---

## Priority 1: Weird Animal Facts You Didn't Know (3 Are Fake. Can You Spot Them?)
- **ID/URL:** `z-Kg8sXCxlU`: https://www.youtube.com/watch?v=z-Kg8sXCxlU
- **Current title:** Weird Animal Facts You Didn't Know (3 Are Fake. Can You Spot Them?) (live title confirmed via oEmbed on 11/16)
- **Current CTR / impressions:** 1.82% CTR on 5,262 impressions, 11.00% average viewed. Sources: `/workspace/packaging/winners-baseline-1115.csv` and Social Studio's brief.
- **Content:** `skills-readonly/skills/oh-meatball/scripts/animal-myths-05.json` (the posted.csv entry is `myths-05`, 10/26). It's a 12-fact quiz: wombat cube poop, octopus 3 hearts, sea otters hold hands, flamingos born pink (fake), starfish regrow, murder of crows, platypus glows, ostrich fastest (fake), duck quack doesn't echo (fake), hummingbirds fly backwards, mantis shrimp cracks glass, elephants can't jump.

| # | Title | Image | Thumbnail text (red word) | Why | Content source |
|---|---|---|---|---|---|
| **A (upload first)** | Weird Animal Facts: A Shrimp Punch That Cracks Glass | `weird-B-cracks-glass.png` | IT CRACKS **GLASS** | This is the most dramatic moment in the video and gives the strongest TOO SLOW-style image (punch, flash, cracked glass, Meatball recoiling). It's a single concrete promise, not a quiz. | Beats 80–86: "True or false? A mantis shrimp can punch hard enough to crack aquarium glass. True." and "people keeping them in small tanks have reported cracked glass." |
| B | Weird Animal Facts That Sound Fake (Only 3 Are) | `weird-A-3-are-fake.png` | 3 ARE **FAKE** | Keeps the quiz promise the video pays off, but in fewer words. Meatball side-eyes the three fakes lined up like suspects. | Beat 3: "Some of these facts sound completely made up, and most of them are real"; beat 4: "Three of these are lies"; beat 95 names the fakes: baby flamingos, ostrich, duck. The three birds drawn are exactly those. |
| C | Weird Animal Facts: Wombats Poop Cubes (+11 More) | `weird-C-cube-poop.png` | CUBE **POOP?** | This is the video's very first line (frame-0 match) and a strong curiosity question. PLAY DEAD?-style question on navy. | Beats 0 and 5–12: "Cube shaped poop." / "True or false? Wombats poop cubes. True!" There are 12 facts in total, so "+11 More" is accurate. |

**Pick: A (the shrimp).** It's the clearest single image and the most concrete promise. The "3 are fake" quiz pair is B, so the test also tells us whether quiz framing helps watch time.

## Priority 2: Animals Thought Extinct Found Alive (One Was Hiding on a Rock for 80 Years)
- **ID/URL:** `o9Emu9oMgCs`: https://www.youtube.com/watch?v=o9Emu9oMgCs
- **Current title:** Animals Thought Extinct Found Alive (One Was Hiding on a Rock for 80 Years) (live title confirmed via oEmbed on 11/16)
- **Current CTR / impressions:** 2.53% CTR on 3,438 impressions, 15.85% average viewed. Sources: `winners-baseline-1115.csv` and Social Studio's brief.
- **Content:** `scripts/explains-01-extinct.json` (`explains-01`, 10/25). It covers the coelacanth (1938, and an Indonesian one found in 1997), the takahē (1898 to 1948), the black-footed ferret (declared extinct 1979; Shep the ranch dog, 1981), and the Lord Howe Island stick insect, "tree lobster" (gone around 1920, found on Ball's Pyramid in 2001).

| # | Title | Image | Thumbnail text (red word) | Why | Content source |
|---|---|---|---|---|---|
| **A (upload first)** | Animals Thought Extinct Found Alive: The Tree Lobster | `extinct-A-hiding-80-years.png` | **HIDING** 80 YEARS | This is the payoff the video promises in its first 12 seconds and delivers last, so the click promise is paid off at the end, which helps watch time. It's a giant insect on a sea rock. It keeps the searched phrase and moves the "80 years" into the image. | Beat 0: "Rats ate every last one on its island. Eighty years later, it turned up alive, on a rock in the middle of the ocean"; beats 34–38: Ball's Pyramid, "known locally as the tree lobster". |
| B | Extinct Animals Found Alive: The Fish That Outlived Dinosaurs | `extinct-B-outlived-dinosaurs.png` | OUTLIVED **DINOSAURS** | Uses the higher-volume search phrase (8.7K/mo per vidIQ in the script note). The coelacanth is the first full story in the video, and the image is a fish next to its own fossil. | Beat 1: "This fish was supposed to have died out with the dinosaurs"; beat 8: "Sixty six million years of being extinct, and it was just in the ocean"; beat 6 shows the fossils. |
| C | Animals Thought Extinct Found Alive (A Ranch Dog Found One) | `extinct-C-a-dog-found-it.png` | A **DOG** FOUND IT | A human-interest story with a dog hero, which gives a very different feel from A and B (warm, not spooky). | Beats 3 and 24–27: "this ferret came back from extinction because a farm dog called Shep brought one home"; "a ranch dog in Wyoming named Shep"; beat 45: "By a curator, a doctor, a dog…" |

**Pick: A (the tree lobster).** It's the video's own promised payoff, so it's the best bet for watch time.

---

## Retitles (text only; thumbnail text is optional)
Same rules apply: none of TRUE/FALSE/Myth/Believe/WRONG/conspiracy, and the searched words and creature appear in the first 40 characters. Each can also run as a "Title only" test.

### Everything You Know About Animals Is WRONG: `gFhrONKK0rI`
https://www.youtube.com/watch?v=gFhrONKK0rI. Current CTR is 2.93% on 750 impressions, 41.80% viewed (`winners-baseline-1115.csv`). It's a 2:15 horizontal video (`data/retention.csv`), script `scripts/animal-myths-01.json`. It covers 4 facts: ostriches don't bury their heads, goldfish remember for months, bulls charge the movement not the red, and bats aren't blind.

1. **Do Ostriches Bury Their Heads? 4 Animal Facts, Fixed** (thumbnail: NOT **HIDING**). This is the opening question at 0:00, so it matches the start of the video. Beat 2: "fixing the animal facts"; on-screen text "NOT HIDING. PARENTING." **Pick.**
2. **Goldfish Don't Have a 3-Second Memory (+3 Animal Facts)** (thumbnail: IT REMEMBERS **YOU**). Beats 9–12: "remember these tricks for months"; on-screen text "IT REMEMBERS YOU."
3. **Why Bulls Charge a Red Cape (It's Not the Red)** (thumbnail: NOT THE **RED**). Beats 13–17. Note: this promises one of the four facts (about 20 seconds), so it's the weakest fit for watch time.

### 12 Animal Myths You've Believed Your Whole Life (Disney Faked One): `RwbgzQisvYM`
https://www.youtube.com/watch?v=RwbgzQisvYM. Current CTR is 1.25% on 399 impressions, 6.58% viewed (`winners-baseline-1115.csv`). Script `scripts/animal-myths-02.json` covers 12 facts, all false (beat 88: "Every single one was false"). The lemming/Disney story runs first (beats 2–11).

1. **Lemmings Don't Jump Off Cliffs. Disney Faked It (and Won an Oscar)** (thumbnail: DISNEY **FAKED** IT). Beats 8–11: White Wilderness (1958), the crew herded them, it won the Oscar. This is the claim the video opens with. Note: the faking claim rests on "a Canadian TV investigation" (beat 9), the same claim the current title already makes. **Pick.**
2. **Are Daddy Longlegs Venomous? 12 Animal Facts, Checked** (thumbnail: MOST **VENOMOUS?**). This is the one honest house angle: beat 32, "the skinny cellar spider in your basement"; beat 34, "Just a very leggy roommate." It's one of 12 segments, and it says "venomous", not "spider", because beat 30 says a harvestman isn't a spider.
3. **12 Animal Facts That Aren't Real (Disney Faked One)** (thumbnail: ALL 12 **FAKE**). Beat 88: "Every single one was false."

### Conspiracy video, now live as "The CIA Tried to Turn a Cat Into a Spy 🐱": `2EC5LDtbUbo`
https://www.youtube.com/watch?v=2EC5LDtbUbo. The original title was "Conspiracy Theories That Turned Out To Be TRUE" (posted.csv, 10/27). Baseline was 0.87% CTR on 115 impressions, 68.89% viewed (`winners-baseline-1115.csv`), but that was **under the old title**; the retitle in `title-changes-apply.csv` is now live. Script `scripts/longform-turned-out-true.json` covers 4 cases: Acoustic Kitty, Gulf of Tonkin, Operation Northwoods, MKUltra.

1. **Keep: The CIA Tried to Turn a Cat Into a Spy 🐱** (thumbnail: **SPY** CAT). Beat 0, word for word. **Pick:** let it collect impressions before testing.
2. **The CIA Spy Cat, MKUltra & 2 More Plans From Declassified Files** (thumbnail: IT WAS **REAL**, the script's own `thumb_text`). Blurb: "four that are documented in declassified files."
3. **Operation Northwoods & the CIA Spy Cat: 4 Cold War Files** (thumbnail: SPY **CAT?**). Beats 5–13 and 28+. Don't say the cat was hit by a taxi: beat 12 labels that a disputed claim.
