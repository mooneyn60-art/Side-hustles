"""Fix batch 1: one row per change, ready for Moondog88 to apply in Studio (nothing is applied by Jarvis).
Inputs: Studio exports (/workspace/yt-studio), public metadata (audio-audit/yt_full.jsonl), thumbnails (samples/fix-batch-1)."""
import csv, json, re, sys, os, statistics as st
sys.path.insert(0, '/workspace/ret'); from kw import is_kwlist
OUT = '/workspace/meatball-animation-v2/samples/fix-batch-1'
rows = json.load(open('/workspace/ret/channel_videos.json'))
thumbs = {r['video']: r['file'] for r in json.load(open(f'{OUT}/fix1_thumbs.json')) if r['video']}
pub = set()
for f in ['/workspace/audio-audit/yt_long_flat.json', '/workspace/audio-audit/yt_shorts_flat.json']:
    d = json.load(open(f)); pub |= {e['id'] for e in (d.get('entries', d) if isinstance(d, dict) else d)}

CREATURES = [('house centipede', '#housecentipede'), ('centipede', '#housecentipede'), ('30-legged', '#housecentipede'), ('mommy', '#daddylonglegs'), ('daddy', '#daddylonglegs'),
    ('harvestman', '#daddylonglegs'), ('cellar spider', '#cellarspider'), ('jumping spider', '#jumpingspider'), ('wolf spider', '#wolfspider'), ('false widow', '#falsewidow'),
    ('black widow', '#blackwidow'), ('widow', '#blackwidow'), ('recluse', '#brownrecluse'), ('roach', '#cockroach'), ('cockroach', '#cockroach'), ('bed bug', '#bedbugs'),
    ('bed mite', '#dustmites'), ('mattress', '#dustmites'), ('pillow', '#dustmites'), ('mite', '#mites'), ('silverfish', '#silverfish'), ('cricket', '#camelcricket'),
    ('boxelder', '#boxelderbugs'), ('lady beetle', '#ladybugs'), ('moth', '#clothesmoth'), ('termite', '#termites'), ('mice', '#mice'), ('mouse', '#mice'), ('stink bug', '#stinkbugs'), ('earwig', '#earwig'), ('flea', '#fleas'),
    ('tick', '#ticks'), ('ant ', '#ants'), ('ants', '#ants'), ('wasp', '#wasps'), ('fly', '#flies'), ('flies', '#flies'), ('carpet beetle', '#carpetbeetle'), ('beetle', '#beetles'),
    ('spider', '#spiders'), ('bug', '#bugs')]
ANIMALS = [('grizzly', '#grizzlybear', '#bearattack'), ('moose', '#moose', '#mooseattack'), ('shark', '#sharks', '#sharkattack'), ('hippo', '#hippo', '#hippoattack'),
    ('bison', '#bison', '#bisonattack'), ('croc', '#crocodile', '#crocodileattack'), ('lion', '#lion', '#lionattack'), ('cassowary', '#cassowary', '#cassowary'),
    ('honey badger', '#honeybadger', '#honeybadger'), ('jellyfish', '#boxjellyfish', '#jellyfishsting'), ('bear', '#bears', '#bearattack')]
def creature(t):
    tl = t.lower()
    for k, tag in CREATURES:
        if re.search(r'\b' + re.escape(k.strip()) + (r'' if k.strip().endswith('-legged') else r'(es|s)?\b'), tl): return tag
    return None
def lane(t, d):
    tl = (t + ' ' + d[:200]).lower()
    if 'things living' in t.lower() or 'spider venomous' in t.lower(): return 'bugs'
    if re.search(r'\b(dog|dogs|cat|cats|kitten|puppy)\b', t.lower()): return 'pets'
    if any(k in tl for k in ['cia', 'conspiracy', 'roswell', 'nuke the moon', 'northwoods', 'investigat', 'declassified', 'bermuda', 'plague of']): return 'mystery'
    if any(k in tl for k in ['faa', 'ground stop', 'flights', 'nvidia', 'jensen', 'election']): return 'news'
    if 'things living' in tl or 'venomous?' in tl or creature(t) and creature(t) != '#bugs' or 'bug' in tl: return 'bugs'
    if any(k in tl for k in ['survive', 'outrun', 'attack']) or any(a[0] in tl for a in ANIMALS): return 'wms'
    if any(k in tl for k in [' dog', 'dogs', ' cat', 'cats', 'kitten', 'puppy']): return 'pets'
    return 'animal-facts'
SERIES = re.compile(r'\s*\((Things Living In Your House|Is This Spider Venomous\?|Kill It or Keep It|Would Meatball Survive\?)[^)]*\)\s*$', re.I)
def clean_title(t):
    t2 = SERIES.sub('', t).strip()
    t2 = re.sub(r'\s*#\d+\s*$', '', t2)
    return t2
