import skia
from PIL import Image
from kit import C
from characters import meatball, quadruped
s = skia.Surface(1600, 1000); cv = s.getCanvas(); cv.clear(C('#ffffff'))
meatball(cv, 230, 380, 1.5, {'face': 'neutral'})
meatball(cv, 560, 380, 1.3, {'face': 'shock', 'arms': 'up', 'sweat': True})
meatball(cv, 300, 800, 1.2, {'face': 'scared', 'run': 1.0})
quadruped(cv, 1150, 560, 1.0, 'grizzly', jaw=0.9)
quadruped(cv, 1150, 960, 0.6, 'grizzly', run=1.4)
Image.fromarray(s.makeImageSnapshot().toarray()[:, :, [2,1,0,3]]).convert('RGB').save('/workspace/meatball-animation-v2/work/character_ref.png')
