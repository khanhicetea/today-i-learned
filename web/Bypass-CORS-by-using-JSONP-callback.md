- Date : 2018-01-08
- Tags : #web #javascript #jsonp

## Bypass CORS by using JSONP callback

Sometimes you are blocked from request a cross-origin resource. Instead of adding our domain to allowed list of them, we can use another way to retrieve data from their API by using JSONP (in case they support it).

The mechanism of JSONP is simple, instead of returning a JSON data. It will return a javascript text with passing your data into a function, whose name is declared in query string. So you just add a new script element with the URL and waiting the callback.

Example :

```js
function callMeBaby(data) {
	console.log(data);
}

var s = document.createElement("script");
s.type = "text/javascript";
s.src = "https://freegeoip.net/json/?callback=callMeBaby";
document.head.appendChild(s);
```

or using jQuery (hide magic)

```js
$.ajax({
    url: "https://freegeoip.net/json/",
    jsonp: "callback",
    dataType: "jsonp",
    success: function( data ) {
        console.log( data );
    }
});
```

