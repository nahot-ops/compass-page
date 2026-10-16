// 使い方:
//   node export.mjs            → compass-ad.mp4 を書き出し
//   node export.mjs stills 1.5 6 ...  → 指定秒数の静止画を stills/ に保存
//   node export.mjs mux        → 今の compass-ad.mp4 にBGMだけ入れ直す（映像は再書き出ししない）
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { mkdirSync, renameSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const dir = path.dirname(fileURLToPath(import.meta.url));
const url = 'file://' + path.join(dir, 'compass-ad.html') + '?export';
const [mode, ...times] = process.argv.slice(2);

// BGM：曲の頭から使い、最後の2秒でフェードアウト。音量はWeb広告の標準（-16 LUFS）に整える
const BGM = path.join(dir, 'assets', 'bgm.mp3');
function mux(video, out, duration) {
  const af = `afade=t=in:d=0.15,afade=t=out:st=${duration - 2}:d=2,loudnorm=I=-16:TP=-1.5:LRA=11`;
  const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-i', video, '-t', String(duration), '-i', BGM,
    '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-af', af, '-ar', '48000', '-c:a', 'aac', '-b:a', '192k',
    '-t', String(duration), '-movflags', '+faststart', out], { stdio: 'inherit' });
  return new Promise((r, j) => ff.on('close', c => c ? j(new Error('ffmpeg ' + c)) : r()));
}

if (mode === 'mux') {
  const tmp = path.join(dir, 'compass-ad.tmp.mp4');
  await mux(path.join(dir, 'compass-ad.mp4'), tmp, 33);
  renameSync(tmp, path.join(dir, 'compass-ad.mp4'));
  console.log('done');
  process.exit(0);
}

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
await page.goto(url);
await page.evaluate(() => window.ready);
const { DURATION, FPS } = await page.evaluate(() => ({ DURATION: window.DURATION, FPS: window.FPS }));
const stage = page.locator('#stage');

if (mode === 'stills') {
  mkdirSync(path.join(dir, 'stills'), { recursive: true });
  for (const t of times) {
    await page.evaluate(t => window.render(t), +t);
    await stage.screenshot({ path: path.join(dir, 'stills', `t${(+t).toFixed(2)}.png`) });
  }
} else {
  const out = path.join(dir, 'compass-ad.video.tmp.mp4');
  const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'png', '-i', '-',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const total = Math.round(DURATION * FPS);
  for (let f = 0; f < total; f++) {
    await page.evaluate(t => window.render(t), f / FPS);
    const buf = await stage.screenshot({ type: 'png' });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (f % 150 === 0) console.log(`frame ${f}/${total}`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  // BGMを入れて、最後まで書き出せたときだけ本番ファイルに置き換える
  const tmp = path.join(dir, 'compass-ad.tmp.mp4');
  await mux(out, tmp, DURATION);
  renameSync(tmp, path.join(dir, 'compass-ad.mp4'));
  console.log('done');
}
await browser.close();