FULL = {'bugs': ('3 Bugs in Your House You Should Never Kill (And 4 You Must)', 'cH3HCZ8GlHk'),
        'spider': ("Don't Kill the Spider in Your Corner. It Eats Bigger Spiders", 'KWOM2-mNmww')}
def hashtags(kind, ln, t):
    c = creature(t)
    if ln == 'bugs':
        tags = [c if c and c != '#bugs' else '#housebugs', '#bugsinyourhouse', '#meatballmyths'] + (['#thingslivinginyourhouse', '#shorts'] if kind == 'short' else [])
    elif ln == 'wms':
        a = next((x for x in ANIMALS if x[0] in t.lower()), ('', '#animals', '#animalattack'))
        tags = ['#wouldyousurvive', a[2], '#meatballmyths'] + (['#shorts'] if kind == 'short' else [])
    elif ln == 'pets':
        tags = ['#dogs' if 'dog' in t.lower() else '#cats', '#petfacts', '#meatballmyths'] + (['#shorts'] if kind == 'short' else [])
    elif ln == 'news': tags = ['#news', '#explained', '#meatballmyths']
    elif ln == 'mystery': tags = ['#declassified', '#history', '#meatballmyths']
    else: tags = ['#animalfacts', '#animals', '#meatballmyths'] + (['#shorts'] if kind == 'short' else [])
    out = []
    for x in tags:
        if x not in out: out.append(x)
    return out[:5]
def clean_desc(d, kind, ln, t, vid):
    keep = []
    for line in d.split('\n'):
        if is_kwlist(line): continue
        if re.fullmatch(r'\s*(#\w+\s*)+', line or 'x'): continue
        line = re.sub(r'(?<!\S)#[A-Za-z]\w*', '', line).rstrip()
        keep.append(line)
    txt = re.sub(r'\n{3,}', '\n\n', '\n'.join(keep)).strip()
    extra = []
    if kind == 'short' and ln == 'bugs':
        ft, fid = FULL['spider'] if creature(t) in ('#daddylonglegs', '#cellarspider', '#spiders', '#jumpingspider', '#wolfspider', '#falsewidow', '#blackwidow', '#brownrecluse') else FULL['bugs']
        if fid != vid: extra.append(f'Full video: {ft} https://youtu.be/{fid}')
        extra.append('Series: Things Living In Your House')
    return (txt + ('\n\n' + '\n'.join(extra) if extra else '') + '\n\n' + ' '.join(hashtags(kind, ln, t))).strip()
PESTS = {'#cockroach', '#bedbugs', '#mice', '#termites', '#carpetbeetle', '#fleas', '#clothesmoth', '#stinkbugs', '#ticks', '#dustmites', '#mites', '#flies', '#ants'}
def pinned(kind, ln, t, d=''):
    src = ' Sources are in the description.' if 'source' in d.lower() else ''
    p = _pinned(kind, ln, t)
    return p.replace(' Sources are in the description.', src).replace(' (Sources in the description.)', src)
def _pinned(kind, ln, t):
    c = creature(t); name = {'#housecentipede': 'house centipede', '#daddylonglegs': 'daddy longlegs', '#cockroach': 'roach', '#dustmites': 'dust mites',
        '#cellarspider': 'cellar spider', '#mites': 'mites', '#bedbugs': 'bed bugs', '#ants': 'ants', '#fleas': 'fleas', '#stinkbugs': 'stink bugs', '#clothesmoth': 'clothes moth', '#carpetbeetle': 'carpet beetle', '#flies': 'flies', '#ticks': 'ticks', '#silverfish': 'silverfish', '#camelcricket': 'camel cricket', '#termites': 'termites', '#mice': 'mouse'}.get(c)
    if ln == 'bugs':
        if 'true or false' in t.lower() or 'venomous' in t.lower(): return 'TRUE or FALSE: did you guess right before the answer? 👇 Sources are in the description.'
        if c in PESTS: return f'Seen {"a " + name if name and not name.endswith("s") else (name or "one")} at home this week? Be honest 👇 Sources are in the description.'
        return (f'Found a {name} at home? Squish it or let it live? 👇 Sources are in the description.' if name else
                'Which one lives in YOUR house? Squish it or let it live? 👇 Sources are in the description.')
    if ln == 'wms':
        if 'grizzly' in t.lower() or 'bear' in t.lower(): return 'Run, play dead, or fight? Pick one before Meatball does 👇 (Sources in the description.)'
        return 'Would YOU survive this one? Yes or no 👇 (Sources in the description.)'
    if ln == 'pets': return 'Does yours do this? Tell me your pet\'s name 👇 Sources are in the description.'
    if ln == 'news': return '(Decision: no pin; see the action column.)'
    if ln == 'mystery': return 'PROVEN, BUSTED or UNSOLVED? Your verdict 👇 Sources are in the description.'
    return 'Which one did you believe? 👇 Sources are in the description.'

