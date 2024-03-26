class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        diff = (len(b) // len(a)) + 2

        s = b + '#' + (a * diff)
        n = len(s)

        lps = [0] * n
        for i in range(1, n):
            j = lps[i-1]

            while j > 0 and s[i] != s[j]:
                j = lps[j-1]
            
            if s[i] == s[j]:
                j += 1
            
            if j == len(b):
                return (i - len(b) - 1) // len(a) + 1
            lps[i] = j
        return -1
            
