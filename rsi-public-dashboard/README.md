# RSI public dashboard

`index.html` is a standalone static page. It contains the snapshot data and the
SVG renderers; no build step or runtime API is required. The public Render URL is
`https://robot-rsi-three-settings-20261106.onrender.com` and the publishing branch
is `rsi-three-settings-public-site`. The deployed root page was checked against
this directory's `index.html`. Render's service settings are managed outside this
repository; there is no Render blueprint here.

## Snapshot contract

- The Luna setting uses the server Registry, sealed effective episode results,
  and operator validation records. Its timestamp is independent of the other
  two settings. Updating Luna does not update their snapshots.
- `DATA.luna.rows` joins research, full development evaluation, and independent
  validation by the exact candidate fingerprint. All nodes in one candidate row
  share the same vertical position. Harness mainline generations and Best
  generations are different quantities.
- Only submitted full-development evaluations appear in the middle lane. Only
  initial B1 validation or validation triggered by committed Best promotion
  appears in the right lane. Local experiments and offline feasibility audits
  do not count as full evaluations or additional robot trials.
- `completed`, `success`, and `calls` use effective results only. Invalid and
  running attempts remain explicit. A partial success fraction is never shown
  as a final 24-case rate. Calls count Robot model requests, not research-agent
  requests, tokens, or charges.
- `maintenance` follows actual global maintenance receipts. Each problem node
  is joined by Problem ID and that receipt's revision ID, with its own judgment,
  evidence, status, and source hash. Hovering a node shows its record references.
  Do not copy a later judgment into an earlier revision or create a maintenance
  column for an unfinished evaluation.

Only the curated public snapshot is embedded. Operator databases, credentials,
raw logs, host paths, and private runtime configuration are not published.
Validation results remain outside the live research feedback pipeline.

## Preview and check

```bash
python3 -m http.server 8767 --directory rsi-public-dashboard
```

The browser check covers all three tabs, candidate alignment, revision order,
text overflow, zoom, and mobile layout. It requires Node 20+ and Playwright with
Chromium. Install browser tooling in a temporary directory, not the robot runtime:

```bash
npm install --prefix /tmp/rsi-site-check playwright
/tmp/rsi-site-check/node_modules/.bin/playwright install chromium
NODE_PATH=/tmp/rsi-site-check/node_modules node tests/site/rsi_dashboard.cjs
```

Set `SITE_URL` to check the deployed site, `CHROMIUM_PATH` to use an existing
Chromium binary, and `SITE_ARTIFACTS` to choose a directory for screenshots and
check results. A CJK font is needed to inspect Chinese text in screenshots.

The page is a fixed snapshot. Publishing it does not start, stop, or modify RSI.
