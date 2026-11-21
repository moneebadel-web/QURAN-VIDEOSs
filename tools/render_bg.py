"""Render background segments from shots.json and concat. Usage: render_bg.py shots.json clipdir out.mp4"""
import json, subprocess, sys, os
shots, cdir, out = json.load(open(sys.argv[1])), sys.argv[2], sys.argv[3]
GRADE = "eq=contrast=1.08:saturation=1.05,colorbalance=rh=0.03:gh=0.01:bh=-0.03:rs=-0.01:bs=0.01,vignette=PI/5"
os.makedirs("seg", exist_ok=True); lst = []
for i, s in enumerate(shots):
    d = round(s["b"] - s["a"], 3); f = f"seg/s{i:02d}.mp4"
    if s["clip"] is None:
        cmd = ["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c=black:s=1080x1920:r=30:d={d}"]
        vf = "format=yuv420p"
    else:
        src = d / 1.25 + 0.2
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(s["ss"]), "-t", str(src), "-i", f"{cdir}/{s['clip']}.mp4"]
        vf = f"setpts=1.25*PTS,fps=30,crop=1214:2160:{s['x']}:0,scale=1080:1920:flags=lanczos,{GRADE},trim=duration={d}"
        if s["fi"]: vf += f",fade=t=in:st=0:d={s['fi']}"
        if s["fo"]: vf += f",fade=t=out:st={d - s['fo']}:d={s['fo']}"
        vf += ",format=yuv420p"
    subprocess.run(cmd + ["-vf", vf, "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "14", "-r", "30", f], check=True)
    lst.append(f"file '{os.path.abspath(f)}'")
open("seg/list.txt", "w").write("\n".join(lst) + "\n")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", "seg/list.txt", "-c", "copy", out], check=True)
print("ok")
