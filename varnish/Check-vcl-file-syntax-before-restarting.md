- Date : 2018-01-31
- Tags : #varnish

## Check vcl file syntax before restarting

Like NginX, Varnish has a syntax checker function that helps us test the syntactic correctness.

```bash
$ varnishd -C -f [vcl file path]
```

Varnish will compile the file and output the result to stdout. If something goes wrong, it will throw a message like

```
> Message from VCC-compiler:
> Expected an action, 'if', '{' or '}'
> ('input' Line 74 Pos 6)
>     vcl_hash(req.http.Cookie);
> -----########------------------
>
> Running VCC-compiler failed, exit 1
```

