# coding=utf-8
"""
input:
    1. 给定一个升序排列的自然数组，eg. [1, 3, 3, 3, 5, 5, 7]
    2. 任意自然数，eg. 3
output:
    数组内值为3区域的左右边界index，eg. f(1) == (0, 0), f(3) == (1, 3)
"""


def binary_search_l(list_, item):
    start, end = 0, len(list_) - 1

    while start <= end:
        mid = (start + end) // 2
        if list_[mid] >= item:
            end = mid - 1
        else:
            start = mid + 1
    if start == len(list_):
        return None
    if list_[start] == item:
        return start


def binary_search_r(list_, item):
    start, end = 0, len(list_) - 1

    while start <= end:
        mid = (start + end) // 2
        if list_[mid] <= item:
            start = mid + 1
        else:
            end = mid - 1
    if end == -1:
        return None
    elif list_[end] == item:
        return end


def range_search(list_, item):
    return binary_search_l(list_, item), binary_search_r(list_, item)


if __name__ == '__main__':
    list_ = [1, 3, 3, 3, 5, 5, 7]
    assert (0, 0) == range_search(list_, 1)
    assert (1, 3) == range_search(list_, 3)
    assert (4, 5) == range_search(list_, 5)
    assert (6, 6) == range_search(list_, 7)
    assert (None, None) == range_search(list_, -1)
    assert (None, None) == range_search(list_, 10)
