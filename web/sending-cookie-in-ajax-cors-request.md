- Date : 2018-03-01
- Tags : #web #http #browser

## Sending Cookie in AJAX CORs request

By default, browser will remove the cookie and authorization header from AJAX CORs request. So
before sending out the request, make sure `withCredentials` must be true.

In this case, CORs response must specify which origin is allowed (mean
no wildcard allowed origin rule).

