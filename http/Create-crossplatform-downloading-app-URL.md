- Date : 2018-01-03
- Tags : #http #mobile #product

## Create cross-platform downloading app URL

You have a mobile app for both platforms iOS and Android, each platform has different download URL. But your user doesn't know which platform he using. Clicking wrong URL will lead to user bounce-rate.

Solution is making only 1 URL to download your app, which can redirect to right place depends on using platform. So how we achieve this ??

The key of problem is detecting user platform, which can be done by extracting the User-Agent header from http request.

| Platform | User-Agent pattern |
| -------- | ------------------ |
| iOS | contains `iPhone` or `iPad` or `iPod` |
| Android | contains `Android` |

This is how I implement using [Caddy web server](https://caddyserver.com/), you can do same thing in Apache or NGINX

```txt
app.yourcompany.com:443 {
    timeouts 1m

    redir 302 {
        if_op or
        if {>User-agent} has iPhone
        if {>User-agent} has iPod
        if {>User-agent} has iPad
	/ [apple-store-url]
    }

    redir 302 {
        if {>User-agent} has Android
	/ [google-play-url]
    }

    redir 302 {
        if {>User-agent} not_has iPhone
        if {>User-agent} not_has iPod
        if {>User-agent} not_has iPad
        if {>User-agent} not_has Android
        / [your-landing-page-which-user-visit-on-desktop-device]
    }
}
```

Then we get cool and easy to remember link, right ?

