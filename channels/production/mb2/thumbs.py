"""Sample thumbnails (1280x720): one big emotional subject, 2-3 words, high contrast (packaging spec)."""
import skia, numpy as np, os, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from kit import C, fill, stroke, text_outlined, path_poly
from characters import meatball, quadruped
import render as R
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
TW, TH = 1280, 720
def save(s, name): Image.fromarray(s.makeImageSnapshot().toarray()[:, :, [2, 1, 0, 3]]).convert('RGB').save(os.path.join(OUT, name))
# A: rig, bright, bear lunging at a terrified Meatball
s = skia.Surface(TW, TH); cv = s.getCanvas()
cv.drawPaint(skia.Paint(Shader=skia.GradientShader.MakeRadial((900, 330), 900, [C('#ffe066'), C('#ff7a00')])))
quadruped(cv, 360, 1100, 2.1, 'grizzly', jaw=1.0, look=(-0.4, 0.4))
meatball(cv, 250, 470, 1.55, {'face': 'shock', 'arms': 'up', 'sweat': True, 'lean': -10, 'look': (1, -0.5)})
text_outlined(cv, "DON'T RUN", 900, 150, 150, '#ffffff', '#000', 22, rot=-4)
save(s, 'thumb_A_rig-v2.png')
# B: illustrated chase panel, 2 words
s = skia.Surface(TW, TH); cv = s.getCanvas(); img = R.panel('p3_chase.jpg')
cv.save(); sc = TW / img.width() * 1.0; cv.scale(sc, sc); cv.translate(0, -img.height()*0.30); cv.drawImage(img, 0, 0, skia.SamplingOptions(skia.FilterMode.kLinear)); cv.restore()
text_outlined(cv, 'TOO SLOW', 960, 170, 140, '#ffd23f', '#000', 22, rot=-5)
save(s, 'thumb_B_illustrated.png')
# B2: play-dead panel with a question
s = skia.Surface(TW, TH); cv = s.getCanvas(); img = R.panel('p4_playdead.jpg')
cv.drawPaint(fill('#f4f8fb'))
cv.save(); sc = TH / (img.height()*0.62); cv.translate(640, 0); cv.scale(sc, sc); cv.translate(-img.width()*0.5, -img.height()*0.28); cv.drawImage(img, 0, 0, skia.SamplingOptions(skia.FilterMode.kLinear)); cv.restore()
text_outlined(cv, 'PLAY', 230, 300, 150, '#1b8a3a', '#000', 20); text_outlined(cv, 'DEAD?', 230, 470, 150, '#e0241c', '#000', 20)
save(s, 'thumb_B2_illustrated-question.png')
print('ok')
