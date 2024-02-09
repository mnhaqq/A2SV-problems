class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        l = 0
        for r in range(1, len(nums)):
            while l < r and nums[l] % 2 == 0:
                l += 1
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
        return nums