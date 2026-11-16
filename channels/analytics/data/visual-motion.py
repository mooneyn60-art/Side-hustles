#!/usr/bin/env python3
"""Visual-change metrics for a video: per-frame mean abs diff at 10 fps (96px wide grayscale).
cut = diff > 30 (0-255), static = diff < 1.0 (nothing moving), motion = mean diff excluding cuts."""
import subprocess, sys, json, numpy as np
def frames(path, fps=10, w=96, t=None):
    p=subprocess.run(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height','-of','csv=p=0',path],capture_output=True,text=True).stdout.strip().split('\n')[0].split(',')
    W,H=int(p[0]),int(p[1]); h=int(round(w*H/W/2))*2
    cmd=['ffmpeg','-v','error']+(['-t',str(t)] if t else [])+['-i',path,'-vf',f'fps={fps},scale={w}:{h},format=gray','-f','rawvideo','-']
    raw=subprocess.run(cmd,capture_output=True).stdout
    return np.frombuffer(raw,np.uint8).reshape(-1,h,w).astype(np.float32)
def metrics(path,t=None):
    f=frames(path,t=t); d=np.abs(np.diff(f,axis=0)).mean(axis=(1,2)); n=len(f)/10
    cuts=int((d>30).sum()); nc=d[d<=30]
    # longest run of near-static frames (s)
    run=best=0
    for x in d:
        run=run+1 if x<1.0 else 0; best=max(best,run)
    first3=d[:30]
    return dict(file=path.split('/')[-1],sec=round(n,1),cuts_per_min=round(cuts/n*60,1),avg_shot_s=round(n/max(cuts,1),2),
        motion=round(float(nc.mean()),2),static_pct=round(float((d<1.0).mean()*100),1),longest_static_s=round(best/10,1),
        motion_first3s=round(float(first3[first3<=30].mean()) if len(first3) else 0,2),cuts_first3s=int((first3>30).sum()))
if __name__=='__main__':
    t=None
    a=sys.argv[1:]
    if a and a[0].startswith('--t='): t=float(a[0][4:]); a=a[1:]
    for p in a: print(json.dumps(metrics(p,t)))
