- Date : 2018-04-24
- Tags : #networking #dns #development

## Setup wildcard domains .test for development in MacOS

Too tired of setting your local domain each time you create new virtual development domain, etc helloworld.test, unit.test point to 127.0.0.1

There is a better way to achieve that by using **dnsmasq**, then set up a wildcard domains for development. In this case I use **.test** because **.dev** has been owned by Google and they strictly use HTTPS in mainly browsers.

Install dnsmasq

```bash
$ brew install dnsmasq
```

Adding .test wildcard to config file

```bash
$ echo 'address=/.test/127.0.0.1' > $(brew --prefix)/etc/dnsmasq.conf
```

Setup dnsmasq as a startup service

```bash
$ sudo brew services start dnsmasq
```

Then add `127.0.0.1` (dnsmasq IP) as first DNS resolver

```
System Preferences > Network > Wi-Fi > Advanced... > DNS > add 127.0.0.1 > move it to top of the list.
```

Checking everything is worked by listing all resolvers

```bash
$ scutil --dns
```

Try it out

```bash
$ nslookup -type=a something.test
$ ping helloworld.test
```

