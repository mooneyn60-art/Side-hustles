#!/usr/bin/env python3
"""Retention-v2 Short renderer in the C v3 house style (spec: "Shorts retention spec v2").
Data-driven: an episode dict = script lines (TTS), shots anchored to spoken words, choice chips, cards.
Rules it enforces (lint() prints them and fails loudly):
  frame 0 = threat + Meatball in one panel, voice at 0.0 s, no intro/logo/series tag
  3-4 pictures in the first 2.8 s, then a new picture every 1.0-2.5 s (never a hold > 2.5 s)
  15-20 s total, the last shot re-uses frame 0's framing and the last line runs into the first line (loop)
  captions: Anton 112, active word yellow at 1.08x, groups clamped to 820 px, centred in y 1180-1500
Usage: rv2.py EPISODE OUT.mp4 [--label TEXT]      EPISODE in EPISODES (house-centipede, daddy-longlegs)"""
import json, math, os, subprocess, sys
import numpy as np, skia
from PIL import Image
from kit import W, H, FPS, C, fill, stroke, lerp, clamp, ease_out, back_out, spring, wobble, text_outlined, font
from characters import meatball
import audio
import render as R   # reuses panels, Ken Burns, cards, ink wipe, grade, grain, timeline helpers

HERE = os.path.dirname(os.path.abspath(__file__))
P = lambda name, z0, z1, c0, c1, shake=0: ('panel', name, z0, z1, c0, c1, shake)
MB = lambda bg, **st: ('mb', bg, st)          # rig Meatball reaction on a flat/burst background
PUNCH = lambda txt, col, bg: ('punch', txt, col, bg)   # stamp word on a burst (counts as a picture)

