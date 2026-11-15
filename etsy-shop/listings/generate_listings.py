#!/usr/bin/env python3
"""Generate rewritten FurEver Faces Etsy listings and validate title/tag rules."""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _ids import PRINTIFY_IDS
from _designs import DESIGNS, HOOKS

OUT = HERE

PRODUCT_LABEL = {
    "tee": "Tee", "mug": "Mug", "sweatshirt": "Sweatshirt", "ornament": "Ornament",
    "wall": "Wall Art", "bandana": "Pet Bandana", "tank": "Pet Tank Top",
}
CLOSING = "Order by Dec 5 for Christmas delivery. Artwork created with AI tools."
WHO = "For goldendoodle, labradoodle, and bernedoodle people."
WHO_MOM = "For goldendoodle, labradoodle, and bernedoodle moms."
WHO_DAD = "For goldendoodle, labradoodle, and bernedoodle dads."
WHO_FAM = "For goldendoodle, labradoodle, and bernedoodle parents."

STUDIO_LOCKED = {
    ("mom", "tee"): {
        "heading": "Doodle Mom Tee",
        "intro": "Ready-to-paste Etsy listing. Rewritten Nov 15, 2026 by Etsy Studio. Source template: `skills/dropship/ETSY_LISTINGS.md` on `claude/blissful-allen-waez05` (Doodle Mom: Tee). That file says to list the mom/dad designs first. This copy matches the notebook example in `listings/doodle-mom-tee.md` exactly.",
        "title": "Doodle Mom Shirt, Goldendoodle Mama Tee, Curls Cuddles & Chaos, Cute Cartoon Dog Mom Gift",
        "tags": ["doodle mom shirt", "goldendoodle mom", "dog mom shirt", "labradoodle mom", "bernedoodle gift", "doodle mama", "dog lover tee", "cute dog cartoon", "unisex dog shirt", "doodle mom gift", "dog mom humor", "cartoon dog tee", "goldendoodle gift"],
        "description": "Curls, cuddles, and chaos. That is the job. A cartoon doodle in a pink bandana on a unisex Bella + Canvas cotton tee, sizes S to 2XL, printed to order in the USA. For goldendoodle, labradoodle, and bernedoodle moms. Pair it with the matching dog bandana if you want the whole family in on it. Order by Dec 5 for Christmas delivery. Artwork created with AI tools.",
        "price_note": "$26.00 — this is the tee price in both `skills/dropship/ETSY_LISTINGS.md` and `skills/dropship/ETSY_STATE.md`. The listings file also notes that $26.00 can leave a thin margin if shipping is free; confirm Printify cost before publishing.",
    },
    ("santa", "ornament"): {
        "heading": "Santa Paws Goldendoodle Christmas Ornament",
        "intro": "Ready-to-paste Etsy listing. Rewritten Nov 15, 2026 by Etsy Studio. Source template: `skills/dropship/ETSY_LISTINGS.md` on `claude/blissful-allen-waez05` (Santa Paws: Ornament). This copy matches the notebook example in `listings/santa-paws-ornament.md` exactly. Placed in the catalog file because this assignment asked for Santa Paws tee and mug in the Christmas push; the Nov 15 audit still treats this ornament as a lead Christmas item.",
        "title": "Santa Paws Goldendoodle Christmas Ornament, Cute Doodle Tree Decor, Funny Gift for Doodle Mom",
        "tags": ["santa paws", "goldendoodle", "doodle ornament", "christmas dog", "labradoodle", "bernedoodle", "dog ornament", "doodle mom gift", "pet christmas", "funny dog gift", "tree decoration", "ceramic ornament", "christmas gift"],
        "description": "He's on the nice list. Pending. A cream doodle in a Santa hat, arms full of gifts, and the line every doodle parent already says out loud. Hang it on the tree or tuck it in a stocking. Round ceramic ornament with ribbon, printed to order in the USA. Also designed for labradoodle and bernedoodle families. Order by Dec 5 for Christmas delivery. Artwork created with AI tools.",
        "price_note": "Do not publish until Moondog88 picks a price. The source files disagree:\n\n- $21.99 in `skills/dropship/ETSY_LISTINGS.md`\n- $16.99 in `skills/dropship/ETSY_STATE.md`\n\nCheck actual Printify cost plus shipping, then use one price on every ornament listing. Suggested range until then: $16.99–$21.99 (from those files only; not verified market data).",
    },
}


def load_listings():
    items = []
    for name in ("_listings_push.json", "_listings_cat_a.json", "_listings_cat_b.json", "_listings_cat_c.json"):
        items.extend(json.loads((HERE / name).read_text()))
    return items


