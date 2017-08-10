- Date : 2017-08-08
- Tags : #web #google

## Ping Google to crawl updated content

When you post new content to your website, the fastest way is ping search engines to notify them. After that, they will try to crawl and index your page.

One way to ping search engines is using XMLRPC ping

This is a example XMLRPC request (HTTP POST request with xml body)

**Request**

```http
> POST /ping/RPC2 HTTP/1.1
> Host: blogsearch.google.com
> User-Agent: curl/7.47.0
> Accept: */*
> content-type: application/xml
> Content-Length: 239
> 
<?xml version="1.0" encoding="UTF-8"?>
<methodCall>
   <methodName>weblogUpdates.extendedPing</methodName>
   <params>
      <param>
         <value>Page Title</value>
      </param>
      <param>
         <value>http://example.com/helloworld.html</value>
      </param>
   </params>
</methodCall>
```

**Response**

```http
< HTTP/1.1 200 OK
< Content-Type: text/xml; charset=ISO-8859-1
< X-Content-Type-Options: nosniff
< Date: Tue, 08 Aug 2017 05:04:01 GMT
< Server: psfe
< Cache-Control: private
< X-XSS-Protection: 1; mode=block
< X-Frame-Options: SAMEORIGIN
< Accept-Ranges: none
< Vary: Accept-Encoding
< Transfer-Encoding: chunked
< 
<?xml version="1.0"?>
<methodResponse><params>
  <param><value><struct>
    <member>
      <name>flerror</name><value><boolean>0</boolean></value>
    </member>
    <member>
      <name>message</name><value>Thanks for the ping.</value>
    </member>
  </struct></value></param>
</params></methodResponse>
```

Popular XML Servers

```
http://blogsearch.google.com/ping/RPC2
http://api.moreover.com/ping
http://bblog.com/ping.php
http://bitacoras.net/ping
http://blog.goo.ne.jp/XMLRPC
http://blogmatcher.com/u.php
http://coreblog.org/ping/
http://mod-pubsub.org/kn_apps/blogchatt
http://www.lasermemory.com/lsrpc/
http://ping.amagle.com/
http://ping.cocolog-nifty.com/xmlrpc
http://ping.exblog.jp/xmlrpc
http://ping.feedburner.com
http://ping.myblog.jp
http://ping.rootblog.com/rpc.php
http://ping.syndic8.com/xmlrpc.php
http://ping.weblogalot.com/rpc.php
http://pingoat.com/goat/RPC2
http://rcs.datashed.net/RPC2/
http://rpc.blogrolling.com/pinger/
http://rpc.pingomatic.com
http://rpc.technorati.com/rpc/ping
http://rpc.weblogs.com/RPC2
http://www.blogpeople.net/servlet/weblogUpdates
http://www.blogroots.com/tb_populi.blog?id=1
http://www.blogshares.com/rpc.php
http://www.blogsnow.com/ping
http://www.blogstreet.com/xrbin/xmlrpc.cgi
http://xping.pubsub.com/ping/
```

