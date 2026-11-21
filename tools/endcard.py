"""Find start of TikTok end card (dark #161823-ish screen held to the end). Usage: endcard.py video.mp4"""
import sys, subprocess, numpy as np
f = sys.argv[1]
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-vf', 'fps=10,scale=64:64', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                     capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, 64, 64, 3).astype(int)
ref = np.array([14, 16, 27])
near = (np.abs(fr - ref).sum(-1) < 36).mean((1, 2))   # share of pixels near end-card colour
dark = (fr.sum(-1) < 40).mean((1, 2))
card = (near > 0.8)
i = len(card)
while i > 0 and card[i - 1]: i -= 1
print(round(i / 10, 2))
