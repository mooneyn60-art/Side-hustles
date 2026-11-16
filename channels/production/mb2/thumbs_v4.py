"""v4 thumbnails (Nov 15): adds what the outliers have and fix1 lacked: a readable fear/shock face (both eyes wide, mouth open),
Meatball looking AT the threat or at the viewer, the threat big and identifiable in the same frame (threat -> victim),
a curiosity device (arrow / circle / silhouette), rim glow for depth, text that adds to the title instead of repeating it.
Usage: thumbs_v4.py OUTDIR   (1280x720 + phone copies 168x94 + fix1_thumbs_v4_sheet.png)"""
import os, sys, textwrap, math, skia, numpy as np
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(__file__))
from kit import text_outlined
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = sys.argv[1]; PH = os.path.join(OUT, 'phone_check'); os.makedirs(PH, exist_ok=True)
F = 'Anton-Regular.ttf'; RED, YEL, WHT, BLK = '#E0201B', '#FFD21F', '#ffffff', '#111111'

def paint(c): return skia.Paint(Color=skia.Color(*Image.new('RGB', (1, 1), c).getpixel((0, 0))), AntiAlias=True)
def arrow(cv, x0, y0, x1, y1, col=YEL, w=26):
    a = math.atan2(y1 - y0, x1 - x0); hx, hy = x1 - 70*math.cos(a), y1 - 70*math.sin(a)
    for c, ww in (('#000', w + 16), (col, w)):
        p = paint(c); p.setStyle(skia.Paint.kStroke_Style); p.setStrokeWidth(ww); p.setStrokeCap(skia.Paint.kRound_Cap)
        cv.drawLine(x0, y0, hx, hy, p)
        tri = skia.Path(); n = (math.cos(a + math.pi/2), math.sin(a + math.pi/2)); k = 52 + (ww - w)
        tri.moveTo(x1 + (ww - w)*math.cos(a)*0.6, y1 + (ww - w)*math.sin(a)*0.6); tri.lineTo(hx + n[0]*k, hy + n[1]*k); tri.lineTo(hx - n[0]*k, hy - n[1]*k); tri.close()
        cv.drawPath(tri, paint(c))
def circle(cv, x, y, r, col=RED):
    for c, ww in (('#000', 26), (col, 14)):
        p = paint(c); p.setStyle(skia.Paint.kStroke_Style); p.setStrokeWidth(ww); cv.drawCircle(x, y, r, p)

def thumb(art, z, foc, words, marks=()):
    TW, TH = 1280, 720; s = skia.Surface(TW, TH); cv = s.getCanvas()
    im = Image.open(os.path.join(HERE, 'art', art)).convert('RGBA').resize((TW, TH), Image.LANCZOS)
    img = skia.Image.fromarray(np.array(im), colorType=skia.kRGBA_8888_ColorType)
    cx, cy = foc[0]*TW, foc[1]*TH; hw, hh = TW/2/z, TH/2/z; cx = min(max(cx, hw), TW - hw); cy = min(max(cy, hh), TH - hh)
    cv.save(); cv.translate(TW/2, TH/2); cv.scale(z, z); cv.translate(-cx, -cy); cv.drawImage(img, 0, 0, skia.SamplingOptions(skia.FilterMode.kLinear)); cv.restore()
    for m in marks: (arrow if m[0] == 'arrow' else circle)(cv, *m[1:])
    for (t, col, x, y, px) in words:
        text_outlined(cv, t, x, y, px, col, '#000' if col != BLK else '#ffffff', 28 if col != BLK else 14, F, rot=-4)
    return Image.fromarray(s.makeImageSnapshot().toarray()[:, :, [2, 1, 0]]).convert('RGB')

