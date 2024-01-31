from heapq import heapify, heappush, heappop

class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        piles = [-num for num in piles]
        heapify(piles)

        for _ in range(k):
            maxx = -heappop(piles)
            maxx -= maxx // 2
            heappush(piles, -maxx)
        piles = [-num for num in piles]
        return sum(piles)