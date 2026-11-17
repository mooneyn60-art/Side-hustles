import numpy as np, wave, subprocess, sys
from scipy.signal import resample_poly
from scipy.ndimage import maximum_filter1d, uniform_filter1d
SR=48000
def rd(fn):
    raw=subprocess.run(['ffmpeg','-v','error','-i',fn,'-f','f32le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout
    return np.frombuffer(raw,np.float32).astype(np.float64)
def lufs(x):
    # BS.1770 K-weighting via ffmpeg-free biquads
    from scipy.signal import lfilter
    b1=[1.53512485958697,-2.69169618940638,1.19839281085285]; a1=[1,-1.69065929318241,0.73248077421585]
    b2=[1.0,-2.0,1.0]; a2=[1,-1.99004745483398,0.99007225036621]
    y=lfilter(b2,a2,lfilter(b1,a1,x))
    n=int(0.4*SR); hop=int(0.1*SR)
    ms=np.array([np.mean(y[i:i+n]**2) for i in range(0,len(y)-n,hop)])
    l=-0.691+10*np.log10(ms+1e-12); g=ms[l>-70]
    rel=-0.691+10*np.log10(g.mean())-10; g2=ms[(l>-70)&(l>rel)]
    return -0.691+10*np.log10(g2.mean())
def limit(x,thr_db=-1.6):
    thr=10**(thr_db/20)
    up=resample_poly(x,4,1); pk=np.abs(up).reshape(-1,4).max(1)[:len(x)]
    if len(pk)<len(x): pk=np.pad(pk,(0,len(x)-len(pk)))
    g=np.minimum(1,thr/np.maximum(pk,1e-9))
    win=int(0.006*SR)
    g=-maximum_filter1d(-g,win*2+1)          # lookahead min
    g=uniform_filter1d(g,win)                 # smooth
    g=np.minimum(g,-maximum_filter1d(-g,win)) 
    return x*g
def tp(x): return 20*np.log10(np.abs(resample_poly(x,4,1)).max())
sp=rd('speech_raw.wav')
L=lufs(sp); sp=sp*10**((-14-L)/20)
for _ in range(3):
    sp=limit(sp); L=lufs(sp); sp=sp*10**((-14-L)/20)
sp=limit(sp)
print('speech LUFS %.2f TP %.2f'%(lufs(sp),tp(sp)))
K='/workspace/sound/comedy-kit/'
cues=[('boing',2.05,0.40),('boing',3.12,0.28),('record-scratch',4.20,0.45),('sad-trombone',7.30,0.38),('record-scratch',10.85,0.40),('boing',15.30,0.40)]
out=sp.copy()
for n,t,g in cues:
    a=rd(K+n+'.wav')*g; i=int(t*SR); m=min(len(a),len(out)-i); out[i:i+m]+=a[:m]
out=limit(out,-1.6)
print('mix LUFS %.2f TP %.2f'%(lufs(out),tp(out)))
np.save('speech_final.npy',sp)
out=out*10**(-3.01/20)
st=np.stack([out,out],1)
spst=sp*10**(-3.01/20); w2=wave.open('speech_only.wav','wb'); w2.setnchannels(2); w2.setsampwidth(2); w2.setframerate(SR); w2.writeframes((np.clip(np.stack([spst,spst],1),-1,1)*32767).astype(np.int16).tobytes()); w2.close()
w=wave.open('mix.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((np.clip(st,-1,1)*32767).astype(np.int16).tobytes()); w.close()
