class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = list(str(num))
        
        ans = num
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                arr[i], arr[j] = arr[j], arr[i]
                ans = max(ans, int("".join(arr)))
                arr[i], arr[j] = arr[j], arr[i]

        return ans
        