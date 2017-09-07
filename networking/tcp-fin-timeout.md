- Date : 2017-09-07
- Tags : #networking

## TCP FIN timeout

The TCP FIN timeout belays the amount of time a port must be inactive before it can reused for another connection. The default is often 60 seconds, but can normally be safely reduced to 30 or even 15 seconds:

```
net.ipv4.tcp_fin_timeout = 15
```

Ref : https://www.linode.com/docs/web-servers/nginx/configure-nginx-for-optimized-performance
