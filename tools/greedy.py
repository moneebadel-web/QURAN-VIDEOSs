import sys, numpy as np
M = "/home/claude/dl/asr/sherpa-onnx-omnilingual-asr-1600-languages-300M-ctc-int8-2025-11-12/"
toks = [l.rstrip('\n').rsplit(' ', 1)[0] for l in open(M + "tokens.txt", encoding='utf8')]
lp = np.load(sys.argv[1])['lp']; g = lp.argmax(1); out = []; prev = -1
for i in g:
    if i != prev and i != 0: out.append(toks[i])
    prev = i
print(''.join(out))
