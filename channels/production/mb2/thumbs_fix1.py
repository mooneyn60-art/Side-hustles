"""Fix batch 1 thumbnails, DON'T MOVE direction (picked by Moondog88's side, Nov 15): one huge Meatball face with the threat
touching or engulfing it, flat saturated field, 1-3 huge words on the empty left side (one accent word), nothing in the
bottom-right timestamp zone. Long-forms 1280x720, Shorts covers 1080x1920. Writes phone-size copies (168x94 / 108x192)
and the before/after sheet. Usage: thumbs_fix1.py OUTDIR"""
import os, sys, json, textwrap, skia, numpy as np
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(__file__))
from kit import text_outlined
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = sys.argv[1]; PH = os.path.join(OUT, 'phone_check'); os.makedirs(PH, exist_ok=True)
OURS = '/workspace/outliers/thumbs'; F = 'Anton-Regular.ttf'; RED, YEL, WHT, BLK = '#E0201B', '#FFD21F', '#ffffff', '#111111'

def recolor_bg(im, new):   # repaint the flat red field connected to the left edge (variant C); BFS over the red mask
    from collections import deque
    a = np.array(im.convert('RGB')); ai = a.astype(int); red = (ai[..., 0] > 120) & (ai[..., 1] < 70) & (ai[..., 2] < 70)
    h, w = red.shape; bg = np.zeros_like(red); q = deque((y, 0) for y in range(h) if red[y, 0])
    for y, x in q: bg[y, x] = True
    while q:
        y, x = q.popleft()
        for yy, xx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
            if 0 <= yy < h and 0 <= xx < w and red[yy, xx] and not bg[yy, xx]: bg[yy, xx] = True; q.append((yy, xx))
    a[bg] = Image.new('RGB', (1, 1), new).getpixel((0, 0)); return Image.fromarray(a)

def long_thumb(art, z, foc, words, recolor=None):
    TW, TH = 1280, 720; s = skia.Surface(TW, TH); cv = s.getCanvas()
    im = Image.open(os.path.join(HERE, 'art', art)).convert('RGB').resize((TW, TH), Image.LANCZOS)
    if recolor: im = recolor_bg(im, recolor)
    img = skia.Image.fromarray(np.array(im.convert('RGBA')), colorType=skia.kRGBA_8888_ColorType)
    cx, cy = foc[0]*TW, foc[1]*TH; hw, hh = TW/2/z, TH/2/z; cx = min(max(cx, hw), TW - hw); cy = min(max(cy, hh), TH - hh)
    cv.save(); cv.translate(TW/2, TH/2); cv.scale(z, z); cv.translate(-cx, -cy); cv.drawImage(img, 0, 0, skia.SamplingOptions(skia.FilterMode.kLinear)); cv.restore()
    for (t, col, x, y, px) in words:
        text_outlined(cv, t, x, y, px, col, '#000' if col != BLK else '#ffffff', 28 if col != BLK else 14, F, rot=-4)
    return Image.fromarray(s.makeImageSnapshot().toarray()[:, :, [2, 1, 0]]).convert('RGB')

def short_cover(art, words, bg, vertical=True, z=1.0, foc=(0.5, 0.5)):
    TW, TH = 1080, 1920; s = skia.Surface(TW, TH); cv = s.getCanvas(); cv.clear(skia.Color4f.FromColor(skia.ColorSetRGB(*Image.new('RGB', (1, 1), bg).getpixel((0, 0)))))
    im = Image.open(os.path.join(HERE, 'art', art)).convert('RGBA')
    if vertical:
        im = im.resize((TW, TH), Image.LANCZOS); img = skia.Image.fromarray(np.array(im), colorType=skia.kRGBA_8888_ColorType)
        cx, cy = foc[0]*TW, foc[1]*TH; hw, hh = TW/2/z, TH/2/z; cx = min(max(cx, hw), TW - hw); cy = min(max(cy, hh), TH - hh)
        cv.save(); cv.translate(TW/2, TH/2); cv.scale(z, z); cv.translate(-cx, -cy); cv.drawImage(img, 0, 0, skia.SamplingOptions(skia.FilterMode.kLinear)); cv.restore()
    else:   # 16:9 art on a matching flat field, face band in the middle third, words above
        h = int(TW*im.height/im.width*1.5); im = im.resize((int(TW*1.5), h), Image.LANCZOS)
        img = skia.Image.fromarray(np.array(im), colorType=skia.kRGBA_8888_ColorType); cv.drawImage(img, -TW*0.48, 760)
    for (t, col, x, y, px) in words:
        text_outlined(cv, t, x, y, px, col, '#000', 30, F, rot=-4)
    return Image.fromarray(s.makeImageSnapshot().toarray()[:, :, [2, 1, 0]]).convert('RGB')

