- Date : 2017-09-26
- Tags : #sysadmin #bash #shell

## BASH return a value in function

Creating function is a good way to refactor your bash script. But BASH doesn't support returning a value in true way, so it makes a bit of challenge to handle that.

You can use this trick

```bash
hello() {
	echo "Hello $1"
}

hw=$(hello "KhanhIceTea")
echo $hw
```

But what if you want to echo log message in hello function, it will be merged to returned value.

```bash
hello() {
	echo "System is weaking up and brush its teeth :))"
	echo "Hello $1"
}

hw=$(hello "KhanhIceTea")
echo "This is returned value of hello function :"
echo $hw
```

This is a how to resolve it, forwarding log message to stderr instead of stdout by default

```bash
hello() {
	echo "System is weaking up and brush its teeth :))" >&2
	echo "Hello $1"
}

hw=$(hello "KhanhIceTea")
echo "This is returned value of hello function :"
echo $hw
```

> Where there is a shell, there is a way !