EPISODES = {
 'house-centipede': dict(
    dir='rv2-house-centipede', gaps=[0, 0.16, 0.16, 0.18, 0.16, 0.12],
    cap_key={'centipede', 'squish', 'live', 'thirty', 'legs', 'night', 'roaches', 'silverfish', 'spiders', 'hunter', 'eat', 'meatball'},
    chips=[('SQUISH', '#ff4b3e', (0, 'Squish')), ('LET IT LIVE', '#7CFF6B', (0, 'let'))], strike=None,
    cards=[(1, 'Thirty', [('30 LEGS', '#ffd23f', 110), ('HUNTS AT NIGHT: PENN STATE EXTENSION', '#ffffff', 38)]),
           (2, 'eats', [('EATS ROACHES + SILVERFISH', '#7CFF6B', 76), ('AND SPIDERS (PENN STATE EXT.)', '#ffffff', 40)]),
           (4, 'see', [('LOTS OF THEM = LOTS OF PREY', '#ffd23f', 68)]),
           (5, 'So', [('SQUISH OR LET IT LIVE? COMMENT', '#ffd23f', 58)])],
    shots=[((0, 'You'), P('rv2_cent_hook.jpg', 1.04, 1.14, (0.5, 0.46), (0.5, 0.44), 10)),     # frame 0: threat + Meatball
           ((0, 'Squish'), P('rv2_cent_hook.jpg', 2.0, 2.2, (0.30, 0.74), (0.30, 0.72), 14)),  # Meatball + slipper
           ((0, 'let'), P('rv2_cent_hook.jpg', 2.3, 2.6, (0.46, 0.33), (0.46, 0.32), 8)),      # centipede face
           ((1, "It's"), P('thumb_art_house-centipede.jpg', 1.0, 1.12, (0.74, 0.5), (0.70, 0.48))),
           ((1, 'hunts'), P('rv2_cent_hook.jpg', 1.5, 1.7, (0.70, 0.40), (0.62, 0.38))),
           ((2, 'roaches'), P('thumb_art_house-centipede.jpg', 1.15, 1.3, (0.55, 0.55), (0.52, 0.55))),
           ((2, 'even'), P('thumb_art_corner-spider.jpg', 1.2, 1.4, (0.62, 0.42), (0.64, 0.40))),
           ((3, 'Meatball'), P('rv2_cent_hook.jpg', 1.8, 1.6, (0.30, 0.70), (0.32, 0.72), 12)),
           ((3, 'Now'), P('rv2_cent_hunter.jpg', 1.0, 1.15, (0.5, 0.45), (0.5, 0.38))),
           ((3, 'one'), P('rv2_cent_hunter.jpg', 1.9, 2.1, (0.62, 0.33), (0.62, 0.31), 6)),      # punch-in on the watching roaches
           ((4, 'And'), MB('#1b3fae', face='shock', arms='up', sweat=True, size=2.1, y=1050)),
           ((4, "you've"), P('thumb_art_house-centipede.jpg', 1.9, 2.1, (0.45, 0.66), (0.45, 0.62))),
           ((5, 'So'), P('rv2_cent_hook.jpg', 1.14, 1.04, (0.5, 0.44), (0.5, 0.46), 10))]),      # loop: frame 0 framing
 'daddy-longlegs': dict(
    dir='rv2-daddy-longlegs', gaps=[0, 0.12, 0.12, 0.12, 0.12, 0.10],
    cap_key={'daddy', 'longlegs', 'venomous', 'true', 'false', 'harvestman', 'spider', 'venom', 'cellar', 'proof', 'myth', 'fangs', 'spiders'},
    chips=[('TRUE', '#7CFF6B', (0, 'True')), ('FALSE', '#ff4b3e', (0, 'false'))], strike=('TRUE', (1, 'False')),
    cards=[(0, "You've", [('TRUE OR FALSE?', '#ff4b3e', 96), ('DADDY LONGLEGS = MOST VENOMOUS SPIDER', '#ffffff', 40)]),   # the claim on frame 0 (what the live 53.7%-stayed Short did)
           (1, 'Two', [('2 ANIMALS, 1 NAME', '#ffd23f', 96)]),
           (2, 'has', [('NOT A SPIDER. NO VENOM', '#7CFF6B', 80), ('HARVESTMAN: UF/IFAS EXTENSION', '#ffffff', 40)]),
           (3, 'but', [('NO PROOF IT HURTS PEOPLE', '#7CFF6B', 76), ('CELLAR SPIDER: UC RIVERSIDE', '#ffffff', 40)]),
           (4, 'Also', [('MYTH', '#ff4b3e', 130), ('UC RIVERSIDE (R. VETTER)', '#ffffff', 40)]),
           (5, 'So', [('TRUE OR FALSE? COMMENT', '#ffd23f', 64)])],
    shots=[((0, "You've"), P('rv2_dll_hook.jpg', 1.04, 1.14, (0.5, 0.48), (0.5, 0.46), 8)),
           ((0, 'longlegs'), P('rv2_dll_hook.jpg', 2.0, 2.3, (0.5, 0.30), (0.5, 0.29), 6)),
           ((0, 'venomous'), P('rv2_dll_hook.jpg', 1.8, 2.0, (0.5, 0.74), (0.5, 0.72), 12)),
           ((0, 'True'), MB('burst', face='shock', arms='up', sweat=True, size=2.0, y=1000)),
           ((1, 'False'), PUNCH('FALSE!', '#ff3b2f', 'burst')),
           ((1, 'Two'), ('split', ('rv2_harvestman.jpg', 1.5, (0.45, 0.42)), ('rv2_dll_hook.jpg', 1.6, (0.5, 0.30)))),
           ((2, 'The'), P('rv2_harvestman.jpg', 1.0, 1.15, (0.5, 0.5), (0.48, 0.45))),
           ((2, 'and'), P('rv2_harvestman.jpg', 1.9, 2.1, (0.48, 0.44), (0.48, 0.42))),
           ((3, 'The'), P('rv2_dll_hook.jpg', 1.6, 1.8, (0.5, 0.32), (0.5, 0.30))),
           ((3, 'but'), MB('#2e7d4f', face='happy', arms=(14, -14), size=2.0, y=1050)),
           ((4, 'Fangs'), P('thumb_art_corner-spider.jpg', 1.5, 1.7, (0.62, 0.40), (0.64, 0.38), 6)),
           ((4, 'Also'), PUNCH('MYTH', '#ffd23f', 'burst_red')),
           ((5, 'It'), P('thumb_art_corner-spider.jpg', 1.0, 1.12, (0.62, 0.5), (0.60, 0.48))),
           ((5, 'So'), P('rv2_dll_hook.jpg', 1.14, 1.04, (0.5, 0.46), (0.5, 0.48), 8))]),
}

