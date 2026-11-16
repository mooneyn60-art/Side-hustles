import glob, os, json, numpy as np, librosa, pyloudnorm as pyln
from faster_whisper import WhisperModel
M = WhisperModel("small.en", device="cpu", compute_type="int8")
res = []
for d in sorted(glob.glob("/workspace/audio-audit/sep/out/htdemucs/*/")):
    name = os.path.basename(d.rstrip("/"))
    v, sr = librosa.load(d+"vocals.wav", sr=44100, mono=True, duration=20)
    m, _ = librosa.load(d+"no_vocals.wav", sr=44100, mono=True, duration=20)
    meter = pyln.Meter(sr)
    vl, ml = meter.integrated_loudness(v), meter.integrated_loudness(m)
    hop = int(0.05*sr)
    rv = librosa.feature.rms(y=v, frame_length=hop*2, hop_length=hop)[0]; rm = librosa.feature.rms(y=m, frame_length=hop*2, hop_length=hop)[0]
    dv = 20*np.log10(rv+1e-9); dm = 20*np.log10(rm+1e-9)
    act = dv > dv.max()-25
    # ducking: music level while voice talks vs while voice is silent (frames >=150ms away from speech)
    from scipy.ndimage import binary_dilation
    quiet = ~binary_dilation(act, iterations=3)
    m_under = float(np.mean(dm[act])) if act.any() else None
    m_gap = float(np.mean(dm[quiet])) if quiet.sum() > 4 else None
    v_talk = float(np.mean(dv[act]))
    v16 = librosa.resample(v, orig_sr=sr, target_sr=16000)
    segs, _ = M.transcribe(v16, word_timestamps=True, beam_size=5, condition_on_previous_text=False)
    w = [x for s in segs for x in s.words]
    span = (w[-1].end - w[0].start) if len(w) > 1 else 0
    f0, vf, _ = librosa.pyin(v16, fmin=60, fmax=400, sr=16000, frame_length=1024, hop_length=320)
    f = f0[vf & ~np.isnan(f0)]
    st = 12*np.log2(f/np.median(f)); st = st[np.abs(st) < 9]
    tempo = librosa.beat.beat_track(y=m, sr=sr)[0]
    onset = librosa.onset.onset_detect(y=m, sr=sr, units="time")
    res.append(dict(clip=name, voice_lufs=round(vl,1), music_lufs=round(ml,1), voice_minus_music_lu=round(vl-ml,1),
        music_under_voice_db=round(m_under-v_talk,1) if m_under else None,
        music_in_pauses_db=round(m_gap-v_talk,1) if m_gap else None,
        ducking_db=round(m_gap-m_under,1) if (m_gap and m_under) else None,
        wpm=round(len(w)/span*60) if span else None, first_word_s=round(w[0].start,2) if w else None,
        hook3=" ".join(x.word.strip() for x in w if x.start < 3),
        f0_med=round(float(np.median(f)),1), f0_iqr_st=round(float(np.percentile(st,75)-np.percentile(st,25)),2),
        f0_p5_p95_st=round(float(np.percentile(st,95)-np.percentile(st,5)),1),
        music_bpm=round(float(np.atleast_1d(tempo)[0])), music_onsets_per_s=round(len(onset)/20,2),
        transcript=" ".join(x.word.strip() for x in w)))
    print(json.dumps(res[-1])[:300], flush=True)
json.dump(res, open("/workspace/audio-audit/results_stems.json","w"), indent=1)
