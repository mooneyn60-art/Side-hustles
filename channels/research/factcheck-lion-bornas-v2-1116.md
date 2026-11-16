# Fact-check: longform-lion-bornas-v2 (full live-source pass)

**Script:** `/workspace/drafts/longform-lion-bornas-v2.md`  
**Fact pack:** `/workspace/drafts/facts/lion-bornas.md` (LB1–LB43)  
**Checked:** Sun Nov 15, 2026, ~7:30 PM ET (America/New_York)  
**Scope:** Every spoken claim, including speed, roar, lifespan, cub-death figures and disagreements, and the Kruger / Tanzania safety lines with their conditions. Scripts were not edited.

## Blocking issues

**None on the biology numbers.** Speed, roar, lifespan, and cub-death disagreements are all spoken as pairs (or with an explicit “another source” / “depending on the source”). Kruger keeps “unless you’re in a designated area,” body inside, and doors closed. Two recommended fixes: (1) the Tanzania 563 / 308 figures are from a 2005 paper covering 1990 through about then, but s9.l2 says “from 1990 on”; (2) s1.l8’s “mostly among close relatives” was not on the live SDZWA pages opened today.

## Date conflict to reconcile (do not book yet)

MASTER_ORDERS line 217 still says **dog Sat 12/12, wolf Sat 12/19**. That does not line up with the rest of the calendar as it stands tonight (all times America/New_York):

| Source | What it currently says |
|---|---|
| MASTER_ORDERS line 217 | Dog 12/12, wolf 12/19 |
| MASTER_ORDERS line 69 | Dog and wolf "by the data's rank" on **12/19 and 12/26** |
| Lion v2 itself (checks section) | Social Studio has **lion on 12/12 as the fallback** and **dog on 12/19**. This file does not change that. |
| Side-hustles `packaging/related-video-rule.md` (cited in the dog draft) | Dog on **Sat 12/19 08:00** |
| Dog long-form and dog-teasers drafts | **12/12 vs 12/19 is pending.** Ready by Wed 12/9. Do not book either date. |
| Polar / end-screen note in lion v2 | Polar build `end_label` still says **Sat 11/28**, but `posted.csv` (as cited in the dog-teasers draft) lists the house-cat long-form live Fri 11/13 17:00, and polar booked **Sat 12/5 08:00**. 11/28 looks stale. |

**Ask Claude / Social Studio to pick one Saturday stack and write it in one place.** Until that call is in: do not book 12/12 or 12/19, and do not treat 11/28 as a live lion date without checking the current calendar.

## Verdict counts

| Action | Count |
|---|---|
| Pass (spoken fact lines) | 48 |
| Fix (recommended) | 2 |
| Fix (optional hedge) | 2 |
| Cut | 0 |
| Jokes (all Pass) | 14 |
| Unsafe-to-imitate | 0 |

Do **not** use San Diego Zoo’s public-page “17 years on average” (unlabelled wild vs zoo). The script correctly leaves it out.

## Sources opened live this assignment (15 Nov 2026)

