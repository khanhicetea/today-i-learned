- Date : 2015-12-04
- Tags : #php #docker #cli-server


## Run built-in server via Docker

Docker is the fast and clean way to run Linux programs.

We can run a PHP project via PHP built-in server and Docker.

```bash
docker run -it -p 8080:8080 -v `pwd`:/code php:7 php -S 0.0.0.0:8080 -t /code/web /code/web/server.php
```

With `server.php` content is

```php
<?php

$filename = __DIR__.preg_replace('#(\?.*)$#', '', $_SERVER['REQUEST_URI']);
if (php_sapi_name() === 'cli-server' && is_file($filename)) {
    return false;

}

// Run application below
$app = new Application();
$app->run();
```

