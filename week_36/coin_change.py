class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # def dp(idx, target):
        #     if target == 0:
        #         return 0
        #     if target < 0 or idx < 0:
        #         return float('inf')
            
        #     state = (idx, target)
        #     if state not in memo:
        #         one = dp(idx, target-coins[idx]) + 1
        #         two = dp(idx-1, target)
        #         memo[state] = min(one, two)
        #     return memo[state]

        # memo = {}
        # ans = dp(len(coins)-1, amount)
        # if ans == float('inf'):
        #     return -1
        # return ans

        dp = [[float('inf')] * (amount + 1) for _ in range(len(coins) + 1)]

        for i in range(len(coins) + 1):
            dp[i][0] = 0

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    dp[i][j] = min(dp[i][j - coins[i - 1]] + 1, dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        if dp[len(coins)][amount] == float('inf'):
            return -1
        return dp[len(coins)][amount]

            