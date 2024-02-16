class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        maxx = 0
        for num in nums:
            maxx = maxx | num
        
        count = 0
        def backtrack(idx, curr):
            nonlocal maxx, count
            if curr == maxx:
                count += 1
            
            for i in range(idx, len(nums)):
                backtrack(i+1, curr | nums[i])
                
        backtrack(0, 0)
        return count