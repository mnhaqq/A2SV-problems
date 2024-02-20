from math import ceil

class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        ans = tt = 0

        for i in range(len(nums)):
            tt += nums[i]
            if nums[i] > ans:
                ans = max(ans, ceil(tt/(i+1)))
        return ans