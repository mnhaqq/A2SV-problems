class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        s = s[::-1]
        window = 0
        p = 1
        for i in range(k):
            window += (ord(s[i]) - ord('a') + 1) * pow(power, k-i-1, modulo)
            window %= modulo

        if window % modulo == hashValue:
            ans = s[i-k+1:i+1][::-1]

        p = pow(power, k-1, modulo)

        for i in range(k, len(s)):
            window -= ((ord(s[i-k]) - ord('a') + 1) * p)
            window *= power
            window += ((ord(s[i]) - ord('a') + 1))
            window %= modulo

            if window % modulo == hashValue:
                ans = s[i-k+1:i+1][::-1]

        return ans
