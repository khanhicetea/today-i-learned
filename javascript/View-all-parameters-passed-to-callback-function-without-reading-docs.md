- Date : 2018-10-30
- Tags : #javascript #debug

## View all parameters passed to callback function without reading docs

Time before, I often meet the situation that I forgot the parameters pass to a function (so I have to searching the API docs to read via Google). This progress can take you huge time if it repeats many times.

So I think one way to debug the parameters without reading API docs, that is pass `console.log` as a callback function parameter.

Examples :

```js
[3,9,27].forEach(console.log);
// So you will get
// 3 0
// 9 1
// 27 2
// Then you know , first parameter is item, second parameter is indexed key
```

```js
jQuery.ajax('/data.json').done(console.log).fail(console.error);
```

