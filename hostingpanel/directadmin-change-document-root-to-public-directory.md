- Date : 2022-03-09
- Tags : #hostingpanel #directadmin #hosting #webserver

## DirectAdmin change document root to public directory

By default, the document root of a domain in DirectAdmin (DA) has the format

/home/**[your_username]**/domains/**[your_domain]**/public_html

But in case you have to run modern PHP app like Laravel or Symfony framework (they use child **public** directory as their docroot). In some case, using .htaccess file to rewrite is a hacky way to solve problem (or this is the option when you don't have Admin account of DA)

So, if you have an Admin account, try this

Open menu **Server Manager > Custom HTTPD Configurations**, then click on your domain httpd config file, then click CUSTOMIZE 

In the large textbox, add this line (remind to replace username and domain) to

```text
|?DOCROOT=/home/[your_username]/domains/[your_domain]/public_html/public|
```

Click SAVE to save modification. Then go to Service Monitor and reload your webservers (Nginx, Apache or OpenLiteSpeed)

