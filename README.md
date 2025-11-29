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

## Architecture Overview

- **Raspberry Pi Probe**  
  Runs a Python script that measures network health (latency, jitter, packet loss) and sends JSON to the Cloudflare Worker.

- **Cloudflare Worker**  
  Exposes:
  - `POST /ingest` – accepts measurements from the Pi
  - `GET /history` – returns stored measurements for the dashboard

- **Durable Object: NetprobeHistory**  
  Stores all received measurements in persistent storage so they can be queried later.

<img width="900" src="assets/Architecture.jpg" />

