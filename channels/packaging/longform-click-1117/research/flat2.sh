for q in "would you survive" "your life as a" "what if you were born as an animal"; do
  u="https://www.youtube.com/results?search_query=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote_plus(sys.argv[1]))" "$q")&sp=EgIIBQ%253D%253D"
  yt-dlp --flat-playlist -J "$u" 2>/dev/null | python3 -c "
import sys,json
d=json.load(sys.stdin)
for e in d.get('entries',[]):
  if (e.get('duration') or 0)>180: print(json.dumps({k:e.get(k) for k in ['id','title','channel','channel_id','view_count','duration']}|{'q':sys.argv[1]}))
" "$q" >> flat.jsonl
  echo "done $q"
done
echo ALLDONE
