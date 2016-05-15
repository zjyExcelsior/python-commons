# coding: utf-8
'''
Some methods about functools
'''
from functools import partial

def func1(a, b):
    return a, b

func2 = partial(func1, 1)

if __name__ == '__main__':
    ret = func2(2)
    print ret