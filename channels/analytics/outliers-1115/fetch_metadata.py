import json, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
Y='/opt/audit/bin/yt-dlp'
ids=[l.strip() for l in open(sys.argv[1]) if l.strip()]
done=set()
try:
    for l in open('full.jsonl'): done.add(json.loads(l)['id'])
except Exception: pass
K=['id','title','view_count','channel','channel_id','channel_follower_count','duration','upload_date','thumbnail','like_count','comment_count','description','tags']
def get(i):
    r=subprocess.run([Y,'-j','--skip-download','--no-warnings',f'https://www.youtube.com/watch?v={i}'],capture_output=True,text=True,timeout=90)
    try: d=json.loads(r.stdout)
    except Exception: return None
    o={k:d.get(k) for k in K}; o['description']=(o['description'] or '')[:400]; return o
todo=[i for i in ids if i not in done]
with ThreadPoolExecutor(8) as ex, open('full.jsonl','a') as f:
    for o in ex.map(get,todo):
        if o: f.write(json.dumps(o)+'\n'); f.flush()
print('done', len(todo))
