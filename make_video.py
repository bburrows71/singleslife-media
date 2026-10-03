#!/usr/bin/env python3
"""Turn a post's rendered slides into a 9:16 MP4 for TikTok / YouTube Shorts / Reels.

Usage: python3 make_video.py posts/X [seconds_per_slide]
Writes posts/X/<slug>-video.mp4 (1080x1920, H.264, 30fps, silent AAC track). Each 1080x1350 slide is
centered on the brand's pine background with a short crossfade between slides.
"""
import sys, subprocess, pathlib
d = pathlib.Path(sys.argv[1]); per = float(sys.argv[2]) if len(sys.argv) > 2 else 4.0
slides = sorted(p for p in d.glob("*.jpg"))
if not slides: sys.exit("no slides in " + str(d))
slug = slides[0].name.rsplit("-", 1)[0]
out = d / f"{slug}-video.mp4"
fade = 0.5 if len(slides) > 1 else 0
args = ["ffmpeg", "-y", "-loglevel", "error"]
for s in slides: args += ["-loop", "1", "-t", str(per + fade), "-i", str(s)]
total = per * len(slides) + fade
args += ["-f", "lavfi", "-t", str(total), "-i", "anullsrc=r=44100:cl=stereo"]
f = []
for i in range(len(slides)):
    f.append(f"[{i}:v]scale=1080:1350,pad=1080:1920:0:285:color=0x1F3B37,setsar=1,fps=30,format=yuv420p[v{i}]")
last = "v0"
for i in range(1, len(slides)):
    f.append(f"[{last}][v{i}]xfade=transition=fade:duration={fade}:offset={per*i}[x{i}]")
    last = f"x{i}"
args += ["-filter_complex", ";".join(f), "-map", f"[{last}]", "-map", f"{len(slides)}:a",
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30", "-c:a", "aac", "-shortest", "-movflags", "+faststart", str(out)]
subprocess.run(args, check=True)
print(out)
