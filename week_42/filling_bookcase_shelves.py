from functools import lru_cache

class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        @lru_cache
        def dp(i, height, c):
            if i >= len(books):
                return height
            
            one = dp(i+1, books[i][1], books[i][0]) + height
            
            if books[i][0] + c <= shelfWidth:
                return min(one, dp(i+1, max(height, books[i][1]), books[i][0]+c))
            
            return one
        
        return dp(0, 0, 0)

        @lru_cache
        def dp(idx):
            if idx == len(books):
                return 0
            rw = rh = 0
            ans = float('inf')
            for i in range(idx, len(books)):
                w, h = books[i]
                if w + rw <= shelfWidth:
                    rh = max(rh, h)
                    ans = min(ans, rh + dp(i+1))
                rw += w
            return ans
        
        return dp(0)