# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # Find the smallest element to the right of arr[i].
        while cur_index < len(arr):
            if arr[cur_index] < arr[smallest_index]:
                smallest_index = cur_index
            cur_index += 1
        # Swap arr[i] with the smallest element.
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap = True
    while swap:
        swap = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swap = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    counter = []
    for i in range(len(arr)):
        if arr[i] < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        if arr[i] > maximum:
            maximum = arr[i]
            counter += [0] * ((maximum + 1) - len(counter))
        counter[arr[i]] += 1
    for i in range(1, len(counter)):
        counter[i] += counter[i - 1]
    counter.insert(0, 0)
    counter.pop()
    new = [0] * len(arr)
    for x in arr:
        new[counter[x]] = x
        counter[x] -= 1
    return new
