#!/usr/bin/env python3
"""mb2 renderer: one script -> one 1080x1920 Short in three candidate styles.
  rig     fully procedural vector (Meatball puppet rig + species rigs, parallax, camera, FX)
  panels  illustrated key-art panels with motion (Ken Burns, punch-ins, shake, flashes)
  hybrid  panels for the money shots, rig animation for the action beats
Usage: render.py STYLE OUT.mp4 [--label TEXT] [--frames N]   (episode: Would Meatball Survive? #3, grizzly)
Audio follows channels/production-spec-audio-v2.md (wpm ~200, ducked bed, -14 LUFS two-pass)."""
import json, math, os, subprocess, sys
import numpy as np, skia
from PIL import Image
from kit import W, H, FPS, C, fill, stroke, lerp, clamp, ease_out, ease_in_out, back_out, spring, wobble, text_outlined, smooth_path, path_poly, font, INK
from characters import meatball, quadruped
import audio

HERE = os.path.dirname(os.path.abspath(__file__)); WORK = os.path.join(HERE, 'episodes', 'grizzly-wms-3')
EP = dict(text=["You can't outrun a grizzly. Bears can run as fast as a racehorse.", "Meatball ran anyway. Meatball is not a racehorse. Bears will chase what runs, like dogs.", "If a surprised grizzly knocks you down, play dead, hands behind your neck.", "If it keeps going, or it stalked you, fight like hell.", "Meatball lived. Nothing's guaranteed, because"],
    lines=[f'{WORK}/v{i}' for i in range(1, 6)], gaps=[0, 0.16, 0.18, 0.16, 0.28],
    cap_key={'grizzly', 'racehorse', 'meatball', 'chase', 'dead', 'knocks', 'neck', 'fight', 'hell', 'lived', 'guaranteed', 'outrun', 'dogs', 'bears'},
    cards=[  # (beat, anchor word, rows)
        (0, 'racehorse', [('FAST AS A RACEHORSE', '#ff4b3e', 92), ('UPHILL AND DOWN: U.S. PARK SERVICE', '#ffffff', 40)]),
        (2, 'play', [('PLAY DEAD', '#7CFF6B', 104), ('ONLY IF IT KNOCKS YOU DOWN', '#ffffff', 44), ('STOMACH DOWN, HANDS BEHIND YOUR NECK', '#ffffff', 34)]),
        (3, 'If', [('FIGHT BACK', '#ff4b3e', 104), ('IF IT KEEPS GOING OR STALKED YOU', '#ffffff', 40), ("BLACK BEAR: DON'T PLAY DEAD (PARK SERVICE)", '#ffd23f', 34)]),
        (4, 'Meatball', [('EVER MET A BEAR? COMMENT', '#ffd23f', 64)]),
    ])

# ------------------------------------------------------------------ timeline helpers
import re
def norm(s): return re.sub(r'[^a-z]', '', s.lower())
class TL:
    def __init__(self, words, spans, dur):
        self.words, self.spans, self.dur = words, spans, dur
    def w(self, beat, word, n=1):
        k = 0
        for x in self.words:
            if x['beat'] == beat and norm(x['w']).startswith(norm(word)) and (len(norm(x['w'])) - len(norm(word))) <= 1:
                k += 1
                if k == n: return x['t']
        raise KeyError((beat, word))
    def b0(self, i): return self.spans[i][0]
    def b1(self, i): return self.spans[i][1] if i < len(self.spans) else self.dur

