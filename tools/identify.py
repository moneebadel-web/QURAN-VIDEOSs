"""Find sura/ayat range for a greedy transcript. Usage: identify.py greedy.txt"""
import sys, json, unicodedata, re
from rapidfuzz import fuzz
Q = json.load(open('/home/claude/dl/qj/package/dist/quran.json', encoding='utf8'))

def norm(w):
    w = w.replace('ٰ', 'ا').replace('ٱ', 'ا').replace('ۥ', '').replace('ۦ', '')
    w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    w = re.sub('[أإآٱ]', 'ا', w).replace('ى', 'ي').replace('ة', 'ه').replace('ؤ', 'و').replace('ئ', 'ي')
    w = re.sub('[^ء-ي ]', '', w)
    return re.sub(' +', ' ', w).strip()

def run(txt):
    t = norm(txt); t = t.replace('بسم الله الرحمن الرحيم', '').replace('باسم الله الرحمن الرحيم', '').strip()
    best = None
    for s in Q:
        vs = s['verses']; text = ''; starts = []
        for v in vs:
            starts.append(len(text)); text += norm(v['text']) + ' '
        al = fuzz.partial_ratio_alignment(t, text, score_cutoff=50)
        if al and (best is None or al.score > best[0]):
            a = max(i for i, x in enumerate(starts) if x <= al.dest_start)
            b = max(i for i, x in enumerate(starts) if x <= max(al.dest_end - 3, al.dest_start))
            best = (al.score, s['id'], s.get('transliteration'), vs[a]['id'], vs[b]['id'], text, starts)
    sc, sid, name, a, b, text, starts = best
    def loc(piece, tail):
        al = fuzz.partial_ratio_alignment(piece, text)
        pos = al.dest_end - 2 if tail else al.dest_start
        return [i for i, x in enumerate(starts) if x <= pos][-1] + 1, round(al.score)
    ws = t.split()
    h = loc(' '.join(ws[:4]), False); e = loc(' '.join(ws[-4:]), True)
    return (round(sc), sid, name, a, b, 'head', h, 'tail', e)
print(run(open(sys.argv[1], encoding='utf8').read()))
