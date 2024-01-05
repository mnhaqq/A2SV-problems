from collections import Counter
from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dic = Counter(nums)
        heap = [(-freq, num) for num, freq in dic.items()]
        heapify(heap)

        ans = []
        i = 0
        while i < k:
            freq, val = heappop(heap)
            ans.append(val)
            i += 1
        return ans