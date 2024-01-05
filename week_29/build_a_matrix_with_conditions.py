from collections import defaultdict, deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:

        def top_sort(conditions):
            graph = defaultdict(set)
            indegree = defaultdict(int)

            for a, b in conditions:
                if b not in graph[a]:
                    indegree[b] += 1
                graph[a].add(b)

            queue = deque([i for i in range(1, k+1) if indegree[i] == 0])
            pos = [-1] * (k+1)
            i = 0

            while queue:
                node = queue.popleft()
                pos[node] = i
                i += 1

                for nei in graph[node]:
                    indegree[nei] -= 1

                    if indegree[nei] == 0:
                        queue.append(nei)
            return pos
        

        row = top_sort(rowConditions)
        col = top_sort(colConditions)
        mat = [[0] * k for _ in range(k)]

        for i in range(1, k+1):
            if row[i] == -1 or col[i] == -1:
                return []
            mat[row[i]][col[i]] = i
        return mat