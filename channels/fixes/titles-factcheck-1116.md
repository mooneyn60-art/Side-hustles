# Titles fact-check — 16 Nov 2026

Checked against scripts, fact packs, YouTube descriptions in `/workspace/ret/channel_videos.json`, packaging lint specs, and retention openings, all read this session. Spoken lines and descriptions were not invented. Titles must not claim more than the video or source. Required hedges stay word for word. Scripts were not edited. Nothing was committed, posted, or messaged.

Times below are America/New_York.

## Verdict counts

- **PASS:** 93
- **FIX:** 8
- **UNVERIFIABLE:** 2
- **Total titles in `/workspace/fixes/titles-1116.md`:** 103

## Required special checks

### 1. Lilies — `0WyELCaZOls` (#14) — **UNVERIFIABLE**

Proposed: “Are Lilies Poisonous to Cats? Inside Sauce's Kidneys”

Spoken script for the posted lily Short (`0WyELCaZOls`) was not found on the box, and no fetchable transcript or opening was located this session. The house-cat fact pack and the Short's packaging lint description do name kidneys, so 'Kidneys' is allowed in a title *if* the posted cut says it. The required ASPCA Animal Poison Control closing line belongs in the last spoken line, last caption line, and description (title-pattern §3 / toxic-food rule), not the 60-character YouTube title, which cannot hold it.

- Fact pack quote (kidneys named): “The FDA says a small amount of a true lily or daylily, even pollen licked off fur or vase water, can cause fatal kidney failure in cats in under 3 days.”
  - Source: `/workspace/skills-readonly/skills/oh-meatball/research/87-house-cat-life-factpack.md` row HC-E1.
