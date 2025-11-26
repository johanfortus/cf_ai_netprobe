# NetProbe

Analyze network health using a Raspberry Pi probe and Cloudflare Workers AI

---
## Setup

Before starting, make sure you have the following:
- **Raspberry Pi 3 / 4 / 5**
- **Node.js 18+**
- **Python 3.8+**

Clone the repository to your local machine and navigate into the project folder:
```bash
git clone https://github.com/johanfortus/cf_ai_netprobe
cd cf_ai_netprobe
```
Set up the Cloudflare Worker:
```bash
cd worker
npm install
npx wrangler dev
```
This starts the Worker locally at:
```
http://localhost:8787
```

## System Architecture
1. **Raspberry Pi Probe** - Collects network metrics.
2. **Cloudflare Worker** - Handles ingestion and triggers other services.
3. **Durable Object (NetProbe History)** - Stores historical measurements for trend analysis.
4. **Workers AI** - Generates summaries.
5. **Cloudflare Pages Dashboard** - Displays history and insights in the browser.

<img width="900" src="assets/Architecture.jpg" />
