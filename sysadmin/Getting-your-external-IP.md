- Date : 2017-11-24
- Tags : #sysadmin #dns #ip

## Getting your external IP

We can get our external IP address by following ways :

1. Call http request : `curl http://wtfismyip.com/text` or `curl http://ifconfig.me/ip`
2. Lookup A record for hostname `nslookup myip.opendns.com resolver1.opendns.com` (this only works when you use resolver of OpenDNS)

**Bonus** : `curl https://v6.ident.me/` for IPv6

