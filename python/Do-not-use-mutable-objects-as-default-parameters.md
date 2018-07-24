- Date : 2018-07-24
- Tags : #python #function

## Do not use mutable objects as default parameters

I learned this from [learn-python3](https://github.com/jerry-git/learn-python3/blob/master/notebooks/beginner/functions.ipynb)

Example :

```python
def append_if_multiple_of_five(number, magical_list=[]):
    if number % 5 == 0:
        magical_list.append(number)
    return magical_list

print(append_if_multiple_of_five(100))
print(append_if_multiple_of_five(105))
print(append_if_multiple_of_five(123))
print(append_if_multiple_of_five(123, []))
print(append_if_multiple_of_five(123))
```

Result :

```
[100]
[100, 105]
[100, 105]
[]
[100, 105]
```

So default parameters in Python are shared between function calls if it isn't passed from caller. So be careful because shared mutable object can affect your logic between function calls, where MAGIC was born !

One safe way to achieve the goal, use `None` as replacement like this

```python
def append_if_multiple_of_five(number, magical_list=None):
    if not magical_list:
        magical_list = []
    if number % 5 == 0:
        magical_list.append(number)
    return magical_list

print(append_if_multiple_of_five(100))
print(append_if_multiple_of_five(105))
print(append_if_multiple_of_five(123))
print(append_if_multiple_of_five(123, []))
print(append_if_multiple_of_five(123))
```

Result :

```
[100]
[105]
[]
[]
[]
```

