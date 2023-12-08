- Date : 2023-12-08
- Tags : #php #web

## Transform array to object shorthand

To transform a array to stdClass in PHP, try to cast type using `(object)` before the array variable.

```php
$arr = ['a' => 1, 'b' => 5];
$obj = (object) $arr;
echo $obj->b;
```

