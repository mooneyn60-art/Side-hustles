"""v3 thumbnail + title PAIRS engineered to the 11/15 outlier study (see production-spec-animation-v2.md "Packaging checklist").
Each: one huge emotional subject + one dominant threat, flat clean field, <=3 words with exactly one red word, words top-left
(never bottom-right), and words that ADD to the title instead of repeating it. Writes 1280x720 PNGs, 168x94 checks and a pairs sheet."""
import os, sys, json, skia, numpy as np
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(__file__))
from kit import text_outlined
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = sys.argv[1]; os.makedirs(os.path.join(OUT, 'phone_check'), exist_ok=True)
TW, TH = 1280, 720; F = 'Anton-Regular.ttf'; RED, YEL, WHT = '#E0201B', '#FFD21F', '#ffffff'
PAIRS = [  # file, art, zoom, (cx, cy) focus, words [(text, colour, x, y, size)], title
    ('v3_thumb_1_too-slow.png', 'thumb_art_tooslow.jpg', 1.10, (0.55, 0.56), [('TOO', WHT, 180, 165, 145), ('SLOW', RED, 460, 145, 145)],
     "You Can't Outrun a Grizzly. Here's What Works"),
    ('v3_thumb_2_play-dead.png', 'thumb_art_playdead.jpg', 1.18, (0.62, 0.55), [('PLAY', YEL, 235, 270, 220), ('DEAD?', RED, 250, 520, 220)],
     "A Grizzly Is Sniffing You. Do You Move?"),
    ('v3_thumb_3_dont-move.png', 'thumb_art_peek.jpg', 1.0, (0.5, 0.5), [("DON'T", WHT, 270, 300, 220), ('MOVE', YEL, 270, 560, 250)],
     "Would You Survive a Grizzly Attack? (Meatball Tried)"),
    ('v3_thumb_4_corner-spider.png', 'thumb_art_corner-spider.jpg', 1.0, (0.5, 0.5), [('EATS', '#111111', 190, 140, 120), ('BIGGER', RED, 215, 270, 130), ('SPIDERS', '#111111', 225, 385, 110)],
     "Your Life as the Skinny Spider in Your Ceiling Corner"),
    ('v3_thumb_5_house-centipede.png', 'thumb_art_house-centipede.jpg', 1.0, (0.5, 0.5), [('LET IT', WHT, 215, 140, 125), ('LIVE?', RED, 520, 130, 135)],
     "Why the House Centipede in Your Bathroom Is on Your Side"),
]
def render(file, art, z, foc, words):
    s = skia.Surface(TW, TH); cv = s.getCanvas()
    im = Image.open(os.path.join(HERE, 'art', art)).convert('RGBA').resize((TW, TH), Image.LANCZOS)
    img = skia.Image.fromarray(np.array(im), colorType=skia.kRGBA_8888_ColorType)
    cx, cy = foc[0]*TW, foc[1]*TH; hw, hh = TW/2/z, TH/2/z; cx = min(max(cx, hw), TW - hw); cy = min(max(cy, hh), TH - hh)
    cv.save(); cv.translate(TW/2, TH/2); cv.scale(z, z); cv.translate(-cx, -cy); cv.drawImage(img, 0, 0, skia.SamplingOptions(skia.FilterMode.kLinear)); cv.restore()
    for (t, col, x, y, px) in words:
        text_outlined(cv, t, x, y, px, col, '#000' if col != '#111111' else '#ffffff', 26 if col != '#111111' else 14, F, rot=-4)
    out = Image.fromarray(s.makeImageSnapshot().toarray()[:, :, [2, 1, 0]]).convert('RGB')
    out.save(os.path.join(OUT, file)); out.resize((168, 94), Image.LANCZOS).save(os.path.join(OUT, 'phone_check', file)); return out
cards = []
for file, art, z, foc, words, title in PAIRS:
    im = render(file, art, z, foc, words)
    cards.append((im, title, file))
# pairs sheet: each row = full thumb | phone-size (168x94) card with the title as it shows in the feed
FT = ImageFont.truetype(os.path.join(HERE, 'assets', 'Anton-Regular.ttf'), 30); FS = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 13) if os.path.exists('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf') else FT
W, RH = 640 + 30 + 420, 360 + 30
sheet = Image.new('RGB', (W, RH*len(cards) + 20), '#0f0f0f'); d = ImageDraw.Draw(sheet)
for i, (im, title, file) in enumerate(cards):
    y = 10 + i*RH; sheet.paste(im.resize((640, 360), Image.LANCZOS), (10, y))
    sheet.paste(im.resize((168, 94), Image.LANCZOS), (680, y + 10))
    import textwrap
    for j, line in enumerate(textwrap.wrap(title, 26)[:3]): d.text((858, y + 10 + j*17), line, font=FS, fill='#f1f1f1')
    d.text((858, y + 66), 'Meatball Myths', font=FS, fill='#aaaaaa')
    for j, line in enumerate(textwrap.wrap(f'TITLE: {title}', 30)): d.text((680, y + 130 + j*36), line, font=FT, fill='#ffd23f')
    d.text((680, y + 320), file, font=FS, fill='#888888')
sheet.save(os.path.join(OUT, 'v3_thumb_title_pairs.png'))
json.dump([{'file': f, 'title': t} for _, t, f in cards], open(os.path.join(OUT, 'v3_thumb_title_pairs.json'), 'w'), indent=1)
print('ok')
