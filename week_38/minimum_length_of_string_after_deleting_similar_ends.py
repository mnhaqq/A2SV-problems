class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 1:
            return 1

        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            while l <= r and s[l] == s[r]:
                l += 1
            while l <= r and s[r] == s[l-1]:
                r -= 1

        return r-l+1 
