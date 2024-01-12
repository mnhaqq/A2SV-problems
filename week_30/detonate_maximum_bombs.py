from collections import defaultdict
from math import sqrt

class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                x = (bombs[i][0] - bombs[j][0]) ** 2
                y = (bombs[i][1] - bombs[j][1]) ** 2
                if sqrt(x + y) <= bombs[i][2]:
                    graph[i].append(j)
        

        def dfs(node):
            nonlocal check
            nonlocal ans
            check += 1
            ans = max(ans, check)
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        
        ans = 0
        for i in range(len(bombs)):
            visited = set()
            check = 0
            dfs(i)
        return ans       