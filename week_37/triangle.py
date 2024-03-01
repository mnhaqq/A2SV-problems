class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dp(r, c):
            if not 0 <= c <= r:
                return float('inf')
            if r >= len(triangle):
                return 0
            
            one = dp(r+1, c)
            two = dp(r+1, c+1)
            return min(one, two) + triangle[r][c]
        
        return dp(0, 0)
            
