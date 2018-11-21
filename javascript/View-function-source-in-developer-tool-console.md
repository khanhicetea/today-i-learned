- Date : 2018-11-21
- Tags : #javascript #debug

## View function source in developer tool console

If you are in console of developer tool and you want to know what the function does, you can view its source by: 

1. call `.toSource()` of variable or function name in Firefox

Example :

```js
>> function hello(name) { return "Hello " + name; }

>> hello.toSource();
<- "function hello(name) { return \"Hello \" + name; }"
```

2. click 'show function definition' in Chrome

![show function definition](https://user-images.githubusercontent.com/4528223/48824066-be18b380-ed95-11e8-9bfb-0812b3508f0c.png)

