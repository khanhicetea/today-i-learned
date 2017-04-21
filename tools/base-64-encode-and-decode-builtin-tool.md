- Date : 2017-04-21
- Tags : #tools #encoding #web

## Base 64 encode and decode builtin tool

Browsers have helpers function to encode and decode base64 :

- `btoa` : base64 encode
- `atob` : base64 decode

```
> btoa('Hello world')
"SGVsbG8gV29ybGQgIQ=="

> atob('SW4gR29kIFdlIFRydXN0ICE=')
"In God We Trust !"
```
