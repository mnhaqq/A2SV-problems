class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                result.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()
                    
        result = []
        backtrack([])
        return result