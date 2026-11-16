import asyncio, json, sys, edge_tts
async def main(text, out, rate="+10%", pitch="+3Hz", voice="en-US-AndrewMultilingualNeural"):
    c = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch, boundary="WordBoundary")
    words=[]
    with open(out+".mp3","wb") as f:
        async for ch in c.stream():
            if ch["type"]=="audio": f.write(ch["data"])
            elif ch["type"]=="WordBoundary":
                words.append({"w":ch["text"],"t":ch["offset"]/1e7,"d":ch["duration"]/1e7})
    json.dump(words,open(out+".words.json","w"),indent=0)
import time
for i in range(5):
    try:
        asyncio.run(main(sys.argv[1], sys.argv[2], *(sys.argv[3:5]))); break
    except Exception as e:
        print("retry",i,e); time.sleep(2)
else: sys.exit(1)
