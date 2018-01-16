- Date : 2018-01-16
- Tags : #networking #firewall #security

## Set up simple rate limiting on specified port using UFW

Allow unmetrered connections on networking is so risky. Attacker can use the brute-force attacks to comprosise your service (or simple DOS).

Linux has a cool firewall to hanlde this, via `ip-tables`. But it's so complicated to remember all the rule and syntax. That's why `UFW` was born to save us. :D

You can use simple command to manage your firewall

```bash
$ ufw default deny incoming # deny any incoming port, should be run before allow any port
$ ufw default allow outgoing # allow any outgoing port
$ ufw allow 80 # allow port 80
$ ufw deny 53/udp # allow udp protocol to port 53
$ ufw disable # disable firewall
$ ufw enable # enable firewall
$ ufw status # check all the rules
$ ufw delete [num] # delete the rule by its order in status result
$ ufw reload # reload all rule
$ ufw limit ssh/tcp # finnaly, limit ssh (port 22 tcp), deny connections if an IP address has attempted to initiate 6 or more connections in the last 30 seconds
```

