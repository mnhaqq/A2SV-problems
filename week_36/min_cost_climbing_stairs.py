class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        def dp(idx):
            if idx == len(cost)-1 or idx == len(cost)-2:
                return cost[idx]

            if memo[idx] == -1:
                one = dp(idx+1)
                two = dp(idx+2)
                memo[idx] = min(one, two) + cost[idx]
            return memo[idx]
            
        memo = [-1] * len(cost)
        a = dp(0)
        b = dp(1)
        return min(a, b)