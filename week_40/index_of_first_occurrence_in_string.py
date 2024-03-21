class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        mod = 10 ** 9 + 7
        def hash(word):
            ans = 0
            n = len(word)
            a = 31 ** (n-1)
            for i in range(n):
                ans += (ord(word[i]) - ord('a') + 1) * (31 ** (n-1-i))
                ans %= mod

            return ans
        
        h_needle = hash(needle)
        window = hash(haystack[:len(needle)])
        n = len(needle)
        p = 31 ** n

        l = 0
        for r in range(n, len(haystack)):
            if h_needle == window:
                return l
            window *= 31 
            window = window % mod
            window -= (hash(haystack[l]) * p)
            window += (ord(haystack[r]) - ord('a') + 1)
            window = window % mod
            l += 1

        if h_needle == window:
            return l
        return -1
