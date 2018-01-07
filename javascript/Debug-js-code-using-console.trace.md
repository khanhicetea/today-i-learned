- Date : 2018-01-07
- Tags : #javascript #debug

## Debug js code using console.trace

Browsers provide an useful function help you debug easier than using simple `console.log` function.

That is `console.trace`, which prints a stack trace to called function.

Example :

```js
function foo() {
	var a = 1;
	bar(a);
}
function bar(x) {
	console.log(x);
	console.trace();
}

foo();
```

