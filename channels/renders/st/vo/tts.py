import asyncio, json, edge_tts
L=["Giant house spider in your tub? Probably stuck.",
"His dog, Noodle, stares from the bathmat.",
"It is not an extremely active climber.",
"In the Pacific Northwest, the giant house spider is usually trapped in sinks or bathtubs where it has ventured in search of water.",
"What's the biggest spider you've found in your tub? And"]
async def go():
    out=[]
    for i,t in enumerate(L):
        c=edge_tts.Communicate(t,"en-US-AndrewNeural",rate="+10%",boundary="WordBoundary")
        words=[]
        with open(f"l{i}.mp3","wb") as f:
            async for ch in c.stream():
                if ch["type"]=="audio": f.write(ch["data"])
                elif ch["type"]=="WordBoundary":
                    words.append((ch["offset"]/1e7,ch["duration"]/1e7,ch["text"]))
        out.append({"text":t,"words":words})
    json.dump(out,open("words.json","w"),indent=1)
asyncio.run(go())
