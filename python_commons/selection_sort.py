# coding=utf-8
"""selection sort(选择排序)"""


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def selection_sort(arr):
    length = len(arr)
    for i in xrange(length):
        small = arr[i]
        pos = None
        for j in xrange(i + 1, length):
            if arr[j] < small:
                small = arr[j]
                pos = j
        if pos:
            swap(arr, i, pos)


if __name__ == '__main__':
    arr = [10, 7, 3, 1, 9, 7, 4, 3]
    selection_sort(arr)
    print(arr)
