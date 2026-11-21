// Generic transparent PNG renderer. Usage: node render_html.js jobs.json
// jobs.json = {css: "...", items: [{path, html}]}
const fs = require('fs'), { chromium } = require('playwright');
const job = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const b64 = f => fs.readFileSync(f).toString('base64');
const fonts = `
@font-face{font-family:AQ;src:url(data:font/ttf;base64,${b64('/home/claude/fonts/Amiri-1.000/AmiriQuran.ttf')})}
@font-face{font-family:IN;src:url(data:font/ttf;base64,${b64('/home/claude/fonts/Inter.ttf')})}
@font-face{font-family:LA;src:url(data:font/ttf;base64,${b64('/home/claude/fonts/Lateef.ttf')})}
@font-face{font-family:MO;src:url(data:font/ttf;base64,${b64('/home/claude/fonts/Montserrat.ttf')})}
html,body{margin:0;width:1080px;height:1920px;background:transparent;overflow:hidden}`;
(async () => {
  const br = await chromium.launch(); const pg = await br.newPage({ viewport: { width: 1080, height: 1920 } });
  for (const it of job.items) {
    await pg.setContent(`<style>${fonts}${job.css}</style>${it.html}`);
    await pg.evaluate(() => document.fonts.ready);
    if (it.fit) await pg.evaluate((sel) => {           // shrink font until element fits width
      const e = document.querySelector(sel); let fs = parseFloat(getComputedStyle(e).fontSize);
      while (e.scrollWidth > 1000 && fs > 40) { fs -= 6; e.style.fontSize = fs + 'px'; }
    }, it.fit);
    await pg.screenshot({ path: it.path, omitBackground: true });
  }
  await br.close(); console.log('rendered', job.items.length);
})();
