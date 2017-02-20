# coding: utf-8
"""
some decorator examples
"""
import functools

def first_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'first_decorator'
        return func(*args, **kw)
    return wrapper

def second_decorator(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print text
            print 'second_decorator'
            return func(*args, **kw)
        return wrapper
    return decorator

@first_decorator
def test_first(name):
    return name

@second_decorator('testing...')
def test_second(name):
    return name

if __name__ == '__main__':
    print test_first.__name__
    print test_first('zhujiongyao')
    print test_second.__name__
    print test_second('zhujiongyao')