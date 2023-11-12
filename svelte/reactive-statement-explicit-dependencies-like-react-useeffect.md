- Date : 2023-11-12
- Tags : #svelte #js #reactive #web

## Reactive statement explicit dependencies like React useEffect

Svelte uses it compiler to detect the reactive dependencies, to trigger the reactive updater function. So our work need is make sure all dependent variables appear in the line.

I use the below logic trick like this (!0 always true so it won't run init array [x,z,y]), but compiler always see the x,z,y in dependencies. :D

```js
result = (!0 || [x,y,z]) ? calc() : null;
```

OK, here is sample Svelve 4 code (sure Svelte 5 Runes is the saver)

```html
<script>
	let x = 1;
	let y = 1;	
	let z = 1;	
	let result = 0;

	function calc() {
			return x * y * z;
	}

	$: result = (!0 || [x,y,z]) ? calc() : null;

	function handleClickX() {
		x += 1;
	}
	
	function handleClickY() {
		y += 1;
	}

	function handleClickZ() {
		z += 1;
	}
</script>

<button on:click={handleClickX}>
	x = {x}
</button>
<button on:click={handleClickY}>
	y = {y}
</button>
<button on:click={handleClickZ}>
	z = {z}
</button>

<p>Result = {result}</p>
```


