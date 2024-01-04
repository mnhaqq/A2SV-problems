class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        middle_val = float('-inf')
        stack = []

        for num in reversed(nums):
            if num < middle_val:
                print(num, stack[-1], middle_val)
                return True

            while stack and stack[-1] < num:
                middle_val = stack.pop()
            
            stack.append(num)
        return False