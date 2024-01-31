from heapq import heappop, heappush

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a, -b, -c]
        score = 0

        while len(heap) > 1:
            num1 = (-heappop(heap)) - 1
            num2 = (-heappop(heap)) - 1
            
            if num1 > 0:
                heappush(heap, -num1)
            if num2 > 0:
                heappush(heap, -num2)

            score += 1
        return score
