"""Puppet rigs: Meatball (squash/stretch, blinks, brows, lip flap, run cycle, poses) and a parametric
quadruped (grizzly, horse) with a gallop cycle, open jaw and cel shading. Units: Meatball body radius = 100."""
import math, random, skia
from kit import C, fill, stroke, shape, smooth_path, path_poly, INK, lerp, clamp

BROWN, BROWN_D, BROWN_L, SAUCE, SAUCE_D = '#8b4a2b', '#5e2f1a', '#b0673f', '#d8342c', '#9e1f19'
_rng = random.Random(7)
_LUMPS = [1 + _rng.uniform(-0.035, 0.035) for _ in range(18)]
_SPECKS = [(_rng.uniform(-70, 70), _rng.uniform(-60, 75), _rng.uniform(5, 11)) for _ in range(14)]

FACES = {  # brow angle L/R (deg, + = inner end down = angry), brow lift, mouth curve
    'neutral': (0, 0, 0.2), 'shock': (-18, 16, 0), 'scared': (-25, 10, -0.6), 'determined': (24, -4, -0.1),
    'smug': (8, -6, 0.7), 'hurt': (-20, 6, -0.8), 'happy': (-6, 8, 1.0), 'angry': (30, -8, -0.7)}

def limb(cv, x0, y0, a1, l1, a2, l2, w, end_r, end='hand'):
    """Two-segment stick limb; angles in degrees, 0 = straight down, + = toward +x."""
    r1, r2 = math.radians(a1), math.radians(a1 + a2)
    x1, y1 = x0 + math.sin(r1)*l1, y0 + math.cos(r1)*l1
    x2, y2 = x1 + math.sin(r2)*l2, y1 + math.cos(r2)*l2
    p = skia.Path(); p.moveTo(x0, y0); p.lineTo(x1, y1); p.lineTo(x2, y2)
    cv.drawPath(p, stroke(INK, w))
    if end == 'hand': cv.drawCircle(x2, y2, end_r, fill(INK))
    else:
        cv.save(); cv.translate(x2, y2); cv.rotate(math.degrees(-r2)*0.3)
        cv.drawOval(skia.Rect(-end_r*0.6, -end_r*0.55, end_r*1.6, end_r*0.55), fill(INK)); cv.restore()
    return x2, y2