LF = {  # hand-written long-form packaging (titles keep only claims already in each video)
 'cH3HCZ8GlHk': ('3 Bugs in Your House You Should Never Kill (And 4 You Must)', 'KEEP: best CTR on the channel (5.44%). New thumbnail only; Test & Compare it against the live one if offered.'),
 'KWOM2-mNmww': ("Don't Kill the Spider in Your Corner. It Eats Bigger Spiders", 'KEEP title (4.63%). New thumbnail drops the repeated words from the title idea (adds the face + threat). Optional title test: "Your Life as the Skinny Spider in Your Ceiling Corner" (POV formula; check it matches the video).'),
 'xeAsg5ECpgw': ('3 More Bugs in Your House You Should Never Kill (And 5 You Must)', 'KEEP title (4.37%). New thumbnail (NOT THE MOTH = the cold-open claim).'),
 'Lid8JXhg1Q4': ('6 Creatures Living in Your House Right Now (You Never See Them)', 'Only 33 impressions: packaging is not the bottleneck yet. New thumbnail + keep title (case fix). Feature it in the Things Living In Your House shelf.'),
 'bqij8Ht6SX4': ('Every Bug in Your House, Ranked From Harmless to Nightmare', '1.31% CTR on 305 impressions. New thumbnail (WHO\'S #1? hides the top spot like the video does); drop the emoji.'),
 'viD-nbPdaxk': ('Your Life as a House Cat: 8 Ways It Goes Wrong', 'Off-lane (pets paused). Keep public for watch hours; remove its keyword-list line; no new art.'),
 'Uqj0QL8G0d4': ('How Wolves Became Dogs (The Funny History of Man\'s Best Friend)', 'Off-lane. Keep public (watch hours count toward YPP); no new art.'),
 'z-Kg8sXCxlU': ("Weird Animal Facts You Didn't Know (3 Are Fake. Can You Spot Them?)", 'Off-lane but most impressions (5,262 at 1.82%). Keep public; no new art in batch 1.'),
 'o9Emu9oMgCs': ('Animals Thought Extinct Found Alive (One Was Hiding on a Rock for 80 Years)', 'Off-lane. Keep public; no change.'),
 'RwbgzQisvYM': ("12 Animal Myths You've Believed Your Whole Life (Disney Faked One)", 'Off-lane. Keep public; no change.'),
 'gFhrONKK0rI': ('Everything You Know About Animals Is WRONG', 'Off-lane. Keep public; no change.'),
 '2EC5LDtbUbo': ('The CIA Tried to Turn a Cat Into a Spy', 'Off-lane (CIA paused). Keep public for watch hours; drop it from the channel home page; drop the emoji.'),
 '4-gvZTWf2wg': ('The CIA Tried to Steal a Soviet Sub With a Giant Claw', 'Off-lane (CIA paused). Keep public; drop it from the channel home page; drop the emoji.'),
}
out = []
for r in rows:
    if r['id'] not in pub: continue
    kind = 'long' if r['id'] in LF else 'short'
    ln = lane(r['title'], r['desc'])
    if kind == 'long':
        new, note = LF[r['id']]
        if r['id'] in ('cH3HCZ8GlHk', 'KWOM2-mNmww', 'xeAsg5ECpgw', 'Lid8JXhg1Q4', 'bqij8Ht6SX4'): ln = 'bugs'
    else:
        new = clean_title(r['title']); note = ''
        if ln == 'news': note = 'DECISION: dated news (as of Nov 13). Suggest Unlist (reversible) once it is no longer current, or add a dated correction line. Do not delete.'
        elif ln in ('mystery', 'pets', 'animal-facts'): note = 'Off-lane: keep public (views count), no new art; title/hashtag clean only.'
    desc = r['desc']; kw = any(is_kwlist(l) for l in desc.split('\n'))
    hs_now = re.findall(r'(?<!\S)#\w+', desc + ' ' + r['title'])
    issues = []
    if kw: issues.append('keyword-list line (YouTube: ordinary descriptive tags in the description are prohibited)')
    if len(hs_now) > 5: issues.append(f'{len(hs_now)} hashtags')
    if kind == 'long' and not hs_now: issues.append('no hashtags')
    if re.search(r'#\d', r['title']): issues.append('"#N" series number in title')
    if SERIES.search(r['title']): issues.append('series tag eats title space')
    imp = int(r['impr'] or 0); ctr = float(r['ctr'] or 0)
    # impact score (estimate): long-forms weigh impressions in the bug lane; Shorts weigh views (search + channel page)
    score = (imp/100*(2 if ln == 'bugs' else 0.6) + (30 if r['id'] in thumbs else 0) + (25 if kw else 0)) if kind == 'long' else (r['views']/150 + (12 if r['id'] in thumbs else 0) + (8 if ln == 'news' else 0))
    out.append(dict(video_id=r['id'], url=f"https://youtu.be/{r['id']}", type='Long-form' if kind == 'long' else 'Short', lane=ln, published=r['published'], views=r['views'],
        impressions=r['impr'], ctr_pct=r['ctr'], avd=r['avd'], current_title=r['title'], proposed_title=new, proposed_title_chars=len(new), title_changed='yes' if new != r['title'] else 'no',
        new_thumbnail=thumbs.get(r['id'], ''), issues='; '.join(issues), cleaned_description=clean_desc(desc, kind, ln, r['title'], r['id']),
        hashtags=' '.join(hashtags(kind, ln, r['title'])), pinned_comment=pinned(kind, ln, r['title'], r['desc']), notes=note, score=round(score, 1)))