def captions(cv, tl, t, keys, y=1430, maxw=820):
    """Word-by-word: groups of 1-3 words pop on; the word being spoken is yellow at 1.08x; group clamped to maxw."""
    groups, cur = [], []
    for x in tl.words:
        cur.append(x)
        if x['w'][-1:] in ',.?!' or len(cur) == 3 or R.norm(x['w']) in keys: groups.append(cur); cur = []
    if cur: groups.append(cur)
    for gi, g in enumerate(groups):
        t0 = g[0]['t']; t1 = groups[gi + 1][0]['t'] if gi + 1 < len(groups) else g[-1]['t'] + g[-1]['d'] + 0.3
        if not (t0 <= t < t1): continue
        sc = 0.6 + 0.4*spring((t - t0)*1.6, 2.6, 7)
        words = [x['w'].upper().rstrip('.,!?') for x in g]
        act = [src['t'] <= t < src['t'] + max(src['d'], 0.12) + 0.04 for src in g]
        pxs = [(124 if R.norm(w) in keys else 112)*(1.08 if a else 1.0) for w, a in zip(words, act)]
        widths = [font('Anton-Regular.ttf', px).measureText(w) + 0.30*px for w, px in zip(words, pxs)]   # measured at drawn size
        tw = sum(widths); fit = min(1.0, maxw/tw)
        cv.save(); cv.translate(W/2, y); cv.scale(sc*fit, sc*fit); x = -tw/2
        for w, ww, px, a in zip(words, widths, pxs, act):
            text_outlined(cv, w, x + ww/2, 0, px, '#FFD21F' if (a or R.norm(w) in keys) else '#ffffff', '#000', px*0.18, center=True)
            x += ww
        cv.restore()

def chips(cv, tl, t, spec, strike, end):
    if t >= end: return
    f = font('Anton-Regular.ttf', 62); opts = [(s, c, tl.w(*a)) for s, c, a in spec]
    ws = [f.measureText(o[0]) + 50 for o in opts]; x = (W - sum(ws) - 20*(len(ws) - 1))/2; y = 1225
    for (txt, col, t0), w in zip(opts, ws):
        if t >= t0:
            sc = back_out(clamp((t - t0)/0.22)); cv.save(); cv.translate(x + w/2, y); cv.scale(sc, sc)
            r = skia.RRect.MakeRectXY(skia.Rect(-w/2, -54, w/2, 32), 20, 20)
            cv.drawRRect(r, fill(C('#111111', 235))); cv.drawRRect(r, stroke(col, 7)); text_outlined(cv, txt, 0, 8, 62, col, '#000', 0)
            if strike and txt == strike[0]:
                ts = tl.w(*strike[1])
                if t >= ts: k = clamp((t - ts)/0.15); cv.drawLine(-w/2 + 10, 20, -w/2 + 10 + (w - 20)*k, -40, stroke('#ff2020', 14))
            cv.restore()
        x += w + 20

