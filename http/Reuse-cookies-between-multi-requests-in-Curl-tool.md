- Date : 2018-05-22
- Tags : #http #curl #cookie

## Reuse cookies between multi requests in Curl tool

Curl is good lib and tool to simulate HTTP requests. One common usecase is reusing the cookies between 2 or more requests. So you don't have to copied last "Set-Cookie" of previous response then paste it to "Cookie" of next request.

To achieve that, you have to use a cookie jar (sounds fun) to store cookies then use that cookie jar in next request. We have two parameters :

**-c [cookie_jar_file]** : store response cookies in a file

**-b [cookie_jar_file]** : getting cookies from cookie jar file then send it in request

Combine them together we can simulate a real browser HTTP requests easily.

Example :

```bash
$ curl -c cookies.txt -b cookies.txt -XPOST -d "user=admin&password=hahahehe" http://example.com/login
......
$ curl -c cookies.txt -b cookies.txt -XGET http://example.com/dashboard
Hello admin !
```

