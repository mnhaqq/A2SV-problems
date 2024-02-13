class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        diff = []
        for i in range(len(costs)):
            diff.append((costs[i][0]-costs[i][1], i))
        diff.sort()

        ans = 0
        n = len(costs)//2
        for i in range(len(diff)):
            idx = diff[i][1]
            if i < n:
                ans += costs[idx][0]
            else:
                ans += costs[idx][1]
        return ans