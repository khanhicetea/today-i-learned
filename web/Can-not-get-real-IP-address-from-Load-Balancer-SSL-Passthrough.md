- Date : 2019-03-14
- Tags : #web #loadbalancer #ssl

## Can not get real IP address from Load Balancer SSL Passthrough

When you use a load balancer stay in front of your app, and use SSL Passthrough mode. You will never get real IP of client, because Load balancer works like a TCP load balancer, which means it can not add extra HTTP headers into encrypted traffic from client when it doesn't handle SSL termination.

So if you use 1 domain or wildcard subdomains, it's better if you use SSL Termination mode.

