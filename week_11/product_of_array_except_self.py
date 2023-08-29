class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums)
        suffix_product = [1] * len(nums)
        for i in range(len(nums)-1):
            prefix_product[i+1] = prefix_product[i] * nums[i]
        for i in range(len(nums)-1, 0, -1):
            suffix_product[i-1] = suffix_product[i] * nums[i]
        ans = [0]*len(nums)
        for i in range(len(ans)):
            ans[i] = suffix_product[i] * prefix_product[i]
        return ans