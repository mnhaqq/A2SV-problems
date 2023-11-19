class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(curr):
            if len(curr) <= len(nums):
                result.append(curr.copy())

            if len(curr) == 0:
                for i in nums:
                    curr.add(i)
                    backtrack(curr)
                    curr.remove(i)
            else:
                for i in nums:
                    if i <= max(curr):
                        continue
                    curr.add(i)
                    backtrack(curr)
                    curr.remove(i)

        result = []
        backtrack(set())
        return result