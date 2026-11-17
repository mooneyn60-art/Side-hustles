# Style test v2 (Claude, night of 11/16 to 11/17)

**Output:** channels/renders/style-test-v2-1117.mp4, 19.6 s, 1080x1920, 30 fps. This is a test for Moondog88 and is not to be posted.
**Script:** channels/scripts/ep5-s1-funny-v2.md @ 4598369. Every VO line is word for word, and no facts were changed.
**Pipeline:** your channels/renders/st/ (render.py's helpers, audio.py, master.py) with new shots for the v2 beat table, in render2.py and master2.py here. The /workspace paths now point to the repo. The Luckiest Guy font comes from @fontsource/luckiest-guy, because the machine doesn't have the TTF.

## Your three fixes
1. **Voice:** en-US-AndrewMultilingualNeural at +15% and +3 Hz (your 11:05 PM answer). The fact payoff ("It is not an extremely active climber.") starts at 2.63 s and ends by about 4.3 s.
2. **Captions off the bodies:** captions sit at y 420, just under the WSU card, and every character is placed below them. Checked on a contact sheet of every shot.
3. **Spider skitter:** a stepped scuttle (quick small hops, alternating tilt and flip) on the close-ups, the wide shot and the wall climb, using the existing cutouts with no new leg art.

## Beats as built (times from the voice timeline)
| Time | Shot |
|---|---|
| 0.00 | Spider close-up |
| 1.40 | Wide tub shot: spider small at the far end; Meatball across the room in a shower cap, shoe raised (shing at 1.50) |
| 2.63 | Spider slides up the wall and back down (slide whistle) |
| 4.57 | Meatball alone; shoe planted on the sink with a flag, smug, then "nailed it" (ta-da) |
| 6.84 | Hallway: Noodle startled, zips out left, bathmat spinning (claw skitter) |
| 9.82 | Spider by a water droplet |
| 11.8 | Sauce in the dry sink, slow half-lid blink (bloop) |
| 14.7 | Noodle peeks round the doorframe and snaps back |
| 15.7 | Back to the spider |
| 17.0 | Meatball with the shoe raised |
| 17.95 | Sauce nudges the shoe off the sink rim into the dry basin (thunk) |
| 19.2 | Hard cut back to the frame-1 spider close-up for the loop |

## Sound
The comedy kit has no shing, slide whistle, ta-da, claw or bloop sound, so these are short synth effects made in master2.py. Swap in real ones if Voice & Sound has them. There are no swears.

## Checks
- Transcript (faster-whisper base.en) matches the script. It dropped the first "It" of line 2, but the word is in the audio.
- Speech is normalized to -14 LUFS, true peak -1.6.
- Different from the script: Sauce "blinks" with her half-lid pose, because the kit has no blink frame.
