# coding=utf-8
"""斐波那契数

0, 1, 1, 2, 3, 5, 8, 13, 21, ...
"""


def fibo(n):
    """返回斐波那契数

    f(0) = 0
    f(1) = 1
    f(n) = f(n-1) + f(n-2) (n>=2)
    """
    a, b = 0, 1
    for _ in xrange(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    assert fibo(0) == 0
    assert fibo(1) == 1
    assert fibo(2) == 1
    assert fibo(3) == 2
    assert fibo(4) == 3
    assert fibo(5) == 5
    assert fibo(6) == 8
    assert fibo(7) == 13
