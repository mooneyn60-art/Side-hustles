# What Happens If You Leave a House Centipede in Your Bathroom? (Saturday long-form): script v1

YouTube, 16:9, posts **Sat 11/21 8 AM ET** (not scheduled by this draft). Voice **E2** (`kokoro:adam-puck`, formant 1.05, base rate +32% / pitch +2Hz as in the flagship spec; gaps 0.12 s at most, gap lint). Same v4 look as the flagship. Outline for the renderer: `skills/oh-meatball/scripts/longform-centipede-bathroom.outline.json` (same lines).

**Length:** 675 spoken words. At 165 words a minute the voice ends at 4:05, then a 20 s end screen: **about 4:25 total** (target 3:30-4:30). Timestamps are estimates; re-time from the render.

**Status:** draft for Research & QA (a different model checks every line against the live pages in the fact pack before the render). Not rendered, not scheduled. Fact pack: `skills/oh-meatball/research/facts/centipede-bathroom-sat.md` (CB# tags).

**Format (autopsy title #1, lane Q):** one typed question said in the first sentence and on the first card; the three possible answers named by 0:20 (dies? leaves? moves in?); a named source by about 0:30 (University of Kentucky); a spoken re-hook every 27-60 s; a one-line answer at the end that calls back the opening (the shoe goes back in the closet); the practical 'what to do' with its source.

**Story frame:** Meatball leaves one house centipede in his bathroom and checks on it: Night 1 at 11 PM (why bathrooms), 2 AM (the night shift, night-vision), 3 AM (the sink: the one freak-out), Day 3 (where did it go), Day 7 (what it means, what to do), then the answer at dawn. A new time and a new spot in or near the bathroom each chapter (mirror and sink, floor and tub edge, the sink at 3 AM, the under-sink cabinet in daylight, the hallway and laundry room); the cold open and the answer share the tile wall so the callback reads.

**Checks against the brief:** joke lines (no facts) at 0:40, 0:56, 1:04, 1:13, 1:32, 1:41, 2:03, 2:16, 2:31, 2:44, 3:08, 3:27, 3:38, gaps 16, 8, 9, 19, 9, 22, 13, 15, 13, 24, 19, 12 s; the cold open's 'Stop. Put the shoe down.' is a comic beat too. One freak-out (3 AM sink). BUG CAM / night-vision at about 0:31, 1:05, 1:22, 1:38, 2:22, 3:02. Spoken re-hook questions at 0:11, 0:28, 1:17, 1:53, 2:35, 2:54, 3:35, 3:43, 3:55, 3:58. No swears anywhere (QUALITY FIRST: none in the first 7 s, title, caption or on-screen text; burned captions show every spoken word, so none at all). No joke before 0:25. The bite answer is the hedged MSU line; the words 'harmless' and 'never bites' are not used.

**Animation (TASKS 'LONG-FORM ANIMATION FIXES' + QUALITY FIRST):** the centipede fills the frame at 0:00 and Meatball is big by 0:02; one shot per line plus a camera move mid-line on any line over 12 words (cuts every 5 s or less, nothing held over 8 s except the 20 s end screen); characters at least 40% of frame height; v3 lamp, flashlight and night-vision light; numbers are acted out, no charts; a re-hook card with a sound hit at each chapter; the backgrounds do not repeat more than twice (the tile wall: cold open and answer only). The bug is drawn calm; it is never hurt, squashed or shown in distress.

**Voice direction:** the `act` value on each line (curious, smug, shocked, shout, story) maps to the renderer's ACT table; fact lines carry rate +20% (= fact read), the two scared/shout freak-out lines +34% / +12Hz. Short punchy sentences, contractions everywhere.

Line format: `time` line **[source tag]** (direction) *visual (room, shot or move, card, gag)*. Tags: CB# = the fact pack; `story`, `joke`, `opinion`, `hook` = no fact.

## 0:00 Cold open: the shoe

Room: **Bathroom, 11 PM: light switch, tiled wall by the mirror**

- `0:00` What happens if you leave a house centipede in your bathroom? **[hook (typed question, no fact)]** (curious) *FRAME 0: the bathroom light snaps on and a house centipede FILLS the frame on the white tile by the mirror, already moving (legs ripple, antennae sweep). Hard cut at 0:02 to Meatball BIG in the doorway (half the frame), paw still on the switch. Sound hit on the card. CARD: WHAT HAPPENS IF YOU LEAVE IT?.*
- `0:04` You flip on the light, it's on the wall, and your paw grabs a shoe. **[story]** (story) *Camera move by 0:04: whip-pan wall to Meatball; his paw slides a sneaker off the shoe rack without looking. Push-in on the sneaker.*
- `0:09` Stop. Put the shoe down. **[story]** (shocked) *Freeze-frame: sneaker mid-swing, centipede frozen on the tile. Record-scratch SFX. The STOP card slams in. CARD: STOP.*
- `0:11` Does it dry up and die, leave, or move in? **[story (three outcomes, no fact)]** (curious) *Three quick cuts, one per outcome: a dried-up silhouette with a question mark, a silhouette walking out under the door, a silhouette with a tiny suitcase. Each lands with a pop. CARD: DIES? LEAVES? MOVES IN?.*
- `0:15` Tonight, I leave one in my bathroom and check on it all week. **[story]** (smug) *Meatball puts the sneaker in the hall closet (remember the closet: it is the callback), tapes a sign on the bathroom door: DO NOT DISTURB: SCIENCE. A wall clock reads 11:00. CARD: NIGHT 1 · 11 PM.*
- `0:20` Kentucky entomologists say house centipedes associate with the more humid areas, like bathrooms. **[CB1]** (fact: +20%) *Named source on screen by about 0:30: a drawn page labelled UNIVERSITY OF KENTUCKY ENTOMOLOGY slides in; behind it, steam curls up the mirror and the centipede sits in the damp corner by the tub. CARD: UNIV. OF KENTUCKY: HUMID AREAS, LIKE BATHROOMS.*
- `0:24` But they can often turn up in other rooms, too. **[CB1 (hedge kept)]** (fact: +20%) *Quick map of the house: little centipede pins pop up in the basement, a closet, the kitchen. Camera snaps back to the bathroom.*

## 0:28 11 PM: Why the bathroom?

Room: **Bathroom: steamy mirror and sink** · Re-hook card: **NIGHT 1 · 11 PM**

- `0:28` So why the bathroom? Short answer: water. **[story (lead-in to CB3)]** (curious) *RE-HOOK CARD 'WHY THE BATHROOM?' + sound hit. The mirror fogs; a drip falls from the faucet in slow motion. CARD: WHY THE BATHROOM?.*
- `0:31` Ohio State says centipedes lack the waxy coating that helps hold water inside the body. **[CB3]** (fact: +20%) *BUG CAM (interrupt): macro shot sliding along the centipede's back; a cartoon 'wax coat' peels off a beetle next to it for contrast, the centipede has none. CARD: NO WAXY COAT.*
- `0:36` So they lose water fast when the air is dry. **[CB3 (Sombke 2021: 'lose water rapidly at low humidity')]** (fact: +20%) *Act it out: a little water-drop meter above the centipede drains when Meatball opens the window to dry air, then refills when he shuts it. CARD: LOSES WATER FAST IN DRY AIR.*
- `0:40` Meatball's nose has the same problem. He just licks it. **[joke (no new fact)]** (smug) *Close on Meatball licking his own nose, deadpan to camera.*
- `0:43` Most centipedes that wander into a house die shortly after, from the lack of moisture. **[CB4]** (fact: +20%) *Act it out: a little parade of OTHER centipedes (stubby, different body shape) marches in under the front door and wilts one by one on a dry carpet (simple tip-over, no gore). CARD: MOST CENTIPEDES INDOORS DRY OUT.*
- `0:49` But the house centipede is the only centipede that can survive inside buildings. **[CB2]** (fact: +20%) *Cut back to the bathroom: the house centipede strolls past the wilted ones' silhouettes on the card, unbothered. Spotlight on it. CARD: THE ONLY CENTIPEDE THAT LIVES INDOORS.*
- `0:53` It can live its entire life indoors. **[CB2]** (fact: +20%) *Act it out: a tiny calendar on the bathroom wall flips through seasons while the centipede stays on the tile.*
- `0:56` Rent free. In my bathroom. I pay the water bill. **[joke (no new fact)]** (smug) *Meatball holds up a water bill, stares at the centipede, then at the camera.*
- `1:00` Missouri's Department of Conservation says they turn up indoors especially in winter. **[CB7]** (fact: +20%) *Cut: snow starts falling outside the bathroom window; the centipede is inside on the warm tile. CARD: INDOORS: ESPECIALLY IN WINTER.*
- `1:04` Great. It's November. **[joke (no new fact)]** (smug) *Meatball looks at a wall calendar on NOVEMBER, slow blink.*
- `1:05` And right where its antennae start, it has a weird little opening. **[CB5]** (fact: +20%) *BUG CAM: extreme close-up on the base of the antenna; a little opening glows. CARD: SCAPE ORGAN.*
- `1:09` Scientists think it may sense humidity. That's not proven yet. **[CB5 (hedge kept: hypothesis)]** (fact: +20%) *A drawn microscope swings in; a big question mark stamps over the word PROVEN. CARD: MAY SENSE HUMIDITY · NOT PROVEN.*
- `1:13` A built-in humidity meter. My bathroom fan doesn't even work. **[joke (no new fact)]** (smug) *Meatball flips the bathroom fan switch: it rattles and dies. Dust puffs out.*
- `1:17` So it can live in there. But what is it going to eat? **[story (re-hook)]** (curious) *The wall clock spins from 11 to 2. Lights go off. Sound hit. CARD: WHAT DOES IT EAT?.*

## 1:22 2 AM: The night shift

Room: **Bathroom floor and tub edge, lights off (night-vision)** · Re-hook card: **NIGHT 1 · 2 AM**

- `1:22` Two AM. Lights off. Bug cam on. **[story]** (curious) *RE-HOOK CARD 'NIGHT 1 · 2 AM' + sound hit. BUG CAM (interrupt): green night-vision view from the floor, timestamp ticking. CARD: BUG CAM · 2:00 AM.*
- `1:24` Connecticut's experiment station says house centipedes are nocturnal and incredibly wary. **[CB6]** (fact: +20%) *Night-vision: the centipede's head pokes out from behind the toilet, antennae testing the air, then the whole body flows out. CARD: NOCTURNAL · INCREDIBLY WARY.*
- `1:28` They patrol floors and walls in search of food. **[CB7]** (fact: +20%) *Camera tracks low along the floor behind it, then tilts up as it runs up the wall by the towel rack (walls only, not the ceiling). CARD: PATROLS FLOORS AND WALLS.*
- `1:32` Meatball patrols the kitchen the same way. Different menu. **[joke (no new fact)]** (smug) *Cutaway: Meatball in a night-vision kitchen, nose in the fridge light.*
- `1:35` On the menu: flies, crickets, moths and earwigs. **[CB8]** (fact: +20%) *Four quick cuts, one per bug, each one framed like a menu card in the night-vision shot. CARD: FLIES · CRICKETS · MOTHS · EARWIGS.*
- `1:38` Its legs are barbed to help hold prey. **[CB8]** (fact: +20%) *BUG CAM close-up: tiny barbs along one leg light up; it closes around a cardboard moth (no gore, the moth just disappears off frame). CARD: BARBED LEGS.*
- `1:41` Velcro legs. Meatball wants Velcro legs. **[joke (no new fact)]** (smug) *Meatball sticks his paw to his own leg, it does not stick, he sighs.*
- `1:43` Hunting at night, they can get trapped if they fall into a sink or bathtub. **[CB9]** (fact: +20%) *Night-vision: the centipede runs along the sink rim, one foot slips, it slides into the white basin. Slow push-in. CARD: CAN GET TRAPPED IN A SINK OR TUB.*
- `1:48` Three AM. I need the bathroom. **[story (re-hook)]** (scared: +34% / +12Hz) *Clock to 3:00. Meatball shuffles in half asleep, toothbrush in mouth, flips the light on.*

## 1:51 3 AM: The sink

Room: **Bathroom sink, light on, Meatball on the toilet tank** · Re-hook card: **NIGHT 1 · 3 AM**

- `1:51` It's in the sink. It's in my sink! **[story]** (shout: +34% / +12Hz) *FREAK-OUT (interrupt, the one big one): Meatball sees it in the basin, spits the toothbrush, launches straight up onto the toilet tank, then onto the towel rack, holding the toothbrush like a sword. Fast cuts, camera shake, sound hits. CARD: IT'S IN THE SINK.*
- `1:53` Okay. Breathe. Will it bite me? **[story]** (curious) *Meatball peeks over the towel rack, ears flat. Card spins in. CARD: WILL IT BITE YOU?.*
- `1:56` Mississippi State says bites are uncommon, and usually only if you handle it or press it against your skin. **[CB11]** (fact: +20%) *Slow push-in on the centipede sitting still in the basin; Meatball lowers the toothbrush a little. CARD: BITES ARE UNCOMMON · USUALLY ONLY IF HANDLED OR PRESSED ON SKIN.*
- `2:03` So I don't grab it. I build it a towel ramp. I'm a host now. **[story + joke (keeps the CB11 condition; Meatball's action, not advice)]** (smug) *Meatball drapes a towel from the sink rim to the floor, then backs away fast.*
- `2:08` They're not aggressive, and they flee the moment they're discovered. **[CB6]** (fact: +20%) *The centipede climbs the towel and bolts down it at full speed. CARD: NOT AGGRESSIVE · FLEES WHEN FOUND.*
- `2:12` It darts away and hides under anything. Tonight, that's my bath mat. **[CB6 + story]** (fact: +20%) *It zips across the floor and vanishes under the bath mat. The mat settles. Silence. CARD: HIDES UNDER ANYTHING.*
- `2:16` I'm not stepping on that bath mat until Thursday. **[joke (no new fact)]** (smug) *Meatball tiptoes around the mat in a wide circle and leaves.*

## 2:19 Day 3: Where did it go?

Room: **Bathroom by daylight: under-sink cabinet and baseboard** · Re-hook card: **DAY 3 · NOON**

- `2:19` Day three. Broad daylight. No centipede anywhere. **[story (re-hook)]** (curious) *RE-HOOK CARD 'DAY 3' + sound hit. Bright daylight through the window; Meatball lifts the bath mat: nothing. CARD: DAY 3 · WHERE DID IT GO?.*
- `2:22` Utah State says that by day, centipedes hide in crevices or cracks. **[CB12]** (fact: +20%) *BUG CAM (interrupt): camera slides into a gap under the sink cabinet; two antennae tips poke out of the dark, then pull back. CARD: BY DAY: HIDES IN CRACKS.*
- `2:26` And they leave no traces: no droppings, no eggs, no damage to your home. **[CB12]** (fact: +20%) *Act it out: Meatball with a giant magnifying glass checks the baseboard, the cabinet, the towels: three green check marks pop. CARD: NO DROPPINGS · NO EGGS · NO DAMAGE.*
- `2:31` Cleanest roommate I've ever had. Low bar. I'm the other roommate. **[joke (no new fact)]** (smug) *Pan to Meatball's messy side of the counter: a pile of chew toys and a dropped sock.*
- `2:35` But will it move in for good? Here's the catch. **[story (re-hook)]** (curious) *Record-scratch; Meatball turns to camera. CARD: WILL IT MOVE IN?.*
- `2:39` Unlike other centipedes, house centipedes can breed indoors, especially where it's moist or humid. **[CB10]** (fact: +20%) *Cut: a drop of water runs down the shower wall; Meatball follows it with his eyes, horror slowly building. CARD: CAN BREED INDOORS · ESPECIALLY IN DAMP ROOMS.*
- `2:44` My bathroom is basically a swamp with a mirror. **[joke (no new fact)]** (smug) *Meatball wipes the fogged mirror; it fogs right back up.*
- `2:47` And if you see them often, Penn State says that points to plenty of the bugs they eat. **[CB13]** (fact: +20%) *Act it out: one centipede on the card, then a crowd of tiny generic bugs fills in behind it like a buffet line. CARD: SEEN OFTEN? PLENTY OF PREY BUGS.*
- `2:54` So what does it mean for your house? And what do you do? **[story (re-hook)]** (curious) *The calendar flips to day 7. Sound hit. CARD: WHAT DOES IT MEAN?.*

## 2:59 Day 7: What to do

Room: **Hallway and laundry room: baseboards, sticky traps, dehumidifier** · Re-hook card: **DAY 7 · MORNING**

- `2:59` Day seven. Time to find out what it's been eating. **[story]** (smug) *RE-HOOK CARD 'DAY 7' + sound hit. Hallway by the laundry room, morning light; Meatball holds a stack of small sticky traps like playing cards. CARD: DAY 7.*
- `3:02` Ohio State says sticky traps show which bugs, and how many, are in your home. **[CB14]** (fact: +20%) *BUG CAM (interrupt): from the floor as Meatball sets traps along the baseboard; next morning a few tiny generic bugs are on them (no number shown). CARD: STICKY TRAPS: WHICH BUGS, HOW MANY.*
- `3:08` Meatball tested the first one with his own paw. **[joke (no new fact)]** (smug) *Meatball's paw is stuck to a trap; he shakes it, it flaps, he gives up.*
- `3:11` Mississippi State says focus control on the bugs they eat, and cut indoor moisture. **[CB18]** (fact: +20%) *Split screen: a small bug crossed out on the left, a water drop crossed out on the right. CARD: CONTROL THE BUGS IT EATS · CUT THE MOISTURE.*
- `3:16` Utah State says dry out damp areas, like the laundry room and the bathroom. **[CB15]** (fact: +20%) *Cut to the laundry room: Meatball mops a puddle under the washer, then wipes the bathroom floor. CARD: DRY OUT DAMP AREAS.*
- `3:21` To keep them from coming out in the open, Connecticut's experts suggest fans or dehumidifiers. **[CB15]** (fact: +20%) *Meatball drags in a dehumidifier (drawn, generic, no brand) and finally fixes the bathroom fan; it spins. CARD: FANS · DEHUMIDIFIERS.*
- `3:27` My fan works now. It only took a centipede. **[joke (no new fact)]** (smug) *Meatball stands under the spinning fan, ears blowing back, proud.*
- `3:30` And skip the bug bomb. Ohio State says those are ineffective against centipedes. **[CB16]** (fact: +20%) *A bug bomb can on the floor gets a big red NO stamp (never shown going off). CARD: BUG BOMBS: INEFFECTIVE ON CENTIPEDES.*
- `3:35` Can't live with it? Maryland Extension says escort it outdoors. **[CB17]** (fact: +20%) *Meatball holds the front door open with a little bow, a paper cup and card ready (the cup is never shown over the bug). CARD: CAN'T LIVE WITH IT? ESCORT IT OUTSIDE.*
- `3:38` Meatball held the door for ten minutes. It went back under the mat. **[joke (CB6 hides under anything; no new fact)]** (smug) *Wide-to-close: Meatball still holding the door, snow blowing in, then a cut to the bath mat with two antennae tips sticking out.*

## 3:43 The answer

Room: **Bathroom at dawn, then the hall closet** · Re-hook card: **THE ANSWER**

- `3:43` So, what happens if you leave a house centipede in your bathroom? **[callback (title question)]** (curious) *RE-HOOK CARD 'THE ANSWER' + sound hit. Same tile wall as the first frame, now at dawn; the centipede on the wall again. CARD: WHAT HAPPENS IF YOU LEAVE IT?.*
- `3:47` It hides by day, hunts by night, and points you to the damp. **[recap: CB12, CB7, CB1/CB6/CB15]** (story) *Three quick callbacks: the crack under the cabinet, the night-vision patrol, the fogged mirror. CARD: HIDES · HUNTS · POINTS TO THE DAMP.*
- `3:52` Meatball's verdict: it stays, and the fan stays on. **[opinion]** (smug) *Meatball stamps VERDICT on a sticky note and slaps it on the mirror; the fan spins. CARD: VERDICT: IT STAYS.*
- `3:55` And the shoe? Back in the closet. **[callback (story)]** (smug) *Callback to 0:05: the hall closet opens, the sneaker sits there; Meatball closes the door with his hip. The centipede's antennae wave from under the bath mat.*
- `3:58` Would you let it stay? Tell me in the comments. **[comment prompt]** (curious) *Meatball points at the viewer; comment-bubble icon. Sound hit. CARD: WOULD YOU LET IT STAY?.*
- `4:01` Next: every bug in your house, ranked. It's on the channel. **[next step (Watch next: House Bugs Ranked by Meatball)]** (story) *Meatball walks toward a door marked HOUSE BUGS RANKED; the tier board peeks through. Then the 20 s end screen. CARD: WATCH NEXT: HOUSE BUGS RANKED.*
- `4:05` [NO VOICE: 20 s end screen] *END SCREEN, nothing important in the corners: 'House Bugs Ranked by Meatball' (the flagship) + the House Centipede playlist (never a Short), subscribe button. Music only.*

---

## Title options (pick 1)

1. What Happens If You Leave a House Centipede in Your Bathroom (60 characters)
2. House Centipede in Your Bathroom? Here's What Happens (53 characters)
3. I Left a House Centipede in My Bathroom for a Week (50 characters)

Title 1 is the autopsy's typed question (#1 in the 10-video plan). With the '?' it is 61 characters, so it is written without the question mark to meet the 60-character cap; if Studio allows 61, add it back. Title 2 leads with 'house centipede in bathroom', which YouTube autocomplete shows (`postkit.py kw "house centipede in"`, 11/18). Title 3 is Meatball's story (a statement, true of the video). No banned words (TRUE or FALSE, Myth, Believe, Cartoons, Lied, Did you know), no swears, no 'harmless'.

## Description

```
House centipedes associate with the more humid areas of a building, such as bathrooms, though they can often be found in other rooms (University of Kentucky); bites are uncommon, and usually only if one is handled or pressed against the skin (Mississippi State Extension).

Meatball finds a house centipede on his bathroom wall, puts the shoe away, and checks on it for a week: at 11 PM, at 2 AM, at 3 AM in the sink, on day 3 and on day 7. Every fact comes from a university extension, a state agency or a peer-reviewed paper, listed below.

Chapters
0:00 Cold open: the shoe
0:28 11 PM: Why the bathroom?
1:22 2 AM: The night shift
1:51 3 AM: The sink
2:19 Day 3: Where did it go?
2:59 Day 7: What to do
3:43 The answer

Watch next
House Bugs Ranked by Meatball, From Harmless to Get Out: [link]

What the sources suggest: dry out damp areas such as the laundry room and bathroom (Utah State); fans or dehumidifiers to keep them from coming out in the open (Connecticut Agricultural Experiment Station); bug bombs are ineffective against centipedes (Ohio State). Always read and follow any pesticide label.

Sources
- University of Kentucky Entomology ENTFACT ef645, Centipedes and Millipedes in and Around the Home: https://entomology.mgcafe.uky.edu/ef645
- Ohio State University Extension ENT-50, Centipedes: https://ohioline.osu.edu/factsheet/ENT-50
- Utah State University Extension, Centipedes: https://extension.usu.edu/planthealth/research/centipede.pdf
- Sombke et al. 2021, The antennal scape organ of Scutigera coleoptrata, Frontiers in Zoology 18:57: https://pmc.ncbi.nlm.nih.gov/articles/PMC8567564/
- Connecticut Agricultural Experiment Station, House Centipede: https://portal.ct.gov/-/media/caes/documents/publications/fact_sheets/entomology/house_centipede_scutigera.pdf
- Missouri Department of Conservation, House Centipede: https://mdc.mo.gov/discover-nature/field-guide/house-centipede
- University of Arkansas Arthropod Museum, House centipede: https://arthropod.uark.edu/house-centipede/
- University of Wisconsin Garden Facts, Centipedes: https://hort.extension.wisc.edu/files/2014/11/Centipedes.pdf
- Mississippi State University Extension, Bug's Eye View No. 29: https://www.accessibility.extension.msstate.edu/newsletters/bugs-eye-view/2015/house-centipede-no-29
- Penn State Extension, House Centipedes: https://extension.psu.edu/house-centipedes
- Washington State University PestSense, House centipede: https://pestsense.cahnrs.wsu.edu/fact-sheet/house-centipede/
- University of Maryland Extension, Centipedes: https://extension.umd.edu/resource/centipedes

Where did you last find a house centipede, and did it get the shoe or the towel ramp?
```

Chapter times are the 165 wpm estimates; reset them from the final render (YouTube needs 0:00 first, 3+ chapters, each 10 s or longer: all met by the estimates).

## Pinned comment

> Where did you last find a house centipede, and did it get the shoe or the towel ramp?

Open question that pulls a story (MASTER_ORDERS 'Posting'), with no claim in it.

## Thumbnail brief (tools/thumbs.py, the fixed long-form look)

- Huge house centipede face on the left, Meatball reacting big on the right, the yellow 2-3 word label, the sky-blue background every thumbnail uses. No tier board (this is not a ranking video): leave out `--board`.
- Labels are questions that claim no more than the title (thumbs.py rule).
- Run from `skills/oh-meatball`:

```
python3 tools/thumbs.py one --bug centipede --label "LEAVE IT?" --pose shock --mood smug episodes/thumbs-bathroom/thumb-bathroom-A-leaveit.png
python3 tools/thumbs.py one --bug centipede --label "IN YOUR BATHROOM?" --pose nervous episodes/thumbs-bathroom/thumb-bathroom-B-bathroom.png
python3 tools/thumbs.py one --bug centipede --label "STAY OR GO?" --pose think episodes/thumbs-bathroom/thumb-bathroom-C-stayorgo.png
```

- A is the default on the post; B and C are the Test & Compare challengers. Check each phone-check/*_320.png: the label cap height must read 18 px or more at 320x180 (the script prints it). If 'IN YOUR BATHROOM?' runs under 18 px, use 'BATHROOM?'.
- Studio's brand-kit note (11/18): keep Meatball's face from touching the label.

## UNSOURCED, cut

- "Never bites" / "harmless to people" / "harmless": Banned by the brief. Penn State, Ohio State and Oklahoma State use 'harmless'; not said. The bite answer is the hedged MSU line (CB11).
- "It starves in there" / how many days it lasts with no food or water: No opened source gives a survival time for a house centipede without food or water. The only humidity-mortality numbers found are for a symphylan (Scutigerella immaculata), not a centipede. The 'dies?' outcome is asked, then answered only with sourced lines (most centipedes dry out indoors; this one can live indoors).
- "It drinks from the sink / the drips": No source says it drinks from sinks or condensation. The bathroom pull is told only as humidity (CB1, CB3, CB10).
- "It came up the drain": Drains are a Penn State harborage line already used in 4-v6 and Part 5; not used, and no source says a bathroom sink drain.
- "Bathrooms have silverfish, so that's what it eats": No source ties the bathroom to a prey list. The menu line names prey from MDC without saying they live in the bathroom.
- "Seeing one in daylight means an infestation": Only the museumpests.net sheet (prepared by Buffalo State students) says daytime sightings 'may indicate a pronounced infestation'. Weaker source; replaced by Penn State's 'seen frequently' line (CB13).
- "Its presence means your bathroom humidity is too high": Same student-prepared sheet ('elevated humidity levels'). The recap says only 'points you to the damp', resting on CB1, CB6 and CB15.
- "It senses humidity with its antennae" (as fact): Sombke 2021 calls the scape organ's job a hypothesis ('may be hypothesized to function as hygroreceptors'). Said with 'scientists think it may' and 'not proven yet'.
- "Escort it outside" in winter is safe for it: Penn State says house centipedes do not survive winters outdoors in Pennsylvania. The UMD line is said as UMD's advice only; the door gag never shows it going out.
- Wisconsin: 'originally from Mexico': Contradicts Penn State, UKY and Arkansas (Mediterranean). Not used; the CB9 sink line is the only Wisconsin claim.
- Insecticide sprays, perimeter bands, named chemicals: Sourced (OSU, UKY, Wisconsin, USU) but left out: a spray how-to needs label and safety conditions the video has no time for. Only the OSU 'bug bombs are ineffective' line is used.

## Already used (not repeated as facts or punchlines)

- Flagship 'House Bugs Ranked' centipede chapter: about 16 inches a second; runs up walls to hunt; faceted eyes; bites uncommon unless handled or pressed (MSU); fangs too small to pierce skin easily (UKY); eats cockroaches and silverfish (UKY); half pouncing, half lassoing; infestations in single digits; 'don't grab it'.
- Parts 1-3 (TikTok/Shorts): 15 pairs / 30 legs; feelers like legs, which end is the face; fast runner; venom fangs, 'almost never' stings unless grabbed; prey lists (bed bugs, baby roaches, silverfish, spiders, flies, moths, carpet beetle larvae); hunts at night; most never seen; hides in basements, cellars, bathrooms; four pairs at hatch; 3 years to grow up, up to 7 years; female back legs; don't bother spraying; dry out the damp spots.
- 4-v6 (11/7): up to 150 babies; leg snaps off; floor drains with no water trap; cement block walls; cardboard; up to 4 inches across; Mediterranean, PA 1849; hunts outside along walls in summer; can't survive winter outside up north; bite rare, 'fix the damp spots and seal the dry drains'.
- Part 4 (11/17): Guinness 1973 listing; 16 in/s, close to 1 mph; dart-stop-freeze; pounce/lasso; walls; faceted eyes; leg-floss grooming; cleans missing legs; back spiracles; eggs singly in soil; newly molted males eaten.
- Part 5 / 'centipede-5' (11/15): drops and regrows legs; body an inch, 3-4 in with legs; babies with eight legs; 3 years to grow; catches several at once; dry drains, cardboard, crawl spaces; never seen; some fall into the tub and get trapped; lots of them may mean a bigger bug problem; dry the room, fix leaks, move cardboard; won't harm pets, clothes, house; bite like a bee sting.

**Deliberate overlaps, and why they stay:**

- CB9 (can get trapped in a sink or bathtub): Part 5 said 'Some fall into your tub at night and get trapped' as a punchline. Here it is a set-up line with a new source (Wisconsin) and leads the story into the sink freak-out; the joke is new.
- CB13 (seen often = plenty of prey): Part 5 said 'Seeing lots? You may have a bigger bug problem.' Here it is Penn State's wording and is used to answer 'what it means for your house', not as a punchline.
- CB11 (hedged bite line): the brief requires it; the flagship used the same MSU sentence. Kept word for word, said once. The UKY fang line from the flagship is not repeated.
- CB15 (dry out damp areas): Parts 1-3 said 'dry out the damp'. The brief allows it only if a source says it: Utah State now says it word for word, with Connecticut's fans/dehumidifiers as the new detail.

## Source tags

- **CB1**: University of Kentucky Entomology ENTFACT ef645, Centipedes and Millipedes in and Around the Home: https://entomology.mgcafe.uky.edu/ef645
- **CB2**: University of Kentucky ef645 (as above); Ohio State University Extension ENT-50, Centipedes: https://ohioline.osu.edu/factsheet/ENT-50 ; Utah State University Extension, Centipedes: https://extension.usu.edu/planthealth/research/centipede.pdf
- **CB3**: Ohio State ENT-50 (as above); Sombke, Rosenberg, Hilken & Müller 2021, Frontiers in Zoology 18:57, The antennal scape organ of Scutigera coleoptrata: https://pmc.ncbi.nlm.nih.gov/articles/PMC8567564/ ; Utah State (as above)
- **CB4**: University of Kentucky ef645 (as above); Ohio State ENT-50 (as above)
- **CB5**: Sombke et al. 2021, Frontiers in Zoology (as above)
- **CB6**: Connecticut Agricultural Experiment Station (Dugas), House Centipede fact sheet: https://portal.ct.gov/-/media/caes/documents/publications/fact_sheets/entomology/house_centipede_scutigera.pdf
- **CB7**: Missouri Department of Conservation, House Centipede field guide: https://mdc.mo.gov/discover-nature/field-guide/house-centipede
- **CB8**: Missouri Department of Conservation (as above); University of Arkansas Arthropod Museum, House centipede: https://arthropod.uark.edu/house-centipede/
- **CB9**: University of Wisconsin Garden Facts XHT1113 (Pellitteri), Centipedes: https://hort.extension.wisc.edu/files/2014/11/Centipedes.pdf
- **CB10**: Mississippi State University Extension, Bug's Eye View No. 29, House Centipede: https://www.accessibility.extension.msstate.edu/newsletters/bugs-eye-view/2015/house-centipede-no-29
- **CB11**: Mississippi State Bug's Eye View No. 29 (as above); University of Kentucky ef645 (as above)
- **CB12**: Utah State University Extension, Centipedes (as above)
- **CB13**: Penn State Extension, House Centipedes: https://extension.psu.edu/house-centipedes
- **CB14**: Ohio State ENT-50 (as above); Penn State Extension (as above)
- **CB15**: Utah State (as above); Connecticut Agricultural Experiment Station (as above); University of Arkansas (as above); Washington State University PestSense, House centipede: https://pestsense.cahnrs.wsu.edu/fact-sheet/house-centipede/
- **CB16**: Ohio State ENT-50 (as above)
- **CB17**: University of Maryland Extension, Centipedes: https://extension.umd.edu/resource/centipedes
- **CB18**: Mississippi State Bug's Eye View No. 29 (as above)

## Notes for the main session

- `skills/oh-meatball/data/posted.csv` still lists `longform-house-centipede-v2.mp4` ('Don't Squish the 30-Legged Bug in Your Bathroom (Here's Why)') for YouTube **Sat 11/21 08:00**, the same slot. Studio's 11/18 note gives that slot to this video; the old 3D long-form needs pulling or moving (and Metricool checking) before this one is scheduled.
- The renderer `tools/drawn_ranked.py` is built for the six-suspect flagship (tier board, suspect chips, hard-coded per-line directions in DIRECT). This outline keeps the flagship's JSON shape and adds an optional `act` per line for the voice direction; the build needs a SHOTS recipe for these lines (bathroom-only set, night-vision BUG CAM, the sink freak-out).
- No swears were used. MASTER_ORDERS allows mild words in long-forms after 0:25, but QUALITY FIRST bans them from on-screen text and the burned captions show every word.
