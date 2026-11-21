"""Build one Quran TikTok video. Usage: build.py config.json
config: {src, work, fr, sura, design, basmala, verses:{v:{de,clips:[ids]}}, end?}
Needs work/words.json + work/align.json (from words.py / align.py)."""
import json, subprocess, sys, os, re, html
import numpy as np
from PIL import Image

C = json.load(open(sys.argv[1], encoding='utf8'))
W = C['work']; os.makedirs(W + '/seg', exist_ok=True); os.makedirs(W + '/subs', exist_ok=True)
POOL = json.load(open('/home/claude/tools/pool.json'))
CLIPS = '/home/claude/broll/clips'
GRADE = "eq=contrast=1.08:saturation=1.05,colorbalance=rh=0.03:gh=0.01:bh=-0.03:rs=-0.01:bs=0.01,vignette=PI/5"
def sh(cmd): subprocess.run(cmd, check=True)
def dur(f): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout)

words = json.load(open(W + '/words.json', encoding='utf8'))
al = json.load(open(W + '/align.json', encoding='utf8'))
for w, a in zip(words, al): w.update(start=a['start'], end=a['end'])
D = dur(C['src'])

# ---------- audio energy, end point, pauses ----------
a = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', C['src'], '-ac', '1', '-ar', '16000', '-f', 's16le', '-'],
                                 capture_output=True).stdout, np.int16).astype(np.float32) / 32768
n = len(a) // 320; e = 10 * np.log10((a[:n * 320].reshape(n, 320) ** 2).mean(1) + 1e-10)
p90 = np.percentile(e, 90)
def runs(mask, t0, t1, minlen):
    out = []; i = int(t0 / .02); j1 = min(int(t1 / .02), n)
    while i < j1:
        if mask[i]:
            j = i
            while j < j1 and mask[j]: j += 1
            if (j - i) * .02 >= minlen: out.append((i * .02, j * .02))
            i = j
        else: i += 1
    return out
last = words[-1]['end']
if C.get('end'): END = C['end']
else:
    r = runs(e < p90 - 25, max(0, last - 0.6), D, 0.3)
    END = min(D - 0.05, (r[0][0] + 0.4) if r else D - 0.05)
    card = float(subprocess.run(['python3', '/home/claude/tools/endcard.py', C['src']], capture_output=True, text=True).stdout)
    END = min(END, card - 0.08)
END = round(END, 2)
words = [w for w in words if w['start'] < END - 0.25]
for w in words: w['end'] = min(w['end'], END)
pauses = []
for k in range(len(words) - 1):
    g0, g1 = words[k]['end'] - 0.1, words[k + 1]['start'] + 0.05
    if g1 - g0 < 0.4: continue
    r = runs(e < p90 - 20, g0, g1, 0.26)
    if r:
        ps, pe = r[0][0], r[-1][1]
        if pe - ps >= 0.6: pauses.append((k, round(ps, 2), round(pe, 2)))
pk = {p[0]: p for p in pauses}

# ---------- shots ----------
segs = []; use = {}
def pick(v):
    lst = C['verses'][str(v)]['clips']
    k = use.get(v, 0); use[v] = k + 1
    cid = lst[k % len(lst)]; rep = k // len(lst)
    return cid, rep
satz = []; cur = [0]
for k in range(1, len(words)):
    if (k - 1) in pk: satz.append(cur); cur = [k]
    else: cur.append(k)
satz.append(cur)
t_img = 0.0
for si, s in enumerate(satz):
    start = t_img
    stop = (pk[s[-1]][1] + 0.25) if s[-1] in pk else END
    cuts = [start]; nw = 0
    for k in s[1:]:
        nw += 1; t = words[k]['start']
        if (t - cuts[-1] >= 1.3 and nw >= 2) or t - cuts[-1] >= 2.6:
            if stop - t >= 0.6: cuts.append(t); nw = 0
    # split overly long shots
    out = []
    for i, c in enumerate(cuts):
        nxt = cuts[i + 1] if i + 1 < len(cuts) else stop
        out.append(c)
        while nxt - out[-1] > 6.0: out.append(out[-1] + 5.0) if nxt - out[-1] - 5.0 >= 1.3 else out.append((out[-1] + nxt) / 2)
    cuts = out
    for i, c in enumerate(cuts):
        b = cuts[i + 1] if i + 1 < len(cuts) else stop
        wk = [k for k in s if words[k]['start'] >= c - 0.01] or [s[-1]]
        v = words[wk[0]]['v'] if words[wk[0]]['v'] else words[s[0]]['v']
        if v == 0: v = next(w['v'] for w in words if w['v'])
        cid, rep = pick(v)
        segs.append(dict(a=round(c, 3), b=round(b, 3), clip=cid, rep=rep,
                         fi=0.25 if (i == 0 and si > 0) else 0, fo=0.25 if (i == len(cuts) - 1 and s[-1] in pk) else 0))
    if s[-1] in pk:
        pe = pk[s[-1]][2]
        segs.append(dict(a=round(stop, 3), b=round(pe - 0.25, 3), clip=None))
        t_img = pe - 0.25