- Packaging lint description (kidneys named, not confirmed as posted speech): “The FDA says the entire lily plant is toxic: the stem, leaves, flowers, pollen, and even the water in a vase. It can cause a cat to develop fatal kidney failure in less than 3 days.”
  - Source: `/workspace/packaging/lint-specs/yt-open-cat-lilies.json` description (packaging copy, not confirmed as the posted Short's spoken lines).
- Long-form spoken lines (different video): “The FDA says true lilies and daylilies can cause fatal kidney failure in cats. / Fatal kidney failure, in under three days.”
  - Source: `/workspace/skills-readonly/skills/oh-meatball/scripts/longform-born-as-house-cat.json` (the long-form, not this Short).

**Ruling:** Do not treat 'Kidneys' as a fail — the pack names kidneys. Do not PASS the title until the posted Short's spoken wording is confirmed. Keep the ASPCA close on the last spoken line, last caption line, and description; do not try to shoehorn it into the title.

### 2. Turkey — `ZFtZo6KPjHM` (#29) — **FIX**

- Proposed: “Can Dogs Eat Turkey? Inside Noodle's Stomach”
- Corrected: “Can Dogs Eat Turkey? Boneless and Fully Cooked” (46 characters)
- Why: The food-safety condition was dropped. The script and posted title both keep the ASPCA condition 'boneless and fully cooked.'
- Script/pack line: “Can dogs eat turkey? The ASPCA says if you share, make it boneless and fully cooked.”
- Source: `/workspace/skills-readonly/skills/oh-meatball/scripts/drawn-house/dog-turkey-v6-yt.json` beat 0. Description: "If you do decide to share a small bite of turkey, it says to make sure it's boneless and fully cooked." Posted title also uses that phrase.

### 3. Guilty look — `xIbnhX10r7k` (#26) — **FIX**

- Proposed: “Why Do Dogs Look Guilty? Inside Noodle's Brain”
- Corrected: “Why Do Dogs Look Guilty? It May Not Be a Confession” (51 characters)
- Why: The proposed title drops the required hedge. Spoken line and posted title both use 'may not be a confession.' Keep that wording.
- Script/pack line: “Your dog's guilty look may not be a confession.”
- Source: `/workspace/skills-readonly/skills/oh-meatball/scripts/drawn-house/dog-guilty-look-v6-yt.json` beat 0. Posted title: "14 Dogs Tested: Your Dog's Guilty Look May Not Be a Confession."

### 4. Spider rain — `slF0ATLLfxc` (#81) — **PASS**

- Proposed: “Spider Rain: Can It Actually Rain Spiders?”
- The video is about ballooning in general, not Australia only. Australia is one example. The proposed general title is fair and should not be narrowed to Australia.
- Script line: “In Australia, whole fields turned white.”
- Source: `/workspace/skills-readonly/skills/oh-meatball/scripts/v4-spiders.json` beat 17 (Meatball vs Spiders #2). Source note on beat 11: "Goulburn, NSW, May 2015: millions of ballooning spiders left fields covered in silk ('angel hair') — https://www.smithsonianmag.com/smart-news/millions-baby-spiders-rained-down-australia-180955318/" Other spoken beats cover silk ballooning, electric fields, planes, and Darwin at sea.

### 5. Dust mites (how do you know) — `s_L3sGikMWU` (#76) — **FIX**

- Proposed: “How Do You Know If You Have Dust Mites?”
- Corrected: “Dust Mites in Your Mattress” (27 characters)
- Why: The proposed title asks how you know if you have dust mites. The script describes what they are, that they are too small to see, that they eat shed skin, and that they don't bite. It does not give detection signs or a test.
- Script lines: “There are tiny monsters in your bed, eating your skin. Dust mites. Eight legs. Cousins of spiders and ticks. Way too small to see. They eat the skin flakes you shed. One gram of dust can hold thousands. They don't drink. They soak water out of the air. They don't bite. It's their poop that makes you sneeze.”
- Source: `/workspace/skills-readonly/skills/oh-meatball/scripts/drawn-house/dust-mites-yt.json` spoken beats. Opening in `/workspace/ret/openings_joined.json` matches beat 0.

## All FIX titles

### #1 `KWOM2-mNmww` — **FIX**

- Old: Don't Kill the Spider in Your Corner. It Eats Bigger Spiders
- Proposed: Should You Kill Spiders? Inside Your Ceiling Corner
- Corrected: **Should You Kill the Spider in Your Ceiling Corner?** (50 characters)
- Why: The proposed title widens a cellar-spider / ceiling-corner video to spiders in general.
- Supporting line: “That skinny spider in the corner of your ceiling is hunting something in your house. Sometimes, something much bigger. ... If you're not sure what spider you have, don't handle it.”
- Source: YouTube description for `KWOM2-mNmww` in `/workspace/ret/channel_videos.json` (read this session).

### #13 `gFhrONKK0rI` — **FIX**

- Old: Everything You Know About Animals Is WRONG
- Proposed: Animal Myths Debunked: Everything You Know Is Wrong
- Corrected: **4 Animal Myths You Might Still Believe** (38 characters)
- Why: The title claims 'Everything You Know Is Wrong.' The video covers four specific myths (ostriches, goldfish, bulls, bats), not everything.
- Supporting line: “Ostriches don't bury their heads in the sand. Goldfish don't have a 3-second memory. Bulls don't hate red. And bats? Not blind. Meatball fixes the animal "facts" your teacher, your uncle and the whole internet got wrong.”
- Source: YouTube description for `gFhrONKK0rI` in `/workspace/ret/channel_videos.json` (read this session).

### #16 `A9lteZ9mtDE` — **FIX**

- Old: Female Dust Mites in Your Bed Lay About 50 Eggs 😬 (Things Living In Your House #56)
- Proposed: Where Do Dust Mites Come From?
- Corrected: **Female Dust Mites in Your Bed Lay About 50 Eggs** (47 characters)
- Why: The proposed title asks where dust mites come from. The script is about egg count and life cycle, not origin. Keep the hedge 'about 50'.
- Supporting line: “Your bed's female mites lay about 50 eggs. ... In ideal conditions, eggs are adults in about a month. Adults live about one to two months. ... Keep humidity under 50 percent, and mites struggle.”
- Source: `/workspace/skills-readonly/skills/oh-meatball/scripts/drawn-house/dust-mites-v6-yt.json` spoken beats and description (University of Kentucky Entomology, ENTFACT-646).

### #26 `xIbnhX10r7k` — **FIX**

- Old: 14 Dogs Tested: Your Dog's Guilty Look May Not Be a Confession 🐶 (Things Living In Your House #65)
- Proposed: Why Do Dogs Look Guilty? Inside Noodle's Brain
- Corrected: **Why Do Dogs Look Guilty? It May Not Be a Confession** (51 characters)
- Why: The proposed title drops the required hedge. Spoken line and posted title both use 'may not be a confession.' Keep that wording.
- Supporting line: “Your dog's guilty look may not be a confession.”
- Source: `/workspace/skills-readonly/skills/oh-meatball/scripts/drawn-house/dog-guilty-look-v6-yt.json` beat 0. Posted title: "14 Dogs Tested: Your Dog's Guilty Look May Not Be a Confession."

### #29 `ZFtZo6KPjHM` — **FIX**

- Old: If Dogs Eat Turkey: Boneless and Fully Cooked, Says the ASPCA 🦃 (Things Living In Your House #70)
- Proposed: Can Dogs Eat Turkey? Inside Noodle's Stomach
- Corrected: **Can Dogs Eat Turkey? Boneless and Fully Cooked** (46 characters)
- Why: The food-safety condition was dropped. The script and posted title both keep the ASPCA condition 'boneless and fully cooked.'
- Supporting line: “Can dogs eat turkey? The ASPCA says if you share, make it boneless and fully cooked.”
- Source: `/workspace/skills-readonly/skills/oh-meatball/scripts/drawn-house/dog-turkey-v6-yt.json` beat 0. Description: "If you do decide to share a small bite of turkey, it says to make sure it's boneless and fully cooked." Posted title also uses that phrase.

### #50 `RhU0OBK0Om0` — **FIX**

- Old: Dust Mites: 8 Legs Live In Your Pillow 😬 (Things Living In Your House #49)
- Proposed: What Do Dust Mites Look Like?
- Corrected: **Do Eight-Legged Dust Mites Live in Your Pillow?** (47 characters)
- Why: The proposed title asks what dust mites look like. The posted title and the 3-second opening only say the pillow has eight-legged dust-mite roommates. No script was found that gives a visual ID (size, color, shape).
- Supporting line: “Opening (retention openings file, first ~3s, ASR): "Meatball, your pillow has eight legged roommates. Gus mites," (ASR likely heard 'Dust mites'). Posted title: "Dust Mites: 8 Legs Live In Your Pillow."”
- Source: `/workspace/ret/openings_joined.json` entry for `RhU0OBK0Om0`; posted title in `/workspace/ret/channel_videos.json`. Full spoken script not found this session.

### #61 `YrPzxjXZJCY` — **FIX**

- Old: A Brown Recluse Hides in Your Shoes and Its Venom Can Kill Skin 🕷️ (Is This Spider Venomous? #2)
- Proposed: Where Do Brown Recluse Spiders Live?
- Corrected: **Can a Brown Recluse Hide in Your Shoes?** (39 characters)
- Why: The proposed title asks where brown recluses live (typically a geographic-range question). The YouTube short scripts matching the posted title are about hiding in shoes, venom, and six eyes. Range lines appear only in a longer TikTok cut (`brown-recluse-tt.json`) that does not match the posted YT title.
- Supporting line: “The spider in your shoe has venom that can kill skin. Shrink down. By day, it hides in shoes. Venomous? Yes. About one bite in ten scars. Count its eyes: six, not eight. One Kansas house had over two thousand. Nobody was bitten.”
- Source: `/workspace/skills-readonly/skills/oh-meatball/scripts/drawn-house/brown-recluse-v4-yt.json` (same spoken lines in v2 and v3). Posted title: "A Brown Recluse Hides in Your Shoes and Its Venom Can Kill Skin."

### #76 `s_L3sGikMWU` — **FIX**

- Old: Millions of Mites Can Live in Your Mattress 😬 (Things Living In Your House #2)
- Proposed: How Do You Know If You Have Dust Mites?
- Corrected: **Dust Mites in Your Mattress** (27 characters)
- Why: The proposed title asks how you know if you have dust mites. The script describes what they are, that they are too small to see, that they eat shed skin, and that they don't bite. It does not give detection signs or a test.
- Supporting line: “There are tiny monsters in your bed, eating your skin. Dust mites. Eight legs. Cousins of spiders and ticks. Way too small to see. They eat the skin flakes you shed. One gram of dust can hold thousands. They don't drink. They soak water out of the air. They don't bite. It's their poop that makes you sneeze.”
- Source: `/workspace/skills-readonly/skills/oh-meatball/scripts/drawn-house/dust-mites-yt.json` spoken beats. Opening in `/workspace/ret/openings_joined.json` matches beat 0.

## UNVERIFIABLE

### #14 `0WyELCaZOls` — **UNVERIFIABLE**

See special check 1 above. Proposed title may be used only after the posted Short's spoken lines are confirmed to name kidneys.

### #15 `6RlqUWLbfz8` — **UNVERIFIABLE**

- Old: A Grizzly Is Sniffing You. Do You Move?
- Proposed: What to Do If a Grizzly Bear Approaches You?
- Why: No matching script, YouTube description, or fetchable transcript for `6RlqUWLbfz8` was found this session. The posted title is 'A Grizzly Is Sniffing You. Do You Move?' The proposed title widens that to any approach and asks for advice the video may or may not give. Nearby grizzly scripts (`grizzly-wms-v6-yt.json` and related) belong to the different video 'You Can't Outrun a Grizzly Bear' (`ySeN6ul2mlQ`, #25) and were not used as a substitute.

## Notable PASSes (checked closely)

### #81 `slF0ATLLfxc` — **PASS** — Spider Rain: Can It Actually Rain Spiders?

- The video is about ballooning in general, not Australia only. Australia is one example. The proposed general title is fair and should not be narrowed to Australia.
- “In Australia, whole fields turned white.”
- Source: `/workspace/skills-readonly/skills/oh-meatball/scripts/v4-spiders.json` beat 17 (Meatball vs Spiders #2). Source note on beat 11: "Goulburn, NSW, May 2015: millions of ballooning spiders left fields covered in silk ('angel hair') — https://www.smithsonianmag.com/smart-news/millions-baby-spiders-rained-down-australia-180955318/" Other spoken beats cover silk ballooning, electric fields, planes, and Darwin at sea.

### #25 `ySeN6ul2mlQ` — **PASS** — Can You Outrun a Grizzly Bear?

- The script answers the question (you can't; bears can run as fast as a racehorse; do not run).
- “You can't outrun a grizzly. Bears can run as fast as a racehorse.”
- Source: `/workspace/skills-readonly/skills/oh-meatball/scripts/drawn-house/grizzly-wms-v6-yt.json`.

### #33 `-O-_YBst4R8` — **PASS** — How Do You Know If You Have Termites?

- The script does answer detection in part (wood looks fine outside, screwdriver test, mud tubes).
- “The wood looks fine outside. But it's thin, and a screwdriver pokes right through. ... Underground termites build mud tubes up to the wood, to stay damp.”
- Source: `/workspace/skills-readonly/skills/oh-meatball/scripts/drawn-house/termite-yt.json`.

### #47 `-Fths6h79_o` — **PASS** — Why Are There So Many Stink Bugs?

- The script explains fall overwintering in houses and the 26,000-in-one-house count, which supports a 'why so many' question.
- “One man in Maryland caught over twenty six thousand inside his house, in six months. ... In the fall, they crawl into your house, to spend the winter.”
- Source: `/workspace/skills-readonly/skills/oh-meatball/scripts/drawn-house/stink-bug-yt.json`.

### #48 `wHCrmIPdCgg` — **PASS** — What Kills Dust Mites?

- The script answers what kills them: wash at 130°F or freeze 24 hours (poop/allergen remains).
- “Wash your sheets under 130 degrees, and the mites in your bed live. ... Can't wash it? Freeze it for 24 hours. They die. But the poop stays behind.”
- Source: `/workspace/skills-readonly/skills/oh-meatball/scripts/drawn-house/dust-mites-2-v6-yt.json`.

## Full verdict table

| # | Type | ID | Proposed title | Verdict | Corrected title / note |
|---|---|---|---|---|---|
| 1 | Long | `KWOM2-mNmww` | Should You Kill Spiders? Inside Your Ceiling Corner | FIX | Should You Kill the Spider in Your Ceiling Corner? |
| 2 | Long | `viD-nbPdaxk` | What Happens to Your Cat When You Keep Them Indoors? | PASS | — |
| 3 | Long | `xeAsg5ECpgw` | Bugs in Your House You Should Never Kill: 3 More | PASS | — |
| 4 | Long | `cH3HCZ8GlHk` | 3 Bugs in Your House You Should Never Kill (And 4 You Must) | PASS | — |
| 5 | Long | `4-gvZTWf2wg` | Project Azorian: The CIA's Giant Claw for a Soviet Sub | PASS | — |
| 6 | Long | `bqij8Ht6SX4` | Most Dangerous Bugs in Your House, Ranked | PASS | — |
| 7 | Long | `Lid8JXhg1Q4` | 6 Creatures Living in Your House Right Now | PASS | — |
| 8 | Long | `2EC5LDtbUbo` | Acoustic Kitty: The CIA's Cat Spy Project | PASS | — |
| 9 | Long | `z-Kg8sXCxlU` | Weird Animal Facts You Didn't Know (3 Are Fake) | PASS | — |
| 10 | Long | `o9Emu9oMgCs` | Animals Thought to Be Extinct but Still Alive | PASS | — |
| 11 | Long | `Uqj0QL8G0d4` | How Did Wolves Become Dogs? Inside Noodle's DNA | PASS | — |
| 12 | Long | `RwbgzQisvYM` | Animal Myths You Still Believe (Disney Faked One) | PASS | — |
| 13 | Long | `gFhrONKK0rI` | Animal Myths Debunked: Everything You Know Is Wrong | FIX | 4 Animal Myths You Might Still Believe |
| 14 | Short | `0WyELCaZOls` | Are Lilies Poisonous to Cats? Inside Sauce's Kidneys | UNVERIFIABLE | Spoken cut not found this session |
| 15 | Short | `6RlqUWLbfz8` | What to Do If a Grizzly Bear Approaches You? | UNVERIFIABLE | No matching script or transcript this session |
| 16 | Short | `A9lteZ9mtDE` | Where Do Dust Mites Come From? | FIX | Female Dust Mites in Your Bed Lay About 50 Eggs |
| 17 | Short | `w_eCp3tO_dQ` | Are Daddy Long Legs Dangerous? | PASS | — |
| 18 | Short | `fIkJjdAk7DU` | Should I Kill House Centipedes? | PASS | — |
| 19 | Short | `ee11oL_NVv4` | What Do Daddy Long Legs Eat? | PASS | — |
| 20 | Short | `0nxiX4PgQAk` | How Many Shark Attacks Per Year? | PASS | — |
| 21 | Short | `MEEPvBFpcQM` | How Small of a Hole Can a Mouse Fit Through? | PASS | — |
| 22 | Short | `S2Cd7bme-FY` | Do Cats Know Their Names? Inside Sauce's Brain | PASS | — |
| 23 | Short | `UBxPyhlF-3g` | Are Cellar Spiders Dangerous? | PASS | — |
| 24 | Short | `L6xt-kze48M` | House Centipede vs Spider: Who Wins? | PASS | — |
| 25 | Short | `ySeN6ul2mlQ` | Can You Outrun a Grizzly Bear? | PASS | — |
| 26 | Short | `xIbnhX10r7k` | Why Do Dogs Look Guilty? Inside Noodle's Brain | FIX | Why Do Dogs Look Guilty? It May Not Be a Confession |
| 27 | Short | `Jnfkdif5DAk` | Why Does My Dog Stare at Me? Inside Noodle's Brain | PASS | — |
| 28 | Short | `U5rb_1PXazA` | Why Do Cats Purr? Inside Sauce's Voice Box | PASS | — |
| 29 | Short | `ZFtZo6KPjHM` | Can Dogs Eat Turkey? Inside Noodle's Stomach | FIX | Can Dogs Eat Turkey? Boneless and Fully Cooked |
| 30 | Short | `n-LJuGWbtvw` | Are Moose Dangerous? | PASS | — |
| 31 | Short | `LaGXZE9aEMs` | Can Cats Taste Sweet? Inside Sauce's Tongue | PASS | — |
| 32 | Short | `LtaMCY1CEK0` | False Widow vs Black Widow: How to Tell Them Apart | PASS | — |
| 33 | Short | `-O-_YBst4R8` | How Do You Know If You Have Termites? | PASS | — |
| 34 | Short | `vn-MTvvQsbg` | Camel Crickets: What's Jumping in Your Basement? | PASS | — |
| 35 | Short | `sPrA70BWGtg` | What Are Boxelder Bugs? | PASS | — |
| 36 | Short | `IvskPD8cY8I` | How Do Roaches Get in Your House? | PASS | — |
| 37 | Short | `ExqLbAxnFPc` | Are Wolf Spiders Dangerous? | PASS | — |
| 38 | Short | `EPimwC5VMgo` | Why You Should Not Kill House Centipedes | PASS | — |
| 39 | Short | `MoQEU9Ii0PU` | Are Asian Lady Beetles Dangerous? | PASS | — |
| 40 | Short | `kiECtPVTcAA` | Why Are Stink Bugs in My House? | PASS | — |
| 41 | Short | `YOoBG8vqs4M` | Are House Spiders Dangerous? | PASS | — |
| 42 | Short | `bm6LzV7eRwg` | Is Daddy Long Legs a Spider? | PASS | — |
| 43 | Short | `ghqr3NDZJY0` | What Does a Mouse Eat? | PASS | — |
| 44 | Short | `taxvYvHCK5k` | Project Azorian: How the CIA Tried to Steal a Sub | PASS | — |
| 45 | Short | `sRJ53EzJY-4` | Cellar Spider vs House Spider: Who Eats Who? | PASS | — |
| 46 | Short | `heI2W3z1hk4` | How Fast Can Bed Bugs Crawl? | PASS | — |
| 47 | Short | `-Fths6h79_o` | Why Are There So Many Stink Bugs? | PASS | — |
| 48 | Short | `wHCrmIPdCgg` | What Kills Dust Mites? | PASS | — |
| 49 | Short | `FeVJWESbIO8` | How Fast Do Roaches Multiply? | PASS | — |
| 50 | Short | `RhU0OBK0Om0` | What Do Dust Mites Look Like? | FIX | Do Eight-Legged Dust Mites Live in Your Pillow? |
| 51 | Short | `1RJw2Pex_Ro` | How Far Can a Jumping Spider Jump? | PASS | — |
| 52 | Short | `dtJdGyuZ1Cc` | Where Do House Centipedes Come From? | PASS | — |
| 53 | Short | `hB5MSJ0y22Q` | How Many Eyes Does a Jumping Spider Have? | PASS | — |
| 54 | Short | `oYkMV5SgkkM` | What Is a Pill Bug? | PASS | — |
| 55 | Short | `pDIsEE8UaQ8` | What Do Bed Bug Bites Look Like? | PASS | — |
| 56 | Short | `1hdMaSxJtkU` | How Many Babies Do Roaches Have? | PASS | — |
| 57 | Short | `QUErD_8A2Ls` | Are House Spiders Venomous? | PASS | — |
| 58 | Short | `66YDY0wDiaU` | How Do You Get Scabies? | PASS | — |
| 59 | Short | `mwe44vC0jus` | How Many Legs Do Centipedes Have? | PASS | — |
| 60 | Short | `FJfiXPoPKK4` | What Do House Centipedes Eat? | PASS | — |
| 61 | Short | `YrPzxjXZJCY` | Where Do Brown Recluse Spiders Live? | FIX | Can a Brown Recluse Hide in Your Shoes? |
| 62 | Short | `Iqww6xgMvig` | Are House Centipedes Dangerous? | PASS | — |
| 63 | Short | `CQcxoE88ABU` | Mouse Droppings in Kitchen: How Many a Day? | PASS | — |
| 64 | Short | `rOdR52lgmDs` | Why Are Cassowaries So Dangerous? | PASS | — |
| 65 | Short | `FTKRLEoa-nU` | Can Cockroaches Live Without Their Heads? | PASS | — |
| 66 | Short | `NxrPLnfEivo` | Jumping Spider in Space: Did It Keep Hunting? | PASS | — |
| 67 | Short | `rLo5MQ8o7F8` | How Do Bed Bugs Bite? | PASS | — |
| 68 | Short | `8t6SDFRGYGs` | How Do Jumping Spiders See? | PASS | — |
| 69 | Short | `480rNDZcXLY` | What Is a Bombardier Beetle? | PASS | — |
| 70 | Short | `vrYgUAN6NBE` | What Kills Black Widows? | PASS | — |
| 71 | Short | `X80bMFb2Vs0` | How Far Can an Owl Turn Its Head? | PASS | — |
| 72 | Short | `twDDpxzrqMw` | Hawk Moth Caterpillar: Snake Mimic Explained | PASS | — |
| 73 | Short | `MXxBz1p23Ck` | Why Do Possums Play Dead? | PASS | — |
| 74 | Short | `oyLxrxANFUU` | What Do Silverfish Eat? | PASS | — |
| 75 | Short | `eKymJSeNhnI` | Do We Have Mites on Our Face? | PASS | — |
| 76 | Short | `s_L3sGikMWU` | How Do You Know If You Have Dust Mites? | FIX | Dust Mites in Your Mattress |
| 77 | Short | `mgbxqkfHLRY` | Do Flies Throw Up When They Land? | PASS | — |
| 78 | Short | `QQJYhTckYCE` | What Are House Centipedes? | PASS | — |
| 79 | Short | `sxvnbCnfEJQ` | Is the Bermuda Triangle Real? | PASS | — |
| 80 | Short | `8Cte_n27TDA` | What Caused the Dancing Plague of 1518? | PASS | — |
| 81 | Short | `slF0ATLLfxc` | Spider Rain: Can It Actually Rain Spiders? | PASS | — |
| 82 | Short | `C7KaAarFUag` | What Is Operation Northwoods? | PASS | — |
| 83 | Short | `HB3DoItvgxM` | What Is the Most Venomous Fish in the World? | PASS | — |
| 84 | Short | `gxi2NH2uuVk` | What Really Happened at Roswell? | PASS | — |
| 85 | Short | `5NuXsDETAeE` | Ironclad Beetle vs Car: Can It Survive? | PASS | — |
| 86 | Short | `88gaODWt4qY` | Project A119: The US Plan to Nuke the Moon | PASS | — |
| 87 | Short | `BPApE_A4SxE` | How Deadly Is a Puffer Fish? | PASS | — |
| 88 | Short | `K9G9aHnurgs` | Killdeer Broken Wing Act: Why Does It Fake? | PASS | — |
| 89 | Short | `BbXgW3KPzdg` | How Dangerous Is a Honey Badger? | PASS | — |
| 90 | Short | `OPeW46cLBOk` | Ghost Crab Growling: Teeth in Its Stomach | PASS | — |
| 91 | Short | `TSAD-WKNAzs` | What Happens If a Box Jellyfish Stings You? | PASS | — |
| 92 | Short | `A4-ltJOdto8` | Portia Spider Hunting Other Spiders | PASS | — |
| 93 | Short | `nC1QZ1GqPxg` | Can a Cassowary Kill You? | PASS | — |
| 94 | Short | `Us0zIbxiR-A` | Are Daddy Longlegs the Most Venomous Spiders? 🕷️ | PASS | — |
| 95 | Short | `Cy4Ap6Yak9A` | Do Elephants Drink Water With Their Trunks? | PASS | — |
| 96 | Short | `YPlQnGUy7A0` | Why Do Bulls Hate the Color Red? | PASS | — |
| 97 | Short | `FycW5_cOevA` | Do Lemmings Jump Off Cliffs? | PASS | — |
| 98 | Short | `eWEZhNxW8fk` | Do Goldfish Have Good Memory? | PASS | — |
| 99 | Short | `4IcgbBL0_8s` | Can Owls Turn Their Head 360? | PASS | — |
| 100 | Short | `SHQ2FzL-9Vc` | Do Porcupines Shoot Quills? | PASS | — |
| 101 | Short | `fNmRjqYh3Aw` | Do Camels Store Water in Their Humps? | PASS | — |
| 102 | Short | `Ufg_uKRnh_Y` | Can Sharks Live in Freshwater? | PASS | — |
| 103 | Short | `sp_lZedjjF4` | Do Ostriches Bury Their Heads in the Sand? | PASS | — |

## Method notes

- A PASS means the proposed title does not claim more than the video or its sourced description/script, and it does not drop a required hedge.
- Question titles PASS when the video actually answers the question (for example #33 termites: wood looks fine, screwdriver test, mud tubes; #48 dust mites: 130°F / freeze 24 hours).
- Weak automatic script matches in the join file were ignored when the script title clearly belonged to a different video.
- `#14` and `#15` are listed as UNVERIFIABLE, not FIX or PASS, because the posted cut could not be read.

