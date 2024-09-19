from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        for a, b in relations:
            graph[a].append(b)
            incoming[b] += 1

        queue = deque([i for i in range(1, n+1) if incoming[i] == 0])

        dist = [0] + time

        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                dist[nei] = max(dist[nei], dist[node] + time[nei-1])
                incoming[nei] -= 1
                if incoming[nei] == 0:
                    queue.append(nei)
            
        return max(dist)