# ------------------------------------------------------------------ backgrounds (rig)
def bg_forest(cv, camx, t, tint=None, snow=False):
    sky = skia.GradientShader.MakeLinear([(0, 0), (0, H)], [C('#bfe3f2') if not snow else C('#dfe9f2'), C('#f3f0d8') if not snow else C('#ffffff')])
    cv.drawPaint(skia.Paint(Shader=sky))
    # far mountains
    for layer, (col, par, base, amp) in enumerate([('#9cc3b9', 0.15, 900, 160), ('#6f9f8a', 0.35, 1030, 120)]):
        if snow: col = ['#c9d6e3', '#aebfd0'][layer]
        pts = [(-200, H)]
        for i in range(0, 15):
            x = i*120 - (camx*par) % 240 - 120
            pts.append((x, base - amp*(0.5 + 0.5*math.sin(i*1.7 + layer))))
        pts.append((W + 300, H)); cv.drawPath(path_poly(pts), fill(col))
    # mid trees (parallax 0.6) and near trees (1.0)
    for par, col, sc, y0 in ((0.6, '#3f7a52' if not snow else '#4b7a64', 0.8, 1180), (1.0, '#2c5e3c' if not snow else '#355e4c', 1.15, 1300)):
        span = 260*sc
        off = (camx*par) % span
        for i in range(-1, int(W/span) + 3):
            x = i*span - off; hh = 520*sc
            cv.drawRect(skia.Rect(x - 14*sc, y0 - 60*sc, x + 14*sc, y0 + 40), fill('#5b3a22'))
            for k in range(3):
                w2 = (120 - k*30)*sc; yy = y0 - 60*sc - k*130*sc
                p = path_poly([(x - w2, yy), (x, yy - 210*sc), (x + w2, yy)])
                cv.drawPath(p, fill(col)); cv.drawPath(p, stroke(INK, 7))
                if snow: cv.drawPath(path_poly([(x - w2*0.4, yy - 120*sc), (x, yy - 210*sc), (x + w2*0.4, yy - 120*sc)]), fill('#ffffff'))
    ground = '#8a6a43' if not snow else '#f4f8fb'
    cv.drawRect(skia.Rect(0, 1320, W, H), fill(ground))
    cv.drawLine(0, 1320, W, 1320, stroke(INK, 8))
    for i in range(14):  # ground marks scroll at 1.2x
        x = (i*170 - camx*1.25) % (W + 200) - 100
        cv.drawLine(x, 1420 + (i % 3)*90, x + 60, 1420 + (i % 3)*90, stroke(C('#000000', 40), 8))
    if tint: cv.drawPaint(fill(tint))
def bg_burst(cv, t, col1='#c4161c', col2='#7a0a0e', spin=0.2):
    cv.drawPaint(fill(col2))
    cx, cy = W/2, H*0.42
    for i in range(24):
        a0 = i/24*2*math.pi + t*spin; a1 = a0 + math.pi/24
        cv.drawPath(path_poly([(cx, cy), (cx + math.cos(a0)*2400, cy + math.sin(a0)*2400), (cx + math.cos(a1)*2400, cy + math.sin(a1)*2400)]), fill(col1))
def speed_lines(cv, t, n=26, horiz=True, alpha=160, seed=0):
    rs = np.random.default_rng(seed + int(t*20))
    for i in range(n):
        y = rs.uniform(150, H - 150); x = rs.uniform(-200, W); L = rs.uniform(200, 600)
        if horiz: cv.drawLine(x, y, x + L, y, stroke(C('#ffffff', alpha), rs.uniform(4, 10)))
def radial_lines(cv, t, cx=W/2, cy=H*0.45, alpha=150, seed=0):
    rs = np.random.default_rng(seed + int(t*15))
    for i in range(70):
        a = rs.uniform(0, 2*math.pi); r0 = rs.uniform(520, 760); r1 = r0 + rs.uniform(300, 900)
        cv.drawLine(cx + math.cos(a)*r0, cy + math.sin(a)*r0, cx + math.cos(a)*r1, cy + math.sin(a)*r1, stroke(C('#ffffff', alpha), rs.uniform(3, 9)))
def mark(cv, x, y, s, kind, t):
    """'!' surprise / 'stars' dizzy / 'pow' comic letters."""
    sc = back_out(clamp(t/0.25))*s
    cv.save(); cv.translate(x, y); cv.scale(sc, sc)
    if kind == '!':
        text_outlined(cv, '!', 0, 0, 220, '#ffd23f', '#000', 18, 'Bangers-Regular.ttf')
    elif kind == 'stars':
        for k in range(3):
            a = t*6 + k*2.1; sx, sy = math.cos(a)*90, math.sin(a)*30
            text_outlined(cv, '*', sx, sy, 90, '#ffd23f', '#000', 10, 'Bangers-Regular.ttf')
    elif kind == 'pow':
        star = [(math.cos(i/16*2*math.pi)*(260 if i % 2 == 0 else 160), math.sin(i/16*2*math.pi)*(200 if i % 2 == 0 else 120)) for i in range(16)]
        p = path_poly(star); cv.drawPath(p, fill('#ffd23f')); cv.drawPath(p, stroke(INK, 12))
        text_outlined(cv, 'POW!', 0, 50, 150, '#ff3b2f', '#000', 16, 'Bangers-Regular.ttf', rot=-8)
    cv.restore()

