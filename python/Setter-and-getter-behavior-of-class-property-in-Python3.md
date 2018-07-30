- Date : 2018-07-30
- Tags : #python #pythonic

## Setter and getter behavior of class property in Python3

In previous TIL, I learned about the way to [define getter and setter in Javascript](/til/2018-01-07-define-property-of-an-object-in-hacking-way/)

Today, I learned it in Pythonic way ;) (in Python3)

So here is example (the easy way to learn from a code) :

```python
class A:
    def __init__(self,x):
        print ('init', x)
        self.x = x

    @property
    def x(self):
        print ('getter')
        return self.__x

    @x.setter
    def x(self, x):
        print ('setter', x)
        if x < 0:
            self.__x = 0
        elif x % 2 == 0:
            self.__x = x
        else:
            self.__x = x * 2

a = A(10)
print(a.x)
a.x = -1
print(a.x)
a.x = 2
print(a.x)
a.x = 7
print(a.x)
```

This is so cool feature, and even it has `deleter` property method, which triggers when we run `del object.property` :D

In reactive JS framework that they use getter and setter like a core of Reactive, let find out more next articles ;)