def product_sentence(kind: str):
    missing = []
    if kind == "tee":
        return ("On a unisex Bella + Canvas cotton tee, sizes S to 2XL, printed to order in the USA.", missing)
    if kind == "mug":
        return ("On a ceramic mug, 11 oz or 15 oz, dishwasher and microwave safe, printed to order in the USA.", missing)
    if kind == "ornament":
        return ("Round ceramic ornament with ribbon, printed to order in the USA. (Ceramic, ribbon, and USA wording is from the first-batch ornament listings in ETSY_LISTINGS.md; ETSY_STATE.md uses the same ornament blueprint 537 / Duplium.)", missing)
    if kind == "wall":
        return ("Gallery-wrapped canvas, 12 x 16 in or 16 x 20 in, printed to order in the USA.", missing)
    if kind == "sweatshirt":
        missing.append("Sweatshirt material and size range are not stated in the source files.")
        return ("On a sweatshirt. ETSY_STATE.md lists print provider Monster Digital, blueprint 49, priced at $39.99. Material, size range, and “printed in the USA” are not stated for sweatshirts in the source files.", missing)
    if kind == "bandana":
        missing.append("Pet bandana material, sizes, and care facts are not stated in the source files.")
        return ("A Pet Bandana (Printify blueprint 562, Printed Mint). ETSY_STATE.md does not state material, sizes, or care, and does not say it is printed in the USA.", missing)
    if kind == "tank":
        missing.append("Pet tank material, sizes, and care facts are not stated in the source files.")
        return ("A Pet Tank Top (Printify blueprint 571, Printed Mint). ETSY_STATE.md does not state material, sizes, or care, and does not say it is printed in the USA.", missing)
    raise ValueError(kind)


def who_for(slug: str) -> str:
    if slug in {"mom", "era"}:
        return WHO_MOM
    if slug in {"dad", "best"}:
        return WHO_DAD
    if slug == "fam":
        return WHO_FAM
    return WHO


def extra_line(kind: str, slug: str) -> str:
    if kind in {"bandana", "tank"}:
        return "ETSY_STATE.md says each dog listing should link to its human tee and back."
    if kind == "tee" and slug in {"mom", "dad", "santa", "fam", "velcro", "sock", "bed", "surf2", "zoom", "glow"}:
        return "A matching pet bandana and pet tank exist for this design; link the listings to each other."
    return ""


def price_note(kind: str, has_id: bool) -> str:
    bits = []
    if kind == "tee":
        bits.append("$26.00 — the tee price in both `skills/dropship/ETSY_LISTINGS.md` (`$26.00`) and `skills/dropship/ETSY_STATE.md` (`tee $26`). The listings file also notes that $26.00 can leave a thin margin if shipping is free; confirm Printify cost before publishing.")
    elif kind == "mug":
        bits.append("The source files disagree on the mug price. Do not invent a third number; pick one and use it on every mug listing:")
        bits.append("")
        bits.append("- $18.00 in `skills/dropship/ETSY_LISTINGS.md`")
        bits.append("- $17.99 in `skills/dropship/ETSY_STATE.md` (`Prices: tee $26, sweatshirt $39.99, mug $17.99, ornament $16.99.`)")
        bits.append("")
        bits.append("See `03-pricing-memo.md`. Suggested range until then: $17.99–$18.00 (from those files only; not verified market data).")
    elif kind == "ornament":
        bits.append("Do not publish until Moondog88 picks a price. The source files disagree:")
        bits.append("")
        bits.append("- $21.99 in `skills/dropship/ETSY_LISTINGS.md`")
        bits.append("- $16.99 in `skills/dropship/ETSY_STATE.md` (`Prices: tee $26, sweatshirt $39.99, mug $17.99, ornament $16.99.`)")
        bits.append("")
        bits.append("Check actual Printify cost plus shipping, then use one price on every ornament listing. Suggested range until then: $16.99–$21.99 (from those files only; not verified market data).")
    elif kind == "sweatshirt":
        bits.append("$39.99 — the sweatshirt price in `skills/dropship/ETSY_STATE.md` (`Prices: tee $26, sweatshirt $39.99, mug $17.99, ornament $16.99.`). Sweatshirts are not priced in ETSY_LISTINGS.md.")
    elif kind == "wall":
        bits.append("$59.99 — the wall-art price in `skills/dropship/ETSY_LISTINGS.md`. Wall art is not priced and has no Printify product id in ETSY_STATE.md.")
    elif kind == "bandana":
        bits.append("$18.99 — the pet bandana price in `skills/dropship/ETSY_STATE.md` (`Pet Bandana (blueprint 562, Printed Mint 70, $18.99, ...)`). Not priced in ETSY_LISTINGS.md.")
    elif kind == "tank":
        bits.append("$27.99 — the pet tank price in `skills/dropship/ETSY_STATE.md` (`Pet Tank Top (571, Printed Mint 70, $27.99, ...)`). Not priced in ETSY_LISTINGS.md.")
    if not has_id:
        bits.append("")
        bits.append("FLAG: no Printify product id for this item in ETSY_STATE.md. Copy exists or was drafted from ETSY_LISTINGS.md only. Confirm the product has been created in Printify before pasting this live.")
    return "\n".join(bits)


