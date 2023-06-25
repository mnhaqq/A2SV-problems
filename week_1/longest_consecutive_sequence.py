class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        current = maximum = i = 1
        while i < len(nums):
            if nums[i-1] != nums[i]:
                if nums[i-1] + 1 == nums[i]:
                    current+=1
                else:
                    maximum = max(maximum, current)
                    current = 1
            i+=1

        return max(maximum, current)