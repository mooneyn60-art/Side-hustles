import json, math, random, sys, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from multiprocessing import Pool
W,H,FPS=1080,1920,30
TL=json.load(open('timeline.json')); TOTAL=TL['total']; WORDS=TL['words']
NF=int(round(TOTAL*FPS))
FONT='/dev/shm/st2/fonts/package/files/luckiest-guy-latin-400-normal.woff'
INK=(17,17,17)
SPR={}
def spr(n):
    if n not in SPR: SPR[n]=Image.open(f'cut/{n}.png').convert('RGBA')
    return SPR[n]
RS={}
def sized(n,h,flip=False):
    k=(n,int(h),flip)
    if k not in RS:
        s=spr(n); w=max(1,int(s.width*h/s.height)); im=s.resize((w,int(h)),Image.LANCZOS)
        if flip: im=im.transpose(Image.FLIP_LEFT_RIGHT)
        RS[k]=im
    return RS[k]
def ease_back(x,c=1.2):
    x=min(max(x,0),1); return 1+(c+1)*(x-1)**3+c*(x-1)**2
def ease_io(x):
    x=min(max(x,0),1); return x*x*(3-2*x)
def place(fr,n,cx,by,h,sx=1.0,sy=1.0,rot=0,flip=False,alpha=1.0):
    """bottom-center anchor at (cx,by); h = base height; sx/sy squash"""
    if h<6: return
    s=sized(n,h,flip)
    if sx!=1 or sy!=1:
        s=s.resize((max(1,int(s.width*sx)),max(1,int(s.height*sy))),Image.BILINEAR)
    if rot: s=s.rotate(rot,resample=Image.BICUBIC,expand=True)
    if alpha<1:
        a=s.getchannel('A').point(lambda v:int(v*alpha)); s=s.copy(); s.putalpha(a)
    fr.alpha_composite(s,(int(cx-s.width/2),int(by-s.height)))
# ---------------- backgrounds (drawn 2x then downsampled) ----------------
BG={}
def S2(): 
    im=Image.new('RGB',(W*2,H*2),(255,255,255)); return im,ImageDraw.Draw(im)
def tiles(d,y0,y1,col=(191,230,232),grout=(150,205,208),sz=240):
    d.rectangle([0,y0,W*2,y1],fill=col)
    for x in range(0,W*2+1,sz): d.line([x,y0,x,y1],fill=grout,width=8)
    for y in range(y0,y1+1,sz): d.line([0,y,W*2,y],fill=grout,width=8)
def floor(d,y0):
    d.rectangle([0,y0,W*2,H*2],fill=(233,213,181))
    for y in range(y0,H*2,140): d.line([0,y,W*2,y],fill=(214,190,152),width=8)
    d.line([0,y0,W*2,y0],fill=INK,width=14)
def bg_tubclose():
    im,d=S2()
    d.rectangle([0,0,W*2,H*2],fill=(120,190,200))
    tiles(d,0,H*2)
    # tub interior, top-down
    d.rounded_rectangle([60,520,W*2-60,H*2+400],radius=420,fill=(255,255,255),outline=INK,width=22)
    d.rounded_rectangle([200,700,W*2-200,H*2+300],radius=340,fill=(236,244,250))
    d.rounded_rectangle([260,760,W*2-260,H*2+260],radius=300,fill=(248,251,253))
    # gloss streaks
    d.line([380,900,520,820],fill=(255,255,255),width=30)
    # drain
    cx,cy=W,2700
    d.ellipse([cx-110,cy-110,cx+110,cy+110],fill=(200,205,212),outline=INK,width=14)
    for k in range(-60,61,30): d.line([cx+k,cy-70,cx+k,cy+70],fill=(120,125,135),width=10)
    return im
def bg_wide():
    im,d=S2()
    tiles(d,0,2300)
    floor(d,2300)
    d.rounded_rectangle([880,1640,W*2+200,2420],radius=120,fill=(255,255,255),outline=INK,width=18)
    d.rounded_rectangle([920,1680,W*2+200,1790],radius=60,fill=(230,240,247))
    d.rectangle([1000,2420,1080,2500],fill=INK); d.rectangle([W*2-120,2420,W*2-40,2500],fill=INK)
    d.rounded_rectangle([1900,1420,1980,1660],radius=30,fill=(200,206,214),outline=INK,width=12)
    d.rounded_rectangle([1780,1400,1980,1470],radius=30,fill=(200,206,214),outline=INK,width=12)
    d.line([0,420,W*2,420],fill=INK,width=16)
    for i,x in enumerate(range(-40,560,110)):
        d.rounded_rectangle([x,440,x+120,1900],radius=40,fill=(255,214,120) if i%2 else (255,196,90),outline=INK,width=10)
    return im
