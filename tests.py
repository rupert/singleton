import copy

from singleton import singleton


@singleton
class C(object):
    pass


def test_singleton():
    a = C()
    b = C()
    assert a is b


def test_init_called_once():
    @singleton
    class Test(object):
        init = 0

        def __init__(self):
            Test.init += 1

    Test()
    Test()

    assert Test.init == 1


def test_multiple_singletons():
    @singleton
    class Test(object):
        pass

    a = C()
    b = Test()

    assert a is not b


def test_copy():
    a = C()
    b = copy.copy(a)

    assert a is b


def test_deepcopy():
    a = C()
    b = copy.deepcopy(a)

    assert a is b
