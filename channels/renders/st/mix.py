import numpy as np, wave, subprocess
SR=48000
def rd(fn):
    raw=subprocess.run(['ffmpeg','-v','error','-i',fn,'-f','s16le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout
    return np.frombuffer(raw,np.int16).astype(np.float32)/32768
sp=rd('speech_norm.wav'); out=sp.copy()
K='/workspace/sound/comedy-kit/'
cues=[('boing',2.05,0.40),('boing',3.12,0.28),('record-scratch',4.20,0.45),('sad-trombone',7.30,0.38),('record-scratch',10.85,0.40),('boing',15.30,0.40)]
for n,t,g in cues:
    a=rd(K+n+'.wav')*g; i=int(t*SR); m=min(len(a),len(out)-i); out[i:i+m]+=a[:m]
w=wave.open('mix_raw.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((np.clip(out,-1,1)*32767).astype(np.int16).tobytes()); w.close()
