# coding=utf-8
"""bubble sort(冒泡排序)"""


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def bubble_sort(arr):
    for i in xrange(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)


if __name__ == '__main__':
    arr = [10, 7, 3, 1, 9, 7, 4, 3]
    bubble_sort(arr)
    print arr