def attributes(kind: str, slug: str, has_id: bool, missing: list[str]) -> str:
    pid = PRINTIFY_IDS.get(f"{kind}:{slug}")
    lines = [
        "- Production partner: Printify (ETSY_LISTINGS.md: “name Printify as the production partner”).",
        "- When made: made to order (print-on-demand; etsy-factory listing.json pattern uses `made_to_order`).",
    ]
    if kind == "tee":
        lines += [
            "- Materials / sizes (from ETSY_LISTINGS.md): cotton (Bella + Canvas); unisex S to 2XL.",
            "- Print: Monster Digital, blueprint 12; tee scale 0.95 at y 0.42 (ETSY_STATE.md).",
        ]
    elif kind == "mug":
        lines += [
            "- Materials / sizes (from ETSY_LISTINGS.md): ceramic; 11 oz or 15 oz; dishwasher and microwave safe.",
            "- Print: SPOKE, blueprint 68; three copies at x 0.17/0.5/0.83, scale 0.31 (ETSY_STATE.md).",
        ]
    elif kind == "ornament":
        lines += [
            "- Materials (from ETSY_LISTINGS.md first-batch ornaments): round ceramic ornament with ribbon.",
            "- Print: Duplium, blueprint 537; ornament scale 0.6 (ETSY_STATE.md).",
        ]
    elif kind == "wall":
        lines += [
            "- Materials / sizes (from ETSY_LISTINGS.md): gallery-wrapped canvas, 12 x 16 in or 16 x 20 in.",
            "- Print provider / blueprint: not stated in ETSY_STATE.md.",
        ]
    elif kind == "sweatshirt":
        lines += [
            "- Materials / sizes: not stated in the source files.",
            "- Print: Monster Digital, blueprint 49 (ETSY_STATE.md).",
        ]
    elif kind == "bandana":
        lines += [
            "- Materials / sizes / care: not stated in the source files.",
            "- Print: Printed Mint, blueprint 562; scale 0.29 at y 0.34 (ETSY_STATE.md).",
        ]
    elif kind == "tank":
        lines += [
            "- Materials / sizes / care: not stated in the source files.",
            "- Print: Printed Mint, blueprint 571; scale 0.9 at y 0.35 (ETSY_STATE.md).",
        ]
    if pid:
        lines.append(f"- Printify product id (ETSY_STATE.md, Etsy store): `{pid}`.")
    else:
        lines.append("- Printify product id: none in ETSY_STATE.md.")
    for m in missing:
        lines.append(f"- FLAG: {m}")
    return "\n".join(lines)


def photo_notes(kind: str, slug: str) -> str:
    d = DESIGNS[slug]
    print_name = f"fureverfaces/print/PRINT-{d['print']}.png"
    bits = [
        f"Print file: `{print_name}` on `mooneyn60-art/AI-Youtube-Shorts-Generator_SamurAIGPT`, branch `claude/blissful-allen-waez05`. ETSY_LISTINGS.md says to create the product in Printify with that file and that Printify adds the product photos — “about ten images per listing, generated by Printify when the listing is published.” No custom photo order is specified in the listing source files.",
        "The Nov 15 creative audit (local Side-hustles notebook) suggests leading with a real product photo, then a lifestyle shot, and demoting flat illustrated blanks. That is a suggestion from the audit, not a photo sequence in the Printify/listing files.",
    ]
    if kind in {"bandana", "tank"}:
        bits.append("ETSY_STATE.md: “Each dog listing links to its human tee and back.”")
    return " ".join(bits)


