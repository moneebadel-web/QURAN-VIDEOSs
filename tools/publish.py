"""Copy finished video into repo, push, print media URL + caption JSON. Usage: publish.py <id> <slug>"""
import json, subprocess, sys, shutil, os
vid, slug = sys.argv[1], sys.argv[2]
W = f'/home/claude/work/batch/{vid}'; R = '/home/claude/quran-videoss'
C = json.load(open(W + '/config.json', encoding='utf8')); words = json.load(open(W + '/words.json', encoding='utf8'))
d = f'{R}/videos/{slug}'; os.makedirs(d, exist_ok=True)
src = W + '/master.mp4'
if os.path.getsize(src) > 95e6:
    du = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)
    kb = int(88e6 * 8 / du / 1000) - 260
    subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-c:v','libx264','-preset','medium','-b:v',f'{kb}k','-maxrate',f'{int(kb*1.3)}k','-bufsize',f'{kb*2}k','-c:a','copy','-movflags','+faststart',W+'/master_s.mp4'],check=True)
    src = W + '/master_s.mp4'
shutil.copy(src, d + '/master.mp4')
for f in ['config.json', 'words.json', 'align.json', 'shots.json']: shutil.copy(f'{W}/{f}', d)
def g(*a): return subprocess.run(['git', '-C', R] + list(a), capture_output=True, text=True)
g('add', '-A'); g('commit', '-q', '-m', f'Video {slug}\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01GZKPvMXkQ6DB1ETKygWmbi')
p = subprocess.run(['git', '-C', R, '-c', 'push.negotiate=true', 'push', 'origin', 'main'], capture_output=True, text=True)
sha = g('rev-parse', 'HEAD').stdout.strip()
vs = [v for v in dict.fromkeys(w['v'] for w in words) if v]
rng = f"{C['sura']}:{vs[0]}" + (f"–{vs[-1]}" if len(vs) > 1 else '')
cap = f"Sure {C['name']} {rng}\n\n" + '\n'.join(C['verses'][str(v)]['de'] for v in vs) + \
      "\n\n#quran #koran #islam #quranrecitation #qurantiktok"
print(json.dumps(dict(url=f'https://raw.githubusercontent.com/moneebadel-web/QURAN-VIDEOSs/{sha}/videos/{slug}/master.mp4',
                      caption=cap, push=p.stderr.strip()[-80:]), ensure_ascii=False))