segs[-1]['fo'] = 0.4
json.dump(segs, open(W + '/shots.json', 'w'), indent=1)

# ---------- render background ----------
lst = []
for i, s in enumerate(segs):
    d = round(s['b'] - s['a'], 3); f = f"{W}/seg/s{i:03d}.mp4"
    if d <= 0.02: continue
    if s['clip'] is None:
        cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', f'color=c=black:s=1080x1920:r=30:d={d}']; vf = 'format=yuv420p'
    else:
        P = POOL[str(s['clip'])]; cl = dur(f"{CLIPS}/{s['clip']}.mp4"); need = d / 1.25 + 0.2
        ss = P.get('ss', 0.5) + s['rep'] * 4.0
        if ss + need > cl: ss = max(0, cl - need - 0.1)
        cmd = ['ffmpeg', '-v', 'error', '-y', '-ss', f'{ss:.2f}', '-t', f'{need:.2f}', '-i', f"{CLIPS}/{s['clip']}.mp4"]
        vf = f"setpts=1.25*PTS,fps=30,crop=1214:2160:{P.get('x', 1313)}:0,scale=1080:1920:flags=lanczos,{GRADE},tpad=stop_mode=clone:stop_duration=1,trim=duration={d}"
        if s['fi']: vf += f",fade=t=in:st=0:d={s['fi']}"
        if s['fo']: vf += f",fade=t=out:st={max(0, d - s['fo']):.3f}:d={s['fo']}"
        vf += ',format=yuv420p'
    sh(cmd + ['-vf', vf, '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '14', '-r', '30', f])
    lst.append(f"file '{os.path.abspath(f)}'")
open(W + '/seg/list.txt', 'w').write('\n'.join(lst) + '\n')
sh(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', W + '/seg/list.txt',
    '-i', '/home/claude/tools/grad.png', '-filter_complex', '[0][1]overlay,format=yuv420p',
    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '14', '-an', W + '/bg.mp4'])

# ---------- subtitles ----------
def aq(s): return s.replace('ٗ', 'ࣰ').replace('ٞ', 'ࣱ').replace('ٖ', 'ࣲ').replace('۞', '').strip()
def esc(s): return html.escape(s)
WAQF = set('ۖۗۚۛۙۘ')
vend = {}
for k, w in enumerate(words): vend[w['v']] = k
def de(v): return C['verses'][str(v)]['de']
items = []; ovl = []   # ovl: (png, x, y, t_in, fade_in, t_out, fade_out, pop)
if C['design'] == 1:
    css = """#blk{position:absolute;left:70px;right:70px;bottom:520px;text-align:center}
.ar{font-family:AQ;font-size:78px;line-height:1.55;color:#fff;direction:rtl;text-shadow:0 2px 6px rgba(0,0,0,.85),0 0 28px rgba(0,0,0,.55)}
.de{font-family:IN;font-weight:500;font-size:38px;line-height:1.3;color:#f3ead8;margin-top:44px;text-shadow:0 2px 6px rgba(0,0,0,.85),0 0 28px rgba(0,0,0,.55)}
.h{visibility:hidden}"""
    lines = []; cur = []
    for k, w in enumerate(words):
        if cur:
            p = words[cur[-1]]
            brk = (w['v'] != p['v']) or ((k - 1) in pk) or (p['w'][-1] in WAQF) or len(cur) >= 5 or \
                  sum(len(words[j]['w']) for j in cur) > 34
            if brk: lines.append(cur); cur = []
        cur.append(k)
    lines.append(cur)
    for li, L in enumerate(lines):
        nxt = lines[li + 1][0] if li + 1 < len(lines) else None
        t_out = (words[nxt]['start'] - 0.12) if nxt is not None else END - 0.1
        if L[-1] in pk: t_out = min(t_out, pk[L[-1]][1] + 0.25)
        v = words[L[0]]['v']
        for j, k in enumerate(L):
            ar = ' '.join(f'<span class="{"" if q == k else "h"}">{esc(aq(words[q]["w"]))}</span>' for q in L)
            p = f"{W}/subs/l{li}_w{j}.png"
            items.append(dict(path=p, html=f'<div id="blk"><div class="ar">{ar}</div><div class="de h">{esc(de(v))}</div></div>'))
            ovl.append([p, max(0, words[k]['start'] - 0.06), 0.55, t_out - 0.25, 0.25, 0])
    # German per verse
    for v in dict.fromkeys(w['v'] for w in words):
        ks = [k for k, w in enumerate(words) if w['v'] == v]
        t_in = words[ks[0]]['start'] + 0.35
        lastline = [L for L in lines if ks[-1] in L][0]; li = lines.index(lastline)
        nxt = lines[li + 1][0] if li + 1 < len(lines) else None
        t_out = (words[nxt]['start'] - 0.12) if nxt is not None else END - 0.1
        if ks[-1] in pk: t_out = min(t_out, pk[ks[-1]][1] + 0.25)
        p = f"{W}/subs/de_{v}.png"
        items.append(dict(path=p, html=f'<div id="blk"><div class="ar h">ا</div><div class="de">{esc(de(v))}</div></div>'))
        ovl.append([p, t_in, 0.5, t_out - 0.25, 0.25, 0])
else:
    css = """#big{position:absolute;left:0;right:0;top:620px;height:420px;display:flex;align-items:center;justify-content:center}
#big span{font-family:LA;font-size:200px;color:#fff;direction:rtl;white-space:nowrap;text-shadow:0 3px 10px rgba(0,0,0,.8),0 0 40px rgba(0,0,0,.5)}
#de{position:absolute;left:80px;right:80px;top:1130px;text-align:center;font-family:MO;font-weight:300;font-size:36px;line-height:1.35;color:#f3ead8;text-shadow:0 2px 6px rgba(0,0,0,.85),0 0 24px rgba(0,0,0,.6)}
#card{position:absolute;left:70px;right:70px;top:560px;text-align:center}
#card .ar{font-family:LA;font-size:120px;line-height:1.35;color:#fff;direction:rtl;text-shadow:0 3px 10px rgba(0,0,0,.8)}
#card .nm{font-family:MO;font-weight:300;font-size:30px;letter-spacing:4px;color:#d9cdb5;margin-top:26px}
#card .ln{width:180px;height:1px;background:rgba(243,234,216,.7);margin:22px auto}
#card .de{font-family:MO;font-weight:300;font-size:36px;line-height:1.35;color:#f3ead8}"""
    for k, w in enumerate(words):
        nxt = words[k + 1]['start'] - 0.04 if k + 1 < len(words) else END - 0.1
        if k in pk: nxt = min(nxt, pk[k][1] + 0.25)
        p = f"{W}/subs/w{k}.png"
        items.append(dict(path=p, html=f'<div id="big"><span>{esc(w["w"].replace("۞", ""))}</span></div>', fit='#big span'))
        ovl.append([p, max(0, w['start'] - 0.06), 0.18, nxt - 0.15, 0.15, 1])
    vs = list(dict.fromkeys(w['v'] for w in words))
    tail = END - words[-1]['end']
    for v in vs:
        ks = [k for k, w in enumerate(words) if w['v'] == v]
        t_out = words[ks[-1] + 1]['start'] - 0.04 if ks[-1] + 1 < len(words) else END - 0.1
        if ks[-1] in pk: t_out = min(t_out, pk[ks[-1]][1] + 0.25)
        if v == vs[-1] and tail >= 1.6: t_out = words[-1]['end'] + 0.1
        p = f"{W}/subs/de_{v}.png"
        items.append(dict(path=p, html=f'<div id="de">{esc(de(v))}</div>'))
        ovl.append([p, words[ks[0]]['start'] + 0.35, 0.5, t_out - 0.25, 0.25, 0])
    if tail >= 1.6:
        v = vs[-1]; ks = [k for k, w in enumerate(words) if w['v'] == v]
        ar = ' '.join(words[k]['w'].replace('۞', '') for k in ks)
        nm = f"{C['name']} · {C['sura']}:{v}" if v else C['name']
        p = f"{W}/subs/card.png"
        items.append(dict(path=p, html=f'<div id="card"><div class="ar" style="font-size:{120 if len(ks) <= 6 else 84}px">{esc(ar)}</div><div class="nm">{esc(nm)}</div><div class="ln"></div><div class="de">{esc(de(v))}</div></div>'))
        ovl.append([p, words[-1]['end'] + 0.1, 0.5, END - 0.4, 0.4, 0])
json.dump(dict(css=css, items=items), open(W + '/subs/jobs.json', 'w', encoding='utf8'), ensure_ascii=False)
sh(['node', '/home/claude/tools/render_html.js', W + '/subs/jobs.json'])

# ---------- compose ----------
ins, fc = [], []; cur = '0:v'; k = 2
for i, (p, tin, fi, tout, fo, pop) in enumerate(ovl):
    if tout <= tin + 0.1: tout = tin + 0.4
    bb = Image.open(p).getbbox()
    if not bb: continue
    x0, y0, x1, y1 = max(0, bb[0] - 20), max(0, bb[1] - 20), min(1080, bb[2] + 20), min(1920, bb[3] + 20)
    w_, h_ = (x1 - x0) // 2 * 2, (y1 - y0) // 2 * 2
    ins += ['-loop', '1', '-framerate', '30', '-t', f'{END:.2f}', '-i', p]
    ch = f"[{k}:v]crop={w_}:{h_}:{x0}:{y0},format=rgba,fade=t=in:st={tin:.3f}:d={fi}:alpha=1,fade=t=out:st={tout:.3f}:d={fo}:alpha=1"
    if pop:
        ch += f",scale=w='trunc(iw*min(1,0.8+0.2*max(0,(t-{tin:.3f}))/0.25)/2)*2':h=-2:eval=frame"
        fc.append(ch + f"[o{k}]")
        pos = f"x='{x0}+({w_}-w)/2':y='{y0}+({h_}-h)/2'"
    else:
        fc.append(ch + f"[o{k}]"); pos = f"x={x0}:y={y0}"
    fc.append(f"[{cur}][o{k}]overlay={pos}:eval=frame:enable='between(t,{tin - 0.05:.3f},{tout + fo + 0.05:.3f})'[v{k}]")
    cur = f'v{k}'; k += 1
fc.append(f"[{cur}]format=yuv420p[vout]")
fc.append(f"[1:a]atrim=0:{END},afade=t=out:st={END - 0.4:.2f}:d=0.4[aout]")
open(W + '/fc.txt', 'w').write(';'.join(fc))
sh(['ffmpeg', '-v', 'error', '-y', '-i', W + '/bg.mp4', '-i', C['src']] + ins +
   ['-filter_complex_script', W + '/fc.txt', '-map', '[vout]', '-map', '[aout]', '-t', f'{END:.2f}',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-maxrate', '11M', '-bufsize', '22M', '-r', '30',
    '-c:a', 'aac', '-b:a', '256k', '-movflags', '+faststart', W + '/master.mp4'])
# QA sheet at word times
ts = [words[k]['start'] + 0.3 for k in range(0, len(words), max(1, len(words) // 14))][:15]
fl = []
for i, t in enumerate(ts):
    f = f"{W}/q{i:02d}.png"
    sh(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.2f}', '-i', W + '/master.mp4', '-frames:v', '1', '-vf',
        f"scale=216:-1,drawtext=text='{t:.1f}':x=6:y=6:fontsize=22:fontcolor=yellow", f]); fl.append(f)
sh(['ffmpeg', '-v', 'error', '-y', '-pattern_type', 'glob', '-i', W + '/q*.png', '-vf', 'tile=5x3', W + '/qa.jpg'])
for f in fl: os.remove(f)
print(json.dumps(dict(end=END, pauses=pauses, shots=len(segs), words=len(words))))
