class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        def dp(idx, summ):
            if idx == len(nums):
                if summ == target:
                    return 1
                else:
                    return 0
            
            state = (idx, summ)
            if state not in memo:
                one = dp(idx+1, summ + nums[idx])
                two = dp(idx+1, summ - nums[idx])
                memo[state] = one + two
            return memo[state]
        
        memo = {}
        return dp(0, 0)