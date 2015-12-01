- Date : 2015-12-01
- Tags : #python #string #unicode


## String Format Unicode params

```python
unicode_thing = u"Xin chào mọi người"
a = '{}'.format(unicode_thing)
```
will cause the error `UnicodeEncodeError: 'ascii' codec can't encode character u'\xe0' in position 6: ordinal not in range(128)`

The solution is add `u` prefix the pattern (it means using unicode pattern) :

```python
unicode_thing = u"Xin chào mọi người"
a = u'{}'.format(unicode_thing)
```

