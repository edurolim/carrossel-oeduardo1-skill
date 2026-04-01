const playwright = require('playwright');
const OUT = '/Users/eduardorolim/Documents/Documentos Atual - MacBook Air de Eduardo/carrossel-v2-edu-99hud/output/claude-computer-use';

(async () => {
  const browser = await playwright.chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1080, height: 1350 });
  await page.goto('http://localhost:8742/carrossel.html', { waitUntil: 'networkidle' });
  await page.waitForTimeout(3000);

  const cssW = await page.evaluate(() => window.innerWidth);
  const cssH = await page.evaluate(() => window.innerHeight);
  const scale = cssW / 1080;
  const slides = await page.locator('body > div').all();
  console.log(`${slides.length} slides, scale: ${scale}`);

  for (let i = 0; i < slides.length; i++)
    await slides[i].evaluate(el => el.style.display = 'none');

  for (let i = 0; i < slides.length; i++) {
    const num = String(i + 1).padStart(2, '0');
    const classes = await slides[i].evaluate(el => el.className);
    const bg = classes.includes('slide-tipo-a') ? '#0d0d0d' : '#000000';

    await page.evaluate(c => {
      document.documentElement.style.background = c;
      document.body.style.background = c;
    }, bg);

    await slides[i].evaluate((el, s) => {
      el.style.cssText = `display:flex;position:fixed;top:0;left:0;width:1080px;height:1350px;z-index:9999;transform:scale(${s});transform-origin:top left;`;
    }, scale);

    await page.waitForTimeout(400);
    await page.screenshot({ path: `${OUT}/slide_${num}.png`, clip: { x: 0, y: 0, width: cssW, height: cssH } });
    console.log(`✅ slide_${num}.png`);

    await slides[i].evaluate(el => { el.style.cssText = 'display:none'; });
  }

  await browser.close();
  console.log('\n✅ Concluído!');
})();
