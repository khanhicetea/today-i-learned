- Date : 2018-01-10
- Tags : #javascript #web #debug

## Tracking changes of cookie on webpage

Using `Object.defineProperty` helper function as I wrote 3 days ago. We could track the changes of cookie on webpage.

```js
var cookieSetterOrig = document.__lookupSetter__("cookie"); // get origin setter function
var cookieGetterOrig = document.__lookupGetter__("cookie"); // get origin getter function
Object.defineProperty(document, "cookie", {
    get: function () {
	console.trace();
        return cookieGetterOrig.apply(document);
    },
    set: function () {
	console.log(arguments);
	console.trace();
        return cookieSetterOrig.apply(document, arguments);
    },
    configurable: true
});
```

**Notice** : This code only works if cookie is changed by javascript, not http header request !