def description_for(slug: str, kind: str, missing: list[str]) -> str:
    d = DESIGNS[slug]
    prod, miss = product_sentence(kind)
    missing.extend(miss)
    extra = extra_line(kind, slug)
    parts = [HOOKS[slug], f"{d['art']} {prod}", who_for(slug)]
    if extra:
        parts.append(extra)
    parts.append(CLOSING)
    return " ".join(parts)


def source_line(slug: str, kind: str) -> str:
    d = DESIGNS[slug]
    label = f"{d['name']}: {PRODUCT_LABEL[kind]}"
    base = (
        "Ready-to-paste Etsy listing. Rewritten Nov 15, 2026 by Etsy Studio. "
        "Pattern matches the notebook examples in `listings/` (title, 13 tags, description, price note)."
    )
    if (slug, kind) in STUDIO_LOCKED:
        return STUDIO_LOCKED[(slug, kind)]["intro"]
    if d["src"] == "listings":
        return (
            f"{base} Source template: `skills/dropship/ETSY_LISTINGS.md` on `claude/blissful-allen-waez05` "
            f"({label}). Product facts also from `skills/dropship/ETSY_STATE.md`."
        )
    return (
        f"{base} No listing copy existed in ETSY_LISTINGS.md for this design. "
        f"Slogan and artwork were read from the print file "
        f"`fureverfaces/print/PRINT-{d['print']}.png` on "
        f"`mooneyn60-art/AI-Youtube-Shorts-Generator_SamurAIGPT`, branch `claude/blissful-allen-waez05` "
        f"(listed as source-of-truth in the Side-hustles TASKS.md). "
        f"Product facts from `skills/dropship/ETSY_STATE.md`. "
        f"FLAG: confirm the print-file wording before publishing if you want a typo check."
    )


def heading_for(slug: str, kind: str) -> str:
    if (slug, kind) in STUDIO_LOCKED:
        return STUDIO_LOCKED[(slug, kind)]["heading"]
    return f"{DESIGNS[slug]['name']} {PRODUCT_LABEL[kind]}"


def title_and_tags(item):
    locked = STUDIO_LOCKED.get((item["slug"], item["kind"]))
    if locked:
        return locked["title"], locked["tags"]
    return item["title"], item["tags"]


def render_listing(item: dict) -> str:
    slug, kind = item["slug"], item["kind"]
    missing: list[str] = []
    locked = STUDIO_LOCKED.get((slug, kind))
    if locked:
        title, tags, desc, pnote, intro, heading = (
            locked["title"], locked["tags"], locked["description"],
            locked["price_note"], locked["intro"], locked["heading"],
        )
        _, miss = product_sentence(kind)
        missing.extend(miss)
    else:
        title, tags = item["title"], item["tags"]
        desc = description_for(slug, kind, missing)
        has_id = f"{kind}:{slug}" in PRINTIFY_IDS
        pnote = price_note(kind, has_id)
        intro = source_line(slug, kind)
        heading = heading_for(slug, kind)
    has_id = f"{kind}:{slug}" in PRINTIFY_IDS
    attr = attributes(kind, slug, has_id, missing)
    photos = photo_notes(kind, slug)
    return "\n".join([
        f"# {heading}", "", intro, "",
        "## Title", "", title, "",
        f"({len(title)} characters; Etsy limit 140)", "",
        "## Tags (13, each 20 characters or fewer)", "",
        "\n".join(tags), "",
        "## Description", "", desc, "",
        "## Price note", "", pnote, "",
        "## Suggested attributes", "", attr, "",
        "## Photo notes", "", photos, "",
    ])


def validate(items):
    errors = []
    seen = set()
    all_tags = Counter()
    titles = []
    for it in items:
        key = (it["slug"], it["kind"])
        if key in seen:
            errors.append(f"duplicate listing {key}")
        seen.add(key)
        title, tags = title_and_tags(it)
        titles.append(title)
        if len(title) > 140:
            errors.append(f"TITLE TOO LONG ({len(title)}): {title}")
        if len(tags) != 13:
            errors.append(f"{key} has {len(tags)} tags, need 13")
        if len(set(t.lower() for t in tags)) != len(tags):
            errors.append(f"{key} has duplicate tags: {tags}")
        for t in tags:
            if len(t) > 20:
                errors.append(f"{key} tag over 20 chars ({len(t)}): {t!r}")
            if not t.strip() or t != t.strip() or "," in t:
                errors.append(f"{key} bad tag: {t!r}")
            all_tags[t.lower()] += 1
        if title.startswith("Goldendoodle ") and "Doodle Mom Dad Gift" in title:
            errors.append(f"{key} still uses old stencil: {title}")
    if len(set(titles)) != len(titles):
        errors.append("duplicate titles: " + str([t for t, c in Counter(titles).items() if c > 1]))
    return errors, all_tags, titles


