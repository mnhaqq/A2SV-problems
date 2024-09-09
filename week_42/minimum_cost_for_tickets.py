class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        back = [1,7,30]
        days = set(days)
        dp = [0] * (max(days) + 1)
        for i in range(1, len(dp)):
            two = three = float('inf')
            if i not in days:
                dp[i] = dp[i-1]
            else:
                for j in range(len(costs)):
                    dp[i] = min(dp[i],dp[i - back[j]] +costs[j])

        return dp[-1]
            
