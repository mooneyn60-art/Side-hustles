import json, os
from PIL import Image, ImageDraw, ImageFont
F='/workspace/meatball-animation-v2/mb2/assets/Anton-Regular.ttf'
S=sorted(json.load(open('selected.json')),key=lambda x:-(x['view_count']/x['channel_follower_count']))
ours=json.load(open('ours.json'))
TW,TH=320,180; cols=7; pad=8; lab=46
def tile(img_path,l1,l2,col='#ffffff'):
    t=Image.new('RGB',(TW,TH+lab),'#111')
    im=Image.open(img_path).convert('RGB')
    w,h=im.size; r=16/9
    if w/h>r: nw=int(h*r); im=im.crop(((w-nw)//2,0,(w-nw)//2+nw,h))
    else: nh=int(w/r); im=im.crop((0,(h-nh)//2,w,(h-nh)//2+nh))
    t.paste(im.resize((TW,TH),Image.LANCZOS),(0,0))
    d=ImageDraw.Draw(t); f1=ImageFont.truetype(F,19); f2=ImageFont.truetype(F,15)
    d.text((6,TH+2),l1,font=f1,fill=col); d.text((6,TH+25),l2[:46],font=f2,fill='#bbbbbb'); return t
def k(n): return f'{n/1e6:.1f}M' if n>=1e6 else f'{n/1e3:.0f}k' if n>=1e3 else str(n)
tiles=[tile(f"thumbs/{x['id']}.jpg",f"{x['view_count']/x['channel_follower_count']:.0f}x subs  {k(x['view_count'])} views  {'SHORT' if (x['duration'] or 0)<=180 and x['id'] in ('IZm2W2IJ3V4','Lp6Im6SJamw','CHXcQqsprB0','9KgSFg-7fjU') else str(round((x['duration'] or 0)/60))+'m'}",x['title'],'#ffd23f') for x in S]
ot=[tile(f"thumbs/ours_{x['id']}.jpg",f"OURS  {k(x['views'])} views  {'SHORT' if x['short'] else str(round(x['dur']/60))+'m'}",x['title'],'#ff6b5e') for x in ours]
P=json.load(open('/workspace/meatball-animation-v2/samples/v3_thumb_title_pairs.json'))
v2=[tile(f"/workspace/meatball-animation-v2/samples/{p['file']}",'NEW v3 PAIR',p['title'],'#7CFF6B') for p in P]
rows_o=(len(tiles)+cols-1)//cols; rows_u=(len(ot)+cols-1)//cols
hdr=60
W=cols*(TW+pad)+pad; H=hdr+rows_o*(TH+lab+pad)+hdr+rows_u*(TH+lab+pad)+hdr+(TH+lab+pad)+pad
sh=Image.new('RGB',(W,H),'#000'); d=ImageDraw.Draw(sh); fh=ImageFont.truetype(F,34)
d.text((pad,10),f"OUTLIERS in/near our lane ({len(tiles)}): views ÷ channel subscribers, sorted. Pulled Nov 15 2026 via yt-dlp",font=fh,fill='#ffd23f')
for i,t in enumerate(tiles): sh.paste(t,(pad+(i%cols)*(TW+pad),hdr+(i//cols)*(TH+lab+pad)))
y0=hdr+rows_o*(TH+lab+pad)
d.text((pad,y0+10),"OURS: all 13 long-forms + top 3 Shorts (Meatball Myths, 1,010 subs; long-form median 43 views)",font=fh,fill='#ff6b5e')
for i,t in enumerate(ot): sh.paste(t,(pad+(i%cols)*(TW+pad),y0+hdr+(i//cols)*(TH+lab+pad)))
y1=y0+hdr+rows_u*(TH+lab+pad)
d.text((pad,y1+10),'NEW: v3 thumbnail + title pairs built to the outlier patterns',font=fh,fill='#7CFF6B')
for i,t in enumerate(v2): sh.paste(t,(pad+i*(TW+pad),y1+hdr))
out=os.environ.get('OUT','/workspace/meatball-animation-v2/samples/v3_outlier_contact_sheet.png')
sh.save(out); print(sh.size)
