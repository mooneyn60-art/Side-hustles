import json, subprocess, numpy as np, wave
SR=48000
def load(fn):
    raw=subprocess.run(['ffmpeg','-v','error','-i',fn,'-f','s16le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout
    return np.frombuffer(raw,np.int16).astype(np.float32)/32768
W=json.load(open('vo/words.json'))
starts=[];t=0.0
for i,l in enumerate(W):
    starts.append(t)
    lw=l['words'][-1]; t+= lw[0]+lw[1]+0.24
total=starts[-1]+W[-1]['words'][-1][0]+W[-1]['words'][-1][1]+0.12
print('starts',[round(s,3) for s in starts],'total',round(total,3))
N=int(total*SR)+1
sp=np.zeros(N,np.float32)
for i,s in enumerate(starts):
    a=load(f'vo/l{i}.mp3'); i0=int(s*SR); n=min(len(a),N-i0); sp[i0:i0+n]+=a[:n]
# words absolute
words=[]
for i,l in enumerate(W):
    for (o,d,w) in l['words']: words.append([round(starts[i]+o,3),round(starts[i]+o+d,3),w,i])
json.dump({'starts':starts,'total':total,'words':words},open('timeline.json','w'),indent=1)
def wr(fn,x):
    x=np.clip(x,-1,1); w=wave.open(fn,'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x*32767).astype(np.int16).tobytes()); w.close()
wr('speech_raw.wav',sp)
