class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k==0:
            return
        nums[:] = nums[-k%len(nums):]+nums[:(len(nums)-k)%len(nums)]