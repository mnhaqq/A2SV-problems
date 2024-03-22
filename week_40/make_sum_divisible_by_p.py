class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:        
        p_s = [0] * (len(nums) + 1)
        for i in range(1, len(p_s)):
            p_s[i] = (p_s[i-1] + nums[i-1])
        
        target = p_s[-1] % p
        if target == 0:
            return 0

        dic = dict()
        ans = len(nums)
        for i in range(len(p_s)):
            curr = p_s[i] % p
            if ((curr - target) % p) in dic:
                ans = min(ans, i - dic[(curr-target) % p])
            dic[curr]= i
        
        if ans >= len(nums):
            return -1
        return ans
