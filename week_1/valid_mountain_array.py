class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        max_index = arr.index(max(arr))

        if max_index == 0 or max_index == len(arr)-1:
            return False

        for i in range(max_index):
            if arr[i+1] <= arr[i]:
                return False

        for i in range(max_index, len(arr)-1):
            if arr[i+1] >= arr[i]:
                return False
        return True