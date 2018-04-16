# coding=utf-8
"""insertion sort(插入排序)"""


def insertion_sort(arr):
    for index in xrange(1, len(arr)):
        current_value = arr[index]
        position = index

        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position = position - 1

        arr[position] = current_value


if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    insertion_sort(arr)
    print(arr)
