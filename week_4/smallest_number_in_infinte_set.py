class SmallestInfiniteSet:

    def __init__(self):
        self.set = set([i for i in range(1,1001)])

    def popSmallest(self) -> int:
        tmp = sorted(self.set)
        self.set.remove(tmp[0])
        return tmp[0]
        

    def addBack(self, num: int) -> None:
        if num not in self.set:
            self.set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)