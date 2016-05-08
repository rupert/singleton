import six


class Singleton(type):
    def __new__(cls, name, bases, attrs):
        def __copy__(self):
            return self

        def __deepcopy__(self, memo):
            return self

        attrs['__copy__'] = __copy__
        attrs['__deepcopy__'] = __deepcopy__

        return super(Singleton, cls).__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        super(Singleton, cls).__init__(name, bases, attrs)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)

        return cls.instance


def singleton(cls):
    return six.add_metaclass(Singleton)(cls)
