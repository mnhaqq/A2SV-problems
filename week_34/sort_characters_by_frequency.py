from collections import Counter
from heapq import heapify, heappop

class Solution:
    def frequencySort(self, s: str) -> str:
        dic = Counter(s)
        heap = [(-dic[i], i) for i in dic.keys()]
        heapify(heap)
        
        ans = ""
        while heap:
            freq, char = heappop(heap)
            ans += char * (-freq)
        return ans