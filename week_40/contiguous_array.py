class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = dict()
        ans = r_s = 0
        dic[0] = 0
        for i in range(1, len(nums) + 1):
            if nums[i-1] == 1:
                r_s += 1
            else:
                r_s -= 1

            if r_s in dic:
                ans = max(ans, i - dic[r_s])
            else:
                dic[r_s] = i
            
        return ans