def meatball(cv, x, y, size=1.0, st=None):
    """Draw Meatball with body centre at (x, y). size 1.0 -> body radius 100 px.
    st: face, look(dx,dy), blink 0..1, mouth 0..1, squash (sx, sy), lean deg, run phase or None,
    arms (aL, aR) deg or 'up'/'fists'/'behind_neck', legs 'stand'/'flat', sweat, bandage, flip, dizzy."""
    st = st or {}
    face = FACES.get(st.get('face', 'neutral'), FACES['neutral'])
    sx, sy = st.get('squash', (1.0, 1.0))
    run = st.get('run')
    bob = abs(math.sin(run)) * -14 if run is not None else 0
    cv.save(); cv.translate(x, y + bob*size); cv.scale(size, size)
    if st.get('flip'): cv.scale(-1, 1)
    cv.rotate(st.get('lean', 0))
    # ---- legs (behind body)
    legs = st.get('legs', 'stand')
    if run is not None:
        for k, ph in ((-1, run), (1, run + math.pi)):
            a = math.sin(ph) * 50; knee = max(0, -math.cos(ph)) * 70
            limb(cv, k*30, 90, a, 70, -knee, 70, 11, 26, 'foot')
    elif legs == 'stand':
        for k in (-1, 1): limb(cv, k*34, 92, k*8, 75, -k*6, 70, 11, 26, 'foot')
    elif legs == 'kick':
        limb(cv, -34, 92, -10, 75, 4, 70, 11, 26, 'foot'); limb(cv, 34, 92, 75, 75, 10, 75, 11, 26, 'foot')
    # ---- body (squash/stretch around the feet line keeps contact believable)
    cv.save(); cv.scale(sx, sy)
    pts = []
    for i, l in enumerate(_LUMPS):
        a = i / len(_LUMPS) * 2*math.pi
        pts.append((math.cos(a)*100*l, math.sin(a)*100*l))
    body = smooth_path(pts)
    cv.drawPath(body, fill(BROWN))
    cv.save(); cv.clipPath(body, doAntiAlias=True)
    cv.drawCircle(28, 40, 108, fill(BROWN_D)); cv.drawCircle(-10, -8, 96, fill(BROWN))  # cel shade crescent
    for (px, py, r) in _SPECKS: cv.drawCircle(px, py, r, fill(C(BROWN_D, 200)))
    cv.drawOval(skia.Rect(-62, -70, -22, -40), fill(C(BROWN_L, 220)))
    cv.restore()
    cv.drawPath(body, stroke(INK, 9))
    # sauce cap with drips
    sauce = smooth_path([(-62, -72), (-40, -98), (0, -108), (40, -98), (64, -70), (52, -52), (44, -40), (36, -55),
                         (14, -60), (4, -38), (-6, -60), (-30, -58), (-38, -44), (-48, -60)])
    shape(cv, sauce, SAUCE, 7)
    cv.drawOval(skia.Rect(-30, -98, 0, -86), fill(C('#ff8a7a', 200)))
    if st.get('bandage'):
        cv.save(); cv.rotate(-18); cv.drawRect(skia.Rect(-80, -20, 80, 2), fill('#f4ecd8')); cv.drawRect(skia.Rect(-80, -20, 80, 2), stroke(INK, 5)); cv.restore()
    # ---- arms
    arms = st.get('arms', (14, -14))
    if run is not None and arms in ((14, -14),):
        arms = (math.sin(run + math.pi)*60, math.sin(run)*60)
    cv.save(); cv.scale(1/sx, 1/sy)
    if arms == 'up':
        limb(cv, -80, 10, -145, 70, -15, 65, 10, 15); limb(cv, 80, 10, 145, 70, 15, 65, 10, 15)
    elif arms == 'fists':
        limb(cv, -82, 20, -55, 62, 125, 50, 10, 21); limb(cv, 82, 20, 55, 62, -125, 50, 10, 21)
    elif arms == 'behind_neck':
        limb(cv, -80, 0, -150, 60, 70, 55, 10, 15); limb(cv, 80, 0, 150, 60, -70, 55, 10, 15)
    elif arms == 'point':
        limb(cv, -82, 20, -20, 70, 10, 65, 10, 15); limb(cv, 82, 10, 95, 75, 5, 70, 10, 15)
    else:
        aL, aR = arms
        limb(cv, -84, 20, -abs(aL) if aL >= 0 else -aL, 72, -20, 66, 10, 15)
        limb(cv, 84, 20, abs(aR) if aR <= 0 else aR, 72, 20, 66, 10, 15)
    cv.restore()
    # ---- face
    lx, ly = st.get('look', (0, 0)); blink = clamp(st.get('blink', 0))
    for k in (-1, 1):
        ex, ey = k*34, -14
        ew, eh = 27, 32 * (1 - blink*0.92)
        if st.get('face') == 'shock': ew, eh = 31, 38 * (1 - blink*0.92)
        if st.get('dizzy'):
            cv.drawOval(skia.Rect(ex-ew, ey-32, ex+ew, ey+32), fill('#ffffff')); cv.drawOval(skia.Rect(ex-ew, ey-32, ex+ew, ey+32), stroke(INK, 6))
            p = skia.Path(); p.moveTo(ex-14, ey-14); p.lineTo(ex+14, ey+14); p.moveTo(ex+14, ey-14); p.lineTo(ex-14, ey+14)
            cv.drawPath(p, stroke(INK, 7)); continue
        r = skia.Rect(ex-ew, ey-eh, ex+ew, ey+eh)
        cv.drawOval(r, fill('#ffffff')); cv.drawOval(r, stroke(INK, 6))
        if blink < 0.7:
            pr = 12 if st.get('face') != 'shock' else 8
            cv.drawCircle(ex + lx*11, ey + ly*12, pr, fill(INK))
            cv.drawCircle(ex + lx*11 - 4, ey + ly*12 - 5, 3.5, fill('#ffffff'))
        # brow
        ba, lift, _ = face
        cv.save(); cv.translate(ex, ey - 44 - lift); cv.rotate(-ba * k)
        cv.drawLine(-22, 0, 22, 0, stroke(INK, 9)); cv.restore()
    # mouth: open amount from audio; closed curve from face
    m = clamp(st.get('mouth', 0)); curve = face[2]
    if m > 0.08 or st.get('face') in ('shock', 'scared'):
        mo = max(m, 0.45 if st.get('face') in ('shock', 'scared') else 0)
        mw, mh = 30 + 6*mo, 6 + 30*mo
        r = skia.Rect(-mw, 44 - mh*0.4, mw, 44 + mh*0.9)
        cv.drawOval(r, fill('#5a0f0f'))
        cv.save(); cv.clipRect(r); cv.drawOval(skia.Rect(-mw*0.6, 44 + mh*0.35, mw*0.6, 44 + mh*1.3), fill('#e2595a')); cv.restore()
        cv.drawOval(r, stroke(INK, 6))
    else:
        p = skia.Path(); p.moveTo(-26, 42); p.quadTo(0, 42 + curve*26, 26, 42); cv.drawPath(p, stroke(INK, 7))
    if st.get('sweat'):
        dp = smooth_path([(96, -60), (106, -34), (100, -22), (88, -24), (86, -38)])
        shape(cv, dp, '#8fd3ff', 5)
    cv.restore()  # body scale
    cv.restore()


