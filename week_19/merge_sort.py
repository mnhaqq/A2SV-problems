def merge(arr1, arr2):
    p1 = p2 = 0
    arr = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] <= arr2[p2]:
            arr.append(arr1[p1])
            p1 += 1
        else:
            arr.append(arr2[p2])
            p2 += 1
 
    arr.extend(arr1[p1:])
    arr.extend(arr2[p2:])
    return arr

def sort(arr):
    if len(arr) <= 1:
        return arr[:]
    
    arr1 = sort(arr[:len(arr)//2])
    arr2 = sort(arr[len(arr)//2:])

    return merge(arr1, arr2)

arr = [5, 1, 3]
ans = sort(arr)
print(ans)