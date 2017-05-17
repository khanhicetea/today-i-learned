- Date : 2015-12-04
- Tags : #sysadmin #websocket #log


## View real-time logs using websocketd

I found a handy tool for making a websocket right on your shell.
It is **websocketd** : http://websocketd.com/

Its phisolophy is so simple :
> Just read incoming text from stdin and write outgoing text to stdout. Messaging is simple.

Read its docs, I follow the ez tutorial `10 second tutorial` and see how cool does it work.
Let make something cool with this, we got a UNIX tool that print out to `stdout` in real-time with changes of end file.

Ok cool, change the command to
```bash
websocketd --port=8080 tail -f logs/web_access.log
```

Tada ! Open the webpage that listens the websocket you made and see the magic :D You can tracking access log of website or system in real-time way.
