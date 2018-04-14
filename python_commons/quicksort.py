# coding=utf-8
"""quick sort"""


def swap(arr, i, j):
    if i != j:
        arr[i], arr[j] = arr[j], arr[i]


def partition(arr, begin, end):
    pivot = begin
    for i in xrange(begin + 1, end + 1):
        if arr[i] <= arr[begin]:
            pivot += 1
            swap(arr, i, pivot)
    swap(arr, begin, pivot)
    return pivot


def quicksort(arr, begin=0, end=None):
    if end is None:
        end = len(arr) - 1

    def _quicksort(arr, begin, end):
        if begin >= end:
            return
        pivot = partition(arr, begin, end)
        _quicksort(arr, begin, pivot - 1)
        _quicksort(arr, pivot + 1, end)

    return _quicksort(arr, begin, end)


array = [97, 200, 100, 101, 211, 107]
quicksort(array)
print array
