- Date : 2018-11-21
- Tags : #javascript #debug

## View function source in developer tool console

If you are in console of developer tool and you want to know what the function does, you can view its source by call `.toSource()` of variable or function name.

Example :

```js
>> function hello(name) { return "Hello " + name; }

>> hello.toSource();
<- function hello(name) { return "Hello " + name; }
```

