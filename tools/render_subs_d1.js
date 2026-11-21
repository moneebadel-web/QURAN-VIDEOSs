// Design 1 "Sanft einblenden": renders one transparent 1080x1920 PNG per Arabic word
// (positioned in its full verse line) and one per German line.
// Usage: node render_subs_d1.js groups.json outdir
const fs = require('fs'), path = require('path'), { chromium } = require('playwright');
const [,, gfile, outdir] = process.argv;
const groups = JSON.parse(fs.readFileSync(gfile, 'utf8'));
const b64 = f => fs.readFileSync(f).toString('base64');
const amiri = b64('/home/claude/fonts/Amiri-1.000/AmiriQuran.ttf');
const inter = b64('/home/claude/fonts/Inter.ttf');
const fix = s => s.replace(/ٗ/g, 'ࣰ').replace(/ٞ/g, 'ࣱ').replace(/ٖ/g, 'ࣲ').replace(/۞/g, '').trim();
const css = `
@font-face{font-family:AQ;src:url(data:font/ttf;base64,${amiri})}
@font-face{font-family:IN;src:url(data:font/ttf;base64,${inter})}
html,body{margin:0;width:1080px;height:1920px;background:transparent}
#blk{position:absolute;left:70px;right:70px;bottom:520px;text-align:center}
.ar{font-family:AQ;font-size:78px;line-height:1.55;color:#fff;direction:rtl;
  text-shadow:0 2px 6px rgba(0,0,0,.85),0 0 28px rgba(0,0,0,.55)}
.de{font-family:IN;font-weight:500;font-size:38px;line-height:1.3;color:#f3ead8;margin-top:44px;
  text-shadow:0 2px 6px rgba(0,0,0,.85),0 0 28px rgba(0,0,0,.55)}
.h{visibility:hidden}`;
(async () => {
  fs.mkdirSync(outdir, { recursive: true });
  const br = await chromium.launch(); const pg = await br.newPage({ viewport: { width: 1080, height: 1920 } });
  for (const [gi, g] of groups.entries()) {
    const words = g.words.map(fix);
    const shots = words.map((_, k) => ({ name: `g${gi}_w${k}.png`, ar: k, de: false }));
    shots.push({ name: `g${gi}_de.png`, ar: -1, de: true });
    for (const s of shots) {
      const ar = words.map((w, k) => `<span class="${k === s.ar ? '' : 'h'}">${w}</span>`).join(' ');
      await pg.setContent(`<style>${css}</style><div id="blk"><div class="ar">${ar}</div><div class="de ${s.de ? '' : 'h'}">${g.de}</div></div>`);
      await pg.evaluate(() => document.fonts.ready);
      await pg.screenshot({ path: path.join(outdir, s.name), omitBackground: true });
    }
  }
  await br.close(); console.log('done');
})();
