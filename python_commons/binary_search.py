# coding=utf-8
"""二分查找算法"""


def binary_search(list_, item):
    """二分查找(非递归方式)"""
    start, end = 0, len(list_) - 1
    while start <= end:
        mid = (start + end) // 2
        if list_[mid] == item:
            return True
        elif item < list_[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False


def binary_search2(list_, item):
    """二分查找(递归方式)"""
    start, end = 0, len(list_) - 1
    if start > end:
        return False
    mid = (start + end) // 2
    if list_[mid] == item:
        return True
    elif item < list_[mid]:
        return binary_search2(list_[:mid], item)
    else:
        return binary_search2(list_[mid + 1:], item)


if __name__ == '__main__':
    list_ = [1, 2, 3, 4, 5, 6]
    assert False is binary_search(list_, 0)
    assert False is binary_search2(list_, 0)
    assert False is binary_search(list_, 10)
    assert False is binary_search2(list_, 10)
    for i in xrange(1, 7):
        assert True is binary_search(list_, i)
        assert True is binary_search2(list_, i)
