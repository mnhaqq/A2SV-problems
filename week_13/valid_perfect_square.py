class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num ** (1/2) % 1 == 0:
            return True
        return False