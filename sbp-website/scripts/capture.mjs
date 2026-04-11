import { chromium } from "playwright";
import fs from "node:fs";
import path from "node:path";

const outDir = path.resolve(".screenshots");
fs.mkdirSync(outDir, { recursive: true });

const pages = [
  { route: "/", name: "01-home" },
  { route: "/about", name: "02-about" },
  { route: "/programs", name: "03-programs" },
  { route: "/gallery", name: "04-gallery" },
  { route: "/get-involved", name: "05-get-involved" },
  { route: "/contact", name: "06-contact" },
];

const viewports = [
  { name: "desktop", width: 1440, height: 900 },
  { name: "mobile", width: 390, height: 844 },
];

(async () => {
  const browser = await chromium.launch();
  try {
    for (const vp of viewports) {
      const ctx = await browser.newContext({
        viewport: { width: vp.width, height: vp.height },
        deviceScaleFactor: 2,
        reducedMotion: "reduce",
      });
      const page = await ctx.newPage();
      for (const p of pages) {
        const url = `http://localhost:5173${p.route}`;
        await page.goto(url, { waitUntil: "networkidle" });
        // Give framer-motion a tick
        await page.waitForTimeout(400);
        const file = path.join(outDir, `${p.name}-${vp.name}.png`);
        await page.screenshot({ path: file, fullPage: true });
        console.log(`✔ ${file}`);
      }
      await ctx.close();
    }
  } finally {
    await browser.close();
  }
})();
