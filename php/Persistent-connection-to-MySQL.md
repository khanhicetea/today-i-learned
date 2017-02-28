- Date : 2017-02-28
- Tags : #php #mysql #database

## Persistent connection to MySQL

When a PHP process connects to MySQL server, the connection can be persistent if your PHP config has `mysql.allow_persistent` or `mysqli.allow_persistent`. (PDO has the attribute `ATTR_PERSISTENT`)

```php
$dbh = new PDO('DSN', 'KhanhDepZai', 'QuenMatKhauCMNR', array(PDO::ATTR_PERSISTENT => TRUE));
```

## Object destruction

PHP destruct an object automatically when an object lost all its references.

**Example code:**

```php
<?php

$x = null;

function klog($x) {
    echo $x . ' => ';
}

class A {
    private $k;
    function __construct($k) {
        $this->k = $k;
    }

    function b() {
        klog('[b]');
    }

    function __destruct() {
        klog("[{$this->k} has been killed]");
    }
}

function c($k) {
    return new A($k);
}

function d() {
    c('d')->b();
}

function e() {
    global $x;
    $x = c('e');
    $x->b();
    klog('[e]');
}

function f() {
    klog('[f]');
}

d();
e();
f();
```

**Result:**

```
[b] => [d has been killed] => [b] => [e] => [f] => [e has been killed] =>
```

## Reducing PDO persistent connections in PHP long-run process (connect to multiples databases)

Instead of using a service object, we should use a factory design pattern for each job (each connection). PHP will close MySQL connection because it destructs object PDO. Then we can reduce the number of connections to MySQL at a same time.

I learned this case when implement a web-consumer (long-run process) to run database migration for multiples databases.

Before fixing this, our MySQL server had been crashed because of a huge opened connections.

Now, everything works like a charm !

![Bring it on](https://i.giphy.com/mVJojMQvDwixG.gif)
