class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        #top-down
        def dp(curr):
            if curr == target:
                return 1
            if curr > target:
                return 0
            
            if memo[curr] == -1:
                ans = 0
                for num in nums:
                    ans += dp(curr + num)
                memo[curr] = ans
            return memo[curr]
        memo = [-1] * (target + 1)
        return dp(0)

        #bottom up
        dp = [0] * (target + 1)
        dp[target] = 1
        for i in range(target, -1, -1):
            ans = 0
            for num in nums:
                if (i + num) < len(dp):
                    dp[i] += dp[i + num]
        return dp[0]
        