class Solution:
    def longestPrefix(self, s: str) -> str:
        mod = 10 ** 9 + 7
        
        l, r = 0, len(s) - 1
        p = 1
        hash_l = hash_r = 0
        idx = -1

        for l in range(len(s)-1):
            hash_l *= 31
            hash_l += ord(s[l]) - ord('a') + 1
            hash_l = hash_l % mod

            hash_r += ((ord(s[r]) - ord('a') + 1) * p)
            hash_r = hash_r % mod

            p *= 31
            p %= mod

            if hash_l == hash_r:
                idx = l
            r -= 1

        if idx == -1:
            return ""
        return s[:idx+1]
