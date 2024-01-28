class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        ans = 0
        l = r = -1

        for i in range(len(nums)):
            if nums[i] > right:
               l = r = i
               continue

            if nums[i] >= left:
                r = i 
            ans += (r-l)
        return ans