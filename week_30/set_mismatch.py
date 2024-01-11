class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)

        i = 0
        while i < n:
            if nums[i] != (i + 1) and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1  
        
        res = []
        for i in range(len(nums)):
            if nums[i] != (i+1):
                res.append(nums[i])
                res.append(i+1)
        return res