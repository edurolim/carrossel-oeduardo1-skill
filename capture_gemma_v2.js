const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const http = require('http');
const { spawn } = require('child_process');

try { require('playwright'); } catch(e) {
  console.log('Installing playwright...');
  execSync('npm install playwright', { cwd: '/Users/eduardorolim/Documents/Documentos Atual - MacBook Air de Eduardo/carrossel-v2-edu-99hud/', stdio: 'inherit' });
}

const playwright = require('playwright');

const OUT_DIR = '/Users/eduardorolim/Documents/Documentos Atual - MacBook Air de Eduardo/carrossel-v2-edu-99hud/output/gemma4-gratis-v2';
const SERVE_DIR = OUT_DIR;
const PORT = 8879;

function startServer() {
  const server = http.createServer((req, res) => {
    let filePath = path.join(SERVE_DIR, req.url === '/' ? 'carrossel.html' : req.url);
    fs.readFile(filePath, (err, data) => {
      if (err) { res.writeHead(404); res.end(); return; }
      const ext = path.extname(filePath);
      const types = { '.html':'text/html', '.js':'text/javascript', '.css':'text/css', '.jpg':'image/jpeg', '.png':'image/png' };
      res.writeHead(200, { 'Content-Type': types[ext] || 'application/octet-stream' });
      res.end(data);
    });
  });
  server.listen(PORT);
  return server;
}

(async () => {
  const server = startServer();
  await new Promise(r => setTimeout(r, 500));

  const browser = await playwright.chromium.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewportSize({ width: 1080, height: 1350 });
  await page.goto(`http://localhost:${PORT}/carrossel.html`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(3000);

  const cssW = await page.evaluate(() => window.innerWidth);
  const cssH = await page.evaluate(() => window.innerHeight);
  const scale = cssW / 1080;
  console.log(`viewport: ${cssW}x${cssH}, scale: ${scale}`);

  const slides = await page.locator('body > div').all();
  console.log(`Total slides: ${slides.length}`);

  for (let i = 0; i < slides.length; i++)
    await slides[i].evaluate(el => el.style.display = 'none');

  for (let i = 0; i < slides.length; i++) {
    const num = String(i + 1).padStart(2, '0');
    const outPath = path.join(OUT_DIR, `slide_${num}.png`);
    const classes = await slides[i].evaluate(el => el.className);
    const bgColor = classes.includes('slide-cta') ? '#ffffff' : classes.includes('slide-tipo-a') ? '#0d0d0d' : '#000000';

    await page.evaluate(c => {
      document.documentElement.style.background = c;
      document.body.style.background = c;
    }, bgColor);

    await slides[i].evaluate((el, s) => {
      el.style.display = 'flex';
      el.style.position = 'fixed';
      el.style.top = '0';
      el.style.left = '0';
      el.style.width = '1080px';
      el.style.height = '1350px';
      el.style.zIndex = '9999';
      el.style.transform = `scale(${s})`;
      el.style.transformOrigin = 'top left';
    }, scale);

    await page.waitForTimeout(500);
    await page.screenshot({ path: outPath, clip: { x: 0, y: 0, width: cssW, height: cssH } });
    console.log(`slide_${num}.png OK`);

    await slides[i].evaluate(el => {
      el.style.display = 'none';
      el.style.position = '';
      el.style.transform = '';
      el.style.zIndex = '';
    });
  }

  await browser.close();
  server.close();
  console.log('Done.');
})();