# ------------------------------------------------------------------ panels (illustrated)
_imgs = {}
def panel(name):
    if name not in _imgs:
        im = Image.open(os.path.join(HERE, 'art', name)).convert('RGBA')
        if name == 'p1_roar.jpg':  # bottom 28% of this one is blank: keep the drawn part
            im = im.crop((0, 0, im.width, int(im.height*0.715)))
        a = np.array(im); _imgs[name] = skia.Image.fromarray(a, colorType=skia.kRGBA_8888_ColorType)
    return _imgs[name]
def draw_panel(cv, name, u, z0, z1, c0, c1, rot=0.0):
    """Ken Burns: zoom z0->z1 and centre c0->c1 (fractions of the image) over u in 0..1, cover-fit."""
    img = panel(name); iw, ih = img.width(), img.height()
    k = ease_in_out(u); z = lerp(z0, z1, k); cx = lerp(c0[0], c1[0], k)*iw; cy = lerp(c0[1], c1[1], k)*ih
    base = max(W/iw, H/ih); s = base*z
    cv.save(); cv.translate(W/2, H/2); cv.rotate(rot); cv.scale(s, s); cv.translate(-cx, -cy)
    cv.drawImage(img, 0, 0, skia.SamplingOptions(skia.FilterMode.kLinear, skia.MipmapMode.kLinear)); cv.restore()

# ------------------------------------------------------------------ overlays
def captions(cv, tl, t, keys, y=1430):
    """Kinetic captions: 1-3 word groups that pop on with a spring, keyword in yellow, bigger and centred."""
    groups, cur = [], []
    for x in tl.words:
        cur.append(x)
        end = x['w'][-1:] in ',.?!' or len(cur) == 3 or x['w'].strip('.,').lower() in keys
        if end: groups.append(cur); cur = []
    if cur: groups.append(cur)
    for gi, g in enumerate(groups):
        t0 = g[0]['t']; t1 = groups[gi + 1][0]['t'] if gi + 1 < len(groups) else g[-1]['t'] + g[-1]['d'] + 0.3
        if t0 <= t < t1:
            u = t - t0; sc = 0.6 + 0.4*spring(u*1.6, 2.6, 7)
            words = [x['w'].upper().rstrip('.,!?') for x in g]
            f = font('Anton-Regular.ttf', 112)
            widths = [f.measureText(w + ' ') for w in words]; tw = sum(widths)
            cv.save(); cv.translate(W/2, y); cv.scale(sc, sc)
            x = -tw/2
            for w, ww, src in zip(words, widths, g):
                key = w.strip('.,!?').lower() in keys
                text_outlined(cv, w, x + ww/2, 0, 112 if not key else 124, '#ffd23f' if key else '#ffffff', '#000', 20, center=True)
                x += ww
            cv.restore()
def cards(cv, tl, t, spec):
    for i, (beat, word, rows) in enumerate(spec):
        t0 = tl.w(beat, word); t1 = tl.b1(beat) + (0.15 if beat < 4 else 1.0)
        if beat == 0: t1 = tl.b1(0)
        if not (t0 <= t < t1): continue
        u = t - t0; y = 300
        for j, (txt, col, px) in enumerate(rows):
            uj = clamp((u - j*0.12)/0.35)
            if uj <= 0: continue
            sc = back_out(uj)
            if j == 0:
                text_outlined(cv, txt, W/2, y + px*0.8, px, col, '#000', px*0.17, scale=sc, rot=-2*(1 - uj))
                y += px*1.05
            else:
                f = font('Anton-Regular.ttf', px); tw = f.measureText(txt)
                cv.save(); cv.translate(W/2, y + px*0.6); cv.scale(sc, sc)
                r = skia.RRect.MakeRectXY(skia.Rect(-tw/2 - 24, -px*0.95, tw/2 + 24, px*0.45), 18, 18)
                cv.drawRRect(r, fill(C('#111111', 225)))
                text_outlined(cv, txt, 0, 0, px, col, '#000', 0)
                cv.restore(); y += px*1.45
