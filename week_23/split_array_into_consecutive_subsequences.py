from heapq import heappop, heappush

class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        heap = []
        for i in range(len(nums)):
            while heap and heap[0][0] < nums[i] - 1:
                if heap[0][1] < 3:
                    return False
                heappop(heap)
            if heap and heap[0][0] == nums[i] - 1:
                tmp = heappop(heap)
                tmp[0] = nums[i]
                tmp[1] += 1
                heappush(heap, tmp)
            else:
                heappush(heap, [nums[i], 1])

        for element in heap:
            if element[1] < 3:
                return False
        return True