def draw(cv, shot, t, u, d, mouth):
    kind = shot[0]
    if kind == 'panel':
        _, name, z0, z1, c0, c1, shake = shot; sk = shake*math.exp(-u*3)
        cv.save(); cv.translate(wobble(t, 7, sk, 12), wobble(t, 8, sk, 12))
        R.draw_panel(cv, name, clamp(u/max(d, 0.01)), z0, z1, c0, c1, rot=wobble(t, 9, 0.6, 0.8)); cv.restore()
    elif kind == 'split':   # two panels stacked, ink line between: "two animals, one name"
        for i, (name, z, c) in enumerate(shot[1:]):
            cv.save(); cv.clipRect(skia.Rect(0, i*H/2, W, (i + 1)*H/2)); cv.translate(0, (i - 0.5)*H/2 + lerp(30, 0, ease_out(clamp(u/0.3)))*(1 if i else -1))
            R.draw_panel(cv, name, clamp(u/max(d, 0.01)), z, z*1.08, c, c); cv.restore()
        cv.drawLine(0, H/2, W, H/2, stroke('#111111', 16))
    elif kind == 'mb':
        _, bg, st = shot; st = dict(st); size = st.pop('size', 2.0); y = st.pop('y', 1050)
        if bg.startswith('burst'): R.bg_burst(cv, t)
        else: cv.drawPaint(fill(bg)); R.radial_lines(cv, t, W/2, y - 100, 90)
        z = lerp(1.0, 1.08, u/max(d, 0.01)); cv.save(); cv.translate(W/2, y); cv.scale(z, z)
        st.update(mouth=mouth, squash=(1 + 0.05*math.sin(u*24), 1 - 0.05*math.sin(u*24)), blink=1.0 if (t % 2.9) < 0.08 else 0.0)
        meatball(cv, 0, 0, size, st); cv.restore()
    elif kind == 'punch':
        _, txt, col, bg = shot
        R.bg_burst(cv, t, *(('#ffcc33', '#ff8a00') if bg == 'burst' else ('#c4161c', '#7a0a0e')), 0.6)
        sc = back_out(clamp(u/0.18))*lerp(1.0, 1.06, u/max(d, 0.01))
        text_outlined(cv, txt, W/2, 820, 300, col, '#000', 30, 'Bangers-Regular.ttf', scale=sc, rot=-6)
        meatball(cv, W/2, 1180, 1.3, {'face': 'shock', 'mouth': mouth, 'arms': 'up'})

def lint(tl, sh, dur):
    starts = [a for a, b, _ in sh]; holds = [b - a for a, b, _ in sh]
    first = [x for x in tl.words if x['t'] < 3.0]
    rep = dict(dur=round(dur, 2), voice_start=round(tl.words[0]['t'], 2), pictures_first_2_8s=sum(1 for a in starts if a < 2.8),
               max_hold_after_hook=round(max(h for (a, b, _), h in zip(sh, holds) if a >= 2.8), 2), shots=len(sh),
               cuts_per_min=round((len(sh) - 1)/dur*60, 1), words_first_3s=len(first), loop=sh[-1][2][1] == sh[0][2][1])
    ok = (14.5 <= dur <= 20.5 and rep['voice_start'] <= 0.1 and 3 <= rep['pictures_first_2_8s'] <= 5 and rep['max_hold_after_hook'] <= 2.5 and rep['loop'])
    rep['pass'] = ok; print('RETENTION LINT', json.dumps(rep)); return rep

