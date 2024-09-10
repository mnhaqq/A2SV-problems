from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        incoming = defaultdict(int)

        if n == 1:
            return [0]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            incoming[a] += 1
            incoming[b] += 1
        
        queue = deque([i for i in range(n) if incoming[i] == 1])

        while n > 2:
            n -= len(queue)
            level = len(queue)

            for _ in range(level):
                node = queue.popleft()

                for nei in graph[node]:
                    incoming[nei] -= 1
                    if incoming[nei] == 1:
                        queue.append(nei)

        return queue
