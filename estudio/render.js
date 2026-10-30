// Renderiza cada .html indicado a PNG. Tamaño desde <meta name="size" content="WxH">.
// Uso: node render.js out/dir file1.html file2.html ...
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const [outDir, ...files] = process.argv.slice(2);
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  for (const f of files) {
    const html = fs.readFileSync(f, 'utf8');
    const m = html.match(/name="size" content="(\d+)x(\d+)"/);
    const [w, h] = m ? [+m[1], +m[2]] : [1080, 1350];
    const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    await page.goto('file://' + path.resolve(f));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(150);
    const out = path.join(outDir, path.basename(f, '.html') + '.png');
    await page.screenshot({ path: out, type: 'png' });
    await page.close();
    console.log('ok', out);
  }
  await browser.close();
})();
