- Date : 2018-08-18
- Tags : #sysadmin #curl #dns

## Curl override Name Resolution with specific IP address

You can overrride the Name Resolution with specific IP address without adding the hostname to /etc/hosts file by using `--resolve` option.

Syntax :

```bash
--resolve <host:port:address>
```

It will resolve IP **address** when connect to **host** on **port**


Example :

This will connect **127.0.0.1**

```bash
$ curl --resolve google.com:80:127.0.0.1 "http://google.com/"
```

But this won't connect **127.0.0.1**, because we use 443 port for https

```bash
$ curl --resolve google.com:80:127.0.0.1 "https://google.com/"
```

For cover all ports, use `*` wildcard

```bash
$ curl --resolve google.com:*:127.0.0.1 "https://google.com/"
```

