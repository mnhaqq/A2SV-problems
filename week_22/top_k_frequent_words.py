from collections import Counter
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        dic = Counter(words)
        heap = []
        for key, value in dic.items():
            heap.append((-value, key))
        heapify(heap)
         
        ans = []
        for i in range(k):
            ans.append(heappop(heap)[1])
        return ans