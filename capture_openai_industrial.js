const { chromium } = require('playwright');
const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 8883;
const OUTPUT_DIR = path.join(__dirname, 'output/openai-industrial');
const HTML_FILE = path.join(OUTPUT_DIR, 'carrossel.html');

const server = http.createServer((req, res) => {
  let filePath = req.url === '/' ? HTML_FILE : path.join(OUTPUT_DIR, req.url);
  fs.readFile(filePath, (err, data) => {
    if (err) { res.writeHead(404); res.end(); return; }
    const ext = path.extname(filePath).toLowerCase();
    const mime = { '.html': 'text/html', '.jpg': 'image/jpeg', '.png': 'image/png', '.css': 'text/css' };
    res.writeHead(200, { 'Content-Type': mime[ext] || 'application/octet-stream' });
    res.end(data);
  });
});

server.listen(PORT, async () => {
  console.log(`Server running on port ${PORT}`);
  const browser = await chromium.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' });
  const page = await browser.newPage();
  const DPR = 1;
  await page.setViewportSize({ width: 1080 * DPR, height: 1350 * DPR, deviceScaleFactor: DPR });
  await page.goto(`http://localhost:${PORT}/`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(2000);

  const slides = await page.$$('.slide-capa, .slide-split, .slide-mini-cta, .slide-tipo-c, .slide-tipo-a, .slide-tipo-d, .slide-cta');
  console.log(`Found ${slides.length} slides`);

  for (let i = 0; i < slides.length; i++) {
    const num = String(i + 1).padStart(2, '0');
    const outPath = path.join(OUTPUT_DIR, `slide_${num}.png`);
    await slides[i].screenshot({ path: outPath });
    console.log(`Captured slide_${num}.png`);
  }

  await browser.close();
  server.close();
  console.log('Done!');
});
