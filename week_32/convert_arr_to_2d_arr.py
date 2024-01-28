from collections import defaultdict

class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        ans = []
        dic = defaultdict(int)

        for i in range(len(nums)):
            dic[nums[i]] += 1
            if dic[nums[i]] > len(ans):
                ans.append([nums[i]])
            else:
                ans[dic[nums[i]]-1].append(nums[i])
        return ans 