def label(cv, text):
    if not text: return
    f = font('Anton-Regular.ttf', 48); tw = f.measureText(text)
    r = skia.RRect.MakeRectXY(skia.Rect(24, 1790, 24 + tw + 40, 1866), 16, 16)
    cv.drawRRect(r, fill(C('#000000', 190))); text_outlined(cv, text, 44, 1846, 48, '#ffffff', '#000', 0, center=False)
def flash(cv, t, at, d=0.1):
    if at <= t < at + d: cv.drawPaint(fill(C('#ffffff', int(255*(1 - (t - at)/d)))))

# ------------------------------------------------------------------ the shots
def shots(tl):
    B = tl.b0; E = tl.b1; Wd = tl.w
    return [  # (start, end, rig_shot, panel_shot, hybrid_uses_panel)
        (0, Wd(0, 'Bears'), 'roar_cu', ('p1_roar.jpg', 1.18, 1.32, (0.5, 0.42), (0.5, 0.40)), True),
        (Wd(0, 'Bears'), Wd(0, 'racehorse'), 'gallop', ('p3_chase.jpg', 2.4, 2.7, (0.66, 0.42), (0.64, 0.40)), False),
        (Wd(0, 'racehorse'), B(1), 'race', ('p2_horse.jpg', 1.35, 1.25, (0.40, 0.52), (0.60, 0.50)), False),
        (B(1), Wd(1, 'is'), 'mb_cu', ('p3_chase.jpg', 1.9, 2.2, (0.32, 0.64), (0.33, 0.62)), False),
        (Wd(1, 'is'), Wd(1, 'Bears'), 'treadmill', ('p3_chase.jpg', 1.0, 1.12, (0.5, 0.5), (0.5, 0.55)), False),
        (Wd(1, 'Bears'), Wd(1, 'like'), 'eye_cu', ('p1_roar.jpg', 2.6, 3.0, (0.5, 0.30), (0.5, 0.29)), False),
        (Wd(1, 'like'), B(2), 'chase', ('p3_chase.jpg', 1.15, 1.0, (0.55, 0.45), (0.5, 0.5)), False),
        (B(2), Wd(2, 'knocks'), 'surprise', ('p4_playdead.jpg', 2.0, 2.3, (0.58, 0.45), (0.56, 0.47)), False),
        (Wd(2, 'knocks'), Wd(2, 'play'), 'knock', ('p4_playdead.jpg', 1.6, 1.2, (0.45, 0.6), (0.5, 0.55)), False),
        (Wd(2, 'play'), B(3), 'playdead', ('p4_playdead.jpg', 1.05, 1.15, (0.5, 0.55), (0.48, 0.58)), True),
        (B(3), Wd(3, 'fight'), 'loom', ('p5_fight.jpg', 1.9, 1.35, (0.45, 0.25), (0.5, 0.45)), True),
        (Wd(3, 'fight'), B(4), 'fight', ('p5_fight.jpg', 1.15, 1.45, (0.5, 0.62), (0.5, 0.72)), True),
        (B(4), Wd(4, 'Nothing'), 'lived', ('p6_lived.jpg', 1.0, 1.15, (0.5, 0.55), (0.5, 0.58)), False),
        (Wd(4, 'Nothing'), tl.dur + 0.01, 'roar_cu', ('p1_roar.jpg', 1.32, 1.18, (0.5, 0.40), (0.5, 0.42)), True),
    ]

