"""CTC Viterbi forced alignment of Uthmani words.
Usage: align.py lp.npz words.json out.json   (words.json = list of Uthmani words)"""
import sys, json, unicodedata, numpy as np
M = "/home/claude/dl/asr/sherpa-onnx-omnilingual-asr-1600-languages-300M-ctc-int8-2025-11-12/"
toks = [l.rstrip('\n').rsplit(' ', 1)[0] for l in open(M + "tokens.txt", encoding='utf8')]
tid = {t: i for i, t in enumerate(toks)}
lp = np.load(sys.argv[1])['lp']; words = json.load(open(sys.argv[2], encoding='utf8'))

def norm(w):
    w = w.replace('ٰ', 'ا').replace('ٱ', 'ا').replace('ۥ', '').replace('ۦ', '')
    w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    return ''.join(c for c in w if c in tid)

seq, owner = [], []
for k, w in enumerate(words):
    if k: seq.append(tid[' ']); owner.append(-1)
    for c in norm(w): seq.append(tid[c]); owner.append(k)
T, L = len(lp), len(seq)
S = 2 * L + 1; ext = [0] * S
for i, s in enumerate(seq): ext[2 * i + 1] = s
NEG = -1e30
dp = np.full((T, S), NEG); bp = np.zeros((T, S), np.int32)
dp[0, 0] = lp[0, 0]; dp[0, 1] = lp[0, ext[1]]
for t in range(1, T):
    p = dp[t - 1]
    for s in range(S):
        best, arg = p[s], s
        if s >= 1 and p[s - 1] > best: best, arg = p[s - 1], s - 1
        if s >= 2 and ext[s] != 0 and ext[s] != ext[s - 2] and p[s - 2] > best: best, arg = p[s - 2], s - 2
        dp[t, s] = best + lp[t, ext[s]]; bp[t, s] = arg
s = S - 1 if dp[-1, S - 1] > dp[-1, S - 2] else S - 2
path = [0] * T
for t in range(T - 1, -1, -1):
    path[t] = s; s = bp[t, s]
st, en = {}, {}
for t, s in enumerate(path):
    if s % 2 == 1:
        k = owner[(s - 1) // 2]
        if k >= 0:
            st.setdefault(k, t); en[k] = t
res = [{"w": w, "start": round(st[k] * 0.02, 3), "end": round((en[k] + 1) * 0.02, 3)} for k, w in enumerate(words)]
json.dump(res, open(sys.argv[3], 'w', encoding='utf8'), ensure_ascii=False, indent=1)
for r in res: print(r['start'], r['end'], r['w'])
