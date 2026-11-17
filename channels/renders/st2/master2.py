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
K='/home/user/side-hustles/channels/sound/comedy-kit/'
import json
TLs=json.load(open('timeline.json'))['starts']; L0,L1,L2,L3,L4,L5=TLs
def env(n,a=0.005,r=0.08):
    e=np.ones(n); na=int(a*SR); nr=int(r*SR)
    e[:na]=np.linspace(0,1,na); e[-nr:]*=np.linspace(1,0,nr); return e
def tone(f0,f1,dur,harm=(1,),amp=0.5):
    n=int(dur*SR); f=np.linspace(f0,f1,n); ph=2*np.pi*np.cumsum(f)/SR
    x=sum(np.sin(ph*h)/(k+1) for k,h in enumerate(harm)); return amp*x*env(n)
def shing():
    n=int(0.45*SR); t=np.arange(n)/SR
    x=sum(np.sin(2*np.pi*f*t)*np.exp(-t*6) for f in (2400,3150,4200,5300))*0.18
    return x
def slide(): return tone(1300,280,0.42,harm=(1,2),amp=0.35)
def tada():
    a=tone(523,523,0.12,harm=(1,2,3,4),amp=0.22); b=tone(784,784,0.45,harm=(1,2,3,4),amp=0.25)
    return np.concatenate([a,np.zeros(int(0.03*SR)),b])
def claws():
    out=np.zeros(int(0.5*SR)); rnd=np.random.default_rng(3)
    for k in range(9):
        i=int(k*0.05*SR); n=int(0.012*SR); out[i:i+n]+=rnd.normal(0,0.25,n)*np.linspace(1,0,n)
    return out
def bloop(): return tone(700,250,0.16,amp=0.4)
def thunk():
    n=int(0.25*SR); t=np.arange(n)/SR
    return 0.6*np.sin(2*np.pi*(90+60*np.exp(-t*30))*t)*np.exp(-t*18)
syn=[(shing(),L0+1.50),(slide(),L1+(L2-L1)*0.62),(tada(),L2+1.10),(claws(),L3+0.45),(bloop(),L4+2.55),(thunk(),L5+0.94+0.70)]
out=sp.copy()
for a,t in syn:
    i=int(t*SR); m=min(len(a),len(out)-i); out[i:i+m]+=a[:m]
out=limit(out,-1.6)
print('mix LUFS %.2f TP %.2f'%(lufs(out),tp(out)))
np.save('speech_final.npy',sp)
out=out*10**(-3.01/20)
st=np.stack([out,out],1)
spst=sp*10**(-3.01/20); w2=wave.open('speech_only.wav','wb'); w2.setnchannels(2); w2.setsampwidth(2); w2.setframerate(SR); w2.writeframes((np.clip(np.stack([spst,spst],1),-1,1)*32767).astype(np.int16).tobytes()); w2.close()
w=wave.open('mix.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((np.clip(st,-1,1)*32767).astype(np.int16).tobytes()); w.close()
