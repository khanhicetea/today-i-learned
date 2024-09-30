- Date : 2024-09-30
- Tags : #js #alpinejs #javascript #web

## Run multiple AlpineJS inits and effects on same element

This trick allows you to run multiple init and effects using AlpineJS on same element

```html
<div
       x-init
       x-init.1="console.log('click 1, a = ' + a)"
       x-init.2="console.log('click 2, b = ' + b)"
       x-effect.1="console.log('a is changed')"
       @click="a = 100"
       x-data.1='{"a":1, "b":3}'
       x-data.2='{"b":2}'
       x-text="'a = ' + a + ' , b = ' + b"
  >
          Hello world
</div>
```

Check this demo on JSBin : https://jsbin.com/vetunuhade/edit?html,js,console,output
