# Can cats eat turkey — packaging draft

**DRAFT PENDING a dedicated cat-turkey fact pack, a second-model check, a script, and a schedule slot.** There is no `cat-turkey` research file, script, or `posted.csv` row in the skills repo on this pass. Dog-turkey (`#70`, `yt-dog-turkey-v6`) is already posted (Thu 11/12). Do not invent cat-only claims. No repo edit, commit, push, or post from this file.

## What the repo actually has

`skills/oh-meatball/research/facts/dog-turkey.md` (opened 2026-11-12) and `dog-turkey-check.md` (cleared 2026-11-12, with wording changes). Useful overlap, quoted only as that pack already wrote it:

- DOGT1, ASPCA Thanksgiving Safety Tips: "If you do decide to feed your pet a small bite of turkey or other meat, make sure it's boneless and fully cooked." The same paragraph opens with "we recommend sticking to your pet's normal diet on Thanksgiving." The pack's note: "Pets here means cats and dogs. Quote the page again before it goes on screen."
- DOGT2, same page: "Raw or undercooked turkey may contain salmonella bacteria and poultry bones can be a major choking hazard."
- DOGT3, same page, trash: empty it during the day or keep the pet out of that area. The pack quotes the line before it: "your garbage can fill up with bones, chocolate, onions and plenty of other holiday hazards." That is a trash-hazards list, not a cat-onion or cat-chocolate fact pack.
- DOGT4, FDA "Keep Your Dogs and Cats Safe From Holiday Hazards" (content current as of 12/17/2025): the carcass line is about dogs ("Dogs, especially, are notorious for helping themselves to the turkey carcass…"). The wrap-and-bin line says "a trash bin that your pets can't get into."
- DOGT6, same FDA page, says "your pet" for fatty scraps and roasted turkey skin; the cleared dog-turkey check keeps "can upset the stomach" and the FDA's "don't give," and leaves out "life-threatening."
- The pack's coverage rule: "The ASPCA turkey line says 'your pet' (the page speaks of 'your cat and dog'); the FDA trash and carcass line says 'your dog'; the FDA skin line says 'your pet'." Use "dog" only where the FDA says dog.
- Do not use "A Feast Fit for a King" (mix turkey, sweet potatoes, green beans, drizzle of gravy). The pack forbids that section because it conflicts with the bouillon/gravy sodium line.
- Do not use the AVMA splinter line in packaging. The second-model check removed it from the dog-turkey description because the checker could not open the AVMA page.

The Social Studio audit used the same ASPCA Thanksgiving page (opened 11/15) as a pets page, not a cats-only page. This file does not take extra audit claims (for example a standalone onions-and-garlic line) that are not already written into the repo pack.

## Facts still needed (do not fill these by guessing)

1. A dedicated `research/facts/cat-turkey.md` that re-opens the live ASPCA and FDA pages and quotes every line as it applies to cats, with the date opened.
2. A second-model check of that pack and of any script, separate from the 11/12 dog-turkey check.
3. Whether a cat-specific carcass or trash behavior line exists. Do not reuse "dogs are notorious for the turkey carcass" as a cat fact.
4. Whether processed turkey (bacon, ham, lunch meat, sausage, pepperoni, deli slices — all of which appear in `postkit.py kw` suggestions) is covered. If the pages do not say, do not tag or title those foods.
5. Onion, garlic, gravy/bouillon, and chocolate as they apply to cats. Those may belong in their own videos. Do not pile them into this description without a checked quote.
6. A safe-amount line: the dog pack found none. Do not invent one for cats.
7. Episode number, Sauce gag that adds no danger or dose, schedule slot (Thanksgiving is Thu 11/26/2026; Shorts dates 11/22–11/24 and 11/26–12/04 are empty in `posted.csv`), and a Related-video target.

Until that pack exists, the metadata below is a holding draft that only restates DOGT1 and DOGT2, plus the "pets means cats and dogs" note. It is not cleared for posting.

## YouTube title

`If Cats Eat Turkey: Boneless and Fully Cooked, Says the ASPCA 🐱 (Things Living In Your House)`

94 UTF-16 units. Statement form (a leading `Can Cats Eat Turkey?` would fail lint). Searched words (`cats eat turkey`) sit in the first 40, matching the dog-turkey pattern `If Dogs Eat Turkey:…`. "Your cat" is not the lead; searched words won under title-formula clause 10, same choice as `#70`. No episode number is assigned. Lint (`/workspace/packaging/lint-specs/title-cats-turkey.json`): pass, 0 fail, 1 hashtag WARN, title 94 of 100. (That stub still had a couple of unmatched food tags; the tag list in this file is the corrected one.)

## YouTube description

Can cats eat turkey? The ASPCA Thanksgiving page, already quoted in the dog-turkey fact pack, recommends sticking to your pet's normal diet on Thanksgiving. If you do decide to feed your pet a small bite of turkey or other meat, it says to make sure it is boneless and fully cooked. Raw or undercooked turkey may contain salmonella, and poultry bones can be a major choking hazard. That pack notes that "pets" on this line means cats and dogs. This draft does not add a safe amount, a carcass habit for cats, or any food the pack did not check. Quote the live page again in a cat-turkey pack before this goes on screen. When in doubt, ask your vet.

#cancatseatturkey #turkeybones #thanksgivingpets #meatballmyths #shorts

Sources: skills/oh-meatball/research/facts/dog-turkey.md (DOGT1, DOGT2) and research/facts/dog-turkey-check.md; ASPCA, Thanksgiving Safety Tips, https://www.aspca.org/pet-care/general-pet-care/thanksgiving-safety-tips (opened in that pack on 2026-11-12). General information, not veterinary advice.

## Tags (10, each ≤30 characters, from `postkit.py kw`)

Keyword file: `/workspace/packaging/kw/kw-studio-assignments.csv` (run 2026-11-15, America/New_York). Every tag is a query this holding draft can actually answer (turkey, turkey meat, bones) or a series/brand tag. Processed-meat suggestions (ham, bacon, lunch meat, sausage, pepperoni, deli) are omitted until a pack covers them. `can cats eat turkey carcass` is omitted because the FDA carcass line is about dogs. `can cats eat turkey bones raw or cooked` is 39 characters and over the cap.

1. can cats eat turkey
2. can cats have turkey
3. can cats eat turkey meat
4. can cats eat turkey breast
5. can cats eat turkey bones
6. do cats eat turkey bones
7. can cats eat bones
8. can cats eat raw turkey bones
9. things living in your house
10. Meatball Myths

Tag 8 stays only if the script repeats the ASPCA raw/undercooked line. If the cat pack later drops raw, drop the tag.

## TikTok caption (Studio shape; pending the hashtag decision)

```
can cats eat turkey?

The ASPCA says to stick to your pet's normal diet, and if you share a small bite, make it boneless and fully cooked. Poultry bones can be a major choking hazard. This is a holding draft until a cat-turkey pack re-quotes the live page. What did your cat try to steal off the Thanksgiving table?
#cancatseatturkey #turkeybones #thanksgivingpets #meatballmyths
```

If MASTER_ORDERS wins the hashtag fight, drop `#meatballmyths` and add two topic tags the checked script actually answers.

## Pinned comment

What did your cat try to steal off the Thanksgiving table? Full list in the Related video 👆

Open question, not yes/no. Keep the Related-video line only if the Short is on-topic to that week's long-form (`related-video-rule.md`). If it is a holiday pet Short next to a bug or born-as wildlife long-form, point it at the Things Living In Your House playlist instead, or at a pet long-form if one is the week's lead.
