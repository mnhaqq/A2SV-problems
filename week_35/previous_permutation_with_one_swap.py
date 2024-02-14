class Solution:
    def prevPermOpt1(self, arr: list[int]) -> list[int]:
        idx = -1
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > arr[i+1]:
                idx = i
                break
        if idx == -1:
            return arr
        
        swap_pos = idx+1
        for i in range(idx+1, len(arr)):
            if arr[idx] > arr[i] and arr[swap_pos] < arr[i]:
                    swap_pos = i
        arr[idx], arr[swap_pos] = arr[swap_pos], arr[idx]
        return arr