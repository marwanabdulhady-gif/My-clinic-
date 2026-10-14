'use strict';
// Optional browser tooling only. Nothing here is shipped in a learner package.
const fs = require('node:fs');
const path = require('node:path');
const {pathToFileURL, fileURLToPath} = require('node:url');
const {brotliDecompressSync} = require('node:zlib');
const {execFileSync} = require('node:child_process');
const repo = path.resolve(__dirname, '../../../..');
const tooling = path.join(repo, '.generated/tooling/node_modules');

async function launchBrowser() {
  const {chromium} = require(process.env.PLAYWRIGHT_MODULE || path.join(tooling, 'playwright'));
  const launch = {headless: true};
  if (process.env.CHROMIUM_EXECUTABLE) {
    launch.executablePath = process.env.CHROMIUM_EXECUTABLE;
    launch.args = ['--no-sandbox'];
  } else {
    const spec = process.env.CHROMIUM_MODULE || pathToFileURL(path.join(tooling, '@sparticuz/chromium/build/index.js')).href;
    const imported = await import(spec);
    const binary = imported.default || imported;
    // The npm binary bundles NSS/NSPR; minimal Linux sandboxes may not have them.
    // Extract that local archive, rather than fetching OS packages or altering system files.
    const modulePath = spec.startsWith('file:') ? fileURLToPath(spec) : path.resolve(spec);
    const archive = path.resolve(path.dirname(modulePath), '../bin/al2023.tar.br');
    if (process.platform === 'linux' && fs.existsSync(archive)) {
      const libs = path.join(repo, '.generated/browser-runtime');
      fs.mkdirSync(libs, {recursive: true});
      if (!fs.existsSync(path.join(libs, 'lib/libnspr4.so'))) {
        const tar = path.join(libs, 'al2023.tar');
        fs.writeFileSync(tar, brotliDecompressSync(fs.readFileSync(archive)));
        execFileSync('tar', ['-xf', tar, '-C', libs]);
        fs.unlinkSync(tar);
      }
      launch.env = {...process.env, LD_LIBRARY_PATH: path.join(libs, 'lib') + ':' + (process.env.LD_LIBRARY_PATH || '')};
    }
    launch.executablePath = await binary.executablePath();
    launch.args = binary.args.filter(arg => !['--disable-web-security', '--allow-running-insecure-content'].includes(arg));
  }
  return chromium.launch(launch);
}
module.exports = {launchBrowser, repo};