ITEMS = [  # (file, kind, video id or None, current title, proposed title, render args)
 # DON'T MOVE: baseline + 3 challengers (girlfriend's pick = baseline)
 ('fix1_dontmove_0_baseline.png', 'long', None, '(new WMS long-form)', 'Would You Survive a Grizzly Attack? (Meatball Tried)',
  ('thumb_art_peek.jpg', 1.0, (0.5, 0.5), [("DON'T", WHT, 270, 300, 220), ('MOVE', YEL, 270, 560, 250)])),
 ('fix1_dontmove_A_tighter.png', 'long', None, '', 'Would You Survive a Grizzly Attack? (Meatball Tried)',
  ('thumb_art_peek.jpg', 1.28, (0.70, 0.50), [("DON'T", WHT, 320, 280, 230), ('MOVE', YEL, 320, 575, 270)])),
 ('fix1_dontmove_B_one-word.png', 'long', None, '', 'Would You Survive a Grizzly Attack? (Meatball Tried)',
  ('thumb_art_peek.jpg', 1.12, (0.62, 0.5), [('MOVE?', YEL, 390, 470, 270)])),
 ('fix1_dontmove_C_contrast.png', 'long', None, '', 'Would You Survive a Grizzly Attack? (Meatball Tried)',
  ('thumb_art_peek.jpg', 1.12, (0.62, 0.5), [("DON'T", WHT, 260, 290, 230), ('MOVE', YEL, 260, 570, 270)], '#0b2a8a')),
 # long-forms in the lane
 ('fix1_lf_cH3HCZ8GlHk_3-bugs-never-kill.png', 'long', 'cH3HCZ8GlHk', '3 Bugs in Your House You Should Never Kill (And 4 You Must)', '3 Bugs in Your House You Should Never Kill (And 4 You Must)',
  ('thumb_art_house-centipede.jpg', 1.18, (0.66, 0.5), [('KEEP', WHT, 200, 170, 170), ('THIS', YEL, 200, 360, 190), ('ONE', WHT, 200, 545, 170)])),
 ('fix1_lf_KWOM2-mNmww_corner-spider.png', 'long', 'KWOM2-mNmww', "Don't Kill the Spider in Your Corner. It Eats Bigger Spiders", 'Your Life as the Skinny Spider in Your Ceiling Corner',
  ('fx_spider_face.jpg', 1.0, (0.5, 0.5), [('EATS', BLK, 250, 190, 170), ('BIGGER', RED, 250, 380, 180), ('SPIDERS', BLK, 250, 560, 160)])),
 ('fix1_lf_xeAsg5ECpgw_3-more-bugs.png', 'long', 'xeAsg5ECpgw', '3 More Bugs in Your House You Should Never Kill (And 5 You Must)', '3 More Bugs in Your House You Should Never Kill (And 5 You Must)',
  ('fx_moth_face.jpg', 1.0, (0.5, 0.5), [('NOT', WHT, 230, 200, 190), ('THE', WHT, 230, 390, 170), ('MOTH', YEL, 230, 590, 210)])),
 ('fix1_lf_Lid8JXhg1Q4_6-creatures.png', 'long', 'Lid8JXhg1Q4', '6 Creatures Living In Your House Right Now (You Never See Them)', '6 Creatures Living in Your House Right Now (You Never See Them)',
  ('fx_mite_face.jpg', 1.0, (0.5, 0.5), [('IN', WHT, 230, 200, 190), ('YOUR', WHT, 230, 390, 190), ('BED', YEL, 230, 590, 220)])),
 ('fix1_lf_bqij8Ht6SX4_every-bug-ranked.png', 'long', 'bqij8Ht6SX4', 'Every Bug in Your House, Ranked From Harmless to Nightmare 🐛', 'Every Bug in Your House, Ranked From Harmless to Nightmare',
  ('fx_recluse_face.jpg', 1.0, (0.5, 0.5), [("WHO'S", WHT, 250, 260, 200), ('#1?', RED, 250, 520, 260)])),
 # top Shorts (vertical covers, set in the YouTube app)
 ('fix1_sh_Us0zIbxiR-A_daddy-longlegs.png', 'short', 'Us0zIbxiR-A', 'Are Daddy Longlegs the Most Venomous Spiders? 🕷️', 'Are Daddy Longlegs the Most Venomous Spiders? 🕷️',
  ('rv2_dll_hook.jpg', [('VENOMOUS?', YEL, 540, 1080, 170)], '#2a2622', True, 1.0)),
 ('fix1_sh_EPimwC5VMgo_house-centipede.png', 'short', 'EPimwC5VMgo', 'The House Centipede You Squish Is Protecting You 🐛 (Things Living In Your House)', 'The House Centipede You Squish Is Protecting You 🐛',
  ('rv2_cent_hook.jpg', [('LET IT', WHT, 540, 1180, 170), ('LIVE?', YEL, 540, 1370, 190)], '#ddd', True, 1.0)),
 ('fix1_sh_1hdMaSxJtkU_roach-babies.png', 'short', '1hdMaSxJtkU', 'Your Roach Has 40 Babies 🪳 (Things Living In Your House #N)', 'Your Roach Has 40 Babies 🪳',
  ('fx_roach_face.jpg', [('40', WHT, 540, 380, 300), ('BABIES', YEL, 540, 640, 230)], '#ff7a00', False)),
 ('fix1_sh_wHCrmIPdCgg_bed-mites.png', 'short', 'wHCrmIPdCgg', 'Your Bed Mites Die at 130°F 😬 (Things Living In Your House #N)', 'Your Bed Mites Die at 130°F 😬',
  ('fx_mite_face.jpg', [('WASH', WHT, 540, 380, 230), ('HOTTER', YEL, 540, 640, 230)], '#1b3fae', False)),
 ('fix1_sh_bm6LzV7eRwg_mommy-longlegs.png', 'short', 'bm6LzV7eRwg', "3 'Mommy Longlegs' in Your Home 🕷️ (Is This Spider Venomous? #N)", "3 'Mommy Longlegs' in Your Home 🕷️",
  ('rv2_harvestman.jpg', [('NOT A', WHT, 540, 300, 170), ('SPIDER', YEL, 540, 500, 210)], '#222', True, 1.0)),
]
rows = []
for file, kind, vid, cur, new, args in ITEMS:
    im = long_thumb(*args) if kind == 'long' else short_cover(*args)
    im.save(os.path.join(OUT, file)); small = (168, 94) if kind == 'long' else (108, 192)
    im.resize(small, Image.LANCZOS).save(os.path.join(PH, file)); rows.append(dict(file=file, kind=kind, video=vid, current_title=cur, proposed_title=new))
