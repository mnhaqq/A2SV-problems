from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        num_distinct = len(set(nums))
        dic = dict()
        count = l = 0
        for r in range(len(nums)):
            dic[nums[r]] = dic.get(nums[r], 0) + 1
            while len(dic) == num_distinct:
                count += len(nums) -r
                dic[nums[l]] -= 1
                if dic[nums[l]] == 0:
                    del dic[nums[l]]
                l += 1
        return count