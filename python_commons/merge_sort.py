# coding=utf-8
"""merge sort(归并排序)"""


def merge(left, right):
    result = []
    left_length = len(left)
    right_length = len(right)
    i, j = 0, 0
    while i < left_length and j < right_length:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result = result + right[j:] if i == left_length else result + left[i:]
    return result


def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]
    middle = len(arr) / 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)


if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    ret = merge_sort(arr)
    print ret
