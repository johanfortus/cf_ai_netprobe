/**
 * Welcome to Cloudflare Workers! This is your first worker.
 *
 * - Run `npm run dev` in your terminal to start a development server
 * - Open a browser tab at http://localhost:8787/ to see your worker in action
 * - Run `npm run deploy` to publish your worker
 *
 * Bind resources to your worker in `wrangler.jsonc`. After adding bindings, a type definition for the
 * `Env` object can be regenerated with `npm run cf-typegen`.
 *
 * Learn more at https://developers.cloudflare.com/workers/
 */

export default {

	async fetch(request, env, ctx): Promise<Response> {
		const url = new URL(request.url);

		if (url.pathname === '/message') {
			return new Response('Hello, World!');
		}
		if (url.pathname === '/random') {
			return new Response(crypto.randomUUID());
		}

		// health check
		if (url.pathname === '/status') {
			return new Response(
				JSON.stringify({ ok: true, time: Date.now() }),
				{ headers: { "Content-Type": "application/json" } }
			);
		}

		// Pi sends network measurements here
		if (url.pathname === '/ingest' && request.method === 'POST') {
			const data = await request.json();
			console.log("Measurement from Pi: ", data);
			return new Response("OK");
		}

		// UI reads history
		if (url.pathname === '/history') {

			const mock = [
				{ latency: 42, jitter: 3, timestamp: Date.now() },
				{ latency: 51, jitter: 5, timestamp: Date.now() - 5000 }
			];

			return new Response(
				JSON.stringify(mock),
				{ headers: { "Content-Type": "application/json" } }
			);
		}
		
		return new Response('Not Found', { status: 404 });
	},
} satisfies ExportedHandler<Env>;