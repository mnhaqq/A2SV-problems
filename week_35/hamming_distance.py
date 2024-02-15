class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        k = max(x, y).bit_length()
        count = 0

        for i in range(k+1):
            if (x & (1 << i) != 0) != (y & (1 << i) != 0):
                count += 1
        return count