from heapq import heapify, heappop

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        for i in range(len(score)):
            score[i] = (score[i], i)
        heapify(score)
        
        ans = [-1] * len(score)
        pos = len(score)
        while score:
            val, idx = heappop(score)
            if pos == 1:
                ans[idx] = "Gold Medal"
            elif pos == 2:
                ans[idx] = "Silver Medal"
            elif pos == 3:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(pos)
            pos -= 1
        return ans