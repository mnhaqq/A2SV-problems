class Solution:
    def tribonacci(self, n: int) -> int:
        def dp(num):
            if num <= 1:
                return num
            if num == 2:
                return 1
            
            if num not in memo:
                memo[num] = dp(num-1) + dp(num-2) + dp(num-3)
            return memo[num]

        memo = {}
        return dp(n)