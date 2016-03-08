- Date : 2016-03-08
- Tags : #php #input #post-data


## F-cking stupid limit of input vars

Today, I tried to debug many hours to find out why my POST request missing some data (specify `_token` hidden field). :disappointed:

I tried to config NGINX and PHPFPM max_post_size, client_max_body_size but they still gone. After 2-3 hours searching on Google, I found the link from PHP.net,
it has a config value about limiting max input vars (default = 1000), so it causes the problem about missing data.

So I changed `max_input_vars = 9999` in my `php.ini` and everything works like a charm. :smiley:

At least, I had a luck cos it doesn't run my POST request when missing the CSRF token :grin: My data is save !!!

