class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i, j):
            if i >= n:
                return m - j
            if j >= m:
                return n - i

            if word1[i] == word2[j]:
                return dp(i+1, j+1)

            return 1 + min(dp(i+1, j), dp(i, j+1), dp(i+1, j+1))
        
        n = len(word1)
        m = len(word2)
        return dp(0, 0)
