class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        def dp(idx):
            if idx < 2:
                arr[idx] = idx
                return idx
            
            if arr[idx] == -1:
                if idx % 2 == 0:
                    arr[idx] = dp(idx//2)
                else:
                    arr[idx] = dp((idx-1)//2) + dp((idx-1)//2 + 1)
            return arr[idx]

        arr = [-1] * (n+1)
        for i in range(n, -1, -1):
            dp(i)
        return max(arr)