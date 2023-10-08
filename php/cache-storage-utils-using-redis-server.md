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
            $cached_str = $this->redis->get($key);
            $cached = is_null($cached_str) ? false : unserialize($cached_str);

            if ($cached) {
                return $cached;
            }

            $freshData = $dataFn();
            $this->redis->set($key, serialize($freshData), "ex", $ttl);

            return $freshData;
        } catch (PredisException $e) {
            return $dataFn();
        }
    }
}
```
