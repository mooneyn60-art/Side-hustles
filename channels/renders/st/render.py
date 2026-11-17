import json, math, random, sys, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from multiprocessing import Pool
W,H,FPS=1080,1920,30
TL=json.load(open('timeline.json')); TOTAL=TL['total']; WORDS=TL['words']
NF=int(round(TOTAL*FPS))
FONT='/usr/share/fonts/truetype/sand-box/google/Luckiest Guy/LuckiestGuy-Regular.ttf'
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
LINES=["Giant house spider in your tub? Probably stuck.","His dog, Noodle, stares from the bathmat.","It is not an extremely active climber.","In the Pacific Northwest, the giant house spider is usually trapped in sinks or bathtubs where it has ventured in search of water.","What's the biggest spider you've found in your tub? And"]
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
    cx=495; y=1060; x=cx-tw/2
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
# ---------------- shots ----------------
def wiggle(t,hz=10): return (int(t*hz)%2==1)
def shot(t):
    """returns (frame RGBA, zoom, focus(x,y), shake(dx,dy))"""
    z=1.0; foc=(540,960); sh=(0,0)
    if t<2.70:  # A: tub close, spider skitters, punch-in, tries wall, boing slide
        fr=getbg('tubclose').copy()
        # skitter path
        if t<1.75:
            x=300+260*ease_io(t/1.7)+12*math.sin(t*40); y=1000+20*math.sin(t*23)
            name='spider_panicked'
        elif t<2.05:
            k=(t-1.75)/0.30; x=560; y=1000-150*ease_io(k); name='spider_panicked'
        else:
            k=(t-2.05)/0.25; x=560; y=850+150*min(1,k*k); name='spider_ohno'
        sq=1.0
        if t>=2.30: 
            k=(t-2.30)/0.25; sq=1+0.22*math.sin(min(1,k)*math.pi)*(1-min(1,k))
        if t<1.75: speedlines(fr,x,y-170,1,0,n=5,length=150,spread=140,seed=int(t*10))
        if 1.75<=t<2.05: speedlines(fr,x,y-150,0,-1,n=5,length=120,spread=130,seed=3)
        if t>=2.05 and t<2.35: speedlines(fr,x,y-300,0,1,n=5,length=140,spread=130,seed=4)
        place(fr,name,x,y,480,sx=sq,sy=1/sq,rot=(4 if wiggle(t,12) else -4),flip=wiggle(t,8))
        # camera
        if t<0.35: sh=(int(18*math.sin(t*90)),int(14*math.cos(t*70)))
        z=1.0+0.15*ease_back((t-0.61)/0.25) if t>=0.61 else 1.0
        if t>=1.75: z=1.15-0.08*ease_io((t-1.75)/0.5)
        foc=(540,880)
        if 2.05<=t<2.25: sh=(int(10*math.sin(t*120)),0)
        return fr,z,foc,sh
    if t<4.10:  # B: wide; Meatball hops in, Noodle on mat pops on his name
        fr=getbg('wide').copy(); lt=t-2.70
        place(fr,'spider_smug',800,905,180,rot=(3 if wiggle(t,6) else -3))
        mat(fr,560,1500)
        k=min(1,lt/0.42); mx=-120+330*ease_io(k); hop=math.sin(k*math.pi)*210 if k<1 else 0
        sq=1.0
        if 0.42<=lt<0.62: sq=1+0.2*math.sin((lt-0.42)/0.2*math.pi)
        bob=6*math.sin(lt*14) if lt>0.62 else 0
        place(fr,'mb_roasting',mx,1470-hop+bob,300,sx=sq,sy=1/sq)
        nname='noodle_happy' if t<3.60 else 'noodle_startled'
        nsq=1.0
        if t>=3.60: nsq=1+0.18*math.sin(min(1,(t-3.60)/0.2)*math.pi)*(1-min(1,(t-3.6)/0.4))
        place(fr,nname,600,1490,310,sx=nsq,sy=1/nsq)
        if 3.60<=t<3.95: burst(fr,600,1330,190,250,n=12)
        z=1.12+0.04*ease_io(lt/1.4); foc=(520,1180)
        return fr,z,foc,sh
    if t<5.55:  # C: Noodle close, stare, record scratch freeze
        fr=getbg('wide').copy(); lt=t-4.10
        place(fr,'spider_offended',860,905,170,flip=wiggle(t,6))
        nm='noodle_startled' if t<4.20 else 'noodle_unimpressed'
        mat(fr,470,1620)
        place(fr,nm,470,1600,760)
        if t>=4.20:
            d=ImageDraw.Draw(fr)
            for k in range(3):
                d.line([620,1080+k*22,830,875+k*14],fill=(255,211,77,230),width=10)
        z=1.0+0.12*ease_back((t-4.20)/0.2) if t>=4.20 else 1.04
        foc=(560,1000)
        if 4.20<=t<4.45: sh=(int(12*math.sin(t*100)),int(6*math.cos(t*80)))
        return fr,z,foc,sh
    if t<7.55:  # D: tub wall climb attempt, slide, laugh
        fr=getbg('wall').copy(); lt=t-5.55
        if t<6.85:
            k=(t-5.55)/1.30; y=1500-520*ease_io(k)+10*math.sin(t*45); nm='spider_panicked'; x=560+8*math.sin(t*60)
            speedlines(fr,x,y-150,0,-1,n=5,length=130,spread=140,seed=int(t*8))
        else:
            k=min(1,(t-6.85)/0.28); y=980+520*k*k; nm='spider_ohno'; x=560
            if k<1: speedlines(fr,x,y-320,0,1,n=5,length=150,spread=140,seed=9)
        sq=1.0
        if t>=7.13: kk=(t-7.13)/0.3; sq=1+0.28*math.sin(min(1,kk)*math.pi)*(1-min(1,kk))
        place(fr,nm,x,y,440,sx=sq,sy=1/sq,rot=(5 if wiggle(t,14) else -5) if t<6.85 else 0,flip=wiggle(t,10))
        if t>=7.0:
            k=ease_back((t-7.0)/0.25); place(fr,'mb_roastlaugh',190,1500+12*math.sin(t*30),260*k)
        z=1.0+0.06*ease_io(lt/2); foc=(560,1200)
        if 7.13<=t<7.35: sh=(0,int(14*math.sin(t*120)))
        return fr,z,foc,sh
    if t<9.05:  # E: wide, slow pan, Meatball "nailed it"
        fr=getbg('wide').copy(); lt=t-7.55
        place(fr,'spider_ohno',800,905,180)
        mat(fr,560,1500)
        place(fr,'noodle_unimpressed',600,1490,310)
        place(fr,'mb_nailedit',200,1470+5*math.sin(t*10),300)
        z=1.14; foc=(470+130*ease_io(lt/1.5),1180)
        return fr,z,foc,sh
    if t<10.35: # F: spider glamour pose punch-in
        fr=getbg('tubclose').copy(); lt=t-9.05
        k=ease_back(lt/0.25)
        if lt>0.2: burst(fr,540,760,260,420,n=18,col=(255,211,77,255),seed=lt*2)
        place(fr,'spider_smug',540,1010,520*max(0.01,k),rot=6*math.sin(lt*8))
        z=1.0+0.15*ease_io(lt/1.3); foc=(540,800)
        return fr,z,foc,sh
    if t<11.85: # G: sink, Sauce watches & yawns huge
        fr=getbg('sink').copy(); lt=t-10.35
        place(fr,'spider_panicked',560,1010,210,rot=(4 if wiggle(t,12) else -4),flip=wiggle(t,8))
        if t<10.85: nm='sauce_unimpressed'; s=1.0
        else: nm='sauce_yawn'; s=1+0.25*ease_back((t-10.85)/0.2)
        place(fr,nm,900,1265,380*s)
        z=1.04+0.10*(ease_back((t-10.85)/0.2) if t>=10.85 else 0); foc=(780,1050)
        return fr,z,foc,sh
    if t<13.25: # H: tub wide, spider wanders tub floor, Meatball peeks
        fr=getbg('tubclose').copy(); lt=t-11.85
        x=820-520*ease_io(lt/1.4)+10*math.sin(t*40); y=1000+30*math.sin(t*9)
        speedlines(fr,x,y-130,-1,0,n=4,length=110,spread=100,seed=int(t*8))
        place(fr,'spider_offended',x,y,420,rot=(4 if wiggle(t,12) else -4),flip=wiggle(t,8))
        pk=ease_back((lt-0.5)/0.3) if lt>0.5 else 0
        if pk>0: place(fr,'mb_smug',1120-180*pk,1480,300)
        z=1.0; foc=(540,960)
        return fr,z,foc,sh
    if t<14.35: # I: faucet drip, spider looks up
        fr=getbg('faucet').copy(); lt=t-13.25
        place(fr,'spider_smug' if t<13.85 else 'spider_offended',600,1560,460)
        # drop
        d=ImageDraw.Draw(fr)
        if lt<0.6:
            dy=430+ (lt/0.6)**2*820
            d.ellipse([415,dy,455,dy+60],fill=(143,211,255),outline=INK,width=5)
            d.polygon([(420,dy+22),(435,dy-20),(450,dy+22)],fill=(143,211,255))
        elif lt<0.9:
            for a in range(-2,3):
                d.ellipse([435+a*40-14,1260-abs(a)*20,435+a*40+14,1288-abs(a)*20],fill=(143,211,255),outline=INK,width=4)
        z=1.0 if t<13.85 else 1.0+0.12*ease_back((t-13.85)/0.2); foc=(435,1300)
        if 13.85<=t<14.05: sh=(int(10*math.sin(t*110)),0)
        return fr,z,foc,sh
    if t<15.70: # J: Noodle slides the whole bathmat further from the tub, with himself on it
        fr=getbg('wide').copy(); lt=t-14.35
        k=ease_io(min(1,lt/0.95)); dx=-380*k
        place(fr,'spider_smug',800,905,180)
        if 0.05<lt<0.95: speedlines(fr,600+dx,1380,-1,0,n=4,length=170,spread=150,seed=int(t*8))
        mat(fr,560+dx,1500)
        sq=1.0
        if lt>=0.95: kk=(lt-0.95)/0.3; sq=1+0.15*math.sin(min(1,kk)*math.pi)*(1-min(1,kk))
        place(fr,'noodle_worried',600+dx,1490,310,sx=sq,sy=1/sq)
        z=1.12; foc=(470,1180)
        if 0.95<=lt<1.15: sh=(int(10*math.sin(t*120)),0)
        return fr,z,foc,sh
    # K: spider close, looks at viewer, slow push, loop flash
    fr=getbg('tubclose').copy(); lt=t-15.70
    nm='spider_smug'
    place(fr,nm,540,1020,600,rot=3*math.sin(lt*6))
    z=1.0+0.18*ease_io(lt/1.3); foc=(540,880)
    return fr,z,foc,sh
