from math import ceil

class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        speed = -1
        low, high = 1, 10**7
        
        while low <= high:
            mid = (low + high) // 2
            tmp = 0
            for i in range(len(dist)-1):
                tmp += ceil(dist[i] / mid)
            
            tmp += dist[-1] / mid
            
            if tmp <= hour:
                speed = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return speed