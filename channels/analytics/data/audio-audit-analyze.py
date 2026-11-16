import sys, json, subprocess, re, os, numpy as np, librosa
from faster_whisper import WhisperModel
M = WhisperModel("base.en", device="cpu", compute_type="int8")
def sh(c): return subprocess.run(c, capture_output=True, text=True)
def loud(p):
    r = sh(["ffmpeg","-hide_banner","-i",p,"-vn","-af","loudnorm=I=-14:TP=-1:print_format=json","-f","null","-"]).stderr
    j = json.loads(r[r.rindex("{"):r.rindex("}")+1]); return float(j["input_i"]), float(j["input_tp"]), float(j["input_lra"])
def cuts(p, dur):
    r = sh(["ffmpeg","-hide_banner","-i",p,"-an","-vf","scale=160:-2,select='gt(scene,0.30)',showinfo","-f","null","-"]).stderr
    n = len(re.findall(r"pts_time:", r)); return n, round(n/dur*60,1), round(dur/(n+1),2)
out = []
for p in sys.argv[1:]:
    wav = "/tmp/a.wav"; sh(["ffmpeg","-y","-v","error","-i",p,"-vn","-ac","1","-ar","16000",wav])
    y, sr = librosa.load(wav, sr=16000); dur = len(y)/sr
    I, TP, LRA = loud(p)
    segs, _ = M.transcribe(y, word_timestamps=True, vad_filter=False, beam_size=1)
    words = [w for s in segs for w in s.words]
    text = " ".join(w.word.strip() for w in words)
    speech = np.zeros(len(y), bool)
    for w in words: speech[int(w.start*sr):int(w.end*sr)] = True
    spoken = sum(w.end-w.start for w in words)
    first, last = (words[0].start, words[-1].end) if words else (0, 0)
    gaps = [words[i+1].start - words[i].end for i in range(len(words)-1)]
    rms = lambda x: 20*np.log10(np.sqrt(np.mean(x**2))+1e-9)
    # pause floor: frames in gaps >= 0.25 s (shrunk 60 ms each side) vs speech frames
    pm = np.zeros(len(y), bool)
    for i,g in enumerate(gaps):
        if g >= 0.25: pm[int((words[i].end+0.06)*sr):int((words[i+1].start-0.06)*sr)] = True
    v_db = rms(y[speech]) if speech.any() else None
    p_db = rms(y[pm]) if pm.sum() > sr*0.3 else None
    tail = y[int(last*sr)+int(0.1*sr):]; t_db = rms(tail) if len(tail) > sr*0.5 else None
    # pitch on speech only
    f0, vf, _ = librosa.pyin(y, fmin=60, fmax=400, sr=sr, frame_length=1024, hop_length=320)
    mask = speech[::320][:len(f0)] & vf
    f = f0[mask]; f = f[~np.isnan(f)]
    st = 12*np.log2(f/np.median(f)) if len(f) else np.array([0.0])
    st = st[np.abs(st) < 9] if len(st) else st
    n, cpm, asl = cuts(p, dur)
    hook = " ".join(w.word.strip() for w in words if w.start < 3.0)
    out.append(dict(file=os.path.basename(p), dur=round(dur,1), lufs=I, tp=TP, lra=LRA,
        words=len(words), wpm_total=round(len(words)/dur*60), wpm_speaking=round(len(words)/max(last-first,1e-3)*60),
        voice_start_s=round(first,2), speech_cover=round(spoken/dur,2),
        gaps_over_0_7s=sum(g>0.7 for g in gaps), longest_gap=round(max(gaps),2) if gaps else None,
        f0_median_hz=round(float(np.median(f)),1) if len(f) else None, f0_sd_semitones=round(float(np.std(st)),2), f0_iqr_st=round(float(np.percentile(st,75)-np.percentile(st,25)),2),
        f0_range_p5_p95_st=round(float(np.percentile(st,95)-np.percentile(st,5)),1),
        voice_rms_db=round(v_db,1) if v_db else None, pause_floor_db=round(p_db,1) if p_db else None,
        bed_below_voice_db=round(v_db-p_db,1) if (v_db and p_db) else None, tail_db=round(t_db,1) if t_db else None,
        cuts=n, cuts_per_min=cpm, avg_shot_s=asl, hook_0_3s=hook, transcript=text))
    print(json.dumps(out[-1],default=float)[:400], flush=True)
json.dump(out, open(os.environ.get("OUT","results.json"),"w"), indent=1, default=float)
