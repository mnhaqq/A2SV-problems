class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = l = 0
        window = 1

        for r in range(len(nums)):
            window *= nums[r]

            while l <= r and window >= k:
                window //= nums[l]
                l += 1
            
            ans += r - l + 1
        
        return ans
