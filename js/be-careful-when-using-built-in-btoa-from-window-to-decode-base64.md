- Date : 2023-11-29
- Tags : #js #base64 #encode #decode #web

## Be careful when using built-in btoa from window to decode base64

`window.btoa` is built-in function to encode string to base64 string, but it can't process any Unicode characters (each char must be fit in 1 byte, but Unicode is multi-byte char)

So solution is transform the value to Latin character using some pre-processing function like 

```js
const new_btoa = (val) => btoa(unescape(encodeURIComponent(val)))
const result = new_btoa('Hế lô xin chào')
```

So you have to pair the `atob` too

```js
const new_atob = (val) => decodeURIComponent(escape(atob(val)))
console.log(new_atob(result))
```

Or using 3rd-lib like https://www.npmjs.com/package/js-base64 (I recommend use this way)


