class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        
        # @cache
        # def dp(l, r, flag):
        #     if l == r and flag:
        #         return nums[l]
        #     elif l == r:
        #         return -nums[l]
            
        #     if flag:
        #         one = nums[l] + dp(l+1, r, False)
        #         two = nums[r] + dp(l, r-1, False)
        #         return max(one, two)
        #     else:
        #         one = -nums[l] + dp(l+1, r, True)
        #         two = -nums[r] + dp(l, r-1, True)
        #         return min(one, two)
            
            
        # return dp(0, len(nums)-1, True) >= 0

        dp = [[[0]*2 for _ in range(len(nums))] for _ in range(len(nums))]

        for l in range(len(nums)-1, -1, -1):
            for r in range(l, len(nums)):
                if l == r:
                    dp[l][r][False] = -nums[l]
                    dp[l][r][True] = nums[l]
                    continue

                one = nums[l] + dp[l+1][r][False]
                two = nums[r] + dp[l][r-1][False]
                dp[l][r][True] = max(one, two)

                one = -nums[l] + dp[l+1][r][True]
                two = -nums[r] + dp[l][r-1][True]
                dp[l][r][False] = min(one, two)

        ans = dp[0][-1][True]
        return ans >= 0
            