FX = os.path.join(os.path.dirname(OUT), 'fix-batch-1') if not os.path.exists(os.path.join(OUT, 'fix1_dontmove_0_baseline.png')) else OUT
ITEMS = [  # file, video, title, fix1 file it replaces, diagnosis, render args
 ('fix1_v4_dontmove_baseline.png', None, 'Would You Survive a Grizzly Attack? (Meatball Tried)', 'fix1_dontmove_0_baseline.png',
  'Bear read as just teeth at 168px and the one-eye wince looked like a wink: now a full bear face plus wide-eyed frozen fear, rim glow.',
  ('v4_dontmove.jpg', 1.0, (0.5, 0.5), [("DON'T", WHT, 260, 290, 225), ('MOVE', YEL, 260, 560, 255)])),
 ('fix1_v4_dontmove_B_move.png', None, 'Would You Survive a Grizzly Attack? (Meatball Tried)', 'fix1_dontmove_B_one-word.png',
  'Challenger B on the v4 art: same fix, one word.',
  ('v4_dontmove.jpg', 1.0, (0.5, 0.5), [('MOVE?', YEL, 300, 450, 225)])),
 ('fix1_v4_lf_cH3HCZ8GlHk.png', 'cH3HCZ8GlHk', '3 Bugs in Your House You Should Never Kill (And 4 You Must)', 'fix1_lf_cH3HCZ8GlHk_3-bugs-never-kill.png',
  'No Meatball reaction and no reason to keep it: now he gasps at a centipede catching a roach, arrow to the centipede.',
  ('v4_centipede.jpg', 1.0, (0.5, 0.5), [('KEEP', WHT, 1020, 160, 165), ('THIS', YEL, 1020, 340, 185), ('ONE', WHT, 1020, 515, 165)], [('arrow', 880, 290, 690, 250)])),
 ('fix1_v4_lf_KWOM2-mNmww.png', 'KWOM2-mNmww', "Don't Kill the Spider in Your Corner. It Eats Bigger Spiders", 'fix1_lf_KWOM2-mNmww_corner-spider.png',
  'Text repeated the title and the spider sat out of his eye line: now he freezes mid-swing below the skinny spider wrapping a bigger one, WAIT! + arrow.',
  ('v4_corner_spider.jpg', 1.0, (0.5, 0.5), [('WAIT!', RED, 280, 400, 290)], [('arrow', 520, 200, 840, 240, BLK)])),
 ('fix1_v4_lf_xeAsg5ECpgw.png', 'xeAsg5ECpgw', '3 More Bugs in Your House You Should Never Kill (And 5 You Must)', 'fix1_lf_xeAsg5ECpgw_3-more-bugs.png',
  'The real culprit was hidden: now the larvae are visible in the sweater holes and circled, shock face, the innocent moth above.',
  ('v4_moth.jpg', 1.0, (0.5, 0.5), [('NOT', WHT, 260, 200, 180), ('THE', WHT, 260, 380, 160), ('MOTH', YEL, 260, 580, 215)], [('circle', 742, 538, 85)])),
 ('fix1_v4_lf_Lid8JXhg1Q4.png', 'Lid8JXhg1Q4', '6 Creatures Living in Your House Right Now (You Never See Them)', 'fix1_lf_Lid8JXhg1Q4_6-creatures.png',
  'Mites were a brown blob on his head: now a magnifier reveals them on the pillow next to his screaming face.',
  ('v4_bed.jpg', 1.0, (0.5, 0.5), [('IN', WHT, 250, 200, 185), ('YOUR', WHT, 250, 385, 185), ('BED', YEL, 250, 590, 225)])),
 ('fix1_v4_lf_bqij8Ht6SX4.png', 'bqij8Ht6SX4', 'Every Bug in Your House, Ranked From Harmless to Nightmare', 'fix1_lf_bqij8Ht6SX4_every-bug-ranked.png',
  'Showed the answer (recluse) so no curiosity gap: now #1 is a glowing silhouette on a podium, terrified Meatball below.',
  ('v4_ranked.jpg', 1.0, (0.5, 0.5), [("WHO'S", WHT, 270, 270, 205), ('#1?', RED, 270, 530, 265)])),
]
rows = []
for file, vid, title, old, diag, args in ITEMS:
    im = thumb(*args); im.save(os.path.join(OUT, file)); im.resize((168, 94), Image.LANCZOS).save(os.path.join(PH, file))
    rows.append((file, vid, title, old, diag))
FS = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15); FB = ImageFont.truetype(os.path.join(HERE, 'assets', F), 26)
RH = 230; sheet = Image.new('RGB', (1560, 70 + RH*len(rows)), '#0f0f0f'); d = ImageDraw.Draw(sheet)
d.text((10, 16), 'BEFORE (fix1)', font=FB, fill='#ff6b6b'); d.text((300, 16), 'AFTER (v4, not live)', font=FB, fill='#7CFF6B'); d.text((590, 16), 'phone 168x94: before | after   + what was missing', font=FB, fill='#aaaaaa')
for i, (file, vid, title, old, diag) in enumerate(rows):
    y = 70 + i*RH; b = Image.open(os.path.join(FX, old)).convert('RGB'); a = Image.open(os.path.join(OUT, file))
    sheet.paste(b.resize((272, 153), Image.LANCZOS), (10, y)); sheet.paste(a.resize((272, 153), Image.LANCZOS), (300, y))
    sheet.paste(b.resize((168, 94), Image.LANCZOS), (590, y)); sheet.paste(a.resize((168, 94), Image.LANCZOS), (770, y))
    d.text((950, y), textwrap.shorten(title, 62), font=FS, fill='#f1f1f1')
    d.text((950, y + 26), textwrap.fill('Missing: ' + diag, 64), font=FS, fill='#ffd23f')
sheet.save(os.path.join(OUT, 'fix1_thumbs_v4_sheet.png')); print('ok', len(rows))
