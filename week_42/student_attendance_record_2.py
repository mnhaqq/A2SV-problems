class Solution:
    def __init__(self):
        self.memo = dict()

    def checkRecord(self, n: int) -> int:
        return self.dp(n, 0, 0, 0)

    
    def dp(self, n, i, num_a, num_l):
        if num_a >= 2:
            return 0
        if num_l >= 3:
            return 0
        if i == n:
            return 1
        if (i, num_a, num_l) in self.memo:
            return self.memo[(i, num_a, num_l)]
        
                
        P = self.dp(n, i+1, num_a, 0)
        L = self.dp(n, i+1, num_a, num_l+1)
        A = self.dp(n, i+1, num_a+1, 0)
        self.memo[(i, num_a, num_l)] = (P + L + A) % (10 ** 9 + 7)
        return self.memo[(i, num_a, num_l)]