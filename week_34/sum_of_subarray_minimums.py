class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        prev_less = [-1] * n
        ans = [0] * n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                prev_less[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            ans[i] = ans[prev_less[i]] + (arr[i] * (i-prev_less[i]))
        return sum(ans) % (10**9 + 7)