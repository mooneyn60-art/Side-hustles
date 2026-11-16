"""Channel banner for fix batch 1: 2560x1440, everything that matters inside YouTube's 1546x423 all-device safe area."""
import os, sys, skia, numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(__file__))
from kit import text_outlined
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = sys.argv[1]
BW, BH = 2560, 1440; SX, SY, SW, SH = (BW - 1546)//2, (BH - 423)//2, 1546, 423
s = skia.Surface(BW, BH); cv = s.getCanvas()
im = Image.open(os.path.join(HERE, 'art', 'banner_art_v3.jpg')).convert('RGBA').resize((BW, BH), Image.LANCZOS)
cv.drawImage(skia.Image.fromarray(np.array(im), colorType=skia.kRGBA_8888_ColorType), 0, 0)
for (x0, x1, lines) in ((SX + 10, SX + 520, [('MEATBALL', '#ffffff', 112), ('MYTHS', '#FFD21F', 130)]),
                        (SX + SW - 560, SX + SW - 10, [('BUGS IN YOUR HOUSE.', '#ffffff', 58), ('ANIMALS THAT', '#ffffff', 58), ('COULD END YOU.', '#FFD21F', 64)])):
    r = skia.RRect.MakeRectXY(skia.Rect(x0, SY + 40, x1, SY + SH - 40), 28, 28)
    p = skia.Paint(Color=skia.Color(10, 10, 10, 215), AntiAlias=True); cv.drawRRect(r, p)
    pe = skia.Paint(Color=skia.Color(0, 0, 0), Style=skia.Paint.kStroke_Style, StrokeWidth=8, AntiAlias=True); cv.drawRRect(r, pe)
    tot = sum(px*1.08 for _, _, px in lines); y = SY + SH/2 - tot/2
    for t, col, px in lines:
        y += px*1.0; text_outlined(cv, t, (x0 + x1)/2, y, px, col, '#000', px*0.12, 'Anton-Regular.ttf'); y += px*0.08
out = Image.fromarray(s.makeImageSnapshot().toarray()[:, :, [2, 1, 0]]).convert('RGB'); out.save(os.path.join(OUT, 'fix1_channel_banner_2560x1440.jpg'), quality=92)
chk = out.copy(); d = ImageDraw.Draw(chk); d.rectangle([SX, SY, SX + SW, SY + SH], outline='#00ff66', width=6)
d.rectangle([(BW - 2560)//2, SY, BW, SY + SH], outline='#ff3b3b', width=3)
chk.resize((1280, 720)).save(os.path.join(OUT, 'fix1_channel_banner_safe-area-check.jpg'))
out.crop((SX, SY, SX + SW, SY + SH)).save(os.path.join(OUT, 'fix1_channel_banner_mobile-crop.jpg'))
print('ok')
