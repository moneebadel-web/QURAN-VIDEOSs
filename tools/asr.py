"""CTC logits over windowed audio. Usage: asr.py audio16k.raw out.npz"""
import sys, numpy as np, onnxruntime as ort
M = "/home/claude/dl/asr/sherpa-onnx-omnilingual-asr-1600-languages-300M-ctc-int8-2025-11-12/"
raw, out = sys.argv[1], sys.argv[2]
a = np.frombuffer(open(raw, 'rb').read(), dtype=np.int16).astype(np.float32) / 32768
sr = 16000; W, S = 20 * sr, 16 * sr
sess = ort.InferenceSession(M + "model.int8.onnx")
toks = [l.rstrip('\n').rsplit(' ', 1)[0] for l in open(M + "tokens.txt", encoding='utf8')]
nfr = int(np.ceil(len(a) / 320))
acc = None; cnt = np.zeros(nfr)
starts = list(range(0, max(1, len(a) - W + S), S)) or [0]
for st in starts:
    seg = a[st:st + W]
    seg = (seg - seg.mean()) / (seg.std() + 1e-7)
    lg = sess.run(None, {'x': seg[None].astype(np.float32)})[0][0]
    lp = lg - np.logaddexp.reduce(lg, axis=1, keepdims=True)
    f0 = st // 320
    n = min(len(lp), nfr - f0)
    if acc is None: acc = np.zeros((nfr, lp.shape[1]), np.float32)
    # triangular weight to favour window centres
    w = np.minimum(np.arange(n) + 1, n - np.arange(n)).astype(np.float32)
    if st == 0: w[:n // 2] = n
    if st == starts[-1]: w[n // 2:] = n
    acc[f0:f0 + n] += lp[:n] * w[:, None]; cnt[f0:f0 + n] += w
    if st + W >= len(a): break
lp = acc / np.maximum(cnt, 1e-6)[:, None]
lp = lp - np.logaddexp.reduce(lp, axis=1, keepdims=True)
g = lp.argmax(1); txt = []; prev = -1
for i in g:
    if i != prev and i != 0: txt.append(toks[i])
    prev = i
print(''.join(txt).replace('▁', ' '))
np.savez(out, lp=lp)