INTRO_1 = """# Christmas push listings

Ready-to-paste rewrites for the short Christmas list. Written Nov 15, 2026 (America/New_York) by Etsy Studio. GitHub was not edited.

This file covers the set named in the assignment: Santa Paws tee and mug; Snow Day (tee, mug, sweatshirt, and ornament — every Snow Day SKU in ETSY_STATE.md); Doodle Dad (tee, mug, sweatshirt, and ornament); and the Santa, Mom, and Dad pet bandanas and tanks.

The Nov 15 audit and TASKS.md also treat the Santa Paws ornament and the Doodle Mom tee as lead Christmas items. Those two already have Etsy Studio rewrites; they are in `02-catalog.md` (and in the Side-hustles notebook at `listings/santa-paws-ornament.md` and `listings/doodle-mom-tee.md`). The Santa Paws sweatshirt and wall art are likewise in the catalog file because this assignment specified tee and mug only for Santa Paws.

Pattern for each listing matches the three notebook examples: Title (with character count), 13 tags on separate lines, a short human description, and a price note that quotes the source files. Suggested attributes and photo notes are added after that, only from source facts. Printify descriptions should stay plain text (ETSY_STATE.md: “Printify descriptions must be plain text with newlines (HTML breaks on Etsy)”).

No prices were changed. Ornament and mug prices still conflict across the source files — see `03-pricing-memo.md` and the price notes below. Do not invent sales or search numbers; none are in the source files.

**Listing count in this file: 16.**
"""

INTRO_2 = """# Catalog listings (the rest of the dog shop)

Ready-to-paste rewrites for the rest of the FurEver Faces / PrintanPress dog catalog, including the 12 funny tees that had no listing copy, all remaining sweatshirts, the remaining pet bandanas and tanks, and the wall-art / extra mug / extra ornament drafts that appear in ETSY_LISTINGS.md but have no Printify id in ETSY_STATE.md. Written Nov 15, 2026 (America/New_York) by Etsy Studio. GitHub was not edited.

The Doodle Mom tee and Santa Paws ornament in this file are the exact Etsy Studio rewrites from the Side-hustles notebook examples. Funny-tee slogans and artwork were read from `fureverfaces/print/PRINT-*.png` (shorts repo, branch `claude/blissful-allen-waez05`) because ETSY_LISTINGS.md had no copy for those designs. Flag those listings for a typo check against the print file before publishing.

Pattern matches the notebook examples (title, character count, 13 tags, description, price note), plus suggested attributes and photo notes from source facts only. Missing material/size facts are flagged, not filled in. No prices were changed. No sales or search numbers are cited.

**Listing count in this file: 79.**
"""


def toc(items):
    lines = ["## Contents", ""]
    for it in items:
        title, _ = title_and_tags(it)
        lines.append(f"- {heading_for(it['slug'], it['kind'])} — {len(title)} characters")
    lines.append("")
    return "\n".join(lines)


def write_file(path: Path, intro: str, items):
    parts = [intro, "", toc(items)]
    for it in items:
        parts.append(render_listing(it))
        parts.append("---")
        parts.append("")
    path.write_text("\n".join(parts).rstrip() + "\n")


def main() -> int:
    items = load_listings()
    errors, tag_counts, titles = validate(items)
    push = [i for i in items if i["file"] == 1]
    catalog = [i for i in items if i["file"] == 2]
    if len(push) != 16:
        errors.append(f"expected 16 christmas listings, got {len(push)}")
    if len(catalog) != 79:
        errors.append(f"expected 79 catalog listings, got {len(catalog)}")
    if len(items) != 95:
        errors.append(f"expected 95 total, got {len(items)}")
    if errors:
        print("VALIDATION FAILED:", file=sys.stderr)
        for e in errors:
            print(" -", e, file=sys.stderr)
        return 1
    write_file(OUT / "01-christmas-push.md", INTRO_1, push)
    write_file(OUT / "02-catalog.md", INTRO_2, catalog)
    print(f"OK: {len(push)} christmas, {len(catalog)} catalog, {len(items)} total")
    print(f"Unique tags: {len(tag_counts)}; reused: {sum(1 for c in tag_counts.values() if c > 1)}")
    print("Most reused tags:")
    for t, c in tag_counts.most_common(15):
        print(f"  {c:3d}  {t} ({len(t)} chars)")
    print(f"Title lengths: min {min(map(len, titles))}, max {max(map(len, titles))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
