#!/usr/bin/env node

// Liest einen LinkedIn-Beitrag direkt über einen eigenen CDP-Tab. Dieser kleine
// Fallback vermeidet Konflikte, wenn eine andere Playwright-Instanz am Debug-Port hängt.

const endpoint = (process.argv[2] || '').replace(/\/$/, '');
const targetUrl = process.argv[3] || '';

if (!endpoint || !targetUrl) {
  process.stderr.write('usage: cdp_post_text.mjs <cdp-endpoint> <url>\n');
  process.exit(2);
}

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
let target;
let socket;

async function run() {
  const response = await fetch(`${endpoint}/json/new?${encodeURIComponent('about:blank')}`, {
    method: 'PUT',
  });
  if (!response.ok) throw new Error(`CDP target: HTTP ${response.status}`);
  target = await response.json();

  socket = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => {
    socket.addEventListener('open', resolve, {once: true});
    socket.addEventListener('error', () => reject(new Error('CDP websocket failed')), {once: true});
  });

  let serial = 0;
  const pending = new Map();
  socket.addEventListener('message', event => {
    const message = JSON.parse(String(event.data));
    if (!message.id || !pending.has(message.id)) return;
    const {resolve, reject} = pending.get(message.id);
    pending.delete(message.id);
    if (message.error) reject(new Error(message.error.message || 'CDP command failed'));
    else resolve(message.result || {});
  });

  const send = (method, params = {}) => new Promise((resolve, reject) => {
    const id = ++serial;
    pending.set(id, {resolve, reject});
    socket.send(JSON.stringify({id, method, params}));
  });

  await send('Page.enable');
  await send('Runtime.enable');
  await send('Page.navigate', {url: targetUrl});

  const expression = `(() => {
    const selectors = [
      'div.feed-shared-update-v2',
      "div[role='listitem'][componentkey^='update-card-focus']",
      "[data-urn^='urn:li:activity']",
      'main article'
    ];
    let node = null;
    for (const selector of selectors) {
      node = document.querySelector(selector);
      if (node) break;
    }
    if (!node) return null;
    const contentNode = node.querySelector(
      ".update-components-text, .feed-shared-inline-show-more-text, [data-test-id='main-feed-activity-card__commentary']"
    );
    const text = (contentNode?.innerText || node.innerText || '')
      .split('\\n')
      .filter(line => line.trim().toLowerCase() !== 'hashtag')
      .join('\\n')
      .trim();
    if (!text) return null;
    const authorNode = node.querySelector([
      "span.update-components-actor__name",
      ".update-components-actor__name span[aria-hidden='true']",
      ".update-components-actor__title span[aria-hidden='true']",
      "a.update-components-actor__meta-link span[aria-hidden='true']"
    ].join(','));
    const fullLines = (node.innerText || '').split('\\n').map(line => line.trim()).filter(Boolean);
    const inferredAuthor = fullLines[0]?.toLowerCase() === 'feed post' ? fullLines[1] : '';
    return {
      text,
      author: (authorNode?.innerText || inferredAuthor || '').trim(),
      url: location.href
    };
  })()`;

  for (let attempt = 0; attempt < 20; attempt += 1) {
    await sleep(attempt === 0 ? 2500 : 750);
    const evaluated = await send('Runtime.evaluate', {
      expression,
      returnByValue: true,
      awaitPromise: true,
    });
    const value = evaluated.result?.value;
    if (value?.text) return value;
  }
  throw new Error('Kein LinkedIn-Beitrag im neuen Tab gefunden');
}

try {
  const result = await run();
  process.stdout.write(`${JSON.stringify(result)}\n`);
} catch (error) {
  process.stderr.write(`${error?.message || error}\n`);
  process.exitCode = 1;
} finally {
  try { socket?.close(); } catch {}
  if (target?.id) {
    try { await fetch(`${endpoint}/json/close/${target.id}`); } catch {}
  }
}
