class Solution:
    def checkPossible(self, piles, h, k):
        i = count = 0
        while i < len(piles):
            count += ceil(piles[i]/k)
            i+=1
        if count <= h:
            return True
        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low <= high:
            mid = (low+high) // 2
            if self.checkPossible(piles, h, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans