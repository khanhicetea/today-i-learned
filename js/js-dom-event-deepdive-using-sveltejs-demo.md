- Date : 2023-09-01
- Tags : js svelte dom

## JS DOM event deepdive using SvelteJS demo

The DOM event handling go through 2 phrases : Capture and Bubble (with support of preventDefault, stopPropagation, stopImmediatePropagation methods to modify behavior)

![JS DOM event](https://user-images.githubusercontent.com/4528223/264920890-13fa04c5-a1ca-4e56-bdf4-1b0f1f234c47.png)

Try the demo here : https://svelte.dev/repl/99d1edbf7bd9426384be2c7763d2e872?version=4.2.0

```html
<script>
	const onClickEle = (e) => {
		console.log((new Date()).toISOString() + " : Clicked " + e.currentTarget.tagName)
	}
</script>

<h5>Default (bubble)</h5>
<div on:click={onClickEle}>
	<button on:click={onClickEle}>Click here!</button>
</div>

<h5>Default (bubble with stopPropagation)</h5>
<div on:click={onClickEle}>
	<button on:click|stopPropagation={onClickEle}>Click here!</button>
</div>

<h5>Parent capture</h5>
<div on:click|capture={onClickEle}>
	<button on:click={onClickEle}>Click here!</button>
</div>

<h5>Parent capture stopPropagation</h5>
<div on:click|capture|stopPropagation={onClickEle}>
	<button on:click={onClickEle}>Click here!</button>
</div>

<h5>Self (ele = event target)</h5>
<div on:click|self={onClickEle}>
	<button on:click={onClickEle}>Click here!</button>
</div>

<style>
		div { padding: 10px 30px; background: gray; cursor: pointer; display: inline }
</style>
```

