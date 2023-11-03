class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        minimum = max(prices)
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                profit = max(profit, prices[i]-minimum)
        return profit
        