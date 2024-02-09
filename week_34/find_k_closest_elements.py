from heapq import heapify, heappop

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        arr = [(abs(i-x), i) for i in arr]
        heapify(arr)
        ans = []
        while arr and len(ans) < k:
            ans.append(heappop(arr)[1])
        ans.sort()
        return ans