import glob
import re, os
"""mb2 audio: assemble per-line TTS into one voice track with planned gaps, synthesize SFX and a
procedural music bed (no licences), duck the music under the voice (production-spec-audio-v2 §1),
and give the renderer a mouth-open envelope for lip flap."""
import json, os, subprocess, numpy as np
SR = 48000
def load(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).copy()
def save(path, x):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', path], input=x.astype(np.float32).tobytes())
def assemble(lines, gaps, lead=0.0):
    """lines: [(mp3, words.json)], gaps[i] = silence before line i. Returns voice, words (global t), beat spans."""
    out, words, spans, t = [np.zeros(int(lead*SR), np.float32)], [], [], lead
    for i, (mp3, wj) in enumerate(lines):
        if i: out.append(np.zeros(int(gaps[i]*SR), np.float32)); t += gaps[i]
        x = load(mp3); w = json.load(open(wj))
        a = max(0.0, w[0]['t'] - 0.03); b = min(len(x)/SR, w[-1]['t'] + w[-1]['d'] + 0.10)
        seg = x[int(a*SR):int(b*SR)]
        fade = int(0.01*SR); seg[:fade] *= np.linspace(0, 1, fade); seg[-fade:] *= np.linspace(1, 0, fade)
        for ww in w: words.append({'w': ww['w'], 't': round(t + ww['t'] - a, 3), 'd': ww['d'], 'beat': i})
        spans.append((round(t, 3), round(t + len(seg)/SR, 3)))
        out.append(seg); t += len(seg)/SR
    return np.concatenate(out), words, spans
def voice_chain(inp, outp):
    """Presence chain from production-spec-audio-v2 §3 (no room echo)."""
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', inp, '-af',
        'highpass=f=70,equalizer=f=180:t=q:w=1:g=2,equalizer=f=3200:t=q:w=1:g=2.5,equalizer=f=7500:t=q:w=1:g=-2,'
        'acompressor=threshold=-20dB:ratio=3:attack=8:release=120', '-ar', str(SR), '-ac', '1', outp], check=True)
def envelope(x, fps=30):
    """Per-frame mouth openness 0..1 from voice RMS (lip flap), with a little smoothing."""
    hop = SR // fps; n = len(x) // hop
    r = np.sqrt(np.array([np.mean(x[i*hop:(i+1)*hop]**2) for i in range(n)]) + 1e-9)
    r = r / (np.percentile(r, 95) + 1e-9)
    r = np.clip((r - 0.12) / 0.8, 0, 1)
    return np.convolve(r, [0.25, 0.5, 0.25], mode='same')
# ---------------------------------------------------------------- SFX (synthesized)
rng = np.random.default_rng(3)
def _t(d): return np.arange(int(d*SR)) / SR
def whoosh(d=0.35):
    n = rng.standard_normal(int(d*SR)).astype(np.float32); t = _t(d)
    # sweep a resonant band by mixing differently smoothed noise
    lo = np.convolve(n, np.ones(40)/40, 'same'); hi = n - np.convolve(n, np.ones(6)/6, 'same')
    mix = lo * (1 - t/d) + hi * (t/d) * 0.6
    env = np.sin(np.pi * t/d) ** 1.5
    return (mix * env * 0.9).astype(np.float32)
def impact(d=0.5):
    t = _t(d); f = 110 * np.exp(-t*9) + 38
    body = np.sin(2*np.pi*np.cumsum(f)/SR) * np.exp(-t*7)
    click = rng.standard_normal(len(t)) * np.exp(-t*60) * 0.6
    return (np.tanh((body + click) * 2.2) * 0.8).astype(np.float32)
def pop(d=0.12):
    t = _t(d); f = 900 * np.exp(-t*25) + 300
    return (np.sin(2*np.pi*np.cumsum(f)/SR) * np.exp(-t*30) * 0.6).astype(np.float32)
def scratch(d=0.35):
    t = _t(d); f = 300 + 1400*np.abs(np.sin(2*np.pi*t*5))
    s = np.sign(np.sin(2*np.pi*np.cumsum(f)/SR)) * 0.25 + rng.standard_normal(len(t))*0.15
    return (s * np.exp(-t*4)).astype(np.float32)
def roar(d=1.1):
    t = _t(d); n = rng.standard_normal(len(t))
    lo = np.convolve(n, np.ones(25)/25, 'same') * 6
    am = 0.6 + 0.4*np.sin(2*np.pi*t*23) * np.sin(2*np.pi*t*3.1)
    tone = np.sin(2*np.pi*np.cumsum(90 + 30*np.sin(2*np.pi*t*1.3))/SR)
    env = np.minimum(1, t/0.08) * np.exp(-np.maximum(0, t-0.5)*4)
    return (np.tanh((lo*am + tone*0.6) * 1.5) * env * 0.8).astype(np.float32)
def heartbeat_stop(d=1.2):
    out = np.zeros(int(d*SR), np.float32)
    for at in (0.0, 0.18, 0.7):
        k = impact(0.25) * 0.7; i = int(at*SR); out[i:i+len(k)] += k[:len(out)-i]
    return out
def ding(d=0.6):
    t = _t(d); return (np.sin(2*np.pi*1320*t) * np.exp(-t*6) * 0.35 + np.sin(2*np.pi*1980*t)*np.exp(-t*9)*0.15).astype(np.float32)
def footsteps(d=1.0, rate=7):
    out = np.zeros(int(d*SR), np.float32); k = impact(0.12) * 0.35
    for i in range(int(d*rate)):
        j = int(i/rate*SR); out[j:j+len(k)] += k[:len(out)-j]
    return out
