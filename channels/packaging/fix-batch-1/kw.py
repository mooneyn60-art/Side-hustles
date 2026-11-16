import re, statistics as st
def is_kwlist(line):
    fr = [f.strip() for f in line.strip().rstrip('.').split(',') if f.strip()]
    if len(fr) < 6 or re.search(r'\d:\d\d', line) or line.lstrip().startswith(('Sources', 'Photos', 'Source')): return False
    wl = [len(f.split()) for f in fr]
    return st.median(wl) <= 5 and max(wl) <= 9 and sum(1 for f in fr if f[:1].islower()) >= len(fr)*0.4
