const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// Install playwright if needed
try {
  require('playwright');
} catch(e) {
  console.log('Installing playwright...');
  execSync('npm install playwright', { cwd: '/Users/eduardorolim/Documents/Documentos Atual - MacBook Air de Eduardo/carrossel-v2-edu-99hud/', stdio: 'inherit' });
  execSync('npx playwright install chromium', { cwd: '/Users/eduardorolim/Documents/Documentos Atual - MacBook Air de Eduardo/carrossel-v2-edu-99hud/', stdio: 'inherit' });
}

const playwright = require('playwright');

const OUT_DIR = '/Users/eduardorolim/Documents/Documentos Atual - MacBook Air de Eduardo/carrossel-v2-edu-99hud/output/amazon-transformer';

(async () => {
  const browser = await playwright.chromium.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewportSize({ width: 1080, height: 1350 });

  await page.goto('http://localhost:8738/carrossel.html', { waitUntil: 'networkidle' });
  await page.waitForTimeout(3000);

  const dpr = await page.evaluate(() => window.devicePixelRatio);
  const cssW = await page.evaluate(() => window.innerWidth);
  const cssH = await page.evaluate(() => window.innerHeight);
  const scale = cssW / 1080;

  console.log(`DPR: ${dpr}, viewport: ${cssW}x${cssH}, scale: ${scale}`);

  const slides = await page.locator('body > div').all();
  const total = slides.length;
  console.log(`Total slides: ${total}`);

  // Hide all slides
  for (let i = 0; i < total; i++)
    await slides[i].evaluate(el => el.style.display = 'none');

  for (let i = 0; i < total; i++) {
    const num = String(i + 1).padStart(2, '0');
    const outPath = path.join(OUT_DIR, `slide_${num}.png`);

    const classes = await slides[i].evaluate(el => el.className);
    const isTipoA = classes.includes('slide-tipo-a');
    const bgColor = isTipoA ? '#0d0d0d' : '#000000';

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

    await page.waitForTimeout(400);

    await page.screenshot({
      path: outPath,
      clip: { x: 0, y: 0, width: cssW, height: cssH }
    });

    await slides[i].evaluate(el => {
      el.style.display = 'none';
      el.style.position = '';
      el.style.transform = '';
      el.style.transformOrigin = '';
      el.style.zIndex = '';
      el.style.width = '';
      el.style.height = '';
    });

    console.log(`✅ slide_${num}.png salvo`);
  }

  // Restore all
  for (let i = 0; i < total; i++)
    await slides[i].evaluate(el => el.style.display = '');

  await browser.close();
  console.log('\n✅ Todos os slides capturados!');
})();
