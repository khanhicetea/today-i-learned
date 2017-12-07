- Date : 2017-12-07
- Tags : #web #proxy #firewall

## Using web proxy to bypass firewalls

Someday, you will be blocked by a firewall while trying crawling or accessing some website. The reason is they block your IP address from accessing the server.

One solution is using a web proxy (http proxy, socks4 or socks5) to bypass the firewall, by adding the middle-man server between you and target. It's a bit unsecured but you could use for https site only.

Some HTTP Proxy supports https will stream TLS data from target to you (so don't worry about proxy server can read you data). Btw, it only knows which domain and IP address you're connecting.

To find a free proxy from the internet, try this service : https://gimmeproxy.com/

It provides a cool API to fetch new proxy from its database.

Example this endpoint will return JSON response including proxy `anonymous`, `supports HTTPS`, `from Japan` and `minimum speed more than 100KB`

```
http://gimmeproxy.com/api/getProxy?anonymityLevel=1&supportsHttps=false&country=JP&minSpeed=100 
```

In case you need more requests per day, try a subscription (cancelable and refundable). I tried last days, and really like their service (although I cancelled subscription b/c I don't need proxy anymore).

> Break the rules ! ;)