MAT=None
def mat(fr,cx,by):
    global MAT
    if MAT is None:
        m=Image.new('RGBA',(1000,300),(0,0,0,0)); d=ImageDraw.Draw(m)
        for x in range(40,960,46): d.line([x,220,x,280],fill=(80,140,190,255),width=10)
        d.rounded_rectangle([10,10,990,240],radius=60,fill=(111,179,224,255),outline=INK,width=14)
        d.rounded_rectangle([60,50,940,200],radius=40,outline=(160,205,236,255),width=10)
        MAT=m.resize((500,150),Image.LANCZOS)
    fr.alpha_composite(MAT,(int(cx-250),int(by-110)))
def bg_wall():
    im,d=S2()
    tiles(d,0,H*2)
    d.rounded_rectangle([140,300,W*2-140,H*2+200],radius=200,fill=(255,255,255),outline=INK,width=22)
    for i,x in enumerate([420,700,1500]): d.line([x,500,x,3400],fill=(232,241,248),width=60+20*i)
    d.rectangle([162,3260,W*2-162,H*2],fill=(232,240,247))
    d.line([162,3260,W*2-162,3260],fill=(170,185,200),width=10)
    return im
def bg_sink():
    im,d=S2()
    tiles(d,0,H*2,col=(205,230,240),grout=(165,200,215))
    d.rectangle([0,2500,W*2,H*2],fill=(243,225,199)); d.line([0,2500,W*2,2500],fill=INK,width=16)
    d.rectangle([0,2440,W*2,2520],fill=(250,238,220),outline=INK,width=14)
    d.ellipse([260,1500,1900,2560],fill=(255,255,255),outline=INK,width=20)
    d.ellipse([380,1600,1780,2440],fill=(225,238,246))
    d.ellipse([1020,2120,1140,2190],fill=(160,168,178),outline=INK,width=10)
    d.rounded_rectangle([1020,1000,1140,1520],radius=40,fill=(200,206,214),outline=INK,width=14)
    d.rounded_rectangle([700,960,1140,1080],radius=50,fill=(200,206,214),outline=INK,width=14)
    return im
def bg_faucet():
    im,d=S2()
    tiles(d,0,H*2)
    d.rounded_rectangle([140,2200,W*2-140,H*2+200],radius=200,fill=(255,255,255),outline=INK,width=22)
    d.rectangle([162,2350,W*2-162,H*2],fill=(240,246,251))
    d.rounded_rectangle([1300,400,1560,1500],radius=80,fill=(200,206,214),outline=INK,width=18)
    d.rounded_rectangle([760,400,1560,620],radius=100,fill=(200,206,214),outline=INK,width=18)
    d.rounded_rectangle([760,560,980,860],radius=60,fill=(185,192,202),outline=INK,width=18)
    d.line([830,460,1200,460],fill=(255,255,255),width=24)
    return im
def getbg(n):
    if n not in BG:
        BG[n]=globals()['bg_'+n]().resize((W,H),Image.LANCZOS).convert('RGBA')
    return BG[n]
# ---------------- overlays ----------------
def speedlines(fr,cx,cy,dirx,diry,n=6,length=160,spread=120,seed=0,col=(60,60,70,170),w=7):
    n=min(n,4)
    d=ImageDraw.Draw(fr); rnd=random.Random(seed)
    for i in range(n):
        off=(i-(n-1)/2)*spread/(n/2)
        px,py=cx+(-diry)*off,cy+dirx*off
        L=length*(0.6+0.4*rnd.random()); b=230+rnd.random()*60
        d.line([px-dirx*b,py-diry*b,px-dirx*(b+L),py-diry*(b+L)],fill=col,width=w)
def burst(fr,cx,cy,r0,r1,n=16,col=(255,211,77,255),seed=1):
    d=ImageDraw.Draw(fr)
    for i in range(n):
        a=2*math.pi*i/n+seed
        d.line([cx+math.cos(a)*r0,cy+math.sin(a)*r0,cx+math.cos(a)*r1,cy+math.sin(a)*r1],fill=col,width=14)
FCACHE={}
def font(sz):
    if sz not in FCACHE: FCACHE[sz]=ImageFont.truetype(FONT,sz)
    return FCACHE[sz]
