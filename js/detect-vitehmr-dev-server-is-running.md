- Date : 2024-08-04
- Tags : js web vite hmr

## Detect ViteHMR dev server is running

Vite server has a middleware named `viteHMRPingMiddleware` in this source code

https://github.com/vitejs/vite/blob/81327eb980c308474a586a9cb9c0c5fff10eba34/packages/vite/src/node/server/index.ts#L876

So we have a simple way to check if Vite HMR server is running by calling a ping http request to the url endpoint (with timeout 1s)

```js
function checkViteHMR() {
	fetch('http://localhost:5173/_ping', {
		method: 'HEAD',
		headers: {
			'Accept': 'text/x-vite-ping'
		}
	})
	.then(response => {
		if (response.status === 204) {
			// Do something here
			console.log('Vite HMR is running');
		} else {
			console.log('Received response with status:', response.status);
		}
	})
	.catch(error => {
		console.error('Error making request:', error);
	});
}
```
