"""v2 thumbnails (1280x720): art generated from art/meatball_ref_sheet_v1.jpg on a flat clean background,
one big Meatball emotion + one dominant threat, 2 words max in bold outlined text. Also writes 168x94 phone-size checks."""
import os, sys, skia, numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from kit import C, text_outlined
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
TW, TH = 1280, 720
def base(art):
    s = skia.Surface(TW, TH); cv = s.getCanvas()
    a = np.array(Image.open(os.path.join(HERE, 'art', art)).convert('RGBA').resize((TW, TH), Image.LANCZOS))
    cv.drawImage(skia.Image.fromarray(a, colorType=skia.kRGBA_8888_ColorType), 0, 0); return s, cv
def save(s, name):
    im = Image.fromarray(s.makeImageSnapshot().toarray()[:, :, [2, 1, 0]]).convert('RGB'); im.save(os.path.join(OUT, name))
    im.resize((168, 94), Image.LANCZOS).save(os.path.join(OUT, 'phone_check', name))
os.makedirs(os.path.join(OUT, 'phone_check'), exist_ok=True)
F = 'Anton-Regular.ttf'
s, cv = base('thumb_art_tooslow.jpg')   # 1: TOO SLOW (chase): terror face + bear jaws
text_outlined(cv, 'TOO', 160, 170, 165, '#ffffff', '#000', 28, F, rot=-5)
text_outlined(cv, 'SLOW', 470, 150, 165, '#E0201B', '#000', 28, F, rot=-5)   # words top, out of the bottom-right timestamp zone
save(s, 'thumb_v2_1_too-slow.png')
s, cv = base('thumb_art_playdead.jpg')  # 2: PLAY DEAD? (sniff test)
text_outlined(cv, 'PLAY', 255, 300, 230, '#FFD21F', '#000', 30, F, rot=-4)
text_outlined(cv, 'DEAD?', 265, 560, 230, '#E0201B', '#000', 30, F, rot=-4)
save(s, 'thumb_v2_2_play-dead.png')
s, cv = base('thumb_art_peek.jpg')      # 3: PLAY DEAD? variant: one eye peeking inside the jaws
text_outlined(cv, "DON'T", 270, 300, 220, '#ffffff', '#000', 30, F, rot=-4)
text_outlined(cv, 'MOVE', 270, 560, 250, '#FFD21F', '#000', 30, F, rot=-4)
save(s, 'thumb_v2_3_dont-move.png')
print('ok')
