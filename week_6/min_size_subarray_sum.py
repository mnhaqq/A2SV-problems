class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        min_len=float("inf")
        l=0
        subarr_sum=0
        for r in range(n):
            subarr_sum+=nums[r]
            while subarr_sum>=target:
                min_len=min(min_len,r-l+1)
                subarr_sum-=nums[l]
                l+=1
        if min_len==float("inf"):
            min_len=0
        return min_len
