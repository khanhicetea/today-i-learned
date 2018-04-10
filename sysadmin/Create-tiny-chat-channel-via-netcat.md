- Date : 2018-04-10
- Tags : #sysadmin #trick #messaging

## Create tiny chat channel via netcat

In a network, you can create a tiny chatting channel using netcat. It's lightweight TCP protocol with plain-text transmission, so be carefully on using.

First, create a channel by picking port number (ex: 7777)

```bash
$ sudo nc -l 0.0.0.0 7777
```

Then, tell you friend your IP and channel port. He will use this info to connect the channel

```bash
$ nc 192.168.1.2 7777
```

Finnally, start chatting !! Each message will be send when you press [Enter]

Note: End the session by press `Ctrl + D`

