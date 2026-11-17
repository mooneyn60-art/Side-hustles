import asyncio, json, sys
sys.path.insert(0,'/home/user/skills/skills/oh-meatball/tools')
from facts import speak
L=["Giant house spider in your tub? Probably stuck.",
"It is not an extremely active climber.",
"Meatball takes full credit for the trapping.",
"His dog, Noodle, is already halfway down the hall.",
"In the Pacific Northwest, the giant house spider is usually trapped in sinks or bathtubs where it has ventured in search of water.",
"What's the biggest spider you've found in your tub? And"]
async def go():
    out=[]
    for i,t in enumerate(L):
        w=await speak(t,"en-US-AndrewMultilingualNeural",f"l{i}.mp3","+15%","+3Hz")
        out.append({"text":t,"words":[[s,e-s,x] for s,e,x in w]})
    json.dump(out,open("words.json","w"),indent=1)
asyncio.run(go())
