class Solution:
    def findComplement(self, num: int) -> int:
        k = num.bit_length()
        return num ^ ((1 << k) - 1)