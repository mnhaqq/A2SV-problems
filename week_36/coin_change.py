class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        def dp(idx, target):
            if target == 0:
                return 0
            if target < 0 or idx < 0:
                return float('inf')
            
            state = (idx, target)
            if state not in memo:
                one = dp(idx, target-coins[idx]) + 1
                two = dp(idx-1, target)
                memo[state] = min(one, two)
            return memo[state]

        memo = {}
        ans = dp(len(coins)-1, amount)
        if ans == float('inf'):
            return -1
        return ans
