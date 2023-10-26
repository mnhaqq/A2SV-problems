dic = dict()
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        if n-1 not in dic:
            dic[n-1] = self.climbStairs(n-1)
        if n-2 not in dic:
            dic[n-2] = self.climbStairs(n-2)
        return dic[n-1] + dic[n-2] 