SFX = dict(whoosh=whoosh, impact=impact, pop=pop, scratch=scratch, roar=roar, heart=heartbeat_stop, ding=ding, steps=footsteps)
# ---------------------------------------------------------------- music bed ("cold-war" danger clock, 120 bpm)
def bed(dur, bpm=120, seed=1):
    t = _t(dur); beat = 60/bpm; out = np.zeros(len(t), np.float32)
    # low string drone (minor), slow tremolo
    for f, a in ((55, 0.22), (65.4, 0.14), (82.4, 0.12), (110, 0.06)):
        out += (np.sin(2*np.pi*f*t) + 0.3*np.sin(4*np.pi*f*t)) * a * (0.75 + 0.25*np.sin(2*np.pi*t*6))
    # ticking clock on 8ths + kick on the beat
    tick = (np.sin(2*np.pi*2400*_t(0.03)) * np.exp(-_t(0.03)*200) * 0.35).astype(np.float32)
    kick = impact(0.3) * 0.45
    k = 0
    while k*beat/2 < dur:
        i = int(k*beat/2*SR)
        out[i:i+len(tick)] += tick[:len(out)-i]
        if k % 2 == 0: out[i:i+len(kick)] += kick[:len(out)-i]
        k += 1
    # pizzicato motif every bar
    notes = [220, 261.6, 246.9, 196]
    for bar in range(int(dur/(beat*4)) + 1):
        for j, f in enumerate(notes):
            i = int((bar*4 + j) * beat * SR); tt = _t(0.25)
            pz = np.sin(2*np.pi*f*tt) * np.exp(-tt*14) * 0.18
            if i >= len(out): continue
            out[i:i+len(pz)] += pz[:len(out)-i]
    return out * 0.6
def mix(voice, sfx_events, dur, music=True, duck_db=-8, music_under_db=-20):
    """sfx_events: [(t, name, gain_db)]. Music ducked by the voice envelope with a 180 ms release."""
    n = int(dur*SR); v = np.zeros(n, np.float32); v[:min(n, len(voice))] = voice[:n]
    vr = np.sqrt(np.mean(v[v != 0]**2) + 1e-12)
    out = v.copy()
    talk = (np.abs(np.convolve(v, np.ones(int(0.02*SR))/int(0.02*SR), 'same')) > vr*0.08).astype(np.float32)
    rel = int(0.18*SR); talk = np.clip(np.convolve(talk, np.ones(rel)/rel, 'same') * 3, 0, 1)
    if music:
        m = bed(dur); mr = np.sqrt(np.mean(m**2))
        base = vr * 10**((music_under_db - duck_db)/20) / mr   # level in pauses (-12 dB under voice)
        m = m * base * (1 - talk*(1 - 10**(duck_db/20)))
        out += m
    for (t0, name, g) in sfx_events:
        s = SFX[name]() * 10**(g/20) * vr / 0.2
        i = int(t0*SR)
        if i < n: out[i:i+len(s)] += s[:n-i] * (1 - 0.5*talk[i:i+len(s)][:n-i])
    return out
def measure(f):
    """Integrated loudness (LUFS) and true peak (dBTP) of a file's audio, via ffmpeg ebur128."""
    e = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', f, '-map', 'a:0', '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
    summ = e[e.rindex('Summary:'):]
    I = float(re.search(r'I:\s+(-?[\d.]+) LUFS', summ).group(1)); TP = float(re.search(r'Peak:\s+(-?[\d.]+) dBFS', summ).group(1))
    return I, TP
def master(wav_in, video_in, out_mp4, target=-14.0, tp_max=-1.5, copy_video=False):
    """v2 mastering (spec §5): gain -> 4x-oversampled limiter (true-peak safe) -> 48 k, measured on the ENCODED AAC and
    iterated until integrated = -14.0 +/-0.2 LUFS and true peak <= -1.5 dBTP. (v1 used loudnorm: the peak cap held it at -14.6.)"""
    pre = out_mp4 + '.c.wav'   # v2.2: gentle 2:1 bus compressor first, so the limiter does ~3 dB, not 6+ (stops the TP oscillation)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', wav_in, '-af', 'acompressor=threshold=0.0316:ratio=2:attack=5:release=100', pre], check=True)
    wav_in = pre; g = target - measure(wav_in)[0]; lim = 0.70; tmp = out_mp4 + '.a.m4a'; best = None
    for it in range(12):   # v2.1: gentle gain steps, keep the best passing encode (AAC overshoot made v2 oscillate)
        af = f"volume={g:.2f}dB,aresample=192000,alimiter=limit={lim:.3f}:attack=2:release=80:level=false,aresample=48000"
        cand = f'{tmp}.{it}.m4a'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', wav_in, '-af', af, '-c:a', 'aac', '-b:a', '192k', cand], check=True)
        I, TP = measure(cand); print(f'master pass {it + 1}: gain {g:+.2f} dB, limit {lim:.3f} -> {I:.2f} LUFS, {TP:.2f} dBTP')
        if TP <= tp_max and (best is None or abs(I - target) < abs(best[1] - target)): best = (cand, I, TP)
        if best and abs(best[1] - target) <= 0.1: break
        if TP > tp_max: lim *= 10**((tp_max - TP - 0.5)/20)
        else: g += (target - I)*0.9
    if best is None: raise RuntimeError('master: no pass met the true-peak ceiling')
    os.replace(best[0], tmp)
    for f in glob.glob(tmp + '.*.m4a') + [pre]: os.remove(f)
    vc = ['-c:v', 'copy'] if copy_video else ['-c:v', 'libx264', '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-crf', '20', '-preset', 'medium']
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', video_in, '-i', tmp, '-map', '0:v', '-map', '1:a', *vc,
                    '-c:a', 'copy', '-movflags', '+faststart', '-shortest', out_mp4], check=True)
    os.remove(tmp)
