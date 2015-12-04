- Date : 2015-12-04
- Tags : #python #clone #ref-var


## Reference assign object variable

When you have a object `x` and assign `y = x`, `y` will be a ref of `x` (it looks like pointer of C). So changing property of `y` means changing property of `x`.

Ex :

```python
x = {"a": 1, "b": 2}
y = x
y['a'] = 100
print x['a'] # Result is 100
```

So if you want clone the value, use `copy` lib :

```python
import copy
x = {"a": 1, "b": 2}
y = copy.deepcopy(x)
y['a'] = 100
print x['a'] # Result is 1
```

