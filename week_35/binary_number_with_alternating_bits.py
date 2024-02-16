class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = -1
        k = n.bit_length() - 1

        while k >= 0:
            test = 0
            if n & (1 << k) > 0:
                test = 1

            if test == prev:
                return False
            prev = test
            k -= 1 
        return True