def rig_shot(cv, name, t, u, d, mouth, tl):
    """t = global time, u = time into the shot, d = shot length."""
    blink = 1.0 if (t % 3.1) < 0.09 else 0.0
    if name == 'roar_cu':
        bg_forest(cv, 40*u, t)
        cv.save(); sh = 14*math.exp(-u*2.5); cv.translate(wobble(t, 1, sh, 9), wobble(t, 2, sh, 9))
        z = 1 + 0.06*u; cv.translate(W/2, H/2); cv.scale(z, z); cv.translate(-W/2, -H/2)
        quadruped(cv, -40, 1480, 2.5, 'grizzly', jaw=0.55 + 0.45*abs(math.sin(u*7)), look=(-0.6, 0.4))
        radial_lines(cv, t, W*0.62, H*0.30, 120)
        meatball(cv, 250, 1580, 1.4, {'face': 'shock', 'arms': 'up', 'sweat': True, 'mouth': mouth, 'lean': -12 - 4*math.sin(u*20), 'look': (1, -0.6), 'squash': (1.08, 0.92)})
        cv.restore()
    elif name == 'gallop':
        bg_forest(cv, 2400*u, t); speed_lines(cv, t)
        quadruped(cv, 470 + 30*math.sin(u*3), 1500, 1.5, 'grizzly', run=u*15, jaw=0.4)
    elif name == 'race':
        bg_forest(cv, 2600*u, t); speed_lines(cv, t, 18)
        quadruped(cv, 560, 1060, 1.05, 'horse', run=u*14 + 1)
        quadruped(cv, 520, 1680, 1.2, 'grizzly', run=u*15, jaw=0.3)
        text_outlined(cv, '=', 900, 1330, 200, '#ffd23f', '#000', 18, 'Bangers-Regular.ttf', scale=back_out(clamp(u/0.3)))
    elif name == 'mb_cu':
        bg_forest(cv, 0, t)
        k = clamp(u/(d*0.7)); z = lerp(2.2, 2.5, k)
        cv.save(); cv.translate(W/2, H*0.55); cv.scale(z, z)
        dx = 0 if u < d - 0.25 else (u - (d - 0.25))*4000  # zips out of frame
        meatball(cv, dx, 0, 1.0, {'face': 'scared', 'sweat': True, 'mouth': mouth, 'blink': blink, 'look': (-1, 0), 'squash': (1 + 0.04*math.sin(u*30), 1 - 0.04*math.sin(u*30))})
        cv.restore()
        if u > d - 0.25: speed_lines(cv, t, 30)
    elif name == 'treadmill':  # legs a blur, background barely moves: he is not a racehorse
        bg_forest(cv, 120*u, t)
        meatball(cv, 540, 1180, 1.75, {'face': 'scared', 'run': u*38, 'mouth': mouth, 'sweat': True, 'lean': 14, 'look': (1, 0)})
        for k in range(4): cv.drawCircle(300 - k*60 - (u*200 % 60), 1470 - k*10, 30 - k*5, fill(C('#d9c7a0', 200 - k*40)))
    elif name == 'eye_cu':
        cv.drawPaint(fill('#4f3220'))
        cv.save(); z = lerp(1.0, 1.15, u/d); cv.translate(W/2, H/2); cv.scale(z, z)
        cv.drawOval(skia.Rect(-330, -170, 330, 170), fill('#ffffff')); cv.drawOval(skia.Rect(-330, -170, 330, 170), stroke(INK, 18))
        pr = lerp(120, 70, clamp(u/0.4)); cv.drawCircle(0, 0, pr, fill(INK)); cv.drawCircle(-30, -40, 24, fill('#ffffff'))
        lid = clamp(u/0.35)*120
        cv.drawRect(skia.Rect(-360, -220, 360, -170 + lid), fill('#4f3220'))
        cv.drawLine(-360, -150 + lid*0.4, 320, -230 + lid, stroke(INK, 30))
        cv.restore(); radial_lines(cv, t, W/2, H/2, 90)
    elif name == 'chase':
        bg_forest(cv, 2200*u, t); speed_lines(cv, t, 16)
        meatball(cv, 850, 1230, 1.4, {'face': 'scared', 'run': u*30, 'mouth': mouth, 'sweat': True, 'lean': 16, 'look': (-1, 0)})
        quadruped(cv, 200 + 90*u, 1560, 1.3, 'grizzly', run=u*15, jaw=0.6)
    elif name == 'surprise':
        bg_forest(cv, 0, t, snow=True)
        quadruped(cv, 780, 1600, 1.6, 'grizzly', jaw=0.15, mood='surprised', flip=True, look=(-1, 0), blink=blink)
        meatball(cv, 210, 1300, 1.4, {'face': 'shock', 'mouth': mouth, 'look': (1, 0), 'arms': 'up'})
        if u > 0.15: mark(cv, 640, 760, 1.0, '!', u - 0.15)
    elif name == 'knock':
        bg_forest(cv, 0, t, snow=True)
        cv.save(); sh = 26*math.exp(-u*4); cv.translate(wobble(t, 3, sh, 14), wobble(t, 4, sh, 14))
        quadruped(cv, 820, 1600, 1.6, 'grizzly', jaw=0.5, flip=True)
        k = ease_out(clamp(u/0.35))
        meatball(cv, lerp(330, 170, k), lerp(1300, 1420, k), 1.4, {'face': 'hurt', 'dizzy': u > 0.3, 'lean': -95*k, 'legs': 'kick', 'arms': 'up'})
        if u > 0.3: mark(cv, 170, 1220, 1.0, 'stars', u - 0.3)
        cv.restore()
        if u < 0.06: cv.drawPaint(fill(C('#000000', 255))); meatball(cv, 330, 1330, 1.1, {'face': 'hurt'})  # impact frame
    elif name == 'playdead':
        bg_forest(cv, 0, t, snow=True)
        cv.save(); cv.translate(380, 1450); cv.rotate(-90)
        meatball(cv, 0, 0, 1.45, {'face': 'hurt', 'blink': 1.0, 'arms': 'behind_neck', 'legs': 'kick'})
        cv.restore()
        sn = math.sin(u*9)*12
        quadruped(cv, 900 + sn, 1640, 1.45, 'grizzly', mood='surprised', flip=True, look=(-1, 0.6), jaw=0.05)
        cv.drawCircle(500 + sn, 1240, 10 + 4*math.sin(u*18), fill(C('#ffffff', 180)))
    elif name == 'loom':
        bg_burst(cv, t)
        cv.save(); z = lerp(1.25, 1.0, ease_out(u/d)); cv.translate(W/2, H); cv.scale(z, z); cv.translate(-W/2, -H)
        quadruped(cv, 520, 1900, 1.9, 'grizzly', jaw=0.6 + 0.3*math.sin(u*6), rear=0.55)
        cv.restore()
        pulse = int(60 + 60*abs(math.sin(u*8))); cv.drawPaint(fill(C('#ff0000', pulse//3)))
        meatball(cv, 250, 1600, 0.9, {'face': 'scared', 'mouth': mouth, 'sweat': True, 'look': (1, -1)})
    elif name == 'fight':
        bg_burst(cv, t, '#ffcc33', '#ff8a00', 0.8); radial_lines(cv, t, W/2, H*0.55, 200)
        cv.save(); sh = 22*math.exp(-u*3); cv.translate(wobble(t, 5, sh, 15), wobble(t, 6, sh, 15))
        jump = -abs(math.sin(u*9))*120
        meatball(cv, 540, 1250 + jump, 2.0, {'face': 'determined', 'arms': 'fists', 'mouth': mouth, 'squash': (0.92, 1.08) if jump < -60 else (1.1, 0.9)})
        if u > 0.25: mark(cv, 760, 620, 1.0, 'pow', u - 0.25)
        cv.restore()
    elif name == 'lived':
        bg_forest(cv, 30*u, t, tint=C('#ff9a3c', 50))
        meatball(cv, 540, 1180, 1.8, {'face': 'happy', 'bandage': True, 'mouth': mouth, 'arms': (14, -14), 'blink': blink, 'lean': 6*math.sin(u*3)})

def render(style, out, label_text='', max_frames=None):
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    lines = [(p + '.mp3', p + '.words.json') for p in EP['lines']]
    voice, words, spans = audio.assemble(lines, EP['gaps'])
    for bi, txt in enumerate(EP['text']):  # restore punctuation from the script (TTS boundaries drop it)
        toks = txt.split(); ws = [x for x in words if x['beat'] == bi]
        if len(toks) == len(ws):
            for x, tk in zip(ws, toks): x['w'] = tk
    tmp = out + '.voice.wav'; audio.save(tmp, voice); audio.voice_chain(tmp, tmp + '.p.wav')
    voice = audio.load(tmp + '.p.wav'); dur = len(voice)/audio.SR + 0.35
    tl = TL(words, spans, dur); env = audio.envelope(voice)
    sh = shots(tl)
    # SFX plan (spec §4: whoosh only on location changes, one signature sting, comic hits)
    sfx = [(0.0, 'roar', -2), (tl.w(0, 'Bears') - 0.12, 'whoosh', -8), (tl.w(0, 'racehorse'), 'pop', -8),
           (tl.w(1, 'is') + 0.25, 'scratch', -10), (tl.w(1, 'Bears'), 'heart', -8), (tl.w(1, 'like') - 0.1, 'whoosh', -8),
           (tl.w(2, 'knocks'), 'impact', -3), (tl.w(2, 'play'), 'ding', -12), (tl.b0(3), 'heart', -6),
           (tl.w(3, 'fight'), 'impact', -4), (tl.w(3, 'fight') + 0.3, 'pop', -6), (tl.w(4, 'Nothing') - 0.1, 'whoosh', -8), (tl.dur - 0.9, 'roar', -6)]
    mixw = audio.mix(voice, sfx, dur); audio.save(out + '.mix.wav', mixw)
    n = int(dur*FPS) if not max_frames else max_frames
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgra', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-pix_fmt', 'yuv420p', out + '.video.mp4'], stdin=subprocess.PIPE)
    surf = skia.Surface(W, H); cv = surf.getCanvas()
    cuts = []
    for fi in range(n):
        t = fi/FPS; mouth = float(env[fi]) if fi < len(env) else 0.0
        for si, (a, b, rname, pnl, hyb) in enumerate(sh):
            if a <= t < b: break
        u, d = t - a, b - a
        cv.clear(C('#000000'))
        use_panel = style == 'panels' or (style == 'hybrid' and hyb)
        if use_panel:
            name, z0, z1, c0, c1 = pnl
            cv.save()
            shk = 0
            if rname in ('roar_cu', 'knock', 'fight'): shk = 16*math.exp(-u*3)
            cv.translate(wobble(t, 7, shk, 12), wobble(t, 8, shk, 12))
            draw_panel(cv, name, clamp(u/max(d, 0.01)), z0, z1, c0, c1, rot=wobble(t, 9, 0.6, 0.8))
            cv.restore()
            if rname == 'gallop' or rname == 'race': speed_lines(cv, t, 14, alpha=120)
            if rname == 'fight' and u > 0.25: mark(cv, 780, 560, 0.9, 'pow', u - 0.25)
            if rname == 'surprise' and u > 0.15: mark(cv, 600, 640, 0.9, '!', u - 0.15)
            if rname == 'knock' and u < 0.07: cv.drawPaint(fill(C('#ffffff', 230)))
        else:
            rig_shot(cv, rname, t, u, d, mouth, tl)
        # whip transition: 3-frame directional smear on every cut
        if u < 0.1 and si > 0:
            k = 1 - u/0.1; cv.drawPaint(fill(C('#ffffff', int(70*k))))
        cards(cv, tl, t, EP['cards'])
        captions(cv, tl, t, EP['cap_key'])
        # top series tag for the first 1.8 s
        if t < 1.8: text_outlined(cv, 'WOULD MEATBALL SURVIVE? #3', W/2, 150, 54, '#ffffff', '#000', 10, alpha=int(255*clamp((1.8 - t)/0.3)))
        label(cv, label_text)
        enc.stdin.write(surf.makeImageSnapshot().tobytes())
    enc.stdin.close(); enc.wait()
    audio.master(out + '.mix.wav', out + '.video.mp4', out)
    for f in (tmp, tmp + '.p.wav', out + '.mix.wav', out + '.video.mp4'):
        try: os.remove(f)
        except OSError: pass
    json.dump({'shots': [(round(a, 2), round(b, 2), r) for a, b, r, _, _ in sh], 'words': words, 'dur': dur}, open(out + '.timeline.json', 'w'), indent=0)
    print('wrote', out, round(dur, 2), 's')

if __name__ == '__main__':
    a = sys.argv[1:]; lab = ''; mf = None
    if '--label' in a: i = a.index('--label'); lab = a[i + 1]; del a[i:i + 2]
    if '--frames' in a: i = a.index('--frames'); mf = int(a[i + 1]); del a[i:i + 2]
    render(a[0], a[1], lab, mf)
