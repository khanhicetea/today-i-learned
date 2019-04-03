- Date : 2019-04-03
- Tags : #networking #nginx #loadbalancer

## Use NGINX as a TCP,UDP load balancer

NGINX is well known as a simple and good web server right now, but not everyone knows that NGINX can act like a TCP-UDP loadbalancer. So you won't need to install HAProxy when you need a LoadBalancer.

This feature is released on NGINX 1.9+. So you can setup it by this rule

```
stream {
	upstream backend1 {
		server s1.backend1.com:12345;
		server s2.backend1.com:12345;
	}
	server {
		listen 54321;
		proxy_pass backend1;
	}
	upstream backend2 {
		server s1.backend2.com:7777;
		server s2.backend2.com:7777;
		server s3.backend2.com:7777;
	}
	server {
		listen 8888 udp; # add udp keyword if you want UDP server
		proxy_pass backend2;
	}
}
```

To learn more, click here : https://docs.nginx.com/nginx/admin-guide/load-balancer/tcp-udp-load-balancer/

