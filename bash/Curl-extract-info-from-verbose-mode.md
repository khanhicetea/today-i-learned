- Date : 2018-08-07
- Tags : #bash #curl

## Curl extract info from verbose mode

Curl is great tool to do thing with HTTP in command line interface. Sometimes your want to get extra info from HTTP response and put in a variable. Here is the way :

Using `--write-out` is magical option help you to write out all info you want, or put it in a variable.

Example :

```bash
$ code=$(curl --write-out %{response_code} --silent --output /dev/null https://khanhicetea.com)
$ echo $code # get http response status code
200
```

```bash
$ tracetime=$(curl --write-out "%{time_namelookup} %{time_connect} %{time_appconnect} %{time_pretransfer} %{time_redirect} %{time_starttransfer} %{time_total}" --silent --output /dev/null https://khanhicetea.com)
$ echo $tracetime # Trace all timing of http connection (in seconds)
0.068 0.097 0.370 0.370 0.000 0.720 0.721
```

Use case :

Below code is cron bash script that checks if http response code equals :
- 502 (Bad Gateway), then restart the backend server (nginx -> apache2)
- not 200 then restart the frontend server (nginx)

```bash
#!/bin/bash

code=$(curl --write-out %{response_code} --silent --output /dev/null http://example.com)
[ $code -eq 502 ] && sudo systemctl restart httpd || echo "everything works fine"
[ ! $code -eq 200 ] && sudo systemctl restart nginx || echo "everything works fine"
```

More info variables, you can check it [here](https://ec.haxx.se/usingcurl-verbose.html)

