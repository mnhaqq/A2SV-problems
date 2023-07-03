class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = [0] * (max(nums)+1)
        for i in range(len(nums)):
            counter[nums[i]]+=1
        final = []
        for i in range(len(nums)):
            final.append(sum(counter[0:nums[i]]))
        return final