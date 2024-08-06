- Date : 2024-08-06
- Tags : php web programing

## PHP memory allocation when passing arguments into function

In PHP, when you pass variables into another function arguments, it

1. Copy the variable memory if the argument is scalar data type (int, float, bool, ...), because it's cheap operations
2. Copy a `shadow clone jutsu` variable zval struct (24-32 bytes), then point the real data pointer of dynamically data type (array, string, $object)

Below testing will say more than me

```php
<?php

class A {
  public $arr;
  public function __construct() {
    $this->arr = array_fill(0, 10000, "Hello world");
  }

  public function push(){
    $this->arr[] = "ok";
  }
}

function haha() {
  $a = func_get_args()[0];
  mem("inside func haha, after func_get_args");
  return $a;
}

function a($b, $c) {
  $a = new A();
  $str = str_repeat("Helo", 100000);
  mem("after create an object A");
  $x = haha($a, $str, $b, $c);
  mem("after call func_get_args");
  $x->arr[] = "there";
  var_dump($a->arr[count($a->arr) - 1]);
  var_dump($x->arr[count($x->arr) - 1]);
  $x->push();
  var_dump($a->arr[count($a->arr) - 1]);
  var_dump($x->arr[count($x->arr) - 1]);
  mem("after modify arr property");
  // var_dump($a === $x);
  return $b+$c;
}

function mem($msg = null) {
  if ($msg) print_r($msg . " : ");
  echo (memory_get_usage(false) . " bytes\n");
}

mem("start");
var_dump(a(1,2));
mem("end");
```

This is the result

```shell
start : 469464 bytes
after create an object A : 1137200 bytes
inside func haha, after func_get_args : 1137200 bytes
after call func_get_args : 1137200 bytes
string(5) "there"
string(5) "there"
string(2) "ok"
string(2) "ok"
after modify arr property : 1137200 bytes
int(3)
end : 469464 bytes
```

Surprise ! :D

