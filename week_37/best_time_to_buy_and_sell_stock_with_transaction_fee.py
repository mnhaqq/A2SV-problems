class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # @cache
        # def dp(idx, flag):
        #     if idx == len(prices):
        #         return 0
        #     if flag:
        #         return max(dp(idx+1, True), -prices[idx] + dp(idx+1, False))
        #     else:
        #         return max(prices[idx] + dp(idx+1, True) - fee, dp(idx+1, False))

        # return dp(0, True)

        dp = [[0] * 2 for _ in range(len(prices) + 1)]
        for i in range(len(dp)-2, -1, -1):
            dp[i][0] = max(prices[i] + dp[i+1][1] - fee, dp[i+1][0])
            dp[i][1] = max(dp[i+1][1], -prices[i] + dp[i+1][0])
        return dp[0][1]
