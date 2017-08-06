- Date : 2017-08-06
- Tags : #php #mistake

## realpath function

If you pass a non-exists path to function `realpath`, it returns empty string. So please don't do something like :

```php
function storage_path($folder) {
	return realpath(__DIR__.'/storage/'.$folder);
}
```

if you expect it return full path of new folder !
