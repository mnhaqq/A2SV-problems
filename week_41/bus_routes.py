class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(list)

        for i in range(len(routes)):
            for stop in routes[i]:
                graph[stop].append(i)

        queue = deque(graph[source])
        visited = set(graph[source])
        
        ans = 1
        while queue:
            level = len(queue)
            for _ in range(level):
                route = queue.popleft()
                for stop in routes[route]:
                    if stop == target:
                        return ans
                
                    for nei in graph[stop]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
            ans += 1
        return -1
