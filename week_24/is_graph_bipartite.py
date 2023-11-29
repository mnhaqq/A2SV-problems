from collections import defaultdict

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        adj_list = defaultdict(list)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                adj_list[i].append(graph[i][j])
                
        colors = [-1] * len(graph)

        def dfs(node, prev):
            if colors[node] != -1:
                return

            colors[node] = prev
            if prev < 1:
                prev = 1
            else:
                prev = 0
            
            for neighbour in adj_list[node]:
                dfs(neighbour, prev)
        
        for i in range(len(colors)):
            if colors[i] == -1:
                dfs(i, 0)
        for key, arr in adj_list.items():
            for neighbour in arr:
                if colors[key] == colors[neighbour]:
                    return False
        return True