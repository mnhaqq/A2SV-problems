class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calcPow(base = x, exp=abs(n)):
            if exp == 0:
                return 1
            half = calcPow(base, exp//2)
            if exp % 2 == 0:
                return half * half
            return base * half * half
        ans = calcPow()
        if n < 0:
            return 1/ans
        return ans