class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        indices = dict()

        dp = [1] * len(arr)
        indices[arr[0]] = 0

        for i in range(1, len(arr)):
            if (arr[i] - difference) in indices:
                idx = indices[(arr[i] - difference)]
                dp[i] = dp[idx] + 1
            indices[arr[i]] = i
            
        return max(dp)