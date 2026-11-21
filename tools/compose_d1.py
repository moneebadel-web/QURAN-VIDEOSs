"""Overlay Design-1 subtitle PNGs on background, add original audio.
Usage: compose_d1.py bg.mp4 raw.mp4 groups.json ends.json subsdir END out.mp4
ends.json = list of [fade_out_start, fade_out_dur] per group."""
import json, subprocess, sys
from PIL import Image
bg, raw, gf, ef, sd, END, out = sys.argv[1:8]; END = float(END)
G = json.load(open(gf)); E = json.load(open(ef))
Y0, H = 900, 620  # crop band containing the subtitle block
ins, chains, labels = [], [], []
k = 2
for gi, g in enumerate(G):
    fo, fod = E[gi]
    items = [(f"{sd}/g{gi}_w{j}.png", max(0, t - 0.06), 0.55) for j, t in enumerate(g["t"])]
    items.append((f"{sd}/g{gi}_de.png", g["t"][0] + 0.35, 0.5))
    for p, st, d in items:
        im = Image.open(p); assert im.getbbox()[1] >= Y0 and im.getbbox()[3] <= Y0 + H, (p, im.getbbox())
        ins += ["-loop", "1", "-t", str(END), "-i", p]
        chains.append(f"[{k}:v]crop=1080:{H}:0:{Y0},format=rgba,fade=t=in:st={st:.3f}:d={d}:alpha=1,"
                      f"fade=t=out:st={fo:.3f}:d={fod}:alpha=1[o{k}]")
        labels.append(f"o{k}"); k += 1
fc = chains[:]; cur = "0:v"
for i, l in enumerate(labels):
    nxt = f"v{i}"; fc.append(f"[{cur}][{l}]overlay=0:{Y0}:format=auto[{nxt}]"); cur = nxt
fc.append(f"[{cur}]format=yuv420p[vout]")
fc.append(f"[1:a]atrim=0:{END},afade=t=out:st={END - 0.4}:d=0.4[aout]")
cmd = ["ffmpeg", "-v", "error", "-y", "-i", bg, "-i", raw] + ins + [
    "-filter_complex", ";".join(fc), "-map", "[vout]", "-map", "[aout]", "-t", str(END),
    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-maxrate", "11M", "-bufsize", "22M", "-r", "30",
    "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", out]
subprocess.run(cmd, check=True); print("ok")