1. [Smithsonian’s National Zoo, Lion](https://nationalzoo.si.edu/animals/lion)
2. [San Diego Zoo, Lion (public page)](https://sandiegozoo.org/animals/lion) — and the saved extract at `/workspace/drafts/facts/.lion-src/sdz.txt`, re-checked today
3. [SDZWA fact sheet: Summary](https://ielc.libguides.com/sdzg/factsheets/lions/summary)
4. [SDZWA fact sheet: Reproduction & Development](https://ielc.libguides.com/sdzg/factsheets/lions/reproduction)
5. [SDZWA fact sheet: Behavior & Ecology](https://ielc.libguides.com/sdzg/factsheets/lions/behavior)
6. [SDZWA fact sheet: Diet & Feeding](https://ielc.libguides.com/sdzg/factsheets/lions/diet)
7. [SDZWA fact sheet: Population & Conservation](https://ielc.libguides.com/sdzg/factsheets/lions/population)
8. [Panthera, Lion](https://panthera.org/cat/lion)
9. [IUCN Red List, *Panthera leo*](https://www.iucnredlist.org/species/15951/259030422)
10. [SANParks, Kruger National Park — Vital Information](https://www.sanparks.org/parks/kruger/useful-information/vital-information)
11. [Packer et al. 2005, *Nature*, PubMed](https://pubmed.ncbi.nlm.nih.gov/16107828/)
12. [Bauer et al. 2015, *PNAS*, PubMed](https://pubmed.ncbi.nlm.nih.gov/26504235/)

---

## 0–1. Day one and the hiding place

| Line | Claim (quoted) | Pack | Verdict | Action | Live source quote / note | Fix |
|---|---|---|---|---|---|---|
| s0.l1, s11.l4 | "You weigh about three pounds" | LB2 | Verified | **Pass** | San Diego Zoo: "Weight at birth: about 3 pounds (1.4 kilograms)." SDZWA also lists 1.5 kg (3.3 lb); the script stays with "about three" from the Zoo page and does not flatten the two. | — |
| s0.l2 | "Your coat has light spots. They fade as you grow." | LB5 | Verified | **Pass** | Smithsonian, live: "Young lions have light spotting on their coats that disappears as they grow." | — |
| s0.l3 | "Up to 80 percent of lion cubs die before they turn two." | LB9 | Verified | **Pass** | Smithsonian, live: "Due to dangers, including starvation during times of food shortage and attacks by male lions taking over prides, up to 80 percent of lion cubs die within their first 2 years of life." The other figure (average 60% in year one) is spoken at s2.l1. Good. | — |
| s1.l1 | "Your mother carried you for about three and a half months. She usually has one to four cubs, and keeps you away from the pride until you're six to eight weeks old." | LB1, LB3 | Verified | **Pass** | Smithsonian: "Females usually give birth to one to four cubs after a gestation of about 3 1/2 months." SDZWA: "Remain separate from pride members until cubs are 6-8 weeks old." San Diego Zoo’s “Almost 4 months” / hidden “four to six weeks” (mobility, used at s1.l6) are not flattened into this line. | — |
| s1.l5–l6 | Carried "by the back of your neck." Hidden "until you can get around on your own, at about four to six weeks." | LB4 | Verified | **Pass** | SDZWA: "Hides cubs until mobile at 4-6 weeks of age" and "Moves by picking cubs up by back of their necks." | — |
| s1.l7, s1.l11 | Crèche "Usually four to ten. Sometimes more than twenty-five." "in a big crèche, young cubs compete with older, bigger ones, and the youngest die most often." | LB6 | Verified | **Pass** | SDZWA: "Cubs ‘pooled’ to form a crèche Usually 4-10 cubs, but may be more than 25 cubs" and "In very large crèches, young cubs must compete with larger, older cubs Youngest cubs have highest mortality." | — |
| s1.l8 | "Lionesses nurse each other's cubs, mostly among close relatives." | LB7 | Partly verified | **Fix** | Live SDZWA summary, today: "Females nurse one another's cubs." Live reproduction page: "Communally nurse cubs All lactating lionesses typically participate Cubs suckle from any lactating female, though females try to give milk primarily to their own young (Pusey and Packer 1994)." The pack’s “Most common among closely related females” / “allosuckling” wording was **not** on the live fact-sheet pages opened this session. | Corrected line: "Lionesses nurse each other's cubs." URL: https://ielc.libguides.com/sdzg/factsheets/lions/summary Quote: "Females nurse one another's cubs." Drop “mostly among close relatives” unless a live page that actually says it is re-opened. |
| s1.l9 | "Weaned cubs may even steal milk from nursing females for up to twelve months." | LB8 | Verified | **Pass** | SDZWA: "Weaned cubs may steal milk from lactating females for up to 12 months (Pusey and Packer 1994; West and Packer 2013)." "May" is kept. | — |

---

## 2. The odds (cub-death disagreement)

| Line | Claim (quoted) | Pack | Verdict | Action | Live source quote / note | Fix |
|---|---|---|---|---|---|---|
| s2.l1 | "Depending on the count, up to 80 percent of cubs die by age two, or on average 60 percent in the first year alone." | LB9, LB10 | Verified | **Pass** | Smithsonian 80% / first 2 years, as above. SDZWA, live: "On average, 60% of cubs die within the first year of life (West and Packer 2013)." Both figures, both time windows, "depending on the count" / "on average." Not flattened. | — |
| s2.l2 | "It's higher in some places, like the Serengeti and Kruger." | LB10 | Verified | **Pass** | SDZWA: "Higher in some locations (e.g., Serengeti and Kruger National Parks)." | — |
| s2.l4–l6 | Causes: "infanticide, abandonment after a takeover, starvation, and disease." Buffalo and elephants "occasionally gore or trample cubs." "leopards, hyenas, and other lions all hunt cubs." | LB11 | Verified | **Pass** | SDZWA: "Common causes: infanticide (or abandonment after takeover), starvation, and disease (West and Packer 2013)" and "Buffalo and elephant occasionally gore or trample lion cubs Predators (cubs) E.g., leopards, hyenas, other lions." | — |
| s2.l7 | "Make it to your first birthday, and the death rate drops below 20 percent." | LB10 | Verified | **Pass** | SDZWA: "After reaching one year, mortality declines to less than 20% (Packer et al. 2001)." | — |

---

## 3. The takeover

| Line | Claim (quoted) | Pack | Verdict | Action | Live source quote / note | Fix |
|---|---|---|---|---|---|---|
| s3.l1 | "They hold it for about two years on average, often until another group throws them out." | LB12 | Verified | **Pass** | Smithsonian, live: "Adult males that are fortunate enough to achieve residency within a pride hold tenure for an average of two years, often leaving due to eviction by another coalition of males." (s8.l7 later uses the SDZWA 2–3 year average; the two are close and not flattened into one number on this line.) | — |
| s3.l2 | "when new males take over, they will kill all cubs that cannot run from them." | LB12 | Verified | **Pass** | Smithsonian: "Males entering a new pride will kill all cubs that cannot run from them." "Will," not "may," matches the source. | — |
| s3.l3 | "In the Serengeti, that's more than a quarter of all cubs. It's less common elsewhere." | LB13 | Verified | **Pass** | SDZWA: "Frequent in Serengeti More than 1/4 of all cubs are killed by invading males (Sunquist and Sunquist 2002) Less frequent in other areas." | — |

---

## 4. Hunting school (speed, success)

| Line | Claim (quoted) | Pack | Verdict | Action | Live source quote / note | Fix |
|---|---|---|---|---|---|---|
| s4.l3 | "Males join in rarely: in as few as 3 to 4 percent of hunts by one count, and under 10 percent of the time by another." | LB22 | Verified | **Pass** | SDZWA diet: "Males take part in as few as 3-4% of hunts (Wilson and Mittermeier 2009)." San Diego Zoo: "they hunt less than 10% of the time." Two measures kept apart ("of hunts" vs "of the time"). | — |
| s4.l4 | "You have to learn which prey to pick, and when to go. By about two, lionesses are competent hunters." | LB17 | Verified | **Pass** | SDZWA: "Must learn Which prey are appropriate How to time an attack (not rush prey too soon) By 2 years of age, lionesses are competent hunters (Sunquist 2002)." | — |
| s4.l5 | "A lioness can sprint at up to 33, or up to 37, miles an hour, depending on the source, and only over 100 to 200 metres." | LB18 | Verified | **Pass** | San Diego Zoo, live: "A lioness can sprint at up to 33 miles (53 kilometers) per hour." SDZWA summary, live: "Bursts of speed up to 45-60 km/hr (24-37 mph) for short distances (100-200 m)." Diet page of the same sheet converts the same 45–60 km/h as **28–37 mph**. "Up to 37" is the shared ceiling; the 100–200 m condition is spoken. The summary’s “24-37” looks like a conversion typo (45 km/h is ~28 mph, not 24). Do not use 24 as a spoken figure. | — |
| s4.l6 | "In one Kalahari count, 38 percent of hunts worked. In the Serengeti, 23. In Etosha, 15." | LB19 | Verified | **Pass** | SDZWA diet, live: "Success rates High: 38%, Kalahari (Eloff 1984) Moderate: 23%, Serengeti (Schaller 1972) Low: 15%, Etosha National Park (Stander 1972)." The fact sheet still cites **Stander 1972**; the script’s on-screen tag already corrects this to **Stander 1992** (the sheet cites Stander 1992 correctly for the 5% scavenging figure on the same page). The 15 / 23 / 38 figures themselves match the live sheet. | — |
| s4.l7 | "Lions hunting alone do worse than lions hunting in a group." | LB19 | Verified | **Pass** | SDZWA: "Lions hunting alone are less successful than those hunting with several other lions." | — |
| s4.l8 | "lions take prey as big as buffalo and giraffes, and one lion can bring down an animal up to twice its own weight." | LB21 | Verified | **Pass** | San Diego Zoo: "Lions have been spotted taking down prey as large as buffalo and giraffes!" SDZWA: "Single lions can bring down animals up to twice their own weight (Estes 2012)." | — |
| s4.l9 | "they risk being badly injured while bringing prey down." | LB20 | Verified | **Pass** | SDZWA: "Risk of being severely injured while subduing prey (West and Packer 2013)." | — |

---

## 5–7. Neighbours, kicked out, taking a pride (roar)

| Line | Claim (quoted) | Pack | Verdict | Action | Live source quote / note | Fix |
|---|---|---|---|---|---|---|
| s6.l1 | "Lions steal kills from hyenas, leopards, and other predators. And at times, they lose their own to hyena groups." | LB24 | Verified | **Pass** | Smithsonian, live: "Lions also steal kills from hyenas, leopards and other predators. At times, they may lose their own catches to hyena groups." | — |
| s6.l2–l3 | "females may lose up to 20 percent of their kills to spotted hyenas, and another 17 percent to other lions when the pride's males are away." "A male nearby helps protect the kill." | LB23 | Verified | **Pass** | SDZWA: "Presence of a male helps protect kills from scavenging by spotted hyenas (Wilson and Mittermeier 2009) Females may lose up to 20% of kills to spotted hyenas (Cooper 1991) and another 17% to other lions when male pride members are absent." | — |
| s6.l5 | "Lions scavenge too. It can be as little as 5 percent of their food in dry places, or as much as 53 percent on open plains." | LB25 | Verified | **Pass** | SDZWA: "May be as low as 5% of food in arid environments with lower prey densities (Stander 1992) May be as high as 53% of food (open plains habitat) (Schaller 1972)." | — |
| s7.l1 | "Young males are driven out once they're big enough to compete with the dominant males, usually between two and four years old." | LB26, LB27 | Verified | **Pass** | Smithsonian: "Young males are driven from their prides when they grow large enough to compete with the dominant males (usually between the ages of 2 and 4)." SDZWA: "Males generally leave natal area at 2-3 years of age." Both windows are in the tag; the spoken "usually between two and four" follows Smithsonian and covers 2–3. | — |
| s7.l2 | "Females usually stay in their mothers' prides for life, unless food runs short." | LB26 | Verified | **Pass** | Smithsonian: "Females usually stay in their mothers' prides for life, unless food scarcity forces them out." | — |
| s7.l3–l4 | Nomads "following the migrating herds: usually young males, in pairs or small groups, often related." "Nomadic males must hunt alone or scavenge." | LB28 | Verified | **Pass** | San Diego Zoo: "Lions that do not live in prides are called nomads, and they range far and wide while following migrating herds of large game. Nomads are generally young males, roaming in pairs or small groups and often related to one another." Smithsonian: "Nomadic males must hunt alone or scavenge from other animals." | — |
| s7.l6 | "Nomads have a high natural death rate." | LB29 | Verified | **Pass** | SDZWA population page: "Nomadic lions (which experience high natural mortality) often killed (Ikanda and Packer 2008)." No invented percentage. | — |
| s7.l7 | "Males travel two to three times farther from home than females, though in Kruger, most young male groups stayed close." | LB27 | Verified | **Pass** | SDZWA: "Males disperse from their natal area; travel 2-3 times farther than females (Dolrenry et al. 2014, except as noted) Exception: Kruger National Park (Funston et al. 2003) 80% of young male coalitions remained close to natal territories." "Most" fairly covers 80%. | — |
| s7.l9 | "you find your brothers and cousins, and you go looking for somebody else's pride." | LB26 | Verified | **Pass** | Smithsonian: "They create coalitions, usually with brothers and cousins, and search for a pride to take over." | — |
| s8.l1 | "Males team up in groups of two to four, sometimes as many as eight, to compete for mates." | LB35 | Verified | **Pass** | Panthera, live: "Prides of two to four individuals (or as many as eight) join forces to compete for mates." The script correctly says male groups / team-ups, not “prides,” which is Panthera’s sloppy caption word. | — |
| s8.l2 | "A new male has to fight the males already there. He gets driven off, or he pushes them out." | LB30 | Verified | **Pass** | San Diego Zoo: "When a new male tries to join a pride, he must fight the males already there. The new male is either driven off or succeeds in pushing out the existing males." | — |
| s8.l3 | "Bigger groups win time. They can hold a pride more than twice as long as a single male or a pair." | LB31 | Verified | **Pass** | SDZWA: "Larger groups can ‘hold tenure’ more than twice as long as a single male or pair of males (Wilson and Mittermeier 2009)." | — |
| s8.l4, s10.l0–l1 | Pride "several lions to as many as 40." "Lions are the world's most social cats." Pride is lionesses, mothers, sisters, cousins, cubs, and a few unrelated adult males. | LB34, LB26 | Verified | **Pass** | Smithsonian: "Lions are the world's most social felines. They live in groups of related females, called prides, which may comprise several to as many as 40 individuals…" San Diego Zoo’s 3–30 range is correctly unused (one source per disagreement). San Diego Zoo: "A pride can have 3 to 30 lions and is made up of lionesses (mothers, sisters, and cousins), and their cubs," plus resident males — used only for the family makeup, not the count. | — |
| s8.l6 | "it carries up to three to five miles, depending on the source." | LB33 | Verified, slight wording | **Fix (optional)** | Smithsonian, live: "both males and females mark their territories by roaring — which can be heard up to five miles away." San Diego Zoo: "A lion’s roar can be heard up to 3 miles (4.8 kilometers) away." SDZWA: "May be heard as far as 5 km (3 miles) away, under certain conditions." The spoken 3-to-5-mile pair is Smithsonian 5 vs Zoo/SDZWA 3. The tag’s “SDZWA (5 km)” is the same 3 miles, not a third figure. | Optional: add “under some conditions” (SDZWA). Not blocking. Do not treat 5 km as 5 miles. |
| s8.l7 | "Males stay with a pride two to three years on average, and hold one and father cubs for only about six years in a whole lifetime." | LB31, LB32 | Verified | **Pass** | SDZWA: "Remain with pride, on average, only 2-3 years; may be less" and "Hold pride tenure and sire offspring for only about 6 years during lifetime (Funston et al. 2003)." | — |

---

## 8. Time, and people (lifespan, Tanzania, Kruger)

| Line | Claim (quoted) | Pack | Verdict | Action | Live source quote / note | Fix |
|---|---|---|---|---|---|---|
| s9.l1 | "A wild lioness may live up to about 16 years, and males rarely past 12, though another source puts both ceilings higher." | LB40 | Verified | **Pass** | Smithsonian, live: "In the wild, a lioness may live up to 16 years, but males rarely live past the age of 12." SDZWA summary, live: "Wild populations: median life expectancies unknown; males rarely live past 16 years and females rarely live past 18 years (maximum)." Disagreement is spoken. San Diego Zoo’s unlabelled “17 years on average” is correctly unused. | — |
| s9.l2 | "In Tanzania, lions killed more than 563 people from 1990 on, and injured at least 308. Attacks peaked at harvest time." | LB39 | Needs a date window | **Fix** | Packer et al. 2005, *Nature*, live abstract: "they have killed more than 563 Tanzanians since 1990 and injured at least 308. Attacks have increased dramatically during this time: they peak at harvest time each year and are most frequent in areas with few prey apart from bush pigs… starting point for devising strategies to reduce the risk to rural Tanzanians of lion attacks." The 563 / 308 figures are the count in that paper (about 1990–2005), not an open-ended total “from 1990 on” as of 2026. The line is about rural Tanzania, not safari visitors, and is not applied to Kruger tourists. Harvest-time condition is spoken. | Corrected line: "In Tanzania, a mid-2000s count found lions had killed more than 563 people since 1990, and injured at least 308. Attacks peaked at harvest time." URL: https://pubmed.ncbi.nlm.nih.gov/16107828/ Quote: "they have killed more than 563 Tanzanians since 1990 and injured at least 308." Optional extra hedge (not required if the date window is fixed): keep “rural” in view so this is never applied to park visitors. |
| s9.l3 | "If you visit Kruger National Park, the park's rules say to stay in your vehicle unless you're in a designated area, keep every part of your body inside, and keep the doors closed." | LB41 | Verified | **Pass** | SANParks Vital Information, live: "Visitors must remain in their vehicles unless in a designated area. Remember that no part of the body may protrude from a window or sunroof or any other part of the vehicle. Vehicle doors should be closed at all times." "Unless you're in a designated area," body inside, and doors closed are all spoken. "The park's rules" keeps the scope. | — |
| s9.l4 | "Meatball booked a Kruger trip. Noodle had to stay home. Kruger's rules say no pets." | LB41 | Verified | **Pass** | SANParks, live: "No live animal (domestic or wild) may be brought into, or removed from the Kruger National Park. That is why NO PETS ARE ALLOWED here." Joke does not invent a rule. | — |
| s9.l5 | "Lions are listed as Vulnerable, with about 23,000 mature lions left, and falling." | LB37 | Verified | **Pass** | IUCN Red List, live: "Vulnerable" under A2abcd; "Population trend Decreasing Number of mature individuals 23,000." Assessment date on the page is February 2023 (published 2024). "About 23,000" and "mature" are kept. Smithsonian’s “estimated 20,000” and Panthera’s “about 24,000 lions remaining” (not labelled mature) are correctly unused. | — |
| s9.l7 | "Lion numbers are falling everywhere except four southern countries: Botswana, Namibia, South Africa, and Zimbabwe." | LB38 | Verified | **Pass** | Bauer et al. 2015, live abstract: "We found a striking geographical pattern: African lion populations are declining everywhere, except in four southern countries (Botswana, Namibia, South Africa, and Zimbabwe)." | — |
| s10.l2 | "You rest up to 21 hours a day. Lying around counts." | LB42 | Verified | **Pass** | San Diego Zoo: "long bouts of lying around that total up to 21 hours!" SDZWA: "May rest up to 20-21 hours per day, on average (Schaller 1972)." "Lying around counts" matches the Zoo wording. | — |
| s10.l4 | "lions are at the top of the food chain." | LB43 | Verified | **Pass** | San Diego Zoo: "lions are at the top of the food chain." | — |
| s11.l1–l3 | Verdict recap: 80% by age two, new males, hyenas, the road for males; most social cats; top of the food chain. Opinion closer. | several | Verified | **Pass** | Recap only; the 80% figure is still the Smithsonian one already sourced. "Our verdict, and it's an opinion" is labelled as opinion. | — |

---

## Jokes (every joke; all Pass)

No joke adds a speed, roar, lifespan, or cub-death number, or unsays a Kruger / Tanzania condition.

| Line | Joke | Action | Note |
|---|---|---|---|
| s1.l4 | Meatball hid in the laundry basket; Sauce sat on the lid. | **Pass** | Character gag. |
| s1.l10 | Meatball tried the milk-steal on Noodle's water bowl. | **Pass** | After the sourced "may steal milk" line; no new claim. |
| s2.l3 | Bike helmet indoors. | **Pass** | After both cub-death figures, not on them. No invented survival tactic. |
| s2.l8 | First-birthday party; Noodle ate the cake. | **Pass** | After the <20% line, not a "the cake saved him" claim. |
| s3.l4 | No-new-males sign on the cat flap. | **Pass** | No infanticide joke about a real animal. |
| s4.l10 | Meatball tackled a beanbag twice his weight. | **Pass** | After the 2×-weight line; the beanbag winning is a gag, not a hunt-success number. |
| s5.l0–l1 | Halfway stamps; comment prompt. | **Pass** | Not a fact claim. |
| s6.l4 | Spatula-guarded steak; Noodle has it. | **Pass** | No 20% / 17% change. |
| s6.l6 | "Hell of a neighbourhood." | **Pass** | Tone, no number. |
| s7.l8 | Sauce took the chair; juice box in the driveway. | **Pass** | No nomad-mortality number. |
| s8.l5 | Coalition with Sauce; coalition of one. | **Pass** | No 2-to-4 / 8 change. |
| s8.l8 | "Six years. Out of a whole damn life." | **Pass** | Mild word on the already-sourced six-year tenure, not a new figure. |
| s9.l6 | Meatball counted one cardboard lion. | **Pass** | After the IUCN line, not on it. |
| s10.l3, s11.l5–l6 | Sauce in the chair; cardboard crown; stamps. | **Pass** | Character close. |

---

## Disagreements checklist

| Topic | How the script handles it | Verdict |
|---|---|---|
| Cub deaths: 80% by age 2 (Smithsonian) vs avg 60% in year 1, higher in Serengeti/Kruger, then <20% (SDZWA) | Both spoken at s2.l1, plus the place and after-year-one lines | **Pass** |
| Speed: 33 mph (Zoo) vs up to 37 mph over 100–200 m (SDZWA) | Both ceilings + the distance condition | **Pass** |
| Roar: 5 miles (Smithsonian) vs 3 miles / 5 km (Zoo, SDZWA) | "Up to three to five miles, depending on the source" | **Pass** (optional “under some conditions”) |
| Lifespan: lioness 16 / males rarely past 12 (Smithsonian) vs males 16 / females 18 max (SDZWA) | "Up to about 16… rarely past 12, though another source puts both ceilings higher." Zoo “17 years on average” unused | **Pass** |
| Pride size: several to 40 (Smithsonian) vs 3–30 (Zoo) | Uses Smithsonian only | **Pass** |
| Male hunt share: 3–4% of hunts vs <10% of the time | Both, with the different units kept | **Pass** |

