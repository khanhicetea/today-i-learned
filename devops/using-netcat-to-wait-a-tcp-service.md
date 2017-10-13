- Date : 2017-10-13
- Tags : #devops #ci #netcat

## Using netcat to wait a TCP service

When doing a CI/CD testing, you would need to connect a external service (RDBMS, HTTP server or generic TCP server service). So you need waiting the service before running your test app.

One way to do right waiting instead of sleep for a specified time is using `netcat` tool

```bash
$ while ! echo -e '\x04' | nc [service_host] [service_port]; do sleep 1; done;
```

Examples

- MySQL service on port 3306

```bash
$ while ! echo -e '\x04' | nc 127.0.0.1 3306; do sleep 1; done;
$ ./run_test.sh
```

Explanation :

`echo -e '\x04'` will send an EOT (End Of Transmission) to the TCP every second to check if it's ready !

