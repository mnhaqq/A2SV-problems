class Solution:
    def rob(self, nums: list[int]) -> int:
        def dp(idx, first):
            if idx >= len(nums):
                return 0
            if idx == len(nums) - 1:
                if first:
                    return 0
                return nums[idx]
            
            if idx == len(nums) - 2:
                if first:
                    return nums[idx]
                return max(nums[idx], nums[idx+1])
            
            state = (idx, first)
            if state not in memo:
                memo[state] = max(dp(idx+1, first), dp(idx+2, first) + nums[idx])
            return memo[state]
        
        memo = {}
        return max(nums[0] + dp(2, True), dp(1, False))