def render(epname, out, label_text=''):
    ep = EPISODES[epname]; work = os.path.join(HERE, 'episodes', ep['dir'])
    lines = json.load(open(os.path.join(HERE, 'episodes', 'rv2_lines.json')))[ep['dir']]
    voice, words, spans = audio.assemble([(f'{work}/v{i}.mp3', f'{work}/v{i}.words.json') for i in range(1, len(lines) + 1)], ep['gaps'])
    for bi, txt in enumerate(lines):
        toks = txt.split(); ws = [x for x in words if x['beat'] == bi]
        if len(toks) == len(ws):
            for x, tk in zip(ws, toks): x['w'] = tk
    tmp = out + '.voice.wav'; audio.save(tmp, voice); audio.voice_chain(tmp, tmp + '.p.wav')
    voice = audio.load(tmp + '.p.wav'); dur = len(voice)/audio.SR + 0.25
    tl = R.TL(words, spans, dur); env = audio.envelope(voice)
    st = [tl.w(*a) if a != (0, lines[0].split()[0]) else 0.0 for a, _ in ep['shots']]
    sh = [(st[i], st[i + 1] if i + 1 < len(st) else dur + 0.01, s) for i, (_, s) in enumerate(ep['shots'])]
    rep = lint(tl, sh, dur)
    sfx = [(0.0, 'impact', -6)] + [(tl.w(*a), 'pop', -8) for _, _, a in ep['chips']]
    for i in range(1, len(sh)):
        sfx.append((sh[i][0] - 0.06, 'whoosh' if sh[i][2][0] != sh[i - 1][2][0] else 'pop', -11 if sh[i][2][0] != sh[i - 1][2][0] else -14))
        if sh[i][2][0] == 'punch': sfx.append((sh[i][0], 'impact', -4))
    mixw = audio.mix(voice, sfx, dur); audio.save(out + '.mix.wav', mixw)
    n = int(dur*FPS)
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgra', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', out + '.video.mp4'], stdin=subprocess.PIPE)
    surf = skia.Surface(W, H); cv = surf.getCanvas(); grain = R.grain_tiles()
    gradep = skia.Paint(ColorFilter=R.GRADE); gp = skia.Paint(BlendMode=skia.BlendMode.kOverlay); gp.setAlphaf(0.5)
    soft = skia.Paint(ImageFilter=skia.ImageFilters.Blur(0.8, 0.8))
    chip_end = tl.b0(1) + 0.8
    for fi in range(n):
        t = fi/FPS; mouth = float(env[fi]) if fi < len(env) else 0.0
        si = max(i for i, (a, b, _) in enumerate(sh) if a <= t); a, b, s = sh[si]; u, d = t - a, b - a
        cv.clear(C('#000000')); cv.saveLayer(None, gradep)
        if s[0] == 'mb': cv.saveLayer(None, soft)
        draw(cv, s, t, u, d, mouth)
        if s[0] == 'mb': cv.restore()
        wipe = si > 0 and u < 0.24 and (s[0] == 'panel') != (sh[si - 1][2][0] == 'panel') and d >= 0.8
        if wipe: R.ink_wipe(cv, u/0.24, lambda: draw(cv, sh[si - 1][2], t, a - sh[si - 1][0], a - sh[si - 1][0], 0.0))
        cv.restore()
        cv.drawImageRect(grain[fi % len(grain)], skia.Rect(0, 0, W, H), skia.SamplingOptions(skia.FilterMode.kLinear), gp)
        if u < 0.08 and si > 0 and not wipe: cv.drawPaint(fill(C('#ffffff', int(70*(1 - u/0.08)))))
        R.cards(cv, tl, t, ep['cards']); chips(cv, tl, t, ep['chips'], ep['strike'], chip_end)
        captions(cv, tl, t, {R.norm(k) for k in ep['cap_key']})
        R.label(cv, label_text)
        enc.stdin.write(surf.makeImageSnapshot().tobytes())
    enc.stdin.close(); enc.wait()
    audio.master(out + '.mix.wav', out + '.video.mp4', out)
    for f in (tmp, tmp + '.p.wav') + (() if os.environ.get('KEEP') else (out + '.mix.wav', out + '.video.mp4')):
        try: os.remove(f)
        except OSError: pass
    json.dump({'lint': rep, 'shots': [(round(a, 2), round(b, 2), s[0], s[1] if len(s) > 1 and isinstance(s[1], str) else '') for a, b, s in sh], 'words': words}, open(out + '.timeline.json', 'w'), indent=0)
    print('wrote', out, round(dur, 2))

if __name__ == '__main__':
    a = sys.argv[1:]; lab = ''
    if '--label' in a: i = a.index('--label'); lab = a[i + 1]; del a[i:i + 2]
    render(a[0], a[1], lab)
