"""words.py sura v1 w1 v2 w2 out.json [basmala]
Word list from v1 (starting at word index w1) to v2 (word index w2 inclusive, -1 = end)."""
import sys, json
Q = json.load(open('/home/claude/dl/qj/package/dist/quran.json', encoding='utf8'))
s, v1, w1, v2, w2, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
bas = len(sys.argv) > 7 and sys.argv[7] == 'basmala'
W = []
if bas:
    for i, x in enumerate(Q[0]['verses'][0]['text'].split()):
        W.append({'w': x, 'v': 0, 'i': i})
for v in Q[s-1]['verses'][v1-1:v2]:
    ws = [x.replace('۞', '') for x in v['text'].split()]
    ws = [x for x in ws if x]
    lo = w1 if v['id'] == v1 else 0
    hi = (w2 if w2 >= 0 else len(ws) - 1) if v['id'] == v2 else len(ws) - 1
    for i in range(lo, hi + 1):
        W.append({'w': ws[i], 'v': v['id'], 'i': i, 'n': len(ws)})
json.dump(W, open(out, 'w', encoding='utf8'), ensure_ascii=False)
json.dump([x['w'] for x in W], open(out.replace('.json', '_plain.json'), 'w', encoding='utf8'), ensure_ascii=False)
