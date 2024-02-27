class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def inbound(i):
            return 0 <= i < len(matrix)

        @cache
        def dp(r, c):
            if not inbound(c):
                return float('inf')
            if not inbound(r):
                return 0
            
            one = dp(r+1, c-1)
            two = dp(r+1, c)
            three = dp(r+1, c+1)

            return min(one, two, three) + matrix[r][c]

        ans = float('inf')
        for i in range(len(matrix)):
            ans = min(ans, dp(0, i))
        return ans