CARD=None
def card():
    global CARD
    if CARD is None:
        im=Image.new('RGBA',(820,200),(0,0,0,0)); d=ImageDraw.Draw(im)
        d.rounded_rectangle([0,0,819,199],radius=36,fill=(20,20,28,215),outline=(255,255,255,255),width=5)
        t1='PACIFIC NORTHWEST ·'; t2='GIANT HOUSE SPIDER (WSU)'
        f1=font(48); f2=font(66)
        w1=d.textlength(t1,font=f1); w2=d.textlength(t2,font=f2)
        d.text(((820-w1)/2,22),t1,font=f1,fill=(255,255,255),stroke_width=5,stroke_fill=INK)
        d.text(((820-w2)/2,90),t2,font=f2,fill=(255,211,77),stroke_width=6,stroke_fill=INK)
        CARD=im
    return CARD
LINES=["Giant house spider in your tub? Probably stuck.","It is not an extremely active climber.","Meatball takes full credit for the trapping.","His dog, Noodle, is already halfway down the hall.","In the Pacific Northwest, the giant house spider is usually trapped in sinks or bathtubs where it has ventured in search of water.","What's the biggest spider you've found in your tub? And"]
TOK=[]
for l in LINES: TOK+=l.split()
assert len(TOK)==len(WORDS),(len(TOK),len(WORDS))
for k,w in enumerate(WORDS): w.append(TOK[k].upper())
GROUPS=[];cur=[]
for i,wd in enumerate(WORDS):
    cur.append(wd)
    txt=' '.join(x[4] for x in cur)
    nxt=WORDS[i+1] if i+1<len(WORDS) else None
    endp = nxt is None or nxt[3]!=wd[3] or wd[4].endswith((',','?','.'))
    if len(cur)>=3 or endp or (nxt and len(txt)+1+len(nxt[4])>15):
        GROUPS.append(cur); cur=[]
