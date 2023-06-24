class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums = [str(num) for num in nums]
        
        tmp = []
        for num in nums:
            tmp.append(num[::-1])
        nums += tmp
        nums = [int(num) for num in nums]
        return(len(set(nums)))