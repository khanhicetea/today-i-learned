- Date : 2023-11-25
- Tags : #laravel #php #tips #web

## Split a Collection items into 2 groups using 1 boolean function

**Old fashion way**

```php
$groupTrue = $groupFalse = [];
foreach ($items as $item) {
	if (some_logic_function($item)) {
		$groupTrue[] = $item;
	} else {
		$groupFalse[] = $item;
	}
}
```

**New way**

```php
list($groupTrue, $groupFalse) = collect($items)
	->partition(fn ($item) => some_logic_function($item))
	->map(fn ($group) => $group->values());
```

**tip:** Using the last *map* then *values* to reset indexing of 2 groups after spliting.

