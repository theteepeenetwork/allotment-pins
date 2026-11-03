// usage: node tools/shoot.js <workdir> <outdir>   (renders <workdir>/<slug>.html at 1000x1500 to <outdir>/<slug>.jpg)
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const [work, out] = process.argv.slice(2);
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1000, height: 1500 } });
for (const s of JSON.parse(fs.readFileSync(path.join(work, 'list.json')))) { await p.goto('file://' + path.resolve(work, s + '.html')); await p.waitForTimeout(1200); await p.screenshot({ path: path.join(out, s + '.jpg'), type: 'jpeg', quality: 88 }); }
await b.close(); })();
