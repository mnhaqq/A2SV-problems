import random

class Solution:

    def __init__(self, w: list[int]):
        self.p_s = [0] * (len(w) + 1)
        for i in range(1, len(w)+1):
            self.p_s[i] = self.p_s[i-1] + w[i-1]
        self.p_s.pop(0)

    def pickIndex(self) -> int:
        num  = random.randint(1, self.p_s[-1])
        l, h = 0, len(self.p_s)
        while l < h:
            m = (l + h) // 2
            if num > self.p_s[m]:
                l = m + 1
            else:
                h = m 
        return l

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()