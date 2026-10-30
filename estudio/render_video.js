// Uso: node render_video.js page.html outDir duracion fps [t1,t2,...]
// Si se pasan tiempos, solo saca esos fotogramas (previsualización).
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
(async () => {
  const [file, outDir, dur, fps, only] = process.argv.slice(2);
  fs.mkdirSync(outDir, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.resolve(file));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  const times = only ? only.split(',').map(Number)
    : Array.from({ length: Math.round(+dur * +fps) }, (_, i) => i / +fps);
  for (let i = 0; i < times.length; i++) {
    await p.evaluate(t => window.setT(t), times[i]);
    const name = only ? `t${times[i]}.png` : `f${String(i).padStart(4, '0')}.jpg`;
    await p.screenshot({ path: path.join(outDir, name), ...(only ? { type: 'png' } : { type: 'jpeg', quality: 95 }) });
  }
  await b.close();
  console.log('frames', times.length);
})();
