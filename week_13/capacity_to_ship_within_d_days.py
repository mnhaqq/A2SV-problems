class Solution:
    def checkPossible(self, capacity, weights, days):
        shipped, days_used = 0, 1
        for weight in weights:
            shipped += weight
            if shipped > capacity:
                shipped = weight
                days_used += 1
                if days_used > days or shipped > capacity:
                    return False
        return True

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = 1, max(weights)*len(weights)
        while low <= high:
            mid = (low + high) // 2
            if self.checkPossible(mid, weights, days):
                least_capacity = mid
                high = mid - 1
            else:
                low = mid + 1
        return least_capacity