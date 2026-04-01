const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  await page.setViewportSize({ width: 1080, height: 1350 });

  const htmlPath = path.resolve(__dirname, 'output/openai-ipo/carrossel.html');
  await page.goto(`file://${htmlPath}`);
  await page.waitForTimeout(4000);

  const dpr = await page.evaluate(() => window.devicePixelRatio);
  const cssW = await page.evaluate(() => window.innerWidth);
  const cssH = await page.evaluate(() => window.innerHeight);
  const scale = cssW / 1080;

  console.log(`DPR: ${dpr}, CSS: ${cssW}x${cssH}, scale: ${scale}`);

  const slides = await page.locator('body > div').all();
  const total = slides.length;
  console.log(`Total de slides: ${total}`);

  for (let i = 0; i < total; i++)
    await slides[i].evaluate(el => el.style.display = 'none');

  for (let i = 0; i < total; i++) {
    const num = String(i + 1).padStart(2, '0');
    const outPath = path.resolve(__dirname, `output/openai-ipo/slide_${num}.png`);

    const classes = await slides[i].evaluate(el => el.className);
    const isAccent = classes.includes('accent-bg');
    const isEditorial = classes.includes('slide-editorial');
    const bgColor = isAccent ? '#0E9957' : (isEditorial ? '#292A25' : '#000000');

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

    console.log(`✅ slide_${num}.png`);

    await slides[i].evaluate(el => {
      el.style.display = 'none';
      el.style.position = '';
      el.style.transform = '';
      el.style.transformOrigin = '';
    });
  }

  for (let i = 0; i < total; i++)
    await slides[i].evaluate(el => el.style.display = '');

  await browser.close();
  console.log('\n✅ Todos os slides capturados!');
})();
