for q in "house centipede" "bugs in your house you should never kill" "bed bugs" "is this spider venomous" "black widow spider" "would you survive" "can you survive animal" "your life as a" "what if you were born as an animal" "spider in my house" "brown recluse" "daddy long legs" "weird animal facts" "spider in bathtub"; do
  u="https://www.youtube.com/results?search_query=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote_plus(sys.argv[1]))" "$q")&sp=EgIIBQ%253D%253D"
  yt-dlp --flat-playlist -J "$u" 2>/dev/null | python3 -c "
import sys,json
d=json.load(sys.stdin)
for e in d.get('entries',[]):
  if (e.get('duration') or 0)>180: print(json.dumps({k:e.get(k) for k in ['id','title','channel','channel_id','view_count','duration']}|{'q':sys.argv[1]}))
" "$q" >> flat.jsonl
  echo "done $q $(wc -l < flat.jsonl)"
done
echo ALLDONE
