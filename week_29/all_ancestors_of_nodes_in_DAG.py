from collections import defaultdict, deque

class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for a, b in edges:
            graph[a].append(b)
            indegree[b] += 1

        queue = deque([i for i in range(n) if i not in indegree])
        ancestors = [set() for i in range(n)]
        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                ancestors[nei].add(node)
                ancestors[nei].update(ancestors[node])
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
        ancestors = [sorted(list(i)) for i in ancestors]
        return ancestors