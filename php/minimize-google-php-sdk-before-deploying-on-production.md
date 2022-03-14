- Date : 2022-03-14
- Tags : #php #laravel #optimize #composer

## Minimize Google PHP SDK before deploying on production

In case you use `google/apiclient` package to connect to Google API services, remember to cleaning unused services after deploying to production.

So let me show you why

First, lets counting number of classes of Google API services inside composer autoload classmap file (Composer use this file as a mapping to lazyload your needed class)

```bash
$ cat vendor/composer/autoload_classmap.php | grep 'Google' | wc -l
15436
$ du -h vendor/composer/autoload_classmap.php
3.5M    vendor/composer/autoload_classmap.php
```

As you can see, it has almost 15k classes having `Google` in class namespace. And your `autoload_classmap.php` has 3.5Mb in size (so large)

So, let cleaning unused services (by keeping only services you need)

Editing your `composer.json` file by adding `"pre-autoload-dump"` in `scripts` and `"google/apiclient-services"` in `extra`, like below (replace services you need like Drive, Youtube, Sheets, etc..)

```json
{
    "scripts": {
        "pre-autoload-dump": "Google\\Task\\Composer::cleanup"
    },
    "extra": {
        "google/apiclient-services": [
            "Drive",
            "YouTube",
	    "Sheets"
        ]
    }
}
```

Finally, run `composer dump-autoload` again and see the result

```bash
$ cat vendor/composer/autoload_classmap.php | grep 'Google' | wc -l
383
$ du -m vendor/composer/autoload_classmap.php
1.3M    vendor/composer/autoload_classmap.php
```

> Class map reduce from 15k to 400 lines, and size from 3.5M to 1.3M ! Such an optimize !

**Beware : If you add services after cleaning, try to run `rm -r vendor/google/apiclient-services && composer update` to redownloading all services classes.**

