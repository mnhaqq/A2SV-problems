class Solution:
    def rob(self, nums: list[int]) -> int:
        def dp(idx):
            if idx >= len(nums):
                return 0
            if idx not in memo:
                memo[idx] = max(dp(idx+1), dp(idx+2) + nums[idx])
            return memo[idx]
        
        memo = {}
        return dp(0)