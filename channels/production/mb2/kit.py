"""mb2 drawing kit: skia helpers, easing, palette. Everything is vector, 1080x1920 at 30 fps."""
import math, os, skia
HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
INK = 0xFF1A1410
def C(hexs, a=255):
    hexs = hexs.lstrip('#')
    if len(hexs) == 3: hexs = ''.join(ch*2 for ch in hexs)
    return skia.Color(int(hexs[0:2],16), int(hexs[2:4],16), int(hexs[4:6],16), a)
def fill(c): return skia.Paint(Color=c if isinstance(c,int) else C(c), AntiAlias=True)
def stroke(c, w, cap=skia.Paint.kRound_Cap):
    return skia.Paint(Color=c if isinstance(c,int) else C(c), AntiAlias=True, Style=skia.Paint.kStroke_Style,
                      StrokeWidth=w, StrokeCap=cap, StrokeJoin=skia.Paint.kRound_Join)
def lerp(a, b, t): return a + (b - a) * t
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease_out(t): t = clamp(t); return 1 - (1 - t) ** 3
def ease_in_out(t): t = clamp(t); return 3*t*t - 2*t*t*t
def back_out(t, s=1.9):
    t = clamp(t) - 1; return t*t*((s+1)*t + s) + 1
def elastic(t):
    t = clamp(t)
    if t in (0, 1): return t
    return 2 ** (-10*t) * math.sin((t*10 - 0.75) * (2*math.pi/3)) + 1
def spring(t, f=3.2, d=5.5):
    """0->1 with overshoot that settles: good for pops and stops."""
    if t <= 0: return 0.0
    return 1 - math.exp(-d*t) * math.cos(f*2*math.pi*t)
def path_poly(pts, close=True):
    p = skia.Path(); p.moveTo(*pts[0])
    for q in pts[1:]: p.lineTo(*q)
    if close: p.close()
    return p
def smooth_path(pts, close=True, tension=0.5):
    """Catmull-Rom through points -> cubic path (organic outlines)."""
    p = skia.Path(); n = len(pts)
    if n < 3: return path_poly(pts, close)
    p.moveTo(*pts[0])
    rng = range(n) if close else range(n-1)
    for i in rng:
        p0 = pts[(i-1) % n] if (close or i > 0) else pts[i]
        p1 = pts[i]; p2 = pts[(i+1) % n]
        p3 = pts[(i+2) % n] if (close or i+2 < n) else p2
        c1 = (p1[0] + (p2[0]-p0[0])*tension/3, p1[1] + (p2[1]-p0[1])*tension/3)
        c2 = (p2[0] - (p3[0]-p1[0])*tension/3, p2[1] - (p3[1]-p1[1])*tension/3)
        p.cubicTo(c1[0], c1[1], c2[0], c2[1], p2[0], p2[1])
    if close: p.close()
    return p
def shape(cv, path, color, outline=10, ink=INK):
    cv.drawPath(path, fill(color))
    if outline: cv.drawPath(path, stroke(ink, outline))
_tf = {}
def font(name='Anton-Regular.ttf', size=80):
    if name not in _tf: _tf[name] = skia.Typeface.MakeFromFile(os.path.join(HERE, 'assets', name))
    return skia.Font(_tf[name], size)
def text_outlined(cv, s, x, y, size, color='#ffffff', outline='#000000', ow=None, name='Anton-Regular.ttf', center=True, rot=0, scale=1.0, alpha=255):
    f = font(name, size); w = f.measureText(s)
    cv.save(); cv.translate(x, y); cv.rotate(rot); cv.scale(scale, scale)
    ox = -w/2 if center else 0
    blob = skia.TextBlob.MakeFromString(s, f)
    ow = ow if ow is not None else size*0.16
    sp = stroke(C(outline, alpha), ow); sp.setStrokeJoin(skia.Paint.kRound_Join)
    cv.drawTextBlob(blob, ox+size*0.04, size*0.07, fill(C('#000000', int(alpha*0.55))))  # drop shadow
    cv.drawTextBlob(blob, ox, 0, sp)
    cv.drawTextBlob(blob, ox, 0, fill(C(color, alpha)))
    cv.restore(); return w*scale
def wobble(t, seed=0.0, amp=1.0, speed=1.0):
    """Cheap smooth noise (sum of sines) for idle life and handheld camera."""
    return amp * (math.sin(t*1.7*speed + seed*3.1) * 0.6 + math.sin(t*2.9*speed + seed*7.3) * 0.3 + math.sin(t*5.3*speed + seed*1.7) * 0.1)
