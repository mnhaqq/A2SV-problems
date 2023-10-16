from ast import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = dict()
        seeker = placeholder = 0

        while seeker < len(nums):
            dic[nums[seeker]] = dic.get(nums[seeker], 0) + 1
            if dic.get(nums[seeker]) <= 2:
                nums[seeker], nums[placeholder] = nums[placeholder], nums[seeker]
                placeholder += 1
            seeker += 1
        return placeholder