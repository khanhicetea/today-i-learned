- Date : 2023-08-29
- Tags : js es6

## ES6 Module import in client browsers

*moduleA.js*

```js
export const message = "Hello from moduleA!";
```

*moduleB.js*

```js
import { message } from './moduleA.js';
console.log(message);
```

*app.html*

```html
<script type="module" src="moduleB.js"></script>

// Print console log "Hello from moduleA!"
```

So *moduleB.js* acts like a module entry-point, it loads all dependencies deeply to run it-self, so you only need add script tag point to it.

