from bisect import bisect_right as br, bisect_left as bl


# TO-DO: complete the help function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    for i in range(elements):
        if not arrA:
            merged_arr[i] = arrB.pop(0)
        elif not arrB:
            merged_arr[i] = arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA.pop(0)
        elif arrB[0] < arrA[0]:
            merged_arr[i] = arrB.pop(0)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    len_arr = len(arr)
    if len_arr > 1:
        split = len_arr // 2
        left = merge_sort(arr[:split])
        right = merge_sort(arr[split:])
        arr = merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arrA, arrB):
    for x in arrB:
        if x > arrA[-1]:
            arrA += arrB[bl(arrB, x):]
            return arrA
        arrA.insert(br(arrA, x), x)
    return arrA


def merge_sort_in_place(arr, l, r):
    len_arr = r - l
    if len_arr > 1:
        split = len_arr // 2
        arr_l, arr_r = arr[:split], arr[split:]
        left = merge_sort_in_place(arr_l, 0, split)
        right = merge_sort_in_place(arr_r, 0, len(arr_r))
        arr = merge_in_place(left, right)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
