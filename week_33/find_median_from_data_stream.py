from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        #minheap stores larger numbers in stream
        self.minheap = []
        #maxheap stores smaller numbers in stream
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxheap, -num)
        heappush(self.minheap, (heappop(self.maxheap) * -1))

        if len(self.maxheap) < len(self.minheap):
            heappush(self.maxheap, (heappop(self.minheap) * -1))

    def findMedian(self) -> float:
        if ((len(self.maxheap) + len(self.minheap)) % 2) != 0:
            return -self.maxheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()