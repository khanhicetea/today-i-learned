- Date : 2018-04-24
- Tags : #networking #dns #development

## Setup wildcard domains .local for development in MacOS

Too tired of setting your local domain each time you create new virtual development domain, etc helloworld.local, test.local point to 127.0.0.1

There is a better way to achieve that by using **dnsmasq**, then set up a wildcard domains for development. In this case I use **.local** because **.dev** has been owned by Google and they strictly use HTTPS in mainly browsers.

Install dnsmasq

```bash
$ brew install dnsmasq
```

Adding .local wildcard to config file

```bash
$ echo 'address=/.local/127.0.0.1' > $(brew --prefix)/etc/dnsmasq.conf
```

Setup dnsmasq as a startup service

```bash
$ sudo brew services start dnsmasq
```

Then add `127.0.0.1` (dnsmasq IP) as first DNS resolver

```
System Preferences > Network > Wi-Fi > Advanced... > DNS > add 127.0.0.1 > move it to top of the list.
```

Try it out

```bash
$ nslookup -type=a something.local
$ ping helloworld.local
```