def frame(i):
    t=i/FPS
    fr,z,foc,sh=shot(t)
    if z!=1.0:
        cw,ch=W/z,H/z
        x0=min(max(foc[0]-cw/2,0),W-cw); y0=min(max(foc[1]-ch/2,0),H-ch)
        fr=fr.resize((W,H),Image.BICUBIC,box=(x0,y0,x0+cw,y0+ch))
    if sh!=(0,0):
        g=Image.new('RGBA',(W,H),(0,0,0,255)); g.alpha_composite(fr,(sh[0],sh[1]))
        big=fr.resize((int(W*1.04),int(H*1.04))); g=big.crop((int(W*0.02)-sh[0],int(H*0.02)-sh[1],int(W*0.02)-sh[0]+W,int(H*0.02)-sh[1]+H))
        fr=g
    # freeze-frame tint on record scratch beats
    if 4.20<=t<4.40 or 10.85<=t<11.0:
        fr=Image.blend(fr,Image.new('RGBA',(W,H),(255,255,255,255)),0.25)
    fr.alpha_composite(card(),(85,150))
    captions(fr,t)
    return fr.convert('RGB').tobytes()
if __name__=='__main__':
    only=[int(x) for x in sys.argv[1:]]
    if only:
        for i in only: Image.frombytes('RGB',(W,H),frame(i)).save(f'prev_{i:04d}.png')
        sys.exit()
    p=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','video.mp4'],stdin=subprocess.PIPE)
    with Pool(7) as pool:
        for b in pool.imap(frame,range(NF),chunksize=4): p.stdin.write(b)
    p.stdin.close(); p.wait(); print('frames',NF)
