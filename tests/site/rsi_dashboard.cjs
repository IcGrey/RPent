const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const os=require('node:os');
const {pathToFileURL}=require('node:url');
const artifacts=process.env.SITE_ARTIFACTS||fs.mkdtempSync(path.join(os.tmpdir(),'rsi-site-check-'));
fs.mkdirSync(artifacts,{recursive:true});
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:process.env.CHROMIUM_PATH,args:['--no-sandbox']});
 const page=await browser.newPage({viewport:{width:1600,height:1100},deviceScaleFactor:1});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.SITE_URL||pathToFileURL(path.resolve(__dirname,'../../rsi-public-dashboard/index.html')).href);await page.waitForSelector('#flow svg');
 for(const setting of ['luna','h0','ds']){
  await page.locator(`[data-id="${setting}"]`).click();
  assert.equal(await page.locator('#flow svg').count(),1);assert.equal(await page.locator('#problems svg').count(),1);
 }
 await page.locator('[data-id="luna"]').click();
 const checks=await page.evaluate(()=>{
  const groups=[...document.querySelectorAll('#flow g[data-row]')],rows={};
  for(const g of groups){(rows[g.dataset.row]??=[]).push({candidate:g.dataset.candidate,y:g.dataset.y,lane:g.dataset.lane})}
  const problems={};for(const g of document.querySelectorAll('#problems g[data-problem]'))(problems[g.dataset.problem]??=[]).push({revision:+g.dataset.revision,y:g.dataset.y,maintenance:g.dataset.maintenance});
  const overflow=[];
  for(const g of document.querySelectorAll('g[data-row],g[data-problem]')){
   const r=g.querySelector('rect');const right=+r.getAttribute('x')+(+r.getAttribute('width')),bottom=+r.getAttribute('y')+(+r.getAttribute('height'));
   for(const t of g.querySelectorAll('text')){const b=t.getBBox();if(b.x+b.width>right-5||b.y+b.height>bottom-5)overflow.push(t.textContent)}
  }
  return {rows,problems,overflow,dev:DATA.luna.rows.filter(r=>r.dev).map(r=>r.key),validation:DATA.luna.rows.filter(r=>r.validation).map(r=>r.key),snapshot:DATA.luna.snapshot};
 });
 for(const row of Object.values(checks.rows)){assert.equal(new Set(row.map(x=>x.candidate)).size,1);assert.equal(new Set(row.map(x=>x.y)).size,1)}
 assert.deepEqual(checks.dev,['B1','r2','r3','r11']);assert.deepEqual(checks.validation,['B1','r2','r3']);
 assert.equal(Object.keys(checks.problems).length,6);
 for(const nodes of Object.values(checks.problems)){assert.deepEqual(nodes.map(x=>x.revision),[1,2,3]);assert.equal(new Set(nodes.map(x=>x.y)).size,1)}
 assert.deepEqual(checks.overflow,[]);assert.deepEqual(errors,[]);
 await page.screenshot({path:path.join(artifacts,'luna-desktop.png'),fullPage:true});
 await page.locator('#problems').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(artifacts,'luna-problems.png')});
 const width=await page.locator('#flow svg').evaluate(e=>e.getBoundingClientRect().width);
 await page.locator('#plus').click();await page.waitForFunction(w=>document.querySelector('#flow svg').getBoundingClientRect().width>w,width);
 await page.locator('#reset').click();await page.waitForTimeout(200);
 await page.setViewportSize({width:390,height:844});await page.locator('[data-id="luna"]').click();await page.waitForTimeout(200);
 assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
 await page.screenshot({path:path.join(artifacts,'luna-mobile.png'),fullPage:true});
 await page.locator('#plus').click();await page.waitForTimeout(200);assert((await page.locator('#flow').evaluate(e=>e.scrollWidth))>(await page.locator('#flow').evaluate(e=>e.clientWidth)));
 await page.locator('#problem-plus').click();await page.locator('#problem-reset').click();
 fs.writeFileSync(path.join(artifacts,'browser-check.json'),JSON.stringify({checks,errors,desktop:1600,mobile:390},null,2));
 console.log(JSON.stringify({passed:true,snapshot:checks.snapshot,alignedRows:Object.keys(checks.rows).length,problemRows:Object.keys(checks.problems).length,artifacts,errors}));
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
