class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        len_arr = len(arr)
        tmp = -1
        for i in range(len_arr-2, -1, -1):
            prev = arr[i]
            arr[i] = max(tmp, arr[i+1])
            tmp = prev
        arr[-1] = -1
        return arr