def captions(fr,t):
    g=None
    for gi,G in enumerate(GROUPS):
        end=GROUPS[gi+1][0][0] if gi+1<len(GROUPS) else TOTAL
        if G[-1][3]!=(GROUPS[gi+1][0][3] if gi+1<len(GROUPS) else -1): end=min(end,G[-1][1]+0.25)
        if G[0][0]-0.03<=t<end: g=G;break
    if not g: return
    sz=104; f=font(sz); d=ImageDraw.Draw(fr)
    toks=[w[4] for w in g]
    widths=[d.textlength(x,font=f) for x in toks]; sp=d.textlength(' ',font=f)
    tw=sum(widths)+sp*(len(toks)-1)
    while tw>800:
        sz-=6; f=font(sz); widths=[d.textlength(x,font=f) for x in toks]; sp=d.textlength(' ',font=f); tw=sum(widths)+sp*(len(toks)-1)
    cx=540; y=CAPY; x=cx-tw/2
    for k,w in enumerate(g):
        if t<w[0]-0.03: 
            x+=widths[k]+sp; continue
        active = w[0]-0.03<=t<(g[k+1][0]-0.03 if k+1<len(g) else 99)
        pop=ease_back((t-w[0]+0.03)/0.12)
        s=sz*(0.6+0.4*pop) if pop<1 else sz
        s=int(s)
        ff=font(max(20,s))
        col=(255,211,77) if active else (255,255,255)
        wx=d.textlength(w[4],font=ff)
        d.text((x+widths[k]/2-wx/2, y+(sz-s)*0.7),w[4],font=ff,fill=col,stroke_width=max(6,s//10),stroke_fill=INK)
        x+=widths[k]+sp
CAPY=420
ST=TL['starts']
L0,L1,L2,L3,L4,L5=ST
def jit(t,hz,amp,seed=0):
    k=int(t*hz); r=random.Random(k*7919+seed); return (r.random()*2-1)*amp
def skitter(t,x,y,hz=16):
    """quick stepped scuttle: hops of a few px, alternating tilt, tiny bob"""
    step=int(t*hz)
    dx=jit(t,hz,10,1); dy=-abs(math.sin(t*hz*math.pi))*8
    rot=6 if step%2 else -6
    return x+dx,y+dy,rot
def bg_hall():
    im,d=S2()
    d.rectangle([0,0,W*2,H*2],fill=(250,226,170))
    for x in range(0,W*2,90): d.line([x,0,x,2600],fill=(244,214,150),width=26)
    d.rectangle([0,2600,W*2,H*2],fill=(196,140,92)); d.line([0,2600,W*2,2600],fill=INK,width=16)
    for y in range(2700,H*2,150): d.line([0,y,W*2,y],fill=(176,122,78),width=8)
    # doorframe on the right
    d.rectangle([1620,700,2160,2600],fill=(120,82,52)); d.rectangle([1700,780,2160,2600],fill=(60,40,28))
    d.line([1620,700,1620,2600],fill=INK,width=16); d.line([1620,700,2160,700],fill=INK,width=16)
    # picture frame
    d.rectangle([300,900,900,1400],fill=(255,255,255),outline=INK,width=16); d.polygon([(340,1360),(560,1080),(760,1360)],fill=(140,200,140))
    return im
def bg_sink2():  # sink with counter edge, room for a shoe
    im,d=S2()
    tiles(d,0,H*2,col=(205,230,240),grout=(165,200,215))
    d.rectangle([0,2260,W*2,H*2],fill=(243,225,199)); d.line([0,2260,W*2,2260],fill=INK,width=16)
    d.rectangle([0,2200,W*2,2290],fill=(250,238,220),outline=INK,width=14)
    d.ellipse([500,1500,1660,2290],fill=(255,255,255),outline=INK,width=20)
    d.ellipse([600,1580,1560,2200],fill=(225,238,246))
    d.ellipse([1020,1960,1140,2030],fill=(160,168,178),outline=INK,width=10)
    d.rounded_rectangle([1020,1000,1140,1520],radius=40,fill=(200,206,214),outline=INK,width=14)
    d.rounded_rectangle([700,960,1140,1080],radius=50,fill=(200,206,214),outline=INK,width=14)
    return im
globals()['bg_hall']=bg_hall; globals()['bg_sink2']=bg_sink2
SHOE=None
def shoe(h=150):
    global SHOE
    if SHOE is None:
        m=Image.new('RGBA',(520,300),(0,0,0,0)); d=ImageDraw.Draw(m)
        d.rounded_rectangle([20,170,500,270],radius=40,fill=(255,255,255),outline=INK,width=14)
        d.polygon([(40,180),(60,40),(240,30),(300,120),(470,150),(490,190),(40,190)],fill=(220,60,60),outline=INK)
        d.line([(60,40),(240,30),(300,120),(470,150),(490,190)],fill=INK,width=14)
        for k in range(4): d.line([120+k*40,70,150+k*40,120],fill=(255,255,255),width=10)
        SHOE=m
    s=SHOE.resize((int(SHOE.width*h/300),h),Image.LANCZOS); return s
def put(fr,im,cx,cy,rot=0):
    if rot: im=im.rotate(rot,resample=Image.BICUBIC,expand=True)
    fr.alpha_composite(im,(int(cx-im.width/2),int(cy-im.height/2)))
def cap(fr,cx,top,w):
    d=ImageDraw.Draw(fr)
    d.chord([cx-w*0.62,top-w*0.30,cx+w*0.62,top+w*0.34],180,360,fill=(140,200,255),outline=INK,width=8)
    for k in range(-2,3): d.ellipse([cx+k*w*0.22-18,top-w*0.30-10+abs(k)*14,cx+k*w*0.22+18,top-w*0.30+26+abs(k)*14],fill=(255,255,255),outline=INK,width=4)
    d.line([cx-w*0.62,top+w*0.02,cx+w*0.62,top+w*0.02],fill=(90,150,220),width=12)
def shing(fr,cx,cy,t0,t):
    if 0<=t-t0<0.35:
        k=(t-t0)/0.35; d=ImageDraw.Draw(fr); r=40+120*k
        for a in range(4):
            ang=a*math.pi/2+0.4
            d.line([cx+math.cos(ang)*r*0.3,cy+math.sin(ang)*r*0.3,cx+math.cos(ang)*r,cy+math.sin(ang)*r],fill=(255,240,140,255),width=12)
def droplet(fr,cx,cy,s=1.0):
    d=ImageDraw.Draw(fr)
    d.ellipse([cx-40*s,cy-40*s,cx+40*s,cy+40*s],fill=(143,211,255),outline=INK,width=6)
    d.polygon([(cx-36*s,cy-14*s),(cx,cy-95*s),(cx+36*s,cy-14*s)],fill=(143,211,255))
    d.line([(cx-36*s,cy-14*s),(cx,cy-95*s),(cx+36*s,cy-14*s)],fill=INK,width=6)
    d.ellipse([cx-18*s,cy-18*s,cx-4*s,cy-4*s],fill=(255,255,255))
def mbh(fr,name,cx,by,h,raised=True,capon=True,shoeon=True,t=0,salute=False):
    place(fr,name,cx,by,h)
    w=h*0.92
    if capon: cap(fr,cx,by-h*0.82,w*0.62)
    if shoeon and raised:
        put(fr,shoe(int(h*0.42)),cx+w*0.42,by-h*1.0,rot=35)
def shot(t):
    z=1.0; foc=(540,960); sh=(0,0)
    # last 0.4 s: hard cut back to the frame-1 spider close-up (loop)
    if t>=TOTAL-0.40 or t<L0+1.40:
        fr=getbg('tubclose').copy()
        x,y,r=skitter(t,540,1300)
        if t<0.12: x,y,r=540,1300,0
        place(fr,'spider_panicked',x,y,560,rot=r,flip=(int(t*8)%2==1) and t>=0.12)
        if t<0.30: sh=(int(14*math.sin(t*90)),int(10*math.cos(t*70)))
        return fr,1.0,foc,sh
    if t<L1:  # one wide tub shot: spider small at the drain end, Meatball far end, shower cap, shoe like a sword
        fr=getbg('wide').copy(); lt=t-(L0+1.40)
        x,y,r=skitter(t,1000,905,hz=12)
        place(fr,'spider_ohno',x,y,190,rot=r)
        hop=ease_back(min(1,lt/0.18))
        mbh(fr,'mb_happy',170,1600,int(330*hop) if hop>0.05 else 10,t=t)
        shing(fr,170+330*0.92*0.42,1600-330,0.10+L0+1.40,t)
        return fr,1.0,(540,1100),sh
    if t<L2:  # spider slides up the tub wall and straight back down; slide whistle near the end
        fr=getbg('wall').copy(); lt=t-L1; dur=L2-L1
        up_end=dur*0.62
        if lt<up_end:
            k=ease_io(lt/up_end); y=1720-520*k; x,y,r=skitter(t,540,y,hz=18); nm='spider_panicked'
            speedlines(fr,x,y-150,0,-1,n=4,length=110,spread=120,seed=int(t*8))
        else:
            k=min(1,(lt-up_end)/0.30); y=1200+520*k*k; x=540; r=0; nm='spider_ohno'
            if k<1: speedlines(fr,x,y-300,0,1,n=4,length=150,spread=130,seed=9)
        sq=1.0
        if lt>up_end+0.30: kk=(lt-up_end-0.30)/0.3; sq=1+0.25*math.sin(min(1,kk)*math.pi)*(1-min(1,kk))
        place(fr,nm,x,y,430,sx=sq,sy=1/sq,rot=r)
        if 0<=lt-up_end-0.30<0.2: sh=(0,int(12*math.sin(t*120)))
        return fr,1.0,foc,sh
    if t<L3:  # Meatball alone: plants the shoe on the sink like a flag, salutes
        fr=getbg('sink2').copy(); lt=t-L2
        k=ease_back(min(1,lt/0.45))
        sx=760+(330-760)*(1-k) ; sy=2290/2-10
        put(fr,shoe(130),330,900-80*(1-k),rot=-10+50*(1-k))
        if lt>0.40:
            d=ImageDraw.Draw(fr); d.line([330,850,330,640],fill=INK,width=10)
            d.polygon([(330,640),(440,670),(330,705)],fill=(255,211,77),outline=INK)
        nm='mb_nailedit' if lt>0.7 else 'mb_smug'
        place(fr,nm,760,1700,460); cap(fr,760,1700-460*0.82,460*0.92*0.62)
        if lt>1.1: burst(fr,380,660,70,120,n=10)
        return fr,1.04,(600,1150),sh
    if t<L4:  # hallway: Noodle zips left out of frame, bathmat spinning
        fr=getbg('hall').copy(); lt=t-L3
        mat_im=Image.new('RGBA',(520,180),(0,0,0,0)); dd=ImageDraw.Draw(mat_im)
        dd.rounded_rectangle([10,10,510,170],radius=50,fill=(111,179,224,255),outline=INK,width=12)
        put(fr,mat_im,560,1600,rot=(lt*540 if lt<1.6 else 1.6*540)%360)
        k=0 if lt<0.45 else min(1,(lt-0.45)/0.45); x=640-1100*ease_io(k)
        if 0<k<1:
            speedlines(fr,x+200,1420,1,0,n=4,length=220,spread=140,seed=int(t*10))
        if k<1:
            place(fr,'noodle_startled' if lt<0.45 else 'noodle_zoomies',x,1560,360,flip=True,rot=jit(t,20,4) if lt>=0.45 else 0)
        return fr,1.0,foc,sh
    if t<L5:
        lt=t-L4; dur=L5-L4
        a=L4+2.0; b=L4+4.9
        if t<a:  # spider close-up beside a water droplet
            fr=getbg('tubclose').copy()
            droplet(fr,780,1150,1.1)
            x,y,r=skitter(t,470,1320,hz=6)
            place(fr,'spider_smug',x,y,520,rot=r*0.5)
            return fr,1.0+0.05*ease_io(lt/2.0),(540,1100),sh
        if t<b:  # Sauce in the dry sink, slow deadpan blink
            fr=getbg('sink').copy(); kk=t-a
            nm='sauce_smug' if 0.55<=kk<0.95 else 'sauce_unimpressed'
            place(fr,nm,540,1180,400)
            return fr,1.0+0.06*ease_io(kk/2.9),(560,1200),sh
        if t>=b+1.0:  # back to the spider by the droplet for the rest of the fact line
            fr=getbg('tubclose').copy(); droplet(fr,780,1150,1.1)
            x,y,r=skitter(t,470,1320,hz=6); place(fr,'spider_smug',x,y,520,rot=r*0.5)
            return fr,1.05,(540,1100),sh
        # Noodle's head pokes around the hallway doorframe, then snaps back
        fr=getbg('hall').copy(); kk=t-b; rem=1.0
        out_=min(1,kk/0.25) if kk<0.80 else max(0,1-(kk-0.80)/0.10)
        layer=Image.new('RGBA',(W,H),(0,0,0,0))
        place(layer,'noodle_worried',1040-260*ease_io(out_),1560,420,flip=True)
        # mask: only show left of the doorframe edge (x<810)
        m=Image.new('L',(W,H),0); ImageDraw.Draw(m).rectangle([0,0,850,H],fill=255)
        layer.putalpha(Image.composite(layer.getchannel('A'),Image.new('L',(W,H),0),m))
        fr.alpha_composite(layer)
        return fr,1.0,foc,sh
    # line 5: Meatball alone at the sink, shoe raised; then Sauce nudges the shoe off the sink edge into the dry basin
    lt=t-L5; c=0.94
    if lt<c:
        fr=getbg('sink2').copy()
        mbh(fr,'mb_happy',760,1640,360,t=t)
        return fr,1.0,foc,sh
    fr=getbg('sink2').copy(); kk=lt-c
    place(fr,'sauce_swipe' if kk<0.9 else 'sauce_unimpressed',960,1150,330,flip=True)
    if kk<0.35: sx_,sy_,rr=800,900,0
    else:
        q=min(1,(kk-0.35)/0.35); sx_=800-240*q; sy_=900+100*q*q; rr=-110*q
    put(fr,shoe(140),sx_,sy_,rot=rr)
    if 0.70<=kk<0.95: sh=(int(8*math.sin(t*120)),0)
    return fr,1.0,foc,sh
def frame(i):
    t=i/FPS
    fr,z,foc,sh=shot(t)
    if z!=1.0:
        cw,ch=W/z,H/z
        x0=min(max(foc[0]-cw/2,0),W-cw); y0=min(max(foc[1]-ch/2,0),H-ch)
        fr=fr.resize((W,H),Image.BICUBIC,box=(x0,y0,x0+cw,y0+ch))
    if sh!=(0,0):
        big=fr.resize((int(W*1.04),int(H*1.04))); fr=big.crop((int(W*0.02)-sh[0],int(H*0.02)-sh[1],int(W*0.02)-sh[0]+W,int(H*0.02)-sh[1]+H))
    fr.alpha_composite(card(),(130,150))
    captions(fr,t)
    return fr.convert('RGB').tobytes()
if __name__=='__main__':
    only=[float(x) for x in sys.argv[1:]]
    if only:
        for s in only: Image.frombytes('RGB',(W,H),frame(int(s*FPS))).save(f'p_{s:05.2f}.png')
        sys.exit()
    p=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','video.mp4'],stdin=subprocess.PIPE)
    with Pool(6) as pool:
        for b in pool.imap(frame,range(NF),chunksize=4): p.stdin.write(b)
    p.stdin.close(); p.wait(); print('frames',NF)
