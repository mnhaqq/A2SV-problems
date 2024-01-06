## Implementation 1
def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        if arr[i] != (i + 1):
            idx = arr[i]-1
            arr[i], arr[idx] = arr[idx], arr[i]
        else:
            i += 1
    return arr

## Implementation 2
def cyclic_sort_2(arr):
    for i in range(len(arr)):
        while arr[i] != (i + 1):
            idx = arr[i] - 1
            arr[i], arr[idx] = arr[idx], arr[i]
    return arr