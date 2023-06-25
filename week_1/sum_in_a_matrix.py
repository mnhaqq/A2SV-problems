class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        final = 0
        i = 0
        while i < len(nums[0]):
            ops = []
            for row in nums:
                ops.append(max(row))
                row.remove(max(row))
            final += max(ops)

        return final