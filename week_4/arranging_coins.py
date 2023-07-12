class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=0
        if n==1 or n==2:
            return 1
        for i in range(n):
            count+=i
            if count==n:
                return i
            elif count > n:
                return i-1