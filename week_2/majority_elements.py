class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = dict()
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        
        max_count = 0
        for key, value in dic.items():
            if value > max_count:
                majority_element = key
                max_count = value
        
        return majority_element