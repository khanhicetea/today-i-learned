- Date : 2017-04-21
- Tags : #http #benchmark #web

## ab failed responses

When benchmarking a HTTP application server using `ab` tool, you shouldn't only care about how many requests per second, but percentage of Success responses.

A notice that you must have the same content-length in responses, because `ab` tool will assume response having different content-length from `Document Length` (in ab result) is failed response.

**Example**

Webserver using Flask

```python
from flask import Flask
from random import randint
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello" * randint(1,3)

if __name__ == "__main__":
    app.run()
```

Benchmark using ab

```bash
$ ab -n 1000 -c 5 http://127.0.0.1:5000/

This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        Werkzeug/0.12.1
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /
Document Length:        10 bytes

Concurrency Level:      5
Time taken for tests:   0.537 seconds
Complete requests:      1000
Failed requests:        683
   (Connect: 0, Receive: 0, Length: 683, Exceptions: 0)
Total transferred:      164620 bytes
HTML transferred:       9965 bytes
Requests per second:    1862.55 [#/sec] (mean)
Time per request:       2.684 [ms] (mean)
Time per request:       0.537 [ms] (mean, across all concurrent requests)
Transfer rate:          299.43 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     1    3   0.7      2      11
Waiting:        1    2   0.6      2      11
Total:          1    3   0.7      3      11
WARNING: The median and mean for the processing time are not within a normal deviation
        These results are probably not that reliable.

Percentage of the requests served within a certain time (ms)
  50%      3
  66%      3
  75%      3
  80%      3
  90%      3
  95%      3
  98%      5
  99%      6
 100%     11 (longest request)
```

**In this example, first response content-length is 10 ("hello"*2), so every responses has content length is 5 or 15, will be assumed a failed response.**
