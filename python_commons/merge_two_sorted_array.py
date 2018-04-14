# coding=utf-8
"""合并两个有序数组为一个有序数组"""


def merge_two_sorted_array(arr1, arr2):
    arr1_length = len(arr1)
    arr2_length = len(arr2)
    ret = []
    i, j = 0, 0
    while i < arr1_length and j < arr2_length:
        if arr1[i] <= arr2[j]:
            ret.append(arr1[i])
            i += 1
        else:
            ret.append(arr2[j])
            j += 1
    ret = ret + arr2[j:] if i == arr1_length else ret + arr1[i:]
    return ret


if __name__ == '__main__':
    arr1 = [1, 4, 6]
    arr2 = [4, 5]
    ret = merge_two_sorted_array(arr1, arr2)
    print(ret)