CHANNEL = [
 dict(type='Channel', video_id='', current_title='About text: "Meatball investigates the weird: conspiracy theories, strange history, viral claims and very suspicious animals ... (Formerly Meatball Myths.)"',
      proposed_title='ABOUT (replace): see fix1_channel_text.md', issues='About describes the paused CIA/conspiracy format, an old schedule (Tue/Sat, Verdict Wednesday, Viewer Case Friday) and says "Formerly Meatball Myths" while the channel is Meatball Myths', score=95),
 dict(type='Channel', video_id='', current_title='Channel keywords: meatball investigates, conspiracy theories, cold war secrets, unsolved mysteries, bermuda triangle ...',
      proposed_title='KEYWORDS (replace): meatball myths, bugs in your house, house spiders, house centipede, would you survive, bear attack, animal facts, is this spider venomous, things living in your house, cartoon animal facts', issues='Keywords point at the paused lane', score=60),
 dict(type='Channel', video_id='', current_title='Banner: old stick-figure style, "Weird animal facts, drawn. New every day."', proposed_title='fix1_channel_banner_2560x1440.jpg (C v3 style, text inside the 1546x423 safe area)', issues='Old art style; promise does not match the lane', score=55),
 dict(type='Channel', video_id='', current_title='Channel trailer (non-subscribers): not checked (Studio only)', proposed_title='Trailer = 3 Bugs in Your House You Should Never Kill (cH3HCZ8GlHk): best CTR 5.44% and the longest AVD (1:57)', issues='99.3% of viewers are new: the trailer is what they see', score=70),
 dict(type='Channel', video_id='', current_title='Featured video (returning subscribers): not checked', proposed_title="Featured = the newest bug long-form (now: Don't Kill the Spider in Your Corner, KWOM2-mNmww)", issues='', score=40),
 dict(type='Channel', video_id='', current_title='Playlists: Meatball Deep Dives (animal myths, history & declassified) listed first', proposed_title='Home sections in this order: 1 Bugs in Your House: Kill It or Keep It? (Full Episodes) 2 Things Living In Your House (Shorts) 3 Is This Spider Venomous? 4 Would Meatball Survive? 5 Deep Dives last', issues='Home page leads with the paused lane', score=50),
]
for c in CHANNEL:
    for k in ['url', 'lane', 'published', 'views', 'impressions', 'ctr_pct', 'avd', 'proposed_title_chars', 'title_changed', 'new_thumbnail', 'cleaned_description', 'hashtags', 'pinned_comment', 'notes']: c.setdefault(k, '')
    if 'banner' in c['current_title'].lower(): c['new_thumbnail'] = 'fix1_channel_banner_2560x1440.jpg'
allrows = sorted(CHANNEL + out, key=lambda x: -x['score'])
for i, r in enumerate(allrows, 1): r['rank'] = i
cols = ['rank', 'type', 'video_id', 'url', 'lane', 'published', 'views', 'impressions', 'ctr_pct', 'avd', 'current_title', 'proposed_title', 'proposed_title_chars', 'title_changed',
        'new_thumbnail', 'issues', 'cleaned_description', 'hashtags', 'pinned_comment', 'notes', 'score']
with open(f'{OUT}/fix1_changes.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); [w.writerow({k: r.get(k, '') for k in cols}) for r in allrows]
json.dump(allrows, open(f'{OUT}/fix1_changes.json', 'w'), indent=1, ensure_ascii=False)
from collections import Counter
print(len(allrows), Counter(r['type'] for r in allrows), Counter(r['lane'] for r in out), sum(r['title_changed'] == 'yes' for r in out))
for r in allrows[:16]: print(r['rank'], r['type'], r['video_id'], r['score'], (r['proposed_title'] or '')[:70])
