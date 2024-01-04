from collections import deque

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = deque()

        ans = [-1] * len(nums)
        for i in range(len(nums) * 2):
            while stack and nums[stack[-1]] < nums[i % len(nums)]:
                ans[stack[-1]] = nums[i % len(nums)]
                stack.pop()
            stack.append(i % len(nums))
        return ans