json.dump(rows, open(os.path.join(OUT, 'fix1_thumbs.json'), 'w'), indent=1)

# DON'T MOVE challenger sheet at phone size, as it shows in the feed
FS = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 14); FB = ImageFont.truetype(os.path.join(HERE, 'assets', F), 26)
dm = [r for r in rows if r['file'].startswith('fix1_dontmove')]
sheet = Image.new('RGB', (4*420 + 20, 560), '#0f0f0f'); d = ImageDraw.Draw(sheet)
for i, r in enumerate(dm):
    x = 10 + i*420; im = Image.open(os.path.join(OUT, r['file']))
    sheet.paste(im.resize((400, 225), Image.LANCZOS), (x, 50)); sheet.paste(im.resize((168, 94), Image.LANCZOS), (x, 300))
    sheet.paste(im.resize((168, 94), Image.LANCZOS).resize((336, 188), Image.NEAREST), (x + 180, 300)) if False else None
    d.text((x, 12), ['BASELINE (her pick)', 'A: tighter, bigger face', 'B: one word', 'C: blue field'][i], font=FB, fill='#ffd23f')
    d.text((x + 180, 300), 'phone size 168x94', font=FS, fill='#aaaaaa'); d.text((x + 180, 320), textwrap.fill(r['proposed_title'], 26), font=FS, fill='#f1f1f1')
sheet.save(os.path.join(OUT, 'fix1_dontmove_challengers.png'))

# before / after sheet for every channel thumbnail in the batch
ch = [r for r in rows if r['video']]
RH = 250; sheet = Image.new('RGB', (1500, 60 + RH*len(ch)), '#0f0f0f'); d = ImageDraw.Draw(sheet)
d.text((10, 14), 'BEFORE (live now)', font=FB, fill='#ff6b6b'); d.text((520, 14), 'AFTER (fix batch 1, not live)', font=FB, fill='#7CFF6B'); d.text((1040, 14), 'phone size: before | after', font=FB, fill='#aaaaaa')
for i, r in enumerate(ch):
    y = 60 + i*RH; b = Image.open(os.path.join(OURS, f"ours_{r['video']}.jpg")).convert('RGB'); a = Image.open(os.path.join(OUT, r['file']))
    def fit(im, w, h):
        im = im.copy(); im.thumbnail((w, h), Image.LANCZOS); return im
    if r['kind'] == 'long': sb, sa = (168, 94), (168, 94)
    else: sb, sa = (108, 192), (108, 192)
    sheet.paste(fit(b, 480, 230), (10, y)); sheet.paste(fit(a, 480, 230), (520, y))
    sheet.paste(b.resize(sb if r['kind'] == 'long' else (int(b.width*192/b.height), 192), Image.LANCZOS) if r['kind'] == 'long' else fit(b, 140, 192), (1040, y))
    sheet.paste(a.resize(sa, Image.LANCZOS), (1240, y))
    d.text((1040, y + 200), textwrap.shorten(r['proposed_title'], 60), font=FS, fill='#f1f1f1')
sheet.save(os.path.join(OUT, 'fix1_thumbs_before_after.png'))
print('ok', len(rows))
