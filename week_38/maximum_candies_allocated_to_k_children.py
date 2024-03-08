class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        def feasible(size):
            check = 0
            for i in range(len(candies)):
                check += (candies[i] // size)
            return check >= k

        ans = 0
        l, h = 1, max(candies)
        while l <= h:
            mid = (l + h) // 2
            if feasible(mid):
                ans = mid
                l = mid + 1
            else:
                h = mid - 1
        return ans
