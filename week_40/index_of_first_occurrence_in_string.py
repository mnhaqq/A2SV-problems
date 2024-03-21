class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def hash(word):
            ans = 0
            n = len(word)
            for i in range(n):
                ans += (ord(word[i]) - ord('a') + 1) * (31 ** (n-i-1))
            return ans
        
        h_needle = hash(needle)
        window = hash(haystack[:len(needle)])
        n = len(needle)

        l = 0
        for r in range(n, len(haystack)):
            if h_needle == window:
                return l % (10 ** 9 + 7)
            window *= 31
            window -= (hash(haystack[l]) * (31 ** n))
            window += ord(haystack[r]) - ord('a') + 1
            l += 1
        if h_needle == window:
            return l % (10 ** 9 + 7)
        return -1
