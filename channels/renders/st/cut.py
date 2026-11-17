import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as nd
A='/tmp/sh-sched/channels/animation/'
def cut(fn,box,name):
    im=np.asarray(Image.open(A+fn).convert('RGB').crop(box)).astype(int)
    r,g,b=im[...,0],im[...,1],im[...,2]
    lum=(r+g+b)/3
    loose=(lum>160)&((r-b)>=6)&((r-b)<=48)&(g>=b-3)&(g<=r+3)&(np.abs(r-g)<30)
    lab,n=nd.label(loose)
    border=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))-{0}
    bg=np.isin(lab,list(border))
    cream=np.array([253,247,235])
    strict=(np.sqrt(((im-cream)**2).sum(-1))<16)&((r-b)>9)
    lab2,n2=nd.label(strict)
    sizes=nd.sum(strict,lab2,range(1,n2+1))
    big=[i+1 for i,s in enumerate(sizes) if s>12000]
    bg|=np.isin(lab2,big)
    fg=~bg
    SEEDS={'mb_roasting':[(449,1074)],'spider_offended':[(505,215)],'spider_smug':[(122,203)],'spider_ohno':[(1270,214)],'spider_panicked':[(874,165),(894,182)]}
    light=(lum>195)
    hl,hn=nd.label(light)
    for (sx,sy) in SEEDS.get(name,[]):
        k=hl[sy-box[1],sx-box[0]]
        if k: fg[nd.binary_dilation(hl==k,iterations=1)]=False
    fg=nd.binary_opening(fg,iterations=1)
    lab3,n3=nd.label(fg)
    sizes=nd.sum(fg,lab3,range(1,n3+1))
    L=int(np.argmax(sizes))+1
    bl=set(np.unique(np.concatenate([lab3[0],lab3[-1],lab3[:,0],lab3[:,-1]])))
    keep=[i+1 for i,s in enumerate(sizes) if (i+1==L) or (s>0.002*sizes[L-1] and (i+1) not in bl)]
    fg=np.isin(lab3,keep)
    fg=nd.binary_fill_holes(fg) if name.startswith('x') else fg
    fg=nd.binary_erosion(fg,iterations=1)
    a=Image.fromarray((fg*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))
    out=Image.fromarray(im.astype(np.uint8)).convert('RGBA'); out.putalpha(a)
    bb=out.getbbox(); out=out.crop(bb)
    out.save(f'cut/{name}.png'); return out
jobs=[('noodle-sauce-final.jpg',(50,175,612,628),'noodle_main'),
('noodle-sauce-final.jpg',(950,343,1230,634),'sauce_main'),
('noodle-sauce-final.jpg',(650,343,912,634),'mb_main')]
for i,nm in enumerate(['happy','worried','sniff','mouthfull','zoomies','sleepy','unimpressed','startled']):
    jobs.append(('noodle-expressions-v1.jpg',(320*(i%4),0 if i<4 else 345,320*(i%4)+320,340 if i<4 else 720),'noodle_'+nm))
for i,nm in enumerate(['smug','unimpressed','annoyed','shocked','swipe','back','sleep','yawn']):
    jobs.append(('sauce-expressions-v1.jpg',(320*(i%4),0 if i<4 else 345,320*(i%4)+320,340 if i<4 else 720),'sauce_'+nm))
for i,nm in enumerate(['neutral','shock','scared','angry','smug','hurt','happy','dizzy']):
    jobs.append(('meatball-expression-sheet-v1.jpg',(320*(i%4),0 if i<4 else 345,320*(i%4)+320,340 if i<4 else 690),'mb_'+nm))
for nm,(x0,x1) in zip(['smug','offended','panicked','ohno','roasted'],[(40,320),(470,715),(770,1150),(1195,1485),(1580,1880)]):
    jobs.append(('bugs-expressions-v1.jpg',(x0,20,x1,358),'spider_'+nm))
for nm,(x0,x1) in zip(['roasting','roastlaugh','nailedit'],[(410,745),(800,1115),(1205,1495)]):
    jobs.append(('bugs-expressions-v1.jpg',(x0,880,x1,1228),'mb_'+nm))
outs=[]
for j in jobs: outs.append((j[2],cut(*j)))
# contact sheet on magenta to reveal halos
W=8; cs=Image.new('RGB',(W*260,((len(outs)+W-1)//W)*280),(255,0,255))
for k,(nm,o) in enumerate(outs):
    t=o.copy(); t.thumbnail((250,250)); cs.paste(t,((k%W)*260+5,(k//W)*280+5),t)
cs.save('cut/contact.png'); print(len(outs))
