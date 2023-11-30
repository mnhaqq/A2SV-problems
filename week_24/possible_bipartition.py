from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        adj_list = defaultdict(list)
        for a, b in dislikes:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def dfs(node):
            tmp = True
            for neighbour in adj_list[node]:
                if colors[neighbour-1] == -1:
                    if colors[node-1] == 0:
                        colors[neighbour-1] = 1
                    else:
                        colors[neighbour-1] = 0
                    tmp = tmp and dfs(neighbour)          
                else:
                    tmp = tmp and colors[node-1] != colors[neighbour-1]
            return tmp

        colors = [-1] * n
        result = True
        for node in adj_list.keys():
            if colors[node-1] == -1:
                colors[node-1] = 0
                result = result and dfs(node)
        return result