class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        n = len(nums)

        res = []
        i = 0
        while i < n:
            if nums[i] != (i + 1) and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != (i+1):
                res.append(nums[i])
        return res