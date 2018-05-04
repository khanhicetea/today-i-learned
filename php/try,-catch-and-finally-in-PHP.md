- Date : 2018-05-04
- Tags : #php

## try, catch and finally in PHP

We have to deal with exceptions every moment we touch PHP web development, and so please be carefully with running order of exception catching.

Here is an example

```php
<?php

function a() {
	try {
		throw new Exception('dsads');
	} catch (Exception $e) {
		return 'b';
	} finally {
		echo 'c';
	}
}

echo a();
```

Then the output is

```
cb
```

Than mean even `return 'b';` runs, the **finally code** must be runned before function result passes out.

