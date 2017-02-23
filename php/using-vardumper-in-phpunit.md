- Date : 2017-02-23
- Tags : #php #phpunit #testing #english

## Using VarDumper in PHPUnit

The trick is writing the output to STDERR stream, I wrote a helper function below

```php
function phpunit_dump() {
    $cloner = new \Symfony\Component\VarDumper\Cloner\VarCloner();
    $dumper = new \Symfony\Component\VarDumper\Dumper\CliDumper(STDERR);
    foreach (func_get_args() as $var) {
        $dumper->dump($cloner->cloneVar($var));
    }
}
```

How to use it ?

```php
// Something magic here :D

phpunit_dump($magic_var1, $magic_var2, $magic_of_magic);

// So much magic below, can't understand anymore
```

![Magic](http://i.giphy.com/12NUbkX6p4xOO4.gif)
