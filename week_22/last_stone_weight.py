from heapq import heapify, heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)
        while len(stones) > 1:
            a = heappop(stones) * -1
            b = heappop(stones) * -1
            if a == b:
                continue
            else:
                heappush(stones, (a-b) * -1)
        if stones:
            return abs(stones[0])
        return 0