class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        def dp(idx, target):
            if idx >= len(nums) or target <= 0:
                return target == 0
            
            state = (idx, target)
            if state not in memo:
                memo[state] = dp(idx+1, target-nums[idx]) or dp(idx+1, target)
            return memo[state]
        
        memo = {}
        return sum(nums) % 2 == 0 and dp(0, sum(nums)//2)