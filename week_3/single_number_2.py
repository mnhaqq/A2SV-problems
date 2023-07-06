class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = list(set(nums))
        for i in range(len(unique)):
            if nums.count(unique[i]) == 1:
                return unique[i]