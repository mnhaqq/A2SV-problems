class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            while nums[i] < len(nums) and nums[i] != i:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)