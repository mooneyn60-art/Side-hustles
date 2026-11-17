while IFS= read -r q; do
  yt-dlp --no-warnings --skip-download -j "ytsearch1:$q" 2>/dev/null | python3 -c "
import sys,json
for l in sys.stdin:
  d=json.loads(l); print(json.dumps({k:d.get(k) for k in ['id','title','channel','channel_follower_count','view_count','upload_date','duration','webpage_url']}|{'q':sys.argv[1]}))
" "$q" >> resolved.jsonl
  echo "done $q"
done < queries.txt
echo ALLDONE
