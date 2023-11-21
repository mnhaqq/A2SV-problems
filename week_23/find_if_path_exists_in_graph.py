from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        dic = defaultdict(list)

        for src, dest in edges:
            dic[src].append(dest)
            dic[dest].append(src)
        def dfs(vertex, visited):
            if vertex == destination:
                return True
            visited.add(vertex)
            check = False
            for neighbour in dic[vertex]:
                if neighbour not in visited:
                    check = check or dfs(neighbour, visited)
            return check
        visited = set()
        return dfs(source, visited)