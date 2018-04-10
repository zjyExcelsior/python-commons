# coding=utf-8
"""
input:
    1. 给定一个升序排列的自然数组，eg. [1, 3, 3, 3, 5, 5, 7]
    2. 任意自然数，eg. 3
output:
    数组内值为3区域的左右边界index，eg. f(1) == (0, 0), f(3) == (1, 3)
"""


def binary_search_index(list_, item, is_left=True):
    left, right = 0, len(list_) - 1
    pos = None
    while left <= right:
        mid = (left + right) // 2
        if list_[mid] < item:
            left = mid + 1
        elif list_[mid] > item:
            right = mid - 1
        else:
            pos = mid
            if is_left:  # 查找最左值
                right = mid - 1
            else:  # 查找最右值
                left = mid + 1
    return pos


def range_search(list_, item):
    return (binary_search_index(list_, item),
            binary_search_index(list_, item, False))


if __name__ == '__main__':
    list_ = [1, 3, 3, 3, 5, 5, 7]
    assert (0, 0) == range_search(list_, 1)
    assert (1, 3) == range_search(list_, 3)
    assert (4, 5) == range_search(list_, 5)
    assert (6, 6) == range_search(list_, 7)
    assert (None, None) == range_search(list_, -1)
    assert (None, None) == range_search(list_, 10)
