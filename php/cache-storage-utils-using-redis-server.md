- Date : 2023-10-08
- Tags : #php #cache #redis

## Cache storage utils using redis server

I created a small util Cache storage using redis server to cache seriable data, it stores **serialzied data string** in text then **unserialize** to wake the data up.

```php
<?php

namespace App\Library;

use Predis\Client;
use Predis\PredisException;

class CacheStorage
{
    public function __construct(private Client $redis)
    {
    }

    public function remember($key, $ttl, $dataFn)
    {
        try {
            $cached = $this->redis->get($key);

            if ($cached) {
                return unserialize($cached);
            }

            $data = $dataFn();
            $this->redis->set($key, serialize($data), "ex", $ttl);

            return $data;
        } catch (PredisException $e) {
            return $dataFn();
        }
    }
}
```
