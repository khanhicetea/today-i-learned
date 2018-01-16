- Date : 2018-01-16
- Tags : #linux #networking

## Disable IPv6 to stop getting stuck in network

I know IPv6 will be future for networking, but at this moment "It's suck !" :(

Some service will be failed when trying to connect IPv6 destination :

- apt package manager
- smtp
- curl

So I decided to disable IPv6 on every production server.

```bash
$ echo "net.ipv6.conf.all.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf
$ echo "net.ipv6.conf.default.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf
$ echo "net.ipv6.conf.lo.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf
$ 
$ sudo sysctl -p
```

I will re-enable it when everything works perfectly !

