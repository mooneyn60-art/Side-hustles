import json,subprocess,re,os
import numpy as np
from PIL import Image
sh={x['Content']:x for x in json.load(open('/workspace/retention_shorts90.json'))}
feat={}
for f in ['results_ys_small.json','results_yt.json']:
    for r in json.load(open(f)):
        k=r['file'][3:-4]
        if k not in feat or r['words']>feat[k]['words']: feat[k]=r
def scenes(p,th=0.25):
    o=subprocess.run(['ffmpeg','-hide_banner','-i',p,'-vf',f"select='gt(scene,{th})',showinfo",'-an','-f','null','-'],capture_output=True,text=True).stderr
    return [float(m) for m in re.findall(r'pts_time:([\d.]+)',o)]
def frame(p,t,out):
    subprocess.run(['ffmpeg','-y','-loglevel','error','-sseof' if t<0 else '-ss',str(t),'-i',p,'-frames:v','1','-vf','scale=216:384',out])
    return np.asarray(Image.open(out).convert('L'),dtype=float)
rows=[]
os.makedirs('/workspace/ret/frames',exist_ok=True)
for vid in sorted(set(feat)):
    p=f'media/yt_{vid}.mp4'
    if not os.path.exists(p) or vid not in sh: continue
    r=feat[vid]; s=sh[vid]; d=r['dur']
    sc=scenes(p); f0=frame(p,0.05,f'/workspace/ret/frames/{vid}_0.png'); fl=frame(p,-0.4,f'/workspace/ret/frames/{vid}_end.png')
    loop=1-np.abs(f0-fl).mean()/255
    rows.append(dict(id=vid,title=s['Video title'][:60],views=int(s['Views']),apv=float(s['Average percentage viewed (%)']),avd=s['Average view duration'],dur=d,
      voice_start=r['voice_start_s'],wpm=r['wpm_speaking'],speech_cover=r['speech_cover'],longest_gap=r['longest_gap'],gaps07=r['gaps_over_0_7s'],
      cuts_per_min=r['cuts_per_min'],avg_shot=r['avg_shot_s'],first_cut=(sc[0] if sc else None),cuts_0_3=sum(1 for t in sc if t<3),loop_sim=round(loop,3),hook=r['hook_0_3s']))
json.dump(rows,open('/workspace/ret/ours.json','w'),indent=1)
for x in sorted(rows,key=lambda x:-x['views']):
    print(x['views'],x['apv'],x['dur'],x['voice_start'],x['wpm'],x['speech_cover'],x['longest_gap'],x['cuts_per_min'],x['first_cut'],x['cuts_0_3'],x['loop_sim'],'|',x['title'][:40],'|',x['hook'][:60])
