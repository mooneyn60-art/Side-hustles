for q in "house bugs you should never kill" "house centipede" "bed bugs" "is this spider venomous" "black widow spider" "would you survive" "can you survive" "your life as a" "what if you were born as an animal" "spider in my house" "weird animal facts" "brown recluse" "cellar spider daddy long legs" "bugs living in your house"; do
  yt-dlp --skip-download --no-warnings --ignore-errors --dateafter 20260818 --match-filter "duration>180" -j "ytsearch25:$q" 2>/dev/null | python3 -c "
import sys,json
for l in sys.stdin:
  try: d=json.loads(l)
  except: continue
  print(json.dumps({k:d.get(k) for k in ['id','title','channel','channel_follower_count','view_count','upload_date','duration','webpage_url','thumbnail']}|{'q':'$q'}))
" >> raw.jsonl
done
echo DONE
