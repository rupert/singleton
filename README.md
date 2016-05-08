# Python Singleton

A singleton metaclass for Python. Created for fun, do not use!

```python
from singleton import singleton


@singleton
class C(object):
    pass


a = C()
b = C()

assert a is b
```