# ------------------------------------------------------------------ quadrupeds

SPECS = {
    'grizzly': dict(col='#7a5236', dark='#4f3220', belly='#a07450', L=520, Hb=250, leg=135, legw=64, neck=0.0,
                    head=118, snout=0.8, ears='round', hump=0.55, tail=0.12, claws=True),
    'horse': dict(col='#c98a4b', dark='#8a5a2b', belly='#dba66e', L=470, Hb=170, leg=250, legw=30, neck=1.0,
                  head=60, snout=1.9, ears='point', hump=0.0, tail=1.0, claws=False, mane='#3b2412'),
}

def quadruped(cv, x, y, s=1.0, kind='grizzly', run=None, jaw=0.0, mood='angry', flip=False, rear=0.0, look=(1, 0), blink=0):
    """(x, y) = ground point under the chest centre. run = gallop phase (radians) or None (standing).
    jaw 0..1 open, rear 0..1 rears up on hind legs, flip faces left."""
    S = SPECS[kind]; L, Hb, leg, lw = S['L'], S['Hb'], S['leg'], S['legw']
    cv.save(); cv.translate(x, y); cv.scale(-s if flip else s, s)
    bob = -abs(math.sin(run if run is not None else 0)) * 18 if run is not None else 0
    cv.translate(0, bob); cv.rotate(-rear * 35)
    by = -leg - Hb*0.45  # body centre y
    # gallop: rotary gallop phases for 4 legs
    def legpos(i, ph_off, hx):
        if run is None: a, knee = (0, 0)
        else:
            ph = run + ph_off; a = math.sin(ph)*38; knee = max(0, math.cos(ph))*55
        hip = (hx, by + Hb*0.18)
        r1 = math.radians(a); x1, y1 = hip[0] + math.sin(r1)*leg*0.52, hip[1] + math.cos(r1)*leg*0.52
        r2 = math.radians(a - knee if hx < 0 else a + knee*0.6); x2, y2 = x1 + math.sin(r2)*leg*0.55, y1 + math.cos(r2)*leg*0.55
        return hip, (x1, y1), (x2, y2)
    legs = [(-L*0.32, 0.0, True), (L*0.30, 0.9, True), (-L*0.26, 0.45, False), (L*0.36, 1.35, False)]
    def draw_leg(hx, off, back):
        hip, k, f = legpos(0, off, hx)
        col = S['dark'] if back else S['col']
        p = skia.Path(); p.moveTo(*hip); p.lineTo(*k); p.lineTo(*f)
        cv.drawPath(p, stroke(INK, lw + 18)); cv.drawPath(p, stroke(C(col), lw))
        if S['claws']:
            for j in range(3):
                cv.drawLine(f[0] + 8 + j*12, f[1] + 6, f[0] + 22 + j*12, f[1] + 22, stroke('#f2ead8', 8))
        else:
            cv.drawRect(skia.Rect(f[0]-lw*0.7, f[1]-6, f[0]+lw*0.7, f[1]+14), fill(INK))
    for hx, off, back in legs:
        if back: draw_leg(hx, off, back)
    # tail
    tl = S['tail']
    if tl > 0.5:
        sw = math.sin((run or 0)*1.0)*20
        tp = smooth_path([(-L*0.48, by - 30), (-L*0.65, by + 20 + sw), (-L*0.7, by + 140 + sw), (-L*0.6, by + 150 + sw), (-L*0.55, by + 30)])
        shape(cv, tp, S.get('mane', S['dark']), 9)
    # body blob with hump
    hump = S['hump']
    pts = [(-L*0.5, by), (-L*0.42, by - Hb*0.45), (-L*0.1, by - Hb*0.52), (L*0.18, by - Hb*(0.55 + hump*0.45)),
           (L*0.42, by - Hb*0.42), (L*0.52, by + Hb*0.05), (L*0.36, by + Hb*0.45), (0, by + Hb*0.52), (-L*0.38, by + Hb*0.42)]
    body = smooth_path(pts)
    cv.drawPath(body, fill(S['col']))
    cv.save(); cv.clipPath(body, doAntiAlias=True)
    cv.drawOval(skia.Rect(-L*0.6, by + Hb*0.1, L*0.6, by + Hb*0.9), fill(S['belly']))
    cv.drawOval(skia.Rect(-L*0.7, by - Hb*1.1, L*0.7, by - Hb*0.25), fill(C('#ffffff', 28)))
    # fur strokes
    for i in range(9):
        fx = -L*0.4 + i*L*0.1; cv.drawLine(fx, by - Hb*0.2, fx + 14, by - Hb*0.05, stroke(C(S['dark'], 150), 6))
    cv.restore()
    cv.drawPath(body, stroke(INK, 10))
    # neck + head
    nx, ny = L*0.42, by - Hb*0.25
    if S['neck'] > 0:
        neck = smooth_path([(L*0.25, by - Hb*0.3), (L*0.42, by - Hb*1.25), (L*0.6, by - Hb*1.2), (L*0.52, by + Hb*0.1)])
        shape(cv, neck, S['col'], 10)
        mane = smooth_path([(L*0.27, by - Hb*0.35), (L*0.38, by - Hb*1.3), (L*0.45, by - Hb*1.25), (L*0.36, by - Hb*0.3)])
        shape(cv, mane, S['mane'], 7)
        nx, ny = L*0.58, by - Hb*1.2
    for hx, off, back in legs:
        if not back: draw_leg(hx, off, back)
    hr = S['head']
    cv.save(); cv.translate(nx + hr*0.4, ny)
    if S['neck'] > 0: cv.rotate(35)
    # ears
    for ex in (-hr*0.5, hr*0.1):
        if S['ears'] == 'round':
            cv.drawCircle(ex, -hr*0.85, hr*0.32, fill(S['col'])); cv.drawCircle(ex, -hr*0.85, hr*0.32, stroke(INK, 8))
            cv.drawCircle(ex, -hr*0.85, hr*0.15, fill(S['dark']))
        else:
            shape(cv, path_poly([(ex - 14, -hr*0.6), (ex, -hr*1.25), (ex + 16, -hr*0.6)]), S['col'], 7)
    head = smooth_path([(-hr*0.9, -hr*0.2), (-hr*0.5, -hr*0.85), (hr*0.3, -hr*0.8), (hr*0.7, -hr*0.35),
                        (hr*(0.7 + S['snout']*0.6), -hr*0.1), (hr*(0.75 + S['snout']*0.6), hr*0.35), (hr*0.2, hr*0.55), (-hr*0.7, hr*0.5)])
    # jaw (drawn behind head, rotates open)
    if jaw > 0.02:
        cv.save(); cv.translate(hr*0.1, hr*0.35); cv.rotate(jaw*32)
        jp = smooth_path([(-hr*0.3, -hr*0.05), (hr*(0.55 + S['snout']*0.55), -hr*0.05), (hr*(0.55 + S['snout']*0.5), hr*0.25), (-hr*0.2, hr*0.3)])
        shape(cv, jp, S['col'], 8)
        cv.drawRect(skia.Rect(-hr*0.1, -hr*0.12, hr*(0.5 + S['snout']*0.5), hr*0.02), fill('#5a0f0f'))
        for j in range(5):
            tx = hr*0.05 + j*hr*0.22
            cv.drawPath(path_poly([(tx, -hr*0.06), (tx + 10, -hr*0.28), (tx + 20, -hr*0.06)]), fill('#ffffff'))
        cv.restore()
    shape(cv, head, S['col'], 10)
    cv.save(); cv.clipPath(head, doAntiAlias=True)
    cv.drawOval(skia.Rect(hr*0.35, -hr*0.25, hr*(1.0 + S['snout']*0.7), hr*0.7), fill(S['belly'])); cv.restore()
    cv.drawPath(head, stroke(INK, 10))
    # nose, eye, brow
    cv.drawOval(skia.Rect(hr*(0.55 + S['snout']*0.6), -hr*0.22, hr*(0.8 + S['snout']*0.6), hr*0.02), fill(INK))
    if jaw > 0.02:  # upper teeth
        for j in range(5):
            tx = hr*0.15 + j*hr*0.22
            cv.drawPath(path_poly([(tx, hr*0.36), (tx + 10, hr*0.58), (tx + 20, hr*0.36)]), fill('#ffffff'))
    ex, ey = hr*0.15, -hr*0.35
    eh = hr*0.2*(1 - blink*0.9)
    cv.drawOval(skia.Rect(ex - hr*0.17, ey - eh, ex + hr*0.17, ey + eh), fill('#ffffff'))
    cv.drawOval(skia.Rect(ex - hr*0.17, ey - eh, ex + hr*0.17, ey + eh), stroke(INK, 5))
    if blink < 0.7: cv.drawCircle(ex + look[0]*hr*0.06, ey + look[1]*hr*0.05, hr*0.085, fill(INK))
    if mood == 'angry':
        cv.drawLine(ex - hr*0.25, ey - hr*0.38, ex + hr*0.22, ey - hr*0.18, stroke(INK, 10))
    elif mood == 'surprised':
        cv.drawLine(ex - hr*0.2, ey - hr*0.42, ex + hr*0.2, ey - hr*0.42, stroke(INK, 8))
    cv.restore()
    cv.restore()
