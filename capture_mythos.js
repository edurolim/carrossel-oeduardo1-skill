const playwright = require('playwright');
const OUT_DIR = '/Users/eduardorolim/Documents/Documentos Atual - MacBook Air de Eduardo/carrossel-v2-edu-99hud/output/claude-mythos';

(async () => {
  const browser = await playwright.chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1080, height: 1350 });
  await page.goto('http://localhost:8741/carrossel.html', { waitUntil: 'networkidle' });
  await page.waitForTimeout(3000);

  const cssW = await page.evaluate(() => window.innerWidth);
  const cssH = await page.evaluate(() => window.innerHeight);
  const scale = cssW / 1080;
  const slides = await page.locator('body > div').all();
  const total = slides.length;
  console.log(`Total slides: ${total}, scale: ${scale}`);

  for (let i = 0; i < total; i++)
    await slides[i].evaluate(el => el.style.display = 'none');

  for (let i = 0; i < total; i++) {
    const num = String(i + 1).padStart(2, '0');
    const classes = await slides[i].evaluate(el => el.className);
    const bgColor = classes.includes('slide-tipo-a') ? '#0d0d0d' : '#000000';

    await page.evaluate(c => {
      document.documentElement.style.background = c;
      document.body.style.background = c;
    }, bgColor);

    await slides[i].evaluate((el, s) => {
      el.style.display = 'flex';
      el.style.position = 'fixed';
      el.style.top = '0'; el.style.left = '0';
      el.style.width = '1080px'; el.style.height = '1350px';
      el.style.zIndex = '9999';
      el.style.transform = `scale(${s})`;
      el.style.transformOrigin = 'top left';
    }, scale);

    await page.waitForTimeout(400);
    await page.screenshot({ path: `${OUT_DIR}/slide_${num}.png`, clip: { x: 0, y: 0, width: cssW, height: cssH } });
    console.log(`✅ slide_${num}.png`);

    await slides[i].evaluate(el => {
      el.style.display = 'none';
      el.style.position = el.style.transform = el.style.zIndex = '';
      el.style.width = el.style.height = '';
    });
  }

  for (let i = 0; i < total; i++)
    await slides[i].evaluate(el => el.style.display = '');

  await browser.close();
  console.log('\n✅ Todos os slides capturados!');
})();
