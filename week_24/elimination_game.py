class Solution:
    def lastRemaining(self, n: int) -> int:
        def rec(a, n, d, left):
            if n == 1:
                return a
            if left:
                return rec(a+d, n//2, d*2, False)
            else:
                if n % 2 == 0:
                    return rec(a, n//2, d*2, True)
                else:
                    return rec(a+d, n//2, d*2, True)
        return rec(1, n, 1, True)