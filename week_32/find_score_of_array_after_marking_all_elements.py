from heapq import heapify, heappop

class Solution:
    def findScore(self, nums: list[int]) -> int:
        nums = [(nums[i], i) for i in range(len(nums))]
        num_elements = len(nums)
        marked = set()
        heapify(nums)
        
        score = 0
        while len(marked) < num_elements:
            curr = heappop(nums)
            if curr[1] in marked:
                continue
            score += curr[0]

            marked.add(curr[1])
            if 0 <= (curr[1] - 1) < num_elements:
                marked.add(curr[1]-1)
            if 0 <= (curr[1] + 1) < num_elements:
                marked.add(curr[1] + 1)

        return score